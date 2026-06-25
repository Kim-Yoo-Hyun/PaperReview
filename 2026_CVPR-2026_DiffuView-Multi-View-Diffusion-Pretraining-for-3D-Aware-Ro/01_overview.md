# DiffuView: Multi-View Diffusion Pretraining for 3D Aware Robotic Manipulation

- Year/Venue: 2026 / CVPR 2026
- Category: Equivariance, Diffusion, and 3D Action
- Tags: Diffusion, 3D manipulation, Robotics
- Authors: Kaizhao Zhang, Tian Niu, Tianyu Liu, Chenen Guo, Zijun Xu, Qingda Hu, Wenchao Ding ; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2026, pp. 23601-23611
- Paper: https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_DiffuView_Multi-View_Diffusion_Pretraining_for_3D_Aware_Robotic_Manipulation_CVPR_2026_paper.html
- PDF status: downloaded
- GitHub/Project: not identified from primary page

## Problem
생성 모델 또는 policy 모델이 3D 구조와 물리 제약을 보존하지 못하면 로봇 실행이나 3D 장면 생성에서 일관성이 깨진다.

## Core Idea
핵심은 diffusion score/denoising process를 action, 3D generation, 또는 structured scene representation에 적용하면서 geometry prior를 넣는 것이다.

## Paper-Specific Cues
- Topic cue: Robotic manipulation from visual observations remains challenging due to the lack of 3D consistent representations that can generalize across diverse viewpoints and sensor configurations.
- Method cue: In this paper, we introduce DiffuView, a novel framework that learns unified 3D aware representations through multi-view diffusion pretraining and deploys them for imitation ...
- Result cue: Crucially, while multi-view diffusion models have recently shown tremendous success in 3D aware generative synthesis, their powerful representations offer a promising direction for achieving ...

## Input / Output
Input: language instruction plus RGB/RGB-D/point-cloud robot observations. Output: action tokens, poses, trajectories, constraints, or policy decisions.

## Main Claims
- 논문은 `diffusion-based generation or policy learning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다.

## Contribution
- diffusion-based generation or policy learning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Diffusion, 3D manipulation, Robotics.
- 초록에서 확인되는 주요 cue: Robotic, Existing, Crucially, DiffuView, Specifically, The, MetaWorld, Libero.
