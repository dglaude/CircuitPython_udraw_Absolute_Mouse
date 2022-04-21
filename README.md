# CircuitPython_udraw_Absolute_Mouse

This is demonstration of custom USB_HID to make a mouse device that send absolute coordinate (as opposed to normal mouse that do relative move).
This is working on Windows (and maybe other operating system, not tested yet).

# Hardware

* second hand uDraw Wii GameTablet (it talk I2C and connect like a Nunchuck
* Adafruit Wii Nunchuck Breakout Adapter - Qwiic / STEMMA QT => https://www.adafruit.com/product/4836
* Stemma QT cable
* Feather RP2040 (should work with many board that hav, but avoid M0 as this code need long int)

# How to reproduce

Install the following libraries:
* Adafruit_CircuitPython_HID: https://github.com/adafruit/Adafruit_CircuitPython_HID
* wiichuck: https://github.com/jfurcean/CircuitPython_WiiChuck (from the Community Bundle: https://github.com/adafruit/CircuitPython_Community_Bundle/releases/)

Copy the file `mouse_abs.py` from this repo to the CIRCUITPY drive in /lib/adafruit_hid
Copy the files `boot.py` and `code.py` on your CIRCUITPY drive

# Demo

As seen on `Show and Tell` on 20/04/2022 : https://www.youtube.com/watch?v=belKMexuOZA&t=1310s

# Credit

The uDraw specific part is my piece of code and contribution to CircuitPython_WiiChuck.
Everything else has only been possible thanks to:
* @danh for all learn guide and the USB-HID code in the core of CircuitPython and in library
* @bitboy85 for providing working code for mouse_abs: https://gist.github.com/bitboy85/cdcd0e7e04082db414b5f1d23ab09005
* @jfurcean John Furcean for the WiiChuck library: https://github.com/jfurcean/CircuitPython_WiiChuck

