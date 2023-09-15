import numpy as np
from ase.io import read

def extract_mu_raw(file_path):
    # Load the XYZ file
    molecules = list(read(file_path, index=slice(None, None, None)))

    # Extract mu_raw data for each molecule
    mu_raw_list = []
    for idx, molecule in enumerate(molecules):  # Added 'idx' to keep track of the index
        mu_raw = molecule.info.get('mu_raw')
        if mu_raw is not None:
            mu_raw_list.append(mu_raw)
            print(f'Molecule {idx + 1} - mu_raw: {mu_raw}')

    # Convert the list to a NumPy array
    mu_raw_array = np.array(mu_raw_list)

    # Save the NumPy array to a file
    # np.save('pcalc_water_1000.npy', mu_raw_array)
    np.save('mu_raw_ion_solution_1000.npy', mu_raw_array)

# Replace 'your_file.xyz' with the actual path to your XYZ file
extract_mu_raw('ion_solution_1000.xyz')

