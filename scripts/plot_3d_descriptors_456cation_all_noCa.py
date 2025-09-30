import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd

plt.rcParams["figure.dpi"] = 500
plt.rcParams["figure.figsize"] = (3.5, 3)
plt.rcParams["font.size"] = 8

# might should change this such that we have three datasets for the different colors
# that we want to plot for varying compositions that we are and aren't able to make...
data = pd.read_csv("../data/descriptors-456cation-ALL-noCa.csv")
data_sorted = data.sort_values(by="chempot overlap (eV)", ascending=False)
print(data_sorted)

# label data
x = data_sorted["chempot overlap (eV)"]
y = data_sorted["AO mixing energy (eV/atom)"] * 1000
z = data_sorted["stddev bonds (Angstroms)"]

color_j14 = "g"
color_MnFe = "b"
color_MnFeCu = "r"

# Create figure and axes object
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Create scatter plot
ax.scatter(
    x,
    y,
    z,
    marker="o",
    s=20,
    color=[
        color_j14,
        color_j14,
        color_j14,
        color_j14,
        color_j14,
        color_j14,
        color_j14,
        color_j14,
        color_MnFe,
        color_MnFe,
        color_MnFe,
        color_MnFe,
        color_MnFe,
        color_MnFe,
        color_MnFe,
        color_MnFe,
        color_MnFe,
        color_MnFe,
        color_MnFe,
        color_MnFe,
        color_MnFe,
        color_MnFe,
        color_MnFe,
        color_MnFe,
        color_MnFe,
        color_MnFe,
        color_MnFe,
        color_MnFeCu,
        color_MnFeCu,
        color_MnFeCu,
        color_MnFeCu,
        color_MnFeCu,
        color_MnFeCu,
        color_MnFeCu,
        color_MnFeCu,
        color_MnFeCu,
        color_MnFeCu,
        color_MnFeCu,
        color_MnFeCu,
        color_MnFeCu,
        color_MnFeCu,
        color_MnFeCu,
        color_MnFeCu,
        color_MnFeCu,
        color_MnFeCu,
        color_MnFeCu,
        color_MnFeCu,
        color_MnFeCu,
        color_MnFeCu,
        color_MnFeCu,
        color_MnFeCu,
        color_MnFeCu,
        color_MnFeCu,
        color_MnFeCu,
        color_MnFeCu,
        color_MnFeCu,
        color_MnFeCu,
        color_MnFeCu,
        color_MnFeCu,
        color_MnFeCu,
        color_MnFeCu,
        color_MnFeCu,
        color_MnFeCu,
    ],
)

z2 = (
    np.ones(shape=x.shape) * -0.90
)  # * min(x) # have this value match the axes lower limit for wherever the "h" is below

# lines that go to markers
for i, j, k, h in zip(x, y, z, z2):
    print(i, j, k, h)
    if i > 0:
        color = color_j14
    elif i > -0.2:
        color = color_MnFe
    else:
        color = color_MnFeCu
    ax.plot(
        [i, h], [j, j], [k, k], color=color, linewidth=1.5
    )  # change which axes the lines are coming from here with "h"


# Set labels for the axes
ax.set_xlabel(r"μ$_{\rm overlap}$ (eV)")
ax.set_ylabel(r"ΔH$_{\rm mix}$ (meV/atom)")
ax.set_zlabel(r"σ$_{\rm bonds}$ (Å)")

# ax.tick_params(axis="both", which="major", pad=0.005) # tried to move axis ticks and labels closer but eh

# set tick marks
ax.set_xticks([-0.6, 0.0, 0.6, 1.2])
ax.set_yticks([50, 60, 70, 80, 90, 100])
ax.set_zticks([0.03, 0.06, 0.09, 0.12, 0.15])

# set axis limits
ax.set_xlim(-0.90, 1.65)
ax.set_ylim(45, 95)
ax.set_zlim(0.005, 0.16)

# Change grid line spacing
ax.xaxis._axinfo["grid"]["linewidth"] = 0.1
ax.yaxis._axinfo["grid"]["linewidth"] = 0.1
ax.zaxis._axinfo["grid"]["linewidth"] = 0.1
ax.xaxis.pane.set_color("w")
ax.yaxis.pane.set_color("w")
ax.zaxis.pane.set_color("w")

# Show the plot
plt.savefig("../../../Desktop/3Ddescriptors_456cation_all_noCa.png")
plt.show()
