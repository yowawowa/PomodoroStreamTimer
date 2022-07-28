import sys
import wave
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QIcon
from design import Ui_MainWindow
import time
import os
import ctypes
import pyaudio
from win10toast import ToastNotifier
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

# should only require hiddenimports
# datas = collect_data_files('pyaudio')
hiddenimports = collect_submodules('pyaudio')

global sound_path
sound_path = 'end.wav'


class Pomodoro(QMainWindow):
    def __init__(self):
        super(Pomodoro, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.start_button.clicked.connect(self.start_button_clicked)
        self.ui.stop_button.clicked.connect(self.stop_button_clicked)
        self.ui.stop_button.setDisabled(True)
        self.ui.endsound_button.clicked.connect(self.endsound_button_clicked)
        self.setWindowIcon(QIcon('icon.png'))

        myappid = 'Yowa.PomodoroTimer.PomStreamTimer.1.0'  # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        self.ui.ding_button.clicked.connect(self.ding_button_clicked)

    def start_button_clicked(self):
        self.worker = WorkerThread(self.ui.cycles.value(), self.ui.work_time.value(), self.ui.break_time.value(),
                                   sound_path, self.ui.sound_check.isChecked())
        self.worker.start()
        self.worker.update_progress.connect(self.evt_update_progress)
        self.worker.make_sound.connect(self.evt_make_sound)
        self.worker.finished.connect(self.evt_worker_finished)
        self.ui.endsound_button.setDisabled(True)
        self.ui.start_button.setDisabled(True)
        self.ui.stop_button.setEnabled(True)

    def evt_worker_finished(self):
        self.ui.status_label.setText('Ended')
        file = open('time.txt', 'w')
        file.write('')
        file.close()
        self.evt_make_sound()

    def evt_make_sound(self):
        self.sounder = AudioThread(sound_path)
        if self.ui.sound_check.isChecked():
            self.sounder.start()

    def stop_button_clicked(self):
        self.worker.terminate()
        self.ui.status_label.setText('Stopped')
        self.ui.endsound_button.setEnabled(True)
        self.ui.start_button.setEnabled(True)
        self.ui.sound_check.setEnabled(True)

    def evt_update_progress(self, t, cyc, status):
        mins = t // 60
        secs = t % 60
        self.ui.status_label.setText(str(status) + " cycle \n" + str(cyc) + '/' + str(self.ui.cycles.value()))
        self.ui.lcdNumber.display('{:02d}:{:02d}'.format(mins, secs))
        file = open('time.txt', 'w')
        file.write(status + ' ' + str(cyc) + '/' + str(self.ui.cycles.value()) + '\n' + str(
            '{:02d}:{:02d}'.format(mins, secs)))

    def endsound_button_clicked(self):
        file_filter = 'Sound file (*.wav *.mp3)'
        global sound_path
        sound = QFileDialog.getOpenFileName(parent=self, caption='Select sound file', filter=file_filter)
        sound_path = str(os.path.abspath(sound[0]))

    def ding_button_clicked(self):
        self.sounder = AudioThread(sound_path)
        if self.ui.sound_check.isChecked():
            self.sounder.start()


class WorkerThread(QThread):
    update_progress = Signal(int, int, str)
    make_sound = Signal()

    def __init__(self, cycles, work_time, break_time, sound_file_path, sound_check):
        self.cycles = cycles
        self.work_time = work_time
        self.break_time = break_time
        self.endsound = sound_file_path
        self.sound_check = sound_check
        self.a = AudioFile(sound_path)
        super().__init__()

    def run(self):
        print("Pomodoro starts now!")
        cycles_counter = 0
        for i in range(self.cycles):
            cycles_counter += 1
            t = int(self.work_time) * 60  # get work time from user
            while t:
                self.update_progress.emit(t, cycles_counter, 'Study')
                mins = t // 60
                secs = t % 60
                timer = '{:02d}:{:02d}'.format(mins, secs)  # formatting text
                print(timer)  # overwrite previous line
                time.sleep(1)
                t -= 1
            else:
                timer = '{:02d}:{:02d}'.format(0, 0)
                print(timer)
                self.update_progress.emit(0, cycles_counter, 'Study')
                time.sleep(1)
            if cycles_counter != self.cycles:
                print("Break Time!!")
                self.update_progress.emit(t, cycles_counter, 'Study')
                if self.sound_check:
                    self.make_sound.emit()
                t = self.break_time * 60  # get break time from user

            else:
                break
            while t:
                self.update_progress.emit(t, cycles_counter, 'Break')
                mins = t // 60
                secs = t % 60
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(timer)  # overwrite previous line
                time.sleep(1)
                t -= 1
            else:
                self.update_progress.emit(0, cycles_counter, 'Break')
                timer = '{:02d}:{:02d}'.format(0, 0)
                print(timer)
                time.sleep(1)
                print("Work Time!!")
                self.update_progress.emit(t, cycles_counter, 'Break')
                if self.sound_check:
                    self.make_sound.emit()


class AudioFile:
    chunk = 1024

    def __init__(self, file):
        """ Init audio stream """
        self.wf = wave.open(file, 'rb')
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=self.p.get_format_from_width(self.wf.getsampwidth()),
            channels=self.wf.getnchannels(),
            rate=self.wf.getframerate(),
            output=True
        )

    def play(self):
        """ Play entire file """
        data = self.wf.readframes(self.chunk)
        while data != b'':
            self.stream.write(data)
            data = self.wf.readframes(self.chunk)

    def close(self):
        """ Graceful shutdown """
        self.stream.close()
        self.p.terminate()


class AudioThread(QThread):
    def __init__(self, sound_path):
        self.a = AudioFile(sound_path)
        super().__init__()

    def run(self):
        self.a.play()
        self.a.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Pomodoro()
    window.show()

    sys.exit(app.exec())
