# Method

- Year/Venue: 2019 / ICCV
- Category: 3D Equivariance, Calibration, and Registration
- Tags: 3D Vision, registration, 3D geometry, representation
- Paper link: ./2019/ICCV/2019_ICCV_Fully-Convolutional-Geometric-Features/paper.pdf
- Code/Project: https://github.com/chrischoy/FCGF
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this work, we present fully-convolutional geometric features, computed in a single pass by a 3D fully-convolutional network.
- We experimentally validate our approach on both indoor and outdoor datasets.
- If we use a 2D analogy, extracting 3D 3DMatch FMR STD with Rot.

## 원리적 동기
- Existing learning-based features rely on low-level geometric characteristics as input: e.g., angular deviation , point distributions , or volumetric distance functions .
- This process is computationally expensive and features are extracted only at downsampled interest points, thus lowering the spatial resolution for subsequent registration steps.
- In this work, we present fully-convolutional geometric features, computed in a single pass by a 3D fully-convolutional network.

## 핵심 방법론
- HN / RT Spin SHOT FPFH USC PointNet CGF 3DMatch Folding PPFNet PPF-Fold DirectReg CapsuleNet PerfectMatch 0.227 0.238 0.359 0.400 0.471 0.582 0.596 0.613 0.623 0.718 0.746 0.807 ...
- FMR and STD indicate the Feature Match Recall and its standard deviation.
- Dim. indicates feature dimensionality and Time is in milliseconds consumed per feature.
