# bpp-speech

# speech to text 

The speech to text is a separated part of the system allowing to catch voice commands.

# Installing hardware.

## Quickstartguide

```bash
sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev
sudo apt-get install bison libasound2-dev swig libpulse-dev
sudo apt-get install flac
. ~/bpp/venv/bin/activate
cd ~/bpp/bpp-speech
pip install -r requirements.txt
```

If the above exit with error follow manual installtiaon of [pocketsphinx](https://howchoo.com/pi/how-to-install-pocketsphinx-on-a-raspberry-pi)

```bash
mkdir site_installs
cd site_installs/
wget https://sourceforge.net/projects/cmusphinx/files/sphinxbase/5prealpha/sphinxbase-5prealpha.tar.gz/download -O sphinxbase.tar.gz
wget https://sourceforge.net/projects/cmusphinx/files/pocketsphinx/5prealpha/pocketsphinx-5prealpha.tar.gz/download -O pocketsphinx.tar.gz
tar -xzvf sphinxbase.tar.gz
tar -xzvf pocketsphinx.tar.gz
sudo apt-get install bison libasound2-dev swig
cd sphinxbase-5prealpha
./configure --enable-fixed
make
sudo make install
cd ../pocketsphinx-5prealpha
./configure
make
sudo make install
src/programs/pocketsphinx_continuous -samprate 48000 -inmic yes
```

## Microphone hardware

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

## Speech Recognition

The speech recognition (SR) is used with python's [SpeecRecognition](https://pypi.org/project/SpeechRecognition/) and the [code](https://github.com/Uberi/speech_recognition/blob/master/speech_recognition/__init__.py) can be find on [GitHub](https://github.com/Uberi/speech_recognition) .
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
update system and install offline sphinx in you python interpreter space:

`sudo apt-get install flac`  
`pip install pocketsphinx`

## Speech recognition engine

The SR relies on offline engine [CMU Sphinx](https://cmusphinx.github.io/wiki/). Although results are of lower quality than online engines. They are only a few, which can be used offline succesfully.

# Usage

The module provide basic fucnction for speech recognition. The function can be called with python interpreter: `python bpp_speech_recognition.py`  
After the function invocation:
- the default microphone input is initialised,
- the microphone ambiet noise is adjusted for one second,
- the voice command asking for input and stdout request is given,
- the microphone input is listen to, until silence is detected. The function exits if no speech detected for 5 seconds or after 15 seconds of listening.
- the speech is reconginsed,
- the recognised speech is matched against a pattern to decide next step.
- if the pattern is dectected, the appropriate function is called, otherwise a user is informed on lack of recognition.
- the software exits.

After installation test by running:

```bash
cd ~/bpp/bpp-speech/src/bpp_speech
python manual_test_speech_recognition.py
```
Say command!

**if:**
Sphinx error; missing PocketSphinx module: ensure that PocketSphinx is set up correctly.

## Adding pattern.

At current version there are only a few patterns and all the call functions are grouped in the main module. To add additional pattern, the list of word and function call needs to be added.
