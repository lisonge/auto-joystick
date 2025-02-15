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
    print('\033[F\033[K', end='')
    if active:
        print("gamepad on")
    else:
        print("gamepad off")


keyboard.add_hotkey("f2", swtch_state)
print("press 'f2' to switch gamepad on/off\n")

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
            time.sleep(random.uniform(0.1, 0.5))
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()
        time.sleep(2.5)
except KeyboardInterrupt:
    pass

if gamepad is not None:
    del gamepad

print("macropad end")
