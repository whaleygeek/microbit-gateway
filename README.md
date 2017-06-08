# microbit-gateway
A simple gateway onto the micro:bit radio network

## Getting started

Press CLONE OR DOWNLOAD

choose DOWNLOAD ZIP

Unzip the zip file

## IMPORTANT NOTE

If you are sharing radio payloads between PXT and MicroPython,
note there are differences in the payload format. Please read this
article to find out about this:

https://support.microbit.org/solution/articles/19000053168-receiving-radio-data-from-pxt-within-python

I have provided two sets of sample hex files, one for using with PXT, one for using with MicroPython.
If your 'user programs' at the remote micro:bit end are in a specific language, please use the
correct .hex file for the gateway, so you don't have to mess about with the different payload
formats between MicroPython and PXT.

## Using PXT payloads mode

Use this if your users will be writing PXT programs at the micro:bit remote ends.

In the src/for_microbit folder are some zip files, you need:

```
microbit-demo-pxt.hex.zip
microbit-gateway-pxt.hex.zip
```

Unzip these, flash microbit-gateway-pxt.hex onto a gateway micro:bit,
and flash microbit-demo-pxt.hex onto a number of other micro:bits

Power all the demo micro:bits from batteries.

Plug the gateway micro:bit into your computer via the USB lead

run the gateway.py python program (in Python2, note no Python 3 support yet)

It will ask you to unplug your micro:bit, press ENTER, then plug it
in and press ENTER again. Finally it will show you the port name of
the discovered micro:bit and ask you if you want to remember it - press
Y then enter.

The demo program is now running.

The demo program sends a counting number once per second. All your
demo micro:bits should receive and display this number.

If you press A or B on any of your demo micro:bits, you should see
that appear on the console screen of your host computer.


## Using MicroPython payloads mode

Use this if your users will be writing MicroPython programs at the micro:bit remote ends.

In the src/for_microbit folder are some zip files, you need:

```
microbit-demo-python.hex.zip
microbit-gateway-python.hex.zip
```

Unzip these, flash microbit-gateway-python.hex onto a gateway micro:bit,
and flash microbit-demo-python.hex onto a number of other micro:bits

Power all the demo micro:bits from batteries.

Plug the gateway micro:bit into your computer via the USB lead

run the gateway.py python program (in Python2, note no Python 3 support yet)

It will ask you to unplug your micro:bit, press ENTER, then plug it
in and press ENTER again. Finally it will show you the port name of
the discovered micro:bit and ask you if you want to remember it - press
Y then enter.

The demo program is now running.

The demo program sends a counting number once per second. All your
demo micro:bits should receive and display this number.

If you press A or B on any of your demo micro:bits, you should see
that appear on the console screen of your host computer.



## What's next

What comes next is up to you. Any time you use process_outgoing()
in your python code, it sends it to all micro:bits wirelessly.

Every time a micro:bit sends data via the radio network, it will
be processed by the process_incoming() function in your python code.

You could for example use this as a basis for retrieving data from a
web page or online data source (e.g weather data) and sending it
to all micro:bits wirelessly for processing.

Alternatively, you could get it so that every time you do something
on a micro:bit, it sends something up to an internet data service.

If you want any form of 'addressing' in your micro:bits, you'll have
to add this yourself. But this demo should be more than enough to
get you started with internet connecting your micro:bits, or doing
anything where you want to control things on (or from) a main
computer.

## TODO LIST

1. Add in support for Python 3 (bring in Pyserial 3.3 and fixes from other
projects to make this work)

2. add an outer protocol wrapper that allows radio commands to be
actioned by the gateway micro:bit (e.g. change channel, change frequency,
reset radio, change bitrate) in addition to transparrent data transfer

3. add a host-side for the protocol wrapper, and surface the API on the host
side identically to the MicroPython radio API - e.g. so that Pi driven
Python code could do frequency hopping based communications.

4. add in support for multiple micro:bits, all tuned to different channels
(to improve the performance of a Pi based gateway that communicates
on different channels)

5. Find a way to remove the restriction of the MicroPython CTRL-C
problem to allow transparent binary data (perhaps wrap this up in
the wrapping protocol with byte stuffing) so that true binary data
can be sent in both directions without MicroPython stopping.

David Whale

@whaleygeek

8th June 2017


