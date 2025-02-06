from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPainter, QTransform
from PyQt5.QtCore import Qt, QSize

class VerticalLabel(QLabel):
    def __init__(self, text, parent=None):
        super(VerticalLabel, self).__init__(text, parent)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(self.palette().color(self.foregroundRole()))
        painter.setFont(self.font())
        
        # Translate to the bottom-left corner of the widget
        painter.translate(self.width(), self.height())
        # Rotate 90 degrees counter-clockwise
        painter.rotate(-90)
        
        # Draw the text
        painter.drawText(0, 0, self.text())
        painter.end()

    def sizeHint(self):
        size = super(VerticalLabel, self).sizeHint()
        return QSize(size.height(), size.width())

class VerticalText(QWidget):
    def __init__(self, parent=None):
        super(VerticalText, self).__init__(parent)
        
        self.label = VerticalLabel("Vertical Text", self)
        
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        
        self.setLayout(layout)