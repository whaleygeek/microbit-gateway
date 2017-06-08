from microbit import *
import radio

radio.config(group=0)
radio.on()

display.show("-")

while True:
    if button_a.was_pressed():
        radio.send("A")
    if button_b.was_pressed():
        radio.send("B")

    try:
        msg = radio.receive()
        if msg is not None:
            if len(msg) > 0:
                display.show(msg)
    except:
        display.show("X")
        radio.off()
        sleep(250)
        radio.on()
        display.show("-")
