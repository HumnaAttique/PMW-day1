# 3D Reconstruction Methods — Research Notes

## 1. COLMAP / Structure-from-Motion (SfM)
Input: multiple photos of the same object from different angles
Output: 3D point cloud + estimated camera positions
Hardware: works on a regular PC, GPU speeds it up
Difficulty: medium — has a GUI which makes it beginner friendly
PMW use case: rebuilding historical buildings from tourist photos

## 2. NeRF (Neural Radiance Fields)
Input: many photos with known camera angles
Output: photorealistic 3D scene viewable from any angle
Hardware: needs a strong GPU (Google Colab works)
Difficulty: hard — lots of setup involved
PMW use case: immersive 3D views of heritage sites

## 3. Gaussian Splatting
Input: photos (fewer needed than NeRF)
Output: fast high-quality 3D scenes
Hardware: strong GPU recommended
Difficulty: medium-hard
PMW use case: real-time 3D rendering of cultural sites

## 4. Monocular Depth Estimation
Input: a single photo
Output: depth map showing how far things are
Hardware: runs on regular PC or free Colab
Difficulty: easy — lots of pre-built tools available
PMW use case: quick depth previews from any single heritage photo

## 5. Multi-View Stereo (MVS)
Input: multiple calibrated photos
Output: dense 3D mesh
Hardware: regular PC
Difficulty: medium
PMW use case: detailed 3D models of artifacts and sites

## My conclusion
Starting with monocular depth estimation this week because it only
needs one photo and runs free on Colab — good entry point before
moving to heavier methods like NeRF or Gaussian Splatting.