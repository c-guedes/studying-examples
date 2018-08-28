def lergab():
    gab2 = []
    gab = input('Entre com o gabarito:')
    gab = gab.upper()
    limite = 'E'

    #alterar validação do tamanho de gabarito
    while gab.isalpha()== False or len(gab) !=10 or max(gab) > max(limite):
        if len(gab) !=10:
            print('Tamanho do gabarito incorreto.')

        if max(gab) > max(limite):
            print('Inserir somente de A até E')

        if gab.isalpha() == False:
            print('Contem numeros ou caracteres incorretos.')
        gab = input('Entre com o gabarito:')
        gab = gab.upper()
    gab2.append(gab)
    return gab2


def lerep():
    rep = []
    limite = 'E'

    #alterar qntd de input DAS RESPOSTAS   
    c =1
    for i in range(5):
        print('Aluno',c)
        gabrep = input('Entre com a resposta do aluno:')
        c+=1
        gabrep = gabrep.upper()

        
        #alterar validação do tamanho de gabarito, deve ser igual ao lenght do lergab
        if len(gabrep) != 10:
            rep.append('foi impossivel atribuir nota, tamanho do gabarito incorreto.')
        elif not gabrep.isalpha() or max(gabrep)> max(limite):
            if max(gabrep)>max(limite) and not gabrep.isalpha():
                rep.append('foi impossivel atribuir nota, contem numeros ou caracteres incorretos e letra de gabarito inserido incorretamente.')
            elif not gabrep.isalpha():
                rep.append('foi impossivel atribuir nota, contem numeros ou caracteres incorretos.')
            elif max(gabrep) > max(limite):
                rep.append('foi impossivel atribuir nota, letra de gabarito inserido incorretamente.')
        else:
            rep.append(gabrep)
    return(rep)

    

def avalrep():
    gab = lergab()
    rep = lerep()
    imprep = []
    for i, n in enumerate(rep):
        #alterar o tamanho de verificação, deve ser igual ao length do lergab
        if len(n) == 10:
            c=0
            cc=0
            nota = 0
            #alterar o tamanho de verificação, , deve ser igual ao length do lergab
            while c < 10:
                if rep[i][c] == gab[cc][c]:
                    nota+=1   
                c+=1

            imprep.append(str(nota))

        else:
            imprep.append(n)
    return(imprep)

def impnota():
    imprep = avalrep()
    c = 0
    a = 1
    
    while c < len(imprep):
        #se o len do index for menor ou igual a dois, que compreende de 0 a 10 no caso a nota, vai cair nesse if, já que no avalrep fez append de string com length gigantes
        if len(imprep[c]) <= 2:
            print('O aluno', a, 'obteve nota', imprep[c]+'.')
            
        else:
            print('O aluno', a, imprep[c])

        a+=1
        c+=1
impnota()
