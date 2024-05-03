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
def generate(gridForGen):
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
        shipGrid = generate(gridForGen)
    else:
        shipGrid = random.sample(undefinedPos,1)[0]
    return shipGrid

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

'''
给定船只直接抵线放置
'''


nList = []
for t in range(1000):     
    #生成用的网格和实际操作用的网格
    gridForGen = []
    for i in range(10):
        for j in range(10):
            gridForGen.append([i,j])
    grid = gridForGen.copy()

    #生成舰船
    shipGrid00 = [[9,0],[9,1],[9,2],[9,3],[9,4]]
    occ00 = getOccupiedGrids(shipGrid00,gridForGen)
    remainGrid = removeOccupiedGrids(occ00,gridForGen)
    shipGrid01 = [[7,0],[7,1],[7,2],[7,3]]
    occ01 = getOccupiedGrids(shipGrid01,gridForGen)
    remainGrid = removeOccupiedGrids(occ01,gridForGen)
    shipGrid02 = [[5,0],[5,1],[5,2]]
    occ02 = getOccupiedGrids(shipGrid02,gridForGen)
    remainGrid = removeOccupiedGrids(occ02,gridForGen)
    shipGrid03 = [[3,0],[3,1],[3,2]]
    occ03 = getOccupiedGrids(shipGrid03,gridForGen)
    remainGrid = removeOccupiedGrids(occ03,gridForGen)
    shipGrid04 = [[0,0],[0,1]]
    occ04 = getOccupiedGrids(shipGrid04,gridForGen)
    remainGrid = removeOccupiedGrids(occ04,gridForGen)
    #print(shipGridCruiser)
    #print(shipGrid)
    k = 0
    n = 0
    pointer = []
    pointerSeq = []
    trackingPoint = []
    trackingDirPoint = []
    targetGrid = []
    targetGrid = unionForList(targetGrid,shipGrid00)
    targetGrid = unionForList(targetGrid,shipGrid01)
    targetGrid = unionForList(targetGrid,shipGrid02)
    targetGrid = unionForList(targetGrid,shipGrid03)
    targetGrid = unionForList(targetGrid,shipGrid04)
    ship00Alive = True
    ship01Alive = True
    ship02Alive = True
    ship03Alive = True
    ship04Alive = True
    while k < len(targetGrid):
        dirConfirm = False
        #搜索目标
        #首先检验是否有已经被击沉的舰船，并排除周边格点
        if ship00Alive:
            hit00 = 0 
            for hull in shipGrid00:
                if hull not in grid:
                    hit00 = hit00 + 1
            if hit00 >= len(shipGrid00):
                ship00Alive = False
                removeOccupiedGrids(occ00,grid)
        if ship01Alive:
            hit01 = 0 
            for hull in shipGrid01:
                if hull not in grid:
                    hit01 = hit01 + 1
            if hit01 >= len(shipGrid01):
                ship01Alive = False
                removeOccupiedGrids(occ01,grid)
        if ship02Alive:
            hit02 = 0 
            for hull in shipGrid02:
                if hull not in grid:
                    hit02 = hit02 + 1
            if hit02 >= len(shipGrid02):
                ship02Alive = False
                removeOccupiedGrids(occ02,grid)
        if ship03Alive:
            hit03 = 0 
            for hull in shipGrid03:
                if hull not in grid:
                    hit03 = hit03 + 1
            if hit03 >= len(shipGrid03):
                ship03Alive = False
                removeOccupiedGrids(occ03,grid)
        if ship04Alive:
            hit04 = 0 
            for hull in shipGrid04:
                if hull not in grid:
                    hit03 = hit03 + 1
            if hit04 >= len(shipGrid04):
                ship04Alive = False
                removeOccupiedGrids(occ04,grid)
                
                
        #用于确认方向
        if n > 2: 
            dirConfirm = (trackingDirPoint in targetGrid)
            
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
        if (pointer in targetGrid):
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
plt.title('抵线放置时策略3下重复试验结果')  # Add a title to the axes.
plt.legend()  # Add a legend.
plt.show()



#print(len(grid))