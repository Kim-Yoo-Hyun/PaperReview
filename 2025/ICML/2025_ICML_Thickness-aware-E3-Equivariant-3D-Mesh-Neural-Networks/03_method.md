# Method

- Year/Venue: 2025 / ICML poster
- Category: 3D Equivariance, Calibration, and Registration
- Tags: 3D reconstruction, equivariant, 3D Vision
- Paper link: ./2025/ICML/2025_ICML_Thickness-aware-E3-Equivariant-3D-Mesh-Neural-Networks/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this work, we propose a novel framework, the Thickness-aware E(3)-Equivariant 3D Mesh Neural Network (T-EMNN), that effectively integrates the thickness of 3D objects while maintaining the computational ...
- Additionally, we introduce data-driven coordinates that encode spatial information while preserving E(3)-equivariance or invariance properties, ensuring consistent and robust analysis.

## 원리적 동기
- This limitation arises from the disconnected nature of these surfaces and the absence of internal edge connections within the mesh.
- However, existing mesh-based methods focus solely on modeling the surfaces of 3D objects, overlooking their thickness.
- In this work, we propose a novel framework, the Thickness-aware E(3)-Equivariant 3D Mesh Neural Network (T-EMNN), that effectively integrates the thickness of 3D objects while maintaining the computational ...

## 핵심 방법론
- w/o thickness w/o dot product T-EMNN 0.92 0.90 0.88 0.085 0.18 Table 2.
- Ablation study on the thickness edge feature, fi,thick . w/o thick w thick 0.94 0.090 0.20 R2 ( ) 0.96 0.095 0.22 0.16 MAE ( ) 0.100 0.24 ...
- Comparison of baselines with x with our thickness edges.
- MGN inv EGNN EMNN RMSE 0.2156 (0.0064) 0.2191 (0.0143) 0.2132 (0.0046) MAE 0.0908 (0.0027) 0.0912 (0.0067) 0.0892 (0.0025) R2 0.9148 (0.0089) 0.9134 (0.0163) 0.9228 (0.0063) and their extension ...
- This capability transforms previously limited models into robust systems capable of handling transformations effectively, thereby greatly enhancing their ability to capture and represent spatial relationships. (a) Below the ...
