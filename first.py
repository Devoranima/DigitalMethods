import matplotlib.pyplot as plt
import math
def calcTaylor(x):
    e = 10**(-6)
    prev = 0
    next = -0.25*(x**2)

    i = 1
    
    #y = 0.5772156649
    #ln = math.log(x)
    #sum = y + ln
    sum = 0

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
    for _ in range (int(n)):
        x = round(x, 1)
        X.append(x)
        F.append(calcTaylor(x))
        x += h
    
    plt.plot(X, F,  '-ok')
    plt.show()


if __name__ == "__main__":
    main()
