import pyaudio
print("pyaudio imported")
p = pyaudio.PyAudio()
print("initialised")
for i in range(p.get_device_count()):
    print(f"** DEVICE: {p.get_device_info_by_index(i).get('name')}")
