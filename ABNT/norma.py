def nomeABNT(string):
    string = string.upper()
    string = string.split(' ')

#REMOVER DA LISTA PRINCIPAL STRING
    acro = ['DE', 'DA', 'DOS', 'DAS', 'E']
    for i in acro:
        if i in string:
            string.remove(i)

#VERIFICAR AGNOMES / REORDENAR CRIANDO OUTRA LISTA
    verify = 0
    agnome = ['JUNIOR', 'JÚNIOR', 'NETO', 'NETA', 'SOBRINHO', 'SOBRINHA', 'FILHO', 'FILHA']


    # VERIFICAÇÃO SE O NOME FOR PEQUENO E CONTER ALGUM AGNOME, FORMATAÇÃO INCORRETA
    for i in agnome:
        if len(string) == 2 and i in string:
            verify = 3
            print('Impossivel formatação')

    #SE A FORMATAÇÃO FOR POSSIVEL, CASO A VERIFY SEJA != 3 QUE É A CONDIÇÃO
    Nstring = []
    if verify != 3:
        for i in agnome:
            if i in string:
                remover = len(string)-2
                Nstring.append(string[remover])
                Nstring.append(i)
                string.remove(i)
                string.remove(string[remover])
                verify = 1

#SE CAIR NO VERIFY 0
    c = len(string)-1
    if verify == 0:
        sobre = []
        sobre.append(string[c])
        string.remove(string[c])
        
        cont = 0
        nome = []
        while cont < len(string):
            nome.append(string[cont][0])
            cont+=1

        novo = ' '.join(sobre)
        novo2 = '. '.join(nome)
        print(novo + ',', novo2 +'.')                

#SE CAIR NO VERIFY 1
    if verify == 1:
        c = 0
        nome = []
        while c < len(string):
            nome.append(string[c][0])
            c+=1

        novo = ' '.join(Nstring)
        novo2 = '. '.join(nome)
        print(novo + ',', novo2 +'.')
