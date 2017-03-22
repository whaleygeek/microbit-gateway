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

David Whale

@whaleygeek

22nd March 2017


