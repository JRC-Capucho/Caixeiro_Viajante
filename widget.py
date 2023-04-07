from PySide6.QtWidgets import QWidget
from teste import Ui_Form

class Widget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttonSend.clicked.connect(self.clickedButton)



    def clickedButton(self):
        print("Clicked Button")
        self.labelSF.setText(self.lineEdit.text())
        self.labelSI.setText(self.lineEdit.text())

    def textEdit(self):
        print("Tamanho do problema",self.lineEdit.text())
        self.labelSF.setText(self.lineEdit.text())
        self.labelSI.setText(self.lineEdit.text())
        


