import pyaudio


print("pyaudio imported")
p = pyaudio.PyAudio()
print("initialised")

print("default_host_api_info")
for k, v in p.get_default_host_api_info().items():
    print(f"\t {k}: {v}")

print("default_input_device_info")
for k, v in p.get_default_input_device_info().items():
    print(f"\t {k}: {v}")

print("default_output_device_info")
for k, v in p.get_default_output_device_info().items():
    print(f"\t {k}: {v}")
print ("\n")

print(
    f"\nThis machine has {p.get_device_count()} devices "
    f"and {p.get_host_api_count()} available PortAudio Host APIs"
    "\n"
)

for i in range(p.get_device_count()):
    print(
        f"** DEVICE {i} on {p.get_device_info_by_index(i).get('hostApi')}: "
        f"{p.get_device_info_by_index(i).get('name')}; With max channels: "
        f"input= {p.get_device_info_by_index(i).get('maxInputChannels')},"
        f"output= {p.get_device_info_by_index(i).get('maxOutputChannels')}"
    )

mic_device = None

for j in range(p.get_host_api_count()):
    info = p.get_host_api_info_by_index(j)
    numdevices = info.get('deviceCount')
    print(f"--Host Api {j} name: {info.get('name')}, with {numdevices} devices")
    for i in range(0, numdevices):
        curr_device = p.get_device_info_by_host_api_device_index(j, i)
        if (curr_device.get('maxInputChannels')) > 0:
            idx = curr_device.get('index')
            name = curr_device.get('name')
            print(
                f"Input Device id {i} - index: {idx}; name: {name}"
            )
            if "USB PnP" in name:
                mic_device = curr_device

print(
    "Microphone to use: "
    f"{curr_device.get('index')}: {curr_device.get('name')}"
)
for k, v in curr_device.items():
    print(f"\t{k}: {v}")

print(
    "Default input device: "
    f"{p.get_default_input_device_info()}"
)
