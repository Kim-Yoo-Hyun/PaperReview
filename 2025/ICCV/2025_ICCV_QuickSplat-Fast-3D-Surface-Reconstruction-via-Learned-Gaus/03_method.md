# Method

- Year/Venue: 2025 / ICCV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_QuickSplat-Fast-3D-Surface-Reconstruction-via-Learned-Gaus/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Both our method without post-training (“w/o opt”) and with additional SGD iterations (“w/ opt”) obtain better geometry while achieving orders of magnitude faster runtime. # Initializer Densifier (a) ...
- We introduce QuickSplat, which learns datadriven priors to generate dense initializations for 2D gaussian splatting optimization of large-scale indoor scenes.
- In con- trast, our method learns scene priors directly in the Gaussian representation space, allowing it to perform more robustly under such conditions.

## 원리적 동기
- In particular, achieving both high fidelity as well as efficient and fast reconstruction for large scenes remains a difficult problem.
- Surface reconstruction of large, real-world scenes is a key problem in computer vision and graphics.
- Both our method without post-training (“w/o opt”) and with additional SGD iterations (“w/ opt”) obtain better geometry while achieving orders of magnitude faster runtime. # Initializer Densifier (a) ...

## 핵심 방법론
- Both our method without post-training (“w/o opt”) and with additional SGD iterations (“w/ opt”) obtain better geometry while achieving orders of magnitude faster runtime. # Initializer Densifier (a) ...
- In con- trast, our method learns scene priors directly in the Gaussian representation space, allowing it to perform more robustly under such conditions.
- Our method more accurately models flat wall structures and objects details, while producing fewer floating geometry artifacts.
- Our method matches MonoSDF in accuracy while running substantially faster.
- Most importantly, via the learned initializer and densifieroptimizer, our method converges much faster.
