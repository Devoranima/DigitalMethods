import math

def calcSmallFunction(x):
  if x != 0: return (math.cos(x) - 1)/x


def calcBigFunction(arg, n):
  delta = arg / n

  x = 0

  sum = 0
  for _ in range(n):
    sum += delta*calcSmallFunction(x + delta/2)
    x+=delta
  return sum


def calcMainFunction(x):
  n = 1
  e = 10 ** (-4)

  prev = calcBigFunction(x, n)
  n *= 2
  next = calcBigFunction(x, n)
  while abs(next - prev) > e:
    prev = next
    n *= 2
    next = calcBigFunction(x, n)
  return round(prev, 4)

def main():
  a = 0.4
  b = 4 
  h = 0.2
  n = (b - a)/.2 + 1

  x = a
  for _ in range (int(n)):
    x = round(x, 1)
    print(x, calcMainFunction(x))
    x += h


if __name__ == "__main__":
    main()
