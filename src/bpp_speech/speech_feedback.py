import subprocess  # nosec


SPEECH_ENG_PATH = "/home/pi/bpp/mimic1/mimic"


def speak_back(text, voice):
    """Use espeak to convert text to speech."""
    return subprocess.run(  # nosec
        [SPEECH_ENG_PATH, "-t", f"\"{text}\"", f"-voice {voice}"]
    ).returncode


if __name__ == "__main__":
    available_voices = ["ap", "slt", "slt_hts", "kal", "awb", "kal16", "rms"]
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
