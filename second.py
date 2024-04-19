from first import calcTaylor
import matplotlib.pyplot as plt
from scipy.special import sici
import numpy as np
import math 

a = 0.4
b = 4 
h = 0.2
n = (b - a)/.2 + 1
p = a
lmbd = 0.5772156649

X = []
F = []
for _ in range (int(n)):
  p = round(p, 1)
  X.append(p)
  F.append(calcTaylor(p))
  p += h

def calcMyIntegralCosine(x):
  ln = np.log(x)
  return sici(x)[1] - lmbd - ln

def Lagrange(x):
  res = 0
  for i in range(len(X)):
    mult = 1
    for j in range(len(X)):
      if i == j: continue
      mult *= (x - X[j])/(X[i] - X[j])
    res += F[i]*mult
  return res

def main():
  fig, ax = plt.subplots()

  #ax.plot(X, F,  '-ok', label='MyCi(x)')

  x = np.linspace(0.4, 4)
  ax.plot(x, Lagrange(x), color='red')
  ax.plot(x, calcMyIntegralCosine(x), '--', color='blue')
  plt.show()



if __name__ == "__main__":
  main()
