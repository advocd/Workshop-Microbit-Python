# micro:bit compass - Howto

## Überblick

<!--- kurze Einführung -->

In Smartphones ist zur Bestimmung der Ausrichtung ein Magnetometer verbaut. 
Auch der micro:bit ist mit einem solchen digitalen Kompass ausgestattet.

---

## Code

<!--- code Beispiel: kann später von Github copy & pasted werden  -->

Beispiel Kompass:

```python
from microbit import display, Image, sleep, compass

compass.calibrate()

while True:
    direction = compass.heading()
    if direction < 23 and direction > 327:
        display.show(Image.ARROW_N)
    if direction > 24 and direction < 68:
        display.show(Image.ARROW_NE)
    if direction > 69 and direction < 113:
        display.show(Image.ARROW_E)
    if direction > 114 and direction < 158:
        display.show(Image.ARROW_SE)
    if direction > 159 and direction < 203:
        display.show(Image.ARROW_S)
    if direction > 204 and direction < 248:
        display.show(Image.ARROW_SW)
    if direction > 249 and direction < 293:
        display.show(Image.ARROW_W)
    if direction > 294 and direction < 328:
        display.show(Image.ARROW_SW)
```

Beispiel Schalter:

```python
from microbit import compass, display, Image

baseline = compass.get_field_strength() # Take a baseline reading of magnetic strength

while True:
  if abs(compass.get_field_strength() - baseline) > 50000:
      # Magnetic field strength increased by 10000
      display.show(Image.NO)    # Show a cross symbol
  else:
      display.clear()
```

---

## Mögliche Probleme

<!--- Wenn Probleme bekannt sind bitte hier aufführen -->

Das verbaute Magnetometer ist nicht sehr exakt beim Ermitteln des geografischen Nordens.
Die angegebene Richtung ist nur annäherungsweise richtig und kann durch nahegelegene 
magnetische Felder stark gestört werden.

---

## Quellen 

<!--- Bitte alle Quellen angeben -->

[Schalter Code](https://learn.adafruit.com/micro-bit-lesson-1-using-the-built-in-sensors/magnetometer)

[micro:bit Dokumentation](https://microbit-micropython.readthedocs.io/en/v2-docs/compass.html)