#Scan for LCD Address
from microbit import i2c
# Adr=0
def scanner():
    # global Adr
    Adr=i2c.scan()
    return(0x27)
    # return(hex(Adr[0]))
