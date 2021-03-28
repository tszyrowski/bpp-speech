import signal

import gpiozero

import bpp_speech.bpp_speech_recognition


def cb_btn_pressed():
    """Get callback for button press."""
    print("* * * BUTTON PRESSED * * *")
    bpp_speech.bpp_speech_recognition.bpp_recognise()


def btn_listening():
    """Listen to the button action all the time."""
    btn = gpiozero.Button(21)
    btn.when_pressed = cb_btn_pressed
    signal.pause()


if __name__ == "__main__":
    btn_listening()
