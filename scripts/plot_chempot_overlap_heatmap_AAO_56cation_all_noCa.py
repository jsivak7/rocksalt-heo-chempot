# Plots the overlap in oxygen chemical potential between 2 AO phases as a heatmap
# if the value is positive (+), then this is overlap distance
# if the value is negative (-), then this is the distance between

import pandas as pd
import itertools
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

plt.rcParams["figure.dpi"] = 400
plt.rcParams["figure.figsize"] = (4, 4)
plt.rcParams["font.size"] = 12
plt.rcParams["font.serif"] = "Helvetica"


data = pd.read_csv("../data/descriptors-2cation-ALL-noCa.csv")
data = data.set_index("combo")
print(data)

# no Ca since not being looked into here in this paper
cations = ["Mg", "Mn", "Fe", "Co", "Ni", "Cu", "Zn"]
combos = list(
    itertools.combinations(cations, 2)
)  # creates a list of all combinations of cations

label = "chempot overlap (eV)"

chempot_overlaps = np.array(
    [
        [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
        [
            data.loc["MgMn", label],
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
        ],
        [
            data.loc["MgFe", label],
            data.loc["MnFe", label],
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
        ],
        [
            data.loc["MgCo", label],
            data.loc["MnCo", label],
            data.loc["FeCo", label],
            np.nan,
            np.nan,
            np.nan,
            np.nan,
        ],
        [
            data.loc["MgNi", label],
            data.loc["MnNi", label],
            data.loc["FeNi", label],
            data.loc["CoNi", label],
            np.nan,
            np.nan,
            np.nan,
        ],
        [
            data.loc["MgCu", label],
            data.loc["MnCu", label],
            data.loc["FeCu", label],
            data.loc["CoCu", label],
            data.loc["NiCu", label],
            np.nan,
            np.nan,
        ],
        [
            data.loc["MgZn", label],
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
    vmin=-1.1,
    vmax=1.1,
    cmap=sns.diverging_palette(
        12,
        255,
        as_cmap=True,
    ),  # sns.color_palette("vlag_r", as_cmap=True),  # coolwarm_r
    xticklabels=("Mg", "Mn", "Fe", "Co", "Ni", "Cu", "Zn"),
    yticklabels=("Mg", "Mn", "Fe", "Co", "Ni", "Cu", "Zn"),
    annot=False,
    fmt=".1f",
    linewidths=0.75,
    cbar_kws={
        "label": r"μ$_{\rm overlap}$ (eV)",
        "shrink": 0.5,
        "ticks": [-0.6, 0.0, 0.6],
    },
    annot_kws={"fontsize": 6, "color": "k"},
    cbar=True,
    center=0,
)
plt.xticks(weight="bold")
plt.yticks(weight="bold")
plt.yticks(rotation=0)
plt.tick_params(left=False, bottom=False)
plt.show()
