#!/usr/bin/env python3
import subprocess


SPEECH_ENG_PATH = "/home/pi/bpp/mimic1/mimic"


def speak_back(text, voice):
    """Use espeak to convert text to speech."""
    return subprocess.run(
        [SPEECH_ENG_PATH, "-t", f"\"{text}\"", f"-voice {voice}"]
    ).returncode

available_voices = ["ap", "slt", "slt_hts", "kal", "awb", "kal16", "rms",]


if __name__ == "__main__":
    text = (
        "Hello, this is your breath project. Your oxygen level "
        "was 95 % and your hart-rate was 80 bpm."
    )
    for voice in available_voices:
        success = speak_back(text, voice)
        if success == 0:
            print("Succeded")
        else:
            print("Failed")

