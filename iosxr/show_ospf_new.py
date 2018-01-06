''' show_ospf.py

IOSXR parsers for the following show commands:

    * show ospf vrf all-inclusive interface
    * show ospf vrf all-inclusive neighbor detail
    * show ospf vrf all-inclusive
    * show ospf vrf all-inclusive sham-links
    * show ospf vrf all-inclusive virtual-links

    * show ospf mpls traffic-eng link
    * show ospf vrf all-inclusive database router
    * show ospf vrf all-inclusive database network
    * show ospf vrf all-inclusive database summary
    * show ospf vrf all-inclusive database external
    * show ospf vrf all-inclusive database opaque-area
    * show ospf vrf all-inclusive database opaque-as
    * show ospf vrf all-inclusive database opaque-linkl
'''

# Python
import re
import xmltodict
from netaddr import IPAddress

# Metaparser
from metaparser import MetaParser
from metaparser.util.schemaengine import Schema, Any, Or, Optional
from parser.utils.common import Common


# ==================================================
# Schema for 'show ospf vrf all-inclusive interface'
# ==================================================
class ShowOspfVrfAllInclusiveInterfaceSchema(MetaParser):

    ''' Schema for "show ospf vrf all-inclusive interface" '''

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {'instance': 
                            {Any(): 
                                {'areas': 
                                    {Any(): 
                                        {Optional('interfaces'): 
                                            {Any(): 
                                                {'name': str,
                                                'enable': bool,
                                                'line_protocol': bool,
                                                'ip_address': str,
                                                'demand_circuit': bool,
                                                'process_id': str,
                                                'router_id': str,
                                                'interface_type': str,
                                                'bfd': 
                                                    {'enable': bool,
                                                    Optional('interval'): int,
                                                    Optional('min_interval'): int,
                                                    Optional('multiplier'): int,
                                                    Optional('mode'): str,
                                                    },
                                                Optional('cost'): int,
                                                Optional('transmit_delay'): int,
                                                Optional('state'): str,
                                                Optional('priority'): int,
                                                Optional('mtu'): int,
                                                Optional('max_pkt_sz'): int,
                                                Optional('dr_router_id'): str,
                                                Optional('dr_ip_addr'): str,
                                                Optional('bdr_router_id'): str,
                                                Optional('bdr_ip_addr'): str,
                                                Optional('hello_interval'): int,
                                                Optional('dead_interval'): int,
                                                Optional('wait_interval'): int,
                                                Optional('retransmit_interval'): int,
                                                Optional('passive'): bool,
                                                Optional('hello_due_in'): str,
                                                Optional('index'): str,
                                                Optional('flood_queue_length'): int,
                                                Optional('next'): str,
                                                Optional('last_flood_scan_length'): int,
                                                Optional('max_flood_scan_length'): int,
                                                Optional('last_flood_scan_time_msec'): int,
                                                Optional('max_flood_scan_time_msec'): int,
                                                Optional('ls_ack_list'): str,
                                                Optional('ls_ack_list_length'): int,
                                                Optional('high_water_mark'): int,
                                                Optional('nbr_count'): int,
                                                Optional('adj_nbr_count'): int,
                                                Optional('adj_nbr'): str,
                                                Optional('num_nbrs_suppress_hello'): int,
                                                Optional('multi_area_intf_count'): int,
                                                },
                                            },
                                        Optional('virtual_links'):
                                            {Any(): 
                                                {'name': str,
                                                'enable': bool,
                                                'line_protocol': bool,
                                                'ip_address': str,
                                                'demand_circuit': bool,
                                                'process_id': str,
                                                'router_id': str,
                                                'interface_type': str,
                                                'bfd': 
                                                    {'enable': bool,
                                                    Optional('interval'): int,
                                                    Optional('min_interval'): int,
                                                    Optional('multiplier'): int,
                                                    Optional('mode'): str,
                                                    },
                                                Optional('cost'): int,
                                                Optional('transmit_delay'): int,
                                                Optional('state'): str,
                                                Optional('priority'): int,
                                                Optional('mtu'): int,
                                                Optional('max_pkt_sz'): int,
                                                Optional('dr_router_id'): str,
                                                Optional('dr_ip_addr'): str,
                                                Optional('bdr_router_id'): str,
                                                Optional('bdr_ip_addr'): str,
                                                Optional('hello_interval'): int,
                                                Optional('dead_interval'): int,
                                                Optional('wait_interval'): int,
                                                Optional('retransmit_interval'): int,
                                                Optional('passive'): bool,
                                                Optional('hello_due_in'): str,
                                                Optional('index'): str,
                                                Optional('flood_queue_length'): int,
                                                Optional('next'): str,
                                                Optional('last_flood_scan_length'): int,
                                                Optional('max_flood_scan_length'): int,
                                                Optional('last_flood_scan_time_msec'): int,
                                                Optional('max_flood_scan_time_msec'): int,
                                                Optional('ls_ack_list'): str,
                                                Optional('ls_ack_list_length'): int,
                                                Optional('high_water_mark'): int,
                                                Optional('nbr_count'): int,
                                                Optional('adj_nbr_count'): int,
                                                Optional('adj_nbr'): str,
                                                Optional('num_nbrs_suppress_hello'): int,
                                                Optional('multi_area_intf_count'): int,
                                                },
                                            },
                                        Optional('sham_links'):
                                            {Any(): 
                                                {'name': str,
                                                'enable': bool,
                                                'line_protocol': bool,
                                                'ip_address': str,
                                                'demand_circuit': bool,
                                                'process_id': str,
                                                'router_id': str,
                                                'interface_type': str,
                                                'bfd': 
                                                    {'enable': bool,
                                                    Optional('interval'): int,
                                                    Optional('min_interval'): int,
                                                    Optional('multiplier'): int,
                                                    Optional('mode'): str,
                                                    },
                                                Optional('cost'): int,
                                                Optional('transmit_delay'): int,
                                                Optional('state'): str,
                                                Optional('priority'): int,
                                                Optional('mtu'): int,
                                                Optional('max_pkt_sz'): int,
                                                Optional('dr_router_id'): str,
                                                Optional('dr_ip_addr'): str,
                                                Optional('bdr_router_id'): str,
                                                Optional('bdr_ip_addr'): str,
                                                Optional('hello_interval'): int,
                                                Optional('dead_interval'): int,
                                                Optional('wait_interval'): int,
                                                Optional('retransmit_interval'): int,
                                                Optional('passive'): bool,
                                                Optional('hello_due_in'): str,
                                                Optional('index'): str,
                                                Optional('flood_queue_length'): int,
                                                Optional('next'): str,
                                                Optional('last_flood_scan_length'): int,
                                                Optional('max_flood_scan_length'): int,
                                                Optional('last_flood_scan_time_msec'): int,
                                                Optional('max_flood_scan_time_msec'): int,
                                                Optional('ls_ack_list'): str,
                                                Optional('ls_ack_list_length'): int,
                                                Optional('high_water_mark'): int,
                                                Optional('nbr_count'): int,
                                                Optional('adj_nbr_count'): int,
                                                Optional('adj_nbr'): str,
                                                Optional('num_nbrs_suppress_hello'): int,
                                                Optional('multi_area_intf_count'): int,
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }


# ==================================================
# Parser for 'show ospf vrf all-inclusive interface'
# ==================================================
class ShowOspfVrfAllInclusiveInterface(ShowOspfVrfAllInclusiveInterfaceSchema):

    ''' Parser for "show ospf vrf all-inclusive interface" '''

    def cli(self):

        # Execute command on device
        out = self.device.execute('show ospf vrf all-inclusive interface')

        # Init vars
        ret_dict = {}
        af = 'ipv4' # this is ospf - always ipv4

        # Mapping dict
        bool_dict = {'up': True, 'down': False, 'unknown': False}

        for line in out.splitlines():
            line = line.strip()

            # Interfaces for OSPF 1, VRF VRF1
            p1 = re.compile(r'^Interfaces +for +OSPF +(?P<instance>(\S+))'
                             '(?:, +VRF +(?P<vrf>(\S+)))?$')
            m = p1.match(line)
            if m:
                instance = str(m.groupdict()['instance'])
                if m.groupdict()['vrf']:
                    vrf = str(m.groupdict()['vrf'])
                else:
                    vrf = 'default'
                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}
                if 'address_family' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['address_family'] = {}
                if af not in ret_dict['vrf'][vrf]['address_family']:
                    ret_dict['vrf'][vrf]['address_family'][af] = {}
                if 'instance' not in ret_dict['vrf'][vrf]['address_family'][af]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance'] = {}
                if instance not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance] = {}
                    continue

            # GigabitEthernet0/0/0/2 is up, line protocol is up
            # OSPF_SL0 is unknown, line protocol is up
            # OSPF_VL0 is unknown, line protocol is up
            p2 = re.compile(r'^(?P<interface>(\S+)) +is'
                             ' +(?P<enable>(unknown|up|down)), +line +protocol'
                             ' +is +(?P<line_protocol>(up|down))$')
            m = p2.match(line)
            if m:
                interface = str(m.groupdict()['interface'])
                enable = str(m.groupdict()['enable'])
                line_protocol = str(m.groupdict()['line_protocol'])

                # Determine if 'interface' or 'sham_link' or 'virtual_link'
                if re.search('SL', interface):
                    pattern = '(?P<ignore>\S+)_SL(?P<num>(\d+))'
                    n = re.match(pattern, interface)
                    # Set values for dict
                    intf_type = 'sham_links'
                    name = 'SL' + str(n.groupdict()['num'])
                elif re.search('VL', interface):
                    pattern = '(?P<ignore>\S+)_VL(?P<num>(\d+))'
                    n = re.match(pattern, interface)
                    # Set values for dict
                    intf_type = 'virtual_links'
                    name = 'VL' + str(n.groupdict()['num'])
                else:
                    # Set values for dict
                    intf_type = 'interfaces'
                    name = interface
                    continue

            # Internet Address 10.2.3.3/24, Area 0
            p3 = re.compile(r'^Internet +Address +(?P<address>(\S+)),'
                             ' +Area +(?P<area>(\S+))$')
            m = p3.match(line)
            if m:
                ip_address = str(m.groupdict()['address'])
                area = str(IPAddress(str(m.groupdict()['area'])))
                if 'areas' not in ret_dict['vrf'][vrf]['address_family']\
                        [af]['instance'][instance]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'] = {}
                if area not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area] = {}
                    continue

            # Process ID 1, Router ID 3.3.3.3, Network Type POINT_TO_POINT
            # Process ID 1, Router ID 3.3.3.3, Network Type BROADCAST, Cost: 1
            # Process ID 1, VRF VRF1, Router ID 3.3.3.3, Network Type SHAM_LINK, Cost: 111
            p4 = re.compile(r'^Process +ID +(?P<pid>(\S+))'
                             '(?:, +VRF +(?P<vrf>(\S+)))?'
                             ', +Router +ID +(?P<router_id>(\S+))'
                             ', +Network +Type +(?P<interface_type>(\S+))'
                             '(?:, +Cost: +(?P<cost>(\d+)))?$')
            m = p4.match(line)
            if m:
                pid = str(m.groupdict()['pid'])
                router_id = str(m.groupdict()['router_id'])
                interface_type = str(m.groupdict()['interface_type']).lower()
                interface_type = interface_type.replace("_", "-")

                # Get interface values
                if intf_type == 'interfaces':
                    intf_name = interface
                elif intf_type == 'virtual_links':
                    intf_name = area + ' ' + router_id
                elif intf_type == 'sham_links':
                    intf_name = pid + ' ' + router_id

                # Build dictionary
                if intf_type not in ret_dict['vrf'][vrf]['address_family']\
                        [af]['instance'][instance]['areas'][area]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area][intf_type] = {}
                if intf_name not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area][intf_type]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area][intf_type][intf_name] = {}
                # Set sub_dict
                sub_dict = ret_dict['vrf'][vrf]['address_family'][af]\
                            ['instance'][instance]['areas'][area]\
                            [intf_type][intf_name]
                # Set keys
                sub_dict['demand_circuit'] = False
                if 'bfd' not in sub_dict:
                    sub_dict['bfd'] = {}
                sub_dict['bfd']['enable'] = False
                try:
                    sub_dict['name'] = name
                    sub_dict['ip_address'] = ip_address
                    sub_dict['enable'] = bool_dict[enable]
                    sub_dict['line_protocol'] = bool_dict[line_protocol]
                except:
                    pass

                sub_dict['process_id'] = pid
                sub_dict['router_id'] = router_id
                sub_dict['interface_type'] = interface_type
                if m.groupdict()['cost']:
                    sub_dict['cost'] = int(m.groupdict()['cost'])
                continue

            # Transmit Delay is 1 sec, State DR, Priority 1, MTU 1500, MaxPktSz 1500
            p5 = re.compile(r'^Transmit +Delay is +(?P<delay>(\d+)) +sec,'
                             ' +State +(?P<state>(\S+)),'
                             '(?: +Priority +(?P<priority>(\d+)),)?'
                             ' +MTU +(?P<mtu>(\d+)),'
                             ' +MaxPktSz +(?P<max_pkt_sz>(\d+))$')
            m = p5.match(line)
            if m:
                sub_dict['transmit_delay'] = int(m.groupdict()['delay'])
                state = str(m.groupdict()['state']).lower()
                state = state.replace("_", "-")
                sub_dict['state'] = state
                sub_dict['mtu'] = int(m.groupdict()['mtu'])
                sub_dict['max_pkt_sz'] = int(m.groupdict()['max_pkt_sz'])
                if m.groupdict()['priority']:
                    sub_dict['priority'] = int(m.groupdict()['priority'])
                continue

            # Designated Router (ID) 3.3.3.3, Interface address 10.2.3.3
            p6 = re.compile(r'^Designated +Router +\(ID\)'
                             ' +(?P<dr_router_id>(\S+)), +Interface +address'
                             ' +(?P<dr_ip_addr>(\S+))$')
            m = p6.match(line)
            if m:
                sub_dict['dr_router_id'] = str(m.groupdict()['dr_router_id'])
                sub_dict['dr_ip_addr'] = str(m.groupdict()['dr_ip_addr'])
                continue

            # Backup Designated router (ID) 2.2.2.2, Interface address 10.2.3.2
            p7 = re.compile(r'^Backup +Designated +Router +\(ID\)'
                             ' +(?P<bdr_router_id>(\S+)), +Interface +address'
                             ' +(?P<bdr_ip_addr>(\S+))$')
            m = p7.match(line)
            if m:
                sub_dict['bdr_router_id'] = str(m.groupdict()['bdr_router_id'])
                sub_dict['bdr_ip_addr'] = str(m.groupdict()['bdr_ip_addr'])
                continue

            # Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
            p8 = re.compile(r'^Timer +intervals +configured,'
                             ' +Hello +(?P<hello>(\d+)),'
                             ' +Dead +(?P<dead>(\d+)),'
                             ' +Wait +(?P<wait>(\d+)),'
                             ' +Retransmit +(?P<retransmit>(\d+))$')
            m = p8.match(line)
            if m:
                sub_dict['hello_interval'] = int(m.groupdict()['hello'])
                sub_dict['dead_interval'] = int(m.groupdict()['dead'])
                sub_dict['wait_interval'] = int(m.groupdict()['wait'])
                sub_dict['retransmit_interval'] = int(m.groupdict()['retransmit'])
                continue

            # Hello due in 00:00:07:587
            p9_1 = re.compile(r'^Hello +due +in +(?P<hello_due>(\S+))$')
            m = p9_1.match(line)
            if m:
                sub_dict['passive'] = False
                sub_dict['hello_due_in'] = str(m.groupdict()['hello_due'])
                continue

            # No Hellos (Passive interface)
            p9_2 = re.compile(r'^No +Hellos +\(Passive +interface\)$')
            m = p9_2.match(line)
            if m:
                sub_dict['passive'] = True
                continue

            # Index 2/2, flood queue length 0
            p10 = re.compile(r'^Index +(?P<index>(\S+)),'
                               ' +flood +queue +length +(?P<length>(\d+))$')
            m = p10.match(line)
            if m:
                sub_dict['index'] = str(m.groupdict()['index'])
                sub_dict['flood_queue_length'] = int(m.groupdict()['length'])
                continue

            # Next 0(0)/0(0)
            p11 = re.compile(r'^Next +(?P<next>(\S+))$')
            m = p11.match(line)
            if m:
                sub_dict['next'] = str(m.groupdict()['next'])
                continue

            # Last flood scan length is 1, maximum is 3
            p11 = re.compile(r'^Last +flood +scan +length +is +(?P<num>(\d+)),'
                              ' +maximum +is +(?P<max>(\d+))$')
            m = p11.match(line)
            if m:
                sub_dict['last_flood_scan_length'] = int(m.groupdict()['num'])
                sub_dict['max_flood_scan_length'] = int(m.groupdict()['max'])
                continue

            # Last flood scan time is 0 msec, maximum is 0 msec
            p12 = re.compile(r'^Last +flood +scan +time +is +(?P<time1>(\d+))'
                              ' +msec, +maximum +is +(?P<time2>(\d+)) +msec$')
            m = p12.match(line)
            if m:
                sub_dict['last_flood_scan_time_msec'] = \
                    int(m.groupdict()['time1'])
                sub_dict['max_flood_scan_time_msec'] = \
                    int(m.groupdict()['time2'])
                continue

            # LS Ack List: current length 0, high water mark 7
            p13 = re.compile(r'^LS +Ack +List: +(?P<ls_ack_list>(\S+)) +length'
                              ' +(?P<num>(\d+)), +high +water +mark'
                              ' +(?P<num2>(\d+))$')
            m = p13.match(line)
            if m:
                sub_dict['ls_ack_list'] = str(m.groupdict()['ls_ack_list'])
                sub_dict['ls_ack_list_length'] = int(m.groupdict()['num'])
                sub_dict['high_water_mark'] = int(m.groupdict()['num2'])
                continue

            # Neighbor Count is 1, Adjacent neighbor count is 1
            p14 = re.compile(r'^Neighbor +Count +is +(?P<nbr_count>(\d+)),'
                              ' +Adjacent +neighbor +count +is'
                              ' +(?P<adj_nbr_count>(\d+))$')
            m = p14.match(line)
            if m:
                sub_dict['nbr_count'] = int(m.groupdict()['nbr_count'])
                sub_dict['adj_nbr_count'] = int(m.groupdict()['adj_nbr_count'])
                continue

            # Adjacent with neighbor 2.2.2.2  (Backup Designated Router)
            p15 = re.compile(r'^Adjacent +with +neighbor +(?P<adj_nbr>(\S+))'
                              ' +\(.*\)$')
            m = p15.match(line)
            if m:
                sub_dict['adj_nbr'] = str(m.groupdict()['adj_nbr'])
                continue

            # Suppress hello for 0 neighbor(s)
            p16 = re.compile(r'^Suppress +hello +for +(?P<sup>(\d+))'
                              ' +neighbor\(s\)$')
            m = p16.match(line)
            if m:
                sub_dict['num_nbrs_suppress_hello'] = int(m.groupdict()['sup'])
                continue

            # Multi-area interface Count is 0
            p17 = re.compile(r'^Multi-area +interface +Count +is'
                              ' +(?P<count>(\d+))$')
            m = p17.match(line)
            if m:
                sub_dict['multi_area_intf_count'] = int(m.groupdict()['count'])
                continue

            # Configured as demand circuit.
            p18 = re.compile(r'^Configured as demand circuit\.$')
            m = p18.match(line)
            if m:
                sub_dict['demand_circuit'] = True
                continue

            # Run as demand circuit.
            p19 = re.compile(r'^Run as demand circuit\.$')
            m = p19.match(line)
            if m:
                sub_dict['demand_circuit'] = True

            # DoNotAge LSA not allowed (Number of DCbitless LSA is 1).
            p20 = re.compile(r'^DoNotAge LSA not allowed \(.*\)\.$')
            m = p20.match(line)
            if m:
                sub_dict['demand_circuit'] = True

            # BFD enabled, BFD interval 12345 msec, BFD multiplier 50, Mode: Default
            p21 = re.compile(r'^BFD enabled'
                              '(?:, +BFD +interval +(?P<interval>(\d+)) +msec)?'
                              '(?:, +BFD +multiplier +(?P<multi>(\d+)))?'
                              '(?:, +Mode: +(?P<mode>(\S+)))?$')
            m = p21.match(line)
            if m:
                sub_dict['bfd']['enable'] = True
                if m.groupdict()['interval']:
                    sub_dict['bfd']['interval'] = int(m.groupdict()['interval'])
                if m.groupdict()['multi']:
                    sub_dict['bfd']['multiplier'] = int(m.groupdict()['multi'])
                if m.groupdict()['mode']:
                    sub_dict['bfd']['mode'] = str(m.groupdict()['mode'])
                    continue

        return ret_dict


