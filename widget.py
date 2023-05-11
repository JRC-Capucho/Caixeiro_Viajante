from PySide6.QtWidgets import QWidget
from teste import Ui_Form
from caixeiro import Caixeiro


class Widget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.caixeiro = Caixeiro()
        self.setupUi(self)
        self.buttonSend.clicked.connect(self.clickedButton)

        if self.subidaDeEncostaAlterada.isChecked():
            print("ok")
        else:
            print("not ok")

    def clickedButton(self):
        if self.subidaDeEncosta.isChecked():
            tam = int(self.lineEdit.text())

            matriz_one = self.caixeiro.gera_ambiente(5, 20, tam)
            matriz_two = self.caixeiro.gera_ambiente(1, 5, tam)
            si = self.caixeiro.solucao_inicial(tam)
            vi = self.caixeiro.avalia_solucao(si, matriz_one, matriz_two, tam)

            sf, vf = self.caixeiro.encosta(si, matriz_one, matriz_two, vi)

            stringFinal = "Solução Inicial\n" + str(si) + "\nValor Inicial\n" + str(
                vi) + "\nSolução Final\n" + str(sf) + "\nValor Final\n" + str(vf)
            self.solucaoFinal.setPlainText(stringFinal)
            print("Subida de encosta ")

        elif self.subidaDeEncostaAlterada.isChecked():
            tam = int(self.lineEdit.text())
            cont_try = int(self.lineTry.text())
            print(cont_try)
            matriz_one = self.caixeiro.gera_ambiente(5, 20, tam)
            matriz_two = self.caixeiro.gera_ambiente(1, 5, tam)

            si = self.caixeiro.solucao_inicial(tam)
            vi = self.caixeiro.avalia_solucao(si, matriz_one, matriz_two, tam)

            sf, vf, t = self.caixeiro.encosta_alterada(
                si, matriz_one, matriz_two, vi,cont_try)

            stringFinal = "Solução Inicial\n" + str(si) + "\nValor Inicial\n" + str(
                vi) + "\nSolução Final\n" + str(sf) + "\nValor Final\n" + str(vf)

            self.solucaoFinal.setPlainText(stringFinal)
            print("Subida de encosta alterada")

        elif self.temperaSimulada.isChecked():

            tam = int(self.lineEdit.text())

            matriz_one = self.caixeiro.gera_ambiente(5, 20, tam)
            matriz_two = self.caixeiro.gera_ambiente(1, 5, tam)

            si = self.caixeiro.solucao_inicial(tam)
            vi = self.caixeiro.avalia_solucao(si, matriz_one, matriz_two, tam)

            temp = self.caixeiro.gera_temp_inicial(tam,matriz_one,matriz_two)

            sf, vf = self.caixeiro.tempera(si,vi,matriz_one,matriz_two,temp,0.001,0.9)
            ga = self.caixeiro.ganho(vi,vf)


            stringFinal = "Solução Inicial\n" + str(si) + "\nValor Inicial\n" + str(
                vi) + "\nSolução Final\n" + str(sf) + "\nValor Final\n" + str(vf) + "\nGanho Temp\n" + str(ga)

            self.solucaoFinal.setPlainText(stringFinal)
            print("Tempera Simulada")
                                           

        else:
            tam = int(self.lineEdit.text())
            matriz_one = self.caixeiro.gera_ambiente(7, 36, tam)
            matriz_two = self.caixeiro.gera_ambiente(1, 10, tam)

            si = self.caixeiro.solucao_inicial(tam)
            sf = self.caixeiro.avalia_solucao(si, matriz_one, matriz_two, tam)
            stringFinal = "Solução Inicial\n" + \
                str(si) + "\nValor Inicial\n" + str(sf)
            self.solucaoFinal.setPlainText(stringFinal)

        print("Clicked Button")
