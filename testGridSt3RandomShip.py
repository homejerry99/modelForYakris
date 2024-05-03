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
    unionR = []
    unionR = listB.copy()
    for eA in listA:
        if eA not in listB:
            unionR.append(eA)
    #总之去除一下重复...
    union = []
    for eR in unionR:
        if eR not in union:
            union.append(eR)
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

#获取一个格子周边的4角
def getAroundGridsCorner(center,grid):
    ne = [center[0] + 1,center[1] + 1]
    nw = [center[0] - 1,center[1] + 1]
    sw = [center[0] - 1,center[1] - 1]
    se = [center[0] + 1,center[1] + 1]
    aroundCorners = [ne,nw,sw,se]
    posSetsWillBeRemoved = []
    for pos in aroundCorners:
        if pos not in grid:
            posSetsWillBeRemoved.append(pos)
    removeAll(posSetsWillBeRemoved,aroundCorners)
    return aroundCorners
    
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

#获取一艘船占据的格子(自身和周边)
def getOccupiedGrids(ship,gridForGen):
    occupied = []
    occupied = ship.copy()
    for g in ship:
        occupied = unionForList(getAroundGrids(g,gridForGen),occupied)
        occupied = unionForList(getAroundGridsCorner(g,gridForGen),occupied)
    return occupied

#用于在布置完一艘船后移除被占用的的格子(自身和周边)
def removeOccupiedGrids(occupied,gridForGen):
    intersect = intersectionForList(occupied,gridForGen)
    removeAll(intersect,gridForGen)
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
    occCruiser = getOccupiedGrids(shipGridCruiser,gridForGen)
    remainGrid = removeOccupiedGrids(occCruiser,gridForGen)
    shipGridCarrier = generateCarrier(gridForGen)
    occCarrier = getOccupiedGrids(shipGridCarrier,gridForGen)
    remainGrid = removeOccupiedGrids(occCarrier,gridForGen)
    #print(shipGridCruiser)
    #print(shipGridCarrier)
    k = 0
    n = 0
    pointer = []
    pointerSeq = []
    trackingPoint = []
    trackingDirPoint = []
    carrierAlive = True
    crusierAlive = True
    while k < len(shipGridCarrier) + len(shipGridCruiser):
        dirConfirm = False
        #搜索目标
        #首先检验是否有已经被击沉的舰船，并排除周边格点
        if carrierAlive:
            hitCarrier = 0 
            for hull in shipGridCarrier:
                if hull not in grid:
                    hitCarrier = hitCarrier + 1
            if hitCarrier >= len(shipGridCarrier):
                carrierAlive = False
                removeOccupiedGrids(occCarrier,grid)
                
        if crusierAlive:
            hitCrusier = 0 
            for hull in shipGridCruiser:
                if hull not in grid:
                    hitCrusier = hitCrusier + 1
            if hitCrusier >= len(shipGridCruiser):
                crusierAlive = False
                removeOccupiedGrids(occCruiser,grid)
                
        #用于确认方向
        if n > 2: 
            dirConfirm = (trackingDirPoint in shipGridCarrier or trackingDirPoint in shipGridCruiser)
            
        if not trackingPoint:
            pointer = random.sample(grid,1)[0]
        else:
            aroundGrids = getAroundGrids(trackingPoint,grid)
            if not trackingDirPoint:
                if not aroundGrids:
                    pointer = random.sample(grid,1)[0]
                else:
                    pointer = random.sample(aroundGrids,1)[0]
            elif dirConfirm:
                stepX = trackingDirPoint[0] - trackingPoint[0]
                stepY = trackingDirPoint[1] - trackingPoint[1]
                pointer = [pointer[0] + stepX, pointer[1] + stepY]
                if pointer not in grid:
                    pointer = random.sample(grid,1)[0]
            else:
                pointer = random.sample(grid,1)[0]
                
        #命中判断
        if (pointer in shipGridCarrier or pointer in shipGridCruiser):
            if not trackingPoint:
                trackingPoint = pointer
            elif not trackingDirPoint:
                trackingDirPoint = pointer
            k = k + 1
        else:
            if trackingDirPoint:
                trackingPoint = []
                trackingDirPoint = []
                
        grid.remove(pointer)
        pointerSeq.append(pointer)
        n = n + 1
    nList.append(n)
#print(pointerSeq)

print(nList)

fig, ax = plt.subplots()
x = range(1000)
ax.plot(x,[np.average(nList)] * 1000, color = 'red', label = '全部击沉所需平均射击次数')
ax.grid()
ax.scatter(x,nList)
plt.xlabel('试验次数')  # Add an x-label to the axes.
plt.ylabel('试验完成时的射击次数')  # Add a y-label to the axes.
plt.title('随机的巡洋与航母时策略3下重复试验结果')  # Add a title to the axes.
plt.legend()  # Add a legend.
plt.show()



#print(len(grid))