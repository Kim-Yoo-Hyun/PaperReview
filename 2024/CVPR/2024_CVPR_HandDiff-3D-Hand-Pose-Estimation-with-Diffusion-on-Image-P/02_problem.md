# Problem

- Year/Venue: 2024 / CVPR
- Category: 3D Generative Modeling and Diffusion
- Tags: geometry, Diffusion, Generation, point cloud, 3D Vision
- Paper link: ./2024/CVPR/2024_CVPR_HandDiff-3D-Hand-Pose-Estimation-with-Diffusion-on-Image-P/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Essentially, the 3D hand pose estimation can be regarded as a 3D point subset generative problem conditioned on input frames.
- In recent years, significant progress has been made in the field of 3D hand pose estimation by applying deep learning techniques and using low-cost depth cameras.

## 해결하려는 문제
- Experimental results demonstrate that the proposed HandDiff significantly outperforms the existing approaches on four challenging hand pose benchmark datasets.
- However, directly deploying the existing diffusion models to solve hand pose estimation is non-trivial, since they cannot achieve the complex permutation mapping and precise localization.
- Thanks to the recent significant progress on diffusion-based generative models, hand pose estimation can also benefit from the diffusion model to estimate keypoint locations with high quality.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
