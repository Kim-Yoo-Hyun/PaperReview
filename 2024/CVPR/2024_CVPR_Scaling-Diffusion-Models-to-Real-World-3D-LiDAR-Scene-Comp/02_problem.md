# Problem

- Year/Venue: 2024 / CVPR
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: sensor fusion, LiDAR, Diffusion, Generation, 3D Vision
- Paper link: ./2024/CVPR/2024_CVPR_Scaling-Diffusion-Models-to-Real-World-3D-LiDAR-Scene-Comp/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Previous works used diffusion models over range images extracted from LiDAR data, directly applying image-based diffusion methods.
- Such systems rely on the data collected by the sensors installed on the vehicle to perceive the environment but fail to deduce areas only partially observable by the ...
- 3D LiDAR sensors are commonly used to collect sparse 3D point clouds from the scene.

## 해결하려는 문제
- Given the promising results of recent diffusion models as generative models for images, we propose extending them to achieve scene completion from a single 3D LiDAR scan.
- Our experimental evaluation shows that our method can complete the scene given a single LiDAR scan as input, producing a scene with more details compared to state-of-the-art scene ...
- Together with our approach, we propose a regularization loss to stabilize the noise predicted during the denoising process.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
