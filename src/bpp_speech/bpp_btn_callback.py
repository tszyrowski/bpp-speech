"""Callback recipies for button press."""
import bpp_speech_recognition


def cb_btn_pressed():
    """Get callback for button press."""
    print("* * * BUTTON PRESSED * * *")
    bpp_speech_recognition.bpp_recognise()
