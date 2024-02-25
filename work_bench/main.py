from microbit import pin0, sleep

while True:
    s = pin0.read_analog()
    sleep(1000)
    print("Lautstärke:",s)
