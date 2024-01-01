from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import json


def bgp_state_validation(bgp_data):
    try:
        data = json.loads(bgp_data)
        neighbors = data['Cisco-IOS-XE-bgp-oper:bgp-state-data']['neighbors']['neighbor']

        bgp_states = {bgp_n['neighbor-id']: bgp_n['connection']['state'] for bgp_n in neighbors}

        for bgp_n, bgp_state in bgp_states.items():
            if bgp_state != 'established':
                raise ValueError('BGP Neighbor {} not established: {}'.format(bgp_n, bgp_state))
    except Exception:
        raise ValueError('BGP data could not be parsed')
    return bgp_states


class FilterModule(object):
    """PARSE BGP STATE OF THE NEIGHBORS"""
    def filters(self):
        return {
            "bgp_state_validation": bgp_state_validation,
        }
