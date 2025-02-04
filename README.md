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
pip install grpcio>=1.68.0


# Run arduino thermistor:
python -m arduino_thermistor_thermometer --debug --server-name thermistor_thermometer --insecure --serial-port COM5

# run bioshaker:
python -m sila2_driver.qinstruments.bioshake_qx --port 50050

# Sila browser 

cd sila-browser
npm run preview 

# open questions 

How do i see the data in jupyter notebook
How can i use unitelab

# first_connector
Following unitelabs intro to connector:
https://docs-unitelabs-web-815d69b03b66df4c3a4817af38d7e7b09a17f7c4b50b.gitlab.io/connectivity/introduction/installation

