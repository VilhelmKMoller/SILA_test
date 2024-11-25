// Arduino Code for a thermistor based thermometer.
// source: http://www.circuitbasics.com/arduino-thermistor-temperature-sensor-tutorial/
// serial port output (in degree Celsius) :
// T:NN.NN,
// tesed with Arduino Uno and Teensy 3.6


int ThermistorPin = 15; // = A0 Arduino analog input pin of A/D converter

int Vo;
float R1 = 10000; // please adjust: resistor of voltage divider
float logR2, R2, T;
float c1 = 1.009249522e-03, c2 = 2.378405444e-04, c3 = 2.019202697e-07;

void setup() {
  Serial.begin(115200);
  // switching inbuild LED on to indicate operation
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH);
}

void loop() {
  Vo = analogRead(ThermistorPin);
  R2 = R1 * (1023.0 / (float)Vo - 1.0);
  logR2 = log(R2);
  // Steinhart-Hart equation
  T = (1.0 / (c1 + c2*logR2 + c3*logR2*logR2*logR2));
  T = T - 273.15;
  // remove this comment, if you want to have temp. values based on Fahrenheit unit.
  /* T = (T * 9.0)/ 5.0 + 32.0; */

  Serial.print("T:");
  Serial.print(T);
  Serial.println(",");

  delay(1000); // Just waiting 1/2 second before sending the next temperature
}
