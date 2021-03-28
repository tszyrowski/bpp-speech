from ctypes import *  # noqa: F403
from contextlib import contextmanager
import datetime

import pyaudio
import wave

# Recatching warnings from pyaudio ALSA
ERR_HANDLER_ALSA = CFUNCTYPE(  # noqa:F405
    None, c_char_p, c_int, c_char_p, c_int, c_char_p  # noqa:F405
)


def py_error_handler(filename, line, function, err, fmt):
    """Skip ALSA error."""
    pass


c_error_handler = ERR_HANDLER_ALSA(py_error_handler)


@contextmanager
def noalsaerr():
    """Wrap ALSA error."""
    asound = cdll.LoadLibrary('libasound.so')  # noqa: F841,F405
    asound.snd_lib_error_set_handler(c_error_handler)
    yield
    asound.snd_lib_error_set_handler(None)


def record_mic():
    """Record mic output to wac file."""
    # Create mic pamas
    form_1 = pyaudio.paInt16  # 16-bit resolution
    chans = 1  # 1 channel
    samp_rate = 44100  # 44.1kHz sampling rate
    chunk = 1024 * 2  # 2^12 samples for buffer
    record_secs = 3  # seconds to record
    dev_index = 0  # device index found by p.get_device_info_by_index(ii)

    with noalsaerr():
        try:
            audio = pyaudio.PyAudio()  # create pyaudio instantiation
        except Exception as e:
            print("*** ", e)

    # create pyaudio stream
    stream = audio.open(
        format=form_1,
        rate=samp_rate,
        channels=chans,
        input_device_index=dev_index,
        input=True,
        frames_per_buffer=chunk
    )

    print("recording")
    frames = []

    # loop through stream and append audio chunks to frame array
    for ii in range(0, int((samp_rate / chunk) * record_secs)):
        data = stream.read(chunk, exception_on_overflow=False)
        frames.append(data)

    print("finished recording")

    # stop the stream, close it, and terminate the pyaudio instantiation
    stream.stop_stream()
    stream.close()
    audio.terminate()

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H_%M_%S")
    filename = f"./mic_output_{timestamp}.wav"
    # save the audio frames as .wav file
    with wave.open(filename, "wb") as wavefile:
        wavefile.setnchannels(chans)
        wavefile.setsampwidth(audio.get_sample_size(form_1))
        wavefile.setframerate(samp_rate)
        wavefile.writeframes(b''.join(frames))

    print(f"Recording saved as {filename}")


if __name__ == "__main__":
    record_mic()