# ========================================================
# Schema for 'show ospf vrf all-inclusive neighbor detail'
# ========================================================
class ShowOspfVrfAllInclusiveNeighborDetailSchema(MetaParser):

    ''' Schema for "show ospf vrf all-inclusive neighbor detail" '''

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {'instance': 
                            {Any(): 
                                {'total_neighbor_count': int,
                                'areas': 
                                    {Any(): 
                                        {Optional('interfaces'): 
                                            {Any(): 
                                                {'neighbors': 
                                                    {Any(): 
                                                        {'neighbor_router_id': str,
                                                        'address': str,
                                                        'priority': int,
                                                        'state': str,
                                                        'num_state_changes': int,
                                                        'dr_ip_addr': str,
                                                        'bdr_ip_addr': str,
                                                        Optional('options'): str,
                                                        Optional('lls_options'): str,
                                                        Optional('dead_timer'): str,
                                                        Optional('neighbor_uptime'): str,
                                                        Optional('dbd_retrans'): int,
                                                        Optional('index'): str,
                                                        Optional('retransmission_queue_length'): int,
                                                        Optional('num_retransmission'): int,
                                                        Optional('first'): str,
                                                        Optional('next'): str,
                                                        Optional('last_retrans_scan_length'): int,
                                                        Optional('last_retrans_max_scan_length'): int,
                                                        Optional('last_retrans_scan_time_msec'): int,
                                                        Optional('last_retrans_max_scan_time_msec'): int,
                                                        Optional('ls_ack_list'): str,
                                                        Optional('ls_ack_list_pending'): int,
                                                        Optional('high_water_mark'): int,
                                                        },
                                                    },
                                                },
                                            },
                                        Optional('sham_links'):
                                            {Any(): 
                                                {'neighbors': 
                                                    {Any(): 
                                                        {'neighbor_router_id': str,
                                                        'address': str,
                                                        'priority': int,
                                                        'state': str,
                                                        'num_state_changes': int,
                                                        'dr_ip_addr': str,
                                                        'bdr_ip_addr': str,
                                                        Optional('options'): str,
                                                        Optional('lls_options'): str,
                                                        Optional('dead_timer'): str,
                                                        Optional('neighbor_uptime'): str,
                                                        Optional('dbd_retrans'): int,
                                                        Optional('index'): str,
                                                        Optional('retransmission_queue_length'): int,
                                                        Optional('num_retransmission'): int,
                                                        Optional('first'): str,
                                                        Optional('next'): str,
                                                        Optional('last_retrans_scan_length'): int,
                                                        Optional('last_retrans_max_scan_length'): int,
                                                        Optional('last_retrans_scan_time_msec'): int,
                                                        Optional('last_retrans_max_scan_time_msec'): int,
                                                        Optional('ls_ack_list'): str,
                                                        Optional('ls_ack_list_pending'): int,
                                                        Optional('high_water_mark'): int,
                                                        },
                                                    },
                                                },
                                            },
                                        Optional('virtual_links'):
                                            {Any(): 
                                                {'neighbors': 
                                                    {Any(): 
                                                        {'neighbor_router_id': str,
                                                        'address': str,
                                                        'priority': int,
                                                        'state': str,
                                                        'num_state_changes': int,
                                                        'dr_ip_addr': str,
                                                        'bdr_ip_addr': str,
                                                        Optional('options'): str,
                                                        Optional('lls_options'): str,
                                                        Optional('dead_timer'): str,
                                                        Optional('neighbor_uptime'): str,
                                                        Optional('dbd_retrans'): int,
                                                        Optional('index'): str,
                                                        Optional('retransmission_queue_length'): int,
                                                        Optional('num_retransmission'): int,
                                                        Optional('first'): str,
                                                        Optional('next'): str,
                                                        Optional('last_retrans_scan_length'): int,
                                                        Optional('last_retrans_max_scan_length'): int,
                                                        Optional('last_retrans_scan_time_msec'): int,
                                                        Optional('last_retrans_max_scan_time_msec'): int,
                                                        Optional('ls_ack_list'): str,
                                                        Optional('ls_ack_list_pending'): int,
                                                        Optional('high_water_mark'): int,
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }


# ========================================================
# Parser for 'show ospf vrf all-inclusive neighbor detail'
# ========================================================
class ShowOspfVrfAllInclusiveNeighborDetail(ShowOspfVrfAllInclusiveNeighborDetailSchema):

    ''' Parser for "show ospf vrf all-inclusive neighbor detail" '''

    def cli(self):

        # Execute command on device
        out = self.device.execute('show ospf vrf all-inclusive neighbor detail')

        # Init vars
        ret_dict = {}
        af = 'ipv4' # this is ospf - always ipv4

        for line in out.splitlines():
            line = line.strip()

            # Neighbors for OSPF 1
            # Neighbors for OSPF 1, VRF VRF1
            p1 = re.compile(r'^Neighbors +for +OSPF +(?P<instance>(\S+))'
                             '(?:, +VRF +(?P<vrf>(\S+)))?$')
            m = p1.match(line)
            if m:
                instance = str(m.groupdict()['instance'])
                if m.groupdict()['vrf']:
                    vrf = str(m.groupdict()['vrf'])
                else:
                    vrf = 'default'
                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}
                if 'address_family' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['address_family'] = {}
                if af not in ret_dict['vrf'][vrf]['address_family']:
                    ret_dict['vrf'][vrf]['address_family'][af] = {}
                if 'instance' not in ret_dict['vrf'][vrf]['address_family'][af]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance'] = {}
                if instance not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance] = {}
                    continue

            # Neighbor 2.2.2.2, interface address 10.2.3.2
            p2 = re.compile(r'^Neighbor +(?P<neighbor>(\S+)), +interface'
                             ' +address +(?P<address>(\S+))$')
            m = p2.match(line)
            if m:
                neighbor = str(m.groupdict()['neighbor'])
                address = str(m.groupdict()['address'])
                continue

            # In the area 0 via interface GigabitEthernet0/0/0/2 
            p3 = re.compile(r'^In +the +area +(?P<area>(\S+)) +via +interface'
                             ' +(?P<interface>(\S+))$')
            m = p3.match(line)
            if m:
                area = str(IPAddress(str(m.groupdict()['area'])))
                interface = str(m.groupdict()['interface'])

                # Determine if 'interface' or 'sham_link' or 'virtual_link'
                if re.search('SL', interface):
                    # Set values for dict
                    intf_type = 'sham_links'
                    intf_name = area + ' ' + address
                elif re.search('VL', interface):
                    # Set values for dict
                    intf_type = 'virtual_links'
                    intf_name = area + ' ' + address
                else:
                    # Set values for dict
                    intf_type = 'interfaces'
                    intf_name = interface

                if 'areas' not in ret_dict['vrf'][vrf]['address_family']\
                        [af]['instance'][instance]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'] = {}
                if area not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area] = {}
                if intf_type not in ret_dict['vrf'][vrf]['address_family']\
                        [af]['instance'][instance]['areas'][area]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area][intf_type] = {}
                if intf_name not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area][intf_type]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area][intf_type][intf_name] = {}
                if 'neighbors' not in ret_dict['vrf'][vrf]['address_family']\
                        [af]['instance'][instance]['areas'][area][intf_type]\
                        [intf_name]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area][intf_type][intf_name]\
                        ['neighbors'] = {}
                if neighbor not in ret_dict['vrf'][vrf]['address_family']\
                        [af]['instance'][instance]['areas'][area][intf_type]\
                        [intf_name]['neighbors']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area][intf_type][intf_name]\
                        ['neighbors'][neighbor] = {}
                # Set sub_dict
                sub_dict = ret_dict['vrf'][vrf]['address_family'][af]\
                            ['instance'][instance]['areas'][area][intf_type]\
                            [intf_name]['neighbors'][neighbor]
                sub_dict['neighbor_router_id'] = neighbor
                sub_dict['address'] = address
                continue

            # Neighbor priority is 1, State is FULL, 6 state changes
            p4 = re.compile(r'^Neighbor +priority +is +(?P<priority>(\d+)),'
                             ' +State +is +(?P<state>(\S+)),'
                             ' +(?P<num>(\d+)) +state +changes$')
            m = p4.match(line)
            if m:
                sub_dict['priority'] = int(m.groupdict()['priority'])
                state = str(m.groupdict()['state']).lower()
                state = state.replace('_', '-')
                sub_dict['state'] = state
                sub_dict['num_state_changes'] = int(m.groupdict()['num'])
                continue

            # DR is 10.2.3.3 BDR is 10.2.3.2
            p5 = re.compile(r'^DR +is +(?P<dr_ip_addr>(\S+))'
                             ' +BDR +is +(?P<bdr_ip_addr>(\S+))$')
            m = p5.match(line)
            if m:
                sub_dict['dr_ip_addr'] = str(m.groupdict()['dr_ip_addr'])
                sub_dict['bdr_ip_addr'] = str(m.groupdict()['bdr_ip_addr'])
                continue

            # Options is 0x42
            p6_1 = re.compile(r'^Options +is +(?P<options>(\S+))$')
            m = p6_1.match(line)
            if m:
                sub_dict['options'] = str(m.groupdict()['options'])
                continue

            # LLS Options is 0x1 (LR)
            p6_2 = re.compile(r'^LLS +Options +is +(?P<lls_options>(.*))$')
            m = p6_2.match(line)
            if m:
                sub_dict['lls_options'] = str(m.groupdict()['lls_options'])
                continue

            # Dead timer due in 00:00:38
            p7 = re.compile(r'^Dead +timer +due +in +(?P<dead_timer>(\S+))$')
            m = p7.match(line)
            if m:
                sub_dict['dead_timer'] = str(m.groupdict()['dead_timer'])
                continue

            # Neighbor is up for 08:22:07
            p8 = re.compile(r'^Neighbor +is +up +for +(?P<uptime>(\S+))$')
            m = p8.match(line)
            if m:
                sub_dict['neighbor_uptime'] = str(m.groupdict()['uptime'])
                continue

            # Number of DBD retrans during last exchange 0
            p9 = re.compile(r'^Number +of +DBD +retrans +during +last'
                             ' +exchange +(?P<dbd_retrans>(\d+))$')
            m = p9.match(line)
            if m:
                sub_dict['dbd_retrans'] = int(m.groupdict()['dbd_retrans'])
                continue

            # Index 1/1, retransmission queue length 0, number of retransmission 0
            p10 = re.compile(r'^Index +(?P<index>(\S+)) +retransmission +queue'
                             ' +length +(?P<ql>(\d+)), +number +of'
                             ' +retransmission +(?P<num_retrans>(\d+))$')
            m = p10.match(line)
            if m:
                sub_dict['index'] = str(m.groupdict()['index'])
                sub_dict['retransmission_queue_length'] = \
                    int(m.groupdict()['ql'])
                sub_dict['num_retransmission'] = \
                    int(m.groupdict()['num_retrans'])
                continue

            # First 0(0)/0(0) Next 0(0)/0(0)
            p11 = re.compile(r'^First +(?P<first>(\S+)) +Next +(?P<next>(\S+))$')
            m = p11.match(line)
            if m:
                sub_dict['first'] = str(m.groupdict()['first'])
                sub_dict['next'] = str(m.groupdict()['next'])
                continue

            # Last retransmission scan length is 0, maximum is 0
            p12 = re.compile(r'^Last +retransmission +scan +length +is'
                              ' +(?P<num1>(\d+)), +maximum +is'
                              ' +(?P<num2>(\d+))$')
            m = p12.match(line)
            if m:
                sub_dict['last_retrans_scan_length'] = \
                    int(m.groupdict()['num1'])
                sub_dict['last_retrans_max_scan_length'] = \
                    int(m.groupdict()['num2'])
                continue

            # Last retransmission scan time is 0 msec, maximum is 0 msec
            p13 = re.compile(r'^Last +retransmission +scan +time +is'
                              ' +(?P<num1>(\d+)) +msec, +maximum +is'
                              ' +(?P<num2>(\d+)) +msec$')
            m = p13.match(line)
            if m:
                sub_dict['last_retrans_scan_time_msec'] = \
                    int(m.groupdict()['num1'])
                sub_dict['last_retrans_max_scan_time_msec'] = \
                    int(m.groupdict()['num2'])
                continue

            # LS Ack list: NSR-sync pending 0, high water mark 0
            p14 = re.compile(r'^LS +Ack +list: +(?P<ls_ack_list>(\S+))'
                              ' +pending +(?P<pending>(\d+)), +high +water'
                              ' +mark +(?P<mark>(\d+))$')
            m = p14.match(line)
            if m:
                sub_dict['ls_ack_list'] = str(m.groupdict()['ls_ack_list'])
                sub_dict['ls_ack_list_pending'] = int(m.groupdict()['pending'])
                sub_dict['high_water_mark'] = int(m.groupdict()['mark'])
                continue

            # Total neighbor count: 2
            p15 = re.compile(r'^Total +neighbor +count: +(?P<num>(\d+))$')
            m = p15.match(line)
            if m:
                ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                    [instance]['total_neighbor_count'] = \
                        int(m.groupdict()['num'])

        return ret_dict


