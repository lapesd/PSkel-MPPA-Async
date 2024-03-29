#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
if sys.version_info[0] < 3:
   from StringIO import StringIO
else:
   from io import StringIO

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import pandas as pd

mpl.rcParams['axes.linewidth'] = 1.2
mpl.rcParams['font.weight'] = 'bold'

def plotBars(df, valCol, fileName):
   #print df
   #xlabels = list(set(list([val[0] for val in df[[0]].values])))
   xlabels = ["512", "1024", "2048", "4096"]
   print(xlabels)
   xs = range(len(xlabels))
   xx = list(set(list([val[0] for val in df[[1]].values])))
   w = 1.0/(len(xx)+1.0)
   i = 0
   for tileSize in xx:
      fdf = df.loc[df[' TileSize']==tileSize]
      plt.bar(np.array(xs)+i*w, [float(str(val[0]).strip().replace(',','.')) for val in fdf[[valCol]].values], width=w, label=str(tileSize) + 'x' + str(tileSize),color=cm.Blues((i+2)*70), ecolor='black')
      i += 1
   plt.xticks(np.array(xs)+w*len(xlabels)/3,xlabels)
   plt.legend(loc='best', ncol=1, fontsize=24)
   plt.suptitle('Aplicação Jacobi', fontsize=27)
   plt.xlabel(df.columns[0], fontsize=27)
   # plt.ylabel(df.columns[valCol], fontsize=18)
   plt.xlim(-0.15, 3.9)
   plt.grid(which='major', axis='y')
   plt.tick_params(labelsize=27)
   plt.tick_params(pad=12)
   # fig.suptitle('Aplicação Fur', fontsize=20)
   #plt.tick_params(width=2)

   plt.savefig(fileName, bbox_inches='tight')
   plt.clf()

def plotCurves(df, valCol, fileName):
   xs = (list([int(val[0]) for val in df[[2]].values]))
   ys = (list([int(val[0]) for val in df[[valCol]].values]))
   plt.plot(xs,ys,marker='o',linewidth=2)
   #plt.xticks(np.array(xs)+w*len(xlabels)/2,xlabels)
   #plt.legend(loc='best', ncol=1)
   plt.xlabel(df.columns[2])
   plt.ylabel(df.columns[valCol])
   #plt.xlim(-0.15, 2.9)
   plt.grid(which='major', axis='y')
   plt.tick_params(labelsize=18)
   plt.tick_params(pad=10)
   #plt.tick_params(width=2)

   plt.savefig(fileName)
   plt.clf()

#Executando testes de tempo em Barras
data = StringIO('''Matriz de Entrada; TileSize; N of Threads; Total iterations; Inner iterations; Tempo de execução (s); Energia (J)
512; 32; 16; 50; 10; 2.009544; 12.81422156
512; 64; 16; 50; 10; 1.299738; 7.40822626
512; 128; 16; 50; 10; 1.12353; 5.82196924
1024; 32; 16; 50; 10; 7.384094; 49.28125072
1024; 64; 16; 50; 10; 4.72409; 30.83714746
1024; 128; 16; 50; 10; 3.7462; 22.74137146
2048; 32; 16; 50; 10; 28.96022; 196.2910916
2048; 64; 16; 50; 10; 18.37038; 124.6619618
2048; 128; 16; 50; 10; 14.61398; 96.889665
4096; 32; 16; 50; 10; 115.75; 793.35058
4096; 64; 16; 50; 10; 73.33644; 504.1149838
4096; 128; 16; 50; 10; 57.89434; 393.3347468''')
df = pd.read_csv(data, sep=';', header=0)

plotBars(df, 5, 'jacobi-bars-time.pdf')

plotBars(df, 6, 'jacobi-bars-energy.pdf')

# #Executando testes para strongScaling
# data = StringIO('''InputArray; TileSize; N of Threads; Total iterations; inner iterations; Elapsed time (s); Energy (J)
# 2048; 128; 1; 1; 1; 68.22; 287.2061
# 2048; 128; 2; 1; 1; 35.3601; 148.8660
# 2048; 128; 4; 1; 1; 18.7993; 80.6489
# 2048; 128; 8; 1; 1; 10.6695; 45.8788
# 2048; 128; 16; 1; 1; 6.5698; 29.5641''')
# df = pd.read_csv(data, sep=';', header=0)
#
# plotCurves(df, 5, 'fur-strongScaling-time.pdf')
#
# plotCurves(df, 6, 'fur-strongScaling-energy.pdf')
#
# #Executando testes para weakScaling
# data = StringIO('''InputArray; TileSize; N of Threads; Total iterations; inner iterations; Elapsed time (s); Energy (J)
# 256; 128; 2; 1; 1; 0.6497; 2.5078
# 512; 128; 4; 1; 1; 1.2802; 5.2488
# 1024; 128; 8; 1; 1; 2.63; 11.2564
# 2048; 128; 16; 1; 1; 6.56; 29.8480''')
# df = pd.read_csv(data, sep=';', header=0)
#
# plotCurves(df, 5, 'fur-weakScaling-time.pdf')
#
# plotCurves(df, 6, 'fur-weakScaling-energy.pdf')
