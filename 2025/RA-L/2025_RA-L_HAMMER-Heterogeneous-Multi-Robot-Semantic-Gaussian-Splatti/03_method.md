# Method

- Year/Venue: 2025 / RA-L
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Robotics, Gaussian Splatting, semantic
- Paper link: ./2025/RA-L/2025_RA-L_HAMMER-Heterogeneous-Multi-Robot-Semantic-Gaussian-Splatti/paper.pdf
- Code/Project: https://hammer-project.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To that end, we propose HAMMER, a server-based multi-robot Gaussian Splatting method that leverages ROS communication infrastructure to generate 3D, metric-semantic maps from asynchronous robot data-streams.
- HAMMER consists of (i) a one-time frame alignment module that transforms local SLAM poses and image data into a global frame and requires no prior relative pose knowledge, ...
- —3D Gaussian Splatting offers expressive scene reconstruction and can model a broad range of visual, geometric, and semantic information.

## 원리적 동기
- However, efficient real-time map reconstruction with data streamed from multiple robots and devices remains a challenge.
- To that end, we propose HAMMER, a server-based multi-robot Gaussian Splatting method that leverages ROS communication infrastructure to generate 3D, metric-semantic maps from asynchronous robot data-streams.

## 핵심 방법론
- CP-SLAM Metrics Off-0 Apt-0 Apt-1 Apt-2 Avg.
- PSNR [dB] ↑ 28.56 26.12 12.16 23.98 22.71 SSIM ↑ 0.87 0.79 0.31 0.81 0.69 LPIPS ↓ 0.29 0.41 0.97 0.39 0.51 Depth L1 [cm] ↓ 2.74 19.93 ...
