#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle


class Question( ):
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Какой национальности не существует?', 'Смурфы', 'Энцы', 'Чулымци', 'Алеуты'))
question_list.append(Question('Сколько дней шла блокада Ленинграда?', '872', '900', '905', '800'))
question_list.append(Question("Какой калибр орудия у танка Т-34-85?", '85 мм', '90 мм', '80 мм', '610 мм'))
shuffle(question_list)
app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')

btn_OK = QPushButton('Ответить')
question1 = QLabel('Какой нацтональности не существует')
RGB = QGroupBox('Варианты отвентов')
btn1 = QRadioButton('Смурфы')
btn2 = QRadioButton('Энцы')
btn3 = QRadioButton('Чулымцы')
btn4 = QRadioButton('Алеуты')

AnswerButtonGroup = QButtonGroup()
AnswerButtonGroup.addButton(btn1)
AnswerButtonGroup.addButton(btn2)
AnswerButtonGroup.addButton(btn3)
AnswerButtonGroup.addButton(btn4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(btn1)
layout_ans2.addWidget(btn2)
layout_ans3.addWidget(btn3)
layout_ans3.addWidget(btn4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RGB.setLayout(layout_ans1)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(question1, alignment =(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RGB)

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch = 1)
layout_card.addStretch(1)
layout_card.setSpacing(5)


w = QGroupBox('Результат теста')
c = QLabel('Правильно/Неправильно')
v = QLabel('Правильный ответ')
al = QVBoxLayout()
al.addWidget(c, alignment = Qt.AlignLeft)
al.addWidget(v, alignment = Qt.AlignCenter)
w.setLayout(al)
layout_line2.addWidget(w)

def show_result():
    RGB.hide()
    w.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    AnswerButtonGroup.setExclusive(False)
    btn1.setChecked(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)
    AnswerButtonGroup.setExclusive(True)
    w.hide()
    RGB.show()
    btn_OK.setText('Ответить')

def click_ok():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

btn_X = [btn1, btn2, btn3, btn4]

def ask(q: Question):
    shuffle(btn_X)
    btn_X[0].setText(q.right_answer)
    btn_X[1].setText(q.wrong1)
    btn_X[2].setText(q.wrong2)
    btn_X[3].setText(q.wrong3)
    question1.setText(q.question)
    v.setText(q.right_answer)
    show_question()

def check_answer():
    if btn_X[0].isChecked():
        c.setText('Правильно!')
        window.total= window.total + 1
    else:
        c.setText('Неправильно!')
        window.total= window.total-  1
    show_result()

def next_question():
    window.num_of_question += 1
    if window.num_of_question == len(question_list):
        result()
        window.num_of_question = 0
        window.total = 0
    h = question_list[window.num_of_question]
    ask(h)

def result():
    result_win = QMessageBox()
    percent = window.total/len(question_list) * 100
    if percent > 80:
        rs = 'Хорошо'
    elif percent <=80 and percent>60:
        rs = 'Удовлетворительно'
    else:
        rs = 'Плохо'
    result_win.setText('Ваш результат:\n' + str(window.total )+ '/' + str(len(question_list)) + '\n' + rs)
    result_win.exec_()

window.total = 1
window.num_of_question = -1
next_question()
btn_OK.clicked.connect(click_ok)
window.setLayout(layout_card)
window.show()
app.exec()