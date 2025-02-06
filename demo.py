import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from custom_vtext import VerticalText

class DemoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Widget Demo")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        vertical_text_widget = VerticalText()
        layout.addWidget(vertical_text_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = DemoWindow()
    demo.show()
    sys.exit(app.exec_())