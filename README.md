# Raspberry pi pico macro pad

## *CURRENTLY BROKEN - PLEASE HELP* ##

## Main goal: trying to make a begginer-friendly macro pad using the raspberry pi pico ##

## Python version: circuit python v10. ##

## Libraries required: 
* adafruit_ssd1306,
* adafruit_hid,
* adafruit_framebuffer

Have a look in the examples folder as well as the links below to see info about the libaries required:

* https://github.com/adafruit/Adafruit_CircuitPython_framebuf?tab=readme-ov-file
* https://github.com/adafruit/Adafruit_CircuitPython_HID
* https://github.com/adafruit/Adafruit_SSD1306

## Actions it can execute: ##

* Sleep timer - waiting for 1 hour(default - in the future, it will be able to be controlled by a pentiometer), then    using the usb_hid protocol to send a play or pause signal to the device it is plugged into.

* and more coming soon!
