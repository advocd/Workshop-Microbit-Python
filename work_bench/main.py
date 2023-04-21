import lcd1602_i2c
from microbit import pin0, sleep

# Zugriff auf LCD Display einrichten
l = lcd1602_i2c.LCD1620()

while True:
    # Analogen Wert von pin 0 auslesen
    value = pin0.read_analog()

    # Analogen Wert in Temperatur umrechnen
    temp = 300 * value / 1023 

    # auf seriellen Monitor ausgeben
    print(temp)

    # Temperatur auf LCD Display ausgeben
    l.puts("temp: " + str(temp))

    # 1000 Millisekunden warten 
    sleep(1000)





