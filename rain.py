"""
===============
Rain simulation
===============

Simulates rain drops on a surface by animating the scale and opacity
of 50 scatter points.

Author: Nicolas P. Rougier
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Fixing random state
np.random.seed(19680801)

# Create ne Figure and an Axes which fills it
fig = plt.gifure(figsize = (7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon = False)
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])