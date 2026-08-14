# Method

- Year/Venue: 2026 / ICLR Poster
- Category: World Models, Safety, and Recovery
- Tags: Robotics, world model, robot manipulation, controllable generation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://ctrl-world.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- Third-view Camera WPE-Single-View WPE-Multiview IRASim-Single-View IRASim-Multiview Ctrl-World-Single-View Ctrl-World (ours) Computation-based PSNR ↑ SSIM ↑ Model-based LPIPS ↓ FID ↓ FVD ↓ 20.33 21.17 21.36 20.21 21.27 23.56 0.131 ...
- We evaluate our world model’s quality by generating 10-second trajectories.
- Given a randomly sampled initial frame, the model receives a 15-step action chunk (spanning over 1 second) in each interaction and generates for 10 rounds auto-regressively.

## 원리적 동기
- Third-view Camera WPE-Single-View WPE-Multiview IRASim-Single-View IRASim-Multiview Ctrl-World-Single-View Ctrl-World (ours) Computation-based PSNR ↑ SSIM ↑ Model-based LPIPS ↓ FID ↓ FVD ↓ 20.33 21.17 21.36 20.21 21.27 23.56 0.131 ...

## 핵심 방법론
- Third-view Camera WPE-Single-View WPE-Multiview IRASim-Single-View IRASim-Multiview Ctrl-World-Single-View Ctrl-World (ours) Computation-based PSNR ↑ SSIM ↑ Model-based LPIPS ↓ FID ↓ FVD ↓ 20.33 21.17 21.36 20.21 21.27 23.56 0.131 ...
- We evaluate our world model’s quality by generating 10-second trajectories.
- Given a randomly sampled initial frame, the model receives a 15-step action chunk (spanning over 1 second) in each interaction and generates for 10 rounds auto-regressively.
- The results are averaged over 256 clips.
- Ground Truth IRASim Ours Initial Obs Initial Obs Figure 3: Qualitative results on long-horizon rollouts from the validation set.
