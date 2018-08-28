class Node:
    def __init__(self,ant, valor, prox):
        self.prox = prox
        self.ant = ant
        self.info = valor

class Lsde:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0

    def insereInicio(self,valor):
        if self.quant == 0:
            self.prim = self.ult = Node(None,valor,None)
        else:
            self.prim.ant = self.prim = Node(None, valor, self.prim)

        self.quant+=1

    def insereFim(self,valor):
        if self.quant == 0:
            self.ult = Node(valor,None,None)
        else:
            self.ult.prox = self.ult = Node(self.ult,valor,None)

        self.quant+=1

    def insereDepois(self,valor,valor2):
        aux = aux.prox
        aux1 = aux.ant
        while (aux and aux1) != None:
            print('a')
            aux=aux.prox


    def show(self):
        aux = self.prim
        while aux !=None:
            print(aux.info)
            aux = aux.prox

    def showR(self):
        aux = self.ult
        while aux != None:
            print(aux.info)
            aux = aux.ant