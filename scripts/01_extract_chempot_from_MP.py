# Extract the chemical potential diagrams (domains and figures) from the Materials Project database
# Specifically only for A-O phase diagrams/chemical potentials
# GGA/GGA+U calculations only currently
# This is all set up currently for getting the mixed GGA/GGA+U phase diagram which is modified from https://docs.materialsproject.org/methodology/materials-methodology/thermodynamic-stability/phase-diagrams-pds
# but this can be modified to add r2scan as well if desired

from mp_api.client import MPRester
from pymatgen.analysis import chempot_diagram
from pymatgen.analysis.phase_diagram import PhaseDiagram, PDEntry, PDPlotter
from pymatgen.entries.mixing_scheme import MaterialsProjectDFTMixingScheme
from emmet.core.thermo import ThermoType
import numpy as np
import pandas as pd

# user specific!!
MPApiKey = "7Rirk7u8bWuEg6zyoIbDAoXS8zruAbN7"

cations = [
    # "Cr",
    "Mg",
    "Ca",
    "Mn",
    "Fe",
    "Co",
    "Ni",
    "Cu",
    "Zn",
]  # Mg + Ca + 3d row
# ValueError: No A2+O2- phase was found on the convex hull for Sc-O.
# ValueError: No A2+O2- phase was found on the convex hull for V-O.
# ValueError: No A2+O2- phase was found on the convex hull for Cr-O.

# will be populated for each cation
stableranges_AO = {"composition": ["min (eV)", "max (eV)", "distance (eV)"]}

start_bold = "\033[1m"
end_bold = "\033[0m"

for cation in cations:

    elements = [cation, "O"]

    with MPRester(MPApiKey) as mpr:

        # obtain GGA/GGA+U ComputedStructureEntropy objects
        entries = mpr.get_entries_in_chemsys(
            elements=[cation, "O"],
            additional_criteria={"thermo_types": ["GGA_GGA+U"]},
        )

        # apply corrections locally with mixing scheme
        scheme = MaterialsProjectDFTMixingScheme()
        corrected_entries = scheme.process_entries(entries)

    # construct phase diagram
    phasediagram = PhaseDiagram(corrected_entries)

    # construct chemical potential diagram
    chempot = chempot_diagram.ChemicalPotentialDiagram(phasediagram.all_entries)

    print(start_bold + f"\n\n{cation}-O chemical potential diagram" + end_bold)

    chempot_fig = chempot.get_plot(elements)
    chempot_fig.update_yaxes(range=[-8, 0.5])
    chempot_fig.update_layout(width=500, height=1000)
    chempot_fig.write_image(f"../results/chempot-{cation}-O-GGA_GGA+U.png")

    chempot_domains = chempot.domains
    for domain in chempot_domains:
        print(domain)
        print(f"\t{np.round(chempot_domains[domain][0], 4)}")
        print(f"\t{np.round(chempot_domains[domain][1], 4)}")

    ### get oxygen chemical potential range where A2+O2- is stable
    AO_stable_range = None  # to ensure values are always reset
    minimum = None  # to ensure values are always reset
    maximum = None  # to ensure values are always reset

    # get rid of elemental
    chempot_domains.pop(cation)
    chempot_domains.pop("O2")

    # provides a check if there is an AO phases on the convex hull.abs
    # if there is not, then a chemical potential diagram cannot be constructed
    if f"{cation}O" not in chempot_domains:
        raise ValueError(
            f"No A2+O2- phase was found on the convex hull for {cation}-O."
        )

    # go through all compounds present in chemical potential diagram
    for i in chempot_domains:
        if i == "{}O".format(cation):  # only care for the AO in this case
            minimum = chempot_domains[i][0][1]
            maximum = chempot_domains[i][1][1]
            if (
                minimum > maximum
            ):  # since sometimes the order is flipped from MP API pull
                minimum, maximum = maximum, minimum
            print(f"\nstable oxygen range for {cation}O ->")
            print("\tmin = {:.4f} eV".format(minimum))
            print("\tmax = {:.4f} eV".format(maximum))
            stablerange = abs(maximum - minimum)
            print("\tdistance = {:.4f} eV\n\n".format(stablerange))

    stableranges_AO["{}O".format(cation)] = [
        np.around(minimum, 4),
        np.around(maximum, 4),
        np.around(stablerange, 4),
    ]


df = pd.DataFrame.from_dict(stableranges_AO)
print(
    start_bold
    + "A2+O2- stable oxygen chemical potential ranges ->\n\n"
    + end_bold
    + str(df)
)
# df.to_csv("../data/chempot-oxygen-stable-ranges-GGA_GGA+U.csv", index=False)
