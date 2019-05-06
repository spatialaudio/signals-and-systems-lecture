"""Animations of common operations in signal processing."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.collections import LineCollection, PolyCollection
import sympy as sym


def animate_convolution(x, h, y, t, tau, td, taud, interval=75):
    """Plot animation of graphical representation of linear convolution.

    Parameters
    ----------
    x : sympy function
        First function to be convolved.
    h: sympy function
        Second function to be convolved.
    t: sympy variable
        Independent variable for functions (e.g. time).
    tau: sympy variable
        Integration variable for convolution.
    td: array like
        Discrete values of independent variable evaluated for plot.
    taud:
        Discrete values of integration variable evaluated for animation.
    interval:
        Interval in ms between frames of animation.
    Returns
    -------
    matplotlib.animation.FuncAnimation object.

    """
    def animate(ti):
        p = sym.plot(x.subs(t, tau), (tau, taud[0], taud[-1]), show=False)
        line_x.set_segments(p[0].get_segments())

        p = sym.plot(h.subs(t, t - tau).subs(t, ti), (tau, taud[0], taud[-1]),
                     show=False)
        line_h.set_segments(p[0].get_segments())

        p = sym.plot(y, (t, taud[0], taud[-1]), show=False)
        line_y.set_segments(p[0].get_segments())

        p = sym.plot(x.subs(t, tau)*h.subs(t, ti - tau), (tau, -5, 5),
                     show=False)
        points = p[0].get_points()
        verts = [[(xi[0], xi[1]) for xi in np.transpose(np.array(points))]]
        fill.set_verts(verts)

        dot.set_data(ti, y.subs(t, ti))

    # setup plot and line/fill styles
    fig, ax = plt.subplots(2, 1)
    fig.subplots_adjust(hspace=0.5)
    plt.close()  # suppresses empty plot in notebook

    fill = PolyCollection([], facecolors='r')
    fill.set_alpha(0.3)
    ax[0].add_collection(fill)

    line_x = LineCollection([], colors='C0')
    line_x.set_label(r'$x(\tau)$')
    ax[0].add_collection(line_x)

    line_h = LineCollection([], colors='C1')
    line_h.set_label(r'$h(t - \tau)$')
    ax[0].add_collection(line_h)

    line_y = LineCollection([], colors='C2')
    line_y.set_label(r'$y(t)$')
    ax[1].add_collection(line_y)

    dot, = ax[1].plot([], 'ro')

    ax[0].set_xlim((-2, 5))
    ax[0].set_ylim((-.1, 1.2))
    ax[0].set_xlabel(r'$\tau$')
    ax[0].legend(loc='upper right')
    ax[0].grid(True)

    ax[1].set_xlim((-2, 5))
    ax[1].set_ylim((-.1, 1.2))
    ax[1].set_xlabel(r'$t$')
    ax[1].legend(loc='upper right')
    ax[1].grid(True)

    return FuncAnimation(fig, animate, td, interval=interval)
