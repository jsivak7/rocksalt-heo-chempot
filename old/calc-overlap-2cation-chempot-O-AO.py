'''
JTSivak
November 7, 2023

'''

import pandas as pd
import itertools

data = pd.read_csv('./AO-Oxygen-chempot-stablerange-MP-GGA_GGAU_R2SCAN.csv')
print(data)

cations = ['Mg', 'Ca', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn']

combos = list(itertools.combinations(cations, 2)) # creates a list of all the combinations given the 'num_cations' for each combination
    # [('Mg', 'Ca'), ('Mg', 'Mn'), ...]

overlaps = []

for combo in combos:
    print(combo)

    cation1 = combo[0]
    cation2 = combo[1]

    oxide1 = "{}O".format(cation1)
    oxide2 = "{}O".format(cation2)

    min1 = data[oxide1][0]
    max1 = data[oxide1][1]
    min2 = data[oxide2][0]
    max2 = data[oxide2][1]
    overlap = max(min1, min2) - min(max1, max2)
        # if negative, overlap distance
        # if positive, distance between

    print(overlap)
    overlaps.append(overlap)

dict = {
    'combo': combos,
    'overlap_eV': overlaps
}

df = pd.DataFrame.from_dict(dict)
print(df)

df.to_csv('overlaps.csv', index = False)