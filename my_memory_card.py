from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
from random import*

app = QApplication([])
windows = QWidget()
windows.setWindowTitle("Memori cloob")

windows.resize(600, 400)

qlechen = QLabel("Какой национальности не существует?")

Memori__box = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton("Энцы")
rbtn_2 = QRadioButton("Смурфы")
rbtn_3 = QRadioButton("Чулмыцы")
rbtn_4 = QRadioButton("Алеуты")

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

button = QPushButton("Ответить")

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

Memori__box.setLayout(layout_ans1)

Memori = QGroupBox("Результат теста")

rezalt = QLabel("Правельно/Неправелно")
right = QLabel("Правельный ответ")

vtr_1 = QVBoxLayout()
vtr_1.addWidget(rezalt, alignment=(Qt.AlignLeft | Qt.AlignTop))
vtr_1.addWidget(right, alignment=Qt.AlignHCenter, stretch=2)

Memori.setLayout(vtr_1)

layout_lin1 = QHBoxLayout()
layout_lin2 = QHBoxLayout()
layout_lin3 = QHBoxLayout()
mine_layout = QVBoxLayout()

layout_lin1.addWidget(qlechen, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_lin2.addWidget(Memori)
layout_lin2.addWidget(Memori__box)
layout_lin3.addWidget(button)
mine_layout.addLayout(layout_lin1)
mine_layout.addLayout(layout_lin2)
mine_layout.addLayout(layout_lin3)
Memori.hide()
windows.setLayout(mine_layout)

windows.score = 0
windows.total = 0

def show_result():
    Memori__box.hide()
    Memori.show()
    button.setText("Следующий вопрос")

def show_question():
    Memori.hide()
    Memori__box.show()
    button.setText("Ответить")

    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

'''def start_test():
    if button.text()=="Ответить":
        show_result()
    else:
        show_question()'''

class Qlechen():
    def __init__(self, qlechen, right_1, wrong1, wrong2, wrong3):
        self.qlechen = qlechen
        self.right_1 = right_1
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3= wrong3




answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q: Qlechen):
    shuffle(answer)

    answer[0].setText(q.right_1)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    qlechen.setText(q.qlechen)
    right.setText(q.right_1)

    show_question()

def showe_corect(res):
    rezalt.setText(res)
    show_result()

def check_answer():
    if answer[0].isChecked():
        showe_corect("Верно")
        windows.score += 1
        print("Статистика")
        print("-Всего вопросов:", windows.total)
        print("-Правельных ответов", windows.score)
        print("Рейтинг:", windows.score / windows.total *100)
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            showe_corect("Неверно")

question_List = []
question_List.append(Qlechen("етик топ?", "топ", "не топ", "не знаю", "да обожаю"))
question_List.append(Qlechen('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
question_List.append(Qlechen('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))


def next_question():
    windows.total += 1
    print("Статистика")
    print("-Всего вопросов:", windows.total)
    print("-Правельных ответов", windows.score)
    cur_question = randint(0, len(question_List) - 1)
    next = question_List[cur_question]
    ask(next)

def start_test():
    if button.text()=="Ответить":
        check_answer()
    else:
        next_question()

next_question()

button.clicked.connect(start_test)

windows.show()
app.exec_()