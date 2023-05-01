# Bewegungsmelder - Howto



## Verkabelung 

<!--- Bild und Quellenangabe der Verkablung -->

![](img/wired/pir-motion.png)

Abb.: [Handbuch KS0365 Sensor Kit](../material/keystudio/KS0361(KS0365)%20Microbit%20V2.0%20Sensor%20Learning%20Kit.pdf) S. 149

---

## Code

<!--- code Beispiel: kann später von Github copy & pasted werden  -->

```python
from microbit import display, Image, pin0

while True:
  
    if pin0.read_digital() == 1:
        display.show(Image.HEART)
    else:
        display.show(Image.HEART_SMALL)
```

---


## Quellen 

<!--- Bitte alle Quellen angeben -->

Abb.: [Handbuch KS0365 Sensor Kit](../material/keystudio/KS0361(KS0365)%20Microbit%20V2.0%20Sensor%20Learning%20Kit.pdf) S. 149