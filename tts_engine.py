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


from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QTextEdit, QPushButton, 
    QComboBox, QSlider, QLabel, QCheckBox, QHBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon


class TTSApp(QMainWindow):
    def __init__(self, tts_engine, audio_manager):
        super().__init__()
        self.tts_engine = tts_engine
        self.audio_manager = audio_manager

        # Load settings
        self.settings = self.audio_manager.settings
        self.initUI()

    def initUI(self):
        self.setWindowTitle("릴파ㅏㅏㅏㅏㅏㅏㅏㅏㅏ")
        self.setGeometry(100, 100, 600, 500)
        self.setWindowIcon(QIcon("icon.ico"))  # Replace "icon.ico" with your icon file

        layout = QVBoxLayout()

        # Output display area
        self.output_display = QTextEdit(self)
        self.output_display.setReadOnly(True)
        self.output_display.setPlaceholderText("입력한 글자가 여기에 나타날 것입니다.")
        self.output_display.setFont(self.get_current_font())
        layout.addWidget(self.output_display)

        # Input text area
        self.text_input = QLineEdit(self)
        self.text_input.setPlaceholderText("아무거나 쓰고 엔터를 눌러주세요.")
        self.text_input.setFont(self.get_current_font())
        self.text_input.returnPressed.connect(self.on_enter_pressed)
        layout.addWidget(self.text_input)

        # Audio output description
        self.select_device_description = QLabel("TTS 소리를 출력할 장치를 선택해주세요.")
        layout.addWidget(self.select_device_description)

        # Audio output selection
        self.device_selector = QComboBox(self)
        self.device_selector.addItems(self.audio_manager.get_output_devices())
        self.device_selector.setCurrentText(self.settings["output_device"])
        self.device_selector.currentTextChanged.connect(self.on_device_changed)
        layout.addWidget(self.device_selector)

        # Volume slider
        self.volume_label = QLabel(f"볼륨: {self.settings['volume']}", self)
        layout.addWidget(self.volume_label)

        self.volume_slider = QSlider(Qt.Horizontal, self)
        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setValue(self.settings["volume"])
        self.volume_slider.valueChanged.connect(self.on_volume_changed)
        layout.addWidget(self.volume_slider)

        # Font size slider
        font_size_layout = QHBoxLayout()
        font_size_label = QLabel("글자 사이즈:", self)
        self.font_size_slider = QSlider(Qt.Horizontal, self)
        self.font_size_slider.setMinimum(8)
        self.font_size_slider.setMaximum(24)
        self.font_size_slider.setValue(self.settings["font_size"])
        self.font_size_slider.valueChanged.connect(self.on_font_size_changed)

        font_size_layout.addWidget(font_size_label)
        font_size_layout.addWidget(self.font_size_slider)
        layout.addLayout(font_size_layout)

        # Bold font toggle
        self.bold_checkbox = QCheckBox("볼드체 사용 여부", self)
        self.bold_checkbox.setChecked(self.settings["bold"])
        self.bold_checkbox.stateChanged.connect(self.on_bold_changed)
        layout.addWidget(self.bold_checkbox)

        # Set central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def on_enter_pressed(self):
        text = self.text_input.text().strip()
        if text:
            self.output_display.append(text)
            self.tts_engine.speak(text, self.audio_manager.get_device_id_by_name(self.settings["output_device"]))
            self.text_input.clear()

    def on_volume_changed(self, value):
        self.volume_label.setText(f"Volume: {value}")
        self.tts_engine.set_volume(value / 100)
        self.settings["volume"] = value
        self.audio_manager.save_settings()

    def on_device_changed(self, device_name):
        self.audio_manager.set_output_device(device_name)
        self.settings["output_device"] = device_name

    def on_font_size_changed(self, value):
        self.settings["font_size"] = value
        font = self.get_current_font()
        self.text_input.setFont(font)
        self.output_display.setFont(font)
        self.audio_manager.save_settings()

    def on_bold_changed(self, state):
        self.settings["bold"] = state == Qt.Checked
        font = self.get_current_font()
        self.text_input.setFont(font)
        self.output_display.setFont(font)
        self.audio_manager.save_settings()

    def get_current_font(self):
        return QFont("Arial", self.settings["font_size"], QFont.Bold if self.settings["bold"] else QFont.Normal)
