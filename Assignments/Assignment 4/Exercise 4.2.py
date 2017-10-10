# --- Exercise 4.2 ---
from math import sqrt

def QuadraticNormal(a, b, c):
    PositiveRoot = ((-b) + sqrt(b**2 - 4*a*c))/(2*a)
    NegativeRoot = ((-b) - sqrt(b**2 - 4*a*c))/(2*a)
    return PositiveRoot, NegativeRoot
    
def QuadraticOtherWay(a, b, c):
    PositiveRoot = ((2*a)/((-b) + sqrt(b**2 - 4*a*c)))
    NegativeRoot = ((2*a)/((-b) - sqrt(b**2 - 4*a*c)))
    return PositiveRoot, NegativeRoot
    
a = float(input('Enter A: '))
b = float(input('Enter B: '))
c = float(input('Enter C: '))

print('--- Part A ---') #"Normal" Quadratic Formula
PositiveRoot, NegativeRoot = QuadraticNormal(a, b, c)
print('Positive root: {0}\nNegative root: {1}\n'.format(PositiveRoot, NegativeRoot))

print('--- Part B ---') #"Second" Quadratic Formula
PositiveRoot, NegativeRoot = QuadraticOtherWay(a, b, c)
print('Positive root: {0}\nNegative root: {1}\n'.format(PositiveRoot, NegativeRoot))

print('--- Solving 0.001x^2+100X+0.001=0 ---')
#Calculate 0.001x^2+100X+0.001=0 using both methods
#Reassign a, b, c
a = 0.0001
b = 1000.0
c = 0.001

#Simply reuse the above written statements.
#"Normal" Quadratic Formula
PositiveRoot, NegativeRoot = QuadraticNormal(a, b, c)
print('("Normal") Positive root: {0}\nNegative root: {1}'.format(PositiveRoot, NegativeRoot))
#"Second" Quadratic Formula
PositiveRoot, NegativeRoot = QuadraticOtherWay(a, b, c)
print('("Second") Positive root: {0}\nNegative root: {1}'.format(PositiveRoot, NegativeRoot))

print('--- Part c ---')