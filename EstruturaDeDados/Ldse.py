class Node:
    def __init__(self, valor, prox):
        self.info = valor
        self.prox = prox


class Ldse:

    def __init__(self):
        self.prim = self.prox = None
        self.ult = self.prox = None
        self.__quant = 0

    def inserirInicio(self, valor):
        if self.__quant == 0:
            self.prim = self.ult = Node(valor, None)

        else:
            self.prim = Node(valor, self.prim)
        self.__quant += 1


    def inserirFim(self,valor):
        if self.__quant!=0:
            self.ult.prox = self.ult = Node(valor,None)
        else:
            self.prim = self.ult = Node(valor,None)

        self.__quant+=1


    def inserirDepois(self,valor,valor2):
        aux = self.prim
        while aux != None:
            if aux.info == valor:
                if aux.prox == None:
                    self.prim = self.ult = Node(valor, None)
                else:
                    aux.prox = Node(valor2,aux.prox)

                self.__quant+=1

            aux = aux.prox

    def removerInicio(self):
        if self.__quant == 1:
            self.prim = self.ult = None

        else:
            self.prim = self.prim.prox

        self.__quant -= 1

    def removerFim(self):
        aux = self.prim
        if self.__quant == 1:
            self.prim = self.ult = None


        else:
            while aux.prox != self.ult:
                aux = aux.prox
            self.ult = aux
            aux.prox = None

        self.__quant -= 1


    def show(self):
        i = 0
        aux = self.prim
        while aux != None:
            print(aux.info)
            aux = aux.prox
            i += 1