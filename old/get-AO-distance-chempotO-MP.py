'''
JTSivak
November 7, 2023

Uses the MP API to get the Oxygen chemical potential distance that the A2+O2- phase is stable.

This is all set up currently for getting the mixed GGA/GGA+U/r2SCAN phase diagram which is modified from
https://docs.materialsproject.org/methodology/materials-methodology/thermodynamic-stability/phase-diagrams-pds

Returns -->
.csv of AO stable ranges for oxygen chemical potential

'''

from mp_api.client import MPRester
from pymatgen.analysis import chempot_diagram
from pymatgen.analysis.phase_diagram import PhaseDiagram
from pymatgen.analysis.phase_diagram import PDEntry
from emmet.core.thermo import ThermoType
import math
import numpy as np
import pandas as pd

from mp_api.client import MPRester
from pymatgen.analysis.phase_diagram import PhaseDiagram, PDPlotter
from pymatgen.entries.mixing_scheme import MaterialsProjectDFTMixingScheme

MPApiKey = "7Rirk7u8bWuEg6zyoIbDAoXS8zruAbN7"

# dictionary that will be filled with the fractions of chemical potential diagram distances that are AO
stableranges_AO = {
    "label":['min_eV', 'max_eV', 'dist_eV']
    }

# define all cations to sample with oxygen (A-O composition space)
cations = ['Ti'], #'Mg', 'Ca', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn']

for cation in cations:
    elements = [cation, 'O']
    with MPRester(MPApiKey) as mpr:

        # Obtain GGA, GGA+U, and r2SCAN ComputedStructureEntry objects
        entries = mpr.get_entries_in_chemsys(elements=[cation, 'O'], 
                                            additional_criteria={"thermo_types": ["GGA_GGA+U", "R2SCAN"]}) 
        
        # Apply corrections locally with the mixing scheme
        scheme = MaterialsProjectDFTMixingScheme()
        corrected_entries = scheme.process_entries(entries)
        
    # Construct phase diagram
    phasediagram = PhaseDiagram(corrected_entries)
        
    chempot = chempot_diagram.ChemicalPotentialDiagram(phasediagram.all_entries)
    
    # get individual chemical potential diagram
    fig = chempot.get_plot(elements)
    fig.update_yaxes(range=[-8, 0.5])
    fig.update_layout(width = 500, height = 1000)
    fig.write_image("chempot-oxygen-{}-O.png".format(cation))

    domain_dict = chempot._get_domains()
    chempot._get_domains()

    print("\n##### {}-O #####".format(cation))

    print("\nDict of Stable Phases -->\n{}".format(domain_dict))

    stablerange = None # to make sure always resets

    # to get rid of elemental distances
    domain_dict.pop(cation)
    domain_dict.pop('O2')
  
    # go through compounds in the chemical potential diagram
    for i in domain_dict:
        if i == '{}O'.format(cation): # only care for the AO in this case
            min = domain_dict[i][0][1]
            max = domain_dict[i][1][1]
            print("\nStable Oxygen ChemPot Range for AO--> ")
            print("\tMinimum = {:.6f} eV".format(min))
            print("\tMaximum = {:.6f} eV".format(max))

            stablerange = abs(max-min)

            print("\tDistance = {:.6f} eV\n".format(stablerange))

    if stablerange == None:
        stablerange = 0 # else if there is no AO oxide on the chemical potential diagram, this should be 0

    stableranges_AO['{}O'.format(cation)] = [np.around(min, 6), np.around(max, 6), np.around(stablerange, 6)]

# convert to Pandas df and save to a .csv
df = pd.DataFrame.from_dict(stableranges_AO)
print(df)
df.to_csv("AO-Oxygen-chempot-stablerange-MP-GGA_GGAU_R2SCAN.csv", index = False)