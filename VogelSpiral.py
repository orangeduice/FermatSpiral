# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 17:02:17 2024

@author: okcj1g19
"""

import numpy as np
import math
import matplotlib.pyplot as plt


alpha = 137.508*(np.pi/180)
a = 1
N = 1000

r = []
theta = [] 


for n in range(0,N):
    r.append(a*np.sqrt(n))
    theta.append(n*alpha)


fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r)