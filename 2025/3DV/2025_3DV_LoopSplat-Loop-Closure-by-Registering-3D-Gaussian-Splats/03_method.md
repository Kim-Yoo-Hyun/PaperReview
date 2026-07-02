# Method

- Year/Venue: 2025 / 3DV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D Vision
- Paper link: ./2025/3DV/2025_3DV_LoopSplat-Loop-Closure-by-Registering-3D-Gaussian-Splats/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To this end, we propose LoopSplat, which takes RGB-D images as input and performs dense mapping with 3DGS submaps and frame-to-model tracking.
- We use the same RGB-D sequences as .
- We use five DSLR-captured sequences where poses are estimated with COLMAP and refined with the help of laser scans.

## 원리적 동기
- However, existing 3DGS-based methods fail to address the global consistency of the scene via loop closure and/or global bundle adjustment.
- Existing methods can be split into two categories, decoupled and coupled, where decoupled methods do not leverage the dense map for the tracking task, while the coupled methods ...
- To this end, we propose LoopSplat, which takes RGB-D images as input and performs dense mapping with 3DGS submaps and frame-to-model tracking.

## 핵심 방법론
- We use the same RGB-D sequences as .
- We use five DSLR-captured sequences where poses are estimated with COLMAP and refined with the help of laser scans.
- PGO is triggered after loop detection and we use a robust formulation based on line processes .
- For each submap, we update camera poses, the Gaussian means, and covariances Loop Closure Detection.
- Tj ← Tci Tj , µi ← Rci µSi + tci , Σi ← Rci ΣSi RTci (8) . (9) Here, µi and Σi represent the sets of ...
