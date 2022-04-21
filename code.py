# SPDX-FileCopyrightText: 2022 David Glaude
# SPDX-License-Identifier: MIT

import busio
import board
import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_hid.mouse_abs import Mouse
from wiichuck.udraw import UDraw

# simple range mapper, like Arduino map() <= From https://github.com/todbot/circuitpython-tricks#map-an-input-range-to-an-output-range
def map_range(s, a1, a2, b1, b2):
    return  b1 + ((s - a1) * (b2 - b1) / (a2 - a1))

# To create I2C bus on specific pins

#i2c = busio.I2C(board.SCL1, board.SDA1)  # QT Py RP2040 STEMMA connector
#udraw = UDraw(i2c)

udraw = UDraw(board.STEMMA_I2C())

m = Mouse(usb_hid.devices)

# mouse_abs accept value from 0 to 32767 for both X and Y
# Note: Values are NOT pixels! 32767 = 100% (to right or to bottom)

# uDraw provide value from 0 to 4095 for both X and Y
# Note: nor X nor Y cover the full range of value

# Please adjust calibration for your uDraw GameTablet
cal_min_x=110
cal_max_x=1950
cal_min_y=2650
cal_max_y=3980

zDown = False
pDown = False

oldx = 4095
oldy = 4095

while True:
    # We don't use the pressure, maybe converting to watcom protocol would permit that
    position, buttons, _ = udraw.values

    P = buttons.tip or buttons.C  # Both the C button and tip work as LEFT mouse click

    # Handeling the button to create mouse click
    if P and not pDown:
        m.press(Mouse.LEFT_BUTTON)
        pDown = True
    elif not P and pDown:
        m.release(Mouse.LEFT_BUTTON)
        pDown = False

    if buttons.Z and not zDown:
        m.press(Mouse.RIGHT_BUTTON)
        zDown = True
    elif not buttons.Z and zDown:
        m.release(Mouse.RIGHT_BUTTON)
        zDown = False

    # Values (4095,4095) mean the pen is not near the tablet
    if position.x == 4095 or position.y == 4095:
        oldx = 4095
        oldy = 4095
        continue  # We remember that the pen was raised UP

    # If we reach here, the pen was UP and is now DOWN
    if oldx == 4095 or oldy == 4095:
        oldx = position.x
        oldy = position.y
        continue

    if (position.x != oldx) or (position.y != oldy):  # PEN has moved we move the HID mouse
        oldx = position.x
        oldy = position.y
        x = oldx
        y = 4095-oldy
        print(x, y)
        m.move(
            int(map_range( x, cal_min_x, cal_max_x, 0, 32767 )),
            int(map_range( y, cal_min_y, cal_max_y, 0, 32767 )), 0)
