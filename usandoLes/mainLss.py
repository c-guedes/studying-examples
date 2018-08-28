import LSS

l = LSS.Ldse()



l.inserirFim("d")
l.inserirInicio("c")
l.inserirFim("kk")
l.inserirFim("t")

print('#############')
l.show()
l.removerInicio()
print("%%%")
l.show()
print('removendo fim')
l.removerFim()
l.show()