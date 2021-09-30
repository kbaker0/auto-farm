void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  Serial.println("READY: 1-Turn LED on; 0-Turn LED off");
}

/*
a | Get lights status | on/off
b | Get pH level | ?
c | Get ambient temperature | C
d | Get ambient humidity | ?
e | Get water temperature | C
f | Get water level | ?
g | Get electric conductivity | ?
h | Get light reading | ?
0 | Get simulated lights status | on/off
1 | Get simulated simulated pH level | ?
2 | Get simulated ambient temperature | C
3 | Get simulated ambient humidity | ?
4 | Get simulated water temperature | C
5 | Get simulated water level | ?
6 | Get simulated electric conductivity | ?
7 | Get simulated light reading | ?
w | Lights off | None
x | Lights on | RRGGBB
y | Simulate lights off | None
z | Simulate lights on | RRGGBB
*/

void loop() {
  if (Serial.available() > 0) {
    char data = Serial.read();
    char str[2];
    str[0] = data;
    str[1] = '\0';
    Serial.println(str);
    if ( str[0] == '1' ) {
      digitalWrite(LED_BUILTIN, HIGH);
      Serial.println("Lights on...");
      delay(500);
    } else if ( str[0] == '0' ) {
      digitalWrite(LED_BUILTIN, LOW);
      Serial.println("Lights off...");
      delay(500);
    }
    Serial.flush();
  }
}
