#a simple SIR model written in Python
#Jon Zelner
#University of Michigan
#October 8, 2009

#import random number and plotting libraries
import random
import pylab as pl

#set quantities of individuals in each state
S = 1000
I = 1
R = 0

#here, we calculate the total number of individuals in the system 
N = S+I+R

#convert to a float so that we can use it in division without rounding errors
N = float(N)

#set the clock to zero
t = 0

#transmission parameters

#infectivity (probability of generating a new case at each step)
b = .09

#probability of recovering @ each step
g = .05

#lists for keeping track of number of individuals in each state @ each time step
sList = []
iList = []
rList = []
newIList = []

#here, we make a loop that runs as long as there are still infectious individuals
while I > 0:
    newI = 0
    
    #there is a single random trial for each susceptible individual
    for i in range(S):
        #here, we're using a frequency dependent transmission process;
        #density dependence would be b*I
        if random.random() < b*(I/N):
            newI += 1
    
    #keep track of how many individuals are recovering on this step
    recoverI = 0
    for i in range(I):
        if random.random() < g:
            recoverI += 1
    
    #then do the accounting at the end of the step
    S -= newI
    I += (newI - recoverI)
    R += recoverI
    
    #keep track of these values in a list
    sList.append(S)
    iList.append(I)
    rList.append(R)
    newIList.append(newI)
    
    #spit out the time to stdout and increment the timestep
    print('t', t)
    t += 1

print('sList', sList)
print('iList', iList)
print('rList', rList)
print('newIList', newIList)

pl.figure()
pl.plot(iList)
pl.show()
