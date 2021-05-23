"""Main entry point for speech recognition"""
import glob
import os.path
import re
import subprocess  # nosec
import signal
import random

import gpiozero
import speech_recognition as sr


SPEECH_ENG_PATH = "/home/pi/bpp/mimic1/mimic"
DATA_PATH = "/home/pi/bpp/data"
last_cmd = ["last", "lost", "lust", "loose", "us"]
average_cmd = ["average", "coverage"]


def read_last_reading():
    files = glob.glob(DATA_PATH + "/*txt")
    latest_file = max(files, key=os.path.getctime)
    with open(latest_file, "r") as f:
        last_line = f.readlines()[-1].split(",")
        HR = int(re.sub('\D', '', last_line[-2]))
        SPX = int(re.sub('\D', '', last_line[-1]))
        print(HR, SPX, last_line)
    return HR, SPX


def read_average_reading():
    files = glob.glob(DATA_PATH + "/*txt")
    latest_file = max(files, key=os.path.getctime)
    with open(latest_file, "r") as f:
        last_lines = f.readlines()
        HR = 0
        SPX = 0
        i = 0
        for line in last_lines:
            HR += int(re.sub('\D', '', line.split(",")[-2]))
            SPX += int(re.sub('\D', '', line.split(",")[-1]))
            i += 1
    return HR/i, SPX/i


def speak_back(text=None, voice="ap"):
    """Use espeak to convert text to speech."""
    HR, SPX = read_last_reading()
    if text is None:
        text = ("Hello, this is your breath project. Your oxygen level " +
        f"was {SPX} % and your hart-rate was {HR} bpm.")
    return subprocess.run(  # nosec
        [SPEECH_ENG_PATH, "-t", f"{text}", "-voice", f"{voice}"]
    ).returncode


def call_ask_for_cmd(voice="ap"):
    """Call welcome and speech command request."""
    print("Say command!")
    return subprocess.run(  # nosec
        [SPEECH_ENG_PATH, "-t", "Hello, how can I help?", "-voice", f"{voice}"]
    ).returncode


def call_last_reading():
    """Call function reading last reading."""
    print("RETURNING LAST READINGS")
    HR, SPX = read_last_reading()
    text = [
        f"Hello, this is your breath project. Your oxygen level was {SPX} % and your hart-rate was {HR} bpm.",
        f"How are you today? your last oxygen level was {SPX} % and {HR} bpm hart rate",
        f"Hope you well, last oxygen level is {SPX} % and hart rate is {HR} bpm "
    ]
    speak_back(text=random.choice(text), voice="ap")


def call_average_reading():
    """Call function returning average."""
    print("RETURNING AVERAGE READINGS")
    HR, SPX = read_average_reading()
    text = f"Your today average reading for oxygen level was {SPX} % and for hart-rate was {HR} bpm."
    speak_back(text=text, voice="ap")


def call_cannot_understand(speech_cmd):
    """Call function informing sentence does not much possiblities."""
    print(f"can not understand, did you say: {speech_cmd}")
    HR, SPX = read_last_reading()
    text = [
        f"I am not sure what you ask but last Your oxygen level was {SPX} % and your hart-rate was {HR} bpm.",
        f"I think you asked for last reading so your last Your oxygen level was {SPX} % and your hart-rate was {HR} bpm.",
        f"well, I am not celar what you asked but your last Your oxygen level was {SPX} % and your hart-rate was {HR} bpm.",
    ]
    speak_back(text=random.choice(text), voice="ap")


def call_unrecognised_cmd():
    """Call speech did not much any recognaisable input."""
    print("Sphinx could not understand audio")
    HR, SPX = read_last_reading()
    text = f"I am not sure what you ask but last Your oxygen level was {SPX} % and your hart-rate was {HR} bpm."
    speak_back(text=text, voice="ap")


def call_general_error(e):
    """Call general output occured."""
    print("Sphinx error; {0}".format(e))
    text = ("Error occured")
    speak_back(text=text, voice="ap")


def bpp_recognise():
    """Recognise command from microphone."""
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # handle ambient noise, analyzes the audio source for one second
        # r.adjust_for_ambient_noise(source)
        call_ask_for_cmd()
        # records input from the source until silence is detected.
        # Will stop if nothing detected for 5 seconds or
        # after 15 seconds of listening
        audio = r.listen(source, timeout=2, phrase_time_limit=5)

    # recognize speech using Sphinx
    try:
        speech_input = r.recognize_sphinx(audio)
        speech_cmd = speech_input.split(" ")
        print(f"Recognised cmd: {speech_cmd}")
        if any(word in speech_cmd for word in last_cmd):
            call_last_reading()
        if any(word in speech_cmd for word in average_cmd):
            call_average_reading()
        else:
            call_cannot_understand(speech_cmd)

    except sr.UnknownValueError:
        call_unrecognised_cmd()
    except sr.RequestError as e:
        call_general_error(e)

def cb_btn_pressed():
    """Get callback for button press."""
    print("* * * BUTTON PRESSED * * *")
    bpp_recognise()


def btn_listening():
    """Listen to the button action all the time."""
    btn = gpiozero.Button(21)
    btn.when_pressed = cb_btn_pressed
    signal.pause()


if __name__ == "__main__":
    btn_listening()
