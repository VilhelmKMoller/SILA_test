// Arduino Code for a thermistor based thermometer.
// source: http://www.circuitbasics.com/arduino-thermistor-temperature-sensor-tutorial/
// serial port output (in degree Celsius) :
// T:NN.NN,
// tesed with Arduino Uno and Teensy 3.6

#define I_MAX 314
#define SCALE 10

int LED_YELLOW = 17;
int ThermistorPin = 15; // = A0 Arduino analog input pin of A/D converter
int LightResistorPin = 16;


int Vo;
float Vlight;

float R1 = 10000; // please adjust: resistor of voltage divider
float logR2, R2, T;
float c1 = 1.009249522e-03, c2 = 2.378405444e-04, c3 = 2.019202697e-07;

void setup() {
  Serial.begin(115200);
  // switching inbuild LED on to indicate operation
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(LED_YELLOW, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH);
}

void loop() {

  for(int i=0; i<I_MAX; i++){

    T = sin(i*0.1)*SCALE;

  // Vlight = analogRead(LightResistorPin);
  Vlight = random(0, 10); // 10.0; // a random decimal number from 0.00 to 0.99
  // Vo = analogRead(ThermistorPin);
  R2 = R1 * (1023.0 / (float)Vo - 1.0);
  logR2 = log(R2);
  T = T + 273.15;

  // Steinhart-Hart equation
  // T = (1.0 / (c1 + c2*logR2 + c3*logR2*logR2*logR2));
  // T = T - 273.15;

  // remove this comment, if you want to have temp. values based on Fahrenheit unit.
  /* T = (T * 9.0)/ 5.0 + 32.0; */

  Serial.print("T:");
  Serial.print(T);
  Serial.print(", L:");
  Serial.println(Vlight);
    delay(1000); // Just waiting 1/2 second before sending the next temperature
  }
  blink();
}




void blink()
{
  digitalWrite(LED_YELLOW, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(500);                      // wait for a second
  digitalWrite(LED_YELLOW, LOW);   // turn the LED off by making the voltage LOW
  delay(500);                      // wait for a second
}