# Hardware Controller

This system interacts as a mediator between analog sensors and the Raspberry Pi. Since this system exists, we are also connecting all the digital hardware components as well. The controller runs on an Arduino-compatible system, and uses Arduino's C/C++ language.

### Get Commands

Code | Command | Unit | Values/Range
--- | --- | --- | ---
a | Get lights status | Boolean | on/off
b | Get pH level | ?
c | Get ambient temperature | Degrees C | X to Y
d | Get ambient humidity | ?
e | Get water temperature | Degrees C | X to Y
f | Get water level | ?
g | Get electric conductivity | Volt
h | Get light reading | ?
0 | Get simulated lights status | on/off
1 | Get simulated simulated pH level | ?
2 | Get simulated ambient temperature | Degrees C | X to Y
3 | Get simulated ambient humidity | ?
4 | Get simulated water temperature | Degrees C | X to Y
5 | Get simulated water level | ?
6 | Get simulated electric conductivity | Volt
7 | Get simulated light reading | ?

### Set Commands

Code | Command | Argument(s)
--- | --- | ---
w | Lights off | None
x | Lights on | RRGGBB
y | Simulate lights off | None
z | Simulate lights on | RRGGBB
