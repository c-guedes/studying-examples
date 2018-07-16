import os.path
import time

def org_linha(linhas,i):
    arruma = linhas[i].split(';')
    arrumado = []
    for t in range(len(arruma)):
        if '"' in arruma[t]:
            arrumado.append(arruma[t].replace('"', ''))
    if len(arrumado) == 31:
        return arrumado
    else:
        cria_log_erro(i,linhas[i])
        return False
    
def cria_log_erro(i,linhas):   
    arq = open('dados/error_log.txt','a')
    arq.write('Linha;'+str(i)+';erro;'+str(linhas)+'\n')
    arq.close()

def arruma_partido(filtrado,arrumado,linhas):
    partido={}
    for c in range(len(filtrado)):
        for i in range(len(linhas)):
            if arrumado[c][0] == arrumado[i][0] and (arrumado[i][0] != 'Candidato'):
                partido[arrumado[c][0]] = arrumado[i][1]
    return partido

def cria_dic(valor):
    arrumado = []
    filtrado = []
    dic = {}
    if valor == 'prefeito':
        arq = open('dados/cargos/prefeitos/prefeitos_geral.csv', 'r')
    if valor == 'vereadores_geral':
        arq = open('dados/cargos/vereadores/vereadores_geral.csv', 'r')
    linhas = arq.read().split('\n')
    for i in range(len(linhas)):
        arruma = linhas[i].split(';')
        arrumado.append(arruma)
        for t in range(len(arrumado[i])):
            if arrumado[i][0] not in filtrado:
                filtrado.append(arrumado[i][0])
    del filtrado[0]

    for c in range(len(filtrado)):
        soma = 0
        for i in range(len(linhas)):
            if arrumado[c][0] == arrumado[i][0] and (arrumado[i][0] != 'Candidato'):
                soma = soma + int(arrumado[i][2])
        dic[arrumado[c][0]] = soma
    del dic['Candidato']

    partido = arruma_partido(filtrado,arrumado,linhas)
    
    if valor == 'prefeito':
        print('Relatório concluido |################|100%\n')
        escreve = open('dados/prefeitos.csv', 'w')
        escreve.write('CANDIDATO;'+'VOTOS;'+'COLIGAÇÃO'+'\n')
        for i in dic:
            print(i,dic[i],partido[i])
            escreve = open('dados/prefeitos.csv', 'a')
            escreve.write(str(i)+';'+str(dic[i])+';'+str(partido[i])+'\n')
            escreve.close()
            
    if valor == 'vereadores_geral':
        print('Relatório concluido |################|100%\n')
        escreve = open('dados/vereadores.csv', 'w')
        escreve.write('CANDIDATO;'+'VOTOS;'+'COLIGAÇÃO'+'\n')
        for i in dic:
            print(i,dic[i],partido[i])
            escreve = open('dados/vereadores.csv', 'a')
            escreve.write(str(i)+';'+str(dic[i])+';'+str(partido[i])+'\n')
            escreve.close()
    print('\n')
        
def gera_prefeitos(linhas):
    escolha = input('1 - Relatório Geral \n2 - Por município \n3 - Partido \nEscolha:')
    if escolha == '1':
        print('\nGerando relatório   |####            |10%')
        arq_1 = open('dados/cargos/prefeitos/prefeitos_geral.csv', 'w')
        arq_1.write('Candidato;Coligação;Votos;\n')
        arq_1.close()
        for i in range(len(linhas)):
            arruma = org_linha(linhas,i)
            if (arruma != False):
                if arruma[5] == '11':
                    arq_1 = open('dados/cargos/prefeitos/prefeitos_geral.csv', 'a')
                    arq_1.write(arruma[22]+';'+arruma[11]+';'+arruma[23]+'\n')
                    arq_1.close()
                    valor = 'prefeito'
                    
            if i > len(linhas)/2 and not i > (len(linhas)/2)+1:
                print('Gerando relatório   |########        |50%')
        cria_dic(valor)
    ## opção 2
    if escolha == '2':
        muni = input('Nome do municipio:')
        print('\nGerando relatório   |####            |10%')
        a = muni.upper()
        if 'ARAGUA' in a:
            a ='ARAGUAÍNA'
        if 'COLINAS' in a:
            a ='COLINAS DO TOCANTINS'
        arq_1 = open('dados/cargos/prefeitos/'+a+'.csv', 'w')
        arq_1.write('Candidato;Coligação;Votos;\n')
        arq_1.close()      
            
        for i in range(len(linhas)):
            arruma = org_linha(linhas,i)
            if (arruma != False):
                if arruma[5] == '11' and (a in arruma[13]):
                    arq_2 = open('dados/cargos/prefeitos/'+arruma[13]+'.csv', 'a')
                    arq_2.write(arruma[22]+';'+arruma[11]+';'+arruma[23]+'\n')
                    arq_2.close()
                    valor = 'municipio'
                    
                if i == int(len(linhas)/2):
                    print('Gerando relatório   |############    |50%')
                          
        print('Relatório concluido |################|100%\n')
    ## opção 3
    if escolha == '3':
        part = input('Digite a sigla do Partido:')
        print('\nGerando relatório   |####            |10%')
        a = part.upper()
        arq_1 = open('dados/cargos/prefeitos/'+a+'.csv', 'w')
        arq_1.write('Candidato;Votos;\n')
        arq_1.close()           
        for i in range(len(linhas)):
            arruma = org_linha(linhas,i)
            if (arruma != False):
                
                if arruma[5] == '11' and (a == arruma[11]):
                    arq_2 = open('dados/cargos/prefeitos/'+a+'.csv', 'a')
                    arq_2.write(arruma[22]+';'+arruma[23]+'\n')
                    arq_2.close()
                    valor = a
                    
            if i > len(linhas)/2 and not i > (len(linhas)/2)+1:
                print('Gerando relatório   |########        |50%')
        print('Relatório concluido |################|100%\n')
                
