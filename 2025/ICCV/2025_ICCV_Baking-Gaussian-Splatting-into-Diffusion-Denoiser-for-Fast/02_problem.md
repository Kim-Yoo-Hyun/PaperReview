# Problem

- Year/Venue: 2025 / ICCV
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: 3D Vision, Gaussian Splatting, Diffusion
- Paper link: ./2025/ICCV/2025_ICCV_Baking-Gaussian-Splatting-into-Diffusion-Denoiser-for-Fast/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Existing feedforward image-to-3D methods mainly rely on 2D multi-view diffusion models that cannot guarantee 3D consistency.
- Existing feedforward image-to-3D methods are mainly two-stage .

## 해결하려는 문제
- Experiments show that DiffusionGS yields improvements of 2.20 dB/23.25 and 1.34 dB/19.16 in PSNR/FID for objects and scenes than the state-of-the-art methods, without depth estimator.
- Single-view object generation results of our method on GSO , wild images, and text-to-images prompted by stable diffusion or FLUX.
- Plus, to improve the capability and generality of DiffusionGS, we scale up 3D training data by developing a scene-object mixed training strategy.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
