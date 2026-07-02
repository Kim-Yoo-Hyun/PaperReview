# Method

- Year/Venue: 2024 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2024/CVPR/2024_CVPR_pixelSplat-3D-Gaussian-Splats-from-Image-Pairs-for-Scalabl/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We present pixelSplat, which brings the benefits of a primitive-based 3D representation—fast and memoryefficient rendering as well a Ours No Epipolar Encoder No Depth Encoding No Probabilistic Sampling ...
- We introduce pixelSplat, a feed-forward model that learns to reconstruct 3D radiance fields parameterized by 3D Gaussian primitives from pairs of images.
- To solve the problem of local minima that arises in primitive-based function regression, we introduced a novel parameterization of primitive location via a dense probability distribution and introduced ...

## 원리적 동기
- Introduction We investigate the problem of generalizable novel view synthesis from sparse image observations.
- To overcome local minima inherent to sparse and locally supported representations, we predict a dense probability distribution over 3D and sample Gaussian means from that probability distribution.
- We present pixelSplat, which brings the benefits of a primitive-based 3D representation—fast and memoryefficient rendering as well a Ours No Epipolar Encoder No Depth Encoding No Probabilistic Sampling ...

## 핵심 방법론
- To solve the problem of local minima that arises in primitive-based function regression, we introduced a novel parameterization of primitive location via a dense probability distribution and introduced ...
- An exciting avenue for future work is to leverage our model for generative modeling by combining it with diffusion models or to remove the need for camera poses ...
- Both our epipolar encoder and our probabilistic sampling scheme are essential for high-quality novel view synthesis.
- Ours No Epipolar Encoder No Depth Encoding No Probabilistic Sampling Plus Depth Regularization PSNR ↑ SSIM ↑ LPIPS ↓ 26.09 19.89 24.97 24.62 25.28 0.863 0.639 0.830 0.828 ...
