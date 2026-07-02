# Method

- Year/Venue: 2025 / CVPR
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: sensor fusion, LiDAR, Diffusion, Generation, 3D Vision
- Paper link: ./2025/CVPR/2025_CVPR_V2X-R-Cooperative-LiDAR-4D-Radar-Fusion-with-Denoising-Dif/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Experimental Details and Metrics We used 8,084/829/3,166 frames for training/ validation/ testing in our V2X-R dataset, ensuring there is no overlap in the intersection of the training/validation/testing sets.
- Subsequently, we propose a novel cooperative LiDAR-4D radar fusion pipeline for 3D object detection and implement it with multiple fusion strategies.
- To this end, we present V2X-R, the first simulated V2X dataset incorporating LiDAR, camera, and 4D radar modalities.

## 원리적 동기
- Weather-robust 4D radar, with Doppler velocity and additional geometric information, offers a promising solution to this challenge.
- Introduction Outdoor environments, however, present complex and dynamic challenges, including various occlusions and weather conditions .
- Experimental Details and Metrics We used 8,084/829/3,166 frames for training/ validation/ testing in our V2X-R dataset, ensuring there is no overlap in the intersection of the training/validation/testing sets.

## 핵심 방법론
- Experimental Details and Metrics We used 8,084/829/3,166 frames for training/ validation/ testing in our V2X-R dataset, ensuring there is no overlap in the intersection of the training/validation/testing sets.
- We use Adam optimizer with lr = 1e-3, β1 = 0.9, β2 = 0.999.
- Loss Function Method † PFA-Net RTNH† V2XViT‡ AttFuse‡ Where2comm‡ SCOPE‡ CoBEVT‡ CoAlign‡ AdaFusion‡ SICP‡ We trained models with our MDD by the following losses: \label {eq_all} \mathcal {L}_{all} ...
- We first extend the single-agent 4D radar-based FPA-Net and RTNH to the cooperative 4D radar-based method through self-attention agent fusion in AttFuse , marked 5.3.
