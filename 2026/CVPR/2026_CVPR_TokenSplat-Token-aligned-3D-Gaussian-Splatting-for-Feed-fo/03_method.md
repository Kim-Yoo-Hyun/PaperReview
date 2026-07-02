# Method

- Year/Venue: 2026 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, geometry, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_TokenSplat-Token-aligned-3D-Gaussian-Splatting-for-Feed-fo/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We present TokenSplat, a feed-forward framework for joint 3D Gaussian reconstruction and camera pose estimation from unposed multi-view images.
- This maintains clean factorization within a feed-forward architecture, enabling coherent reconstruction and stable pose estimation without iterative refinement.
- Recent feed-forward variants alleviate this by predicting 3D Gaussians directly from input images, but their applicability remains constrained by the requirement for accurate camera poses.

## 원리적 동기
- Furthermore, most existing pose-free methods rely on pixel-aligned 3DGS heads that generate Gaussians at pixellevel gra
- Pose estimation via structurefrom-motion (SfM) is computationally expensive and prone to failure in challenging environments, significantly impacting reconstruction stability.
- We present TokenSplat, a feed-forward framework for joint 3D Gaussian reconstruction and camera pose estimation from unposed multi-view images.

## 핵심 방법론
- Quantitative results of NVS on ScanNet under varying numbers of views.
- The best and second-best values are highlighted.
- Method Poserequired Posefree MVSplat FreeSplat NoPoSplat VicaSplat SPFSplat Anysplat∗ Anysplat Ours PSNR↑ 24.98 25.63 25.55 24.54 25.85 19.84 15.05 26.57
