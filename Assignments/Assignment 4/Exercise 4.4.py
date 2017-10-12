# --- Exercise 4.4 ---
# ======================
#    EXERCISE ANSWERS
# ======================
# On my computer, N=250,000 is the approximate limit for "integral slices calculated per second".
# Of course, this may vary depending on the computer's available resources (CPU speed, number of CPUs or chained GPUs, etc.)
from math import sqrt
import time

def xk(h, k):
    return -1+h*k
    
def yk(xk):
    return sqrt(1-xk**2)
	
def trapezoid(N, a, b): #From class - uses "slices".
    h = 2.0/N 
    y = 0.0
    for k in range (1, N):
        x = xk(h, k)
        y += yk(x)
    return y*h
    
#N = 250000
N = 100
a = 1.0
b = -1.0

start = time.time()
result = trapezoid(N, a, b)
end = time.time()

print 'N={0}\tI={1}\tTime Elapsed: {2} seconds'.format(N, result, (end-start))