# ========================================
# Schema for 'show ospf vrf all-inclusive'
# ========================================
class ShowOspfVrfAllInclusiveSchema(MetaParser):

    ''' Schema for "show ospf vrf all-inclusive" '''

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {'instance': 
                            {Any(): 
                                {'router_id': str,
                                'role': str,
                                'nsr': 
                                    {'enable': bool},
                                Optional('database_control'): 
                                    {'max_lsa': int},
                                'stub_router': 
                                    {Optional('always'): 
                                        {'always': bool,
                                        'include_stub': bool,
                                        'summary_lsa': bool,
                                        'external_lsa': bool,
                                        Optional('duration'): int,
                                        Optional('state'): str},
                                    Optional('on_startup'): 
                                        {'on_startup': bool,
                                        'include_stub': bool,
                                        'summary_lsa': bool,
                                        'external_lsa':bool,
                                        Optional('duration'): int,
                                        Optional('state'): str},
                                    Optional('on_switchover'): 
                                        {'on_switchover': bool,
                                        'include_stub': bool,
                                        'summary_lsa': bool,
                                        'external_lsa': bool,
                                        Optional('duration'): int,
                                        Optional('state'): str},
                                    },
                                'spf_control': 
                                    {Optional('paths'): str,
                                    'throttle': 
                                        {'spf': 
                                            {'start': int,
                                            'hold': int,
                                            'maximum': int},
                                        'lsa': 
                                            {'start': int,
                                            'hold': int,
                                            'maximum': int,
                                            'interval': int,
                                            'arrival': int,
                                            'refresh_interval': int},
                                        },
                                    },
                                Optional('flood_pacing_interval'): int,
                                Optional('retransmission_interval'): int,
                                Optional('adjacency_stagger'): 
                                    {'disable': bool,
                                    'initial_number': int,
                                    'maximum_number': int},
                                Optional('numbers'): 
                                    {Optional('nbrs_forming'): int,
                                    Optional('nbrs_full'): int,
                                    Optional('configured_interfaces'): int,
                                    Optional('external_lsa'): int,
                                    Optional('external_lsa_checksum'): str,
                                    Optional('opaque_as_lsa'): int,
                                    Optional('opaque_as_lsa_checksum'): str,
                                    Optional('dc_bitless'): int,
                                    Optional('do_not_age'): int},
                                Optional('external_flood_list_length'): int,
                                Optional('snmp_trap'): bool,
                                Optional('lsd_state'): str,
                                Optional('lsd_revision'): int,
                                Optional('segment_routing_global_block_default'): str,
                                Optional('strict_spf_capability'): bool,
                                Optional('areas'): 
                                    {Any(): 
                                        {Optional('area_type'): str,
                                        Optional('rrr_enabled'): bool,
                                        Optional('topology_version'): int,
                                        Optional('statistics'): 
                                            {Optional('interfaces_count'): int,
                                            Optional('spf_runs_count'): int,
                                            Optional('area_scope_lsa_count'): int,
                                            Optional('area_scope_lsa_cksum_sum'): str,
                                            Optional('area_scope_opaque_lsa_count'): int,
                                            Optional('area_scope_opaque_lsa_cksum_sum'): str,
                                            Optional('dcbitless_lsa_count'): int,
                                            Optional('indication_lsa_count'): int,
                                            Optional('donotage_lsa_count'): int,
                                            Optional('flood_list_length'): int,
                                            Optional('lfa_interface_count'): int,
                                            Optional('lfa_revision'): int,
                                            Optional('lfa_per_prefix_interface_count'): int,
                                            Optional('nbrs_staggered_mode'): int,
                                            Optional('nbrs_full'): int},
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }


# ========================================
# Parser for 'show ospf vrf all-inclusive'
# ========================================
class ShowOspfVrfAllInclusive(ShowOspfVrfAllInclusiveSchema):

    ''' Parser for "show ospf vrf all-inclusive" '''

    def cli(self):

        # Execute command on device
        out = self.device.execute('show ospf vrf all-inclusive')

        # Init vars
        ret_dict = {}
        af = 'ipv4' # this is ospf - always ipv4

        for line in out.splitlines():
            line = line.strip()

            # Routing Process "ospf 1" with ID 3.3.3.3
            # VRF VRF1 in Routing Process "ospf 1" with ID 3.3.3.3
            p1 = re.compile(r'(?:^VRF +(?P<vrf>(\S+)) +in +)?Routing +Process'
                             ' +\"(?P<instance>([a-zA-Z0-9\s]+))\" +with +ID'
                             ' +(?P<router_id>(\S+))$')
            m = p1.match(line)
            if m:
                instance = str(m.groupdict()['instance'])
                router_id = str(m.groupdict()['router_id'])
                if m.groupdict()['vrf']:
                    vrf = str(m.groupdict()['vrf'])
                else:
                    vrf = 'default'

                # Set structure
                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}
                if 'address_family' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['address_family'] = {}
                if af not in ret_dict['vrf'][vrf]['address_family']:
                    ret_dict['vrf'][vrf]['address_family'][af] = {}
                if 'instance' not in ret_dict['vrf'][vrf]['address_family'][af]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance'] = {}
                if instance not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance] = {}

                # Set sub_dict
                sub_dict = ret_dict['vrf'][vrf]['address_family'][af]\
                            ['instance'][instance]
                sub_dict['router_id'] = router_id
                continue

            # Role: Primary Active
            p2 = re.compile(r'^Role *: +(?P<role>([a-zA-z0-9\s]+))$')
            m = p2.match(line)
            if m:
                sub_dict['role'] = str(m.groupdict()['role']).lower()
                continue

            # NSR (Non-stop routing) is Enabled
            p3 = re.compile(r'^NSR +\(Non-stop routing\) +is +(?P<nsr>(\S+))$')
            m = p3.match(line)
            if m:
                nsr = str(m.groupdict()['nsr']).lower()
                if 'nsr' not in sub_dict:
                    sub_dict['nsr'] = {}
                if nsr == 'enabled':
                    sub_dict['nsr']['enable'] = True
                else:
                    sub_dict['nsr']['enable'] = False
                    continue

            # Supports only single TOS(TOS0) routes
            p3 = re.compile(r'^Supports +only +single +TOS(TOS0) routes$')
            m = p3.match(line)
            if m:
                # Not sure what the key is
                continue

            # Supports opaque LSA
            p4 = re.compile(r'^Supports +opaque +LSA$')
            m = p4.match(line)
            if m:
                # Not sure what the key is
                continue

            # It is an area border and autonomous system boundary router
            p5_0 = re.compile(r'^It +is +an +area +border +and +autonomous'
                               ' +system +boundary +router$')
            m = p5_0.match(line)
            if m:
                # Not sure whast the key is
                continue

            # Router is not originating router-LSAs with maximum metric
            p5_1 = re.compile(r'^Router +is +not +originating +router-LSAs'
                               ' +with +maximum +metric$')
            m = p5_1.match(line)
            if m:
                if 'stub_router' not in sub_dict:
                    sub_dict['stub_router'] = {}
                if 'always' not in sub_dict['stub_router']:
                    sub_dict['stub_router']['always'] = {}
                # Set values
                sub_dict['stub_router']['always']['always'] = False
                sub_dict['stub_router']['always']['include_stub'] = False
                sub_dict['stub_router']['always']['summary_lsa'] = False
                sub_dict['stub_router']['always']['external_lsa'] = False
                continue

            # Originating router-LSAs with maximum metric
            p5_2 = re.compile(r'^Originating +router-LSAs +with +maximum'
                               ' +metric$')
            m = p5_2.match(line)
            if m:
                if 'stub_router' not in sub_dict:
                    sub_dict['stub_router'] = {}
                    continue

            # Condition: always State: active
            # Condition: on switch-over for 10 seconds, State: inactive
            # Condition: on start-up for 5 seconds, State: inactive
            p5_3 = re.compile(r'^Condition:(?: +on)?'
                               ' +(?P<condition>([a-zA-Z\-]+))'
                               '(?: +for +(?P<seconds>(\d+)) +seconds,)?'
                               ' +State: +(?P<state>(\S+))$')
            m = p5_3.match(line)
            if m:
                condition = str(m.groupdict()['condition']).lower()
                if condition != 'always':
                    condition = "on_" + condition.replace("-", "")
                # Set keys
                if condition not in sub_dict['stub_router']:
                    sub_dict['stub_router'][condition] = {}
                sub_dict['stub_router'][condition][condition] = True
                if m.groupdict()['seconds']:
                    sub_dict['stub_router'][condition]['duration'] = \
                        int(m.groupdict()['seconds'])
                if m.groupdict()['state']:
                    sub_dict['stub_router'][condition]['state'] = \
                        str(m.groupdict()['state']).lower()
                continue

            # Advertise stub links with maximum metric in router-LSAs
            p5_4 = re.compile(r'^Advertise +stub +links +with +maximum +metric'
                               ' +in +router\-LSAs$')
            m = p5_4.match(line)
            if m:
                sub_dict['stub_router'][condition]['include_stub'] = True
                continue

            # Advertise summary-LSAs with metric 16711680
            p5_5 = re.compile(r'^Advertise +summary\-LSAs +with +metric'
                               ' +(?P<metric>(\d+))$')
            m = p5_5.match(line)
            if m:
                sub_dict['stub_router'][condition]['summary_lsa'] = True
                continue

            # Advertise external-LSAs with metric 16711680
            p5_6 = re.compile(r'^^Advertise +external\-LSAs +with +metric'
                               ' +(?P<metric>(\d+))$')
            m = p5_6.match(line)
            if m:
                sub_dict['stub_router'][condition]['external_lsa'] = True
                continue

            # Initial SPF schedule delay 50 msecs
            p6 = re.compile(r'^Initial +SPF +schedule +delay +(?P<time>(\S+))'
                             ' +msecs$')
            m = p6.match(line)
            if m:
                start = int(float(m.groupdict()['time']))
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                if 'throttle' not in sub_dict['spf_control']:
                    sub_dict['spf_control']['throttle'] = {}
                if 'spf' not in sub_dict['spf_control']['throttle']:
                    sub_dict['spf_control']['throttle']['spf'] = {}
                sub_dict['spf_control']['throttle']['spf']['start'] = start
                continue

            # Minimum hold time between two consecutive SPFs 200 msecs
            p7 = re.compile(r'^Minimum +hold +time +between +two +consecutive'
                             ' +SPFs +(?P<time>(\S+)) +msecs$')
            m = p7.match(line)
            if m:
                hold = int(float(m.groupdict()['time']))
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                if 'throttle' not in sub_dict['spf_control']:
                    sub_dict['spf_control']['throttle'] = {}
                if 'spf' not in sub_dict['spf_control']['throttle']:
                    sub_dict['spf_control']['throttle']['spf'] = {}
                sub_dict['spf_control']['throttle']['spf']['hold'] = hold
                continue

            # Maximum wait time between two consecutive SPFs 5000 msecs
            p8 = re.compile(r'^Maximum +wait +time +between +two +consecutive'
                             ' +SPFs +(?P<time>(\S+)) +msecs$')
            m = p8.match(line)
            if m:
                maximum = int(float(m.groupdict()['time']))
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                if 'throttle' not in sub_dict['spf_control']:
                    sub_dict['spf_control']['throttle'] = {}
                if 'spf' not in sub_dict['spf_control']['throttle']:
                    sub_dict['spf_control']['throttle']['spf'] = {}
                sub_dict['spf_control']['throttle']['spf']['maximum'] = maximum
                continue

            # Initial LSA throttle delay 50 msecs
            p9 = re.compile(r'^Initial +LSA +throttle +delay +(?P<time>(\S+))'
                             ' +msecs$')
            m = p9.match(line)
            if m:
                start = int(float(m.groupdict()['time']))
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                if 'throttle' not in sub_dict['spf_control']:
                    sub_dict['spf_control']['throttle'] = {}
                if 'lsa' not in sub_dict['spf_control']['throttle']:
                    sub_dict['spf_control']['throttle']['lsa'] = {}
                sub_dict['spf_control']['throttle']['lsa']['start'] = start
                continue

            # Minimum hold time for LSA throttle 200 msecs
            p10 = re.compile(r'^Minimum +hold +time +for +LSA +throttle'
                              ' +(?P<time>(\S+)) +msecs$')
            m = p10.match(line)
            if m:
                hold = int(float(m.groupdict()['time']))
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                if 'throttle' not in sub_dict['spf_control']:
                    sub_dict['spf_control']['throttle'] = {}
                if 'lsa' not in sub_dict['spf_control']['throttle']:
                    sub_dict['spf_control']['throttle']['lsa'] = {}
                sub_dict['spf_control']['throttle']['lsa']['hold'] = hold
                continue

            # Maximum wait time for LSA throttle 5000 msecs
            p11 = re.compile(r'^Maximum +wait +time +for +LSA +throttle'
                              ' +(?P<time>(\S+)) +msecs$')
            m = p11.match(line)
            if m:
                maximum = int(float(m.groupdict()['time']))
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                if 'throttle' not in sub_dict['spf_control']:
                    sub_dict['spf_control']['throttle'] = {}
                if 'lsa' not in sub_dict['spf_control']['throttle']:
                    sub_dict['spf_control']['throttle']['lsa'] = {}
                sub_dict['spf_control']['throttle']['lsa']['maximum'] = maximum
                continue

            # Minimum LSA interval 200 msecs. Minimum LSA arrival 100 msecs
            # Minimum LSA interval 200 msecs. Minimum LSA arrival 100 msecs
            p12 = re.compile(r'^Minimum +LSA +interval +(?P<interval>(\S+))'
                              ' +msecs. +Minimum +LSA +arrival'
                              ' +(?P<arrival>(\S+)) +msecs$')
            m = p12.match(line)
            if m:
                sub_dict['spf_control']['throttle']['lsa']['interval'] = \
                    int(float(m.groupdict()['interval']))
                sub_dict['spf_control']['throttle']['lsa']['arrival'] = \
                    int(float(m.groupdict()['arrival']))
                continue

            # LSA refresh interval 1800 seconds
            p13 = re.compile(r'^LSA +refresh +interval +(?P<refresh>(\S+))'
                              ' +seconds$')
            m = p13.match(line)
            if m:
                sub_dict['spf_control']['throttle']['lsa']\
                    ['refresh_interval'] = int(float(m.groupdict()['refresh']))
                continue

            # Flood pacing interval 33 msecs. Retransmission pacing interval 66 msecs
            p14 = re.compile(r'^Flood +pacing +interval +(?P<flood>(\d+))'
                              ' +msecs\. +Retransmission +pacing +interval'
                              ' +(?P<retransmission>(\d+)) +msecs$')
            m = p14.match(line)
            if m:
                sub_dict['flood_pacing_interval'] = \
                    int(float(m.groupdict()['flood']))
                sub_dict['retransmission_interval'] = \
                    int(float(m.groupdict()['retransmission']))
                continue

            # Adjacency stagger enabled; initial (per area): 2, maximum: 64
            p15 = re.compile(r'^Adjacency +stagger +(?P<adj>(\S+)); +initial'
                              ' +\(per +area\): +(?P<init>(\d+)),'
                              ' +maximum: +(?P<max>(\d+))$')
            m = p15.match(line)
            if m:
                if 'adjacency_stagger' not in sub_dict:
                    sub_dict['adjacency_stagger'] = {}
                if 'enable' in m.groupdict()['adj']:
                    sub_dict['adjacency_stagger']['disable'] = False
                else:
                    sub_dict['adjacency_stagger']['disable'] = True
                sub_dict['adjacency_stagger']['initial_number'] = \
                    int(m.groupdict()['init'])
                sub_dict['adjacency_stagger']['maximum_number'] = \
                    int(m.groupdict()['max'])
                continue

            # Number of neighbors forming: 0, 2 full
            p16 = re.compile(r'^Number +of +neighbors +forming:'
                              ' +(?P<form>(\d+)), +(?P<full>(\d+)) +full$')
            m = p16.match(line)
            if m:
                if 'numbers' not in sub_dict:
                    sub_dict['numbers'] = {}
                sub_dict['numbers']['nbrs_forming'] = int(m.groupdict()['form'])
                sub_dict['numbers']['nbrs_full'] = int(m.groupdict()['full'])
                continue

            # Maximum number of configured interfaces 1024
            p17 = re.compile(r'^Maximum +number +of +configured +interfaces'
                              ' +(?P<cfgd>(\d+))$')
            m = p17.match(line)
            if m:
                if 'numbers' not in sub_dict:
                    sub_dict['numbers'] = {}
                sub_dict['numbers']['configured_interfaces'] = \
                    int(m.groupdict()['cfgd'])
                continue

            # Number of external LSA 1. Checksum Sum 0x00607f
            p18 = re.compile(r'^Number +of +external +LSA +(?P<ext>(\d+))\.'
                              ' +Checksum +Sum +(?P<checksum>(\S+))$')
            m = p18.match(line)
            if m:
                if 'numbers' not in sub_dict:
                    sub_dict['numbers'] = {}
                sub_dict['numbers']['external_lsa'] = int(m.groupdict()['ext'])
                sub_dict['numbers']['external_lsa_checksum'] = \
                    str(m.groupdict()['checksum'])
                continue

            # Number of opaque AS LSA 0. Checksum Sum 00000000
            p19 = re.compile(r'^Number +of +opaque +AS +LSA +(?P<opq>(\d+))\.'
                              ' +Checksum +Sum +(?P<checksum>(\S+))$')
            m = p19.match(line)
            if m:
                if 'numbers' not in sub_dict:
                    sub_dict['numbers'] = {}
                sub_dict['numbers']['opaque_as_lsa'] = int(m.groupdict()['opq'])
                sub_dict['numbers']['opaque_as_lsa_checksum'] = \
                    str(m.groupdict()['checksum'])
                continue

            # Number of DCbitless external and opaque AS LSA 0
            p20 = re.compile(r'^Number +of +DCbitless +external +and +opaque'
                              ' +AS +LSA +(?P<num>(\d+))$')
            m = p20.match(line)
            if m:
                if 'numbers' not in sub_dict:
                    sub_dict['numbers'] = {}
                sub_dict['numbers']['dc_bitless'] = int(m.groupdict()['num'])
                continue

            # Number of DoNotAge external and opaque AS LSA 0
            p21 = re.compile(r'^Number +of +DoNotAge +external +and +opaque'
                              ' +AS +LSA +(?P<num>(\d+))$')
            m = p21.match(line)
            if m:
                if 'numbers' not in sub_dict:
                    sub_dict['numbers'] = {}
                sub_dict['numbers']['do_not_age'] = int(m.groupdict()['num'])
                continue

            # Number of areas in this router is 1. 1 normal 0 stub 0 nssa
            p22 = re.compile(r'^Number +of +areas +in +this +router +is'
                              ' +(?P<num_areas>(\d+))\. +(?P<normal>(\d+))'
                              ' +normal +(?P<stub>(\d+)) +stub +(?P<nssa>(\d+))'
                              ' +nssa$')
            m = p22.match(line)
            if m:
                num_areas = int(m.groupdict()['num_areas'])
                normal = int(m.groupdict()['normal'])
                stub = int(m.groupdict()['stub'])
                nssa = int(m.groupdict()['nssa'])
                if normal == 1:
                    area_type = 'normal'
                elif stub == 1:
                    area_type = 'stub'
                elif nssa == 1:
                    area_type = 'nssa'
                continue

            # External flood list length 0
            p23 = re.compile(r'^External +flood +list +length +(?P<num>(\d+))$')
            m = p23.match(line)
            if m:
                sub_dict['external_flood_list_length'] = int(m.groupdict()['num'])
                continue

            # SNMP trap is enabled
            p24 = re.compile(r'^SNMP +trap +is +(?P<snmp>(\S+))$')
            m = p24.match(line)
            if m:
                if 'enabled' in m.groupdict()['snmp']:
                    sub_dict['snmp_trap'] = True
                else:
                    sub_dict['snmp_trap'] = False
                continue

            # LSD connected, registered, bound, revision 1
            p25 = re.compile(r'^LSD +(?P<lsd>([a-zA-Z\,\s]+)), +revision'
                              ' +(?P<revision>(\d+))$')
            m = p25.match(line)
            if m:
                sub_dict['lsd_state'] = str(m.groupdict()['lsd'])
                sub_dict['lsd_revision'] = int(m.groupdict()['revision'])
                continue

            # Segment Routing Global Block default (16000-23999), not allocated
            p26 = re.compile(r'^Segment +Routing +Global +Block +default'
                              ' +\((?P<sr_block>([0-9\-]+))\), +not +allocated$')
            m = p26.match(line)
            if m:
                sub_dict['segment_routing_global_block_default'] = \
                    str(m.groupdict()['sr_block'])
                continue

            # Strict-SPF capability is enabled
            p27 = re.compile(r'^Strict-SPF +capability +is +(?P<state>(\S+))$')
            m = p27.match(line)
            if m:
                if 'enabled' in m.groupdict()['state']:
                    sub_dict['strict_spf_capability'] = True
                else:
                    sub_dict['strict_spf_capability'] = False
                continue

            # Area BACKBONE(0)
            # Area 1
            p28 = re.compile(r'^Area +(?P<area>(\S+))$')
            m = p28.match(line)
            if m:
                parsed_area = str(m.groupdict()['area'])
                n = re.match('BACKBONE\((?P<area_num>(\d+))\)', parsed_area)
                if n:
                    area = str(IPAddress(str(n.groupdict()['area_num'])))
                else:
                    area = str(IPAddress(str(m.groupdict()['area'])))

                # Create dict
                if 'areas' not in sub_dict:
                    sub_dict['areas'] = {}
                if area not in sub_dict['areas']:
                    sub_dict['areas'][area] = {}
                
                # Set previously parsed values
                try:
                    sub_dict['areas'][area]['area_type'] = area_type
                except:
                    pass
                continue

            # Number of interfaces in this area is 3
            p29 = re.compile(r'^Number +of +interfaces +in +this +area +is'
                              ' +(?P<num_intf>(\d+))$')
            m = p29.match(line)
            if m:
                if 'statistics' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['statistics'] = {}
                sub_dict['areas'][area]['statistics']['interfaces_count'] =\
                    int(m.groupdict()['num_intf'])
                continue

            # Area has RRR enabled, topology version 15
            p30 = re.compile(r'^Area +has +RRR +enabled, +topology +version'
                              ' +(?P<topo_version>(\d+))$')
            m = p30.match(line)
            if m:
                sub_dict['areas'][area]['rrr_enabled'] = True
                sub_dict['areas'][area]['topology_version'] = \
                    int(m.groupdict()['topo_version'])
                continue

            # SPF algorithm executed 26 times
            p31 = re.compile(r'^SPF +algorithm +executed +(?P<count>(\d+))'
                              ' +times$')
            m = p31.match(line)
            if m:
                if 'statistics' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['statistics'] = {}
                sub_dict['areas'][area]['statistics']['spf_runs_count'] = \
                    int(m.groupdict()['count'])
                continue

            # Number of LSA 19.  Checksum Sum 0x0a2fb5
            p32 = re.compile(r'^Number +of +LSA +(?P<lsa_count>(\d+))\.'
                              ' +Checksum +Sum +(?P<checksum_sum>(\S+))$')
            m = p32.match(line)
            if m:
                if 'statistics' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['statistics'] = {}
                sub_dict['areas'][area]['statistics']['area_scope_lsa_count'] =\
                    int(m.groupdict()['lsa_count'])
                sub_dict['areas'][area]['statistics']\
                    ['area_scope_lsa_cksum_sum'] = \
                        str(m.groupdict()['checksum_sum'])
                continue

            # Number of opaque link LSA 0.  Checksum Sum 00000000
            p33 = re.compile(r'^Number +of opaque +link +LSA'
                              ' +(?P<opaque_count>(\d+))\. +Checksum +Sum'
                              ' +(?P<checksum_sum>(\S+))$')
            m = p33.match(line)
            if m:
                if 'statistics' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['statistics'] = {}
                sub_dict['areas'][area]['statistics']\
                    ['area_scope_opaque_lsa_count'] = \
                        int(m.groupdict()['opaque_count'])
                sub_dict['areas'][area]['statistics']\
                    ['area_scope_opaque_lsa_cksum_sum'] = \
                        str(m.groupdict()['checksum_sum'])
                continue

            # Number of DCbitless LSA 5
            p34 = re.compile(r'^Number +of +DCbitless +LSA +(?P<count>(\d+))$')
            m = p34.match(line)
            if m:
                if 'statistics' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['statistics'] = {}
                sub_dict['areas'][area]['statistics']['dcbitless_lsa_count'] = \
                    int(m.groupdict()['count'])
                continue

            # Number of indication LSA 0
            p35 = re.compile(r'^Number +of +indication +LSA +(?P<count>(\d+))$')
            m = p35.match(line)
            if m:
                if 'statistics' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['statistics'] = {}
                sub_dict['areas'][area]['statistics']['indication_lsa_count'] =\
                    int(m.groupdict()['count'])
                continue

            # Number of DoNotAge LSA 0
            p36 = re.compile(r'^Number +of +DoNotAge +LSA +(?P<count>(\d+))$')
            m = p36.match(line)
            if m:
                if 'statistics' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['statistics'] = {}
                sub_dict['areas'][area]['statistics']['donotage_lsa_count'] = \
                    int(m.groupdict()['count'])
                continue

            # Flood list length 0
            p37 = re.compile(r'^Flood +list +length +(?P<len>(\d+))$')
            m = p37.match(line)
            if m:
                if 'statistics' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['statistics'] = {}
                sub_dict['areas'][area]['statistics']['flood_list_length'] = \
                    int(m.groupdict()['len'])
                continue

            # Number of LFA enabled interfaces 0, LFA revision 0
            p38 = re.compile(r'^Number +of +LFA +enabled +interfaces'
                              ' +(?P<count>(\d+)), +LFA +revision'
                              ' +(?P<revision>(\d+))$')
            m = p38.match(line)
            if m:
                if 'statistics' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['statistics'] = {}
                sub_dict['areas'][area]['statistics']['lfa_interface_count'] = \
                    int(m.groupdict()['count'])
                sub_dict['areas'][area]['statistics']['lfa_revision'] = \
                    int(m.groupdict()['revision'])
                continue

            # Number of Per Prefix LFA enabled interfaces 0
            p39 = re.compile(r'^Number +of +Per +Prefix +LFA +enabled'
                              ' +interfaces +(?P<count>(\d+))$')
            m = p39.match(line)
            if m:
                if 'statistics' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['statistics'] = {}
                sub_dict['areas'][area]['statistics']\
                    ['lfa_per_prefix_interface_count'] = \
                        int(m.groupdict()['count'])
                continue

            # Number of neighbors forming in staggered mode 0, 2 full
            p40 = re.compile(r'^Number +of +neighbors +forming +in +staggered'
                              ' +mode +(?P<mode>(\d+)), +(?P<full>(\d+)) +full$')
            m = p40.match(line)
            if m:
                if 'statistics' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['statistics'] = {}
                sub_dict['areas'][area]['statistics']['nbrs_staggered_mode'] = \
                    int(m.groupdict()['mode'])
                sub_dict['areas'][area]['statistics']['nbrs_full'] = \
                    int(m.groupdict()['full'])
                continue

            # Maximum number of non self-generated LSA allowed 123
            p41 = re.compile(r'^Maximum +number +of +non +self-generated +LSA'
                              ' +allowed +(?P<max_lsa>(\d+))$')
            m = p41.match(line)
            if m:
                if 'database_control' not in sub_dict:
                    sub_dict['database_control'] = {}
                sub_dict['database_control']['max_lsa'] = \
                    int(m.groupdict()['max_lsa'])
                continue
        
        return ret_dict


# ======================================================
# Parser for 'show ospf vrf all-inclusive virtual-links'
# Parser for 'show ospf vrf all-inclusive sham-links'
# ======================================================
class ShowOspfLinksParser(MetaParser):

    ''' Parser for "show ip ospf vrf all-inclusive <WORD>-links" '''

    def cli(self, cmd, link_type):

        assert link_type in ['virtual_links', 'sham_links']

        # Execute command on device
        out = self.device.execute(cmd)
        
        # Init vars
        ret_dict = {}
        af = 'ipv4'

        for line in out.splitlines():
            line = line.strip()

            # Virtual Links for OSPF 1
            # Sham Links for OSPF 1, VRF VRF1
            p1 = re.compile(r'^(Virtual|Sham) +Links +for'
                             ' +(?P<instance>([a-zA-Z0-9\s]+))'
                             '(?:, +VRF +(?P<vrf>(\S+)))?$')
            m = p1.match(line)
            if m:
                instance = str(m.groupdict()['instance'])
                if m.groupdict()['vrf']:
                    vrf = str(m.groupdict()['vrf'])
                else:
                    vrf = 'default'

                # Build dict
                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}
                if 'address_family' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['address_family'] = {}
                if af not in ret_dict['vrf'][vrf]['address_family']:
                    ret_dict['vrf'][vrf]['address_family'][af] = {}
                if 'instance' not in ret_dict['vrf'][vrf]['address_family'][af]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance'] = {}
                if instance not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance] = {}
                    continue

            # Sham Link OSPF_SL0 to address 22.22.22.22 is up
            # Virtual Link OSPF_VL0 to router 4.4.4.4 is up
            p2 = re.compile(r'^(Virtual|Sham) +Link +(?P<link>(\S+)) +to'
                             ' +(address|router) +(?P<address>(\S+)) +is'
                             ' +(up|down)$')
            m = p2.match(line)
            if m:
                address = str(m.groupdict()['address'])
                sl_remote_id = vl_router_id = address
                link = str(m.groupdict()['link'])
                n = re.match('(?P<ignore>\S+)_(?P<name>(S|V)L(\d+))', link)
                if n:
                    real_link_name = str(n.groupdict()['name'])
                else:
                    real_link_name = link
                    continue

            # Area 1, source address 33.33.33.33
            p3_1 = re.compile(r'^Area +(?P<area>(\S+)), +source +address'
                             ' +(?P<source_address>(\S+))$')
            m = p3_1.match(line)
            if m:
                area = str(IPAddress(str(m.groupdict()['area'])))
                source_address = str(m.groupdict()['source_address'])

                # Set link_name for sham_link
                link_name = source_address + ' ' + sl_remote_id

                # Create dict
                if 'areas' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'] = {}
                if area not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area] = {}
                if link_type not in  ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area][link_type] = {}
                if link_name not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area][link_type]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area][link_type][link_name] = {}

                # Set sub_dict
                sub_dict = ret_dict['vrf'][vrf]['address_family'][af]\
                            ['instance'][instance]['areas'][area]\
                            [link_type][link_name]

                # Set values
                sub_dict['transit_area_id'] = area
                sub_dict['local_id'] = source_address
                sub_dict['demand_circuit'] = False

                # Set previously parsed values
                try:
                    sub_dict['name'] = real_link_name
                    sub_dict['remote_id'] = sl_remote_id
                except:
                    pass
                continue

            # Transit area 1, via interface GigabitEthernet0/0/0/3, Cost of using 65535
            p3_2 = re.compile(r'^Transit +area +(?P<area>(\S+)), +via +interface'
                               ' +(?P<intf>(\S+)), +Cost +of +using'
                               ' +(?P<cost>(\d+))$')
            m = p3_2.match(line)
            if m:
                area = str(IPAddress(str(m.groupdict()['area'])))
                interface = str(m.groupdict()['intf'])
                cost = int(m.groupdict()['cost'])

                # Set link_name for virtual_link
                link_name = area + ' ' + vl_router_id

                # Create dict
                if 'areas' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'] = {}
                if area not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area] = {}
                if link_type not in  ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area][link_type] = {}
                if link_name not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area][link_type]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area][link_type][link_name] = {}

                # Set sub_dict
                sub_dict = ret_dict['vrf'][vrf]['address_family'][af]\
                            ['instance'][instance]['areas'][area]\
                            [link_type][link_name]

                # Set values
                sub_dict['transit_area_id'] = area
                sub_dict['demand_circuit'] = False
                sub_dict['cost'] = int(m.groupdict()['cost'])

                # Set previously parsed values
                try:
                    sub_dict['name'] = real_link_name
                    sub_dict['router_id'] = vl_router_id
                    sub_dict['dcbitless_lsa_count'] = dcbitless_lsa_count
                    sub_dict['demand_circuit'] = demand_circuit
                except:
                    pass
                continue

            # IfIndex = 2
            p4 = re.compile(r'^IfIndex += +(?P<if_index>(\d+))$')
            m = p4.match(line)
            if m:
                sub_dict['if_index'] = int(m.groupdict()['if_index'])
                continue

            # Run as demand circuit
            p5 = re.compile(r'^Run +as +demand +circuit$')
            m = p5.match(line)
            if m:
                sub_dict['demand_circuit'] = True
                continue

            # DoNotAge LSA not allowed (Number of DCbitless LSA is 1)., Cost of using 111
            # DoNotAge LSA not allowed Run as demand circuit (Number of DCbitless LSA is 1).
            p6 = re.compile(r'^DoNotAge +LSA +not +allowed'
                             '(?: +(?P<demand>(Run +as +demand +circuit)))?'
                             ' +\(Number +of +DCbitless +LSA +is +(?P<dcbitless>(\d+))\).,?'
                             '(?: +Cost +of +using +(?P<cost>(\d+)))?$')
            m = p6.match(line)
            if m:
                dcbitless_lsa_count = int(m.groupdict()['dcbitless'])
                if m.groupdict()['demand']:
                    demand_circuit = True
                # Set values for sham_links
                if link_type == 'sham_links':
                    sub_dict['dcbitless_lsa_count'] = dcbitless_lsa_count
                    if m.groupdict()['cost']:
                        sub_dict['cost'] = int(m.groupdict()['cost'])
                        continue

            # Transmit Delay is 7 sec, State POINT_TO_POINT,
            # Transmit Delay is 5 sec, State POINT_TO_POINT,
            p7 = re.compile(r'^Transmit +Delay +is +(?P<transmit_delay>(\d+))'
                             ' +sec, +State +(?P<state>(\S+)),?$')
            m = p7.match(line)
            if m:
                sub_dict['transmit_delay'] = int(m.groupdict()['transmit_delay'])
                state = str(m.groupdict()['state']).lower()
                state = state.replace("_", "-")
                sub_dict['state'] = state
                continue

            # Timer intervals configured, Hello 3, Dead 13, Wait 13, Retransmit 5
            # Timer intervals configured, Hello 4, Dead 16, Wait 16, Retransmit 44
            p8 = re.compile(r'^Timer +intervals +configured,'
                             ' +Hello +(?P<hello>(\d+)),'
                             ' +Dead +(?P<dead>(\d+)),'
                             ' +Wait +(?P<wait>(\d+)),'
                             ' +Retransmit +(?P<retransmit>(\d+))$')
            m = p8.match(line)
            if m:
                sub_dict['hello_interval'] = int(m.groupdict()['hello'])
                sub_dict['dead_interval'] = int(m.groupdict()['dead'])
                sub_dict['wait_interval'] = int(m.groupdict()['wait'])
                sub_dict['retransmit_interval'] = int(m.groupdict()['retransmit'])
                continue

            # Hello due in 00:00:00:772
            # Hello due in 00:00:03:179
            p9 = re.compile(r'^Hello +due +in +(?P<hello_timer>(\S+))$')
            m = p9.match(line)
            if m:
                sub_dict['hello_timer'] = str(m.groupdict()['hello_timer'])
                continue          
          
            # Non-Stop Forwarding (NSF) enabled, last NSF restart 00:18:16 ago
            p10 = re.compile(r'^Non-Stop +Forwarding +\(NSF\) +enabled,'
                              ' +last +NSF +restart +(?P<restart>(\S+)) +ago$')
            m = p10.match(line)
            if m:
                if 'nsf' not in sub_dict:
                    sub_dict['nsf'] = {}
                sub_dict['nsf']['enable'] = True
                sub_dict['nsf']['last_restart'] = str(m.groupdict()['restart'])
                continue
            
            # Clear text authentication enabled
            p11 = re.compile(r'^(?P<auth>([a-zA-Z\s]+)) +authentication +enabled$')
            m = p11.match(line)
            if m:
                if 'authentication' not in sub_dict:
                    sub_dict['authentication'] = {}
                if 'auth_trailer_key' not in sub_dict['authentication']:
                    sub_dict['authentication']['auth_trailer_key'] = {}
                sub_dict['authentication']['auth_trailer_key']\
                    ['crypto_algorithm'] = str(m.groupdict()['auth']).lower()
                continue

        return ret_dict


