// adafruit code from source: https://www.makerguides.com/arduino-uno-max31855-thermocouple-amplifier/
// SILA prep from source: https://gitlab.com/opensourcelab/devices/temp-ctrl/arduino-thermistor-thermometer/-/blob/develop/arduino_project_thermistor_thermometer/thermistor_thermometer/thermistor_thermometer.ino?ref_type=heads
#include "SPI.h"
#include "Adafruit_MAX31855.h"
 
// Default connection is using software SPI, but comment and uncomment one of
// the two examples below to switch between software SPI and hardware SPI:
 
// Example creating a thermocouple instance with software SPI on any three
// digital IO pins.
#define MAXDO   3
#define MAXCS   4
#define MAXCLK  5
 
// initialize the Thermocouple
Adafruit_MAX31855 thermocouple(MAXCLK, MAXCS, MAXDO);
 
void setup() {
  Serial.begin(9600);
 
  while (!Serial) delay(1); // wait for Serial on Leonardo/Zero, etc
 
  Serial.println("MAX31855 test");
  // wait for MAX chip to stabilize
  delay(500);
  Serial.print("Initializing sensor...");
  if (!thermocouple.begin()) {
    Serial.println("ERROR.");
    while (1) delay(10);
  }
 
 
  Serial.println("DONE.");
}
 
void loop() {
   // read out temp
   double T = thermocouple.readCelsius();
   if (isnan(T)) {
     Serial.println("Thermocouple fault(s) detected!");
     uint8_t e = thermocouple.readError();
     if (e & MAX31855_FAULT_OPEN) Serial.println("FAULT: Thermocouple is open - no connections.");
     if (e & MAX31855_FAULT_SHORT_GND) Serial.println("FAULT: Thermocouple is short-circuited to GND.");
     if (e & MAX31855_FAULT_SHORT_VCC) Serial.println("FAULT: Thermocouple is short-circuited to VCC.");
   } else {
     Serial.print("T:");
     Serial.print(T);
     Serial.println(",");

   }
 
   delay(1000);
}
