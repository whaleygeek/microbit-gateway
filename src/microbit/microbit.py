# microbit.py    15/09/2015    D.J.Whale

"""A serial port connection to a micro:bit"""

# No specific protocol is implied by this interface.
# This just provides a generic transport adaptor to a micro:bit via pyserial

# This was cloned (as a starting point) from the mb_remote project.
# That project came originally from github.com/whaleygeek/anyio.

# NOTE: this is currently written to auto scan, and only supports a single
# micro:bit instance. It might be rewritten later to support any number
# of instances (identification then gets interesting and application specific!)


#----- CONFIGURATION -----------------------------------------------------------

# Choose an embedded pyserial (for ease of distribution).
# Change this flag if you want to use the system installed version.

DEBUG = False
USE_EMBEDDED_PYSERIAL = True
BAUD = 115200

if USE_EMBEDDED_PYSERIAL:
    from os import sys, path
    thisdir = path.dirname(path.abspath(__file__))
    sys.path.append(thisdir)

import serial


#----- PORTSCAN ----------------------------------------------------------------

# This will check for the portscan.cache file with a remembered serial port
# identifier. If that exists, it will just use the serial port identified
# in that file. If the file does not exist, it performs a workflow that
# prompts the user. Note that if you plug your micro:bit into a different
# USB port or use a different USB hub configuration, this may renumber
# the port and require a re-scan. Just delete the portscan.cache file
# and re-run your app code, if that happens.

import portscan

name = portscan.getName()
if name != None:
    if DEBUG:
        print("Using port:" + name)
    PORT = name
else:
    name = portscan.find()
    if name == None:
        raise ValueError("No port selected, giving in")
    PORT = name
    print("Your micro:bit has been detected")
    print("Now running your program...")


#----- CONFIGURE SERIAL PORT ---------------------------------------------------

s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE
s.timeout = 0 # non blocking mode

s.close()
s.port = PORT
s.open()


#----- SERIAL PORT READ AND WRITE ENGINE --------------------------------------

line_buffer = ""
rec_buffer = None

def read_waiting():
    """Poll the serial and fill up rec_buffer if something comes in"""
    global rec_buffer
    if rec_buffer != None:
        return True

    line = process_serial()
    if line != None:
        rec_buffer = line
        return True

    return False


def read():
    """Poll the rec_buffer and remove next line from it if there is a line in it"""
    global rec_buffer

    if not read_waiting():
        return None

    rec = rec_buffer
    rec_buffer = None
    ##print("read:" + rec)
    return rec


def process_serial():
    """Low level serial poll function"""
    global line_buffer

    while True:
        data = s.read(1)
        if len(data) == 0:
            return None # no new data has been received
        data = data[0]

        if data == '\n':
            pass # strip newline

        elif data[0] == '\r':
            line = line_buffer
            line_buffer = ""
            ##print(line)
            return line

        else:
            line_buffer += data


#----- ADAPTOR ----------------------------------------------------------------

# This is here, so you can change the concurrency and blocking model,
# independently of the underlying code, to adapt to how your app wants
# to interact with the serial port.

# NOTE: This is configured for non blocking send and receive, but no threading
# and no callback handling.

def send_message(msg):
    """Send a message to the micro:bit.
        It is the callers responsibility to add newlines if you want them.
    """
    ##print("Sending:%s" % msg)

    s.write(msg)

def get_next_message():
    """Receive a single line of text from the micro:bit.
        Newline characters are pre-stripped from the end.
        If there is not a complete line waiting, returns None.
        Call this regularly to 'pump' the receive engine.
    """
    result = read()
    ##if result != None:
    ##    print("get_next_message:%s" % str(result))
    return result


# END
