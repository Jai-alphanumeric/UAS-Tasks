// UAS Avionics Round 2 Task 2
// Jai A17/01
int ldr=A0;                               //Set A0(Analog Input) for LDR.
int value=0;
void setup() {
Serial.begin(9600);
pinMode(11,OUTPUT);
pinMode(A0,INPUT);
}

void loop() {
value=analogRead(ldr);                    //Reads the Value of LDR(light).
Serial.println("LDR value is :");         //Prints the value of LDR to Serial Monitor.
Serial.println(value);
if(value<256)
  {
    digitalWrite(11,HIGH);                //Makes the LED glow in Dark.
    delay(3000);
    digitalWrite(11,LOW);
    delay(3000);
  }
  else if (value>=256 && value<512)
  {
    digitalWrite(11, HIGH);
    delay(2000);
    digitalWrite(11,LOW);
    delay(2000);

  }
  else if (value>=512 && value<768)
  {
    digitalWrite(11, HIGH);
    delay(1000);
    digitalWrite(11,LOW);
    delay(1000);
  }
  else
  {
    digitalWrite(11,HIGH);                 //Turns the LED OFF in Light.
    delay(500);
    digitalWrite(11,LOW);
    delay(500);
  }
}
