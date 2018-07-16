def ler():
    dados = open('dados.txt', 'r')
    dados = dados.readlines()
    return dados

def agencia():
    dados = ler()
    inf = len(dados)
    verify = []
    c=0
    print('|Verificar agência|')
    while c<inf:
        agencia = dados[c].split('/')
        agencia = agencia[3].split('--')
        agencia = agencia[0]
        if int(agencia[len(agencia)-1])%2 != 0:
            print('-')
            print('Dígito verificador inválido da agência na linha:',c)
            verify.append(c)
            agencia = agencia.split('-')
        if len(agencia[0]) > 4:
            print('-')
            print('Há mais do que quatro algorismos em agencia na linha:',c)
            verify.append(c)
        c+=1
    print('----------------------------------')
    return verify

def conta_corrente():
    dados = ler()
    inf = len(dados)
    verify = agencia()
    c=0
    print('|Verificar conta corrente|')
    while c<inf:
        conta = dados[c].split('/')
        conta = conta[3].split('--')
        conta = conta[1]
        if int(conta[len(conta)-1])%2 == 0:
            print('-')
            print('Dígito verificador de conta corrente inválido na linha:', c)
            verify.append(c)
        conta = conta.split('-')
        if len(conta[0]) > 5:
            print('-')
            print('Há mais do que cinco algorismos de conta corrente válidos na linha:', c)
            verify.append(c)
        c+=1
    print('----------------------------------')
    return verify


def cpf():
    dados = ler()
    inf = len(dados)
    verify = conta_corrente()
    c=0

    print('|Verificar CPF|')
    while c<inf:
        cpf = dados[c].split('/')
        cpf = cpf[0]
        if len(cpf) != 11:
            print('-')
            print('CPF digitado da linha',c,'é inválido!')
            verify.append(c)
        c+=1
    return verify

def cred():
    dados = ler()
    inf = len(dados)
    exc = cpf()
    c = 0
    
    print('----------------------------------')
    print('|Verificar Créditos e Débitos|')
    while c < inf:
        cred = dados[c].split('/')
        cred_v = cred[5]

        if c not in exc:
            if cred_v != 'D':
                print('-')
                print('Linha',c+1,'tem',cred[4],'de créditos')
            else:
                print('-')
                print('Linha',c+1,'tem',cred[4],'de débitos.')
        c+=1        
cred()
