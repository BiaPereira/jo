import pylab as plt
import os
import numpy as np
import matplotlib.pyplot as plt
import itertools
import matplotlib.cbook as cbook
import matplotlib.dates as mdates
import ezodf
import math
from math import log10
from scipy.optimize import curve_fit
from scipy import asarray as ar,exp
from math import sqrt


#Opens file
#filename = input('Name of the file: ')
file = open('F2LiCl_001.txt')
print("open")
fileR = file.read()
#print (fileR)
print (type(fileR))


g = fileR.split(' ',-1)
print(g)
leng = len(g)
print (leng)

i=0
x = []
y = []
for i in range(0,leng-1,4):

    print ('Novos valores')
    print(g[i + 1])
    print(g[i+3])
    x.append(float(g[i + 1]))
    y.append(float(g[i+3]))

print(x)
print('Maximo de x', max(x))

print('Maximo de y', max(y))
print (y)





x1 = ar(x)
y1 = ar(y)

n = len(x1)
m = sum(x1*y1)/n
sigma = sqrt(sum(y1*(x1-mean)**2)/n)


def gaus(x1,a,x0,sigma):
    return a*exp(-(x1-x0)**2/(2*sigma**2))
popt,pcov = curve_fit(gaus, x1, y1, p0=[max(y1), m, sigma])

plt.plot(x1,y1,'b+:',label='data')
plt.plot(x1,gaus(x1,*popt),'ro:',label='fit')
plt.legend()
plt.show()

