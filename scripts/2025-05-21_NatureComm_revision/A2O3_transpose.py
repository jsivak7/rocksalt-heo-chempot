import pandas as pd
import itertools
import numpy as np

chempots = pd.read_csv("../../data/stable_windows_A2O3.csv")
chempots_transposed = chempots.transpose()
print(chempots_transposed)
chempots_transposed.to_csv("../../data/stable_windows_A2O3_transposed.csv")
