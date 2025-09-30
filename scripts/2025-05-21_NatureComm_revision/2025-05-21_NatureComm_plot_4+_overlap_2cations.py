# Plots the overlap in oxygen chemical potential between 2 AO phases as a heatmap
# if the value is positive (+), then this is overlap distance
# if the value is negative (-), then this is the distance between

import pandas as pd
import itertools
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

plt.rcParams["figure.dpi"] = 800
plt.rcParams["figure.figsize"] = (4, 4)
plt.rcParams["font.size"] = 12
plt.rcParams["font.serif"] = "Helvetica"
plt.rcParams["font.weight"] = "bold"


cations = ["Ti", "Hf", "Ce", "Zr"]
combos = list(
    itertools.combinations(cations, 2)
)  # creates a list of all combinations of cations

label = "overlap (eV)"

chempot_overlaps = np.array(
    [
        [np.nan, np.nan, np.nan, np.nan],
        [4.4752, np.nan, np.nan, np.nan],
        [3.7280, 3.7280, np.nan, np.nan],
        [4.4752, 5.6283, 3.7280, np.nan],
    ]
)

sns.heatmap(
    chempot_overlaps,
    square=True,
    vmin=-7,
    vmax=7,
    cmap=sns.diverging_palette(
        12,
        255,
        as_cmap=True,
    ),  # sns.color_palette("vlag_r", as_cmap=True),  # coolwarm_r
    xticklabels=("Ti", "Hf", "Ce", "Zr"),
    yticklabels=("Ti", "Hf", "Ce", "Zr"),
    annot=False,
    fmt=".1f",
    linewidths=0.75,
    cbar_kws={
        "label": r"μ$_{\rm \bf overlap}$ (eV)",
        "shrink": 0.5,
        "ticks": [-5, 0.0, 5],
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
