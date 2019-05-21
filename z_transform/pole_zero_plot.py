import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle
from matplotlib.patches import Circle


def pole_zero_plot(p, z):
    
    fig = plt.figure(figsize=(5,5))
    ax = fig.gca()
    
    for pole in p:
        plt.plot(complex(pole).real, complex(pole).imag, 'rx', markersize=10)
    for zero in z:
        plt.plot(complex(zero).real, complex(zero).imag, 'bo', markersize=10, fillstyle='none')

    unit_circle = Circle((0,0), radius=1, fill=False,
                         color='black', ls='solid', alpha=0.7)
    ax.add_patch(unit_circle)
    ax.axvline(0, color='0.7')
    ax.axhline(0, color='0.7')
    
    plt.axis('equal')
    plt.xlim((-2, 2))
    plt.ylim((-2, 2))
    plt.grid()
    plt.title('Poles and Zeros')
    plt.xlabel(r'Re{$z$}')
    plt.ylabel(r'Im{$z$}')
