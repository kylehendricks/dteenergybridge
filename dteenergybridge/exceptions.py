"""DTE Energy Bridge Exceptions."""


class DteEnergyBridgeError(Exception):
    """Base class for all DTE Energy Bridge exceptions"""


class InvalidResponseError(DteEnergyBridgeError):
    """Response from DTE Energy Bridge was invalid"""


class InvalidArgumentError(DteEnergyBridgeError):
    """Invalid argument"""
