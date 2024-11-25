#!/usr/bin/env python
"""Tests for `arduino_thermistor_thermometer` package."""
# pylint: disable=redefined-outer-name
from arduino_thermistor_thermometer import __version__
from arduino_thermistor_thermometer.arduino_thermistor_thermometer_interface import GreeterInterface
from arduino_thermistor_thermometer.arduino_thermistor_thermometer_impl import HelloWorld

def test_version():
    """Sample pytest test function."""
    assert __version__ == "0.0.1"

def test_GreeterInterface():
    """ testing the formal interface (GreeterInterface)
    """
    assert issubclass(HelloWorld, GreeterInterface)

def test_HelloWorld():
    """ Testing HelloWorld class
    """
    hw = HelloWorld()
    name = 'yvain'
    assert hw.greet_the_world(name) == f"Hello world, {name} !"

