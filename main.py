'''MIT License

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


import sys
from PyQt5.QtWidgets import QApplication
from gui import TTSApp
from tts_engine import TTSEngine
from audio_settings import AudioManager

def main():
    app = QApplication(sys.argv)
    tts_engine = TTSEngine()
    audio_manager = AudioManager()
    main_window = TTSApp(tts_engine, audio_manager)
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
