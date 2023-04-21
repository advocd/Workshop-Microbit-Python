# from microbit import *
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