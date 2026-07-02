# Method

- Year/Venue: 2026 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, geometry, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_E2EGS-Event-to-Edge-Gaussian-Splatting-for-Pose-Free-3D-Re/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We present E2EGS, a pose-free framework operating solely on event streams.
- Edge-guided 3D reconstruction To leverage detected edges during reconstruction, we introduce an edge-guided loss that spatially weights the reconstruction error based on edge confidence.
- We compare our E2EGS with baselines to validate the effectiveness of our approach for both 3D reconstruction and trajectory estimation.

## 원리적 동기
- However, existing event-based NVS methods either assume known poses or rely on depth estimation models that are bounded by their initial observations, failing to generalize as the camera ...
- This assumption makes them vulnerable to common real-world challenges, such as motion blur and adverse lighting conditions that frequently occur during rapid camera movements or in low-light environments.
- We present E2EGS, a pose-free framework operating solely on event streams.

## 핵심 방법론
- Edge-guided 3D reconstruction To leverage detected edges during reconstruction, we introduce an edge-guided loss that spatially weights the reconstruction error based on edge confidence.
- We compare our E2EGS with baselines to validate the effectiveness of our approach for both 3D reconstruction and trajectory estimation.
- For synthetic evaluation, we use IncEventGS’s event data from Replica scenes (room0, room2, office0, office2, and office3).
- For real-world evaluation, we use TUM-VIE sequences (1d, 3d, 6dof, desk, and desk2). (4) where K is the camera’s intrinsic matrix and K−1 [xi , 1]T represents the ...
- For camera pose estimation, we use absolute trajectory error (ATE), which measures the root-mean-square error (RMSE) of the aligned trajectory after SE(3) alignment using the EVO toolbox .
