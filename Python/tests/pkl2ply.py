import pickle
import open3d as o3d
import numpy as np

def pkl2ply(pkl_path, output_path = "output_file.ply"):

    with open(pkl_path, "rb") as f:
        point_cloud = pickle.load(f)

    for key in point_cloud.keys():
        print("Key:", key)

    # Example conversion if point_cloud is a list of dictionaries
    points = np.array([[point['x'], point['y'], point['z']] for point in point_cloud])

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)

    # Save as .ply file
    o3d.io.write_point_cloud(output_path, pcd)

def read_pkl(file_path):
    with open(file_path, 'rb') as f:
        data = pickle.load(f)

    #print(len(data["objects"]))

    #for key in data.keys():
    #    print("Key:", key, type(data[key]))
    
    # Assuming the function expects a numpy array of points
    # Extract points from data (modify this if the structure differs)

    # points = np.vstack([obj['pcd_np'] for obj in data['objects']])

    points = np.vstack([obj['pcd_np'] for obj in data['objects'] if obj['class_name'] == 'keyboard' or obj['class_name'] == 'laptop'])

    # points = np.vstack(data['objects'][0]['pcd_np'])
    return points