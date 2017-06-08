# microbit-gateway
A simple gateway onto the micro:bit radio network

## Getting started

Press CLONE OR DOWNLOAD

choose DOWNLOAD ZIP

Unzip the zip file

In the src/for_microbit folder are two zip files

Unzip these, flash microbit-gateway.hex onto a gateway micro:bit,
and flash microbit-demo.hex onto a number of other micro:bits

Power all the demo micro:bits from batteries.

Plug the gateway micro:bit into your computer via the USB lead

run the demo1.py python program

It will ask you to unplug your micro:bit, press ENTER, then plug it
in and press ENTER again. Finally it will show you the port name of
the discovered micro:bit and ask you if you want to remember it - press
Y then enter.

The demo program is now running.

The demo program sends a counting number once per second. All your
demo micro:bits should receive and display this number.

If you press A or B on any of your demo micro:bits, you should see
that appear on the console screen of your host computer.

## NOTE!!

If you are sharing radio payloads between PXT and MicroPython,
note there are differences in the payload format. Please read this
article to find out about this:

https://support.microbit.org/solution/articles/19000053168-receiving-radio-data-from-pxt-within-python

I will soon be adding a MicroPython based gateway example into this
project too, for people who want the remote micro:bits to be coded
entirely in MicroPython and for them to not need to worry about
packing the extra DAL header and PXT headers required when
sharing data between the two different languages.

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

## IDEAS LIST

1. add an outer protocol wrapper that allows radio commands to be
actioned by the gateway micro:bit (e.g. change channel, change frequency,
reset radio, change bitrate) in addition to transparrent data transfer

2. add a host-side for the protocol wrapper, and surface the API on the host
side identically to the MicroPython radio API - e.g. so that Pi driven
Python code could do frequency hopping based communications.

3. add in support for multiple micro:bits, all tuned to different channels
(to improve the performance of a Pi based gateway that communicates
on different channels)

4. Find a way to remove the restriction of the MicroPython CTRL-C
problem to allow transparrent binary data (perhaps wrap this up in
the wrapping protocol with byte stuffing) so that true binary data
can be sent in both directions without MicroPython stopping.

David Whale

@whaleygeek

22nd March 2017


