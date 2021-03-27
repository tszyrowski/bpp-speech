import speech_recognition as sr


last_cmd = ["last", "lost", "lust", "loose", "us"]
average_cmd = ["average", "coverage"]

def call_ask_for_cmd():
    """Call welcome and speech command request."""
    print("Say command!")

def call_last_reading():
    """Call function reading last reading."""
    print("RETURNING LAST READINGS")

def call_average_reading():
    """Call function returning average."""
    print("RETURNING AVERAGE READINGS")

def call_cannot_understand(speech_cmd):
    """Call function informing sentence does not much possiblities."""
    print(f"can not understand, did you say: {speech_cmd}")

def call_unrecognised_cmd():
    """Call speech did not much any recognaisable input."""
    print("Sphinx could not understand audio")

def call_general_error(e):
    """Call general output occured."""
    print("Sphinx error; {0}".format(e))

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
        audio = r.listen(source, timeout=5, phrase_time_limit=15)

    # recognize speech using Sphinx
    try:
        speech_cmd = r.recognize_sphinx(audio)
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

if __name__ == "__main__":
    bpp_recognise()