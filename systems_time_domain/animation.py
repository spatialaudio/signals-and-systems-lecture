import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sympy as sym


def animate_convolution(x, h, y, t, tau, td, taud):
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

    Returns
    -------
    matplotlib.animation.FuncAnimation object

    """

    def heaviside(x):
        return np.heaviside(x, .5)

    def animate(ti):
        ax[0].collections.clear()
        ax[0].fill_between(taud, 0, h_eval(ti, taud)*x_eval(taud), facecolor='red', alpha=0.3)

        lines[0].set_data(taud, h_eval(ti, taud))
        lines[1].set_data(taud, x_eval(taud))

        lines[2].set_data(taud, y_eval(taud))
        lines[3].set_data(ti, y_eval(ti))

        return lines

    # add numerical evaluation to symbolic functions
    x_eval = sym.lambdify((tau), x.subs(t, tau), modules=['numpy', {'Heaviside': heaviside}])
    h_eval = sym.lambdify((t, tau), h.subs(t, t - tau), modules=['numpy', {'Heaviside': heaviside}])
    y_eval = sym.lambdify((t), y, modules=['numpy', {'Heaviside': heaviside}])

    # setup plot and line styles
    fig, ax = plt.subplots(2, 1)
    fig.subplots_adjust(hspace=0.5)
    plt.close()  # suppresses empty plot in notebook

    lines = [ax[0].plot([], [], label=r'$h(t-\tau)$')[0]]
    lines.append(ax[0].plot([], [], label=r'$x(\tau)$')[0])
    lines.append(ax[1].plot([], [], 'g-', label=r'$y(t) = x(t) * h(t)$')[0])
    lines.append(ax[1].plot([], [], 'ro')[0])

    ax[0].set_xlim((-3, 5))
    ax[0].set_ylim((-.1, 1.2))
    ax[0].set_xlabel(r'$\tau$')
    ax[0].legend(loc='upper right')
    ax[0].grid(True)

    ax[1].set_xlim((-3, 5))
    ax[1].set_ylim((-.1, 1.2))
    ax[1].set_xlabel(r'$t$')
    ax[1].legend(loc='upper right')
    ax[1].grid(True)

    return animation.FuncAnimation(fig, animate, td, interval=50, blit=True)
