from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPainter, QTransform
from PyQt5.QtCore import Qt, QSize


class VerticalLabel(QLabel):

    def __init__(self, *args):
        QLabel.__init__(self, *args)

    def paintEvent(self, event):
        QLabel.paintEvent(self, event)
        painter = QPainter(self)
        painter.translate(0, self.height() - 1)
        painter.rotate(-90)
        self.setGeometry(self.x(), self.y(), self.height(), self.width())
        QLabel.render(self, painter)

    def minimumSizeHint(self):
        size = QLabel.minimumSizeHint(self)
        return QSize(size.height(), size.width())

    def sizeHint(self):
        size = QLabel.sizeHint(self)
        return QSize(size.height(), size.width())


class VerticalText(QWidget):
    def __init__(self, parent=None):
        super(VerticalText, self).__init__(parent)

        self.label = VerticalLabel("Vertical Text", self)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)

        self.setLayout(layout)
