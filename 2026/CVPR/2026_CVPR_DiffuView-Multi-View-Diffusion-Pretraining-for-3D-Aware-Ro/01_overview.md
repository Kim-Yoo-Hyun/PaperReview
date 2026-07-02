# DiffuView: Multi-View Diffusion Pretraining for 3D Aware Robotic Manipulation

- Year/Venue: 2026 / CVPR
- Category: Equivariance, Diffusion, and 3D Action
- Tags: Diffusion, 3D manipulation, Robotics
- Paper link: ./2026/CVPR/2026_CVPR_DiffuView-Multi-View-Diffusion-Pretraining-for-3D-Aware-Ro/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Existing methods, primarily based on masked autoencoders or neural scene representations, struggle to capture robust view correspondences due to a lack of global 3D consistency or the requirement ...
- To overcome this data bottleneck, recent studies have turned to leveraging advances in computer visio
- Robotic manipulation from visual observations remains challenging due to the lack of 3D consistent representations that can generalize across diverse viewpoints and sensor configurations.

## Core Idea
- In this paper, we introduce DiffuView, a novel framework that learns unified 3D aware representations through multi-view diffusion pretraining and deploys them for imitation learning.
- Comparison of visual representation learning paradigms for robotic manipulation. (a) MAE based methods learn visual representations by reconstructing masked regions from observations. (b) 3D reconstruction methods lift 2D ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments in both simulation and realworld scenarios demonstrate that DiffuView achieves superior generalization, improving success rates under viewpoint shifts by nearly 20% compared with existing methods.
- Quantitative results on MetaWorld Benchmark.
- We evaluate DiffuView on two challenging benchmarks, MetaWorld and Libero.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- In this paper, we introduce DiffuView, a novel framework that learns unified 3D aware representations through multi-view diffusion pretraining and deploys them for imitation learning.
- Extensive experiments in both simulation and realworld scenarios demonstrate that DiffuView achieves superior generalization, improving success rates under viewpoint shifts by nearly 20% compared with existing methods.
- Comparison of visual representation learning paradigms for robotic manipulation. (a) MAE based methods learn visual representations by reconstructing masked regions from observations. (b) 3D reconstruction methods lift 2D ...

## Abstract Cue
- Robotic manipulation from visual observations remains challenging due to the lack of 3D consistent representations that can generalize across diverse viewpoints and sensor configurations.
