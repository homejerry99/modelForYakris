import random
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.rc("font",family='STFangsong')

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
for t in range(1000):
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
print(nList)
  
fig, ax = plt.subplots()
x = range(1000)
ax.plot(x,[np.average(nList)] * 1000, color = 'red', label = '击沉全部舰船所需平均射击次数')
ax.grid()
ax.scatter(x,nList)
plt.xlabel('试验次数')  # Add an x-label to the axes.
plt.ylabel('试验完成时的射击次数')  # Add a y-label to the axes.
plt.title('固定的巡洋与航母策略1下重复试验结果')  # Add a title to the axes.
plt.legend()  # Add a legend.
plt.show()


#print(len(grid))