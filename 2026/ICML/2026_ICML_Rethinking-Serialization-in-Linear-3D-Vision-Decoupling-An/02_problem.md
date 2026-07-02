# Problem

- Year/Venue: 2026 / ICML
- Category: 3D Semantic Understanding and Alignment
- Tags: semantic, alignment, 3D Vision
- Paper link: ./2026/ICML/2026_ICML_Rethinking-Serialization-in-Linear-3D-Vision-Decoupling-An/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Existing SSM/mamba methods force 3D point clouds into 1D sequences (top), introducing artificial ordering that disrupts spatial continuity.
- Introduction Effective 3D point cloud understanding must reconcile local anisotropic geometry with global isotropic semantics, but the irregular and unordered nature of point sets makes this difficult.
- GISA is configured according to dataset-level geometric density: dense-scene datasets use Identity Mode to avoid additional geometry-driven re-serialization, whereas sparseobject datasets use Morton serialization to provide a lightweight ...

## 해결하려는 문제
- On ScanNetV2, our model achieves 78.52% mIoU, surpassing PTv3 (77.5%) without pre-training, with only 12.2M parameters and 37G FLOPs.
- We propose AnIsoNet, a framework that decouples anisotropic geometry from isotropic semantics via two dedicated modules: Local Anisotropy Geometric Modeling (LAGM) and Global Isotropy Semantic Aggregation (GISA).
- Architectural comparison of our method with serialization-based methods.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
