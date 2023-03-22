from microbit import *
# Display löschen

while True:
    pin0.write_digital(1)
    print("test")
    sleep(1000)
    pin0.write_digital(0)
    sleep(1000)
