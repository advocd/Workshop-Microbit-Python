from microbit import pin0, sleep

while True:
    print(pin0.read_analog())
    sleep(500)
