from PySide6.QtWidgets import QWidget
from teste import Ui_Form
from caixeiro import Caixeiro


class Widget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.caixeiro = Caixeiro()
        self.setupUi(self)
        self.buttonSend.clicked.connect(self.clickedButton)
        self.subidaDeEncostaAlterada.checkState()
        self.lineTry.setEnabled(False)
        self.UiComponents()
        self.progressBar.setValue(0)

    def UiComponents(self):
        self.subidaDeEncostaAlterada.stateChanged.connect(self.allow)

    def allow(self):
        if not self.subidaDeEncostaAlterada.isChecked():
            self.lineTry.setEnabled(False)
        else:
            self.lineTry.setEnabled(True)

    def clickedButton(self):
        if self.subidaDeEncosta.isChecked():
            tam = int(self.lineEdit.text())

            matriz_one = self.caixeiro.gera_ambiente(5, 20, tam)
            matriz_two = self.caixeiro.gera_ambiente(1, 5, tam)
            ga_aux = 0

            # progressBar
            self.progressBar.setValue(0)
            progress = 1
            pb = tam / 100

            for i in range(tam):
                si = self.caixeiro.solucao_inicial(tam)
                vi = self.caixeiro.avalia_solucao(si, matriz_one, matriz_two, tam)

                sf, vf = self.caixeiro.encosta(si, matriz_one, matriz_two, vi)
                ga_aux += 100*(vi-vf)/vi

                if tam >= 100:
                    if i % pb == 0:
                        self.progressBar.setValue(progress)
                        progress += 1
                else:
                    progress = i * (100 / tam)
                    self.progressBar.setValue(progress)


            ga = round(ga_aux / tam,2)

            stringFinal = "Solução Inicial\n" + str(si) + "\nValor Inicial\n" + str(
                vi) + "\nSolução Final\n" + str(sf) + "\nValor Final\n" + str(vf) + "\nGanho Tempo\n" + str(ga)
            self.solucaoFinal.setPlainText(stringFinal)
            print("Subida de encosta ")


        if self.subidaDeEncostaAlterada.isChecked():
            tam = int(self.lineEdit.text())
            cont_try = int(self.lineTry.text())

            matriz_one = self.caixeiro.gera_ambiente(5, 20, tam)
            matriz_two = self.caixeiro.gera_ambiente(1, 5, tam)
            ga_aux = 0

            # progressBar
            self.progressBar.setValue(0)
            progress = 1
            pb = tam / 100

            for i in range(tam):
                si = self.caixeiro.solucao_inicial(tam)
                vi = self.caixeiro.avalia_solucao(si, matriz_one, matriz_two, tam)

                sf, vf, t = self.caixeiro.encosta_alterada(
                    si, matriz_one, matriz_two, vi,cont_try)

                ga_aux += 100*(vi-vf)/vi

                if tam >= 100:
                    if i % pb == 0:
                        self.progressBar.setValue(progress)
                        progress += 1
                else:
                    progress = i * (100 / tam)
                    self.progressBar.setValue(progress)




            ga = round(ga_aux/tam,2)

            stringFinal = "Solução Inicial\n" + str(si) + "\nValor Inicial\n" + str(
                vi) + "\nSolução Final\n" + str(sf) + "\nValor Final\n" + str(vf) + "\nGanho Tempo\n" + str(ga)

            self.solucaoFinal.setPlainText(stringFinal)

            print("Subida de encosta alterada")
            print("Contidade de tentativa",cont_try)

        if self.temperaSimulada.isChecked():

            tam = int(self.lineEdit.text())
            ga_aux = 0

            matriz_one = self.caixeiro.gera_ambiente(5, 20, tam)
            matriz_two = self.caixeiro.gera_ambiente(1, 5, tam)
            temp = self.caixeiro.gera_temp_inicial(tam,matriz_one,matriz_two)

            # progressBar
            self.progressBar.setValue(0)
            progress = 1
            pb = tam / 100

            for i in range(tam):
                si = self.caixeiro.solucao_inicial(tam)
                vi = self.caixeiro.avalia_solucao(si, matriz_one, matriz_two, tam)

                sf, vf = self.caixeiro.tempera(si,vi,matriz_one,matriz_two,temp,0.01,0.85)

                ga_aux += 100*(vi-vf)/vi

                if tam >= 100:
                    if i % pb == 0:
                        self.progressBar.setValue(progress)
                        progress += 1
                else:
                    progress = i * (100 / tam)
                    self.progressBar.setValue(progress)


            ga = round(ga_aux/tam,2)

            stringFinal = "Solução Inicial\n" + str(si) + "\nValor Inicial\n" + str(
                vi) + "\nSolução Final\n" + str(sf) + "\nValor Final\n" + str(vf) + "\nGanho Tempo\n" + str(ga)

            print(temp)
            self.solucaoFinal.setPlainText(stringFinal)
            print("Tempera Simulada")

        if not any((self.temperaSimulada.isChecked(),self.subidaDeEncosta.isChecked(),self.subidaDeEncostaAlterada.isChecked())):
            tam = int(self.lineEdit.text())
            matriz_one = self.caixeiro.gera_ambiente(5, 20, tam)
            matriz_two = self.caixeiro.gera_ambiente(1, 5, tam)

            ga_aux = 0

            si = self.caixeiro.solucao_inicial(tam)
            sf = self.caixeiro.avalia_solucao(si, matriz_one, matriz_two, tam)

            stringFinal = "Solução Inicial\n" + \
                str(si) + "\nValor Inicial\n" + str(sf)

            self.solucaoFinal.setPlainText(stringFinal)
            print('solucao inicial')

        self.progressBar.setValue(100)
        print("Clicked Button")
