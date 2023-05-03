# micro:bit microphone - Howto

## Überblick

<!--- kurze Einführung -->

Mit dem eingebauten Mikrofon kann der micro:bit Übergänge von Laut zu Leise 
und umgekehrt erkennen.

---

## Code

<!--- code Beispiel: kann später von Github copy & pasted werden  -->

```python
from microbit import microphone, display, sleep
microphone.set_threshold(SoundEvent.LOUD,10)
on = False
while True:
    if microphone.is_event(SoundEvent.LOUD):
        on = not on
    if on:
        display.show()
        sleep(100)
    else:
        display.clear()
        sleep(100)
```

---

## Mögliche Probleme

<!--- Wenn Probleme bekannt sind bitte hier aufführen -->

Wenn das Mikrofon zu empfindlich oder gar nicht reagiert, muss der Grenzwert der Lautstärke
angepasst werden. Das erfolgt über `microphone.set_threshold(SoundEvent.LOUD oder .QUIET,0-255)`.

---

## Quellen

<!--- Bitte alle Quellen angeben -->

[micro:bit Dokumentation](https://microbit-micropython.readthedocs.io/en/v2-docs/microphone.html)
