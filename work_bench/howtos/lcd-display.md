# LCD Display - Howto

## Überblick
Der Microbit kommuniziert mit dem Display via der I2C Verbindung, welche auf der Rückseite des Displays befestigt ist. 

---

## Verkabelung 

![](img/wired/lcd-display.png)
Abb.: [Handbuch KS0365 Sensor Kit](../material/keystudio/KS0361(KS0365)%20Microbit%20V2.0%20Sensor%20Learning%20Kit.pdf) S. 218 ff

---

## Code

```python 
from microbit import *
import lcd1602_i2c
#Alias vergeben
l = lcd1602_i2c.LCD1620()
#Bildschirm Text anzeigen lassen
l.puts("Hello Microbit!")

while True:
    if button_a.is_pressed():
        l.clear()
        l.puts("It works!")
        sleep(500)
    if button_b.is_pressed():
        l.puts('It still works!',x=0,y=1)
        sleep(500)
    if pin_logo.is_touched():
        l.clear()
        break
```

---

## Mögliche Probleme

- evtl. Adresse falsch
  -  mit [scan_for_i2c_addr.py](../scan_for_i2c_addr.py) kann die aktuelle I2C Adresse ausgelesen werden
  -  anschließend korrigieren in [lcd1602_i2c.py](../lcd1602_i2c.py):
     -  `LCD_I2C_ADDR=0x27`

---

## Quellen 

- [Handbuch KS0365 Sensor Kit](../material/keystudio/KS0361(KS0365)%20Microbit%20V2.0%20Sensor%20Learning%20Kit.pdf) S. 218 ff
  
- Quellcode: angepasst auf Basis von: https://github.com/shaoziyang/microbit-lib/tree/master/lcd/I2C_LCD1602

