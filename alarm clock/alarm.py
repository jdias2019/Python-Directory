import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton,
                              QSpinBox, QTimeEdit, QMessageBox, QWidget)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QTimer, QTime


BUTTON_STYLE = """
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

SPINBOX_STYLE = """
    QSpinBox {
        background-color: #2e2e3e;
        color: white;
        border: 2px solid #6c63ff;
        border-radius: 8px;
        font-size: 28px;
        padding: 4px;
    }
    QSpinBox::up-button, QSpinBox::down-button { width: 20px; }
"""


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cool Alarm Clock!")
        self.setGeometry(450, 250, 1100, 600)
        base_dir = os.path.dirname(os.path.realpath(__file__))
        icon = QIcon(os.path.join(base_dir, "assets", "clock.ico"))
        self.setWindowIcon(icon)
        self.setStyleSheet("background-color: #1e1e2e;")

        self._build_nav()
        self._build_clock_panel()
        self._build_stopwatch_panel()
        self._build_timer_panel()
        self._build_alarm_panel()

        self.show_panel("clock")

    #nav buttons

    def _build_nav(self):
        self.stopwatch_button = QPushButton("⏱️  Stopwatch", self)
        self.stopwatch_button.setFont(QFont("Calibri", 16))
        self.stopwatch_button.setGeometry(150, 510, 200, 50)
        self.stopwatch_button.setStyleSheet(BUTTON_STYLE)
        self.stopwatch_button.clicked.connect(lambda: self.show_panel("stopwatch"))

        self.alarm_button = QPushButton("🔔  Set Alarm", self)
        self.alarm_button.setFont(QFont("Calibri", 16))
        self.alarm_button.setGeometry(375, 510, 200, 50)
        self.alarm_button.setStyleSheet(BUTTON_STYLE)
        self.alarm_button.clicked.connect(lambda: self.show_panel("alarm"))

        self.timer_button = QPushButton("⏳  Timer", self)
        self.timer_button.setFont(QFont("Calibri", 16))
        self.timer_button.setGeometry(600, 510, 200, 50)
        self.timer_button.setStyleSheet(BUTTON_STYLE)
        self.timer_button.clicked.connect(lambda: self.show_panel("timer"))

        self.clock_button = QPushButton("🕰️  Clock", self)
        self.clock_button.setFont(QFont("Calibri", 16))
        self.clock_button.setGeometry(825, 510, 200, 50)
        self.clock_button.setStyleSheet(BUTTON_STYLE)
        self.clock_button.clicked.connect(lambda: self.show_panel("clock"))

    #clock 

    def _build_clock_panel(self):
        self.clock_panel = QWidget(self)
        self.clock_panel.setGeometry(0, 0, 1100, 500)

        self.time_label = QLabel(self.clock_panel)
        self.time_label.setFont(QFont("Calibri", 90))
        self.time_label.setGeometry(100, 160, 900, 180)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("color: white; font-weight: bold;")

        self.clock_timer = QTimer(self)
        self.clock_timer.timeout.connect(self._update_clock)
        self.clock_timer.timeout.connect(self._check_alarm)
        self.clock_timer.start(1000)
        self._update_clock()

    def _update_clock(self):
        self.time_label.setText(QTime.currentTime().toString("hh:mm:ss"))

    #stopwatch

    def _build_stopwatch_panel(self):
        self.sw_panel = QWidget(self)
        self.sw_panel.setGeometry(0, 0, 1100, 500)

        self.sw_display = QLabel("00:00:00.0", self.sw_panel)
        self.sw_display.setFont(QFont("Calibri", 72))
        self.sw_display.setGeometry(50, 120, 1000, 150)
        self.sw_display.setAlignment(Qt.AlignCenter)
        self.sw_display.setStyleSheet("color: white; font-weight: bold;")

        self.sw_start_btn = QPushButton("▶  Start", self.sw_panel)
        self.sw_start_btn.setFont(QFont("Calibri", 18))
        self.sw_start_btn.setGeometry(320, 330, 200, 55)
        self.sw_start_btn.setStyleSheet(BUTTON_STYLE)
        self.sw_start_btn.clicked.connect(self._sw_toggle)

        self.sw_reset_btn = QPushButton("↺  Reset", self.sw_panel)
        self.sw_reset_btn.setFont(QFont("Calibri", 18))
        self.sw_reset_btn.setGeometry(580, 330, 200, 55)
        self.sw_reset_btn.setStyleSheet(BUTTON_STYLE)
        self.sw_reset_btn.clicked.connect(self._sw_reset)

        self.sw_elapsed = 0
        self.sw_running = False

        self.sw_timer = QTimer(self)
        self.sw_timer.setInterval(100)
        self.sw_timer.timeout.connect(self._sw_tick)

    def _sw_toggle(self):
        if self.sw_running:
            self.sw_timer.stop()
            self.sw_running = False
            self.sw_start_btn.setText("▶  Start")
        else:
            self.sw_timer.start()
            self.sw_running = True
            self.sw_start_btn.setText("⏸  Pause")

    def _sw_reset(self):
        self.sw_timer.stop()
        self.sw_running = False
        self.sw_elapsed = 0
        self.sw_start_btn.setText("▶  Start")
        self.sw_display.setText("00:00:00.0")

    def _sw_tick(self):
        self.sw_elapsed += 1
        tenths = self.sw_elapsed % 10
        total_secs = self.sw_elapsed // 10
        secs = total_secs % 60
        mins = (total_secs // 60) % 60
        hours = total_secs // 3600
        self.sw_display.setText(f"{hours:02}:{mins:02}:{secs:02}.{tenths}")

    # timer (countdown)

    def _build_timer_panel(self):
        self.tmr_panel = QWidget(self)
        self.tmr_panel.setGeometry(0, 0, 1100, 500)

        for text, x in [("H", 270), ("M", 480), ("S", 690)]:
            lbl = QLabel(text, self.tmr_panel)
            lbl.setFont(QFont("Calibri", 20))
            lbl.setGeometry(x, 80, 60, 35)
            lbl.setStyleSheet("color: #aaa;")
            lbl.setAlignment(Qt.AlignCenter)

        self.tmr_h = QSpinBox(self.tmr_panel)
        self.tmr_h.setRange(0, 23)
        self.tmr_h.setFont(QFont("Calibri", 32))
        self.tmr_h.setGeometry(220, 120, 160, 80)
        self.tmr_h.setStyleSheet(SPINBOX_STYLE)
        self.tmr_h.setAlignment(Qt.AlignCenter)

        self.tmr_m = QSpinBox(self.tmr_panel)
        self.tmr_m.setRange(0, 59)
        self.tmr_m.setFont(QFont("Calibri", 32))
        self.tmr_m.setGeometry(430, 120, 160, 80)
        self.tmr_m.setStyleSheet(SPINBOX_STYLE)
        self.tmr_m.setAlignment(Qt.AlignCenter)

        self.tmr_s = QSpinBox(self.tmr_panel)
        self.tmr_s.setRange(0, 59)
        self.tmr_s.setFont(QFont("Calibri", 32))
        self.tmr_s.setGeometry(640, 120, 160, 80)
        self.tmr_s.setStyleSheet(SPINBOX_STYLE)
        self.tmr_s.setAlignment(Qt.AlignCenter)

        self.tmr_display = QLabel("", self.tmr_panel)
        self.tmr_display.setFont(QFont("Calibri", 64))
        self.tmr_display.setGeometry(100, 225, 900, 110)
        self.tmr_display.setAlignment(Qt.AlignCenter)
        self.tmr_display.setStyleSheet("color: white; font-weight: bold;")

        self.tmr_start_btn = QPushButton("▶  Start", self.tmr_panel)
        self.tmr_start_btn.setFont(QFont("Calibri", 18))
        self.tmr_start_btn.setGeometry(320, 370, 200, 55)
        self.tmr_start_btn.setStyleSheet(BUTTON_STYLE)
        self.tmr_start_btn.clicked.connect(self._tmr_toggle)

        self.tmr_reset_btn = QPushButton("↺  Reset", self.tmr_panel)
        self.tmr_reset_btn.setFont(QFont("Calibri", 18))
        self.tmr_reset_btn.setGeometry(580, 370, 200, 55)
        self.tmr_reset_btn.setStyleSheet(BUTTON_STYLE)
        self.tmr_reset_btn.clicked.connect(self._tmr_reset)

        self.tmr_remaining = 0
        self.tmr_running = False

        self.tmr_timer = QTimer(self)
        self.tmr_timer.setInterval(1000)
        self.tmr_timer.timeout.connect(self._tmr_tick)

    def _tmr_toggle(self):
        if self.tmr_running:
            self.tmr_timer.stop()
            self.tmr_running = False
            self.tmr_start_btn.setText("▶  Start")
        else:
            if self.tmr_remaining == 0:
                total = (self.tmr_h.value() * 3600 +
                         self.tmr_m.value() * 60 +
                         self.tmr_s.value())
                if total == 0:
                    return
                self.tmr_remaining = total
            self.tmr_timer.start()
            self.tmr_running = True
            self.tmr_start_btn.setText("⏸  Pause")
            self._tmr_update_display()

    def _tmr_reset(self):
        self.tmr_timer.stop()
        self.tmr_running = False
        self.tmr_remaining = 0
        self.tmr_start_btn.setText("▶  Start")
        self.tmr_display.setText("")

    def _tmr_tick(self):
        self.tmr_remaining -= 1
        self._tmr_update_display()
        if self.tmr_remaining <= 0:
            self.tmr_timer.stop()
            self.tmr_running = False
            self.tmr_start_btn.setText("▶  Start")
            self.tmr_display.setText("00:00:00")
            QMessageBox.information(self, "Timer", "⏰ Time's up!")

    def _tmr_update_display(self):
        h = self.tmr_remaining // 3600
        m = (self.tmr_remaining % 3600) // 60
        s = self.tmr_remaining % 60
        self.tmr_display.setText(f"{h:02}:{m:02}:{s:02}")

    # alarm

    def _build_alarm_panel(self):
        self.alm_panel = QWidget(self)
        self.alm_panel.setGeometry(0, 0, 1100, 500)

        lbl = QLabel("Set Alarm Time:", self.alm_panel)
        lbl.setFont(QFont("Calibri", 22))
        lbl.setGeometry(350, 80, 400, 45)
        lbl.setAlignment(Qt.AlignCenter)
        lbl.setStyleSheet("color: #aaa;")

        self.alm_time_edit = QTimeEdit(self.alm_panel)
        self.alm_time_edit.setFont(QFont("Calibri", 48))
        self.alm_time_edit.setGeometry(300, 140, 500, 110)
        self.alm_time_edit.setDisplayFormat("HH:mm:ss")
        self.alm_time_edit.setAlignment(Qt.AlignCenter)
        self.alm_time_edit.setStyleSheet("""
            QTimeEdit {
                background-color: #2e2e3e;
                color: white;
                border: 2px solid #6c63ff;
                border-radius: 12px;
                padding: 8px;
            }
            QTimeEdit::up-button, QTimeEdit::down-button { width: 30px; }
        """)

        self.alm_set_btn = QPushButton("🔔  Set Alarm", self.alm_panel)
        self.alm_set_btn.setFont(QFont("Calibri", 18))
        self.alm_set_btn.setGeometry(320, 300, 200, 55)
        self.alm_set_btn.setStyleSheet(BUTTON_STYLE)
        self.alm_set_btn.clicked.connect(self._alm_set)

        self.alm_cancel_btn = QPushButton("✖  Cancel", self.alm_panel)
        self.alm_cancel_btn.setFont(QFont("Calibri", 18))
        self.alm_cancel_btn.setGeometry(580, 300, 200, 55)
        self.alm_cancel_btn.setStyleSheet(BUTTON_STYLE)
        self.alm_cancel_btn.clicked.connect(self._alm_cancel)

        self.alm_status = QLabel("No alarm set", self.alm_panel)
        self.alm_status.setFont(QFont("Calibri", 16))
        self.alm_status.setGeometry(200, 385, 700, 40)
        self.alm_status.setAlignment(Qt.AlignCenter)
        self.alm_status.setStyleSheet("color: #888;")

        self.alarm_time = None
        self.alarm_fired = False

    def _alm_set(self):
        self.alarm_time = self.alm_time_edit.time()
        self.alarm_fired = False
        self.alm_status.setText(f"⏰  Alarm set for {self.alarm_time.toString('HH:mm:ss')}")
        self.alm_status.setStyleSheet("color: #6c63ff; font-weight: bold;")

    def _alm_cancel(self):
        self.alarm_time = None
        self.alarm_fired = False
        self.alm_status.setText("No alarm set")
        self.alm_status.setStyleSheet("color: #888;")

    def _check_alarm(self):
        if self.alarm_time is None or self.alarm_fired:
            return
        now = QTime.currentTime()
        if (now.hour() == self.alarm_time.hour() and
                now.minute() == self.alarm_time.minute() and
                now.second() == self.alarm_time.second()):
            self.alarm_fired = True
            QMessageBox.information(self, "Alarm", "🔔 Wake up!")
            self._alm_cancel()

    # panel switcher 

    def show_panel(self, name):
        for panel in [self.clock_panel, self.sw_panel, self.tmr_panel, self.alm_panel]:
            panel.hide()
        {"clock": self.clock_panel,
         "stopwatch": self.sw_panel,
         "timer": self.tmr_panel,
         "alarm": self.alm_panel}[name].show()


def main():
    app = QApplication(sys.argv)
    base_dir = os.path.dirname(os.path.realpath(__file__))
    app.setWindowIcon(QIcon(os.path.join(base_dir, "assets", "clock.ico")))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()