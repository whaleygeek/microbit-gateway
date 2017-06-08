from microbit import *
import radio

radio.config(group=0)
radio.on()

uart.init(baudrate=115200)

def print(*args, **kwargs):
    pass # disable print function

display.show("-")
while True:
    try:
        msg = radio.receive()
        if msg is not None:
            display.show("_")
            uart.write(msg + "\r")

        msg = uart.readline()
        if msg is not None:
            display.show("^")
            radio.send(msg)
    except:
        display.show("X")
        radio.off()
        sleep(250)
        radio.on()
        display.show("-")
    