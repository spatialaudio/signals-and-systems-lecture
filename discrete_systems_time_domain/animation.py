"""Animations of common operations in signal processing."""
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def animate_discrete_convolution(x, h, y, k, kappa, interval=100):

    def update_stem(stem, x, y):
        stem.markerline.set_data(x, y)
        for idx, stem_line in enumerate(stem.stemlines):
            stem_line.set_data([x[idx], x[idx]], [0, y[idx]])

    def animate(kappa_i):
        update_stem(stem_x, k, x(k))
        update_stem(stem_h, k, h(kappa_i - k))
        dot.set_data(kappa_i, y[-k[0] + kappa_i])

    # setup plot and define objects
    default_figsize = plt.rcParams.get('figure.figsize')
    fig, ax = plt.subplots(2, 1, figsize=(default_figsize[0],
                                          1.5*default_figsize[1]))
    fig.subplots_adjust(hspace=0.2)
    plt.close()  # suppresses empty plot in notebook

    stem_x = ax[0].stem(k, x(k), linefmt='C0-', markerfmt='C0o',
                        basefmt=' ', label=r'$x[\kappa]$')
    stem_h = ax[0].stem(k, h(kappa[0]-k), linefmt='C1-',
                        markerfmt='C1o', basefmt=' ', label=r'$h(k - \kappa)$')
    ax[0].set_xlabel(r'$\kappa$')
    ax[0].legend(loc='upper right')
    ax[0].grid()

    y = y(k)
    ax[1].stem(k, y, linefmt='C2-', markerfmt='C2o', basefmt=' ',
               label=r'$y[k]$')
    dot, = ax[1].plot([], 'ro')
    ax[1].set_xlabel(r'$k$')
    ax[1].legend(loc='upper right')
    ax[1].grid()

    return FuncAnimation(fig, animate, kappa, interval=interval)
