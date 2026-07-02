# Method

- Year/Venue: 2025 / NeurIPS poster
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: Gaussian Splatting, sensor fusion, LiDAR, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_ODG-Occupancy-Prediction-Using-Dual-Gaussians/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this section, we present our proposed 3D occupancy approach, ODG, in which we adopt a dual Gaussian query design to capture the respective dynamic and static elements ...
- In this paper, we present ODG, a hierarchical dual sparse Gaussian representation to effectively capture complex scene dynamics.
- Finally, we describe the training objectives in Sec.

## 원리적 동기
- But existing methods utilize a single transformer which can only handle a smaller number of Gaussians.
- To overcome such drawbacks, another line of research formulate the task of 3D occupancy as direct set prediction, effectively predicting 3D occupancy as set of sparse points from ...
- In this section, we present our proposed 3D occupancy approach, ODG, in which we adopt a dual Gaussian query design to capture the respective dynamic and static elements ...

## 핵심 방법론
- In this section, we present our proposed 3D occupancy approach, ODG, in which we adopt a dual Gaussian query design to capture the respective dynamic and static elements ...
- Finally, we describe the training objectives in Sec.
- Formally, 3D occupancy prediction can be defined as O = G(V), V = F (I), (1) where F (·) consists of an image backbone that extract multi-camera features ...
- To enable an sufficient number of Gaussians, unlike previous methods which only utilizes a single transformer that maintains the same number of points over layers, we predict Gaussians ...
- 3.3) and leverage attention to enable feature interaction between the dual queries (Sec.
