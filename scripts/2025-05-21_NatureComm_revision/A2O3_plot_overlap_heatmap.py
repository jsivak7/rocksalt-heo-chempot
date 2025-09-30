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


cations = [
    "Y3+",
    "La3+",
    "Pr3+",
    "Sm3+",
    "Ce3.0+",
    "Ce3.4+",
    "Ce3.6+",
    "Ce4.0+",
]
combos = list(
    itertools.combinations(cations, 2)
)  # creates a list of all combinations of cations

label = "overlap (eV)"

chempot_overlaps = np.array(
    [
        [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
        [6.4569, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
        [6.2252, 6.2252, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
        [6.4366, 6.4366, 6.2252, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
        [0.2524, 0.2524, 0.2524, 0.2524, np.nan, np.nan, np.nan, np.nan, np.nan],
        [0.9645, 0.9645, 0.9645, 0.9645, np.nan, np.nan, np.nan, np.nan, np.nan],
        [0.9674, 0.9674, 0.9674, 0.9674, np.nan, np.nan, np.nan, np.nan, np.nan],
        [3.7280, 3.7280, 3.7280, 3.7280, np.nan, np.nan, np.nan, np.nan, np.nan],
    ]
)

sns.heatmap(
    chempot_overlaps,
    square=True,
    vmin=-8,
    vmax=8,
    cmap=sns.diverging_palette(
        12,
        255,
        as_cmap=True,
    ),  # sns.color_palette("vlag_r", as_cmap=True),  # coolwarm_r
    xticklabels=(
        r"Y$^{\rm \bf 3\!+}$",
        r"La$^{\rm \bf 3\!+}$",
        r"Pr$^{\rm \bf 3\!+}$",
        r"Sm$^{\rm \bf 3\!+}$",
        r"Ce$^{\rm \bf 3.0\!+}$",
        r"Ce$^{\rm \bf 3.4\!+}$",
        r"Ce$^{\rm \bf 3.6\!+}$",
        r"Ce$^{\rm \bf 4.0\!+}$",
    ),
    yticklabels=(
        r"Y$^{\rm \bf 3\!+}$",
        r"La$^{\rm \bf 3\!+}$",
        r"Pr$^{\rm \bf 3\!+}$",
        r"Sm$^{\rm \bf 3\!+}$",
        r"Ce$^{\rm \bf 3.0\!+}$",
        r"Ce$^{\rm \bf 3.4\!+}$",
        r"Ce$^{\rm \bf 3.6\!+}$",
        r"Ce$^{\rm \bf 4.0\!+}$",
    ),
    annot=False,
    fmt=".1f",
    linewidths=0.75,
    cbar_kws={
        "label": r"${\bf μ_{\rm \bf overlap} (eV)}$",
        "shrink": 0.5,
        "ticks": [-4, 0.0, 4],
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
