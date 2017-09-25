#Data correlation source: http://tylervigen.com/view_correlation?id=28590

import matplotlib.pyplot as plt
from numpy.random import rand

Year = ['2008', '2009', '2010']
Color = ['green', 'blue', 'red']
MilitarySpending = [38579, 40246, 39461]
LawnmowerDeaths = [43, 84, 73]

plt.subplot(211)
plt.plot(MilitarySpending, label='UK Military Spending')
plt.plot(LawnmowerDeaths, label='Lawnmower Deaths')

plt.show()