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
