import math
import matplotlib.pyplot as plt



def calcSmallFunction(x):
    if x == 0: return 0
    return (math.cos(x) - 1)/x


class calculateFunction():


#ORDER:
#0 - calcRightRectangle
#1 - calcLeftRectangle
#2 - calcMiddleRectangle
#3 - calcTrapezoid
#4 - calcSimpson
#5 - calcGauss


    def calcRightRectangle(x0, delta, n):
        x = x0
        sum = 0
        for _ in range(n):
            x+=delta
            sum += calcSmallFunction(x)
        return sum*delta 


    def calcLeftRectangle(x0, delta, n):
        x = x0
        sum = 0
        for _ in range(n):
            sum += calcSmallFunction(x)
            x+=delta
        return sum*delta        

    def calcMiddleRectangle(x0, delta, n):
        x = x0

        sum = 0
        for _ in range(n):
            sum += delta*calcSmallFunction(x + delta/2)
            x+=delta
        return sum


    def calcTrapezoid(x0, delta, n):
        x = x0
        sum = 0
        for _ in range(n):
            sum += calcSmallFunction(x)
            x+=delta
            sum += calcSmallFunction(x)
        return sum*delta/2


    def calcSimpson(x0, delta, n):
        sum = calculateFunction.calcTrapezoid(x0, delta, n) / 3
        sum += 2/3*delta*n*calcSmallFunction(delta/2)
        return sum        


#TODO
    def calcGauss(x0, delta, n):
        x = x0
        sum = 0
        a = 1 - 1 / math.sqrt(3)
        b = 1 + 1 / math.sqrt(3)
        for _ in range(n):
            sum += calcSmallFunction(x + delta*a/2) + calcSmallFunction(x + delta*b/2)
            x+=delta

        return sum*delta/2      
#end of TODO

    def calcBigFunction(x, n, funcNo):
        x0 = 0
        delta = x / n
        return calculateFunction.calculators[funcNo](x0, delta, n)
 
    calculators = (
        calcRightRectangle, 
        calcLeftRectangle,
        calcMiddleRectangle,
        calcTrapezoid,
        calcSimpson,
        calcGauss
    )   

def calcMainFunction(x):
    num = 5
    n = 1
    e = 10 ** (-4)
    
    prev = calculateFunction.calcBigFunction(x, n, num)
    n *= 2
    next = calculateFunction.calcBigFunction(x, n, num)
    while abs(next - prev) > e:
        prev = next
        n *= 2
        next = calculateFunction.calcBigFunction(x, n, num)
    return round(prev, 4)

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
    F.append(calcMainFunction(x))
    x += h
  plt.plot(X, F, '-ok')
  plt.show()


if __name__ == "__main__":
    main()
