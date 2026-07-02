# Method

- Year/Venue: 2025 / ICLR Poster
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Robotics, 3D Vision, Gaussian Splatting
- Paper link: ./2025/ICLR/2025_ICLR_3D-SPATIAL-MULTIMODAL-MEMORY/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- For rendered image quality on evaluation views (views not provided in training), we use common metrics (PSNR, SSIM, and LPIPS ) as Kerbl et al. .
- In compensate, we use point-based loss, where we sample 2000 points ranging from both predict and ground truth features for distance loss computation.
- The reference training features are identical for different methods.

## 원리적 동기
- For rendered image quality on evaluation views (views not provided in training), we use common metrics (PSNR, SSIM, and LPIPS ) as Kerbl et al. .

## 핵심 방법론
- For rendered image quality on evaluation views (views not provided in training), we use common metrics (PSNR, SSIM, and LPIPS ) as Kerbl et al. .
- In compensate, we use point-based loss, where we sample 2000 points ranging from both predict and ground truth features for distance loss computation.
- The reference training features are identical for different methods.
- Previous methods [26; 51] compute the patch-wise distance loss on the rendered features, this not only has a high volume of GPU memory consumption that hinders parallel training ...
- The extracted features are marked in orange in alignment with language representations optionally or continued to be the input of the language Encoder.
