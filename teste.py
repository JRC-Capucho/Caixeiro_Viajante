# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'teste.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QWidget, QMessageBox)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(743, 394)
        Form.setLocale(QLocale(QLocale.Portuguese, QLocale.Brazil))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 251, 31))
        self.message_box = QMessageBox()
        font = QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(270, 30, 101, 31))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(18)
        self.lineEdit.setFont(font1)
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.subidaDeEncosta = QCheckBox(Form)
        self.subidaDeEncosta.setObjectName(u"subidaDeEncosta")
        self.subidaDeEncosta.setGeometry(QRect(10, 130, 221, 41))
        self.subidaDeEncosta.setFont(font)
        self.subidaDeEncostaAlterada = QCheckBox(Form)
        self.subidaDeEncostaAlterada.setObjectName(u"subidaDeEncostaAlterada")
        self.subidaDeEncostaAlterada.setGeometry(QRect(10, 181, 311, 41))
        self.subidaDeEncostaAlterada.setFont(font)
        self.buttonSend = QPushButton(Form)
        self.buttonSend.setObjectName(u"buttonSend")
        self.buttonSend.setGeometry(QRect(150, 290, 80, 32))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(540, 40, 121, 41))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(28)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.solucaoFinal = QPlainTextEdit(Form)
        self.solucaoFinal.setObjectName(u"solucaoFinal")
        self.solucaoFinal.setEnabled(False)
        self.solucaoFinal.setGeometry(QRect(440, 110, 281, 221))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(16)
        font3.setKerning(True)
        self.solucaoFinal.setFont(font3)
        self.solucaoFinal.setStyleSheet(u"color.rgb(255,255,255)")
        self.solucaoFinal.setBackgroundVisible(True)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 80, 239, 41))
        self.label_2.setFont(font)
        self.tentativas = QCheckBox(Form)
        self.tentativas.setObjectName(u"tentativas")
        self.tentativas.setGeometry(QRect(190, 220, 131, 41))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(20)
        self.tentativas.setFont(font4)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(210, 360, 341, 31))
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(14)
        self.label_4.setFont(font5)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Caixeiro Viajante", None))
        self.label.setText(QCoreApplication.translate("Form", u"Tamanho do problema:", None))
        self.subidaDeEncosta.setText(QCoreApplication.translate("Form", u"Subida de encosta", None))
        self.subidaDeEncostaAlterada.setText(QCoreApplication.translate("Form", u"Subida de encosta alterada", None))
        self.buttonSend.setText(QCoreApplication.translate("Form", u"Enviar", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Solu\u00e7\u00e3o", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"M\u00e9todos", None))
        self.tentativas.setText(QCoreApplication.translate("Form", u"Tentativas", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u00a9 Grupo Cesar, Jo\u00e3o, Lucas Adolfo, Lucas Ribeiro", None))
    # retranslateUi

