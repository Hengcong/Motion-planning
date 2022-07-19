# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 15:01:09 2022

@author: ghc19
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import colors


def sub2coord(possub):
    posx = possub[1]
    posy = possub[0]
    return [posx, posy]

def coord2sub(posxy):
    posr = posxy[1]
    posc = posxy[0]
    return [posr, posc]

def drawmap(rows, cols, startSub, goalSub, obsSub):
    field = np.ones((rows, cols))
     
    field[startSub[0], startSub[1]] = 4
    field[goalSub[0], goalSub[1]] = 5
     
    for i in range (len(obsSub)):
        field[obsSub[i][0], obsSub[i][1]] = 2
         
         
    cmap = colors.ListedColormap(['none','white', 'black', 'red', 'yellow', 'magenta',
                                  'green', 'cyan', 'blue'])
    
    
    plt.figure(figsize=(cols,rows))
    ax = plt.gca()
    
    sns.heatmap(field, cmap = cmap,vmin = 0,vmax = 8, linewidths = 1.25, 
                linecolor= 'black', ax = ax, cbar = False)
    
    ax.set_ylabel('rows')
    ax.set_xlabel('cols')
    
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top')
    
    ax.set_xticks(np.arange(cols))
    ax.set_yticks(np.arange(rows))
    
    return field

rows = 4
cols = 5

startSub = [2,0]
goalSub = [2,4]
obsSub = [[1,2],[2,2],[3,2]]

drawmap(rows,cols,startSub,goalSub,obsSub)


pointxy = [2,3]
plt.scatter(pointxy[0],pointxy[1],s = 200,c = 'r')
pointsub = coord2sub(pointxy)
plt.scatter(pointsub[0],pointsub[1],s = 200,c = 'y')
plt.show()