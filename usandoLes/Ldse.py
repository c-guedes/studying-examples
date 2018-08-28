class No():
    def __init__(self,valor,prox):
        self.info = valor
        self.prox = prox

class Ldse():
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0

    def show(self):
        aux = self.prim
        while aux != None:
            print(aux.info)
            aux = aux.prox
            
    def inserirInicio(self,valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor,None)
            
        else:
           self.prim = No(valor,self.prim)
            
        self.quant += 1

    def inserirFim(self,valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor,None)
            
        else:
            self.ult.prox = self.ult = No(valor,None)
            
        self.quant += 1

    def removerInicio(self):
        if self.quant == 1:
            self.prim = self.ult = None
            
        else:
            self.prim = self.prim.prox
            
        self.quant -= 1

    def removerFim(self):
        if self.quant == 1:
            self.prim = self.ult = None
            
        else:
            aux = self.prim
            while aux.prox != self.ult:
                aux = aux.prox
            self.ult = aux 
            aux.prox = None
            
        self.quant -= 1

    def removerDeterminado(self,valor):
        aux = self.prim

        while aux != None:
            if aux.info == valor:
                if aux == self.prim:
                    self.prim = aux.prox
                    
                elif aux == self.ult:
                    self.ult = aux2
                    self.ult.prox = None

                else:
                    aux2.prox = aux.prox

            self.quant -= 1
            aux2 = aux                      
            aux = aux.prox

    def inserirAntes(self,add,alvo):
        aux = self.prim
        
        if alvo == self.prim.info:
            self.prim = No(add,aux)
            self.quant += 1
            
        aux = aux.prox
        while aux != None:
            if alvo == aux.info:
                aux2.prox = No(add,aux)
                self.quant += 1

            aux2 = aux
            aux = aux.prox

    def inserirDepois(self,add,alvo):
        aux = self.prim
        
        while aux != None:
            if alvo == aux.info:
                aux.prox = No(add,aux.prox)

                self.quant += 1
            aux = aux.prox
