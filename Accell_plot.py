# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 09:34:45 2016

@author: fred
"""

from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

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




accVec= np.array([accx,accy,accz])
accT= np.linalg.norm(accVec)


# PLOT GRAPH

f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)


ax1.plot(time,accx)
ax2.plot(time,accy)
ax3.plot(time,accz)




# Add label:
ax1.set_ylabel("Accel X")
ax2.set_ylabel("Accel Y")
ax3.set_ylabel("Accel Z")

plt.xlabel('Time (ms) ')


f.subplots_adjust(hspace=0)
f.suptitle('Acceleration', size=16)






f.show()
