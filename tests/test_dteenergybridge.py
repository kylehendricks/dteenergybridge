#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `dteenergybridge` package."""

import pytest
import requests_mock
import requests.exceptions


from dteenergybridge import dteenergybridge
from dteenergybridge import exceptions


def test_invalid_bridge_version():
    """Tests to make sure constructor throws on invalid bridge_version"""
    with pytest.raises(exceptions.InvalidArgumentError):
        dteenergybridge.DteEnergyBridge('127.0.0.1', 3)


def test_valid_bridge_version():
    """Tests to make sure constructor doesn't throw on valid bridge_version"""
    dteenergybridge.DteEnergyBridge('127.0.0.1', 1)
    dteenergybridge.DteEnergyBridge('127.0.0.1', 2)


def test_instantaneous_demand_v1():
    with requests_mock.Mocker() as req_mock:
        req_mock.get("http://127.0.0.1:80/instantaneousdemand",
                     text='.411 kW')
        dte = dteenergybridge.DteEnergyBridge('127.0.0.1', 1)
        assert dte.get_current_energy_usage() == .411


def test_instantaneous_demand_v2():
    with requests_mock.Mocker() as req_mock:
        req_mock.get("http://127.0.0.1:8888/zigbee/se/instantaneousdemand",
                     text='.411 kW')
        dte = dteenergybridge.DteEnergyBridge('127.0.0.1', 2)
        assert dte.get_current_energy_usage() == .411


def test_requests_exception():
    with requests_mock.Mocker() as req_mock:
        req_mock.get("http://127.0.0.1:80/instantaneousdemand",
                     exc=requests.exceptions.RequestException)
        dte = dteenergybridge.DteEnergyBridge('127.0.0.1', 1)
        with pytest.raises(exceptions.InvalidResponseError):
            dte.get_current_energy_usage()


def test_incorrect_units_response():
    with requests_mock.Mocker() as req_mock:
        req_mock.get("http://127.0.0.1:80/instantaneousdemand",
                     text='411 kW')
        dte = dteenergybridge.DteEnergyBridge('127.0.0.1', 1)
        assert dte.get_current_energy_usage() == .411


def test_bad_formatted_response():
    with requests_mock.Mocker() as req_mock:
        req_mock.get("http://127.0.0.1:80/instantaneousdemand",
                     text='411')
        dte = dteenergybridge.DteEnergyBridge('127.0.0.1', 1)
        with pytest.raises(exceptions.InvalidResponseError):
            dte.get_current_energy_usage()
