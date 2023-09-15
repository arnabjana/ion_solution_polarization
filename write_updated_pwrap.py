import numpy as np
from ase.io import read, write

# Read the original .xyz file
structures = list(read('ion_solution_1000.xyz', ':'))

# Load mu_unwrap values from the NumPy file
mu_unwrap_values = np.load('punwrap_ion_solution_1000.npy')

# Check if the number of structures and mu_unwrap_values match
if len(structures) != len(mu_unwrap_values):
    raise ValueError(f"Number of structures ({len(structures)}) and mu_unwrap_values ({len(mu_unwrap_values)}) must be the same.")

# Add mu_unwrap information to each structure
for structure, mu_unwrap in zip(structures, mu_unwrap_values):
    structure.info['mu_unwrap'] = mu_unwrap

# Write the modified content back to the .xyz file
write('modified_ion_solution_1000.xyz', structures)
