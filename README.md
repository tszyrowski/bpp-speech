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
