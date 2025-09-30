# 2025-05-12

from pytheos import materials_project
from pytheos.stability import phase_diagram
from pytheos.stability.chemical_potential import ChemPotDiagram
import pandas

all_elements = ["Ce", "Zr", "Hf", "Ti", "Sn"]
print(all_elements)

stable_cations = []  # i.e., are on the convex hull for desired composition
stable_window = []  # in eV for oxygen chemical potential
stable_min = []
stable_max = []

for element in all_elements:

    print(f"\n\n\n{element} - O")

    entries = materials_project.query_entries_across_chemsys(
        elements=[element, "O"],
        thermo_type="GGA_GGA+U",
    )
    pd = phase_diagram.generate_phase_diagram(entries=entries)

    chempot = ChemPotDiagram(
        phase_diagram=pd,
        cation=element,
        anion="O",
        target_compound=f"{element}O2",  # A2O3
    )

    if chempot.get_target_anion_range():
        stable_cations.append(element)
        stable_min.append(chempot.get_target_anion_range()[0])
        stable_max.append(chempot.get_target_anion_range()[1])
        stable_window.append(chempot.get_target_anion_range()[2])

    chempot.get_all_stable_ranges()
    print(chempot.all_stable_ranges)

    chempot.plot_diagram(with_target=True)

    #chempot.diagram.savefig(f"diagrams_3+_A2O3/{element}-O.png")

df = pandas.DataFrame(
    {
        "cation": stable_cations,
        "stable_min_eV": stable_min,
        "stable_max_eV": stable_max,
        "stable_window_eV": stable_window,
    }
)

print(df)
df.to_csv("stable_windows_3+_A2O3.csv")
