import random
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.rc("font",family='STFangsong')

#用于移除一整个内部的List
def removeAll(listWillBeRemoved,originalList):
    for e in listWillBeRemoved:
        originalList.remove(e)
    return originalList

#交集
def intersectionForList(listA,listB):
    intersect = []
    for eA in listA:
        if eA in listB:
            intersect.append(eA)
    return intersect

#并集
def unionForList(listA,listB):
    union = []
    union = listB.copy()
    for eA in listA:
        if eA not in listB:
            union.append(eA)
    return union

#获取一个格子周边的格子
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
   
    removeAll(posSetsWillBeRemoved,aroundGrids)
          
    return aroundGrids

#用于随机布置一艘航母
def generateCarrier(gridForGen):
    head = random.sample(gridForGen,1)[0]
    upDir = [head]
    belowDir = [head]
    leftDir = [head]
    rightDir = [head]
    i = 1
    while i < 5:
        upDir.append([head[0],head[1] + i])
        belowDir.append([head[0],head[1] - i])
        leftDir.append([head[0] - i,head[1]])
        rightDir.append([head[0] + i,head[1]])
        i = i + 1
    
    undefinedPos = [upDir,belowDir,leftDir,rightDir]
    posWillBeRemoved = []
    for e in undefinedPos:
        if len(intersectionForList(e,gridForGen)) < 5:
            posWillBeRemoved.append(e)
    removeAll(posWillBeRemoved,undefinedPos)
    if not undefinedPos:
        shipGridCarrier = generateCarrier(gridForGen)
    else:
        shipGridCarrier = random.sample(undefinedPos,1)[0]
    return shipGridCarrier

#用于随机布置一艘巡洋舰
def generateCruiser(gridForGen):
    head = random.sample(gridForGen,1)[0]
    upDir = [head]
    belowDir = [head]
    leftDir = [head]
    rightDir = [head]
    i = 1
    while i < 2:
        upDir.append([head[0],head[1] + i])
        belowDir.append([head[0],head[1] - i])
        leftDir.append([head[0] - i,head[1]])
        rightDir.append([head[0] + i,head[1]])
        i = i + 1
    
    undefinedPos = [upDir,belowDir,leftDir,rightDir]
    posWillBeRemoved = []
    for e in undefinedPos:
        if len(intersectionForList(e,gridForGen)) < 2:
            posWillBeRemoved.append(e)
    removeAll(posWillBeRemoved,undefinedPos)
    if not undefinedPos:
        shipGridCruiser = generateCruiser(gridForGen)
    else:
        shipGridCruiser = random.sample(undefinedPos,1)[0]
    return shipGridCruiser

#用于在布置完一艘船后移除被占用的的格子(自身和周边)
def removeOccupiedGrids(ship,gridForGen):
    occupied = []
    occupied = ship.copy()
    for g in ship:
        occupied = unionForList(getAroundGrids(g,gridForGen),occupied)
    removeAll(occupied,gridForGen)
    return gridForGen


nList = []
for t in range(1000):
        
    #生成用的网格和实际操作用的网格
    gridForGen = []
    for i in range(10):
        for j in range(10):
            gridForGen.append([i,j])
    grid = gridForGen.copy()

    #生成舰船
    shipGridCruiser = generateCruiser(gridForGen)
    remainGrid = removeOccupiedGrids(shipGridCruiser,gridForGen)
    shipGridCarrier = generateCarrier(gridForGen)
    remainGrid = removeOccupiedGrids(shipGridCarrier,gridForGen)
    #print(shipGridCruiser)
    #print(shipGridCarrier)

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

fig, ax = plt.subplots()
x = range(1000)
ax.plot(x,[np.average(nList)] * 1000, color = 'red', label = '击沉全部舰船所需平均射击次数')
ax.grid()
ax.scatter(x,nList)
plt.xlabel('试验次数')  # Add an x-label to the axes.
plt.ylabel('试验完成时的射击次数')  # Add a y-label to the axes.
plt.title('随机舰船分布时策略1下重复试验结果')  # Add a title to the axes.
plt.legend()  # Add a legend.
plt.show()


#print(len(grid))