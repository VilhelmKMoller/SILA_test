# Arduino Thermistor Thermometer

A simple Arduino / Teensy based thermistor thermometer with SiLA control.

## Features

## Installation

    pip install arduino_thermistor_thermometer --index-url https://gitlab.com/api/v4/projects/<gitlab-project-id>/packages/pypi/simple

## Usage

    # starting the thermometer SiLA server (example, please adust the serial port)
    python -m arduino_thermistor_thermometer --debug --server-name thermistor_thermometer --insecure --serial-port /dev/ttyACM0


## Help

    arduino_thermistor_thermometer --help 

## Development

    git clone gitlab.com/opensourcelab/arduino-thermistor-thermometer

    # create a virtual environment and activate it then run

    pip install -e .[dev]

    # run unittests

    invoke test   # use the invoke environment to manage development
    

## Documentation

The Documentation can be found here: [https://opensourcelab.gitlab.io/arduino-thermistor-thermometer](https://opensourcelab.gitlab.io/arduino-thermistor-thermometer) or [arduino-thermistor-thermometer.gitlab.io](arduino_thermistor_thermometer.gitlab.io/)


## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter)
 and the [gitlab.com/opensourcelab/software-dev/cookiecutter-pypackage](https://gitlab.com/opensourcelab/software-dev/cookiecutter-pypackage) project template.



