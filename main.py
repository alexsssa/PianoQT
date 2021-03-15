import sys
import os

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5 import QtMultimedia
from PyQt5.QtWidgets import QApplication, QMainWindow

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


class Piano(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle('Фортепиано [by drammma] - 2021')

        self.BLACK_KEYS = [self.key_Db, self.key_Eb, self.key_Gb, self.key_Ab, self.key_Bb, self.key_Db2, self.key_Eb2,
                           self.key_Gb2, self.key_Ab2, self.key_Bb2]

        self.WHITE_KEYS = [self.key_C7, self.key_D7, self.key_E7, self.key_F7, self.key_G7, self.key_A7, self.key_B7,
                           self.key_C6, self.key_D6, self.key_E6, self.key_F6, self.key_G6, self.key_A6, self.key_B6,
                           self.key_C5]

        for key in self.BLACK_KEYS:
            key.clicked.connect(self.play)

        for key in self.WHITE_KEYS:
            key.clicked.connect(self.play)

    def keyPressEvent(self, event):
        keys = {Qt.Key_Q: self.key_C7, Qt.Key_W: self.key_D7, Qt.Key_E: self.key_E7, Qt.Key_R: self.key_F7,
                Qt.Key_T: self.key_G7, Qt.Key_Y: self.key_A7, Qt.Key_U: self.key_B7, Qt.Key_I: self.key_C6,
                Qt.Key_O: self.key_D6, Qt.Key_P: self.key_E6, Qt.Key_A: self.key_F6, Qt.Key_S: self.key_G6,
                Qt.Key_D: self.key_A6, Qt.Key_F: self.key_B6, Qt.Key_G: self.key_C6, Qt.Key_1: self.key_Db,
                Qt.Key_2: self.key_Eb, Qt.Key_3: self.key_Gb, Qt.Key_4: self.key_Ab, Qt.Key_5: self.key_Bb,
                Qt.Key_6: self.key_Db2, Qt.Key_7: self.key_Eb2, Qt.Key_8: self.key_Gb2, Qt.Key_9: self.key_Ab2,
                Qt.Key_0: self.key_Bb2}
        if event.key() in keys:
            self.play(keys[event.key()])

    def play(self, keyboard):
        if keyboard:
            key = keyboard
        else:
            key = self.sender()
        filename = os.path.join(CURRENT_DIR, f"music/{key.objectName().lstrip('key_')}.wav")
        QtMultimedia.QSound.play(filename)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    class_ = Piano()
    class_.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
