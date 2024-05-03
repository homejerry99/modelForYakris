import random
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

def getAroundGrids(center,grid):
    up = [center[0],center[1] + 1]
    below = [center[0],center[1] - 1]
    left = [center[0] - 1,center[1]]
    right = [center[0] + 1,center[1]]
    
    aroundGrids =  [up,below,left,right]
    posSetsWillBeRemoved = []
    for pos in aroundGrids:
        if pos not in grid:
            posSetsWillBeRemoved.append(pos)
   
    for pos in posSetsWillBeRemoved:
        aroundGrids.remove(pos)
          
    return aroundGrids


shipGridCruiser = [[8,8],[8,9]]
shipGridCarrier = [[2,0],[3,0],[4,0],[5,0],[6,0]]

nList = []
grid = []
for i in range(10):
    for j in range(10):
        grid.append([i,j])
k = 0
n = 0
pointer = []
pointerSeq = []
while k < len(shipGridCarrier) + len(shipGridCruiser):
    if n > 1 and (pointerSeq[n - 1] in shipGridCarrier or pointerSeq[n - 1] in shipGridCruiser):
        aroundGrids = getAroundGrids(pointerSeq[n - 1],grid)
        #如果周边是空集...
        if not aroundGrids:
            pointer = random.sample(grid,1)[0]
        else:
            pointer = random.sample(aroundGrids,1)[0]
    else:
        pointer = random.sample(grid,1)[0]
        #print(pointer)
    if pointer in shipGridCarrier or pointer in shipGridCruiser:
        k = k + 1
        
    grid.remove(pointer)
    pointerSeq.append(pointer)
    n = n + 1
nList.append(n)
#print(pointerSeq)
print(n)
xList = []
yList = []
for wayPoint in pointerSeq:
    xList.append(wayPoint[0])
    yList.append(wayPoint[1])

fig, ax = plt.subplots()
ax.plot(xList,yList)
plt.grid()
plt.show()


'''fig, ax = plt.subplots()
x = range(1000)
ax.plot(x,[np.average(nList)] * 1000, color = 'red')
ax.scatter(x,nList)
plt.grid()
plt.show()
'''

#print(len(grid))