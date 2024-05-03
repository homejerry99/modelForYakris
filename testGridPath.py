import random
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
shipGridCruiser = [[8,8],[8,9]]
shipGridCarrier = [[2,0],[3,0],[4,0],[5,0],[6,0]]

nList = []
grid = []
pointerSeq = []
for i in range(10):
    for j in range(10):
        grid.append([i,j])
k = 0
n = 0
while k < len(shipGridCarrier) + len(shipGridCruiser):
    pointer = random.sample(grid,1)[0]
    #print(pointer)
    if pointer in shipGridCarrier or pointer in shipGridCruiser:
        k = k + 1
    grid.remove(pointer)
    pointerSeq.append(pointer)
    n = n + 1
nList.append(n)
    

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
plt.show()'''





'''
k = 0
n = 0
while k < len(shipGridCarrier) + len(shipGridCruiser):
    pointer = random.sample(grid,1)[0]
    #print(pointer)
    if pointer in shipGridCarrier or pointer in shipGridCruiser:
        k = k + 1
    grid.remove(pointer)
    n = n + 1
print(n)
'''


#print(len(grid))