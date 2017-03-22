import microbit # will auto-connect
import time

SEND_RATE = 1.0 # seconds

def process_incoming(msg):
    print("received:%s" % str(msg)
    #Add your incoming message processing here
    #any radio message sent by any microbit, will arrive here

def process_outgoing():
    # Example of sending a message on a timer
    # Just call microbit.send_message whenever you have new data
    # this will be sent to the gateway micro:bit which will then
    # broadcast it to all listening micro:bit devices
    microbit.send_message("HELLO")

next_send = time.time() + SEND_RATE

print("gateway running")

while True:
    msg = microbit.get_next_message()
    if msg is not None:
        process_incoming(msg)

    now = time.time()
    if now >= next_send:
       next_send = now + SEND_RATE
       process_outgoing()

