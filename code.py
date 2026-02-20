#import the usb stuff
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.mouse import Mouse
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
import usb_hid

#import pins
from digitalio import DigitalInOut, Direction, Pull
import gfx
import machine
import uos
import busio
import board
import microcontroller

#import the display stuff
import time
import adafruit_framebuf
import adafruit_ssd1306

#setting up the i2c pins and display
i2c = busio.I2C(board.GP1, board.GP0)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
display.fill(0)

graphics = gfx.GFX(128, 32, display.pixel, hline=fast_hline, vline=fast_vline)

#create buttons
button1 = board.GP13
button2 = board.GP8
button1 = board.GP3

#setting up the usb
kbd = Keyboard(usb_hid.devices)
m = Mouse(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)

current_type = 0

#define the macros
modeltypes = {
    1: "sleep timer",
    2: "2",
    3: "3"
    }

#how long the sleep timer lasts for, in the future, it will be able to be controlled by a pentometer
timerlength = 3600

#makes the loop loop:
loop = "true"

while loop == "true":
    print("Macro pad ready")
    #check if the only button being pressed is button1
    if current_type == 0 and button1.pressed == true and button2.pressed == false and button3.pressed == false:
        current_type = 1
    #check if the only button being pressed is button2 
    elif current_type == 0 and button1.pressed == false and buttton2.pressed == true and button3.pressed == false:
        current_type = 2
    #check if the only button being pressed is button3
    elif current_type == 0 and button1.pressed == false and buttton2.pressed == false and button3.pressed == true:
        currrent_type = 3
    print(str(modeltypes[current_type]))
    display.text(str(modeltypes[current_type]),0,0)
    display.show()
    if current_type == 1:
        #sleeps for the length of the timer, then presses pause on the usb device
        print("timer set for")
        print(timerlength)
        display.text("timer set for",0,0)
        display.text(timerlength,0,12)
        display.show()
        timer.sleep(timerlength)
        current_type = 0
        cc.send(ConsumerControlCode.PLAY_PAUSE)
    display.fill(0)