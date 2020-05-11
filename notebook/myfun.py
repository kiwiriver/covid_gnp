def plot_q(ax, qextv,  wv, dv, yscale='log',xlabel="Wavelength(nm)", ylabel='', figsize=(4,4)):
    nd=len(dv)
    nwv=len(wv)
    num_plots=len(dv)
    colormap = plt.cm.gist_ncar
    plt.gca().set_prop_cycle(plt.cycler('color', plt.cm.jet(np.linspace(0, 1, num_plots))))

    ax.set_yscale(yscale)
    for j in range(nd):
        tmp=plt.plot(wv,qextv[:,j], label=dv[j])

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    