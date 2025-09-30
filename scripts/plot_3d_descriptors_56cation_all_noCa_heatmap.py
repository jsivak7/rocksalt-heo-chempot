import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.colors as mcolors
import numpy as np
import pandas as pd
import seaborn as sns

plt.rcParams["figure.dpi"] = 400
plt.rcParams["figure.figsize"] = (4, 4)
plt.rcParams["font.size"] = 10
plt.rcParams["font.serif"] = "Helvetica"
plt.rcParams["axes.linewidth"] = 1.65
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
plt.rcParams["xtick.major.width"] = 1.65
plt.rcParams["ytick.major.width"] = 1.65

data = pd.read_csv("../data/descriptors-56cation-ALL-noCa.csv")
data_sorted = data.sort_values(by="chempot overlap (eV)", ascending=False)
print(data_sorted)

colormap = sns.diverging_palette(
    12,
    255,
    as_cmap=True,
)  # sns.color_palette("vlag_r", as_cmap=True)  # coolwarm_r

# label data
x = data_sorted["AO mixing energy (eV/atom)"] * 1000
y = data_sorted["stddev bonds (Angstroms)"]
z = data_sorted["chempot overlap (eV)"]

# Create scatter plot
plt.scatter(
    x,
    y,
    marker="o",
    s=150,
    alpha=0.85,
    c=z,
    cmap=colormap,
    norm=mcolors.TwoSlopeNorm(
        vcenter=0,
        vmin=-1.1,
        vmax=1.1,
    ),
    edgecolors="k",
)

# Set labels for the axes
plt.xlabel(r"ΔH$\bf{_{mix}}$ (meV/atom)", weight="bold")
plt.ylabel(r"σ$\bf_{bonds}$ (Å)", weight="bold")

# set tick marks
plt.xticks(weight="bold")
plt.yticks(weight="bold")

# set axis limits
plt.xlim(47, 93)
plt.ylim(0.015, 0.145)

# plt.colorbar(label=r"μ$_{\rm overlap}$ (eV)", ticks=[-1.0, -0.5, 0, 0.5, 1.0])

# Show the plot
plt.show()
