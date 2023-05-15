from random import shuffle, randint, randrange, uniform
from math import exp, fabs, log
import copy as cp


class Caixeiro():

    def gera_ambiente(self, minimo, maximo, tam):

        matriz = []
        for i in range(tam):
            linha = []
            for j in range(tam):
                if i == j:
                    linha.append(0)
                else:
                    linha.append(randint(minimo, maximo))
            matriz.append(linha)

        return matriz

    def solucao_inicial(self, tam):

        solucao = []
        for i in range(tam):
            solucao.append(i)
        shuffle(solucao)

        return solucao

    def avalia_solucao(self, solucao, matriz1, matriz2, tam):
        valor = 0
        for i in range(tam-1):
            valor += matriz1[solucao[i]][solucao[i+1]] * \
                1/matriz2[solucao[i]][solucao[i+1]]
        valor += matriz1[solucao[tam-1]][solucao[0]] * \
            1/matriz2[solucao[tam-1]][solucao[0]]

        return valor

    def gera_temp_inicial(self, n, matriz1, matriz2, P_TS = 15, P_VA = 0.999):
        solucoes = []
        valores = []

        for i in range(P_TS):
            solucoes= self.solucao_inicial(n)
            z = self.avalia_solucao(solucoes, matriz1, matriz2, n)
            valores.append(z)

        dif = 0
        cont = 0

        for i in range(P_TS-1):
            for j in range(i+1, P_TS):
                dif += fabs(valores[i]-valores[j])
                cont += 1
        dif /= cont
        temp = -dif/log(P_VA)

        return temp

    def encosta(self, solucao_inicial, matriz1, matriz2, valor):
        atual = cp.deepcopy(solucao_inicial)
        valor_atual = valor

        while True:
            novo, valor_novo = self.sucessores_enc(atual, matriz1, matriz2, valor_atual)

            if valor_novo >= valor_atual:
                return atual, valor_atual
            else:
                atual = novo
                valor_atual = valor_novo

    def encosta_alterada(self, solucao_inicial, matriz1, matriz2, valor_inicial,tentativa_max):
        atual = cp.deepcopy(solucao_inicial)
        valor_atual = valor_inicial
        tentativa = 1

        while True:
            novo, valor_novo = self.sucessores_enc(atual, matriz1, matriz2, valor_atual)

            if valor_novo >= valor_atual:
                if tentativa > tentativa_max:
                    return atual, valor_atual, tentativa
                else:
                   tentativa += 1
            else:
                atual = novo
                valor_atual = valor_novo
                tentativa = 1

    def sucessores_enc(self, solucao_inicial, matriz1, matriz2, valor):
        melhor = cp.deepcopy(solucao_inicial)
        valor_melhor = valor

        c = randrange(0, len(solucao_inicial))

        for i in range(len(solucao_inicial)):
            aux = cp.deepcopy(solucao_inicial)
            x = aux[c]
            aux[c] = aux[i]
            aux[i] = x

            valor_aux = self.avalia_solucao(aux, matriz1, matriz2, len(solucao_inicial))

            if valor_aux < valor_melhor:
                melhor = aux
                valor_melhor = valor_aux

        return melhor, valor_melhor

    def tempera(self,solucao_inicial, valor, matriz1, matriz2, tempera_inicial, tempera_final, fator_redutor):
        atual = cp.deepcopy(solucao_inicial)
        valor_atual = valor
        temp = tempera_inicial

        while temp > tempera_final:
            novo, valor_novo = self.sucessores_temp(atual, matriz1, matriz2)
            de = valor_novo - valor_atual
            if de <=0:
                atual = novo
                valor_atual = valor_novo
            else:
                aleatorio = uniform(0, 1)
                aux = exp(-de/temp)
                if aleatorio <= aux:
                    atual = novo
                    valor_atual = valor_novo
            temp = temp * fator_redutor

            return atual, valor_atual
    
    def sucessores_temp(self, solucao_inicial,matriz1, matriz2):
        aux = cp.deepcopy(solucao_inicial)

        c1 = randrange(0, len(solucao_inicial))
        c2 = randrange(0, len(solucao_inicial))

        x = aux[c1]
        aux[c1] = aux[c2]
        aux[c2] = x

        valor_aux = self.avalia_solucao(aux, matriz1, matriz2, len(solucao_inicial))

        return aux, valor_aux
