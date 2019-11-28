import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = plt.axes(xlim = (-2,2), ylim = (-2, 2))
xdata, ydata = [], []
line, = ax.plot([], [])

x = [1.5,1.5,1,1,1.5]
y = [1,1.5,1.5,1,1]
ax1 = fig.add_subplot(111, sharex=ax, sharey=ax)
# ax1 = plt.axes(xlim = (-2,2), ylim = (-2, 2))
ax1.plot(x, y)

def init():
    line.set_data([],[])
    return line,

def animate(i):
    t = 0.01*i
    a = 1
    b = 1
    x = np.sin(a * t + np.pi / 2.0)
    y = np.sin(b*t)
    xdata.append(x)
    ydata.append(y)
    line.set_data(xdata, ydata)
    return line,

ani =  FuncAnimation(\
    fig, animate, init_func=init, frames=500, interval=50, blit=True)
plt.show()