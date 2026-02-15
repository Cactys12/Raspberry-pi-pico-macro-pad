import usb_hid
import time
import busio
from machine import Pin
from board import SCL, SDA
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.mouse import Mouse
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button1 = Pin(3, Pin.IN, Pin.PULL_DOWN)

kbd = Keyboard(usb_hid.devices)
m = Mouse(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)

i2c = busio.I2C(SCL, SDA)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

display.fill(0)

current_type = 0
modeltypes = {
    1: "sleep timer",
    2: "2",
    3: "3"
    }
timerlength = 3600

while true:
    display.fill(0)
    if current_type == 0 and button1.value() == true and button2.value() == false and button3.value() == false:
        current_type = 1
    if current_type == 0 and button1.value() == false and buttton2.value() == true and button3.value() == false:
        current_type = 2
    if current_type == 0 and button1.value() == false and buttton2.value() == false and button3.value() == true:
        currrent_type = 3
    display.text(str(modeltypes[current_type]),0,0)
    display.show()
    if current_type == 1:
        display.text("timer set for"+timerlength,0,0)
        display.show()
        timer.sleep(timerlength)
        current_type = 0
