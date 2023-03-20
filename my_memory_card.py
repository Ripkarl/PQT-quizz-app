from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QRadioButton, QWidget, QGroupBox, QButtonGroup
from random import shuffle



app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Quizz")
question_text = QLabel("what is 1+1?")
answer_button = QPushButton("Answer")
radioBox = QGroupBox("Option")
buttonGroup = QButtonGroup()
radio1 = QRadioButton ('1')
radio2 = QRadioButton ('2')
radio3 = QRadioButton ('3')
radio4 = QRadioButton ('4')

buttonGroup.addButton(radio1)
buttonGroup.addButton(radio2)
buttonGroup.addButton(radio3)
buttonGroup.addButton(radio4)

layout1 = QHBoxLayout()
layout2 = QVBoxLayout()
layout3 = QVBoxLayout()

layout2.addWidget(radio1, alignment = Qt.AlignCenter)
layout2.addWidget(radio2, alignment = Qt.AlignCenter)

layout3.addWidget(radio3, alignment = Qt.AlignCenter)
layout3.addWidget(radio4, alignment = Qt.AlignCenter)

layout1.addLayout(layout2)
layout1.addLayout(layout3)

radioBox.setLayout(layout1)

answerBox = QGroupBox()
correct_text = QLabel('Correct')
result = QLabel("The answer is here!")

colum_1 = QVBoxLayout()
colum_1.addWidget(correct_text, alignment = Qt.AlignCenter)
colum_1.addWidget(result, alignment = Qt.AlignCenter)
answerBox.setLayout(colum_1)

row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

row1.addWidget(question_text, alignment = Qt.AlignCenter)
row2.addWidget(radioBox, alignment = Qt.AlignCenter)
row2.addWidget(answerBox, alignment = Qt.AlignCenter)
answerBox.hide()
row3.addWidget(answer_button, alignment = Qt.AlignCenter )


main_layout = QVBoxLayout()
main_layout.addLayout(row1)
main_layout.addLayout(row2)
main_layout.addLayout(row3)

main_window.setLayout(main_layout)
def correct_answer():
    if radio1.isChecked():
        radioBox.hide()
        correct_text.setText("correct")
        result.setText("2")
        answerBox.show()
        answer_button.setText("Next question")
    else:
        correct_text.setText("incorrect")
        result.setText("the answer is 2")
        answerBox.show()
        radioBox.hide()
        answer_button.setText("Next question")

def show_new_question():
    answerBox.hide()
    radioBox.show()
    answer_button.setText("Answer")
    question_text = QLabel("what is 2+2?")

    buttonGroup.setExclusive(False)
    radio1.setChecked(False) 
    radio2.setChecked(False) 
    radio3.setChecked(False) 
    radio3.setChecked(False) 
    buttonGroup.setExclusive(True)

def click():
    if answer_button.text() == "Answer":
        correct_answer()
    else:
        show_new_question()

answer = [radio1, radio2, radio3, radio4]
def ask_question (question, wrong1, right, wrong2, wrong3):
    shuffle (answer)
    answer[0].setText(right)
    answer[1].setText(wrong1)
    answer[2].setText(wrong3)
    answer[3].setText(wrong2)
    question_text.setText(question)
    result.setText(right)
    show_new_question

def show_correct(res):
    correct_text.setText(res)
    show_results()

def check_answer():
    if answer[0].isChecked():
        pass
    elif answer[1].isChecked() or answer[2].isChecked() or answer [3].isChecked():
        pass




answer_button.clicked.connect(click)

main_window.show()
app.exec_()