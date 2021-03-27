# bpp-speech-to-text

# speech to text 

The speech to text is a separated part of the system allowing to catch voice commands.

# Installing hardware.

To verify the USB microphone is connected run: 
`lsusb -t` 
the command should display output including lines as:

```bash
/:  Bus 01.Port 1: Dev 1, Class=root_hub, Driver=dwc_otg/1p, 480M
    |__ Port 1: Dev 2, If 0, Class=Hub, Driver=hub/5p, 480M
        |__ Port 1: Dev 3, If 0, Class=Vendor Specific Class, Driver=smsc95xx, 480M
        |__ Port 3: Dev 4, If 0, Class=Human Interface Device, Driver=usbhid, 1.5M
        |__ Port 3: Dev 4, If 1, Class=Human Interface Device, Driver=usbhid, 1.5M
        |__ Port 5: Dev 6, If 0, Class=Audio, Driver=snd-usb-audio, 12M
        |__ Port 5: Dev 6, If 1, Class=Audio, Driver=snd-usb-audio, 12M
        |__ Port 5: Dev 6, If 2, Class=Audio, Driver=snd-usb-audio, 12M
        |__ Port 5: Dev 6, If 3, Class=Human Interface Device, Driver=usbhid, 12M
```
with `Driver=snd-usb-audio`

To install python package follow: [blog](https://makersportal.com/blog/2018/8/23/recording-audio-on-the-raspberry-pi-with-python-and-a-usb-microphone)

The initialisation of `pyaudio.PyAudio()` can give large tracback saying it does not recognise devices or find files for a particular

The warnings are caused by config file. [Further instructions](https://stackoverflow.com/questions/7088672/pyaudio-working-but-spits-out-error-messages-each-time/17673011#17673011)

# Speech Recognition

The speech recognition (SR) is used with python's [SpeecRecognition](https://pypi.org/project/SpeechRecognition/) and can be fins on [GitHub](https://github.com/Uberi/speech_recognition).
The SR can be analysed with offline tools  
The module can give error on the first line:

```bash
Sphinx error; missing PocketSphinx module: ensure that PocketSphinx is set up correctly.
Traceback (most recent call last):
  File "mic_recognition.py", line 25, in <module>
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
  File "/home/pi/bpp/venv/vBpp/lib/python3.7/site-packages/speech_recognition/__init__.py", line 828, in recognize_google
    convert_width=2  # audio samples must be 16-bit
  File "/home/pi/bpp/venv/vBpp/lib/python3.7/site-packages/speech_recognition/__init__.py", line 445, in get_flac_data
    flac_converter = get_flac_converter()
  File "/home/pi/bpp/venv/vBpp/lib/python3.7/site-packages/speech_recognition/__init__.py", line 1196, in get_flac_converter
    raise OSError("FLAC conversion utility not available - consider installing the FLAC command line application by running `apt-get install flac` or your operating system's equivalent")
OSError: FLAC conversion utility not available - consider installing the FLAC command line application by running `apt-get install flac` or your operating system's equivalent
```
probably not needed: `sudo apt-get install -qq swig libpulse-dev`

`sudo apt-get install flac`
`pip install pocketsphinx`

# Speech recognition engine

The SR relies on offline engine [CMU Sphinx](https://cmusphinx.github.io/wiki/). Although results are of lower quality than online engines. They are only a few, which can be used offline succesfully.
