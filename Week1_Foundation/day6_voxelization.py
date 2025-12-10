import open3d as o3d
import numpy as np

print("--- Day 3.5: Surface Reconstruction (Points -> Mesh) ---")

# 1. Load a high-quality Point Cloud (The Stanford Bunny)
print("1. Loading Bunny Point Cloud...")
pcd = o3d.io.read_point_cloud(o3d.data.BunnyMesh().path)
# Note: The built-in bunny might be a mesh, let's treat it as points
pcd = o3d.geometry.PointCloud(pcd.points)

# 2. THE MATH: Estimate Normals
# We cannot build a skin if we don't know which way is "up" for every point.
print("2. Estimating Normals (The 'Quills')...")
pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))

# OPTIONAL: Orient normals to ensure they all point "out"
pcd.orient_normals_consistent_tangent_plane(100)

# Visualize just the points with normals first
# Press 'n' in the viewer to see the lines!
# print("   (Close the window to proceed to meshing...)")
# o3d.visualization.draw_geometries([pcd], window_name="Step 1: Points + Normals", point_show_normal=True)

# 3. THE ALGORITHM: Poisson Surface Reconstruction
print("\n3. Running Poisson Reconstruction (Connecting the dots)...")
# This returns two things: The Mesh, and a density array (we ignore density for now)
mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=9)

# 4. Cleanup
# The algorithm often creates a "bubble" around the shape. We crop it.
# (This is just a quick hack to make it look clean)
bbox = pcd.get_axis_aligned_bounding_box()
mesh = mesh.crop(bbox)

# Paint it to look like a solid object (Grey)
mesh.paint_uniform_color([0.5, 0.5, 0.5])
mesh.compute_vertex_normals()

# 5. Visualize the Final Solid Mesh
# print("4. Opening Final Mesh...")
# print("   Controls: Press 'W' to see the wireframe (triangles)!")
# o3d.visualization.draw_geometries([mesh], 
#                                   window_name="Step 2: The Solid Mesh", 
#                                   width=800, height=600,
                                #   mesh_show_wireframe=True)

voxel_grid = o3d.geometry.VoxelGrid.create_from_triangle_mesh(mesh, voxel_size=0.001)
o3d.visualization.draw_geometries([voxel_grid])
voxel_grid.colors = o3d.utility.Vector3dVector(voxel_grid)
o3d.visualization.draw_geometries([pcd])
print("✅ SUCCESS: You turned a cloud of dots into a solid game asset.")