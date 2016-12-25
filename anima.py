import matplotlib
matplotlib.use('Agg')

import csv
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from trajectory import *
from planet import *

def generateAnimation(planets_local):
    patchs = []

    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)

    for i in range(len(planets_local)):
        patchs.insert(len(patchs), plt.Circle((0, 1), 0.1, fc='y'))

    fig = plt.figure("Anima")
    fig.set_dpi(100)
    fig.set_size_inches(7, 6.5)

    ax = plt.axes(xlim=(-40, 30), ylim=(-40, 40))

    def init():
        for i in range(len(planets_local)):
            tr = planets_local[i].trajectoryBessel(100)
            ax.plot(tr[0],tr[1], label=planets_local[i].getName())
            plt.legend()
        for i in range(len(patchs)):
            ax.add_patch(patchs[i])
        return ax,

    def animate(i):
        for k in range(len(patchs)):
            x, y = patchs[k].center
            x = planets_local[k].positionBessel(20*i)[0]
            y = planets_local[k].positionBessel(20*i)[1]
            patchs[k].center = (x, y)

        return ax,

    anim = animation.FuncAnimation(fig, animate,
                                   init_func=init,
                                   frames=500,
                                   interval=100,
                                   blit=False)

    #plt.show()
    anim.save("anim.mp4", writer = writer)
    plt.close()
