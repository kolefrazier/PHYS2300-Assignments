# --- Exercise 3.4-A ---
from visual import *
L = 5
R = 0.3
GreenOrBlue = True

for i in range(-L,L+1):
    for j in range(-L,L+1):
        for k in range(-L,L+1):
            if(GreenOrBlue == True):
                sphere(pos=[i,j,k],radius=R, color=color.green)
                GreenOrBlue = False
            else:
                sphere(pos=[i,j,k],radius=R, color=color.blue)
                GreenOrBlue = True