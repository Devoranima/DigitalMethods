import matplotlib.pyplot as plt
import math
from scipy.special import sici

def calcTaylor(x):
    e = 10**(-6)
    prev = 0
    next = -0.25*(x**2)

    i = 1
    
    sum = 0


    #y = 0.5772156649
    #ln = math.log(x)
    #sum += y + ln
    

    while (abs(next) > e):
        sum += next
        prev = next
        i += 1
        next = (-0.5) * x**2 * (i-1) / i**2 / (2*i-1) * prev
    
    return round(sum, 6)  



def main():
    a = 0.4
    b = 4 
    h = 0.2
    n = (b - a)/.2 + 1
    x = a

    X = []
    F = []
    C = []
    for _ in range (int(n)):
        x = round(x, 1)
        X.append(x)
        F.append(calcTaylor(x))
        #_, ci = sici(x)
        #C.append(ci)
        x += h
    
    fig, ax = plt.subplots()
    ax.plot(X, F,  '-ok', label='MyCi(x)')
    #ax.plot(X, C, '--', label='Ci(x)')
    plt.show()


if __name__ == "__main__":
    main()
