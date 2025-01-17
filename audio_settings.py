'''
MIT License

Copyright (c) 2025 Yeongju Yu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

This project includes the following third-party libraries:

- **PyQt5**: GPL v3
- **pyttsx3**: MIT License
- **pyaudio**: BSD License
- **sounddevice**: MIT License
- **soundfile**: BSD License

Each of these libraries is subject to its respective license terms. Please refer to each library's documentation for detailed license information.
'''


import json
import pyaudio
import os


class AudioManager:
    def __init__(self, settings_file="settings.json"):
        self.audio = pyaudio.PyAudio()
        self.settings_file = settings_file
        self.settings = self.load_settings()
        self.default_device = self.get_default_device()

    def get_output_devices(self):
        devices = []
        for i in range(self.audio.get_device_count()):
            device_info = self.audio.get_device_info_by_index(i)
            if device_info["maxOutputChannels"] > 0:  # 출력 가능한 장치만
                devices.append(device_info["name"])
        return devices

    def get_default_device(self):
        default_index = self.audio.get_default_output_device_info()["index"]
        return self.audio.get_device_info_by_index(default_index)["name"]

    def get_device_id_by_name(self, device_name):
        for i in range(self.audio.get_device_count()):
            device_info = self.audio.get_device_info_by_index(i)
            if device_info["name"] == device_name:
                return device_info["index"]
        return None

    def set_output_device(self, device_name):
        self.settings["output_device"] = device_name
        self.save_settings()
        print(f"Output device set to: {device_name}")

    def save_settings(self):
        with open(self.settings_file, "w") as f:
            json.dump(self.settings, f, indent=4)

    def load_settings(self):
        if os.path.exists(self.settings_file):
            with open(self.settings_file, "r") as f:
                return json.load(f)
        # Default settings
        return {
            "output_device": self.get_default_device(),
            "volume": 50,
            "font_size": 12,
            "bold": False,
        }
