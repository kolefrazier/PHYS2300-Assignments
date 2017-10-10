# --- Exercise 4.2 ---
from math import sqrt

def QuadraticNormal(a, b, c):
    PositiveRoot = ((-b) + sqrt(b**2 - 4*a*c))/(2*a)
    NegativeRoot = ((-b) - sqrt(b**2 - 4*a*c))/(2*a)
    return PositiveRoot, NegativeRoot
    
def QuadraticOtherWay(a, b, c):
    print('lol')
    
a = float(input('Enter A: '))
b = float(input('Enter B: '))
c = float(input('Enter C: '))

print('--- Part A ---')
PositiveRoot, NegativeRoot = QuadraticNormal(a, b, c)

print('--- Part B ---')