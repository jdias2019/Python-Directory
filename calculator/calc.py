import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Calculator")
window.setFixedSize(420, 600)

num1 = ""
num2 = ""
op = ""

display = QLabel("0")
display.setAlignment(Qt.AlignRight)
display.setFixedHeight(80)
display.setFont(QFont("Arial", 32))
display.setStyleSheet("padding: 10px;")

def btn_click(value):
    global num1, num2, op

    if value == "C":
        num1 = ""
        num2 = ""
        op = ""
        display.setText("0")
        return

    if value in ["+", "-", "*", "/", "^"]:
        num1 = display.text()
        op = value
        num2 = ""
        display.setText("0")
        return

    if value == "=":
        num2 = display.text()

        if num1 == "" or op == "" or num2 == "":
            return

        n1 = float(num1)
        n2 = float(num2)
        res = 0

        if op == "+":
            res = n1 + n2
        if op == "-":
            res = n1 - n2
        if op == "*":
            res = n1 * n2
        if op == "^":
            res = n1 ** n2
        if op == "/":
            if n2 == 0:
                display.setText("Error")
                return
            else:
                res = n1 / n2

        if res == int(res):
            res = int(res)

        display.setText(str(res))
        num1 = str(res)
        num2 = ""
        op = ""
        return

    curr = display.text()
    if curr == "0":
        curr = value
    else:
        curr = curr + value
    display.setText(curr)


BTNSTYLE = "QPushButton { background-color: white; border: 1px solid #ccc; border-radius: 8px; font-size: 18px; } QPushButton:hover { background-color: #f0f0f0; } QPushButton:pressed { background-color: #ddd; }"

btnC  =  QPushButton("C")
btnPow = QPushButton("^")
btnDiv = QPushButton("/")
btnMul = QPushButton("*")
btn7  =  QPushButton("7")
btn8  =  QPushButton("8")
btn9  =  QPushButton("9")
btnMin = QPushButton("-")
btn4  =  QPushButton("4")
btn5  =  QPushButton("5")
btn6  =  QPushButton("6")
btnAdd = QPushButton("+")
btn1  =  QPushButton("1")
btn2  =  QPushButton("2")
btn3  =  QPushButton("3")
btnEq  = QPushButton("=")
btn0  =  QPushButton("0")

all_btns = [btnC, btnPow, btnDiv, btnMul, btn7, btn8, btn9, btnMin,
            btn4, btn5, btn6, btnAdd, btn1, btn2, btn3, btnEq, btn0]

for b in all_btns:
    b.setFixedHeight(90)
    b.setFont(QFont("Arial", 18))
    b.setStyleSheet(BTNSTYLE)

btnC.clicked.connect(lambda:   btn_click("C"))
btnPow.clicked.connect(lambda: btn_click("^"))
btnDiv.clicked.connect(lambda: btn_click("/"))
btnMul.clicked.connect(lambda: btn_click("*"))
btn7.clicked.connect(lambda:   btn_click("7"))
btn8.clicked.connect(lambda:   btn_click("8"))
btn9.clicked.connect(lambda:   btn_click("9"))
btnMin.clicked.connect(lambda: btn_click("-"))
btn4.clicked.connect(lambda:   btn_click("4"))
btn5.clicked.connect(lambda:   btn_click("5"))
btn6.clicked.connect(lambda:   btn_click("6"))
btnAdd.clicked.connect(lambda: btn_click("+"))
btn1.clicked.connect(lambda:   btn_click("1"))
btn2.clicked.connect(lambda:   btn_click("2"))
btn3.clicked.connect(lambda:   btn_click("3"))
btnEq.clicked.connect(lambda:  btn_click("="))
btn0.clicked.connect(lambda:   btn_click("0"))

grid = QGridLayout()
grid.setSpacing(8)
grid.addWidget(btnC,   0, 0)
grid.addWidget(btnPow, 0, 1)
grid.addWidget(btnDiv, 0, 2)
grid.addWidget(btnMul, 0, 3)
grid.addWidget(btn7,   1, 0)
grid.addWidget(btn8,   1, 1)
grid.addWidget(btn9,   1, 2)
grid.addWidget(btnMin, 1, 3)
grid.addWidget(btn4,   2, 0)
grid.addWidget(btn5,   2, 1)
grid.addWidget(btn6,   2, 2)
grid.addWidget(btnAdd, 2, 3)
grid.addWidget(btn1,   3, 0)
grid.addWidget(btn2,   3, 1)
grid.addWidget(btn3,   3, 2)
grid.addWidget(btnEq,  3, 3, 2, 1)
btnEq.setFixedHeight(188)
grid.addWidget(btn0,   4, 0, 1, 3)

main_layout = QVBoxLayout()
main_layout.setSpacing(8)
main_layout.setContentsMargins(15, 15, 15, 15)
main_layout.addWidget(display)
main_layout.addLayout(grid)

window.setLayout(main_layout)
window.show()
sys.exit(app.exec_())
