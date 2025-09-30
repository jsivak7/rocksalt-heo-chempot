# Calculates the overlap in oxygen chemical potential between six AO phases
# if the value is positive (+), then this is overlap distance
# if the value is negative (-), then this is the distance between

import pandas as pd
import itertools
import numpy as np

chempots = pd.read_csv("../data/chempot-oxygen-stable-ranges-GGA_GGA+U.csv")
print(chempots)

# added in Ti to compare to Yokokawa phase diagram
cations = ["Mg", "Ca", "Mn", "Fe", "Co", "Ni", "Cu", "Zn"]
combos = list(
    itertools.combinations(cations, 6)
)  # creates a list of all combinations of cations

clean_combos = []
overlaps = []

start_bold = "\033[1m"
end_bold = "\033[0m"

for combo in combos:
    print("\n" + start_bold + str(combo) + end_bold)

    cation1 = combo[0]
    cation2 = combo[1]
    cation3 = combo[2]
    cation4 = combo[3]
    cation5 = combo[4]
    cation6 = combo[5]
    clean_combos.append(f"{cation1}{cation2}{cation3}{cation4}{cation5}{cation6}")

    oxide1 = f"{cation1}O"
    oxide2 = f"{cation2}O"
    oxide3 = f"{cation3}O"
    oxide4 = f"{cation4}O"
    oxide5 = f"{cation5}O"
    oxide6 = f"{cation6}O"

    min1 = chempots[oxide1][0]
    max1 = chempots[oxide1][1]
    min2 = chempots[oxide2][0]
    max2 = chempots[oxide2][1]
    min3 = chempots[oxide3][0]
    max3 = chempots[oxide3][1]
    min4 = chempots[oxide4][0]
    max4 = chempots[oxide4][1]
    min5 = chempots[oxide5][0]
    max5 = chempots[oxide5][1]
    min6 = chempots[oxide6][0]
    max6 = chempots[oxide6][1]
    overlap = min(max1, max2, max3, max4, max5, max6) - max(
        min1, min2, min3, min4, min5, min6
    )

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
df.to_csv("../data/chempot-overlap-6cation-GGA_GGA+U.csv", index=False)
