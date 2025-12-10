import open3d as o3d
import numpy as np

print("Open3D version:", o3d.__version__)

# Create a simple point cloud
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(np.random.rand(100, 3))

print("Successfully created a point cloud!")