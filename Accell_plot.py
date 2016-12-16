# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 09:34:45 2016

@author: fred
"""

from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

## Import data
style.use('ggplot')
path="Data/RecACC_20161214193205.txt"

time= np.loadtxt(path,
                 delimiter = ',',
                 skiprows=1,
                 usecols = (2,))
accx= np.loadtxt(path,
                 delimiter = ',',
                 skiprows=1,
                 usecols = (3,))
accy= np.loadtxt(path,
                 delimiter = ',',
                 skiprows=1,
                 usecols = (4,))
accz= np.loadtxt(path,
                 delimiter = ',',
                 skiprows=1,
                 usecols = (5,))

#Convert time to Second

time0=time[0]
timeS = [(x - time0)/1000000000 for x in time]


## FILTER
# Filter Accx Order 1

accxF1= [0.0] * len(accx)
accxF1[0]=  (accx[0])

#Parameter 
F1param1=0.8
F1limit1=3

#◘ treatement for Acc X
for i in range(1, len(accx)-1):
    print("i= ", i)
    print("accxF1[i-1] ", accxF1[i-1])
    print("accx[i] ", accx[i])
    accxF1[i]= (F1param1*accxF1[i-1]) + ((1-F1param1)*accx[i])



## PLOT GRAPH

f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)


ax1.plot(timeS,accx)
ax1.plot(timeS,accxF1)
ax1.axhline(y=F1limit1, xmin=0, xmax=timeS[-1], linewidth=1, color = 'g')
ax1.axhline(y=-F1limit1, xmin=0, xmax=timeS[-1], linewidth=1, color = 'g')

ax2.plot(timeS,accy)
ax3.plot(timeS,accz)




# Add label:
ax1.set_ylabel("Accel X")
ax2.set_ylabel("Accel Y")
ax3.set_ylabel("Accel Z")

plt.xlabel('Time (s) ')


f.subplots_adjust(hspace=0)
f.suptitle('Acceleration (m/s^2)', size=16)



f.show()
