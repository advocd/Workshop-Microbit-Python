from microbit import display, Image, pin0

while True:
    """
    hier ist auch pin0.read_digital() möglich, 
    dann ist der Wert aber 0 und 1 (Int) und nicht 
    True oder False
    """
    if pin0.is_touched():
        display.show(Image.HEART)
        print("touched")
    else:
        display.show(Image.HEART_SMALL)
        print('not touched')
