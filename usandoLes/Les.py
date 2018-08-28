class Les:
    def __init__(self):
        self.__lista = [None,None,None,None,None]
        self.__quant = 0


    def estaCheio(self):
        if self.__quant == 5:
            return True, print("Está cheia!")
        else:
            return False

    def inserirInicio(self,valor):
        if self.estaCheio() == False:
            i = self.__quant
            while i > 0:
                self.__lista[i] = self.__lista[i-1]
                i-=1
            self.__lista[0] = valor
            self.__quant+=1

    def removerInicio(self):
        i = 0
        while i < self.__quant:
            self.__lista[i] = self.__lista[i+1]
            i+=1
        self.__quant-=1

    def removerFim(self):
        self.__quant-=1


    def inserirFim(self,valor):
        if self.estaCheio() == False:
            self.__lista[self.__quant] = valor
            self.__quant+=1


    def inserirApos(self,inserir,insertei):
        j = 0
        i = self.__quant
        if self.estaCheio() == False:
            while j < self.__quant:
                try:
                    if inserir == self.__lista[j]:
                        posicao = j+1
                        while i >= posicao:
                                self.__lista[i] = self.__lista[i - 1]
                                i-=1
                        self.__lista[posicao] = insertei
                        self.__quant += 1
                except IndexError:
                    return
                j += 1

    def inserirAntes(self,valor,valor2):
        j = 0
        i = self.__quant
        if self.estaCheio() == False:
            while j < self.__quant:
                try:
                    if valor == self.__lista[j]:
                        while i >= j:
                            self.__lista[i] = self.__lista[i-1]
                            i -= 1
                        self.__lista[i+1] = valor2
                except IndexError:
                    return
                j+=1
        self.__quant += 1

    def substituir(self,valor,valor2):
        i = 0
        substituidos = 0
        while i < self.__quant:
            if self.__lista[i] == valor:
                self.__lista[i] = valor2
                substituidos+=1
            i+=1
        print("{0} foram substituidos.".format(substituidos))

    def show(self):
        print(self.__lista)