# Touch2Shape: Touch-Conditioned 3D Diffusion for Shape Exploration and Reconstruction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CVPR
- Authors: Yuanbo Wang, Zhaoxuan Zhang, Jiajin Qiu, Dilong Sun, Zhengyu Meng, Xiaopeng Wei, Xin Yang
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D reconstruction, Diffusion, Generation, 3D Vision, active perception, reinforcement-learning
- Official paper: https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.pdf)

## Why This Paper Is Here

Touch2Shape는 손끝에 닿은 작은 표면의 정보로 물체 전체 형상을 복원하고 다음에 어느 위치를 만질지 고른다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.pdf#page=1) · [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.pdf#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Diffusion models have made breakthroughs in 3D generation tasks.
- **p. 1 / Abstract - extractive body cue:** Current 3D diffusion models focus on reconstructing target shape from images or a set of partial observations.
- **p. 1 / Abstract - extractive body cue:** While excelling in global context understanding, they struggle to capture the local details of complex shapes and limited to the occlusion and lighting conditions.
- **p. 1 / Abstract - extractive body cue:** To overcome these limitations, we utilize tactile images to capture the local 3D information and propose a Touch2Shape model, which leverages a touch-conditioned diffusion model ...
- **p. 1 / Abstract - extractive body cue:** For shape reconstruction, we have developed a touch embedding module to condition the diffusion model in creating a compact representation and a touch shape fusion ...
- **p. 2 / 1. Introduction - extractive body cue:** This limitation presents challenges on two fronts.
- **p. 2 / 1. Introduction - extractive body cue:** However, acquiring 3D data presents greater challenges and costs compared to 2D image and text data.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** The main contributions of this article are as follows: • We propose Touch2Shape, a touch-conditioned 3D diffusion model for shape exploration and reconstruction, utilizing the ...
- **p. 2 / 1. Introduction - extractive body cue:** Extensive experiments validate the effectiveness of our method, demonstrating significant improvements in both reconstruction performance and the ability to improve reconstruction quality through touch exploration.
- **p. 4 / 3.2. Touch Shape Fusion - extractive body cue:** The touch shape fusion module is designed with two goals.
- **p. 4 / 3.1. Touch-conditioned Diffusion Model - extractive body cue:** The loss function for diffusion model training is as follows: Ldiff(t, n) = //Eω(zt, r(t), C(T0, ..., Tn→1)) ↓ωt//2, (2) where ωt is the added ...
- **p. 4 / 3.1. Touch-conditioned Diffusion Model - extractive body cue:** The implementation involves extracting feature tokens from images using ResNet [16], combining them with touch tokens through a dropout layer, and then inputting them together ...
- **p. 5 / 3.3. Policy Training - extractive body cue:** We first employ the pre-trained latent encoder in Figure 2 (c) to encode both the initial and current latent vectors of the touch-conditioned diffusion model.
- **p. 5 / 3.3. Policy Training - extractive body cue:** At each time step, we input the latent vector z of the target object, add noise through the diffusion model, and then use a touchconditioned ...
- **p. 3 / 3. Method - extractive body cue:** In test stage, we gather tactile images (T0, ..., Tn→1) from the target, utilizing the trained diffusion model to obtain a lowdimensional representation for predicting ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The policy model receives the denoised vector as input and is trained using reinforcement learning (Section 3.2). | tactile image/force, vision과 proprioceptive history | p. 4 (3. Method), p. 2 (1. Introduction) |
| State/latent | policy, model, receives, denoised, vector, input, trained, reinforcement, learning, Section, employ, simulated | contact geometry, force state 또는 latent dynamics | p. 4 (3. Method), p. 2 (1. Introduction), p. 4 (3.1. Touch-conditioned Diffusion Model) |
| Output/action | In this work, we employ a simulated robotic arm guided by a trained policy model to touch the target, enabling the acquisition of tactile images to reconstruct the target through touch interaction. | grasp/contact action, force command 또는 object motion | p. 2 (1. Introduction), p. 4 (3.1. Touch-conditioned Diffusion Model), p. 2 (1. Introduction) |
| Objective/outcome | For reward function setting, since the final output shape is not predicted, we design it to be the difference in the diffusion model's loss values. | slip/contact success, force/pose error와 robustness | p. 5 (3.3. Policy Training), p. 5 (3.3. Policy Training), p. 4 (3.1. Touch-conditioned Diffusion Model) |

## Main Claims and Actual Contribution

- 촉각 관측을 조건으로 전역 형상을 생성하는 잠재 확산 모델에 접촉한 국소 표면 정보를 융합한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.pdf#page=5)
- 형상 복원을 개선하도록 접촉 선택 정책을 학습하고 무작위·균등·오라클 선택을 같은 관측 횟수에서 비교했다. [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.pdf#page=7)

## Evaluation Scope

ABC 기반 표 3에서 접촉 영상은 시뮬레이터로 생성했다. 촉각만 썼을 때 파지 동작 5회 후 Chamfer 거리의 초기값 대비 비율은 RL 선택 6.63%, 무작위 선택 8.14%다. 낮을수록 복원 오차가 더 많이 줄었다. [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.pdf#page=5) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.pdf#page=7)

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.3. Evaluation on Policy - extractive body cue:** Furthermore, the Oracle policy is used to select the action which resulted in the best improvement, which is viewed as an upper-bound point of comparison ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 4 (3.1. Touch-conditioned Diffusion Model), p. 5 (3.3. Policy Training)이다.

## 검색 태그 근거

촉각 패치를 모아 확산 모델로 전체 형상을 예측하고, 복원 오차를 줄이는 다음 접촉 위치를 DQN으로 선택한다. 시뮬레이션에서 촉각만 쓰는 조건과 영상을 함께 쓰는 조건의 형상 오차를 비교했다. [원문 3쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.pdf#page=3) · [원문 5쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.pdf#page=5) · [원문 6쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.pdf#page=6)
