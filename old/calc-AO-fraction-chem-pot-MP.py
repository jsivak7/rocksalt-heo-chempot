'''
JTSivak
October 18, 2023

To Do
'''

from mp_api.client import MPRester
from pymatgen.analysis import chempot_diagram
from pymatgen.analysis.phase_diagram import PhaseDiagram
from pymatgen.analysis.phase_diagram import PDEntry
from emmet.core.thermo import ThermoType
import math
import numpy as np

MPApiKey = "7Rirk7u8bWuEg6zyoIbDAoXS8zruAbN7"

# to get the mixed GGA/GGA+U/r2SCAN phase diagram and then get the chemical potential diagram for a given A-O composition space
    # modified from https://docs.materialsproject.org/methodology/materials-methodology/thermodynamic-stability/phase-diagrams-pds

from mp_api.client import MPRester
from pymatgen.analysis.phase_diagram import PhaseDiagram, PDPlotter
from pymatgen.entries.mixing_scheme import MaterialsProjectDFTMixingScheme

# dictionary that will be filled with the fractions of chemical potential diagram distances that are AO
fractions_AO = {} # will be added to with 'cation':'fraction'

# define all cations to sample with oxygen (A-O composition space)
cations = ['Mg', 'Ca', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Pb']

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
    pd = PhaseDiagram(corrected_entries)
        
    chempot = chempot_diagram.ChemicalPotentialDiagram(pd.all_entries)
    fig = chempot.get_plot(elements)
    fig.write_image("{}-O-chempot-oxygen.png".format(cation))

    domain_dict = chempot._get_domains()
    chempot._get_domains()

    def get_distance_on_chempotdiagram(system):
        '''
        gets the euclidian distance of compositions on a chemical potential diagram
        '''
        #print("\n{}".format(system))
        dist = math.dist(domain_dict[system][0], domain_dict[system][1])
        #print(dist)
        return dist

    # to get rid of elemental distances
    domain_dict.pop(cation)
    domain_dict.pop('O2')

    total_distance = 0

    AO = None

    # go through the remaining compounds in the chemical potential diagram
        # sum up all of the distances and get the AO distance
    for i in domain_dict:
        #print("{} = {:.2f}".format(i, get_distance_on_chempotdiagram(i)))
        total_distance += get_distance_on_chempotdiagram(i)
        if i == '{}O'.format(cation):
            AO = get_distance_on_chempotdiagram(i) # if there is an AO oxide on the chemical potnetial diagram, then get this distance

    if AO == None:
        AO = 0 # else if there is no AO oxide on the chemical potential diagram, this should be 0

    print("\n{}O distance = {:.2f}".format(cation, AO))
    #print("Total distance = {:.2f}".format(total_distance))

    print("{}O fraction = {:.2f}".format(cation, AO/total_distance))

    fractions_AO[cation] = np.around(AO/total_distance, 4) # add each AO fraction to the dictionary

print("\n\n##### FINAL AO FRACTIONS #####\n\n")
print(fractions_AO)
