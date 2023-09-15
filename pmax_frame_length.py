from ase.io import read
import numpy as np

def extract_box_lengths(file_path):
    atoms_list = read(file_path, index=":")
    box_lengths = []

    for atoms in atoms_list:
        lattice = atoms.get_cell()
        box_lengths.append(lattice[0, 0])

    return box_lengths

def calculate_Pmax(length):
    return 2.401602135 * length

# Replace 'WATER_1000.xyz' with the actual path to your XYZ file
box_lengths = extract_box_lengths('ion_solution_1000.xyz')

# Calculate Pmax for each molecule
pmax_values = []
for idx, length in enumerate(box_lengths, start=1):
    Pmax = calculate_Pmax(length)
    pmax_values.append(Pmax)
    print(f'Frame {idx} - Pmax: {Pmax}')

# Convert the list of Pmax values to a NumPy array
pmax_array = np.array(pmax_values)

# Save the Pmax array to a file
np.save('pmax_ion_solution_1000.npy', pmax_array)
