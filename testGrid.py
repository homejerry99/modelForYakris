import random
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

from matplotlib.font_manager import FontManager
import subprocess

'''mpl_fonts = set(f.name for f in FontManager().ttflist)

print('all font list get from matplotlib.font_manager:')
for f in sorted(mpl_fonts):
    print('\t' + f)'''

mpl.rc("font",family='STFangsong')

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
    while k < len(shipGridCarrier) + len(shipGridCruiser):
        pointer = random.sample(grid,1)[0]
        #print(pointer)
        if pointer in shipGridCarrier or pointer in shipGridCruiser:
            k = k + 1
        grid.remove(pointer)
        n = n + 1
    nList.append(n)
  
fig, ax = plt.subplots()
x = range(1000)
ax.plot(x,[np.average(nList)] * 1000, color = 'red', label = '击沉全部舰船所需平均射击次数')
ax.grid()
ax.scatter(x,nList)
plt.xlabel('试验次数')  # Add an x-label to the axes.
plt.ylabel('试验完成时的射击次数')  # Add a y-label to the axes.
plt.title('无策略下重复试验结果')  # Add a title to the axes.
plt.legend()  # Add a legend.
plt.show()





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