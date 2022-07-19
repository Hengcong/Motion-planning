# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 11:54:27 2022

@author: ghc19
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import random
import copy
from matplotlib import colors

def sub2coord(possub):
    posx = possub[1]
    posy = possub[0]
    return [posx, posy]
    
def coord2sub(posxy):
    posr = posxy[1]
    posc = posxy[0]
    return [posr, posc]

def xy2sub(sz, x, y):
     r = sz[0] -1 -y
     c = x
     return [r, c]
 
def sub2xy(sz, r, c):
    x = c
    y = sz[0] -1 -r
    return [x, y]

# 

def sub2ind(sz, r, c):
    ind = c*sz[0] + r
    return ind

def ind2sub(sz, ind):
    c = int(ind/sz[0])
    r = ind - c* sz[0]
    return [r, c]

def DrawHeatMap(field):
    rows = len(field)
    cols = len(field[0])
    cmap = colors.ListedColormap(['none','white', 'black', 'red', 'yellow', 'magenta',
                                  'green', 'cyan', 'blue'])
    
    plt.figure(figsize=(12, 8))
    ax = plt.gca()
    
    
    ax = sns.heatmap(field, cmap=cmap, vmin=0, vmax = 8, linewidths =0.8,
                     linecolor ='black', ax =ax, cbar = False)
    
    ax.set_ylabel('rows')
    ax.set_xlabel('cols')
    
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top')
    
    
    ax.set_xticks(np.arange(cols))
    ax.set_yticks(np.arange(rows))
    
    
    