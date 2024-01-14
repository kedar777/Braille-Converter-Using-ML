# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess

# Import the Tkinter-based Braille Converter code
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract
import pyttsx3
from Braille_to_text import Ui_Braille_To_Text


from Braille_Image_to_text import Ui_Braille_Image_to_text

ENGLISH_TO_BRAILLE = {
    "a": "⠁",
    "b": "⠃",
    "c": "⠉",
    "d": "⠙",
    "e": "⠑",
    "f": "⠋",
    "g": "⠛",
    "h": "⠓",
    "i": "⠊",
    "j": "⠚",
    "k": "⠅",
    "l": "⠇",
    "m": "⠍",
    "n": "⠝",
    "o": "⠕",
    "p": "⠏",
    "q": "⠟",
    "r": "⠗",
    "s": "⠎",
    "t": "⠞",
    "u": "⠥",
    "v": "⠧",
    "w": "⠺",
    "x": "⠭",
    "y": "⠽",
    "z": "⠵",
}

BRAILLE_TO_ENGLISH = {v: k for k, v in ENGLISH_TO_BRAILLE.items()}


def text_to_braille():
    input_text = entry.get().lower()
    braille_text = english_to_braille(input_text)
    output_label.config(text=braille_text)


def braille_to_text():
    input_text = entry.get()
    english_text = braille_to_english(input_text)
    output_label.config(text=english_text)
    speak_english(english_text)


def english_to_braille(text):
    braille_text = ""
    for char in text:
        braille_char = ENGLISH_TO_BRAILLE.get(char, char)
        braille_text += braille_char
    return f"Braille: {braille_text}"


def braille_to_english(text):
    english_text = "".join([BRAILLE_TO_ENGLISH.get(char, char) for char in text])
    return f"English: {english_text}"


def speak_english(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


class Ui_Main(object):
    def openWindow(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Braille_To_Text()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow3(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Braille_Image_to_text()
        self.ui.setupUi(self.window)
        self.window.show()

    def braille_enlish_speech(self):
        subprocess.Popen(["python", "braille_enlish_speech.py"])

    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(758, 625)
        Main.setStyleSheet("Background:url('abc.jpg')")
        self.label_3 = QtWidgets.QLabel(Main)
        self.label_3.setGeometry(QtCore.QRect(250, 0, 491, 91))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(36)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Main)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 91, 91))
        self.label_4.setText("")
        self.label_4.setPixmap(
            QtGui.QPixmap(":/icons/E:/YOUR_PROJECT_DIRECTORY/im1.jpg")
        )
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(Main)
        self.label.setGeometry(QtCore.QRect(220, 130, 291, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Main)
        self.pushButton.setGeometry(QtCore.QRect(180, 230, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("Background-Color:rgb(61, 182, 226)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openWindow3)

        self.pushButton_4 = QtWidgets.QPushButton(Main)
        self.pushButton_4.setGeometry(QtCore.QRect(180, 470, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("Background-Color:rgb(61, 182, 226)")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.openWindow)

        # Add a new button for Tkinter Converter
        self.pushButton_tkinter = QtWidgets.QPushButton(Main)
        self.pushButton_tkinter.setGeometry(QtCore.QRect(180, 350, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_tkinter.setFont(font)
        self.pushButton_tkinter.setStyleSheet("Background-Color:rgb(61, 182, 226)")
        self.pushButton_tkinter.setObjectName("pushButton_tkinter")
        self.pushButton_tkinter.setText("text to braille or braille to text")
        self.pushButton_tkinter.clicked.connect(self.braille_enlish_speech)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Form"))
        self.label_3.setText(_translate("Main", "Brebraille"))
        self.label.setText(_translate("Main", "Choose one of them:"))
        self.pushButton.setText(_translate("Main", "Braille Image To Text Convertor"))
        self.pushButton_4.setText(_translate("Main", "Text To Braille Converter"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QWidget()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())
