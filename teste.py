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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(459, 182)
        Form.setLocale(QLocale(QLocale.Portuguese, QLocale.Brazil))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(16)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)

        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 1, 0, 1, 1)

        self.labelSI = QLabel(Form)
        self.labelSI.setObjectName(u"labelSI")
        self.labelSI.setFont(font)

        self.gridLayout.addWidget(self.labelSI, 1, 2, 2, 2)

        self.checkBox_2 = QCheckBox(Form)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout.addWidget(self.checkBox_2, 2, 0, 1, 2)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 3, 2, 1, 2)

        self.labelSF = QLabel(Form)
        self.labelSF.setObjectName(u"labelSF")
        self.labelSF.setFont(font)

        self.gridLayout.addWidget(self.labelSF, 4, 3, 1, 1)

        self.buttonSend = QPushButton(Form)
        self.buttonSend.setObjectName(u"buttonSend")

        self.gridLayout.addWidget(self.buttonSend, 5, 1, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Caixeiro Viajante", None))
        self.label.setText(QCoreApplication.translate("Form", u"Tamanho do problema:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Solu\u00e7\u00e3o Inicial", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"Subida de encosta", None))
        self.labelSI.setText(QCoreApplication.translate("Form", u"saaaaaaaaa", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"Subida de encosta alterada", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Solu\u00e7\u00e3o Final", None))
        self.labelSF.setText(QCoreApplication.translate("Form", u"saaaaaaaaa", None))
        self.buttonSend.setText(QCoreApplication.translate("Form", u"Enviar", None))
    # retranslateUi

