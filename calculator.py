import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget, QLabel

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RED'S CALCULATOR")
        self.setGeometry(800, 300, 400, 200) 
        self.line_1 = QLineEdit(self)
        self.line_2 = QLineEdit(self) 
        self.result_label = QLabel(self)
        self.button_1 = QPushButton("sum", self)
        self.button_2 = QPushButton("subtraction", self)
        self.button_3 = QPushButton("multiplication", self)
        self.button_4 = QPushButton("division", self)
        layout = QVBoxLayout(self)
        layout.addWidget(self.line_1)
        layout.addWidget(self.line_2)
        layout.addWidget(self.button_1)
        layout.addWidget(self.button_2)
        layout.addWidget(self.button_3)
        layout.addWidget(self.button_4)
        layout.addWidget(self.result_label)        
        
        widget = QWidget(self)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.button_1.clicked.connect(self.sum)
        self.button_2.clicked.connect(self.subtraction)
        self.button_3.clicked.connect(self.multiply)
        self.button_4.clicked.connect(self.division)

    def sum(self):
        num1 = float(self.line_1.text())
        num2 = float(self.line_2.text())
        result = num1 + num2
        self.show_result(result)

    def subtraction(self):
        num1 = float(self.line_1.text())
        num2 = float(self.line_2.text())
        result = num1 - num2
        self.show_result(result)

    def multiply(self):
        num1 = float(self.line_1.text())
        num2 = float(self.line_2.text())
        result = num1 * num2
        self.show_result(result)

    def division(self):
        num1 = float(self.line_1.text())
        num2 = float(self.line_2.text())

        if num2 != 0:
            result = num1 / num2
            self.show_result(result)
        else:
            self.show_error("error")

    def show_result(self, result):
        self.result_label.setText(f"result: {result:.2f}")

    def show_error(self, title, message):
        self.result_label.setText(message)

app = QApplication(sys.argv)
win = Calculator()
win.show()
app.exec()
