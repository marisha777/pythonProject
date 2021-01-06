import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog

right_answers = {1: 6, 2: 4, 3: 3, 4: 5, 5: 5, 6: 2, 7: 1, 8: 1, 9: 3, 10: 3, 11: 4, 12: 3, 13: 3, 14: 4, 15: 5}
datas_about_user = []


class InputDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('IQ_test_dialog.ui', self)

        self.setWindowTitle('IQ тест')
        self.setFixedSize(239, 133)
        self.buttonBox.accepted.connect(self.showmainwindow)

    def showmainwindow(self):
        global datas_about_user
        name = self.le_name.text()
        age = self.sb_age.text()
        datas_about_user.append(name)
        datas_about_user.append(age)
        self.mainwindow = IQtest()
        self.mainwindow.show()


class Result(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('IQ_test2.ui', self)

        self.setWindowTitle('IQ тест')
        self.setFixedSize(680, 510)
        self.l_text_result.setAlignment(Qt.AlignCenter)
        self.l_text_result_2.setAlignment(Qt.AlignCenter)
        self.file = open('result_of_IQ_test', mode='r', encoding='utf8').read().split('\n\n')
        self.count_iq()

    def count_iq(self):
        global datas_about_user
        if datas_about_user[2] == 15:
            self.l_text_result.setText(datas_about_user[0] + ', ' + self.file[0].split('\n')[0])
            self.l_text_result_2.setText(self.file[0].split('\n')[1])
        elif datas_about_user[2] == 14:
            self.l_text_result.setText(datas_about_user[0] + ', ' + self.file[1].split('\n')[0])
            self.l_text_result_2.setText(self.file[1].split('\n')[1])
        elif datas_about_user[2] == 13:
            self.l_text_result.setText(datas_about_user[0] + ', ' + self.file[2].split('\n')[0])
            self.l_text_result_2.setText(self.file[2].split('\n')[1])
        elif datas_about_user[2] == 12:
            self.l_text_result.setText(datas_about_user[0] + ', ' + self.file[3].split('\n')[0])
            self.l_text_result_2.setText(self.file[3].split('\n')[1])
        elif datas_about_user[2] == 11:
            self.l_text_result.setText(datas_about_user[0] + ', ' + self.file[4].split('\n')[0])
            self.l_text_result_2.setText(self.file[4].split('\n')[1])
        elif datas_about_user[2] == 10:
            self.l_text_result.setText(datas_about_user[0] + ', ' + self.file[5].split('\n')[0])
            self.l_text_result_2.setText(self.file[5].split('\n')[1])
        elif datas_about_user[2] == 9:
            self.l_text_result.setText(datas_about_user[0] + ', ' + self.file[6].split('\n')[0])
            self.l_text_result_2.setText(self.file[6].split('\n')[1])
        elif datas_about_user[2] == 8:
            self.l_text_result.setText(datas_about_user[0] + ', ' + self.file[7].split('\n')[0])
            self.l_text_result_2.setText(self.file[7].split('\n')[1])
        elif 5 < datas_about_user[2] < 8:
            self.l_text_result.setText(datas_about_user[0] + ', ' + self.file[8].split('\n')[0])
            self.l_text_result_2.setText(self.file[8].split('\n')[1])
        elif 3 < datas_about_user[2] < 6:
            self.l_text_result.setText(datas_about_user[0] + ', ' + self.file[9].split('\n')[0])
            self.l_text_result_2.setText(self.file[9].split('\n')[1])
        elif -1 < datas_about_user[2] < 4:
            self.l_text_result.setText(datas_about_user[0] + ', ' + self.file[10].split('\n')[0])
            self.l_text_result_2.setText(self.file[10].split('\n')[1])


class IQtest(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('IQ_test.ui', self)

        self.setWindowTitle('IQ тест')
        self.setFixedSize(680, 510)

        self.file_images = open('file_of_names_of_images.txt', encoding='utf8').read().split('\n')
        self.file_main_image = self.file_images[0].split()
        self.file_images1 = self.file_images[1].split()
        self.file_images2 = self.file_images[2].split()
        self.file_images3 = self.file_images[3].split()
        self.file_images4 = self.file_images[4].split()
        self.file_images5 = self.file_images[5].split()
        self.file_images6 = self.file_images[6].split()

        self.btn_picture_answer_1.clicked.connect(self.answer)
        self.btn_picture_answer_2.clicked.connect(self.answer)
        self.btn_picture_answer_3.clicked.connect(self.answer)
        self.btn_picture_answer_4.clicked.connect(self.answer)
        self.btn_picture_answer_5.clicked.connect(self.answer)
        self.btn_picture_answer_6.clicked.connect(self.answer)
        self.btn_skip.clicked.connect(self.skip)
        self.l_count_of_tasks.setAlignment(Qt.AlignCenter)
        self.count_of_calls_btn = 1
        self.count_of_right_answers = 0
        self.age = 16

    def answer(self):
        global right_answers
        if self.sender() == self.btn_picture_answer_1:
            if right_answers[self.count_of_calls_btn] == 1:
                self.count_of_right_answers += 1
            self.run()
        elif self.sender() == self.btn_picture_answer_2:
            if right_answers[self.count_of_calls_btn] == 2:
                self.count_of_right_answers += 1
            self.run()
        elif self.sender() == self.btn_picture_answer_3:
            if right_answers[self.count_of_calls_btn] == 3:
                self.count_of_right_answers += 1
            self.run()
        elif self.sender() == self.btn_picture_answer_4:
            if right_answers[self.count_of_calls_btn] == 4:
                self.count_of_right_answers += 1
            self.run()
        elif self.sender() == self.btn_picture_answer_5:
            if right_answers[self.count_of_calls_btn] == 5:
                self.count_of_right_answers += 1
            self.run()
        elif self.sender() == self.btn_picture_answer_6:
            if right_answers[self.count_of_calls_btn] == 6:
                self.count_of_right_answers += 1
            self.run()

    def run(self):
        global datas_about_user
        if self.count_of_calls_btn == 15:
            datas_about_user.append(self.count_of_right_answers)
            self.showwindow()
        else:
            file = self.file_main_image[self.count_of_calls_btn]
            file1 = self.file_images1[self.count_of_calls_btn]
            file2 = self.file_images2[self.count_of_calls_btn]
            file3 = self.file_images3[self.count_of_calls_btn]
            file4 = self.file_images4[self.count_of_calls_btn]
            file5 = self.file_images5[self.count_of_calls_btn]
            file6 = self.file_images6[self.count_of_calls_btn]
            pixmap = QPixmap(file[1:-1])
            self.l_image.setPixmap(pixmap)
            self.btn_picture_answer_1.setIcon(QIcon(file1[1:-1]))
            self.btn_picture_answer_2.setIcon(QIcon(file2[1:-1]))
            self.btn_picture_answer_3.setIcon(QIcon(file3[1:-1]))
            self.btn_picture_answer_4.setIcon(QIcon(file4[1:-1]))
            self.btn_picture_answer_5.setIcon(QIcon(file5[1:-1]))
            self.btn_picture_answer_6.setIcon(QIcon(file6[1:-1]))
            self.count_of_calls_btn += 1
            self.l_count_of_tasks.setText(str(self.count_of_calls_btn) + '/' + '15')

    def skip(self):
        self.run()

    def showwindow(self):
        self.resultwindow = Result()
        self.resultwindow.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = InputDialog()
    ex.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Result()
    ex.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = IQtest()
    ex.show()
    sys.exit(app.exec())
