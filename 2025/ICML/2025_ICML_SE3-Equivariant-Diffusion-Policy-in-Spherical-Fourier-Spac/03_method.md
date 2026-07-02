# Method

- Year/Venue: 2025 / ICML Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, Diffusion, Imitation Learning, equivariant
- Paper link: ./2025/ICML/2025_ICML_SE3-Equivariant-Diffusion-Policy-in-Spherical-Fourier-Spac/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We propose Spherical Diffusion Policy (SDP), a Fourier space SE(3) equivariant method that automatically adapts to changes in the scene.
- To address this issue, we propose Spherical Diffusion Policy (SDP), an SE(3) equivariant diffusion policy that adapts trajectories according to 3D transformations of the scene.
- Lastly, we propose a spherical denoising temporal U-net that achieves spatiotemporal equivariance with computational efficiency.

## 원리적 동기
- Diffusion Policy may struggle to attain robust 3D generalization without training on a large amount of costly human demonstrations to exhaust the possible 3D arrangements of the scene.
- We propose Spherical Diffusion Policy (SDP), a Fourier space SE(3) equivariant method that automatically adapts to changes in the scene.

## 핵심 방법론
- Evaluation success rate on 12 MimicGen tasks with SE(2) initialization.
- We train all the baselines with 100 demonstrations.
- SDP demonstrates the best performance on 10 tasks.
- Stack Three D1 Threading D2 Coffee D2 Hammer Cleanup D1 Mug Cleanup D1 Pick Place D0 Coffee Preparation D1 Average Success Rate Method Ctrl Obs Rel PCD 100 ...
