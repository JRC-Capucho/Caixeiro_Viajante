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

    def gera_temp_inicial(self, n, mat, mat1, P_TS = 15, P_VA = 0.999):
        s = []
        v = []

        for i in range(P_TS):
            s = self.solucao_inicial(n)
            z = self.avalia_solucao(s, mat, mat1, n)
            v.append(z)

        dif = 0
        cont = 0

        for i in range(P_TS-1):
            for j in range(i+1, P_TS):
                dif += fabs(v[i]-v[j])
                cont += 1
        dif /= cont
        temp = -dif/log(P_VA)

        return temp

    def encosta(self, solucao, matriz1, matriz2, valor):
        atual = cp.deepcopy(solucao)
        va = valor

        while True:
            novo, vn = self.sucessores_enc(atual, matriz1, matriz2, va)

            if vn >= va:
                return atual, va
            else:
                atual = novo
                va = vn

    def encosta_alterada(self, solucao, matriz1, matriz2, valor,tmax):
        atual = cp.deepcopy(solucao)
        va = valor
        t = 1

        while True:
            novo, vn = self.sucessores_enc(atual, matriz1, matriz2, va)

            if vn >= va:
                # subida de encosta alterada
                if t > tmax:
                    return atual, va, t
                else:
                   t += 1
            else:
                atual = novo
                va = vn
                t = 1

    def sucessores_enc(self, solucao, matriz1, matriz2, valor):
        melhor = cp.deepcopy(solucao)
        vm = valor

        c = randrange(0, len(solucao))

        for i in range(len(solucao)):
            aux = cp.deepcopy(solucao)
            x = aux[c]
            aux[c] = aux[i]
            aux[i] = x

            v_aux = self.avalia_solucao(aux, matriz1, matriz2, len(solucao))

            if v_aux < vm:
                melhor = aux
                vm = v_aux

        return melhor, vm

    def sucessores_temp(self, s,v ,mat, mat1):

        aux = cp.deepcopy(s)

        c1 = randrange(0, len(s))
        c2 = randrange(0, len(s))

        x = aux[c1]
        aux[c1] = aux[c2]
        aux[c2] = x

        v_aux = self.avalia_solucao(aux, mat, mat1, len(s))

        return aux, v_aux

    def tempera(self,s, v, mat, mat1, tempera_inicial, tempera_final, fator_redutor):
        atual = cp.deepcopy(s)
        va = v
        temp = tempera_inicial

        while temp > tempera_final:
            novo, vn = self.sucessores_temp(atual,va ,  mat, mat1)
            de = vn - va
            if de <= 0:
                atual = novo
                va = vn
            else:
                ale = uniform(0, 1)
                aux = exp(-de/temp)
                if ale <= aux:
                    atual = novo
                    va = vn
        temp = temp * fator_redutor

        return atual, va

