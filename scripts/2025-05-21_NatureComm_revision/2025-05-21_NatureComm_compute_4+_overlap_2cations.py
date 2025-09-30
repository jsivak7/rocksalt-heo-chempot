# Calculates the overlap in oxygen chemical potential between 2 phases
# if the value is positive (+), then this is overlap distance
# if the value is negative (-), then this is the distance between

import pandas as pd
import itertools
import numpy as np

# run this section first to get the transposed data, then remove header numbers
"""
chempots = pd.read_csv("../data/stable_windows_4+.csv")
chempots_transposed = chempots.transpose()
print(chempots_transposed)
chempots_transposed.to_csv("../data/stable_windows_4+.csv")
"""
chempots = pd.read_csv("../data/stable_windows_4+_transposed.csv")
print(chempots)

cations = ["Ti", "Hf", "Ce", "Zr"]

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

    oxide1 = f"{cation1}"
    oxide2 = f"{cation2}"

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
