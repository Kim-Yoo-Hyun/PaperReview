# Method

- Year/Venue: 2026 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_DualSplat-Robust-3D-Gaussian-Splatting-via-Pseudo-Mask-Boo/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In the lower example, our method reduces erroneous background occlusion more effectively and reconstructs a cleaner static layout around the object and wall boundary.
- We observe that transients, which appear in only a subset of views, often manifest as incomplete fragments during conservative initial training.
- We inherit RobustSplat’s progressive MLP training schedule and other hyperparameters in Stage II unless otherwise stated.

## 원리적 동기
- We address this challenge with DualSplat, a Failure-toPrior framework that converts first-pass reconstruction failures into explicit priors for a second reconstruction stage.
- Existing methods face a circular dependency: accurate transient detection requires a well-reconstructed static scene, while clean reconstruction itself depends on reliable transient masks.
- In the lower example, our method reduces erroneous background occlusion more effectively and reconstructs a cleaner static layout around the object and wall boundary.

## 핵심 방법론
- In the lower example, our method reduces erroneous background occlusion more effectively and reconstructs a cleaner static layout around the object and wall boundary.
- We inherit RobustSplat’s progressive MLP training schedule and other hyperparameters in Stage II unless otherwise stated.
- We compared DualSplat with recent 3DGSbased transient-suppression methods, including SpotLessSplats , WildGaussians , DeSplat , DeGauss and RobustSplat .
- PSNR 3DGS WildGaussians DeSplat SpotLessSplats DeGauss RobustSplat 3DGS with pseudo-masks Ours GT 18.92 20.73 20.12 21.12 22.12 21.47 21.01 21.86 Low Occlusion Mountain Fountain SSIM LPIPS PSNR SSIM ...
- Method PSNR Android SSIM LPIPS PSNR Crab1 SSIM LPIPS PSNR Crab2 SSIM LPIPS PSNR Statue SSIM LPIPS PSNR Yoda SSIM LPIPS PSNR Mean SSIM LPIPS 3DGS WildGaussians DeSplat ...
