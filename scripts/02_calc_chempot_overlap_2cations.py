# Calculates the overlap in oxygen chemical potential between 2 AO phases
# if the value is positive (+), then this is overlap distance
# if the value is negative (-), then this is the distance between

import pandas as pd
import itertools
import numpy as np

chempots = pd.read_csv("../data/chempot-oxygen-stable-ranges-GGA_GGA+U.csv")
print(chempots)

cations = ["Mg", "Ca", "Ti", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",] # Mg + Ca + 3d row
    # ValueError: No A2+O2- phase was found on the convex hull for Sc-O.
    # ValueError: No A2+O2- phase was found on the convex hull for V-O.
    # ValueError: No A2+O2- phase was found on the convex hull for Cr-O.

combos = list(
    itertools.combinations(cations, 2)
)  # creates a list of all combinations of cations

clean_combos = []
overlaps = []

start_bold = "\033[1m"
end_bold = "\033[0m"

for combo in combos:
    print("\n" + start_bold + str(combo) + end_bold)

    cation1 = combo[0]
    cation2 = combo[1]
    clean_combos.append(f"{cation1}{cation2}")

    oxide1 = f"{cation1}O"
    oxide2 = f"{cation2}O"

    min1 = chempots[oxide1][0]
    max1 = chempots[oxide1][1]
    min2 = chempots[oxide2][0]
    max2 = chempots[oxide2][1]
    overlap = min(max1, max2) - max(min1, min2)

    print(str(np.round(overlap, 4)) + " eV")
    overlaps.append(np.round(overlap, 4))

dict = {"combo": clean_combos, "overlap (eV)": overlaps}

df = pd.DataFrame(dict)
print(
    start_bold
    + "\n\nStable oxygen chemical potential overlap ->\n\n"
    + end_bold
    + str(df)
)
df.to_csv("../data/chempot-overlap-2cation-GGA_GGA+U.csv", index=False)
