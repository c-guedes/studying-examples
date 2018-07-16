listaN = []
listaC = []

i = 0
while i < 20:
    listaN.append(int(input("Entre com o número: ")))
    i+=1

i = 0
while i < len(listaN):
    c = 0
    if listaN[i] not in listaC:
        listaC.append(listaN[i])
        j = 0
        while j < len(listaN):     
            if listaN[i] == listaN[j]:
                c+=1
            if listaN[i] not in listaC: 
                listaC.append(listaN[i])
            j+=1           
        print("o número", listaN[i], "repete", c,"vez(es)")
    i+=1
