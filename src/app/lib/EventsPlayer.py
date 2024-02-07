import time
from pynput import keyboard, mouse
from PyQt5.QtCore import QObject, pyqtSignal, QThread

class WorkerSignals(QObject):
    finished = pyqtSignal(bool)

class EventsPlayer(QThread):
    STOP_KEY = keyboard.Key.f8

    def __init__(self, input_events, instant=True, parent=None):
        super(EventsPlayer, self).__init__(parent)
        self.progress_signal = WorkerSignals()

        self.input_events = input_events
        self.instant = instant
        self.mouse_ctr = mouse.Controller()
        self.keyboard_ctr = keyboard.Controller()

        self.stop_replaying = False
        self.last_action_time = None

    def run(self):
        keyboard_listener = keyboard.Listener(on_press=self.on_press)
        keyboard_listener.start()

        for event in self.input_events:
            if self.stop_replaying:
                keyboard_listener.stop()
                break

            if self.last_action_time and not self.instant:
                time.sleep(event.timeStamp - self.last_action_time)
                
            event.perform(self.mouse_ctr) if event.event.startswith("mouse") else event.perform(self.keyboard_ctr)
            self.last_action_time = event.timeStamp

        self.progress_signal.finished.emit(self.stop_replaying)

    def on_press(self, key):
        if key == self.STOP_KEY:
            self.stop_replaying = True
            return False
