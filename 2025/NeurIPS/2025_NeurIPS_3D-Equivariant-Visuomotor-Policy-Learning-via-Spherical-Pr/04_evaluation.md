# Evaluation

- Year/Venue: 2025 / NeurIPS Spotlight
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, 3D Vision, equivariant
- Paper link: ./2025/NeurIPS/2025_NeurIPS_3D-Equivariant-Visuomotor-Policy-Learning-via-Spherical-Pr/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet

## Metrics
- mAP
- success rate

## Evaluation Protocol and Results
- We compare against three strong baselines: (1) Diffusion Policy : A diffusion-based policy without any equivariance, serving as the primary reference. (2) EquiDiff (modified) : Designed for fixed-camera ...
- Baselines Our experiments aim to validate the benefits of explicitly modeling equivariance in eyein-hand visuomotor policies.
- 5.1 Simulation Experiment Setting We evaluate ISP on twelve robotic manipulation tasks from the MimicGen benchmark , which is widely used in previous work on closed-loop policy learning ...
- To ensure a fair comparison, all experiments in the following sections, including ablations and method variants, consistently apply SO(2) data augmentation during training by rotating the end-effector pose ...
- We perform extensive experiments in both simulation and the real world that demonstrate that our method consistently outperforms strong baselines in terms of both performance and sample efficiency.
- We compare against three strong baselines: (1) Diffusion Policy : A diffusion-based policy without any equivariance, serving as the primary reference. (2) EquiDiff (modified) : Designed for fixed-camera ...

## Baselines
- We compare against three strong baselines: (1) Diffusion Policy : A diffusion-based policy without any equivariance, serving as the primary reference. (2) EquiDiff (modified) : Designed for fixed-camera ...
- To capture sufficient scene context, we enlarge the camera’s field of view (FOV) to approximate a typical fisheye camera setup and re-generate the enlarged FOV observations using the ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
