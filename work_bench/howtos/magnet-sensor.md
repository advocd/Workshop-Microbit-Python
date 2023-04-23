# Magnet-Sensor (Reed-Sensor) - Howto

## Überblick

<!--- kurze Einführung -->
Mit dem reed Sensor können wir Magnetfelder erkennen. 

---

## Verkabelung 

<!--- Bild und Quellenangabe der Verkablung -->

Abb.: [Handbuch KS0365 Sensor Kit](../material/keystudio/KS0361(KS0365)%20Microbit%20V2.0%20Sensor%20Learning%20Kit.pdf) S. 158 

---

## Code

<!--- code Beispiel: kann später von Github copy & pasted werden  -->

```python
from microbit import pin0, Image, display

while True:
    
    if pin0.read_digital() == 0:
        print("0")
        display.show(Image.HEART)
    else:
        print("1")
        display.show(Image.HEART_SMALL)
```

---

## Mögliche Probleme

<!--- Wenn Probleme bekannt sind bitte hier aufführen -->
- nichts bekannt
---

## Quellen 

<!--- Bitte alle Quellen angeben -->

Abb.: [Handbuch KS0365 Sensor Kit](../material/keystudio/KS0361(KS0365)%20Microbit%20V2.0%20Sensor%20Learning%20Kit.pdf) S. S. 158 