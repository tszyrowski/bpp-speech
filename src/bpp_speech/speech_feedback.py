import glob
import os.path
import re
import subprocess  # nosec


SPEECH_ENG_PATH = "/home/pi/bpp/mimic1/mimic"
DATA_PATH = "/home/pi/bpp/data"

def read_last_reading():
    files = glob.glob(DATA_PATH + "/*txt")
    latest_file = max(files, key=os.path.getctime)
    with open(latest_file, "r") as f:
        last_line = f.readlines()[-1].split(",")
        HR = int(re.sub('\D', '', last_line[-2]))
        SPX = int(re.sub('\D', '', last_line[-1]))
        print(HR, SPX, last_line)
    return HR, SPX


def speak_back(text=None, voice="ap"):
    """Use espeak to convert text to speech."""
    HR, SPX = read_last_reading()
    if text is None:
        text = ("Hello, this is your breath project. Your oxygen level " +
        f"was {SPX} % and your hart-rate was {HR} bpm.")
    return subprocess.run(  # nosec
        [SPEECH_ENG_PATH, "-t", f"{text}", "-voice", f"{voice}"]
    ).returncode


if __name__ == "__main__":
    available_voices = ["ap", "slt", "kal", "awb", "kal16", "rms"]
    for voice in available_voices:
        success = speak_back(voice=voice)
        if success == 0:
            print("Succeded")
        else:
            print("Failed")
