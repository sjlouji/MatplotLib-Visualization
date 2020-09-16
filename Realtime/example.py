import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = []
y = []

index = count()

def animate(i):
    x.append(next(index))
    y.append(random.randint(0,5))
    plt.plot(x,y)
ani  = FuncAnimation(plt.gcf(), animate, interval = 1000)

plt.plot(x,y)

plt.show()