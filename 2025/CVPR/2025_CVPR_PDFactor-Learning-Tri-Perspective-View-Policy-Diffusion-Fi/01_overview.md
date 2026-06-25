# PDFactor: Learning Tri-Perspective View Policy Diffusion Field for Multi-Task Robotic Manipulation

- Year/Venue: 2025 / CVPR
- Category: Equivariance, Diffusion, and 3D Action
- Tags: Diffusion, Robotics, 3D action
- Authors: Jingyi Tian, Le Wang, Sanping Zhou, Sen Wang, Jiayi Li, Haowen Sun, Wei Tang ; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2025, pp. 15757-15767
- Paper: https://openaccess.thecvf.com/content/CVPR2025/html/Tian_PDFactor_Learning_Tri-Perspective_View_Policy_Diffusion_Field_for_Multi-Task_Robotic_CVPR_2025_paper.html
- PDF status: downloaded
- GitHub/Project: not identified from primary page

## Problem
생성 모델 또는 policy 모델이 3D 구조와 물리 제약을 보존하지 못하면 로봇 실행이나 3D 장면 생성에서 일관성이 깨진다.

## Core Idea
핵심은 diffusion score/denoising process를 action, 3D generation, 또는 structured scene representation에 적용하면서 geometry prior를 넣는 것이다.

## Paper-Specific Cues
- Topic cue: Robotic manipulation based on visual observations and natural language instructions is a long-standing challenge in robotics.
- Method cue: In response, we propose PDFactor, a novel framework that models action distribution with a hybrid triplane representation.
- Result cue: Yet prevailing approaches model action distribution by adopting explicit or implicit representations, which often struggle to achieve a trade-off between accuracy and efficiency.

## Input / Output
Input: language instruction plus RGB/RGB-D/point-cloud robot observations. Output: action tokens, poses, trajectories, constraints, or policy decisions.

## Main Claims
- 논문은 `diffusion-based generation or policy learning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다.

## Contribution
- diffusion-based generation or policy learning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Diffusion, Robotics, 3D action.
- 초록에서 확인되는 주요 cue: Robotic, Yet, PDFactor, DoF, This, Experiments, RLBench, Moreover.
