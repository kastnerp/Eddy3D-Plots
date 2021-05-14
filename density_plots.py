from epw import epw
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

dims = (8, 2)

colors = ["black", "black", "black"]
linestyles = [":", "--", "-"]

climas = [r"C:\Users\pkastner\Desktop\Weather\Weather\USA_NY_Syracuse-Hancock.Intl.AP.725190_TMY3.epw",
          r"C:\ProgramData\Solemma\Common\WeatherData\EPW\USA_AZ_Phoenix-Sky.Harbor.Intl.AP.722780_TMY3.epw",
          r"C:\Users\pkastner\Desktop\Weather\Weather\NZL_Wellington.Wellington.934360_IWEC.epw",
          ]

var = "Wind Speed"

fig, ax = plt.subplots(figsize=dims)
a = epw()

for i, x in enumerate(climas):
    a.read(x)
    df = a.dataframe

    ws = df[var]

    sns.distplot(ws, hist=False, kde=True,
                 kde_kws={'shade': True},
                 label=a.headers['LOCATION'][0], ax=ax, color=colors[i])
    ax.lines[i].set_linestyle(linestyles[i])

ax.set(xlim=(0, 17), ylim=(0, 0.35))
ax.set(xlabel=var, ylabel='Density')

# Put the legend out of the figure
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.tight_layout()

# plt.text(0.5, 0.5, 'matplotlib', horizontalalignment='center',   verticalalignment='center', transform=ax.transAxes)
plt.savefig("Wind_Speed_Density_Plot.pdf")
plt.savefig("Wind_Speed_Density_Plot.png", dpi=600)
plt.show()

var = "Dry Bulb Temperature"

fig, ax = plt.subplots(figsize=dims)
a = epw()

for i, x in enumerate(climas):
    a = epw()
    a.read(x)
    df = a.dataframe

    ws = df[var]

    sns.distplot(ws, hist=False, kde=True,
                 kde_kws={'shade': True},
                 label=a.headers['LOCATION'][0], ax=ax, color=colors[i])
    ax.lines[i].set_linestyle(linestyles[i])

ax.set(xlim=(-20, 45))
ax.set(xlabel=var, ylabel='Density')

# Put the legend out of the figure
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.tight_layout()

# plt.text(0.5, 0.5, 'matplotlib', horizontalalignment='center',   verticalalignment='center', transform=ax.transAxes)
plt.savefig("Ambient_Temp_Density_Plot.pdf")
plt.savefig("Ambient_Temp_Density_Plot.png", dpi=600)
plt.show()

var = "Relative Humidity"

fig, ax = plt.subplots(figsize=dims)
a = epw()

for i, x in enumerate(climas):
    a = epw()
    a.read(x)
    df = a.dataframe

    ws = df[var]

    sns.distplot(ws, hist=False, kde=True,
                 kde_kws={'shade': True},
                 label=a.headers['LOCATION'][0], ax=ax, color=colors[i])
    ax.lines[i].set_linestyle(linestyles[i])

ax.set(xlim=(5, 95))
ax.set(xlabel=var, ylabel='Density')
# Put the legend out of the figure
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.tight_layout()

# plt.text(0.5, 0.5, 'matplotlib', horizontalalignment='center',   verticalalignment='center', transform=ax.transAxes)
plt.savefig("Relative_Humidity_Density_Plot.pdf")
plt.savefig("Relative_Humidity_Density_Plot.png", dpi=600)
plt.show()

### Percentiles

vars = ["Dry Bulb Temperature", "Wind Speed",

        "Relative Humidity"]

for i, x in enumerate(climas):
    for j, y in enumerate(vars):
        a = epw()
        a.read(x)
        df = a.dataframe

        d = np.array(df[vars[j]])
        p8 = np.percentile(d, 90)
        p2 = np.percentile(d, 10)
        print(a.headers['LOCATION'][0], str(vars[j]), p2, p8)
