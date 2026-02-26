import os
import json

base_url = "https://raw.githubusercontent.com/piyushmohan01/PIPVIS-Image-Base/master/Body-Pose-Frames"
root = r"./Body-Pose-Frames"   # local path relative to this script

output_path = "manifest_pose.json"

manifest = {}

for subset in os.listdir(root):
    subset_dir = os.path.join(root, subset)
    if not os.path.isdir(subset_dir):
        continue

    manifest[subset] = {}

    for ped in os.listdir(subset_dir):
        ped_dir = os.path.join(subset_dir, ped)
        if not os.path.isdir(ped_dir):
            continue

        frames = {}
        for fname in sorted(os.listdir(ped_dir)):
            if not fname.lower().endswith(".jpg"):
                continue

            # expected file format: frame_<frameid>_pose.jpg
            try:
                frame_num = fname.split("_")[1]
            except IndexError:
                frame_num = fname  # fallback in case of unexpected name

            frames[frame_num] = f"{base_url}/{subset}/{ped}/{fname}"

        manifest[subset][ped] = {"frames": frames}

with open(output_path, "w") as f:
    json.dump(manifest, f, indent=2)