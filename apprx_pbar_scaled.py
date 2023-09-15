from ase import Atoms
from ase.io import read
import numpy as np

# Read the input file
structures = read('ion_solution_1000.xyz', index=':')

scaled_pbar_list = []  # List to store scaled pbar vectors


# Iterate through each structure
for i, atoms in enumerate(structures):
    print(f"Structure {i+1}:")
    print("Atom   px       py       pz")
    print("==========================")
    
    pbar = [0.0, 0.0, 0.0]  # Initialize the pbar vector
    
    for atom in atoms:
        px, py, pz = atom.position
        
        if atom.symbol == 'H':
            px *= 0.5
            py *= 0.5
            pz *= 0.5
        elif atom.symbol == 'O':
            px *= -1
            py *= -1
            pz *= -1
        elif atom.symbol == 'Na':
            px *= 1
            py *= 1
            pz *= 1
        elif atom.symbol == 'Cl':
            px *= -1
            py *= -1
            pz *= -1    
        
        pbar[0] += px
        pbar[1] += py
        pbar[2] += pz
        
        print(f"{atom.symbol}   {px:.6f}   {py:.6f}   {pz:.6f}")
    
    print("==========================")
    
    # Print the calculated pbar vector
    print("pbar:", pbar)
    print("==========================\n")
    
    # Calculate the scaled pbar vector
    scaled_pbar = [coord * 4.80320470063365 for coord in pbar]
    
    # Print the scaled pbar vector
    print("Scaled pbar:", scaled_pbar)
    print("==========================\n")
    
    # Append the scaled pbar vector to the list
    scaled_pbar_list.append(scaled_pbar)
    
# Convert the list of scaled pbar vectors to a NumPy array
scaled_pbar_array = np.array(scaled_pbar_list)

# Save the scaled_pbar_array to a .npy file
np.save('scaled_pbar_ion_solution_1000.npy', scaled_pbar_array)
