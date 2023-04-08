from PySide6.QtWidgets import QWidget
from teste import Ui_Form
from caixeiro import Caixeiro

class Widget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.caixeiro = Caixeiro()
        self.setupUi(self)
        self.buttonSend.clicked.connect(self.clickedButton)
        self.solucaoFinal.isReadOnly()



    def clickedButton(self):
        if self.subidaDeEncosta.isChecked():
            tam = int(self.lineEdit.text())
            matriz_one = self.caixeiro.gera_ambiente(5,10,tam)
            matriz_two =  self.caixeiro.gera_ambiente(5,10,tam)
            matriz_three =  self.caixeiro.gera_ambiente(1,3,tam)
            si = self.caixeiro.solucao_inicial(tam)
            vi = self.caixeiro.avalia_solucao(si,matriz_one,matriz_two,matriz_three,tam)

            sf, vf = self.caixeiro.encosta(si,matriz_one,matriz_two,matriz_three,vi)

            stringFinal = "Solução Inicial\n" + str(si) + "\nValor Inicial\n" + str(vi) + "\nSolução Final\n" +str(sf) +"\nValor Final\n" + str(vf);
            self.solucaoFinal.setPlainText(stringFinal)
        else:
            tam = int(self.lineEdit.text())
            matriz_one = self.caixeiro.gera_ambiente(5,10,tam)
            matriz_two =  self.caixeiro.gera_ambiente(5,10,tam)
            matriz_three =  self.caixeiro.gera_ambiente(1,3,tam)
            si = self.caixeiro.solucao_inicial(tam)
            sf = self.caixeiro.avalia_solucao(si,matriz_one,matriz_two,matriz_three,tam)
            stringFinal = "Solução Inicial\n" + str(si) + "\nValor Inicial\n" + str(sf)
            self.solucaoFinal.setPlainText(stringFinal)
        

        print("Clicked Button")

