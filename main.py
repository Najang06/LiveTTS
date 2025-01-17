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
