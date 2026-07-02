# Method

- Year/Venue: 2026 / ICML
- Category: 3D Semantic Understanding and Alignment
- Tags: semantic, alignment, 3D Vision
- Paper link: ./2026/ICML/2026_ICML_Rethinking-Serialization-in-Linear-3D-Vision-Decoupling-An/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We propose AnIsoNet, a framework that decouples anisotropic geometry from isotropic semantics via two dedicated modules: Local Anisotropy Geometric Modeling (LAGM) and Global Isotropy Semantic Aggregation (GISA).
- Sonata (dec.) reaches 79.1%, which is 0.6% higher than our result, but it uses quadratic decoder attention together with large-scale external pre-training, whereas our model is trained entirely ...
- Architectural comparison of our method with serialization-based methods.

## 원리적 동기
- Existing SSM/mamba methods force 3D point clouds into 1D sequences (top), introducing artificial ordering that disrupts spatial continuity.
- Introduction Effective 3D point cloud understanding must reconcile local anisotropic geometry with global isotropic semantics, but the irregular and unordered nature of point sets makes this difficult.
- We propose AnIsoNet, a framework that decouples anisotropic geometry from isotropic semantics via two dedicated modules: Local Anisotropy Geometric Modeling (LAGM) and Global Isotropy Semantic Aggregation (GISA).

## 핵심 방법론
- Sonata (dec.) reaches 79.1%, which is 0.6% higher than our result, but it uses quadratic decoder attention together with large-scale external pre-training, whereas our model is trained entirely ...
- Underline denotes second-best without pre-training.
- Methods marked with † use external pre-training data. ∗ Best among methods without pre-training.
- Compared with PTv3, it is 1.0% higher on the validation split without external pre-training.
- Our encoder follows DeLA (Chen et al., 2023) with ellipsoidal spectral encoding.
