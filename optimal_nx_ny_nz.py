import numpy as np

def calculate_unwrapped_values(nx, ny, nz, mu_raw_px, mu_raw_py, mu_raw_pz, Pmax):
    Punwrap_px = mu_raw_px + 2 * nx * Pmax
    Punwrap_py = mu_raw_py + 2 * ny * Pmax
    Punwrap_pz = mu_raw_pz + 2 * nz * Pmax
    return Punwrap_px, Punwrap_py, Punwrap_pz

def get_difference(nx, ny, nz, Pbar_px, Pbar_py, Pbar_pz, mu_raw_px, mu_raw_py, mu_raw_pz, Pmax):
    Punwrap_px, Punwrap_py, Punwrap_pz = calculate_unwrapped_values(nx, ny, nz, mu_raw_px, mu_raw_py, mu_raw_pz, Pmax)
    px_diff = abs(Pbar_px - Punwrap_px)
    py_diff = abs(Pbar_py - Punwrap_py)
    pz_diff = abs(Pbar_pz - Punwrap_pz)
    return px_diff, py_diff, pz_diff

# Loaded data for each frame
mu_raw_data = np.load('mu_raw_ion_solution_1000.npy')
pmax_data = np.load('pmax_ion_solution_1000.npy')
pbar_data = np.load('scaled_pbar_ion_solution_1000.npy')

updated_punwrap = []

for frame_idx in range(len(mu_raw_data)):
    mu_raw_px = mu_raw_data[frame_idx][0]
    mu_raw_py = mu_raw_data[frame_idx][1]
    mu_raw_pz = mu_raw_data[frame_idx][2]
    
    Pmax = pmax_data[frame_idx]
    
    Pbar_px = pbar_data[frame_idx][0]
    Pbar_py = pbar_data[frame_idx][1]
    Pbar_pz = pbar_data[frame_idx][2]
    
    nx = 0
    ny = 0
    nz = 0
    
    print(f"Frame {frame_idx+1}:")
    print("Pbar_px:", Pbar_px)
    print("Pbar_py:", Pbar_py)
    print("Pbar_pz:", Pbar_pz)
    print("mu_raw_px or Punwrap_px when nx = 0:", mu_raw_px)
    print("mu_raw_py or Punwrap_py when ny = 0:", mu_raw_py)
    print("mu_raw_pz or Punwrap_pz when nz = 0:", mu_raw_pz)
    print("Pmax:", Pmax)
    
    while True:
        px_diff, py_diff, pz_diff = get_difference(nx, ny, nz, Pbar_px, Pbar_py, Pbar_pz, mu_raw_px, mu_raw_py, mu_raw_pz, Pmax)
        
        # Checked if changing nx, ny, nz can get closer to Pbar
        if get_difference(nx + 1, ny, nz, Pbar_px, Pbar_py, Pbar_pz, mu_raw_px, mu_raw_py, mu_raw_pz, Pmax) < (px_diff, py_diff, pz_diff):
            nx += 1
        elif get_difference(nx - 1, ny, nz, Pbar_px, Pbar_py, Pbar_pz, mu_raw_px, mu_raw_py, mu_raw_pz, Pmax) < (px_diff, py_diff, pz_diff):
            nx -= 1
        elif get_difference(0, ny, nz, Pbar_px, Pbar_py, Pbar_pz, mu_raw_px, mu_raw_py, mu_raw_pz, Pmax) < (px_diff, py_diff, pz_diff):
            nx = 0
        
        if get_difference(nx, ny + 1, nz, Pbar_px, Pbar_py, Pbar_pz, mu_raw_px, mu_raw_py, mu_raw_pz, Pmax) < (px_diff, py_diff, pz_diff):
            ny += 1
        elif get_difference(nx, ny - 1, nz, Pbar_px, Pbar_py, Pbar_pz, mu_raw_px, mu_raw_py, mu_raw_pz, Pmax) < (px_diff, py_diff, pz_diff):
            ny -= 1
        elif get_difference(nx, 0, nz, Pbar_px, Pbar_py, Pbar_pz, mu_raw_px, mu_raw_py, mu_raw_pz, Pmax) < (px_diff, py_diff, pz_diff):
            ny = 0
        
        if get_difference(nx, ny, nz + 1, Pbar_px, Pbar_py, Pbar_pz, mu_raw_px, mu_raw_py, mu_raw_pz, Pmax) < (px_diff, py_diff, pz_diff):
            nz += 1
        elif get_difference(nx, ny, nz - 1, Pbar_px, Pbar_py, Pbar_pz, mu_raw_px, mu_raw_py, mu_raw_pz, Pmax) < (px_diff, py_diff, pz_diff):
            nz -= 1
        elif get_difference(nx, ny, 0, Pbar_px, Pbar_py, Pbar_pz, mu_raw_px, mu_raw_py, mu_raw_pz, Pmax) < (px_diff, py_diff, pz_diff):
            nz = 0
        
        updated_px_diff, updated_py_diff, updated_pz_diff = get_difference(nx, ny, nz, Pbar_px, Pbar_py, Pbar_pz, mu_raw_px, mu_raw_py, mu_raw_pz, Pmax)
        
        # Checked if the differences are not decreasing anymore
        if updated_px_diff >= px_diff and updated_py_diff >= py_diff and updated_pz_diff >= pz_diff:
            break
    
    updated_Punwrap_px, updated_Punwrap_py, updated_Punwrap_pz = calculate_unwrapped_values(nx, ny, nz, mu_raw_px, mu_raw_py, mu_raw_pz, Pmax)
    
    updated_punwrap.append([updated_Punwrap_px, updated_Punwrap_py, updated_Punwrap_pz])

    
    print("Optimal nx:", nx)
    print("Optimal ny:", ny)
    print("Optimal nz:", nz)
    print("Updated Punwrap_px:", updated_Punwrap_px)
    print("Updated Punwrap_py:", updated_Punwrap_py)
    print("Updated Punwrap_pz:", updated_Punwrap_pz)
    print()  # Added an empty line for separation between frames


updated_punwrap = np.array(updated_punwrap)
# saved to punwrap_water_1000.npy file
np.save('punwrap_ion_solution_1000.npy', updated_punwrap)

