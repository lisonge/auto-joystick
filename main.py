import vgamepad as vg
import time
import keyboard
import random

print("macropad started")

click_gap = 0.2
active = False
gamepad: vg.VX360Gamepad | None = None


def swtch_state():
    global active
    active = not active
    if active:
        print("\rgamepad on ", end="")
    else:
        print("\rgamepad off ", end="")


keyboard.add_hotkey("f2", swtch_state)
print("press 'f2' to switch gamepad on/off")

try:
    while True:
        if active:
            if gamepad is None:
                gamepad = vg.VX360Gamepad()
        else:
            if gamepad is not None:
                del gamepad
                gamepad = None
        if gamepad is not None:
            gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()
            time.sleep(random.uniform(0.05, 0.1))
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()
        time.sleep(click_gap)
except KeyboardInterrupt:
    pass

if gamepad is not None:
    del gamepad

print("\nmacropad end")
