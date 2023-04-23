from microbit import pin0, Image, display

while True:
    
    if pin0.read_digital() == 0:
        print("0")
        display.show(Image.HEART)
    else:
        print("1")
        display.show(Image.HEART_SMALL)