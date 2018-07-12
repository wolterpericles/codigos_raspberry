// Firmware para atmega328

void setup()
{
  Serial.begin(9600); 
}

void loop()
{
  // lendo porta analogica A0
  int entrada0 = analogRead(0);
  // lendo porta analogica A1
  int entrada1 = analogRead(1);
  // imprimir serial
  Serial.print(entrada0);
  Serial.print(" ");
  Serial.print(entrada1);
  Serial.print("\n");

  delay(50);
}