# ===================================================
# Schema for 'show ospf vrf all-inclusive sham-links'
# ===================================================
class ShowOspfVrfAllInclusiveShamLinksSchema(MetaParser):

    ''' Schema for 'show ospf vrf all-inclusive sham-links' '''

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {'instance': 
                            {Any(): 
                                {'areas': 
                                    {Any(): 
                                        {'sham_links': 
                                            {Any(): 
                                                {'name': str,
                                                'local_id': str,
                                                'remote_id': str,
                                                'transit_area_id': str,
                                                'hello_interval': int,
                                                'dead_interval': int,
                                                'wait_interval': int,
                                                'retransmit_interval': int,
                                                'transmit_delay': int,
                                                'cost': int,
                                                'state': str,
                                                'hello_timer': str,
                                                'demand_circuit': bool,
                                                'dcbitless_lsa_count': int,
                                                'if_index': int,
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }


# ===================================================
# Parser for 'show ospf vrf all-inclusive sham-links'
# ===================================================
class ShowOspfVrfAllInclusiveShamLinks(ShowOspfVrfAllInclusiveShamLinksSchema, ShowOspfLinksParser):

    ''' Parser for 'show ospf vrf all-inclusive sham-links' '''

    def cli(self):
        
        cmd = 'show ospf vrf all-inclusive sham-links'
        return super().cli(cmd=cmd, link_type='sham_links')


# ======================================================
# Schema for 'show ospf vrf all-inclusive virtual-links'
# ======================================================
class ShowOspfVrfAllInclusiveVirtualLinksSchema(MetaParser):

    ''' Schema for 'show ospf vrf all-inclusive virtual-links' '''

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {'instance': 
                            {Any(): 
                                {'areas': 
                                    {Any(): 
                                        {'virtual_links': 
                                            {Any(): 
                                                {'name': str,
                                                'router_id': str,
                                                'transit_area_id': str,
                                                'hello_interval': int,
                                                'dead_interval': int,
                                                'wait_interval': int,
                                                'retransmit_interval': int,
                                                'transmit_delay': int,
                                                'cost': int,
                                                'state': str,
                                                'hello_timer': str,
                                                'demand_circuit': bool,
                                                'dcbitless_lsa_count': int,
                                                Optional('nsf'): 
                                                    {'enable': bool,
                                                    'last_restart': str},
                                                Optional('authentication'): 
                                                    {'auth_trailer_key': 
                                                        {'crypto_algorithm': str},
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }


# ======================================================
# Parser for 'show ospf vrf all-inclusive virtual-links'
# ======================================================
class ShowOspfVrfAllInclusiveVirtualLinks(ShowOspfVrfAllInclusiveVirtualLinksSchema, ShowOspfLinksParser):

    ''' Parser for 'show ospf vrf all-inclusive virtual-links' '''

    def cli(self):
        
        cmd = 'show ospf vrf all-inclusive virtual-links'
        return super().cli(cmd=cmd, link_type='virtual_links')


# =============================================
# Schema for 'show ospf mpls traffic-eng links'
# =============================================
class ShowOspfMplsTrafficEngLinksSchema(MetaParser):

    ''' Schema for 'show ospf mpls traffic-eng links' '''

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {'instance': 
                            {Any(): 
                                {'mpls': 
                                    {'te': 
                                        {'router_id': str},
                                    },
                                'areas': 
                                    {Any(): 
                                        {'mpls': 
                                            {'te': 
                                                {'enable': bool,
                                                Optional('total_links'): int,
                                                Optional('area_instance'): int,
                                                Optional('link_fragments'): 
                                                    {Any(): 
                                                        {'link_instance': int,
                                                        'network_type': str,
                                                        'link_id': str,
                                                        'interface_address': str,
                                                        'te_admin_metric': int,
                                                        'maximum_bandwidth': int,
                                                        'maximum_reservable_bandwidth': int,
                                                        'total_priority': int,
                                                        'out_interface_id': int,
                                                        'affinity_bit': int,
                                                        'total_extended_admin_group': int,
                                                        'unreserved_bandwidths' : 
                                                            {Any(): 
                                                                {'priority': int,
                                                                'unreserved_bandwidth': int,
                                                                },
                                                            },
                                                        'extended_admin_groups': 
                                                            {Any(): 
                                                                {'value': int,
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }


# =============================================
# Parser for 'show ospf mpls traffic-eng links'
# =============================================
class ShowOspfMplsTrafficEngLinks(ShowOspfMplsTrafficEngLinksSchema):

    ''' Parser for "show ospf mpls traffic-eng links" '''

    def cli(self):

        # Execute command on device
        out = self.device.execute('show ospf mpls traffic-eng links')
        
        # Init vars
        ret_dict = {}
        af = 'ipv4'

        for line in out.splitlines():
            line = line.strip()

            # OSPF Router with ID (3.3.3.3) (Process ID 1)
            p1 = re.compile(r'^OSPF +Router +with +ID +\((?P<router_id>(\S+))\)'
                             ' +\(Process +ID +(?P<instance>(\S+))\)$')
            m = p1.match(line)
            if m:
                vrf = 'default'
                instance = str(m.groupdict()['instance'])
                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}
                if 'address_family' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['address_family'] = {}
                if af not in ret_dict['vrf'][vrf]['address_family']:
                    ret_dict['vrf'][vrf]['address_family'][af] = {}
                if 'instance' not in ret_dict['vrf'][vrf]['address_family'][af]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance'] = {}
                if instance not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance] = {}
                if 'mpls' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['mpls'] = {}
                if 'te' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['mpls']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['mpls']['te'] = {}
                # Set keys
                ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                    [instance]['mpls']['te']['router_id'] = \
                        str(m.groupdict()['router_id'])
                continue

            # Area 0 has 2 MPLS TE links. Area instance is 2.
            p2_1 = re.compile(r'^Area +(?P<area>(\S+)) +has'
                               ' +(?P<total_links>(\d+)) +MPLS +TE links\.'
                               ' +Area +instance +is +(?P<instance>(\d+))\.$')
            m = p2_1.match(line)
            if m:
                area = str(IPAddress(str(m.groupdict()['area'])))
                if 'areas' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'] = {}
                if area not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area] = {}
                if 'mpls' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area]['mpls'] = {}
                if 'te' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area]['mpls']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area]['mpls']['te'] = {}

                # Set sub_dict
                sub_dict = ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area]['mpls']['te']

                # Set values
                sub_dict['enable'] = True
                sub_dict['total_links'] = int(m.groupdict()['total_links'])
                sub_dict['area_instance'] = int(m.groupdict()['instance'])
                continue

            # Area 1 MPLS TE not initialized
            p2_2 = re.compile(r'^Area +(?P<area>(\d+)) +MPLS +TE +not'
                               ' +initialized$')
            m = p2_2.match(line)
            if m:
                area = str(IPAddress(str(m.groupdict()['area'])))
                if 'areas' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'] = {}
                if area not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area] = {}
                if 'mpls' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area]['mpls'] = {}
                if 'te' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area]['mpls']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area]['mpls']['te'] = {}

                # Set sub_dict
                sub_dict = ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area]['mpls']['te']

                # Set values
                sub_dict['enable'] = False
                continue

            # Link is associated with fragment 1. Link instance is 2
            p3 = re.compile(r'^Link +is +associated +with +fragment'
                             ' +(?P<fragment>(\d+))\. +Link +instance +is'
                             ' +(?P<link_instance>(\d+))$')
            m = p3.match(line)
            if m:
                fragment = int(m.groupdict()['fragment'])
                if 'link_fragments' not in sub_dict:
                    sub_dict['link_fragments'] = {}
                if fragment not in sub_dict['link_fragments']:
                    sub_dict['link_fragments'][fragment] = {}

                # Create link_dict
                link_dict = sub_dict['link_fragments'][fragment]

                # Set values
                link_dict['link_instance'] = int(m.groupdict()['link_instance'])
                continue

            # Link connected to Broadcast network
            p4 = re.compile(r'^Link +connected +to +(?P<net>(\S+)) +network$')
            m = p4.match(line)
            if m:
                link_dict['network_type'] = str(m.groupdict()['net']).lower()
                continue

            # Link ID : 10.3.4.4
            p5 = re.compile(r'^Link +ID *: +(?P<link_id>(\S+))$')
            m = p5.match(line)
            if m:
                link_dict['link_id'] = str(m.groupdict()['link_id'])
                continue

            # Interface Address : 10.3.4.3
            p6 = re.compile(r'^Interface +Address *: +(?P<address>(\S+))$')
            m = p6.match(line)
            if m:
                link_dict['interface_address'] = str(m.groupdict()['address'])
                continue

            # Admin Metric : TE: 1
            p7 = re.compile(r'^Admin +Metric *: +TE *: +(?P<metric>(\d+))$')
            m = p7.match(line)
            if m:
                link_dict['te_admin_metric'] = int(m.groupdict()['metric'])
                continue

            # (all bandwidths in bytes/sec)

            # Maximum bandwidth : 125000000
            p8 = re.compile(r'^Maximum +bandwidth *: +(?P<max_band>(\d+))$')
            m = p8.match(line)
            if m:
                link_dict['maximum_bandwidth'] = int(m.groupdict()['max_band'])
                continue

            # Maximum global pool reservable bandwidth : 93750000
            p9 = re.compile(r'^Maximum +global +pool +reservable +bandwidth *:'
                             ' +(?P<max_reserve_band>(\d+))$')
            m = p9.match(line)
            if m:
                link_dict['maximum_reservable_bandwidth'] = \
                    int(m.groupdict()['max_reserve_band'])
                continue

            # Number of Priority : 8
            p9 = re.compile(r'^Number +of +Priority *: +(?P<priority>(\d+))$')
            m = p9.match(line)
            if m:
                link_dict['total_priority'] = int(m.groupdict()['priority'])
                continue

            # Global pool unreserved BW 

            # Priority 0 :             93750000  Priority 1 :           93750000
            # Priority 2 :             93750000  Priority 3 :           93750000
            # Priority 4 :             93750000  Priority 5 :           93750000
            # Priority 6 :             93750000  Priority 7 :           93750000
            p10 = re.compile(r'^Priority +(?P<priority1>(\d+)) *: +(?P<band1>(\d+))'
                              ' *Priority +(?P<priority2>(\d+)) *: +(?P<band2>(\d+))$')
            m = p10.match(line)
            if m:
                priority1 = str(m.groupdict()['priority1'])
                priority2 = str(m.groupdict()['priority2'])
                band1 = str(m.groupdict()['band1'])
                band2 = str(m.groupdict()['band2'])
                value1 = priority1 + ' ' + band1
                value2 = priority2 + ' ' + band2
                if 'unreserved_bandwidths' not in link_dict:
                    link_dict['unreserved_bandwidths'] = {}
                # Set keys for first parsed value
                if value1 not in link_dict['unreserved_bandwidths']:
                    link_dict['unreserved_bandwidths'][value1] = {}
                link_dict['unreserved_bandwidths'][value1]['priority'] = int(priority1)
                link_dict['unreserved_bandwidths'][value1]['unreserved_bandwidth'] = int(band1)
                # Set keys for second parsed value
                if value2 not in link_dict['unreserved_bandwidths']:
                    link_dict['unreserved_bandwidths'][value2] = {}
                link_dict['unreserved_bandwidths'][value2]['priority'] = int(priority2)
                link_dict['unreserved_bandwidths'][value2]['unreserved_bandwidth'] = int(band2)
                continue

            # Out Interface ID : 4
            p11 = re.compile(r'^Out +Interface +ID *: +(?P<out_id>(\d+))$')
            m = p11.match(line)
            if m:
                link_dict['out_interface_id'] = int(m.groupdict()['out_id'])
                continue

            # Affinity Bit : 0
            p12 = re.compile(r'^Affinity +Bit *: +(?P<affinity>(\d+))$')
            m = p12.match(line)
            if m:
                link_dict['affinity_bit'] = int(m.groupdict()['affinity'])
                continue

            # Extended Admin Group : 8
            p13 = re.compile(r'^Extended +Admin +Group *: +(?P<eag>(\d+))$')
            m = p13.match(line)
            if m:
                link_dict['total_extended_admin_group'] = int(m.groupdict()['eag'])
                continue

            # EAG[0]: 0
            # EAG[1]: 0
            p14 = re.compile(r'^EAG\[(?P<group_num>(\d+))\]: +(?P<value>(\d+))$')
            m = p14.match(line)
            if m:
                group_num = int(m.groupdict()['group_num'])
                if 'extended_admin_groups' not in link_dict:
                    link_dict['extended_admin_groups'] = {}
                if group_num not in link_dict['extended_admin_groups']:
                    link_dict['extended_admin_groups'][group_num] = {}
                link_dict['extended_admin_groups'][group_num]['value'] = \
                    int(m.groupdict()['value'])
                continue

        return ret_dict