def gera_vereadores(linhas):
    escolha = input('1 - Relatório Geral \n2 - Por município \n3 - Partido \nEscolha:')
    if escolha == '1':
        print('\nGerando relatório   |####            |10%')
        inicio = time.time()
        arq_1 = open('dados/cargos/vereadores/vereadores_geral.csv', 'w')
        arq_1.write('Candidato;Coligação;Votos;\n')
        arq_1.close()
        for i in range(len(linhas)):
            arruma = org_linha(linhas,i)
            if (arruma != False):
                if arruma[5] == '13':
                    arq_1 = open('dados/cargos/vereadores/vereadores_geral.csv', 'a')
                    arq_1.write(arruma[22]+';'+arruma[11]+';'+arruma[23]+'\n')
                    arq_1.close()
                    valor = 'vereadores_geral'
                    
        cria_dic(valor)                    
        fim = time.time()
        print('Tempo:',str(fim-inicio)[0:4])
        print('\nRelatório concluido |#############|')

    #### opção 2   
    if escolha == '2':
        muni = input('Nome do municipio:')
        print('\nGerando relatório   |####            |10%')
        a = muni.upper()
        if 'ARAGUA' in a:
            a ='ARAGUAÍNA'
        arq_1 = open('dados/cargos/vereadores/'+a+'.csv', 'w')
        arq_1.write('Candidato;Coligação;Votos;\n')
        arq_1.close()
            
        for i in range(len(linhas)):
            arruma = org_linha(linhas,i)
            if (arruma != False):
                if arruma[5] == '13'and (a in arruma[13]): # and (arruma[22] !='NULO') and (arruma[22] !='BRANCO')
                    arq_2 = open('dados/cargos/vereadores/'+arruma[13]+'.csv', 'a')
                    arq_2.write(arruma[22]+';'+arruma[11]+';'+arruma[23]+'\n')
                    arq_2.close()
                    valor = 'municipio_vereadores'
                    
            if i > len(linhas)/2 and not i > (len(linhas)/2)+1:
                print('Gerando relatório   |########        |50%')
        print('Relatório concluido |################|100%\n')
        
    ### opção 3    
    if escolha == '3':
        part = input('Digite a sigla do Partido:')
        print('\nGerando relatório   |####            |10%')
        a = part.upper()
        arq_1 = open('dados/cargos/vereadores/'+a+'.csv', 'w')
        arq_1.write('Candidato;Votos;\n')
        arq_1.close()           
        for i in range(len(linhas)):
            arruma = org_linha(linhas,i)
            if (arruma != False):                
                if arruma[5] == '13' and (a == arruma[11]):
                    arq_2 = open('dados/cargos/vereadores/'+a+'.csv', 'a')
                    arq_2.write(arruma[22]+';'+arruma[23]+'\n')
                    arq_2.close()
                    valor = a
                    
            if i > len(linhas)/2 and not i > (len(linhas)/2)+1:
                print('Gerando relatório   |########        |50%')
        print('Relatório concluido |################|100%\n')
    return

#qntd votos arruma[23]
        
#########################################################
#leitura inicial
arq = open('teste4.txt', 'r')
inicio = time.time()
arquivo = arq.read()
fim = time.time()
print('Tempo para abrir:', str(fim - inicio)[0:4]+'ms')
# linhas
iniciol = time.time()
linhas = arquivo.split('\n')
fiml = time.time()
print('Tempo split:', str(fiml - iniciol)[0:4]+'ms')

# verifica existencia dos arquivos
#if (os.path.isfile('dados/cargos/11.csv') or os.path.isfile('dados/cargos/12.csv')) == False:
 #   separa_cod(linhas)
