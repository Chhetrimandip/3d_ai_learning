import open3d as o3d
import numpy as np
import os

print("--- Day 3: Visualizing 3D Data ---")

# 1. Load a Sample Point Cloud
# Open3D has built-in samples so you don't need to download anything manually.
print("1. Loading Sample Point Cloud...")
pcd = o3d.io.read_point_cloud(o3d.data.PLYPointCloud().path)
print(f"   Loaded {len(pcd.points)} points.")

# Visualize the original
print("   Opening Window 1: Original Colors (Close window to continue)...")
o3d.visualization.draw_geometries([pcd], 
                                  window_name="1. Original",
                                  width=800, height=600)

# 2. THE ENGINEERING PART: Manipulation
print("\n2. Hacking the Matrix (Painting it RED)...")

# Access the points as a numpy array
# We need a color matrix of the same shape: (Number of Points, 3)
num_points = len(pcd.points)

# Create a matrix full of Zeros
new_colors = np.zeros((num_points, 3))

# Set the First Column (Red Channel) to 1.0 for ALL rows
# Syntax: array[:, column_index]
new_colors[:, 0] = 1.0 

# Apply these new colors to the object
pcd.colors = o3d.utility.Vector3dVector(new_colors)

# Visualize the result
print("   Opening Window 2: Red Version (Close window to continue)...")
o3d.visualization.draw_geometries([pcd], 
                                  window_name="2. RED Version",
                                  width=800, height=600)

# 3. Save the result
output_file = "day3_red_cloud.pcd"
o3d.io.write_point_cloud(output_file, pcd)
print(f"\n3. Saved modified data to '{output_file}'")

if os.path.exists(output_file):
    print("✅ SUCCESS: File saved. You have manipulated 3D reality.")
else:
    print("❌ FAILURE: File not saved.")