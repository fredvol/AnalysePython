# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 09:34:45 2016

@author: fred
"""

from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np


#==============================================================================
# FUNCTION
#==============================================================================

def filterOrder1( mylist ):
   "This changes a passed list into this function"
   # Filter Accx Order 1
   mylistF1= [0.0] * len(mylist)
   mylistF1[0]=  (mylist[0])

   # treatement for Acc X
   for i in range(1, len(mylist)-1):

        mylistF1[i]= (F1param1*mylistF1[i-1]) + ((1-F1param1)*mylist[i])
   
   return mylistF1;
   
   
## AVerage 10
def avg10( mylist ):
    submylist = mylist[1:10]
    mylistAvg=sum(submylist)/len(submylist)
    return mylistAvg;

#==============================================================================
# Import data
#==============================================================================
style.use('ggplot')
path="Data/RecACC_20161218193156.txt"
#path="Data/RecACC_20161214193205.txt"

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


#==============================================================================
# ## FILTER
#==============================================================================

#Parameter 
F1param1=0.8
F1limit1=3

# Filter Order 1

accxF1 = filterOrder1(accx)
accyF1 = filterOrder1(accy)
acczF1 = filterOrder1(accz)


#==============================================================================
# Find limits
#==============================================================================

AccXF1Avg=avg10(accxF1)
AccYF1Avg=avg10(accyF1)
AccZF1Avg=avg10(acczF1)

AccXUpper = AccXF1Avg + F1limit1
AccXLower = AccXF1Avg - F1limit1

AccYUpper = AccYF1Avg + F1limit1
AccYLower = AccYF1Avg - F1limit1

AccZUpper = AccZF1Avg + F1limit1
AccZLower = AccZF1Avg - F1limit1



#==============================================================================
# ## PLOT GRAPH
#==============================================================================

f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)


ax1.plot(timeS,accx)
ax1.plot(timeS,accxF1)
ax1.axhline(y=AccXUpper, xmin=0, xmax=timeS[-1], linewidth=1, color = 'g')
ax1.axhline(y=AccXLower, xmin=0, xmax=timeS[-1], linewidth=1, color = 'g')


ax2.plot(timeS,accy)
ax2.plot(timeS,accyF1)
ax2.axhline(y=AccYUpper, xmin=0, xmax=timeS[-1], linewidth=1, color = 'g')
ax2.axhline(y=AccYLower, xmin=0, xmax=timeS[-1], linewidth=1, color = 'g')

ax3.plot(timeS,accz)
ax3.plot(timeS,acczF1)
ax3.axhline(y=AccZUpper, xmin=0, xmax=timeS[-1], linewidth=1, color = 'g')
ax3.axhline(y=AccZLower, xmin=0, xmax=timeS[-1], linewidth=1, color = 'g')




# Add label:
ax1.set_ylabel("Accel X")
ax2.set_ylabel("Accel Y")
ax3.set_ylabel("Accel Z")

plt.xlabel('Time (s) ')


f.subplots_adjust(hspace=0)
f.suptitle('Acceleration (m/s^2)', size=16)



f.show()





