# SILA_test
 test SILA by using Arduino
Attempt to use https://gitlab.com/opensourcelab/devices/temp-ctrl to learn to settup a SILA server using your Arduino

git@gitlab.com:opensourcelab/devices/temp-ctrl/arduino-thermistor-thermometer.git

# Installation / Settup
Setup and activate virtual environment
python -m venv .venv
./.venv/Scripts/activate

Upgrade pip to latest version
sila2[codegen] dependency does not install properly on some versions of pip (version < 23.2.1)
python -m pip install --upgrade pip

Go into the correct folder:
cd arduino-thermistor-thermometer-develop

Install package dev tools
python -m pip install .[dev]

Install packages:
pip install pyserial
pip install pydantic

Run server:
python -m arduino_thermistor_thermometer --debug --server-name thermistor_thermometer --insecure --serial-port COM5


# open questions 

How do i see the data in jupyter notebook
How can i use unitelab