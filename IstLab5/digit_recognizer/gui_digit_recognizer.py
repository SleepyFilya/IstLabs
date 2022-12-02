from keras.models import load_model
import numpy as np

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

model = load_model('mnist.h5')


def predict_digit(img):
    imm = img.scaled(28, 28, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
    incomingImage = imm.convertToFormat(QImage.Format_Grayscale8)

    width = incomingImage.width()
    height = incomingImage.height()

    ptr = incomingImage.bits()
    ptr.setsize(incomingImage.byteCount())
    img = np.array(ptr).reshape(height, width, 1)  # Copies the data

    # изменение размерности для поддержки модели ввода и нормализации
    img = img.reshape(1,28,28,1)
    img = img/255.0
    # предстказание цифры
    res = model.predict([img])[0]
    return np.argmax(res), max(res)

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.top = 400
        self.left = 400
        self.width = 300
        self.height = 300

        self.setWindowTitle("ISIT Lab 5")
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.label = QLabel("", self)
        self.label.setGeometry(125, 100, 100, 100)

        self.drawing = False
        self.brushSize = 10
        self.brushColor = Qt.black

        self.lastPoint = QPoint()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("Options")

        recognizeAction = QAction("Recognize", self)
        recognizeAction.setShortcut("Ctrl+R")
        fileMenu.addAction(recognizeAction)
        recognizeAction.triggered.connect(self.recognize)

        clearAction = QAction("Clear", self)
        clearAction.setShortcut("Ctrl+X")
        fileMenu.addAction(clearAction)
        clearAction.triggered.connect(self.clear)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def recognize(self):
        digit, acc = predict_digit(self.image)
        self.clear()
        self.label.setText(str(digit) + ', ' + str(int(acc * 100)) + '%')

    def clear(self):
        self.image.fill(Qt.white)
        self.update()


def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
