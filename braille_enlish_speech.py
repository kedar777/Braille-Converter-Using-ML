from PyQt5 import QtCore, QtGui, QtWidgets
import pyttsx3
import pyperclip  # Import the pyperclip library for clipboard operations

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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_input = QtWidgets.QLabel(self.centralwidget)
        self.label_input.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label_input.setObjectName("label_input")

        self.input_text = QtWidgets.QLineEdit(self.centralwidget)
        self.input_text.setGeometry(QtCore.QRect(110, 10, 161, 20))
        self.input_text.setObjectName("input_text")

        self.convert_button = QtWidgets.QPushButton(self.centralwidget)
        self.convert_button.setGeometry(QtCore.QRect(10, 50, 141, 31))
        self.convert_button.setObjectName("convert_button")
        self.convert_button.setStyleSheet("background-color: #4CAF50; color: white;")
        self.convert_button.clicked.connect(self.text_to_braille)

        self.convert_button2 = QtWidgets.QPushButton(self.centralwidget)
        self.convert_button2.setGeometry(QtCore.QRect(160, 50, 141, 31))
        self.convert_button2.setObjectName("convert_button2")
        self.convert_button2.setStyleSheet("background-color: #008CBA; color: white;")
        self.convert_button2.clicked.connect(self.braille_to_text)

        self.copy_button = QtWidgets.QPushButton(self.centralwidget)
        self.copy_button.setGeometry(QtCore.QRect(310, 90, 80, 31))
        self.copy_button.setObjectName("copy_button")
        self.copy_button.setStyleSheet("background-color: #e53935; color: white;")
        self.copy_button.clicked.connect(self.copy_output)

        self.output_label = QtWidgets.QLabel(self.centralwidget)
        self.output_label.setGeometry(QtCore.QRect(10, 90, 291, 31))
        self.output_label.setObjectName("output_label")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Braille Converter"))
        self.label_input.setText(_translate("MainWindow", "Input:"))
        self.convert_button.setText(_translate("MainWindow", "Convert to Braille"))
        self.convert_button2.setText(_translate("MainWindow", "Convert to English"))
        self.copy_button.setText(_translate("MainWindow", "Copy"))
        self.output_label.setText(_translate("MainWindow", ""))

    def text_to_braille(self):
        input_text = self.input_text.text().lower()
        braille_text = self.english_to_braille(input_text)
        self.output_label.setText(f"Braille: {braille_text}")

    def braille_to_text(self):
        input_text = self.input_text.text()
        english_text = self.braille_to_english(input_text)
        self.output_label.setText(f"English: {english_text}")
        self.speak_english(english_text)

    def english_to_braille(self, text):
        braille_text = "".join([ENGLISH_TO_BRAILLE.get(char, char) for char in text])
        return braille_text

    def braille_to_english(self, text):
        english_text = "".join([BRAILLE_TO_ENGLISH.get(char, char) for char in text])
        return english_text

    def speak_english(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    def copy_output(self):
        output_text = self.output_label.text().split(":")[1].strip()
        pyperclip.copy(output_text)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
