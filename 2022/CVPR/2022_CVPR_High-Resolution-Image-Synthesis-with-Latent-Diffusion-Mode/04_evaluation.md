# Evaluation

- Year/Venue: 2022 / CVPR
- Category: Foundations: Diffusion and Generative Models
- Tags: Diffusion, latent representation, generation
- Paper link: ./2022/CVPR/2022_CVPR_High-Resolution-Image-Synthesis-with-Latent-Diffusion-Mode/paper.pdf
- Code/Project: https://github.com/CompVis/latent-diffusion
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet
- COCO

## Metrics
- accuracy
- AP
- mAP
- PSNR
- SSIM
- LPIPS
- SR

## Evaluation Protocol and Results
- Input By decomposing the image formation process into a sequential application of denoising autoencoders, diffusion models (DMs) achieve state-of-the-art synthesis results on image data and beyond.
- Our latent diffusion models (LDMs) achieve new state-of-the-art scores for image inpainting and class-conditional image synthesis and highly competitive performance on various tasks, including text-to-image synthesis, unconditional image ...

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
