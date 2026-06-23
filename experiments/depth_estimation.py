import torch
import urllib.request
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# download midas model
model_type = "MiDaS_small"
midas = torch.hub.load("intel-isl/MiDaS", model_type)
midas.eval()

# load transforms
transforms = torch.hub.load("intel-isl/MiDaS", "transforms")
transform = transforms.small_transform

# download a sample image
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Above_Gotham.jpg/800px-Above_Gotham.jpg"
urllib.request.urlretrieve(url, "sample.jpg")

# run depth estimation
img = Image.open("sample.jpg").convert("RGB")
img_np = np.array(img)
input_batch = transform(img_np)

with torch.no_grad():
    prediction = midas(input_batch)
    prediction = torch.nn.functional.interpolate(
        prediction.unsqueeze(1),
        size=img_np.shape[:2],
        mode="bicubic",
        align_corners=False,
    ).squeeze()

depth_map = prediction.numpy()

# save output
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].imshow(img)
axes[0].set_title("Original Image")
axes[0].axis("off")
axes[1].imshow(depth_map, cmap="plasma")
axes[1].set_title("Depth Map")
axes[1].axis("off")
plt.suptitle("Monocular Depth Estimation - PMW Day 1")
plt.tight_layout()
plt.savefig("depth_output.png")
plt.show()
print("Done! Output saved as depth_output.png")