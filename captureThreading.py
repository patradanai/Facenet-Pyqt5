from PyQt5.QtCore import *
import cv2
import numpy as np


class RecordVideo(QObject):
    # Signal * Slot
    imageData = pyqtSignal(np.ndarray)

    def __init__(self, parent=None):
        super(RecordVideo, self).__init__(parent)
        self.capture = cv2.VideoCapture(0)

    def startRecord(self):
        while True:
            ret, frame = self.capture.read()
            frame = cv2.resize(frame, (478, 350), fx=0.5, fy=0.5)
            if ret:
                self.imageData.emit(frame)
