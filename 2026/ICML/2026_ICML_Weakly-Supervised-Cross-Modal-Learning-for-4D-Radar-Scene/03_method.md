# Method

- Year/Venue: 2026 / ICML
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: sensor fusion, LiDAR, 3D Vision
- Paper link: ./2026/ICML/2026_ICML_Weakly-Supervised-Cross-Modal-Learning-for-4D-Radar-Scene/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To overcome these limitations, we propose a task-specific iterative framework for weakly supervised radar scene flow learning, using only images and odometry for auxiliary supervision during training.
- For a fair comparison with the baselines, we use their official loss configuration and hyperparameter settings for network retraining on the VoD radar scene flow dataset.
- To address these limitations and achieve high-accuracy flow estimation on challenging 4D radar data, we propose IterFlow, a task-specific iterative network designed to refine scene flow estimation progressively ...

## 원리적 동기
- To overcome the limitation of expensive 3D scene flow annotations, runtime optimization and self-supervised methods have witnessed remarkable progress in recent years.
- To address this problem, we introduce an instance-level flow smoothness loss Lis .
- To overcome these limitations, we propose a task-specific iterative framework for weakly supervised radar scene flow learning, using only images and odometry for auxiliary supervision during training.

## 핵심 방법론
- For a fair comparison with the baselines, we use their official loss configuration and hyperparameter settings for network retraining on the VoD radar scene flow dataset.
- Following (Ding et al., 2022; 2023; Zhai et al., 2025; Wu et al., 2025), we use standard metrics for evaluation: 1) EPE: average 3D end-point-error measures the L2 ...
- Since the VoD dataset does not provide ready-made scene flow ground truth, we adopt the commonly used preprocessing methods to generate scene flow labels from annotated 3D tracking ...
- Quantitative Evaluation on Network Architecture and Loss Scalability on VoD validation set.
- Scene flow is updated for K = 12 iterations in both training and evaluation stage3 .
