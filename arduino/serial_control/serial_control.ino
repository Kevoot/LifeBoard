int latchPin = 5;
int clockPin = 6;
int dataPin = 4;

byte buf[2];

void setup() {
  Serial.begin(9600);
  pinMode(latchPin, OUTPUT);
  pinMode(dataPin, OUTPUT);
  pinMode(clockPin, OUTPUT);
  digitalWrite(latchPin, LOW);
  shiftOut(dataPin, clockPin, LSBFIRST, 0);
  shiftOut(dataPin, clockPin, LSBFIRST, 0);
  digitalWrite(latchPin, HIGH);
}

void loop() {
  delay(1000);
  if(Serial.available() > 1) {
    Serial.readBytes(buf, 2);
    digitalWrite(latchPin, LOW);
    // Has to be sent in reverse
    shiftOut(dataPin, clockPin, LSBFIRST, buf[1]);
    shiftOut(dataPin, clockPin, LSBFIRST, buf[0]);
    digitalWrite(latchPin, HIGH);
    // Send back confirmation
    Serial.write(buf[0]);
  }
}
