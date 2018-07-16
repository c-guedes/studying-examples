import os.path
import time
from gera import *
from mais_votados import*

def main():
    print('##################### Sistema de geração de relatórios ########################')
    op = input('\n1 - Relatórios por cargo \n2 - Relatório mais votados no cargo \n3 - Relatório mais votados município \n4 - Relatório mais votado Partido \nEscolha:')
    if op == '1':
        escolha = input('1 - Prefeito \n2 - Vereador \nOpção:')
        if escolha == '1':
            gera_prefeitos(linhas)
        else:
            gera_vereadores(linhas)
    if op == '2':
        escolha = input('1 - Prefeito \n2 - Vereador \nOpção:')
        if escolha == '1':
            if (os.path.isfile('dados/cargos/prefeitos/prefeitos_geral.csv')) == True and (os.path.isfile('dados/cargos/prefeitos/prefeitos_geral.csv')) == True:
                mais_prefeitos(escolha)
            else:
                print('\nÉ necessário gerar o relatório geral de vereadores primeiro!\n')
        if escolha == '2':
            if (os.path.isfile('dados/cargos/vereadores/vereadores_geral.csv')) == True and (os.path.isfile('dados/cargos/vereadores/vereadores_geral.csv')) == True:
                mais_vereadores(escolha)
            else:
                print('\nÉ necessário gerar o relatório geral de vereadores primeiro!\n')
        
    if op == '3':
        escolha = input('1 - Prefeito \n2 - Vereador \nOpção:')
        if escolha == '1':
            muni = input('Digite o municipio: ')
            local = muni.upper()
            if (os.path.isfile('dados/cargos/prefeitos/'+local+'.csv')) == True:
                mais_prefeitos(local)
            else:
                print('\nÉ necessário gerar o relatório geral de prefeitos primeiro!\n')
        if escolha == '2':
            muni = input('Digite o municipio: ')
            local = muni.upper()
            if (os.path.isfile('dados/cargos/vereadores/'+local+'.csv')) == True:
                mais_vereadores(local)
            else:
                print('\nÉ necessário gerar o relatório de prefeitos em '+local+' primeiro!\n')

    if op == '4':
        escolha = input('1 - Prefeito \n2 - Vereador \nOpção:')
        if escolha == '1':
            part = input('Digite o municipio: ')
            a = part.upper()
            if (os.path.isfile('dados/cargos/prefeitos/'+local+'.csv')) == True:
                mais_prefeitos(local)
            else:
                print('\nÉ necessário gerar o relatório geral de prefeitos primeiro!\n')
        if escolha == '2':
            part = input('Digite o municipio: ')
            a = muni.upper()
            if (os.path.isfile('dados/cargos/vereadores/'+local+'.csv')) == True:
                mais_vereadores(local)
            else:
                print('\nÉ necessário gerar o relatório de prefeitos em '+local+' primeiro!\n')
while 1:
    main()
