import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QTimer, QTime


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cool Alarm Clock!")
        self.setGeometry(450, 250, 1100, 600)
        base_dir = os.path.dirname(os.path.realpath(__file__))
        icon = QIcon(os.path.join(base_dir, "assets", "clock.ico"))
        self.setWindowIcon(icon)
        self.setStyleSheet("background-color: #1e1e2e;")

        #real time clock
        self.time_label = QLabel(self)
        self.time_label.setFont(QFont("Calibri", 72))
        self.time_label.setGeometry(200, 200, 700, 150)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("color: white; font-weight: bold;")

        self.clock_timer = QTimer(self)
        self.clock_timer.timeout.connect(self.update_time)
        self.clock_timer.start(1000)
        self.update_time()

        button_style = """
            QPushButton {
                background-color: #6c63ff;
                color: white;
                border-radius: 12px;
                font-weight: bold;
                padding: 8px;
            }
            QPushButton:hover { background-color: #7f78ff; }
            QPushButton:pressed { background-color: #574fd6; }
        """

        # stopwatch button
        self.stopwatch_button = QPushButton("⏱️  Stopwatch", self)
        self.stopwatch_button.setFont(QFont("Calibri", 16))
        self.stopwatch_button.setGeometry(150, 400, 250, 55)
        self.stopwatch_button.setStyleSheet(button_style)
        self.stopwatch_button.clicked.connect(self.on_stopwatch)

        #set alarm button
        self.alarm_button = QPushButton("🔔  Set Alarm", self)
        self.alarm_button.setFont(QFont("Calibri", 16))
        self.alarm_button.setGeometry(425, 400, 250, 55)
        self.alarm_button.setStyleSheet(button_style)
        self.alarm_button.clicked.connect(self.on_set_alarm)

        #timer button
        self.timer_button = QPushButton("⏳  Timer", self)
        self.timer_button.setFont(QFont("Calibri", 16))
        self.timer_button.setGeometry(700, 400, 250, 55)
        self.timer_button.setStyleSheet(button_style)
        self.timer_button.clicked.connect(self.on_timer)

    def update_time(self):
        current_time = QTime.currentTime()
        self.time_label.setText(current_time.toString("hh:mm:ss"))

    def on_set_alarm(self):
        print("set alarm clicked")

    def on_stopwatch(self):
        print("stopwatch clicked")

    def on_timer(self):
        print("timer clicked")


def main():
    app = QApplication(sys.argv)
    base_dir = os.path.dirname(os.path.realpath(__file__))
    app.setWindowIcon(QIcon(os.path.join(base_dir, "assets", "clock.ico")))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
