# Plots the overlap in oxygen chemical potential between 2 AO phases as a heatmap
# if the value is positive (+), then this is overlap distance
# if the value is negative (-), then this is the distance between

import pandas as pd
import itertools
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

plt.rcParams["figure.figsize"] = (4, 4)
plt.rcParams["figure.dpi"] = 400
plt.rcParams["font.serif"] = "Arial"
plt.rcParams["font.size"] = 8

data = pd.read_csv("../data/chempot-overlap-2cation-GGA_GGA+U.csv")
data = data.set_index("combo")
print(data)

cations = [
    "Mg",
    "Ca",
    "Ti",
    "Mn",
    "Fe",
    "Co",
    "Ni",
    "Cu",
    "Zn",
]  # Mg + Ca + 3d row
# ValueError: No A2+O2- phase was found on the convex hull for Sc-O.
# ValueError: No A2+O2- phase was found on the convex hull for V-O.
# ValueError: No A2+O2- phase was found on the convex hull for Cr-O.

combos = list(
    itertools.combinations(cations, 2)
)  # creates a list of all combinations of cations

label = "overlap (eV)"

chempot_overlaps = np.array(
    [
        [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
        [
            data.loc["MgCa", label],
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
        ],
        [
            data.loc["MgTi", label],
            data.loc["CaTi", label],
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
        ],
        [
            data.loc["MgMn", label],
            data.loc["CaMn", label],
            data.loc["TiMn", label],
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
        ],
        [
            data.loc["MgFe", label],
            data.loc["CaFe", label],
            data.loc["TiFe", label],
            data.loc["MnFe", label],
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
        ],
        [
            data.loc["MgCo", label],
            data.loc["CaCo", label],
            data.loc["TiCo", label],
            data.loc["MnCo", label],
            data.loc["FeCo", label],
            np.nan,
            np.nan,
            np.nan,
            np.nan,
        ],
        [
            data.loc["MgNi", label],
            data.loc["CaNi", label],
            data.loc["TiNi", label],
            data.loc["MnNi", label],
            data.loc["FeNi", label],
            data.loc["CoNi", label],
            np.nan,
            np.nan,
            np.nan,
        ],
        [
            data.loc["MgCu", label],
            data.loc["CaCu", label],
            data.loc["TiCu", label],
            data.loc["MnCu", label],
            data.loc["FeCu", label],
            data.loc["CoCu", label],
            data.loc["NiCu", label],
            np.nan,
            np.nan,
        ],
        [
            data.loc["MgZn", label],
            data.loc["CaZn", label],
            data.loc["TiZn", label],
            data.loc["MnZn", label],
            data.loc["FeZn", label],
            data.loc["CoZn", label],
            data.loc["NiZn", label],
            data.loc["CuZn", label],
            np.nan,
        ],
    ]
)

sns.heatmap(
    chempot_overlaps,
    square=True,
    vmin=-3.85,
    vmax=3.85,
    cmap=sns.color_palette("coolwarm_r", as_cmap=True),
    xticklabels=("Mg", "Ca", "Ti", "Mn", "Fe", "Co", "Ni", "Cu", "Zn"),
    yticklabels=("Mg", "Ca", "Ti", "Mn", "Fe", "Co", "Ni", "Cu", "Zn"),
    annot=False,
    fmt=".2f",
    linewidths=0.5,
    cbar_kws={"label": r"μ$_{\rm overlap}$ (eV)", "shrink": 0.5},
    annot_kws={"fontsize": 6, "color": "k"},
    cbar=True,
    center=0,
)
plt.yticks(rotation=0)
plt.tick_params(left=False, bottom=False)
plt.show()
