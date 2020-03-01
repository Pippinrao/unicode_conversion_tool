
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from decodeUI import Ui_TransformWin

class Feature(Ui_TransformWin):
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()    
        self.setupUi(MainWindow)
        self.initUI()
        MainWindow.show()
        app.exec_()

    def initUI(self):
        self.decoding_2.clicked.connect(self.clickDecode)
        self.encode.clicked.connect(self.clickEncode)

    def clickEncode(self):
        word = self.text.toPlainText()
        ans = str(word.encode('unicode-escape'))[1:].split('\\\\')
        string = ''
        for s in ans[1:]:
            string = string + '\\' + s
        string = string[:-1]
        self.code.setText(string)

    def clickDecode(self):
        word = self.code.toPlainText()
        ans = word.encode('utf-8').decode('unicode-escape')
        self.text.setText(ans)


