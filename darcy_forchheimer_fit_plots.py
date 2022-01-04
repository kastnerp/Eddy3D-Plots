
# py3 only, see below for py2
import numpy as np
import pandas as pd
from io import StringIO
import scipy.optimize as scy
import matplotlib.pyplot as plt
import proplot as pplt

dims = (6, 2.5)




fig, ax = plt.subplots(figsize=dims)


# Robin Red Holly Cut 0 PA
d1 = '''x	    y			
0.00	0.00				
2.41	9.56				
3.65	22.15				
4.63	35.56				
5.22	44.41				
5.71	53.81				
6.25	64.55				
6.98	79.58				
7.30	87.10				'''

Robin_Red_Holly_Cut_0_PA = pd.read_csv(StringIO(d1), sep='\s+')


# Bakers Blue Spruce, Cut 3 (PC)
d2 = '''x	    y			
0.00	0.00				
3.06	2.26				
4.61	6.21				
5.82	9.38				
6.56	12.57				
7.18	15.50				
7.88	17.61				
8.72	22.41				
9.07	24.01				'''

Bakers_Blue_Spruce = pd.read_csv(StringIO(d2), sep='\s+')

# Blue Shag Eastern White Pine, Cut 0 (PA)
d3 = '''x	    y			
0.00	0.00				
1.79	17.40				
2.70	38.35				
3.48	59.85				
3.86	75.44				
4.29	89.42				
4.67	108.25				
5.18	130.03				'''

Blue_Shag_Eastern = pd.read_csv(StringIO(d3), sep='\s+')

#

blueish = (0/255, 127/255, 255/255)
magenta = (247/255, 60/255, 124/255)
teal = (23/255, 142/255, 146/255)

colors = [blueish, magenta, teal]
labels = [
    "Robin Red Holly, Cut 0 (PA)",
    "Blue Shag Eastern White Pine, Cut 0 (PA)",
    "Bakers Blue Spruce, Cut 3 (PC)"
]


data = [Robin_Red_Holly_Cut_0_PA,Blue_Shag_Eastern, Bakers_Blue_Spruce ]

# objective function
def objective(x, a, b, c):
    # 2nd order polynomial
	return a * x**2 + b*x+c

for i, d in enumerate(data):

    print(i, d)

    # fit curve
    popt, _ = scy.curve_fit(objective, d['x'], d['y'])

    xx =  np.linspace(0,10,100)
    yy = [objective(j, popt[0], popt[1], popt[2]) for j in xx]

    plt.plot(xx,yy ,color = colors[i], label= labels[i])
    plt.scatter(d['x'], d['y'], color=colors[i], facecolors='none',)


#

#

ax.set(xlim=(0, 10), ylim=(0, 150))
ax.set(xlabel="U [m/s]", ylabel='$\Delta$P [Pa]')
# Put the legend out of the figure
plt.legend()
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.tight_layout()

# plt.text(0.5, 0.5, 'matplotlib', horizontalalignment='center',   verticalalignment='center', transform=ax.transAxes)
plt.savefig("Darcy_Forchheimer_Fit.pdf")
plt.savefig("Darcy_Forchheimer_Fit.png", dpi=600)
plt.show()




# ProPlot


for i, d in enumerate(data):

    print(i, d)

    # fit curve
    popt, _ = scy.curve_fit(objective, d['x'], d['y'])

    xx =  np.linspace(0,10,100)
    yy = [objective(j, popt[0], popt[1], popt[2]) for j in xx]

    fig = pplt.figure(share=False)
    ax = fig.subplot(title='Alternate y twin x')

    ax.plot(d)
    ax.plot(d)


#

#

ax.set(xlim=(0, 10), ylim=(0, 150))
ax.set(xlabel="U [m/s]", ylabel='$\Delta$P [Pa]')
# Put the legend out of the figure
pplt.legend()
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
pplt.tight_layout()

# plt.text(0.5, 0.5, 'matplotlib', horizontalalignment='center',   verticalalignment='center', transform=ax.transAxes)
pplt.savefig("Darcy_Forchheimer_Fit_pplot.pdf")
pplt.savefig("Darcy_Forchheimer_Fit_pplot.png", dpi=600)
pplt.show()

