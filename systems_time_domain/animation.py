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
    def my_heaviside(x):
        return np.heaviside(x,1/2)
    
    def animate(ti):
        p = sym.plot(x.subs(t, tau), (tau, taud[0], taud[-1]), show=False)
        line_x.set_segments(p[0].get_segments())

        p = sym.plot(h.subs(t, t - tau).subs(t, ti), (tau, taud[0], taud[-1]),
                     show=False)
        line_h.set_segments(p[0].get_segments())

        p = sym.plot(y, (t, taud[0], taud[-1]), show=False)
        line_y.set_segments(p[0].get_segments())

        p = sym.plot(x.subs(t, tau) * h.subs(t, ti - tau), (tau, -5, 5),
                     show=False)
        
        # see https://github.com/sympy/sympy/issues/21392
        #points = np.array(p[0].get_points())
        # alternative via lambdify
        func = sym.lambdify(tau, x.subs(t, tau) * h.subs(t, ti - tau), modules=['numpy', {'Heaviside':my_heaviside}])
        tt = np.linspace(-5,5,100)
        points = np.vstack((tt, np.asarray(func(tt))))
        
        verts = [[(xi[0], xi[1]) for xi in points.T]]
        fill.set_verts(verts)
        
        dot.set_data(ti, y.subs(t, ti))

    
    # define line/fill collections and setup plot
    default_figsize = plt.rcParams.get('figure.figsize')
    fig, ax = plt.subplots(2, 1, figsize=(default_figsize[0],
                                          1.5*default_figsize[1]))
    fig.subplots_adjust(hspace=0.2)
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

    for axi in ax:
        axi.spines['left'].set_position('zero')
        axi.spines['bottom'].set_position('zero')
        axi.spines['right'].set_color('none')
        axi.spines['top'].set_color('none')
        axi.xaxis.set_ticks_position('bottom')
        axi.yaxis.set_ticks_position('left')
        axi.set_xlim((-3, 4))
        axi.set_ylim((-.1, 1.2))

    ax[0].set_xlabel(r'$\tau$', horizontalalignment='right', x=1.0)
    ax[0].legend(loc='upper right')
    ax[1].set_xlabel(r'$t$', horizontalalignment='right', x=1.0)
    ax[1].legend(loc='upper right')

    return FuncAnimation(fig, animate, td, interval=interval)
