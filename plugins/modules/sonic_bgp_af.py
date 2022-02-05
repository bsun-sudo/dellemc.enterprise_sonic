#!/usr/bin/python
# -*- coding: utf-8 -*-
# © Copyright 2020 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for sonic_bgp_af
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = """
---
module: sonic_bgp_af
version_added: 1.0.0
notes:
- Tested against Enterprise SONiC Distribution by Dell Technologies.
- Supports C(check_mode).
author: Niraimadaiselvam M (@niraimadaiselvamm)
short_description: Manage global BGP address-family and its parameters
description:
  - This module provides configuration management of global BGP_AF parameters on devices running Enterprise SONiC.
  - bgp_as and vrf_name must be created in advance on the device.
options:
  config:
    description:
      - Specifies the BGP_AF related configuration.
    type: list
    elements: dict
    suboptions:
      bgp_as:
        description:
          - Specifies the BGP autonomous system (AS) number which is already configured on the device.
        type: str
        required: true
      vrf_name:
        description:
          - Specifies the VRF name which is already configured on the device.
        type: str
        default: 'default'
      address_family:
        description:
          - Specifies BGP address family related configurations.
        type: dict
        suboptions:
          afis:
            description:
              - List of address families, such as ipv4, ipv6, and l2vpn.
              - afi and safi are required together.
            type: list
            elements: dict
            suboptions:
              afi:
                description:
                  - Type of address family to configure.
                type: str
                choices:
                  - ipv4
                  - ipv6
                  - l2vpn
                required: True
              safi:
                description:
                 - Specifies the type of communication for the address family.
                type: str
                choices:
                  - unicast
                  - evpn
                default: unicast
              dampening:
                description:
                  - Enable route flap dampening if set to true
                type: bool
              network:
                description:
                  - Enable routing on an IP network for each prefix provided in the network
                type: list
                elements: str
              redistribute:
                description:
                  - Specifies the redistribute information from another routing protocol.
                type: list
                elements: dict
                suboptions:
                  protocol:
                    description:
                      - Specifies the protocol for configuring redistribute information.
                    type: str
                    choices: ['ospf', 'static', 'connected']
                    required: True
                  metric:
                    description:
                      - Specifies the metric for redistributed routes.
                    type: str
                  route_map:
                    description:
                      - Specifies the route map reference.
                    type: str
              advertise_default_gw:
                description:
                  - Specifies the advertise default gateway flag.
                type: bool
              advertise_all_vni:
                description:
                  - Specifies the advertise all vni flag.
                type: bool
              max_path:
                description:
                  - Specifies the maximum paths of ibgp and ebgp count.
                type: dict
                suboptions:
                  ibgp:
                    description:
                      - Specifies the count of the ibgp multipaths count.
                    type: int
                  ebgp:
                    description:
                      - Specifies the count of the ebgp multipaths count.
                    type: int
  state:
    description:
      - Specifies the operation to be performed on the BGP_AF process configured on the device.
      - In case of merged, the input configuration is merged with the existing BGP_AF configuration on the device.
      - In case of deleted, the existing BGP_AF configuration is removed from the device.
    default: merged
    choices: ['merged', 'deleted']
    type: str
"""
EXAMPLES = """
# Using deleted
#
# Before state:
# -------------
#
#do show running-configuration bgp
#!
#router bgp 51
# router-id 111.2.2.41
# timers 60 180
# !
# address-family ipv4 unicast
#  maximum-paths 1
#  maximum-paths ibgp 1
#  dampening
# !
# address-family ipv6 unicast
#  redistribute connected route-map bb metric 21
#  redistribute ospf route-map aa metric 27
#  redistribute static route-map bb metric 26
#  maximum-paths 4
#  maximum-paths ibgp 5
# !
# address-family l2vpn evpn
#!
#
- name: Delete BGP Address family configuration from the device
  dellemc.enterprise_sonic.sonic_bgp_af:
     config:
       - bgp_as: 51
         address_family:
           afis:
             - afi: l2vpn
               safi: evpn
               advertise_all_vni: False
               advertise_default_gw: False
             - afi: ipv4
               safi: unicast
             - afi: ipv6
               safi: unicast
               max_path:
                 ebgp: 2
                 ibgp: 5
               redistribute:
                 - metric: "21"
                   protocol: connected
                   route_map: bb
                 - metric: "27"
                   protocol: ospf
                   route_map: aa
                 - metric: "26"
                   protocol: static
                   route_map: bb
     state: deleted

# After state:
# ------------
#
#do show running-configuration bgp
#!
#router bgp 51
# router-id 111.2.2.41
# timers 60 180
# !
# address-family ipv6 unicast
# !
# address-family l2vpn evpn
#
# Using deleted
#
# Before state:
# -------------
#
#do show running-configuration bgp
#!
#router bgp 51
# router-id 111.2.2.41
# timers 60 180
# !
# address-family ipv6 unicast
# !
# address-family l2vpn evpn
#
- name: Delete All BGP address family configurations
  dellemc.enterprise_sonic.sonic_bgp_af:
     config:
     state: deleted


# After state:
# ------------
#
#do show running-configuration bgp
#!
#router bgp 51
# router-id 111.2.2.41
# timers 60 180
#
# Using merged
#
# Before state:
# -------------
#
#do show running-configuration bgp
#!
#router bgp 51
# router-id 111.2.2.41
# timers 60 180
# !
# address-family l2vpn evpn
#
- name: Merge provided BGP address family configuration on the device.
  dellemc.enterprise_sonic.sonic_bgp_af:
     config:
       - bgp_as: 51
         address_family:
           afis:
             - afi: l2vpn
               safi: evpn
               advertise_all_vni: False
               advertise_default_gw: False
             - afi: ipv4
               safi: unicast
               network:
                 - 2.2.2.2/16
                 - 192.168.10.1/32
               dampening: True
             - afi: ipv6
               safi: unicast
               max_path:
                 ebgp: 4
                 ibgp: 5
               redistribute:
                 - metric: "21"
                   protocol: connected
                   route_map: bb
                 - metric: "27"
                   protocol: ospf
                   route_map: aa
                 - metric: "26"
                   protocol: static
                   route_map: bb
     state: merged
# After state:
# ------------
#
#do show running-configuration bgp
#!
#router bgp 51
# router-id 111.2.2.41
# timers 60 180
# !
# address-family ipv4 unicast
#  network 2.2.2.2/16
#  network 192.168.10.1/32
#  dampening
# !
# address-family ipv6 unicast
#  redistribute connected route-map bb metric 21
#  redistribute ospf route-map aa metric 27
#  redistribute static route-map bb metric 26
#  maximum-paths 4
#  maximum-paths ibgp 5
# !
# address-family l2vpn evpn
#
"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: list
  sample: >
    The configuration returned is always in the same format
    of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: list
  sample: >
    The configuration returned always in the same format
    of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.bgp_af.bgp_af import Bgp_afArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.bgp_af.bgp_af import Bgp_af


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=Bgp_afArgs.argument_spec,
                           supports_check_mode=True)

    result = Bgp_af(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
