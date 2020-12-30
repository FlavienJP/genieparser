"""
Module:
    genie.libs.parser.ironware.show_interface

Author:
    James Di Trapani <james@ditrapani.com.au> - https://github.com/jamesditrapani

Description:
    Interface parsers for IronWare devices

Parsers:
    * show interfaces brief
    * show ip interfaces
"""

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
import re

__author__ = 'James Di Trapani <james@ditrapani.com.au>'


# ======================================================
# Schema for 'show interfaces brief wide'
# ======================================================
class ShowInterfacesBriefSchema(MetaParser):
    """Schema for show interfaces brief wide"""
    schema = {
        'interfaces': {
            Any(): {
                'link': str,
                'state': str,
                'speed': str,
                'tag': str,
                'mac': str,
                'description': Or(str, None)
            }
        }
    }


# ====================================================
#  parser for 'show interfaces brief wide'
# ====================================================
class ShowInterfacesBrief(ShowInterfacesBriefSchema):
    """
    Parser for Show Interfaces Brief on Ironware devices
    """
    cli_command = 'show interfaces brief'

    """
    Port   Link     Port-State   Speed Tag MAC            Name
    1/1    Disabled None         None  No  cc4e.2442.1000 description1
    1/2    Up       Forward      1G    No  cc4e.2442.2000 description2
    1/3    Up       Forward      1G    Yes cc4e.2442.3000 description3
    mgmt1  Up       Forward      100M  Yes cc4e.2442.4000
    lb1    Up       N/A          N/A   N/A N/A
    tn30   Down     N/A          N/A   N/A N/A
    """

    def cli(self, output=None):
        if output is None:
            # Append 'wide' to the command due to
            # no 'terminal width 0' on brocade devices
            out = self.device.execute(self.cli_command + ' wide')
        else:
            out = output

        result_dict = {}

        interface_def = {
            'mgmt': 'management',
            'lb': 'loopback',
            'tn': 'tunnel',
            've': 've'
        }

        p0 = re.compile(r'((?P<interface>^\d+\/\d+|mgmt\d+|lb\d+|tn\d+|ve\d+)'
                        r'\s+(?P<link>Up|Down|Disabled)\s+'
                        r'(?P<state>None|Forward|N\/A)\s+'
                        r'(?P<speed>\d+\w|None|N\/A)\s+'
                        r'(?P<tag>No|Yes|N\/A)\s+'
                        r'(?P<mac>\w+.\w+.\w+|N\/A)'
                        r'(\s+(?P<desc>[^$]+)|$))')

        p1 = re.compile(r'((?P<int>^[^\d]+)(?P<num>\d+$))')

        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                if 'interfaces' not in result_dict:
                    interface_dict = result_dict.setdefault('interfaces', {})

                # Work out interface type
                interface = m.groupdict()['interface']
                is_eth = re.match(r'\d+\/\d+', interface)

                if is_eth:
                    int_type = 'ethernet'
                else:
                    n = p1.match(interface)
                    if n:
                        int_type = interface_def.get(n.groupdict()['int'])
                        interface = n.groupdict()['num']

                interface = int_type + interface
                interface_dict[interface] = {
                    'link': m.groupdict()['link'],
                    'state': m.groupdict()['state'],
                    'speed': m.groupdict()['speed'],
                    'tag': m.groupdict()['tag'],
                    'mac': m.groupdict()['mac'],
                    'description': m.groupdict()['desc']
                }

        return result_dict


# ======================================================
# Schema for 'show ip interface {interface}'
# ======================================================
class ShowIPInterfaceSchema(MetaParser):
    """Schema for show ip interface"""
    schema = {
        'interfaces': {
            Any(): {
                'ip': str,
                'ok': str,
                'method': str,
                'status': str,
                'protocol': str,
                'vrf': str,
                Optional('flag'): str
            }
        }
    }


# ====================================================
#  parser for 'show ip interface'
# ====================================================
class ShowIPInterface(ShowIPInterfaceSchema):
    """
    Parser for Show Interfaces {interface} on Ironware devices
    """
    cli_command = 'show ip interface'

    """
Interface    IP-Address     OK?  Method Status     Protocol VRF         FLAG
eth 1/1      10.254.32.221  YES  NVRAM  admin/down down     default-vrf
eth 5/1      10.254.32.3    YES  NVRAM  up         up       default-vrf
eth 7/1      10.254.32.109  YES  manual up         up       default-vrf
ve 150       10.15.15.2     YES  NVRAM  up         up       default-vrf VS
mgmt 1       172.16.15.4   YES  NVRAM  up         up       oob
loopback 1   9.9.9.9  YES  NVRAM  up         up       default-vrf
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}

        p0 = re.compile(r'((?P<int_name>^eth|mgmt|loopback|ve|tn|tunnel)\s+'
                        r'(?P<int_num>\d+/\d+|\d+)\s+'
                        r'(?P<ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+'
                        r'(?P<ok>\w+)\s+'
                        r'(?P<method>\w+)\s+'
                        r'(?P<status>up|down|admin\/down)\s+'
                        r'(?P<protocol>up|down)\s+'
                        r'(?P<vrf>[\S]+)($|\s+'
                        r'(?P<flag>US|VE|VS|V|U|S)))')

        interface_def = {
            'mgmt': 'management',
            'eth': 'ethernet',
            'lb': 'loopback',
            'loopback': 'loopback',
            'tn': 'tunnel',
            'tunnel': 'tunnel',
            've': 've'
        }

        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                if 'interfaces' not in result_dict:
                    interface_dict = result_dict.setdefault('interfaces', {})

                expand = interface_def.get(m.groupdict()['int_name'])
                interface = expand + m.groupdict()['int_num']

                interface_dict[interface] = {
                    'ip': m.groupdict()['ip'],
                    'ok': m.groupdict()['ok'],
                    'method': m.groupdict()['method'],
                    'status': m.groupdict()['status'],
                    'protocol': m.groupdict()['protocol'],
                    'vrf': m.groupdict()['vrf'],
                }

                if m.groupdict().get('flag') is not None:
                    interface_dict[interface]['flag'] = \
                                        m.groupdict().get('flag')

        return result_dict
