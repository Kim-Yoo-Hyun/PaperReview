# Diffusion-EDFs: Bi-equivariant Denoising Generative Modeling on SE(3) for Visual Robotic Manipulation

- Year/Venue: 2024 / CVPR 2024
- Category: Equivariance, Diffusion, and 3D Action
- Tags: equivariant, Diffusion, Robotics
- Authors: Hyunwoo Ryu, Jiwoo Kim, Hyunseok An, Junwoo Chang, Joohwan Seo, Taehan Kim, Yubin Kim, Chaewon Hwang, Jongeun Choi, Roberto Horowitz ; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2024, pp. 18007-18018
- Paper: https://openaccess.thecvf.com/content/CVPR2024/html/Ryu_Diffusion-EDFs_Bi-equivariant_Denoising_Generative_Modeling_on_SE3_for_Visual_Robotic_CVPR_2024_paper.html
- PDF status: downloaded
- GitHub/Project: not identified from primary page

## Problem
생성 모델 또는 policy 모델이 3D 구조와 물리 제약을 보존하지 못하면 로봇 실행이나 3D 장면 생성에서 일관성이 깨진다.

## Core Idea
핵심은 diffusion score/denoising process를 action, 3D generation, 또는 structured scene representation에 적용하면서 geometry prior를 넣는 것이다.

## Paper-Specific Cues
- Topic cue: Diffusion generative modeling has become a promising approach for learning robotic manipulation tasks from stochastic human demonstrations.
- Method cue: In this paper we present Diffusion-EDFs a novel SE(3)-equivariant diffusion-based approach for visual robotic manipulation tasks.
- Result cue: We show that our proposed method achieves remarkable data efficiency requiring only 5 to 10 human demonstrations for effective end-to-end training in less than ...

## Input / Output
Input: language instruction plus RGB/RGB-D/point-cloud robot observations. Output: action tokens, poses, trajectories, constraints, or policy decisions.

## Main Claims
- 논문은 `diffusion-based generation or policy learning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다.

## Contribution
- diffusion-based generation or policy learning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: equivariant, Diffusion, Robotics.
- 초록에서 확인되는 주요 cue: Diffusion, Diffusion-EDFs, Furthermore, Lastly.
