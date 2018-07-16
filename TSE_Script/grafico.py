import pip
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py



nomes = []
votos = []
D = {}
arq = open('Ranking Prefeitos.csv', 'r')
arquivo = arq.read().split('\n')
for i in range(len(arquivo)-1):
    a = arquivo[i].split(';')
    nomes.append(a[0])
    votos.append(int(a[1]))
    #D[a[0]] = int(a[1])

plt.barh(nomes, votos, color='red')
plt.title('Apuração Prefeitos')
plt.show()


'''rects = votos
for rect in rects:
    # Get X and Y placement of label from rect.
    y_value = rect.get_height()
    x_value = rect.get_x() + rect.get_width() / 2

    # Number of points between bar and label. Change to your liking.
    space = 5
    # Vertical alignment for positive values
    va = 'bottom'


plt.bar(range(len(D)), D.values(), align='center')
plt.xticks(range(len(D)), D.keys())
'''
