""" p2_24.py """

# pylint: disable=pointless-string-statement
'''
import numpy as np
import open3d as o3d

model = o3d.data.BunnyMesh()
# model = o3d.data.ArmadilloMesh()
# model = o3d.data.KnotMesh()

mesh = o3d.io.read_triangle_mesh(model.path)
mesh.compute_vertex_normals()

print("model.path:     ", model.path)
print("mesh.vertices:  ", len(np.asarray(mesh.vertices)))
print("mesh.triangles: ", len(np.asarray(mesh.triangles)))

# print("\noriginal poly")
# o3d.visualization.draw_plotly([mesh], window_name=model.path)

# print("\noriginal pts")
# o3d.io.write_triangle_mesh("temp.ply", mesh)
# pcd = o3d.io.read_point_cloud("temp.ply")
# o3d.visualization.draw_plotly([pcd], window_name=model.path)

pts = 3000
print(f"\nsample_points_uniformly ({pts})")
pcd_u = mesh.sample_points_uniformly(number_of_points=pts)
o3d.visualization.draw_plotly([pcd_u], window_name=model.path)

# print(f"\nsample_points_poisson_disk ({pts})")
# pcd_p = mesh.sample_points_poisson_disk(number_of_points=pts)
# o3d.visualization.draw_plotly([pcd_p], window_name=model.path)

'''
