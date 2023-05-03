# micro:bit accelerometer - Howto

## Überblick

<!--- kurze Einführung -->

In Smartphones ist zur Bestimmung der Bewegungsrichtung ein Accelerometer verbaut. 
Auch der micro:bit ist mit einem solchen Beschleunigungssensor ausgestattet.

---

## Code

<!--- code Beispiel: kann später von Github copy & pasted werden  -->

```python
from microbit import accelerometer, display, Image, sleep

while True:
    if accelerometer.was_gesture("shake"):
        display.show(Image.CONFUSED)
        sleep(2000)
        display.clear()

    if accelerometer.was_gesture("left"):
        display.show(Image.ARROW_W)
        sleep(2000)
        display.clear()
    
    if accelerometer.was_gesture("right"):
        display.show(Image.ARROW_E)
        sleep(2000)
        display.clear()
```

---

## Mögliche Probleme

<!--- Wenn Probleme bekannt sind bitte hier aufführen -->

Gesten werden nicht automatisch im Hintergrund geupdatet. Die Gesten müssen dauerhaft
mit einer entsprechenden Funktion abgefragt werden. In den meisten Fällen reicht eine
Schleife mit der Funktion und einer kleinen Auszeit über `sleep()`. (siehe Beispiel oben)

---

## Quellen

<!--- Bitte alle Quellen angeben -->

[micro:bit Dokumentation](https://microbit-micropython.readthedocs.io/en/v2-docs/accelerometer.html)