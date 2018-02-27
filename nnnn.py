import os
import numpy as np
import matplotlib.pyplot as plt
from bisect import bisect
from lmfit.models import GaussianModel, ConstantModel
from scipy.odr import *
from lmfit import Model
import openpyxl
from math import sin, acos, cos, fabs



#Opens file
filename = 'F2LiCL_027.txt'
#filename = 'F2LiCl_001.txt'
tam = len(filename)

if filename[tam-3:tam] == 'txt':
    file = open(filename)
if filename[tam-3:tam] == 'odf':
    base = os.path.splitext(filename)[0]
    os.rename(filename, base + ".txt")
    file = open (filename[0:tam-3]+'txt')
fileR = file.read()

g = fileR.split(' ',-1)
leng = len(g)

#Two list
i=0
x = []
y = []
print(type(g))
for i in range(0,leng-1,4):

    x.append(float(g[i + 1]))
    y.append(float(g[i+3]))
file.close()

#Opens file
filename2 = 'F2LiCl_002.txt'
#filename = 'F2LiCl_001.txt'
tam2 = len(filename2)

if filename2[tam2-3:tam2] == 'txt':
    file2 = open(filename2)
if filename2[tam2-3:tam2] == 'odf':
    base2 = os.path.splitext(filename2)[0]
    os.rename(filename2, base2 + ".txt")
    file2 = open (filename2[0:tam2-3]+'txt')
fileR2 = file2.read()

o = fileR2.split(' ',-1)
leng2 = len(o)

#Two list
j=0
x2 = []
y2 = []
for j in range(0,leng2-1,4):

    x2.append(float(o[j + 1]))
    y2.append(float(o[j+3]))

# Plot
plt.plot(x, y, 'b+', x2, y2, 'g+')
plt.yscale('log', nonposy='clip')

plt.show()