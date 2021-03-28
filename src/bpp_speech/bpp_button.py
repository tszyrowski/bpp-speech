import signal

import gpiozero

import bpp_btn_callback


def btn_listening():
    """Listen to the button action all the time."""
    btn = gpiozero.Button(21)
    btn.when_pressed = bpp_btn_callback.cb_btn_pressed
    signal.pause()


if __name__ == "__main__":
    btn_listening()
