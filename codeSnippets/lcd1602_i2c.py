from microbit import i2c, sleep
from scan_for_i2c_addr import *


#set LCD Address
# LCD_I2C_ADDR=0x27
LCD_I2C_ADDR=scanner()
LCD_I2C_ADDR=scanner()


#Source: https://github.com/shaoziyang/microbit-lib/blob/master/lcd/I2C_LCD1602/mb_i2c_lcd1602.py

class Mensch():
    anzahlDerKnochen=234


    def __str__(self):
        return self._name + " alter: " + str(self._alter)
        
    def __init__(self, name="Anonymos", alter=19):
        """Form a complex number.

        Keyword arguments:
        alter = dein Alter
        name = dein Name
        """
        self._name = name
        self._alter = alter
        self._adr=LCD_I2C_ADDR

 
    def getName(self):
        return self._name
    
    def getAlter(self):
        return self._alter


class LCD1620():
    def __init__(self):
        self.buf = bytearray(1)
        #self.buf = 0x00
        self.BK = 0x08
        self.RS = 0x00
        self.E = 0x04
        self.setcmd(0x33)
        sleep(5)
        self.send(0x30)
        sleep(5)
        self.send(0x20)
        sleep(5)
        self.setcmd(0x28)
        self.setcmd(0x0C)
        self.setcmd(0x06)
        self.setcmd(0x01)
        self.version='1.0'

        


    def setReg(self, dat):
        self.buf[0] = dat
        i2c.write(LCD_I2C_ADDR, self.buf)
        sleep(1)

    def send(self, dat):
        d=dat&0xF0
        d|=self.BK
        d|=self.RS
        self.setReg(d)
        self.setReg(d|0x04)
        self.setReg(d)

    def setcmd(self, cmd):
        self.RS=0
        self.send(cmd)
        self.send(cmd<<4)

    def setdat(self, dat):
        self.RS=1
        self.send(dat)
        self.send(dat<<4)

    def clear(self):
        self.setcmd(1)

    def backlight(self, on):
        if on:
            self.BK=0x08
        else:
            self.BK=0
        self.setcmd(0)

    def on(self):
        self.setcmd(0x0C)

    def off(self):
        self.setcmd(0x08)

    def shl(self):
        self.setcmd(0x18)

    def shr(self):
        self.setcmd(0x1C)

    def char(self, ch, x=-1, y=0):
        if x>=0:
            a=0x80
            if y>0:
                a=0xC0
            a+=x
            self.setcmd(a)
        self.setdat(ch)

    def puts(self, s, x=0, y=0):
        if len(s)>0:
            self.char(ord(s[0]),x,y)
            for i in range(1, len(s)):
                self.char(ord(s[i]))