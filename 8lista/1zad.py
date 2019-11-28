import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = plt.axes(xlim = (0,20), ylim = (0, 20))
xdata, ydata = [], []
snake_len = 5
xdata = list(range(5,5+snake_len))
ydata = [10]*snake_len
line, = ax.plot([], [])

def listOfTuples(l1, l2): 
    return list(map(lambda x, y:(x,y), l1, l2)) 

l1 = np.ceil(np.random.rand(20)*19)
l2 = np.ceil(np.random.rand(20)*19)

ax1 = fig.add_subplot(111, sharex=ax, sharey=ax)
snake_food = dict()
for cx, cy in listOfTuples(l1, l2):
    a = 0.5
    x = [cx+a,cx+a,cx-a,cx-a,cx+a]
    y = [cy-a,cy+a,cy+a,cy-a,cy-a]
    ax1.plot(x, y)


def init():
    line.set_data(xdata, ydata)
    return line,

def animate(i):
    dx = xdata[-1] - xdata[-2]
    dy = ydata[-1] - ydata[-2]
    while True:
        rand = np.random.rand()
        if rand < 0.25:
            c = dx
            dx = dy
            dy = c
        if rand > 0.75:
            c = dx
            dx = -dy
            dy = -c
        newx = xdata[-1]+dx
        newy = ydata[-1]+dy
        if (newx, newy) not in listOfTuples(xdata,ydata)\
            and 0 < newx < 20 \
            and 0 < newy < 20 :
            break
    xdata.append(newx)
    ydata.append(newy)
    if (newx, newy) in listOfTuples(l1, l2):
        ani.event_source.stop()
    xdata.pop(0)
    ydata.pop(0)    
    line.set_data(xdata, ydata)
    return line,

ani =  FuncAnimation(
    fig, 
    animate, 
    init_func=init, 
    frames=10, 
    interval=500, 
    blit=True)
plt.show()