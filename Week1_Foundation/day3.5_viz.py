import open3d as o3d
import numpy as np

print("--- Day 3.5: The RGB Cube Challenge ---")

# Generate a 2x3 2D array (matrix)
# two_d_array = np.random.rand(2, 3)
# 1. Create Data from Scratch
# We want 10,000 points
num_points = 20000

# CHALLENGE 1: Generate random positions
# Use numpy to create a matrix of random numbers between 0 and 1.
# Shape must be (10000, 3) -> [x, y, z] for each point
# Hint: Look up np.random.rand
points_xyz = np.random.rand(num_points, 3) # <--- DELETE THIS and fix it

# 2. Create the Open3D Object
# "Empty" point cloud object
pcd = o3d.geometry.PointCloud()

# CHALLENGE 2: Feed your data into the object
# The .points property expects a "Vector3dVector"
# Look at the syntax from the previous day's code or docs.
pcd.points = o3d.utility.Vector3dVector(points_xyz)

# 3. logic: Color = Position
# We want the color to match the coordinates.
# If a point is at [1, 0, 0] (Far Right), color is [1, 0, 0] (Red).
# If a point is at [0, 1, 0] (Top), color is [0, 1, 0] (Green).

print("Coloring points based on position...")

# CHALLENGE 3: Assign the colors
# Since our coordinates are already between 0.0 and 1.0, 
# and colors expect 0.0 to 1.0, we can just use the position AS the color!
points_xyz[:,0] = 1.0
pcd.colors = o3d.utility.Vector3dVector(points_xyz) # <--- Is this right? Think about it.

# 4. Visualize
print("Opening Viewer...")
# The "Pro" Viewer
# This opens the modern GUI with a settings panel on the right
o3d.visualization.draw([pcd])