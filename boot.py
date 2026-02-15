import usb_hid

usb_hid.enable(
    (usb_hid.Device.KEYBOARD,
     usb_hid.Device.MOUSE,
     USB_hid.Device.CONSUMER_CONTROL)
)