import numpy as np
import PyMieScatt as ps

def run_mie(nv, kv, wv, dv):
    nd=len(dv)
    nwv=len(wv)
    
    #run the mie code for above parameters
    miev=np.array([[ps.MieQ(nv[i]+kv[i]*1.0j,wv[i],dv[j],asDict=True) \
                    for j in range(nd)] \
                   for i in range(nwv)])

    qextv=np.array([[miev[i,j]['Qext'] for j in range(nd)]for i in range(nwv)])
    qscav=np.array([[miev[i,j]['Qsca'] for j in range(nd)]for i in range(nwv)])
    qabsv=np.array([[miev[i,j]['Qabs'] for j in range(nd)]for i in range(nwv)])
    qbackv=np.array([[miev[i,j]['Qback'] for j in range(nd)]for i in range(nwv)])
    gv=np.array([[miev[i,j]['g'] for j in range(nd)]for i in range(nwv)])

    return [qextv,qscav, qabsv, qbackv,gv]

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
    