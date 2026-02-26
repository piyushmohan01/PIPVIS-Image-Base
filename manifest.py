import os
import json

base_url = "https://raw.githubusercontent.com/piyushmohan01/PIPVIS-Image-Base/master/Occlusion-Frames"
root = r"./Occlusion-Frames"

manifest = {}
for subset in os.listdir(root):
    manifest[subset] = {}
    subset_dir = os.path.join(root, subset)
    for ped in os.listdir(subset_dir):
        ped_dir = os.path.join(subset_dir, ped)
        if not os.path.isdir(ped_dir): continue
        frames = {}
        for fname in os.listdir(ped_dir):
            if not fname.lower().endswith(".jpg"): continue
            # extract frame number
            # assume filename like 'frame_5561.jpg'
            frame_num = fname.split("_")[-1].split(".")[0]
            frames[frame_num] = f"{base_url}/{subset}/{ped}/{fname}"
        manifest[subset][ped] = {"frames": frames}

# write manifest
with open("manifest.json","w") as f:
    json.dump(manifest,f,indent=2)