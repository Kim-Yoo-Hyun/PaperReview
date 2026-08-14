# Method

- Year/Venue: 2026 / ICLR Poster
- Category: Neural Scene Representations
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2026/ICLR/2026_ICLR_SurfSplat-Conquering-Feedforward-2D-Gaussian-Splatting-wit/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- PSNR↑ SSIM↑ LPIPS↓ PSNR↑ SSIM↑ LPIPS↓ PSNR↑ SSIM↑ LPIPS↓ PSNR↑ SSIM↑ LPIPS↓ pixelSplat 26.049 0.862 0.137 25.782 0.868 0.207 24.920 0.877 0.269 25.584 0.869 0.204 HiSplat 27.193 0.882 ...
- 256×256 (Standard) 512×512 (HRRC) 1024×1024 (HRRC) Average Method PSNR↑ SSIM↑ LPIPS↓ PSNR↑ SSIM↑ LPIPS↓ PSNR↑ SSIM↑ LPIPS↓ PSNR↑ SSIM↑ LPIPS↓ pixelSplat 28.284 0.842 0.146 27.687 0.848 0.243 26.462 ...
- We report quantitative comparison on the RE10K dataset in Table 1 and on the ACID dataset in Table 2.

## 원리적 동기
- PSNR↑ SSIM↑ LPIPS↓ PSNR↑ SSIM↑ LPIPS↓ PSNR↑ SSIM↑ LPIPS↓ PSNR↑ SSIM↑ LPIPS↓ pixelSplat 26.049 0.862 0.137 25.782 0.868 0.207 24.920 0.877 0.269 25.584 0.869 0.204 HiSplat 27.193 0.882 ...

## 핵심 방법론
- PSNR↑ SSIM↑ LPIPS↓ PSNR↑ SSIM↑ LPIPS↓ PSNR↑ SSIM↑ LPIPS↓ PSNR↑ SSIM↑ LPIPS↓ pixelSplat 26.049 0.862 0.137 25.782 0.868 0.207 24.920 0.877 0.269 25.584 0.869 0.204 HiSplat 27.193 0.882 ...
- 256×256 (Standard) 512×512 (HRRC) 1024×1024 (HRRC) Average Method PSNR↑ SSIM↑ LPIPS↓ PSNR↑ SSIM↑ LPIPS↓ PSNR↑ SSIM↑ LPIPS↓ PSNR↑ SSIM↑ LPIPS↓ pixelSplat 28.284 0.842 0.146 27.687 0.848 0.243 26.462 ...
- We report quantitative comparison on the RE10K dataset in Table 1 and on the ACID dataset in Table 2.
- Our proposed SurfSplat method consistently outperforms previous stateof-the-art methods across various metrics and datasets, especially under high-resolution rendering settings.
- As shown in Figure 4, we visualize the predicted 3D scenes rendered into both RGB and depth maps at the original, ×2, and ×4 resolutions.
