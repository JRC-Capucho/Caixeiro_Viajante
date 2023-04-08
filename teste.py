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
    QPlainTextEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(702, 313)
        Form.setLocale(QLocale(QLocale.Portuguese, QLocale.Brazil))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(12, 39, 239, 29))
        font = QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(261, 42, 101, 25))
        font1 = QFont()
        font1.setPointSize(18)
        self.lineEdit.setFont(font1)
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.subidaDeEncosta = QCheckBox(Form)
        self.subidaDeEncosta.setObjectName(u"subidaDeEncosta")
        self.subidaDeEncosta.setGeometry(QRect(10, 110, 217, 33))
        self.subidaDeEncosta.setFont(font)
        self.subidaDeEncostaAlterada = QCheckBox(Form)
        self.subidaDeEncostaAlterada.setObjectName(u"subidaDeEncostaAlterada")
        self.subidaDeEncostaAlterada.setGeometry(QRect(10, 181, 306, 33))
        self.subidaDeEncostaAlterada.setFont(font)
        self.buttonSend = QPushButton(Form)
        self.buttonSend.setObjectName(u"buttonSend")
        self.buttonSend.setGeometry(QRect(150, 230, 80, 32))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(500, 40, 102, 32))
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
        self.solucaoFinal.setGeometry(QRect(434, 108, 256, 191))
        font3 = QFont()
        font3.setPointSize(16)
        font3.setKerning(True)
        self.solucaoFinal.setFont(font3)
        self.solucaoFinal.setStyleSheet(u"color.rgb(255,255,255)")
        self.solucaoFinal.setBackgroundVisible(True)

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
    # retranslateUi

