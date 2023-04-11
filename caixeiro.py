from random import shuffle, randint, randrange
import copy as cp

class Caixeiro():

    def gera_ambiente(self,minimo,maximo,tam):
        
        matriz = []
        for i in range(tam):
            linha = []
            for j in range(tam):
                if i==j:
                    linha.append(0)
                else:
                    linha.append(randint(minimo,maximo))
            matriz.append(linha)
        
        return matriz

    def solucao_inicial(self,tam):
        
        solucao = []
        for i in range(tam):
            solucao.append(i)
        shuffle(solucao)

        return solucao

    def avalia_solucao(self,solucao,matriz1,matriz2,matriz3,tam):
        
        valor = 0
        for i in range(tam-1):
            valor += matriz1[solucao[i]][solucao[i+1]] + 1/matriz2[solucao[i]][solucao[i+1]] + matriz3[solucao[i]][solucao[i+1]]
                     
        valor += matriz1[solucao[tam-1]][solucao[0]] + 1/matriz2[solucao[tam-1]][solucao[0]] + matriz3[solucao[tam-1]][solucao[0]]
        
        return valor


    def encosta(self,solucao,matriz1,matriz2,matriz3,valor):
        atual = cp.deepcopy(solucao)
        va = valor
        
        while True:
            novo, vn = self.sucessores_enc(atual,matriz1,matriz2,matriz3,va)
    
            if vn>=va:
                    return atual, va
            else:
                atual = novo
                va = vn


    def encosta_alterada(self,solucao,matriz1,matriz2,matriz3,valor):
        atual = cp.deepcopy(solucao)
        va = valor
        tmax = len(atual)
        t = 1
        
        while True:
            novo, vn = self.sucessores_enc(atual,matriz1,matriz2,matriz3,va)
    
            if vn>=va:
                #subida de encosta alterada
                if t>tmax:
                    return atual, va, t
                else:
                    t += 1
            else:
                atual = novo
                va = vn
                t = 1



    def sucessores_enc(self,solucao,matriz1,matriz2,matriz3,valor):
        melhor = cp.deepcopy(solucao)
        vm = valor
        
        c = randrange(0,len(solucao))
        
        for i in range(len(solucao)):
            aux = cp.deepcopy(solucao)
            x      = aux[c]
            aux[c] = aux[i]
            aux[i] = x
            
            v_aux = self.avalia_solucao(aux,matriz1,matriz2,matriz3,len(solucao))
            
            if v_aux<vm:
                melhor = aux
                vm = v_aux
        
        return melhor, vm


    # def ganho():
        # ganho = 100*(vi-vf)/vi
        # for i in N:
            # ganho
        # ganho / N
