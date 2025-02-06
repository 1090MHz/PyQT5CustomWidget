from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class CustomWidget(QWidget):
    def __init__(self, parent=None):
        super(CustomWidget, self).__init__(parent)
        
        self.label = QLabel("This is a custom widget", self)
        
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        
        self.setLayout(layout)