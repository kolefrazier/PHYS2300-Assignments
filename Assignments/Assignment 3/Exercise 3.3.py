#--- Exercise 3.3 ---
from pylab import imshow, show, gray
from numpy import loadtxt

FileName = 'stm.txt'

data = loadtxt(FileName, float)
imshow(data)
show()