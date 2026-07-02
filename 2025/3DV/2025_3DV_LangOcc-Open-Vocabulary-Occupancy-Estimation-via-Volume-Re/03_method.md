# Method

- Year/Venue: 2025 / 3DV
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: sensor fusion, LiDAR, 3D Vision
- Paper link: ./2025/3DV/2025_3DV_LangOcc-Open-Vocabulary-Occupancy-Estimation-via-Volume-Re/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this work we present a novel approach for open vocabulary occupancy estimation called LangOcc, that is trained only via camera images, and can detect arbitrary semantics via ...
- Method OccFlowNet CTF-Occ LangOcc (Full) LangOcc (Reduced) Mode L 3D C C mIoU 26.14 28.53 10.71 11.84 pensive manual labelling and additional sensor data, while our method is ...
- We use the same vocabulary as in Sec.

## 원리적 동기
- However, most existing camera-based methods rely on costly 3D voxel labels or LiDAR scans for training, limiting their practicality and scalability.
- However, most existing 3D occupancy estimation methods rely on expensive 3D ground-truth labels .
- In this work we present a novel approach for open vocabulary occupancy estimation called LangOcc, that is trained only via camera images, and can detect arbitrary semantics via ...

## 핵심 방법론
- Method OccFlowNet CTF-Occ LangOcc (Full) LangOcc (Reduced) Mode L 3D C C mIoU 26.14 28.53 10.71 11.84 pensive manual labelling and additional sensor data, while our method is ...
- We use the same vocabulary as in Sec.
- Our proposed supervision method leads to a significantly better IoU score of 51.59, which confirms that the feature distillation loss provides a better supervision signal for the scene ...
- Training our model with this RGB supervision leads to a geometric IoU score of 41.10.
- Conclusion In this paper, we have proposed a novel model that enables a generic open vocabulary scene representation and a weakly-supervised training mechanism that requires only images as ...
