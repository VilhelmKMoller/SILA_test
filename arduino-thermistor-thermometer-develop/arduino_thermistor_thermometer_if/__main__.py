#!/usr/bin/env python3
# vim:fileencoding=utf-8
"""_____________________________________________________________________

:PROJECT: Arduino Thermistor Thermometer

* Main module command line interface *

:details:  Main module command line interface. 
           !!! Warning: it should have a diffent name than the package name.

.. note:: -
.. todo:: - 
________________________________________________________________________
"""

"""Main module implementation. !!! Warning: it should have a diffent name than the package name. """
"""Console script for arduino_thermistor_thermometer."""

import argparse
import sys
import logging
from arduino_thermistor_thermometer import __version__

from arduino_thermistor_thermometer.arduino_thermistor_thermometer_impl import HelloWorld

logging.basicConfig(
    format="%(levelname)-4s| %(module)s.%(funcName)s: %(message)s",
    level=logging.DEBUG,
)    

def parse_command_line():
    """ Looking for command line arguments"""

    description = "arduino_thermistor_thermometer"
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument("_", nargs="*")

    parser.add_argument(
        "-n", "--name", action="store", default="yvain", help="name to greet"
    )

    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)

    # add more arguments here

    return parser.parse_args()

def main():
    """Console script for arduino_thermistor_thermometer."""
        # or use logging.INFO (=20) or logging.ERROR (=30) for less output
    logging.basicConfig(
        format='%(levelname)-4s| %(module)s.%(funcName)s: %(message)s', level=logging.DEBUG)
    
    
    args = parse_command_line()
        
    if len(sys.argv) <= 2:
        logging.debug("no arguments provided !")


    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into arduino_thermistor_thermometer.__main__")
    
    hw = HelloWorld()
    greeting = hw.greet_the_world(args.name)
    logging.debug(greeting)
    
    return 0


if __name__ == "__main__":

    sys.exit(main())  # pragma: no cover
