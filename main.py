import vgamepad as vg
import time
import keyboard
import random

print("macropad started")

active = False
gamepad: vg.VX360Gamepad | None = None


def swtch_state():
    global active
    active = not active


keyboard.add_hotkey("f2", swtch_state)
print("press 'f2' to switch gamepad on/off")

try:
    while True:
        if active:
            if gamepad is None:
                gamepad = vg.VX360Gamepad()
                print("gamepad on")
        else:
            if gamepad is not None:
                del gamepad
                gamepad = None
                print("gamepad off")
        if gamepad is not None:
            gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()
            time.sleep(random.uniform(0.1, 0.5))
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()
        time.sleep(2.5)
except KeyboardInterrupt:
    pass

if gamepad is not None:
    del gamepad

print("macropad end")
