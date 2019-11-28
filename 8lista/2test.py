import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def update(i, ln):
    i = i+1
    x = i
    y = i ** 2
    x_data = ln.get_xdata()
    y_data = ln.get_ydata()
    ln.set_data(np.concatenate(([x], x_data)),
                np.concatenate(([y], y_data)))
    return ln


if __name__ == "__main__":
    fig, ax = plt.subplots()
    ax.set_xlim(1, 10)
    ax.set_ylim(1, 100)
    line, = ax.loglog([1], [1])
    anim = FuncAnimation(fig, update, frames=np.arange(0, 10), interval=200,
                         fargs=(line, ))
    anim.save('Test.gif', dpi=80, writer='imagemagick')