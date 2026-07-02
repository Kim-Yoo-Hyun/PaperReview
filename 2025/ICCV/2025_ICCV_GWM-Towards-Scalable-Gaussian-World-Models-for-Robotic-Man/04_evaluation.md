# Evaluation

- Year/Venue: 2025 / ICCV
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Gaussian Splatting, world model, Robotics
- Paper link: ./2025/ICCV/2025_ICCV_GWM-Towards-Scalable-Gaussian-World-Models-for-Robotic-Man/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- accuracy
- mAP
- Chamfer
- PSNR
- SSIM
- LPIPS
- SR
- success rate

## Evaluation Protocol and Results
- Both simulated and real-world experiments depict that GWM can precisely predict future scenes conditioned on diverse robot actions, and can be further utilized to train policies that outperform ...
- To achieve real-time training and inference, we design a 3D Gaussian Variational Autoencoder (VAE) to extract latent representations from 3D Gaussians, allowing the diffusion-based world model to operate ...

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
