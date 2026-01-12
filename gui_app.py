import sys
import subprocess
import webbrowser
import time
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QLabel
)

STREAMLIT_PORT = 8501

class Launcher(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard Launcher")
        self.setFixedSize(400, 220)

        self.label = QLabel("Dashboard stopped")

        self.start_button = QPushButton("Start Dashboard")
        self.stop_button = QPushButton("Stop Dashboard")

        self.start_button.clicked.connect(self.start_streamlit)
        self.stop_button.clicked.connect(self.stop_streamlit)

        self.stop_button.setEnabled(False)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        self.setLayout(layout)

        self.process = None

    def start_streamlit(self):
        if self.process is None:
            self.label.setText("Starting dashboard...")
            self.process = subprocess.Popen(
                [
                    "streamlit", "run", "app.py",
                    "--server.port", str(STREAMLIT_PORT),
                    "--server.address", "127.0.0.1"
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

            time.sleep(2)
            webbrowser.open(f"http://localhost:{STREAMLIT_PORT}")

            self.label.setText("Dashboard running 🚀")
            self.start_button.setEnabled(False)
            self.stop_button.setEnabled(True)

    def stop_streamlit(self):
        if self.process is not None:
            self.label.setText("Stopping dashboard...")

            self.process.terminate()
            self.process.wait(timeout=5)

            self.process = None
            self.label.setText("Dashboard stopped")

            self.start_button.setEnabled(True)
            self.stop_button.setEnabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Launcher()
    window.show()
    sys.exit(app.exec())
