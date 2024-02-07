import math
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidget
from PyQt5.QtGui import QPixmap, QImage, QIcon
from PyQt5.QtCore import QProcess, QThread

from ..lib.QtObjectsConfigurator import TableWidgetConfig
from ..lib.InputListener import InputListener, InputEvent
from ..lib.EventsPlayer import EventsPlayer

Ui_MainWindow, QtBaseClass = uic.loadUiType("./src/app/ui/mainWindow.ui")

MAX_LOG = 200

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setupUi(self)
        self.connectFunction()
        self.initUI()

        self.input_events = []

    def connectFunction(self):
        self.startRec_btn.clicked.connect(self.startRec)
        self.replayRec_btn.clicked.connect(self.replayRecBtn)

        self.repeat_spec_times.toggled.connect(self.repeatSettingToggled)
        self.repeat_until_stop.toggled.connect(self.repeatSettingToggled)

    def initUI(self):
        TableWidgetConfig.setSize(self.rec_events_table, len(InputEvent.TABLE_TITLE), 1)
        TableWidgetConfig.setDimensions(self.rec_events_table, self.rec_events_table.width() / self.rec_events_table.columnCount(), 8)
        self.rec_events_table.setHorizontalHeaderLabels(InputEvent.TABLE_TITLE)

    def recResult(self, result):
        self.statusbar.showMessage("Finished recording", 2000)
        self.startRec_btn.setEnabled(True)
        self.replayRec_btn.setEnabled(True)
        self.input_events = result

    def updateRecEvents(self, events: list):
        TableWidgetConfig.setDataDicts(self.rec_events_table, [event.toDict() for event in events], adjust_size=True, use_keys=True)
        self.rec_events_table.scrollToBottom()

    def startRec(self):
        self.statusbar.showMessage("Recording...")
        self.rec_events_table.clearContents()
        TableWidgetConfig.setSize(self.rec_events_table, len(InputEvent.TABLE_TITLE), 1)

        self.startRec_btn.setEnabled(False)
        self.replayRec_btn.setEnabled(False)

        listener = InputListener(parent=self)
        listener.progress_signal.finished.connect(self.recResult)
        listener.progress_signal.progress.connect(self.updateRecEvents)
        listener.start()

    def replayResult(self, is_stop):
        self.repeat_times -= 1
        if self.repeat_times > 0 and not is_stop:
            self.replayRec()
            return

        self.statusbar.showMessage("Finished replaying", 2000)
        self.startRec_btn.setEnabled(True)
        self.replayRec_btn.setEnabled(True)

    def replayRecBtn(self):
        self.repeat_times = math.inf if self.repeat_until_stop.isChecked() else self.repeat_times_spinBox.value()
        self.replayRec()

    def replayRec(self):
        self.statusbar.showMessage("Replaying...")
        self.startRec_btn.setEnabled(False)
        self.replayRec_btn.setEnabled(False)

        eventPlayer = EventsPlayer(self.input_events, instant=self.instant_run.isChecked(), parent=self)
        eventPlayer.progress_signal.finished.connect(self.replayResult)
        eventPlayer.start()

    def repeatSettingToggled(self):
        (self.repeat_until_stop if self.repeat_spec_times.isChecked() else self.repeat_spec_times).setChecked(False)
    