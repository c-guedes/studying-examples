import LSDE

l = LSDE.Lsde()
l.insereInicio("a")
l.insereInicio("b")
l.insereInicio("c")
#l.insereFim("teste")
#l.insereFim("foi sim")
l.insereInicio("k")
l.insereFim("u")
l.insereInicio("t")
print('-----')
l.insereDepois("c","o")
l.show()