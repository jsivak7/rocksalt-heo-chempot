# Plots the overlap in oxygen chemical potential between 5 AO phases for a 5-cation rock salt HEO
# if the value is positive (+), then this is overlap distance
# if the value is negative (-), then this is the distance between

import pandas as pd
import itertools
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

plt.rcParams["figure.figsize"] = (6, 4)
plt.rcParams["figure.dpi"] = 400
plt.rcParams["font.serif"] = "Arial"
plt.rcParams["font.size"] = 8

data = pd.read_csv("../data/descriptors-5cation-ALL-noCa.csv")
data_sorted = data.sort_values(by=["chempot overlap (eV)"], ascending=True)
data_sorted

plt.barh(
    data_sorted["composition"],
    data_sorted["chempot overlap (eV)"],
    color="#e31a1c",
)

plt.xticks([-0.75, -0.5, -0.25, 0.0, 0.25, 0.50, 0.75])
plt.xlim(-0.85, 0.85)
plt.axvline(0, color="black", linestyle="--", zorder=0, linewidth=0.75)
plt.xlabel(r"μ$_{\rm overlap}$ (eV)", size=10)
plt.show()
