# Method

- Year/Venue: 2026 / ICLR Poster
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: sensor fusion, LiDAR, 3D Vision
- Paper link: ./2026/ICLR/2026_ICLR_SimULi-Real-Time-LiDAR-and-Camera-Simulation-with-Unscente/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We minimize the K-distance loss at each training iteration, and update the camera-to-LiDAR assignments every 1000 iterations.
- We define a nearest-neighbor anchoring loss on Gaussian means: n 1 !
- Lanchor = ↔µi ↓ N N (µi , Gl )↔2 , n N N (µ, G) = argminµ→ ↓G ↔µ ↓ µ↗ ↔2 i↓Gc (5) Since running full ...

## 원리적 동기
- We minimize the K-distance loss at each training iteration, and update the camera-to-LiDAR assignments every 1000 iterations.

## 핵심 방법론
- We minimize the K-distance loss at each training iteration, and update the camera-to-LiDAR assignments every 1000 iterations.
- We define a nearest-neighbor anchoring loss on Gaussian means: n 1 !
- Lanchor = ↔µi ↓ N N (µi , Gl )↔2 , n N N (µ, G) = argminµ→ ↓G ↔µ ↓ µ↗ ↔2 i↓Gc (5) Since running full ...
- Existing methods encode camera and LiDAR data into a single NeRF (Yang et al., 2023b; Tonderski et al., 2024) or set of 3D Gaussian particles (Hess et al., ...
