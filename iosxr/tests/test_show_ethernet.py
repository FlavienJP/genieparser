#!/bin/env python

import unittest
from unittest.mock import Mock

import xml.etree.ElementTree as ET

from ats.topology import Device

from genie.ops.base import Context

from metaparser.util.exceptions import SchemaEmptyParserError

from parser.iosxr.show_ethernet import ShowEthernetTrunkDetail, \
                                                  ShowEthernetTags


class test_show_ethernet_trunk_detail(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'interface': 
    {'Gi0/0/0/1': 
        {'dot1q_tunneling_ethertype': '0x9100'}, 
     'Gi0/0/0/0': 
        {}
    }
}

    golden_output = {'execute.return_value': '''
 GigabitEthernet0/0/0/0 is up
   Trunk:
     Outer VLAN tag format is 802.1Q
     Untagged frames processed on GigabitEthernet0/0/0/0
     No native VLAN Id
     MAC filtering: None
   Sub-interfaces: 7
     By type:
       L2: 0
       L3: 7
     By state:
       Up: 7
       Down: 0
       Admin-down: 0
 GigabitEthernet0/0/0/1 is up
   Trunk:
     Outer VLAN tag format is 802.1Q
   Dot1Q Tunneling Ethertype is 0x9100
     Untagged frames processed on GigabitEthernet0/0/0/1
     No native VLAN Id
     MAC filtering: None
   Sub-interfaces: 1
     By type:
       L2: 0
       L3: 1
     By state:
       Up: 1
       Down: 0
       Admin-down: 0
'''}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        intf_obj = ShowEthernetTrunkDetail(device=self.device)
        parsed_output = intf_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        intf_obj = ShowEthernetTrunkDetail(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = intf_obj.parse()


class test_show_ethernet_tags(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'interface': 
    {'Gi0/0/0/1': 
        {'sub_interface': 
            {'Gi0/0/0/1.501': 
                {'vlan_id': {'501': {'layer': 'L3', 'mtu': '1518', 'status': 'Up', 'outer_encapsulation_type': 'dot1Q'}}}}}, 
     'Gi0/0/0/0': 
        {'sub_interface': 
            {'Gi0/0/0/0.503': 
                {'vlan_id': 
                    {'4': 
                        {'layer': 'L3', 'mtu': '1518', 'status': 'Up', 'outer_encapsulation_type': 'dot1Q'}}}, 
             'Gi0/0/0/0.504': 
                {'vlan_id': 
                    {'504': 
                        {'layer': 'L3', 'mtu': '1518', 'status': 'Up', 'outer_encapsulation_type': 'dot1Q'}}}, 
             'Gi0/0/0/0.501': 
                {'vlan_id': 
                    {'4': 
                        {'outer_encapsulation_type': 'dot1ad', 'inner_encapsulation_vlan_id': '5', 'status': 'Up', 'inner_encapsulation_type': 'dot1Q', 'mtu': '1522', 'layer': 'L3'}}}, 
             'Gi0/0/0/0.511': 
                {'vlan_id': 
                    {'511': 
                        {'layer': 'L3', 'mtu': '1518', 'status': 'Up', 'outer_encapsulation_type': 'dot1Q'}}}, 
             'Gi0/0/0/0.505': 
                {'vlan_id': 
                    {'505': 
                        {'layer': 'L3', 'mtu': '1518', 'status': 'Up', 'outer_encapsulation_type': 'dot1Q'}}}, 
             'Gi0/0/0/0.510': 
                {'vlan_id': 
                    {'510': 
                        {'layer': 'L3', 'mtu': '1518', 'status': 'Up', 'outer_encapsulation_type': 'dot1Q'}}}, 
             'Gi0/0/0/0.502': 
                {'vlan_id': 
                    {'502': 
                        {'layer': 'L3', 'mtu': '1518', 'status': 'Up', 'outer_encapsulation_type': 'dot1Q'}}}}
        }
    }
}

    golden_output = {'execute.return_value': '''
St:    AD - Administratively Down, Dn - Down, Up - Up
Ly:    L2 - Switched layer 2 service, L3 = Terminated layer 3 service,
Xtra   C - Match on Cos, E  - Match on Ethertype, M - Match on source MAC
-,+:   Ingress rewrite operation; number of tags to pop and push respectively

Interface               St  MTU  Ly Outer            Inner            Xtra -,+
Gi0/0/0/0.501           Up  1522 L3 .1ad:4           .1Q:5            -    2 0
Gi0/0/0/0.502           Up  1518 L3 .1Q:502          -                -    1 0
Gi0/0/0/0.503           Up  1518 L3 .1Q:4            -                -    1 0
Gi0/0/0/0.504           Up  1518 L3 .1Q:504          -                -    1 0
Gi0/0/0/0.505           Up  1518 L3 .1Q:505          -                -    1 0
Gi0/0/0/0.510           Up  1518 L3 .1Q:510          -                -    1 0
Gi0/0/0/0.511           Up  1518 L3 .1Q:511          -                -    1 0
Gi0/0/0/1.501           Up  1518 L3 .1Q:501          -                -    1 0
'''}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        intf_obj = ShowEthernetTags(device=self.device)
        parsed_output = intf_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        intf_obj = ShowEthernetTags(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = intf_obj.parse()

class test_show_ethernet_tags_yang(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'interface': {'GigabitEthernet0/0/0/0': {'sub_interface': {'GigabitEthernet0/0/0/0.501': {'vlan_id': {'2': {'inner_encapsulation_type': 'dot1q',
                                                                                                             'inner_encapsulation_vlan_id': '5',
                                                                                                             'mtu': '1522',
                                                                                                             'outer_encapsulation_type': 'dot1q'}}}}}}}

    class etree_holder():
      def __init__(self):
        self.data = ET.fromstring('''
         <data>
          <interfaces xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-pfi-im-cmd-oper">
           <interface-xr>
            <interface>
             <interface-name>GigabitEthernet0/0/0/0</interface-name>
             <interface-handle>GigabitEthernet0/0/0/0</interface-handle>
             <interface-type>IFT_GETHERNET</interface-type>
             <hardware-type-string>GigabitEthernet</hardware-type-string>
             <state>im-state-up</state>
             <line-state>im-state-up</line-state>
             <encapsulation>ether</encapsulation>
             <encapsulation-type-string>ARPA</encapsulation-type-string>
             <mtu>1514</mtu>
             <is-l2-transport-enabled>false</is-l2-transport-enabled>
             <state-transition-count>1</state-transition-count>
             <last-state-transition-time>1100222</last-state-transition-time>
             <is-dampening-enabled>false</is-dampening-enabled>
             <speed>1000000</speed>
             <duplexity>im-attr-duplex-full</duplexity>
             <media-type>im-attr-media-other</media-type>
             <link-type>im-attr-link-type-force</link-type>
             <in-flow-control>im-attr-flow-control-off</in-flow-control>
             <out-flow-control>im-attr-flow-control-off</out-flow-control>
             <mac-address>
              <address>52:54:00:a0:af:6d</address>
             </mac-address>
             <burned-in-address>
              <address>52:54:00:a0:af:6d</address>
             </burned-in-address>
             <carrier-delay>
              <carrier-delay-up>10</carrier-delay-up>
              <carrier-delay-down>0</carrier-delay-down>
             </carrier-delay>
             <bandwidth>1000000</bandwidth>
             <max-bandwidth>1000000</max-bandwidth>
             <is-l2-looped>false</is-l2-looped>
             <description></description>
             <data-rates>
              <input-data-rate>0</input-data-rate>
              <input-packet-rate>0</input-packet-rate>
              <output-data-rate>0</output-data-rate>
              <output-packet-rate>0</output-packet-rate>
              <peak-input-data-rate>0</peak-input-data-rate>
              <peak-input-packet-rate>0</peak-input-packet-rate>
              <peak-output-data-rate>0</peak-output-data-rate>
              <peak-output-packet-rate>0</peak-output-packet-rate>
              <bandwidth>1000000</bandwidth>
              <load-interval>9</load-interval>
              <output-load>0</output-load>
              <input-load>0</input-load>
              <reliability>255</reliability>
             </data-rates>
             <interface-statistics>
              <stats-type>full</stats-type>
              <full-interface-stats>
               <packets-received>0</packets-received>
               <bytes-received>0</bytes-received>
               <packets-sent>0</packets-sent>
               <bytes-sent>0</bytes-sent>
               <multicast-packets-received>0</multicast-packets-received>
               <broadcast-packets-received>0</broadcast-packets-received>
               <multicast-packets-sent>0</multicast-packets-sent>
               <broadcast-packets-sent>0</broadcast-packets-sent>
               <output-drops>0</output-drops>
               <output-queue-drops>0</output-queue-drops>
               <input-drops>0</input-drops>
               <input-queue-drops>0</input-queue-drops>
               <runt-packets-received>0</runt-packets-received>
               <giant-packets-received>0</giant-packets-received>
               <throttled-packets-received>0</throttled-packets-received>
               <parity-packets-received>0</parity-packets-received>
               <unknown-protocol-packets-received>0</unknown-protocol-packets-received>
               <input-errors>0</input-errors>
               <crc-errors>0</crc-errors>
               <input-overruns>0</input-overruns>
               <framing-errors-received>0</framing-errors-received>
               <input-ignored-packets>0</input-ignored-packets>
               <input-aborts>0</input-aborts>
               <output-errors>0</output-errors>
               <output-underruns>0</output-underruns>
               <output-buffer-failures>0</output-buffer-failures>
               <output-buffers-swapped-out>0</output-buffers-swapped-out>
               <applique>0</applique>
               <resets>0</resets>
               <carrier-transitions>1</carrier-transitions>
               <availability-flag>0</availability-flag>
               <last-data-time>1490888108</last-data-time>
               <seconds-since-last-clear-counters>0</seconds-since-last-clear-counters>
               <last-discontinuity-time>1489787869</last-discontinuity-time>
               <seconds-since-packet-received>4294967295</seconds-since-packet-received>
               <seconds-since-packet-sent>4294967295</seconds-since-packet-sent>
              </full-interface-stats>
             </interface-statistics>
             <if-index>0</if-index>
            </interface>
            <interface>
             <interface-name>GigabitEthernet0/0/0/0.501</interface-name>
             <interface-handle>GigabitEthernet0/0/0/0.501</interface-handle>
             <interface-type>IFT_VLAN_SUBIF</interface-type>
             <hardware-type-string>VLAN sub-interface(s)</hardware-type-string>
             <state>im-state-up</state>
             <line-state>im-state-up</line-state>
             <encapsulation>dot1q</encapsulation>
             <encapsulation-type-string>802.1Q</encapsulation-type-string>
             <mtu>1522</mtu>
             <is-l2-transport-enabled>false</is-l2-transport-enabled>
             <state-transition-count>1</state-transition-count>
             <last-state-transition-time>1100222</last-state-transition-time>
             <is-dampening-enabled>false</is-dampening-enabled>
             <speed>1000000</speed>
             <mac-address>
              <address>52:54:00:a0:af:6d</address>
             </mac-address>
             <carrier-delay>
              <carrier-delay-up>0</carrier-delay-up>
              <carrier-delay-down>0</carrier-delay-down>
             </carrier-delay>
             <bandwidth>1000000</bandwidth>
             <max-bandwidth>1000000</max-bandwidth>
             <is-l2-looped>false</is-l2-looped>
             <parent-interface-name>GigabitEthernet0/0/0/0</parent-interface-name>
             <description></description>
             <encapsulation-information>
              <encapsulation-type>vlan</encapsulation-type>
              <dot1q-information>
               <encapsulation-details>
                <vlan-encapsulation>qinq</vlan-encapsulation>
                <stack>
                 <outer-tag>2</outer-tag>
                 <second-tag>5</second-tag>
                </stack>
               </encapsulation-details>
              </dot1q-information>
             </encapsulation-information>
             <data-rates>
              <input-data-rate>0</input-data-rate>
              <input-packet-rate>0</input-packet-rate>
              <output-data-rate>0</output-data-rate>
              <output-packet-rate>0</output-packet-rate>
              <peak-input-data-rate>0</peak-input-data-rate>
              <peak-input-packet-rate>0</peak-input-packet-rate>
              <peak-output-data-rate>0</peak-output-data-rate>
              <peak-output-packet-rate>0</peak-output-packet-rate>
              <bandwidth>1000000</bandwidth>
              <load-interval>9</load-interval>
              <output-load>0</output-load>
              <input-load>0</input-load>
              <reliability>255</reliability>
             </data-rates>
             <interface-statistics>
              <stats-type>full</stats-type>
              <full-interface-stats>
               <packets-received>0</packets-received>
               <bytes-received>0</bytes-received>
               <packets-sent>0</packets-sent>
               <bytes-sent>0</bytes-sent>
               <multicast-packets-received>0</multicast-packets-received>
               <broadcast-packets-received>0</broadcast-packets-received>
               <multicast-packets-sent>0</multicast-packets-sent>
               <broadcast-packets-sent>0</broadcast-packets-sent>
               <output-drops>0</output-drops>
               <output-queue-drops>0</output-queue-drops>
               <input-drops>0</input-drops>
               <input-queue-drops>0</input-queue-drops>
               <runt-packets-received>0</runt-packets-received>
               <giant-packets-received>0</giant-packets-received>
               <throttled-packets-received>0</throttled-packets-received>
               <parity-packets-received>0</parity-packets-received>
               <unknown-protocol-packets-received>0</unknown-protocol-packets-received>
               <input-errors>0</input-errors>
               <crc-errors>0</crc-errors>
               <input-overruns>0</input-overruns>
               <framing-errors-received>0</framing-errors-received>
               <input-ignored-packets>0</input-ignored-packets>
               <input-aborts>0</input-aborts>
               <output-errors>0</output-errors>
               <output-underruns>0</output-underruns>
               <output-buffer-failures>0</output-buffer-failures>
               <output-buffers-swapped-out>0</output-buffers-swapped-out>
               <applique>0</applique>
               <resets>0</resets>
               <carrier-transitions>0</carrier-transitions>
               <availability-flag>0</availability-flag>
               <last-data-time>1490888108</last-data-time>
               <seconds-since-last-clear-counters>0</seconds-since-last-clear-counters>
               <last-discontinuity-time>1489787915</last-discontinuity-time>
               <seconds-since-packet-received>4294967295</seconds-since-packet-received>
               <seconds-since-packet-sent>4294967295</seconds-since-packet-sent>
              </full-interface-stats>
             </interface-statistics>
             <if-index>0</if-index>
            </interface>
            <interface>
             <interface-name>GigabitEthernet0/0/0/1</interface-name>
             <interface-handle>GigabitEthernet0/0/0/1</interface-handle>
             <interface-type>IFT_GETHERNET</interface-type>
             <hardware-type-string>GigabitEthernet</hardware-type-string>
             <state>im-state-admin-down</state>
             <line-state>im-state-admin-down</line-state>
             <encapsulation>ether</encapsulation>
             <encapsulation-type-string>ARPA</encapsulation-type-string>
             <mtu>1514</mtu>
             <is-l2-transport-enabled>false</is-l2-transport-enabled>
             <state-transition-count>0</state-transition-count>
             <last-state-transition-time>1100377</last-state-transition-time>
             <is-dampening-enabled>false</is-dampening-enabled>
             <speed>1000000</speed>
             <duplexity>im-attr-duplex-full</duplexity>
             <media-type>im-attr-media-other</media-type>
             <link-type>im-attr-link-type-force</link-type>
             <in-flow-control>im-attr-flow-control-off</in-flow-control>
             <out-flow-control>im-attr-flow-control-off</out-flow-control>
             <mac-address>
              <address>52:54:00:c0:73:42</address>
             </mac-address>
             <burned-in-address>
              <address>52:54:00:c0:73:42</address>
             </burned-in-address>
             <carrier-delay>
              <carrier-delay-up>10</carrier-delay-up>
              <carrier-delay-down>0</carrier-delay-down>
             </carrier-delay>
             <bandwidth>1000000</bandwidth>
             <max-bandwidth>1000000</max-bandwidth>
             <is-l2-looped>false</is-l2-looped>
             <description></description>
             <data-rates>
              <input-data-rate>0</input-data-rate>
              <input-packet-rate>0</input-packet-rate>
              <output-data-rate>0</output-data-rate>
              <output-packet-rate>0</output-packet-rate>
              <peak-input-data-rate>0</peak-input-data-rate>
              <peak-input-packet-rate>0</peak-input-packet-rate>
              <peak-output-data-rate>0</peak-output-data-rate>
              <peak-output-packet-rate>0</peak-output-packet-rate>
              <bandwidth>1000000</bandwidth>
              <load-interval>9</load-interval>
              <output-load>0</output-load>
              <input-load>0</input-load>
              <reliability>255</reliability>
             </data-rates>
             <interface-statistics>
              <stats-type>full</stats-type>
              <full-interface-stats>
               <packets-received>0</packets-received>
               <bytes-received>0</bytes-received>
               <packets-sent>0</packets-sent>
               <bytes-sent>0</bytes-sent>
               <multicast-packets-received>0</multicast-packets-received>
               <broadcast-packets-received>0</broadcast-packets-received>
               <multicast-packets-sent>0</multicast-packets-sent>
               <broadcast-packets-sent>0</broadcast-packets-sent>
               <output-drops>0</output-drops>
               <output-queue-drops>0</output-queue-drops>
               <input-drops>0</input-drops>
               <input-queue-drops>0</input-queue-drops>
               <runt-packets-received>0</runt-packets-received>
               <giant-packets-received>0</giant-packets-received>
               <throttled-packets-received>0</throttled-packets-received>
               <parity-packets-received>0</parity-packets-received>
               <unknown-protocol-packets-received>0</unknown-protocol-packets-received>
               <input-errors>0</input-errors>
               <crc-errors>0</crc-errors>
               <input-overruns>0</input-overruns>
               <framing-errors-received>0</framing-errors-received>
               <input-ignored-packets>0</input-ignored-packets>
               <input-aborts>0</input-aborts>
               <output-errors>0</output-errors>
               <output-underruns>0</output-underruns>
               <output-buffer-failures>0</output-buffer-failures>
               <output-buffers-swapped-out>0</output-buffers-swapped-out>
               <applique>0</applique>
               <resets>0</resets>
               <carrier-transitions>0</carrier-transitions>
               <availability-flag>0</availability-flag>
               <last-data-time>1490888108</last-data-time>
               <seconds-since-last-clear-counters>0</seconds-since-last-clear-counters>
               <last-discontinuity-time>1489787869</last-discontinuity-time>
               <seconds-since-packet-received>4294967295</seconds-since-packet-received>
               <seconds-since-packet-sent>4294967295</seconds-since-packet-sent>
              </full-interface-stats>
             </interface-statistics>
             <if-index>0</if-index>
            </interface>
            <interface>
             <interface-name>GigabitEthernet0/0/0/2</interface-name>
             <interface-handle>GigabitEthernet0/0/0/2</interface-handle>
             <interface-type>IFT_GETHERNET</interface-type>
             <hardware-type-string>GigabitEthernet</hardware-type-string>
             <state>im-state-admin-down</state>
             <line-state>im-state-admin-down</line-state>
             <encapsulation>ether</encapsulation>
             <encapsulation-type-string>ARPA</encapsulation-type-string>
             <mtu>1514</mtu>
             <is-l2-transport-enabled>false</is-l2-transport-enabled>
             <state-transition-count>0</state-transition-count>
             <last-state-transition-time>1100377</last-state-transition-time>
             <is-dampening-enabled>false</is-dampening-enabled>
             <speed>1000000</speed>
             <duplexity>im-attr-duplex-full</duplexity>
             <media-type>im-attr-media-other</media-type>
             <link-type>im-attr-link-type-force</link-type>
             <in-flow-control>im-attr-flow-control-off</in-flow-control>
             <out-flow-control>im-attr-flow-control-off</out-flow-control>
             <mac-address>
              <address>52:54:00:ac:93:a1</address>
             </mac-address>
             <burned-in-address>
              <address>52:54:00:ac:93:a1</address>
             </burned-in-address>
             <carrier-delay>
              <carrier-delay-up>10</carrier-delay-up>
              <carrier-delay-down>0</carrier-delay-down>
             </carrier-delay>
             <bandwidth>1000000</bandwidth>
             <max-bandwidth>1000000</max-bandwidth>
             <is-l2-looped>false</is-l2-looped>
             <description></description>
             <data-rates>
              <input-data-rate>0</input-data-rate>
              <input-packet-rate>0</input-packet-rate>
              <output-data-rate>0</output-data-rate>
              <output-packet-rate>0</output-packet-rate>
              <peak-input-data-rate>0</peak-input-data-rate>
              <peak-input-packet-rate>0</peak-input-packet-rate>
              <peak-output-data-rate>0</peak-output-data-rate>
              <peak-output-packet-rate>0</peak-output-packet-rate>
              <bandwidth>1000000</bandwidth>
              <load-interval>9</load-interval>
              <output-load>0</output-load>
              <input-load>0</input-load>
              <reliability>255</reliability>
             </data-rates>
             <interface-statistics>
              <stats-type>full</stats-type>
              <full-interface-stats>
               <packets-received>0</packets-received>
               <bytes-received>0</bytes-received>
               <packets-sent>0</packets-sent>
               <bytes-sent>0</bytes-sent>
               <multicast-packets-received>0</multicast-packets-received>
               <broadcast-packets-received>0</broadcast-packets-received>
               <multicast-packets-sent>0</multicast-packets-sent>
               <broadcast-packets-sent>0</broadcast-packets-sent>
               <output-drops>0</output-drops>
               <output-queue-drops>0</output-queue-drops>
               <input-drops>0</input-drops>
               <input-queue-drops>0</input-queue-drops>
               <runt-packets-received>0</runt-packets-received>
               <giant-packets-received>0</giant-packets-received>
               <throttled-packets-received>0</throttled-packets-received>
               <parity-packets-received>0</parity-packets-received>
               <unknown-protocol-packets-received>0</unknown-protocol-packets-received>
               <input-errors>0</input-errors>
               <crc-errors>0</crc-errors>
               <input-overruns>0</input-overruns>
               <framing-errors-received>0</framing-errors-received>
               <input-ignored-packets>0</input-ignored-packets>
               <input-aborts>0</input-aborts>
               <output-errors>0</output-errors>
               <output-underruns>0</output-underruns>
               <output-buffer-failures>0</output-buffer-failures>
               <output-buffers-swapped-out>0</output-buffers-swapped-out>
               <applique>0</applique>
               <resets>0</resets>
               <carrier-transitions>0</carrier-transitions>
               <availability-flag>0</availability-flag>
               <last-data-time>1490888108</last-data-time>
               <seconds-since-last-clear-counters>0</seconds-since-last-clear-counters>
               <last-discontinuity-time>1489787869</last-discontinuity-time>
               <seconds-since-packet-received>4294967295</seconds-since-packet-received>
               <seconds-since-packet-sent>4294967295</seconds-since-packet-sent>
              </full-interface-stats>
             </interface-statistics>
             <if-index>0</if-index>
            </interface>
            <interface>
             <interface-name>GigabitEthernet0/0/0/3</interface-name>
             <interface-handle>GigabitEthernet0/0/0/3</interface-handle>
             <interface-type>IFT_GETHERNET</interface-type>
             <hardware-type-string>GigabitEthernet</hardware-type-string>
             <state>im-state-admin-down</state>
             <line-state>im-state-admin-down</line-state>
             <encapsulation>ether</encapsulation>
             <encapsulation-type-string>ARPA</encapsulation-type-string>
             <mtu>1514</mtu>
             <is-l2-transport-enabled>false</is-l2-transport-enabled>
             <state-transition-count>0</state-transition-count>
             <last-state-transition-time>1100377</last-state-transition-time>
             <is-dampening-enabled>false</is-dampening-enabled>
             <speed>1000000</speed>
             <duplexity>im-attr-duplex-full</duplexity>
             <media-type>im-attr-media-other</media-type>
             <link-type>im-attr-link-type-force</link-type>
             <in-flow-control>im-attr-flow-control-off</in-flow-control>
             <out-flow-control>im-attr-flow-control-off</out-flow-control>
             <mac-address>
              <address>52:54:00:a4:55:b9</address>
             </mac-address>
             <burned-in-address>
              <address>52:54:00:a4:55:b9</address>
             </burned-in-address>
             <carrier-delay>
              <carrier-delay-up>10</carrier-delay-up>
              <carrier-delay-down>0</carrier-delay-down>
             </carrier-delay>
             <bandwidth>1000000</bandwidth>
             <max-bandwidth>1000000</max-bandwidth>
             <is-l2-looped>false</is-l2-looped>
             <description></description>
             <data-rates>
              <input-data-rate>0</input-data-rate>
              <input-packet-rate>0</input-packet-rate>
              <output-data-rate>0</output-data-rate>
              <output-packet-rate>0</output-packet-rate>
              <peak-input-data-rate>0</peak-input-data-rate>
              <peak-input-packet-rate>0</peak-input-packet-rate>
              <peak-output-data-rate>0</peak-output-data-rate>
              <peak-output-packet-rate>0</peak-output-packet-rate>
              <bandwidth>1000000</bandwidth>
              <load-interval>9</load-interval>
              <output-load>0</output-load>
              <input-load>0</input-load>
              <reliability>255</reliability>
             </data-rates>
             <interface-statistics>
              <stats-type>full</stats-type>
              <full-interface-stats>
               <packets-received>0</packets-received>
               <bytes-received>0</bytes-received>
               <packets-sent>0</packets-sent>
               <bytes-sent>0</bytes-sent>
               <multicast-packets-received>0</multicast-packets-received>
               <broadcast-packets-received>0</broadcast-packets-received>
               <multicast-packets-sent>0</multicast-packets-sent>
               <broadcast-packets-sent>0</broadcast-packets-sent>
               <output-drops>0</output-drops>
               <output-queue-drops>0</output-queue-drops>
               <input-drops>0</input-drops>
               <input-queue-drops>0</input-queue-drops>
               <runt-packets-received>0</runt-packets-received>
               <giant-packets-received>0</giant-packets-received>
               <throttled-packets-received>0</throttled-packets-received>
               <parity-packets-received>0</parity-packets-received>
               <unknown-protocol-packets-received>0</unknown-protocol-packets-received>
               <input-errors>0</input-errors>
               <crc-errors>0</crc-errors>
               <input-overruns>0</input-overruns>
               <framing-errors-received>0</framing-errors-received>
               <input-ignored-packets>0</input-ignored-packets>
               <input-aborts>0</input-aborts>
               <output-errors>0</output-errors>
               <output-underruns>0</output-underruns>
               <output-buffer-failures>0</output-buffer-failures>
               <output-buffers-swapped-out>0</output-buffers-swapped-out>
               <applique>0</applique>
               <resets>0</resets>
               <carrier-transitions>0</carrier-transitions>
               <availability-flag>0</availability-flag>
               <last-data-time>1490888108</last-data-time>
               <seconds-since-last-clear-counters>0</seconds-since-last-clear-counters>
               <last-discontinuity-time>1489787869</last-discontinuity-time>
               <seconds-since-packet-received>4294967295</seconds-since-packet-received>
               <seconds-since-packet-sent>4294967295</seconds-since-packet-sent>
              </full-interface-stats>
             </interface-statistics>
             <if-index>0</if-index>
            </interface>
            <interface>
             <interface-name>GigabitEthernet0/0/0/4</interface-name>
             <interface-handle>GigabitEthernet0/0/0/4</interface-handle>
             <interface-type>IFT_GETHERNET</interface-type>
             <hardware-type-string>GigabitEthernet</hardware-type-string>
             <state>im-state-admin-down</state>
             <line-state>im-state-admin-down</line-state>
             <encapsulation>ether</encapsulation>
             <encapsulation-type-string>ARPA</encapsulation-type-string>
             <mtu>1514</mtu>
             <is-l2-transport-enabled>false</is-l2-transport-enabled>
             <state-transition-count>0</state-transition-count>
             <last-state-transition-time>1100377</last-state-transition-time>
             <is-dampening-enabled>false</is-dampening-enabled>
             <speed>1000000</speed>
             <duplexity>im-attr-duplex-full</duplexity>
             <media-type>im-attr-media-other</media-type>
             <link-type>im-attr-link-type-force</link-type>
             <in-flow-control>im-attr-flow-control-off</in-flow-control>
             <out-flow-control>im-attr-flow-control-off</out-flow-control>
             <mac-address>
              <address>52:54:00:db:47:8f</address>
             </mac-address>
             <burned-in-address>
              <address>52:54:00:db:47:8f</address>
             </burned-in-address>
             <carrier-delay>
              <carrier-delay-up>10</carrier-delay-up>
              <carrier-delay-down>0</carrier-delay-down>
             </carrier-delay>
             <bandwidth>1000000</bandwidth>
             <max-bandwidth>1000000</max-bandwidth>
             <is-l2-looped>false</is-l2-looped>
             <description></description>
             <data-rates>
              <input-data-rate>0</input-data-rate>
              <input-packet-rate>0</input-packet-rate>
              <output-data-rate>0</output-data-rate>
              <output-packet-rate>0</output-packet-rate>
              <peak-input-data-rate>0</peak-input-data-rate>
              <peak-input-packet-rate>0</peak-input-packet-rate>
              <peak-output-data-rate>0</peak-output-data-rate>
              <peak-output-packet-rate>0</peak-output-packet-rate>
              <bandwidth>1000000</bandwidth>
              <load-interval>9</load-interval>
              <output-load>0</output-load>
              <input-load>0</input-load>
              <reliability>255</reliability>
             </data-rates>
             <interface-statistics>
              <stats-type>full</stats-type>
              <full-interface-stats>
               <packets-received>0</packets-received>
               <bytes-received>0</bytes-received>
               <packets-sent>0</packets-sent>
               <bytes-sent>0</bytes-sent>
               <multicast-packets-received>0</multicast-packets-received>
               <broadcast-packets-received>0</broadcast-packets-received>
               <multicast-packets-sent>0</multicast-packets-sent>
               <broadcast-packets-sent>0</broadcast-packets-sent>
               <output-drops>0</output-drops>
               <output-queue-drops>0</output-queue-drops>
               <input-drops>0</input-drops>
               <input-queue-drops>0</input-queue-drops>
               <runt-packets-received>0</runt-packets-received>
               <giant-packets-received>0</giant-packets-received>
               <throttled-packets-received>0</throttled-packets-received>
               <parity-packets-received>0</parity-packets-received>
               <unknown-protocol-packets-received>0</unknown-protocol-packets-received>
               <input-errors>0</input-errors>
               <crc-errors>0</crc-errors>
               <input-overruns>0</input-overruns>
               <framing-errors-received>0</framing-errors-received>
               <input-ignored-packets>0</input-ignored-packets>
               <input-aborts>0</input-aborts>
               <output-errors>0</output-errors>
               <output-underruns>0</output-underruns>
               <output-buffer-failures>0</output-buffer-failures>
               <output-buffers-swapped-out>0</output-buffers-swapped-out>
               <applique>0</applique>
               <resets>0</resets>
               <carrier-transitions>0</carrier-transitions>
               <availability-flag>0</availability-flag>
               <last-data-time>1490888108</last-data-time>
               <seconds-since-last-clear-counters>0</seconds-since-last-clear-counters>
               <last-discontinuity-time>1489787869</last-discontinuity-time>
               <seconds-since-packet-received>4294967295</seconds-since-packet-received>
               <seconds-since-packet-sent>4294967295</seconds-since-packet-sent>
              </full-interface-stats>
             </interface-statistics>
             <if-index>0</if-index>
            </interface>
            <interface>
             <interface-name>GigabitEthernet0/0/0/5</interface-name>
             <interface-handle>GigabitEthernet0/0/0/5</interface-handle>
             <interface-type>IFT_GETHERNET</interface-type>
             <hardware-type-string>GigabitEthernet</hardware-type-string>
             <state>im-state-admin-down</state>
             <line-state>im-state-admin-down</line-state>
             <encapsulation>ether</encapsulation>
             <encapsulation-type-string>ARPA</encapsulation-type-string>
             <mtu>1514</mtu>
             <is-l2-transport-enabled>false</is-l2-transport-enabled>
             <state-transition-count>0</state-transition-count>
             <last-state-transition-time>1100377</last-state-transition-time>
             <is-dampening-enabled>false</is-dampening-enabled>
             <speed>1000000</speed>
             <duplexity>im-attr-duplex-full</duplexity>
             <media-type>im-attr-media-other</media-type>
             <link-type>im-attr-link-type-force</link-type>
             <in-flow-control>im-attr-flow-control-off</in-flow-control>
             <out-flow-control>im-attr-flow-control-off</out-flow-control>
             <mac-address>
              <address>52:54:00:0c:e9:48</address>
             </mac-address>
             <burned-in-address>
              <address>52:54:00:0c:e9:48</address>
             </burned-in-address>
             <carrier-delay>
              <carrier-delay-up>10</carrier-delay-up>
              <carrier-delay-down>0</carrier-delay-down>
             </carrier-delay>
             <bandwidth>1000000</bandwidth>
             <max-bandwidth>1000000</max-bandwidth>
             <is-l2-looped>false</is-l2-looped>
             <description></description>
             <data-rates>
              <input-data-rate>0</input-data-rate>
              <input-packet-rate>0</input-packet-rate>
              <output-data-rate>0</output-data-rate>
              <output-packet-rate>0</output-packet-rate>
              <peak-input-data-rate>0</peak-input-data-rate>
              <peak-input-packet-rate>0</peak-input-packet-rate>
              <peak-output-data-rate>0</peak-output-data-rate>
              <peak-output-packet-rate>0</peak-output-packet-rate>
              <bandwidth>1000000</bandwidth>
              <load-interval>9</load-interval>
              <output-load>0</output-load>
              <input-load>0</input-load>
              <reliability>255</reliability>
             </data-rates>
             <interface-statistics>
              <stats-type>full</stats-type>
              <full-interface-stats>
               <packets-received>0</packets-received>
               <bytes-received>0</bytes-received>
               <packets-sent>0</packets-sent>
               <bytes-sent>0</bytes-sent>
               <multicast-packets-received>0</multicast-packets-received>
               <broadcast-packets-received>0</broadcast-packets-received>
               <multicast-packets-sent>0</multicast-packets-sent>
               <broadcast-packets-sent>0</broadcast-packets-sent>
               <output-drops>0</output-drops>
               <output-queue-drops>0</output-queue-drops>
               <input-drops>0</input-drops>
               <input-queue-drops>0</input-queue-drops>
               <runt-packets-received>0</runt-packets-received>
               <giant-packets-received>0</giant-packets-received>
               <throttled-packets-received>0</throttled-packets-received>
               <parity-packets-received>0</parity-packets-received>
               <unknown-protocol-packets-received>0</unknown-protocol-packets-received>
               <input-errors>0</input-errors>
               <crc-errors>0</crc-errors>
               <input-overruns>0</input-overruns>
               <framing-errors-received>0</framing-errors-received>
               <input-ignored-packets>0</input-ignored-packets>
               <input-aborts>0</input-aborts>
               <output-errors>0</output-errors>
               <output-underruns>0</output-underruns>
               <output-buffer-failures>0</output-buffer-failures>
               <output-buffers-swapped-out>0</output-buffers-swapped-out>
               <applique>0</applique>
               <resets>0</resets>
               <carrier-transitions>0</carrier-transitions>
               <availability-flag>0</availability-flag>
               <last-data-time>1490888108</last-data-time>
               <seconds-since-last-clear-counters>0</seconds-since-last-clear-counters>
               <last-discontinuity-time>1489787869</last-discontinuity-time>
               <seconds-since-packet-received>4294967295</seconds-since-packet-received>
               <seconds-since-packet-sent>4294967295</seconds-since-packet-sent>
              </full-interface-stats>
             </interface-statistics>
             <if-index>0</if-index>
            </interface>
            <interface>
             <interface-name>GigabitEthernet0/0/0/6</interface-name>
             <interface-handle>GigabitEthernet0/0/0/6</interface-handle>
             <interface-type>IFT_GETHERNET</interface-type>
             <hardware-type-string>GigabitEthernet</hardware-type-string>
             <state>im-state-admin-down</state>
             <line-state>im-state-admin-down</line-state>
             <encapsulation>ether</encapsulation>
             <encapsulation-type-string>ARPA</encapsulation-type-string>
             <mtu>1514</mtu>
             <is-l2-transport-enabled>false</is-l2-transport-enabled>
             <state-transition-count>0</state-transition-count>
             <last-state-transition-time>1100377</last-state-transition-time>
             <is-dampening-enabled>false</is-dampening-enabled>
             <speed>1000000</speed>
             <duplexity>im-attr-duplex-full</duplexity>
             <media-type>im-attr-media-other</media-type>
             <link-type>im-attr-link-type-force</link-type>
             <in-flow-control>im-attr-flow-control-off</in-flow-control>
             <out-flow-control>im-attr-flow-control-off</out-flow-control>
             <mac-address>
              <address>52:54:00:ec:e5:c4</address>
             </mac-address>
             <burned-in-address>
              <address>52:54:00:ec:e5:c4</address>
             </burned-in-address>
             <carrier-delay>
              <carrier-delay-up>10</carrier-delay-up>
              <carrier-delay-down>0</carrier-delay-down>
             </carrier-delay>
             <bandwidth>1000000</bandwidth>
             <max-bandwidth>1000000</max-bandwidth>
             <is-l2-looped>false</is-l2-looped>
             <description></description>
             <data-rates>
              <input-data-rate>0</input-data-rate>
              <input-packet-rate>0</input-packet-rate>
              <output-data-rate>0</output-data-rate>
              <output-packet-rate>0</output-packet-rate>
              <peak-input-data-rate>0</peak-input-data-rate>
              <peak-input-packet-rate>0</peak-input-packet-rate>
              <peak-output-data-rate>0</peak-output-data-rate>
              <peak-output-packet-rate>0</peak-output-packet-rate>
              <bandwidth>1000000</bandwidth>
              <load-interval>9</load-interval>
              <output-load>0</output-load>
              <input-load>0</input-load>
              <reliability>255</reliability>
             </data-rates>
             <interface-statistics>
              <stats-type>full</stats-type>
              <full-interface-stats>
               <packets-received>0</packets-received>
               <bytes-received>0</bytes-received>
               <packets-sent>0</packets-sent>
               <bytes-sent>0</bytes-sent>
               <multicast-packets-received>0</multicast-packets-received>
               <broadcast-packets-received>0</broadcast-packets-received>
               <multicast-packets-sent>0</multicast-packets-sent>
               <broadcast-packets-sent>0</broadcast-packets-sent>
               <output-drops>0</output-drops>
               <output-queue-drops>0</output-queue-drops>
               <input-drops>0</input-drops>
               <input-queue-drops>0</input-queue-drops>
               <runt-packets-received>0</runt-packets-received>
               <giant-packets-received>0</giant-packets-received>
               <throttled-packets-received>0</throttled-packets-received>
               <parity-packets-received>0</parity-packets-received>
               <unknown-protocol-packets-received>0</unknown-protocol-packets-received>
               <input-errors>0</input-errors>
               <crc-errors>0</crc-errors>
               <input-overruns>0</input-overruns>
               <framing-errors-received>0</framing-errors-received>
               <input-ignored-packets>0</input-ignored-packets>
               <input-aborts>0</input-aborts>
               <output-errors>0</output-errors>
               <output-underruns>0</output-underruns>
               <output-buffer-failures>0</output-buffer-failures>
               <output-buffers-swapped-out>0</output-buffers-swapped-out>
               <applique>0</applique>
               <resets>0</resets>
               <carrier-transitions>0</carrier-transitions>
               <availability-flag>0</availability-flag>
               <last-data-time>1490888108</last-data-time>
               <seconds-since-last-clear-counters>0</seconds-since-last-clear-counters>
               <last-discontinuity-time>1489787869</last-discontinuity-time>
               <seconds-since-packet-received>4294967295</seconds-since-packet-received>
               <seconds-since-packet-sent>4294967295</seconds-since-packet-sent>
              </full-interface-stats>
             </interface-statistics>
             <if-index>0</if-index>
            </interface>
            <interface>
             <interface-name>MgmtEth0/0/CPU0/0</interface-name>
             <interface-handle>MgmtEth0/0/CPU0/0</interface-handle>
             <interface-type>IFT_ETHERNET</interface-type>
             <hardware-type-string>Management Ethernet</hardware-type-string>
             <state>im-state-up</state>
             <line-state>im-state-up</line-state>
             <encapsulation>ether</encapsulation>
             <encapsulation-type-string>ARPA</encapsulation-type-string>
             <mtu>1514</mtu>
             <is-l2-transport-enabled>false</is-l2-transport-enabled>
             <state-transition-count>1</state-transition-count>
             <last-state-transition-time>1100222</last-state-transition-time>
             <is-dampening-enabled>false</is-dampening-enabled>
             <speed>1000000</speed>
             <duplexity>im-attr-duplex-unknown</duplexity>
             <media-type>im-attr-media-other</media-type>
             <link-type>im-attr-link-type-auto</link-type>
             <in-flow-control>im-attr-flow-control-off</in-flow-control>
             <out-flow-control>im-attr-flow-control-off</out-flow-control>
             <mac-address>
              <address>52:54:00:ef:a9:52</address>
             </mac-address>
             <burned-in-address>
              <address>52:54:00:ef:a9:52</address>
             </burned-in-address>
             <carrier-delay>
              <carrier-delay-up>10</carrier-delay-up>
              <carrier-delay-down>0</carrier-delay-down>
             </carrier-delay>
             <bandwidth>1000000</bandwidth>
             <max-bandwidth>1000000</max-bandwidth>
             <is-l2-looped>false</is-l2-looped>
             <description></description>
             <arp-information>
              <arp-timeout>14400</arp-timeout>
              <arp-type-name>ARPA</arp-type-name>
              <arp-is-learning-disabled>false</arp-is-learning-disabled>
             </arp-information>
             <ip-information>
              <ip-address>10.85.112.123</ip-address>
              <subnet-mask-length>25</subnet-mask-length>
             </ip-information>
             <data-rates>
              <input-data-rate>192</input-data-rate>
              <input-packet-rate>392</input-packet-rate>
              <output-data-rate>70</output-data-rate>
              <output-packet-rate>105</output-packet-rate>
              <peak-input-data-rate>0</peak-input-data-rate>
              <peak-input-packet-rate>0</peak-input-packet-rate>
              <peak-output-data-rate>0</peak-output-data-rate>
              <peak-output-packet-rate>0</peak-output-packet-rate>
              <bandwidth>1000000</bandwidth>
              <load-interval>9</load-interval>
              <output-load>0</output-load>
              <input-load>0</input-load>
              <reliability>255</reliability>
             </data-rates>
             <interface-statistics>
              <stats-type>full</stats-type>
              <full-interface-stats>
               <packets-received>228836760</packets-received>
               <bytes-received>13447429857</bytes-received>
               <packets-sent>56486840</packets-sent>
               <bytes-sent>4095136965</bytes-sent>
               <multicast-packets-received>1042005</multicast-packets-received>
               <broadcast-packets-received>174752</broadcast-packets-received>
               <multicast-packets-sent>0</multicast-packets-sent>
               <broadcast-packets-sent>21</broadcast-packets-sent>
               <output-drops>0</output-drops>
               <output-queue-drops>0</output-queue-drops>
               <input-drops>0</input-drops>
               <input-queue-drops>0</input-queue-drops>
               <runt-packets-received>0</runt-packets-received>
               <giant-packets-received>0</giant-packets-received>
               <throttled-packets-received>0</throttled-packets-received>
               <parity-packets-received>0</parity-packets-received>
               <unknown-protocol-packets-received>0</unknown-protocol-packets-received>
               <input-errors>0</input-errors>
               <crc-errors>0</crc-errors>
               <input-overruns>0</input-overruns>
               <framing-errors-received>0</framing-errors-received>
               <input-ignored-packets>0</input-ignored-packets>
               <input-aborts>0</input-aborts>
               <output-errors>0</output-errors>
               <output-underruns>0</output-underruns>
               <output-buffer-failures>0</output-buffer-failures>
               <output-buffers-swapped-out>0</output-buffers-swapped-out>
               <applique>0</applique>
               <resets>0</resets>
               <carrier-transitions>1</carrier-transitions>
               <availability-flag>0</availability-flag>
               <last-data-time>1490888108</last-data-time>
               <seconds-since-last-clear-counters>0</seconds-since-last-clear-counters>
               <last-discontinuity-time>1489787864</last-discontinuity-time>
               <seconds-since-packet-received>0</seconds-since-packet-received>
               <seconds-since-packet-sent>0</seconds-since-packet-sent>
              </full-interface-stats>
             </interface-statistics>
             <if-index>0</if-index>
            </interface>
            <interface>
             <interface-name>Null0</interface-name>
             <interface-handle>Null0</interface-handle>
             <interface-type>IFT_NULL</interface-type>
             <hardware-type-string>Null interface</hardware-type-string>
             <state>im-state-up</state>
             <line-state>im-state-up</line-state>
             <encapsulation>null</encapsulation>
             <encapsulation-type-string>Null</encapsulation-type-string>
             <mtu>1500</mtu>
             <is-l2-transport-enabled>false</is-l2-transport-enabled>
             <state-transition-count>1</state-transition-count>
             <last-state-transition-time>1100254</last-state-transition-time>
             <is-dampening-enabled>false</is-dampening-enabled>
             <bandwidth>0</bandwidth>
             <max-bandwidth>0</max-bandwidth>
             <is-l2-looped>false</is-l2-looped>
             <description></description>
             <data-rates>
              <input-data-rate>0</input-data-rate>
              <input-packet-rate>0</input-packet-rate>
              <output-data-rate>0</output-data-rate>
              <output-packet-rate>0</output-packet-rate>
              <peak-input-data-rate>0</peak-input-data-rate>
              <peak-input-packet-rate>0</peak-input-packet-rate>
              <peak-output-data-rate>0</peak-output-data-rate>
              <peak-output-packet-rate>0</peak-output-packet-rate>
              <bandwidth>0</bandwidth>
              <load-interval>9</load-interval>
              <output-load>0</output-load>
              <input-load>0</input-load>
              <reliability>255</reliability>
             </data-rates>
             <interface-statistics>
              <stats-type>full</stats-type>
              <full-interface-stats>
               <packets-received>0</packets-received>
               <bytes-received>0</bytes-received>
               <packets-sent>0</packets-sent>
               <bytes-sent>0</bytes-sent>
               <multicast-packets-received>0</multicast-packets-received>
               <broadcast-packets-received>0</broadcast-packets-received>
               <multicast-packets-sent>0</multicast-packets-sent>
               <broadcast-packets-sent>0</broadcast-packets-sent>
               <output-drops>0</output-drops>
               <output-queue-drops>0</output-queue-drops>
               <input-drops>0</input-drops>
               <input-queue-drops>0</input-queue-drops>
               <runt-packets-received>0</runt-packets-received>
               <giant-packets-received>0</giant-packets-received>
               <throttled-packets-received>0</throttled-packets-received>
               <parity-packets-received>0</parity-packets-received>
               <unknown-protocol-packets-received>0</unknown-protocol-packets-received>
               <input-errors>0</input-errors>
               <crc-errors>0</crc-errors>
               <input-overruns>0</input-overruns>
               <framing-errors-received>0</framing-errors-received>
               <input-ignored-packets>0</input-ignored-packets>
               <input-aborts>0</input-aborts>
               <output-errors>0</output-errors>
               <output-underruns>0</output-underruns>
               <output-buffer-failures>0</output-buffer-failures>
               <output-buffers-swapped-out>0</output-buffers-swapped-out>
               <applique>0</applique>
               <resets>0</resets>
               <carrier-transitions>0</carrier-transitions>
               <availability-flag>0</availability-flag>
               <last-data-time>1490888108</last-data-time>
               <seconds-since-last-clear-counters>0</seconds-since-last-clear-counters>
               <last-discontinuity-time>1489787884</last-discontinuity-time>
               <seconds-since-packet-received>4294967295</seconds-since-packet-received>
               <seconds-since-packet-sent>4294967295</seconds-since-packet-sent>
              </full-interface-stats>
             </interface-statistics>
             <if-index>0</if-index>
            </interface>
           </interface-xr>
          </interfaces>
         </data>
        ''')
    
    golden_output = {'get.return_value': etree_holder()}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        intf_obj = ShowEthernetTags(device=self.device)
        intf_obj.context = Context.yang.value
        parsed_output = intf_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    empty_parsed_output = {'interface': {'GigabitEthernet0/0/0/0': {'sub_interface': {'GigabitEthernet0/0/0/0.501': {}}}}}

    class empty_etree_holder():
      def __init__(self):
        self.data = ET.fromstring('''
         <data>
          <interfaces xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-pfi-im-cmd-oper">
           <interface-xr>
            <interface>
             <interface-name>GigabitEthernet0/0/0/0.501</interface-name>
             <interface-handle>GigabitEthernet0/0/0/0.501</interface-handle>
             <interface-type>IFT_VLAN_SUBIF</interface-type>
             <hardware-type-string>VLAN sub-interface(s)</hardware-type-string>
             <state>im-state-up</state>
             <line-state>im-state-up</line-state>
             <encapsulation>dot1q</encapsulation>
             <encapsulation-type-string>802.1Q</encapsulation-type-string>
             <mtu>1522</mtu>
             <is-l2-transport-enabled>false</is-l2-transport-enabled>
             <state-transition-count>1</state-transition-count>
             <last-state-transition-time>1100222</last-state-transition-time>
             <is-dampening-enabled>false</is-dampening-enabled>
             <speed>1000000</speed>
             <mac-address>
              <address>52:54:00:a0:af:6d</address>
             </mac-address>
             <carrier-delay>
              <carrier-delay-up>0</carrier-delay-up>
              <carrier-delay-down>0</carrier-delay-down>
             </carrier-delay>
             <bandwidth>1000000</bandwidth>
             <max-bandwidth>1000000</max-bandwidth>
             <is-l2-looped>false</is-l2-looped>
             <parent-interface-name>GigabitEthernet0/0/0/0</parent-interface-name>
             <description></description>
             <encapsulation-information>
             </encapsulation-information>
             <data-rates>
              <input-data-rate>0</input-data-rate>
              <input-packet-rate>0</input-packet-rate>
              <output-data-rate>0</output-data-rate>
              <output-packet-rate>0</output-packet-rate>
              <peak-input-data-rate>0</peak-input-data-rate>
              <peak-input-packet-rate>0</peak-input-packet-rate>
              <peak-output-data-rate>0</peak-output-data-rate>
              <peak-output-packet-rate>0</peak-output-packet-rate>
              <bandwidth>1000000</bandwidth>
              <load-interval>9</load-interval>
              <output-load>0</output-load>
              <input-load>0</input-load>
              <reliability>255</reliability>
             </data-rates>
             <interface-statistics>
              <stats-type>full</stats-type>
              <full-interface-stats>
               <packets-received>0</packets-received>
               <bytes-received>0</bytes-received>
               <packets-sent>0</packets-sent>
               <bytes-sent>0</bytes-sent>
               <multicast-packets-received>0</multicast-packets-received>
               <broadcast-packets-received>0</broadcast-packets-received>
               <multicast-packets-sent>0</multicast-packets-sent>
               <broadcast-packets-sent>0</broadcast-packets-sent>
               <output-drops>0</output-drops>
               <output-queue-drops>0</output-queue-drops>
               <input-drops>0</input-drops>
               <input-queue-drops>0</input-queue-drops>
               <runt-packets-received>0</runt-packets-received>
               <giant-packets-received>0</giant-packets-received>
               <throttled-packets-received>0</throttled-packets-received>
               <parity-packets-received>0</parity-packets-received>
               <unknown-protocol-packets-received>0</unknown-protocol-packets-received>
               <input-errors>0</input-errors>
               <crc-errors>0</crc-errors>
               <input-overruns>0</input-overruns>
               <framing-errors-received>0</framing-errors-received>
               <input-ignored-packets>0</input-ignored-packets>
               <input-aborts>0</input-aborts>
               <output-errors>0</output-errors>
               <output-underruns>0</output-underruns>
               <output-buffer-failures>0</output-buffer-failures>
               <output-buffers-swapped-out>0</output-buffers-swapped-out>
               <applique>0</applique>
               <resets>0</resets>
               <carrier-transitions>0</carrier-transitions>
               <availability-flag>0</availability-flag>
               <last-data-time>1490888108</last-data-time>
               <seconds-since-last-clear-counters>0</seconds-since-last-clear-counters>
               <last-discontinuity-time>1489787915</last-discontinuity-time>
               <seconds-since-packet-received>4294967295</seconds-since-packet-received>
               <seconds-since-packet-sent>4294967295</seconds-since-packet-sent>
              </full-interface-stats>
             </interface-statistics>
             <if-index>0</if-index>
            </interface>
           </interface-xr>
          </interfaces>
         </data>
        ''')

    empty_output = {'get.return_value': empty_etree_holder()}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        intf_obj = ShowEthernetTags(device=self.device1)
        intf_obj.context = Context.yang.value
        parsed_output = intf_obj.parse()
        self.assertEqual(parsed_output,self.empty_parsed_output)

if __name__ == '__main__':
    unittest.main()