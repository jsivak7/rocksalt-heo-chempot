import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd

plt.rcParams["figure.dpi"] = 300
plt.rcParams["figure.figsize"] = (3.5, 3)
plt.rcParams["font.size"] = 8

# might should change this such that we have three datasets for the different colors
# that we want to plot for varying compositions that we are and aren't able to make...
data = pd.read_csv("../data/descriptors-56cation-ALL-noCa.csv")
data_sorted = data.sort_values(by="chempot overlap (eV)", ascending=False)
print(data_sorted)

# label data
x = data_sorted["AO mixing energy (eV/atom)"] * 1000
y = data_sorted["chempot overlap (eV)"]
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
    ],
)

z2 = (
    np.ones(shape=x.shape) * -0.90
)  # * min(x) # have this value match the axes lower limit for wherever the "h" is below

# lines that go to markers
for i, j, k, h in zip(x, y, z, z2):
    if j > 0:
        color = color_j14
    elif j > -0.2:
        color = color_MnFe
    else:
        color = color_MnFeCu
    ax.plot(
        [i, i], [j, h], [k, k], color=color, linewidth=1.5
    )  # change which axes the lines are coming from here with "h"

# Set labels for the axes
ax.set_xlabel(r"ΔH$_{\rm mix}$ (meV/atom)")
ax.set_ylabel(r"μ$_{\rm overlap}$ (eV)")
ax.zaxis.set_rotate_label(False)
ax.set_zlabel(r"σ$_{\rm bonds}$ (Å)", rotation=90)

# ax.tick_params(axis="both", which="major", pad=0.005) # tried to move axis ticks and labels closer but eh

# set tick marks
ax.set_xticks([50, 60, 70, 80, 90, 100])
ax.set_yticks([-0.8, -0.4, 0.00, 0.4])
ax.set_zticks([0.03, 0.06, 0.09, 0.12, 0.15])

# set axis limits
ax.set_xlim(45, 95)
ax.set_ylim(-0.90, 0.55)
ax.set_zlim(0.005, 0.16)

ax.xaxis.set_inverted(True)

# Change grid line spacing
ax.xaxis._axinfo["grid"]["linewidth"] = 0.1
ax.yaxis._axinfo["grid"]["linewidth"] = 0.1
ax.zaxis._axinfo["grid"]["linewidth"] = 0.1
ax.xaxis.pane.set_color("w")
ax.yaxis.pane.set_color("w")
ax.zaxis.pane.set_color("w")

# attempts at adding text in for compositions
ax.text(
    90,
    -0.7,
    0.08,
    r"Mg$_{\rm 1/5}$Co$_{\rm 1/5}$Ni$_{\rm 1/5}$Cu$_{\rm 1/5}$Zn$_{\rm 1/5}$O",
    "y",
    color="g",
    size=5,
)
ax.text(
    60,
    -0.2,
    0.062,
    r"Mn/Fe",
    "y",
    color="b",
    size=5,
)
ax.text(
    50,
    -0.825,
    0.140,
    r"Mn/Fe + Cu",
    "x",
    color="r",
    size=5,
)

# Show the plot
ax.view_init(15, 50)  # default is (-140, 60)
plt.savefig("../results/3Ddescriptors_56cation_all_noCa_flipped.png")
# plt.show()
