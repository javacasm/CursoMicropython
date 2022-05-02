/*
  Basado en Physical Pixel

  https://www.arduino.cc/en/Tutorial/BuiltInExamples/PhysicalPixel
*/

const int ledPin = 13; // the pin that the LED is attached to

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
}
long last_mesg = millis();
void loop() {
  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    int incomingByte = Serial.read();
    // if it's a capital H (ASCII 72), turn on the LED:
    switch (incomingByte ) {
     case 10: // fin de linea, no hacemos nada
      break;
     case 'H':
      digitalWrite(ledPin, HIGH);
      Serial.println("Led On");
      break;
     case 'L':
      digitalWrite(ledPin, LOW);
      Serial.println("Led Off");
      break;
     case 'T':
      Serial.print(last_mesg);
      Serial.print(' ');
      Serial.println(millis());
      break;
     default:
      Serial.print(incomingByte);
      Serial.println(" comando desconocido");
      break;
    }
      
  }
  long now = millis();
  if (now - last_mesg >= 2000) {
    Serial.println(now);
    last_mesg = now;
  }
}
