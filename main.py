import vgamepad as vg
import time

gamepad = vg.VX360Gamepad()

print("macropad started")
try:
    while True:
        gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
        gamepad.update()
        time.sleep(0.1)
        gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
        gamepad.update()
        time.sleep(2)
except KeyboardInterrupt:
    pass

del gamepad
print("macropad end")
