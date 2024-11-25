# Serial interface for the Cytomat 2

import random
import time
import logging
import re
from serial import Serial


logger = logging.getLogger(__name__)

class SerialInterface(Serial):
    serial_port: str

    def __init__(self, serial_port: str):
        self.serial_port = serial_port
        super().__init__(serial_port, timeout=1.0)

        self.encoding = "utf-8"

        self._target_temperature = 37.0
        self._current_temperature = 33.0

        self.logger = logger

    def send_command(
        self, command, encoding="utf-8", timeout=1.0
    ):  # Timeout has to be quite long as certain commands take up to a second to produce an ack from the Cytomat
        """
        :param timeout:
        :param max_wait: The maximum waiting time for the communication port becoming available
        :param encoding: the encoding used for the command and the reply
        :param command: the string to write via the serial
        :return: the decoded reply
        """
        start = time()
        self.reset_input_buffer()  # clear the buffer in case some leftovers from the last command remain
        self.reset_output_buffer()  # same for the output buffer jic
        self.timeout = timeout
        self.write(command.encode(encoding))
        try:
            reply = self.read_until("\r".encode(encoding)).decode(encoding)
        except Exception:
            return "no_reply"
        # only log the not so frequent commands
        if "bs" not in command and "ch:it" not in command and "ch:ic" not in command:
            self.logger.info(
                f"to command {command.strip()}, we got reply"
                f" {reply.encode(encoding)} after {round(time() - start,2)} seconds"
            )
        return reply.strip()
    
    @property
    def current_temperature(self):
        try:
            reply = self.read_until("\r".encode(self.encoding)).decode(self.encoding)
            match = re.search(r"T:(\d*\.\d*),\s*L:(\d*)", reply)
            current_temp = float(match.group(1))
        except Exception as err:
            self.logger.error(f"Error reading current temperature: {err}")
            #current_temp = self._current_temperature
            return 0.0
       
        logging.debug(f"current temp. from serial device: {current_temp}")

        #return f"tb {self._current_temperature:4.2f}\r"
        return current_temp
    
    @property
    def current_lightintensity(self):
        try:
            reply = self.read_until("\r".encode(self.encoding)).decode(self.encoding)
            print("----reply", reply)
            match = re.search(r"T:(\d*\.\d*),\s*L:(\d*)", reply)

            current_lightint = float(match.group(2))

            print("----current_lightint", current_lightint)

        except Exception as err:
            self.logger.error(f"Error reading current light intensity: {err}")
            return 0.0
       
        logging.debug(f"current temp. from serial device: {current_lightint}")

        #return f"tb {self._current_temperature:4.2f}\r"
        return current_lightint


class SerialInterfaceSimulation:
    def __init__(self):
    
        self._target_temperature = 37.0
        self._current_temperature = 33.0

        self._target_lightintensity = 96.0
        self._current_lightintensity = 69.0

        self.logger = logger

    def send_command(
        self, command, encoding="utf-8", timeout=1.0
    ):  # Timeout has to be quite long as certain commands take up to a second to produce an ack from the Cytomat
        """
        :param timeout:
        :param max_wait: The maximum waiting time for the communication port becoming available
        :param encoding: the encoding used for the command and the reply
        :param command: the string to write via the serial
        :return: the decoded reply
        """
        start = time()

        self.timeout = timeout

        self.logger.info(command.encode(encoding))

        if "ch:it" in command:
            reply = self.current_temperature

        elif "ll:it" in command:
            self.target_temperature = command
            reply = self.target_temperature

        elif "ch:ic" in command:
            reply = self.current_co2

        elif "ll:ic" in command:
            self.target_co2 = command
            reply = self.target_co2

        reply = "simulation"

    @property
    def current_temperature(self):
        # return random temperature around self._current_temperature plus/minus 3.5 degrees
        self._current_temperature = (
            self._current_temperature + (random.random() * 7.0) - 3.5
        )

        #return f"tb {self._current_temperature:4.2f}\r"
        return self._current_temperature
    
    @property
    def current_lightintensity(self):
        # return random temperature around self._current_temperature plus/minus 3.5 degrees
        self._current_lightintensity = (
            self._current_lightintensity + (random.random() * 10.0) - 1.5
        )

        return self._current_lightintensity

    @current_temperature.setter
    def current_temperature(self, value):
        self._current_temperature = value

    @property
    def target_temperature(self):
        return self._target_temperature

    @target_temperature.setter
    def target_temperature(self, value):
        # TODO: better parsing of the command string
        self._target_temperature = float(value.split(" ")[1])

    @property
    def current_co2(self):
        # return random co2 around self._current_co2 plus/minus 0.5
        self._current_co2 = self._current_co2 + (random.random() * 1.0) - 0.5
        return self._current_co2

    @current_co2.setter
    def current_co2(self, value):
        # TODO: better parsing of the command string
        self._current_co2 = value

    @property
    def target_co2(self):
        return self._target_co2

    @target_co2.setter
    def target_co2(self, value):
        self._target_co2 = float(value.split(" ")[1])
