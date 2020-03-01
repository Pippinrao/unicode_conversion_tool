# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TransformWin(object):
    def setupUi(self, TransformWin):
        TransformWin.setObjectName("TransformWin")
        TransformWin.resize(574, 560)
        self.centralWidget = QtWidgets.QWidget(TransformWin)
        self.centralWidget.setObjectName("centralWidget")
        self.encode = QtWidgets.QPushButton(self.centralWidget)
        self.encode.setGeometry(QtCore.QRect(90, 210, 141, 71))
        self.encode.setObjectName("encode")
        self.text = QtWidgets.QTextEdit(self.centralWidget)
        self.text.setGeometry(QtCore.QRect(50, 40, 481, 141))
        self.text.setObjectName("text")
        self.code = QtWidgets.QTextEdit(self.centralWidget)
        self.code.setGeometry(QtCore.QRect(50, 310, 481, 151))
        self.code.setObjectName("code")
        self.decoding_2 = QtWidgets.QPushButton(self.centralWidget)
        self.decoding_2.setGeometry(QtCore.QRect(340, 210, 141, 71))
        self.decoding_2.setObjectName("decoding_2")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(20, 60, 21, 101))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(20, 330, 21, 101))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        TransformWin.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(TransformWin)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 574, 26))
        self.menuBar.setObjectName("menuBar")
        TransformWin.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(TransformWin)
        self.mainToolBar.setObjectName("mainToolBar")
        TransformWin.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(TransformWin)
        self.statusBar.setObjectName("statusBar")
        TransformWin.setStatusBar(self.statusBar)

        self.retranslateUi(TransformWin)
        QtCore.QMetaObject.connectSlotsByName(TransformWin)

    def retranslateUi(self, TransformWin):
        _translate = QtCore.QCoreApplication.translate
        TransformWin.setWindowTitle(_translate("TransformWin", "MainWindow"))
        self.encode.setText(_translate("TransformWin", "编码"))
        self.decoding_2.setText(_translate("TransformWin", "解码"))
        self.label.setText(_translate("TransformWin", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">文</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">字</span></p></body></html>"))
        self.label_2.setText(_translate("TransformWin", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">编</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">码</span></p></body></html>"))
