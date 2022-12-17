import numpy as np
import matplotlib.pyplot as plt

def pz_plot(z,p,title):
    n_pts = 10000
    plt_lim = np.max([np.max(np.absolute(p)),np.max(np.absolute(z))]) + 0.5
    p_x = [np.real(pole) for pole in p]
    p_y = [np.imag(pole) for pole in p]
    z_x = [np.real(zero) for zero in z]
    z_y = [np.imag(zero) for zero in z]
    plt.figure(figsize = [6,6])
    plt.title(title)
    plt.plot([np.cos(((2.*np.pi)/n_pts)*n) for n in range(n_pts)],
             [np.sin(((2.*np.pi)/n_pts)*n) for n in range(n_pts)],
             linestyle = '--',label='Unit Circle')
    plt.scatter(p_x,p_y,marker='x',color='red',label='Poles')
    plt.scatter(z_x,z_y,marker='o',color='green',label='Zeros')
    plt.xlim([-plt_lim,plt_lim])
    plt.ylim([-plt_lim,plt_lim])
    plt.xlabel('Re{$z$}')
    plt.ylabel('Im{$z$}')
    plt.grid(color='black',linestyle='--',alpha = 0.25)
    plt.legend()
