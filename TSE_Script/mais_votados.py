import os.path
import time

## cada requisição do usuário sera criado um relatório já pesquisado ##
def mais_votados(dic, local, cod):
    dic_v = {}
    votos = []
    nulos_brancos = []
    if (cod == 1) and (local =='1'):
        nome_m = ''
        maior = 0
        for i in dic:
            nome = i
            if (nome != 'NULO') and (nome !='BRANCO'):
                nome_m = nome+' - '+dic[i][1]
                #print(nome)
                votos.append(dic[i])
                dic_v[dic[i][0]] = nome_m
                if int(dic[i][0])> maior:
                    maior = dic[i][0]
            if nome == 'NULO':
                nulos_brancos.append(dic[i][0])
            if nome == 'BRANCO':
                nulos_brancos.append(dic[i][0])        

        print('Ranking Prefeitos.csv gerado na pasta dados.')
        print('Candidato com mais votos:', nome_m, maior, 'votos')
        
        votos.sort(reverse=True)
        for i in range(len(votos)):
            arq = open('dados/Ranking Prefeitos.csv', 'a')
            arq.write(str(dic_v[votos[i][0]])+';'+str(votos[i][0])+'\n')
            
        arq.write('NULOS;'+str(nulos_brancos[0])+'\n')
        arq.write('BRANCOS;'+str(nulos_brancos[1])+'\n')
        arq.close()
        return

    if (cod == 1) and (local !='1'):
        nome_m = ''
        maior = 0
        for i in dic:
            nome = i
            if (nome != 'NULO') and (nome !='BRANCO'):
                nome_m = nome+' - '+dic[i][1]
                #print(nome)
                votos.append(dic[i])
                dic_v[dic[i][0]] = nome_m
                if int(dic[i][0])> maior:
                    maior = dic[i][0]
            if nome == 'NULO':
                nulos_brancos.append(dic[i][0])
            if nome == 'BRANCO':
                nulos_brancos.append(dic[i][0])        

        print('Ranking Prefeitos '+local+'.csv gerado na pasta dados.')
        print('Candidato com mais votos:', nome_m, maior, 'votos')
        
        votos.sort(reverse=True)
        for i in range(len(votos)):
            arq = open('dados/Ranking Prefeitos '+local+'.csv', 'a')
            arq.write('\n'+str(dic_v[votos[i][0]])+';'+str(votos[i][0])+';'+str(local))
           
        arq.write('\nNULOS;'+str(nulos_brancos[0]))
        arq.write('\nBRANCOS;'+str(nulos_brancos[1]))
        arq.close()
        return
#### VEREADORES ##########
    if (cod == 2) and (local =='1'):
        nome_m = ''
        maior = 0
        for i in dic:
            nome = i
            if (nome != 'NULO') and (nome !='BRANCO'):
                nome_m = nome+' - '+dic[i][1]
                #print(nome)
                votos.append(dic[i])
                dic_v[dic[i][0]] = nome_m
                if int(dic[i][0])> maior:
                    maior = dic[i][0]
            if nome == 'NULO':
                nulos_brancos.append(dic[i][0])
            if nome == 'BRANCO':
                nulos_brancos.append(dic[i][0])        

        print('Ranking Prefeitos.csv gerado na pasta dados.')
        print('Candidato com mais votos:', nome_m, maior, 'votos')
        
        votos.sort(reverse=True)
        for i in range(len(votos)):
            arq = open('dados/Ranking Vereadores.csv', 'a')
            arq.write(str(dic_v[votos[i][0]])+';'+str(votos[i][0])+'\n')
            
        arq.write('NULOS;'+str(nulos_brancos[0])+'\n')
        arq.write('BRANCOS;'+str(nulos_brancos[1])+'\n')
        arq.close()
        return

    if cod == 2 and local != '1':
        nome_m = ''
        maior = 0
        for i in dic:
            nome = i
            if (nome != 'NULO') and (nome !='BRANCO'):
                nome_m = nome+' - '+dic[i][1]
                #print(nome)
                votos.append(dic[i])
                dic_v[dic[i][0]] = nome_m
                if int(dic[i][0])> maior:
                    maior = dic[i][0]
            if nome == 'NULO':
                nulos_brancos.append(dic[i][0])
            if nome == 'BRANCO':
                nulos_brancos.append(dic[i][0])        

        print('Ranking Prefeitos.csv gerado na pasta dados.')
        print('Candidato com mais votos:', nome_m, maior, 'votos')
        
        votos.sort(reverse=True)
        for i in range(len(votos)):
            arq = open('dados/Ranking Vereadores '+local+'.csv', 'a')
            arq.write(str(dic_v[votos[i][0]])+';'+str(votos[i][0])+';'+str(local)+'\n')
            
        arq.write('NULOS;'+str(nulos_brancos[0])+'\n')
        arq.write('BRANCOS;'+str(nulos_brancos[1])+'\n')
        arq.close()
        print('Ranking Vereadores '+local+'.csv gerado na pasta dados.')
        return

def mais_prefeitos(local):
    if local == '1':
        partido = ''
        arrumado = []
        filtrado = []
        votos = []
        dic = {}
        arq = open('dados/cargos/prefeitos/prefeitos_geral.csv', 'r')
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
                    partido = arrumado[i][1]
                    
            dic[arrumado[c][0]] = [soma, partido]
        del dic['Candidato']

        cod = 1
        mais_votados(dic, local, cod)
        return
    else:
        print(local)
        partido = ''
        arrumado = []
        filtrado = []
        votos = []
        dic = {}
        arq = open('dados/cargos/prefeitos/'+local+'.csv', 'r')
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
                    partido = arrumado[i][1]
                    
            dic[arrumado[c][0]] = [soma, partido]
        del dic['Candidato']

        cod = 1
        mais_votados(dic, local, cod)
        return
    
def mais_vereadores(local):
    if local == '2':
        partido = ''
        arrumado = []
        filtrado = []
        votos = []
        dic = {}
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
                    partido = arrumado[i][1]
                    
            dic[arrumado[c][0]] = [soma, partido]
        del dic['Candidato']

        cod = 1
        mais_votados(dic, local, cod)
        return
    
    else:
        print(local)
        partido = ''
        arrumado = []
        filtrado = []
        votos = []
        dic = {}
        arq = open('dados/cargos/vereadores/'+local+'.csv', 'r')
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
                    partido = arrumado[i][1]
                    
            dic[arrumado[c][0]] = [soma, partido]
        del dic['Candidato']

        cod = 1
        mais_votados(dic, local, cod)
        return
