from microbit import button_a, pin7, display

""" 
Wir verbinden den buzzer mit p7 in diesem bsp. natürlich kann er auch mit 
jedem anderen pin verbunden werden. 

Beachten p3, p4, p6, p7, p10 sind im Display mode,
das bedeudet, wenn wir diese Pins verwenden müssen wir das Display vom 
Microbit deaktivieren, da wir sonst möglicherweise falsche Werte erhalten 
und/oder das Display seltsame Dinge anzeigt. 
Siehe Handbuch S. 11:  
(4) Notes for the application of Micro:bit main board V2.0 - Abs. D
"""
display.off()
pin7.write_digital(0) # sichergehen das der buzzer aus ist beim start

while True:
    # solang button a gedrückt wird...
    if button_a.is_pressed():
        # ...hören wir ein Signal 
        pin7.write_digital(1)

    # ...button a wird losgelassen (ist nicht gedrückt)
    else:
        #das Signal verstummt
        pin7.write_digital(0)