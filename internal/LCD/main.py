from microbit import *
import mb_i2c_lcd1602
#Alias vergeben
l = mb_i2c_lcd1602.LCD1620()
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