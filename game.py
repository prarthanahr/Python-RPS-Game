# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rps_gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QBrush, QPalette, QImage
from PyQt5.QtCore import QSize
import random
from PyQt5.QtWidgets import QMessageBox


class Ui_Dialog(object):
    def setupUi(self, Dialog):

        self.max_num = 5

        Dialog.setObjectName("Dialog")
        Dialog.resize(1031, 792)

        background_img = QImage("graphics/background.jpg")
        scaled_img = background_img.scaled(QSize(1031, 792))

        palette = QPalette()
        palette.setBrush(10, QBrush(scaled_img))
        Dialog.setPalette(palette)

        Dialog.setWindowIcon(QtGui.QIcon("graphics/icon.png"))
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(50, 30, 111, 91))
        self.lcdNumber.setStyleSheet("QLCDNumber{background-color:rgb(16, 164, 255)}")
        self.lcdNumber.setDigitCount(2)
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_2.setGeometry(QtCore.QRect(780, 30, 111, 91))
        self.lcdNumber_2.setStyleSheet("QLCDNumber{background-color:rgb(16, 164, 255)}")
        self.lcdNumber_2.setDigitCount(2)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 130, 301, 101))
        font = QtGui.QFont()
        font.setPointSize(45)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{color:rgb(85, 0, 0)}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(670, 130, 361, 101))
        font = QtGui.QFont()
        font.setPointSize(45)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{color:rgb(85, 0, 0)}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 270, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(70, 330, 141, 181))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setText("")
        # self.label_4.setPixmap(QtGui.QPixmap("graphics/ROCK.png.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(770, 330, 141, 181))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setText("")
        # self.label_5.setPixmap(QtGui.QPixmap("graphics/SCISSORS.png.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(760, 270, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(330, -30, 281, 341))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("graphics/rps_img.png.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(290, 320, 411, 181))
        self.frame.setStyleSheet(
            "QFrame{background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0.208955 rgba(232, 183, 255, 116));border:3px solid yellow}\n"
            "\n"
            "\n"
            "QToolButton{border:none}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(20, 21, 111, 141))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("graphics/scissor_icon.png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(100, 100))
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.frame)
        self.toolButton_2.setGeometry(QtCore.QRect(150, 20, 111, 141))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolButton_2.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("graphics/paper_icon.png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.frame)
        self.toolButton_3.setGeometry(QtCore.QRect(280, 20, 111, 141))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolButton_3.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("graphics/rock_icon.png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_3.setObjectName("toolButton_3")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(290, 520, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLabel{color:rgb(85, 0, 0)}")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(200, 620, 411, 141))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("QLabel{color:rgb(255, 172, 37)}")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(610, 570, 151, 201))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("graphics/good_luck.png.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.toolButton_3.clicked.connect(self.rock)
        self.toolButton_2.clicked.connect(self.paper)
        self.toolButton.clicked.connect(self.scissor)

    def rock(self):
        # print("Rock")
        self.label_4.setPixmap(QtGui.QPixmap("graphics/ROCK.png"))
        self.run("Rock")

    def paper(self):
        # print("Paper")
        self.label_4.setPixmap(QtGui.QPixmap("graphics/PAPER.png"))
        self.run("Paper")

    def scissor(self):
        # print("Scissors")
        self.label_4.setPixmap(QtGui.QPixmap("graphics/SCISSORS.png"))
        self.run("Scissor")

    def run(self, player_c):

        rn = random.randint(0, 2)

        if rn == 0:
            computer_c = "Rock"
            self.label_5.setPixmap(QtGui.QPixmap("graphics/ROCK.png"))
        elif rn == 1:
            computer_c = "Paper"
            self.label_5.setPixmap(QtGui.QPixmap("graphics/PAPER.png"))
        elif rn == 2:
            computer_c = "Scissor"
            self.label_5.setPixmap(QtGui.QPixmap("graphics/SCISSORS.png"))

        game_dict = {'Rock': ["Crushes", "Scissor"],
                     "Paper": ["Covers", "Rock"],
                     "Scissor": ["Cuts", "Paper"]}

        if player_c == computer_c:
            self.label_9.setText("Draw!")
            self.label_10.clear()
            self.label_8.clear()

        elif computer_c in game_dict[player_c]:
            message = "{} {} {}".format(player_c, game_dict[player_c][0], computer_c)
            self.label_8.setText(message)
            self.label_9.setText("You Win!")
            self.label_10.setPixmap(QtGui.QPixmap("graphics/{}_win.png".format(player_c)))

            c_val = self.lcdNumber.intValue()
            next_val = c_val + 1
            self.lcdNumber.display(next_val)

            if next_val == self.max_num:
                self.end_game("Player")

        elif player_c in game_dict[computer_c]:
            message = "{} {} {}".format(computer_c, game_dict[computer_c][0], player_c)
            self.label_8.setText(message)
            self.label_9.setText("Computer Wins!")
            self.label_10.setPixmap(QtGui.QPixmap("graphics/{}_win.png".format(computer_c)))

            c_val = self.lcdNumber_2.intValue()
            next_val = c_val + 1
            self.lcdNumber_2.display(next_val)

            if next_val == self.max_num:
                self.end_game("Computer")

    def end_game(self, winner):
        box = QMessageBox()
        box.setIcon(QMessageBox.Information)
        box.setWindowIcon(QtGui.QIcon("graphics/icon.png"))
        if winner == "Player":
            box.setText("Congratulations! You Won the Game")
            box.setInformativeText("Well Played :)")
        else:
            box.setText("Computer Won The Game")
            box.setInformativeText("Better Luck Next Time :)")
        box.setWindowTitle("Game Over")
        box.exec_()

        self.reset_gui()

    def reset_gui(self):
        self.lcdNumber_2.display(0)
        self.lcdNumber.display(0)
        self.label_5.clear()
        self.label_4.clear()
        self.label_8.clear()
        self.label_10.setPixmap(QtGui.QPixmap("graphics/good_luck.png"))
        self.label_9.setText("Make Your Move!")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "RPS Game"))
        self.label.setText(_translate("Dialog", "You"))
        self.label_2.setText(_translate("Dialog", "Computer"))
        self.label_3.setText(_translate("Dialog", "You Picked:"))
        self.label_6.setText(_translate("Dialog", "Computer Picked:"))
        self.toolButton.setText(_translate("Dialog", "Scissors"))
        self.toolButton_2.setText(_translate("Dialog", "Paper"))
        self.toolButton_3.setText(_translate("Dialog", "Rock"))
        self.label_9.setText(_translate("Dialog", "Make Your Move!"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
