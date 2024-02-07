import time

from pynput import keyboard, mouse
from PyQt5.QtCore import QObject, pyqtSignal, QThread

class InputEvent:
    TABLE_TITLE = ("TimeStamp", "Event", "Position", "Button", "Key")

    def __init__(self, event, position: tuple = None, button: mouse.Button = None, key: keyboard.Key = None):
        self.event = event
        self.position = position
        self.button = button
        self.key = key

        self.timeStamp = time.time()

    def __repr__(self):
        return f"InputEvent({self.event}, {self.position}, {self.button}, {self.key})"

    def toDict(self):
        return {
            "TimeStamp": self.timeStamp, 
            "Event": self.event, 
            "Position": self.position, 
            "Button": self.button, 
            "Key": self.key
        }

    def perform(self, controller):
        actions = {
            "mouseMove": self.mouseMove,
            "mousePress": self.mousePress,
            "mouseRelease": self.mouseRelease,
            "keyPress": self.keyPress,
            "keyRelease": self.keyRelease,
        }
        action = actions.get(self.event)
        if action:
            action(controller)
    
    def mouseMove(self, controller):
        controller.position = self.position

    def mousePress(self, controller):
        controller.position = self.position
        controller.press(self.button)

    def mouseRelease(self, controller):
        controller.release(self.button)

    def keyPress(self, controller):
        controller.press(self.key)

    def keyRelease(self, controller):
        controller.release(self.key)

class WorkerSignals(QObject):
    finished = pyqtSignal(list)
    progress = pyqtSignal(list)

class InputListener(QThread):
    STOP_KEY = keyboard.Key.f8

    def __init__(self, parent=None):
        super(InputListener, self).__init__(parent)
        self.progress_signal = WorkerSignals()
        self.stop_listening = False
        self.last_action_time = None
        self.is_mouse_down = {
            mouse.Button.left: False,
            mouse.Button.middle: False, 
            mouse.Button.right: False
        }

        self.input_events = []

    def run(self):
        mouse_listener = mouse.Listener(on_click=self.on_click, on_move=self.on_move)
        mouse_listener.start()

        keyboard_listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        keyboard_listener.start()
       
        keyboard_listener.join()
        mouse_listener.stop()

        self.progress_signal.finished.emit(self.input_events)
    

    def on_move(self, x, y):
        if True in self.is_mouse_down.values():
            input_event = InputEvent("mouseMove", position=(x, y))
            self.input_events.append(input_event)

            self.progress_signal.progress.emit(self.input_events)


    def on_click(self, x, y, button, pressed):
        self.is_mouse_down[button] = pressed
        input_event = InputEvent("mousePress" if pressed else "mouseRelease", position=(x, y), button=button)
        self.input_events.append(input_event)

        self.progress_signal.progress.emit(self.input_events)

    def on_press(self, key):
        if key == self.STOP_KEY:
            self.stop_listening = True
            return False
        else:
            input_event = InputEvent("keyPress", key=key)
            self.input_events.append(input_event)

            self.progress_signal.progress.emit(self.input_events)

    def on_release(self, key):
        input_event = InputEvent("keyRelease", key=key)
        self.input_events.append(input_event)

        self.progress_signal.progress.emit(self.input_events)