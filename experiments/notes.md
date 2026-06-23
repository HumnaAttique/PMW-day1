# Experiment Notes - Monocular Depth Estimation

## What I ran
Used HuggingFace transformers pipeline with Depth-Anything-V2 model on Google Colab.

## Input
A simple synthetic image I created using Python (sky, cloud, tree, trunk).

## Output
A depth map showing estimated distances:
- Yellow/orange = closer to camera (the cloud)
- Purple/blue = further away (background sky)

## What I learned
- Monocular depth estimation works from just ONE image
- The model correctly identified the cloud as the closest object
- It runs completely free on Google Colab, no GPU needed locally
- For PreserveMy.World this could be used for quick depth previews
  of heritage site photos without needing expensive equipment

## What failed
First two attempts failed because Wikipedia image URLs were blocked.
Fixed by generating a synthetic image with Python's PIL library instead.

## Colab link
https://colab.research.google.com/drive/1P3j6eWjkyvGEE0HmwDNVKrcemNUdNrFF