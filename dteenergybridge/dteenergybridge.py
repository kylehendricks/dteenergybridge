# -*- coding: utf-8 -*-

import requests

from dteenergybridge import exceptions


class DteEnergyBridge:
    """Performs API requests against the DTE Energy Bridge"""

    def __init__(self, host, bridge_version=1, timeout=5):
        self.base_url = "http://{}:{}/".format(host, '80' if bridge_version == 1 else '8888')
        self.timeout = timeout

        if bridge_version not in (1, 2):
            raise exceptions.InvalidArgumentError('Bridge version must be either 1 or 2')

        self.bridge_version = bridge_version

    def instantaneous_demand_path(self):
        """The URL path to the instantaneousdemand API"""
        return 'instantaneousdemand' if self.bridge_version == 1 else 'zigbee/se/instantaneousdemand'

    def get_current_energy_usage(self):
        """Returns the current energy usage in kW"""
        try:
            response = requests.get(self.base_url + self.instantaneous_demand_path(), timeout=self.timeout)
        except (requests.exceptions.RequestException, ValueError) as exc:
            raise exceptions.InvalidResponseError() from exc

        if response.status_code != 200:
            raise exceptions.InvalidResponseError("Received status {} from DTE Energy Bridge".format(response.status_code))

        response_split = response.text.split()

        if len(response_split) != 2:
            raise exceptions.InvalidResponseError("Received bad response '{}' from DTE Energy Bridge".format(response.text))

        val = float(response_split[0])

        # A workaround for a bug in the DTE energy bridge.
        # The returned value can randomly be in W or kW.  Checking for a
        # a decimal seems to be a reliable way to determine the units.
        return val if '.' in response_split[0] else val / 1000
