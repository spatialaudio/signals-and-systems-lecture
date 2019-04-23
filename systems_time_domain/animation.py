from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import sympy as sym
from sympy.plotting.plot import MatplotlibBackend
import numpy as np


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
    taud: array_like
        Discrete values of integration variable evaluated for animation.
    interval: integer
        Interval in ms between frames.

    Returns
    -------
    matplotlib.animation.FuncAnimation object

    """
    def heaviside(x):
        return np.heaviside(x, .5)

    def animate(ti):
        ax[0].clear()
        ax[0].fill_between(taud, 0, xh_eval(ti, taud), facecolor='red', alpha=0.3)
        p1 = sym.plot(h.subs(t, t - tau).subs(t, ti), (tau, taud[0], taud[-1]), xlabel=r'$\tau$', ylabel=r'$h(t-\tau)$, $x(\tau)$', line_color='C0', show=False)
        p1.append(sym.plot(x.subs(t, tau), (tau, taud[0], taud[-1]), line_color='C1', show=False)[0])
        backend1 = MatplotlibBackend(p1)
        backend1.ax = ax[0]
        backend1.process_series()
        plt.close(backend1.fig)

        ax[1].clear()
        ax[1].plot(ti, y.subs(t, ti), 'ro')
        p2 = sym.plot(y, (t, taud[0], taud[-1]), xlabel=r'$t$', ylabel=r'$y(t)$', line_color='C2', show=False)
        backend2 = MatplotlibBackend(p2)
        backend2.ax = ax[1]
        backend2.process_series()
        plt.close(backend2.fig)

    # add numerical evaluation to symbolic functions
    xh_eval = sym.lambdify((t, tau), x.subs(t, tau) * h.subs(t, t - tau), modules=['numpy', {'Heaviside': heaviside}])

    # setup plot
    fig, ax = plt.subplots(nrows=2)

    for axi in ax:
        axi.spines['top'].set_color('none')
        axi.spines['right'].set_color('none')
        axi.spines['bottom'].set_position('zero')

    plt.close()  # suppress empty plot in notebook

    return FuncAnimation(fig, animate, td, interval=interval)
