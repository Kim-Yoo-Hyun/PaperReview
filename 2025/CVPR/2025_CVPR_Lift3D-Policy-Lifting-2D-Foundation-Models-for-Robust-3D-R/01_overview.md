# Lift3D Policy: Lifting 2D Foundation Models for Robust 3D Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Jia_Lift3D_Policy_Lifting_2D_Foundation_Models_for_Robust_3D_Robotic_CVPR_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Jia_Lift3D_Policy_Lifting_2D_Foundation_Models_for_Robust_3D_Robotic_CVPR_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CVPR
- Authors: Yueru Jia, Jiaming Liu, Sixiang Chen, Chenyang Gu, Zhilve Wang, Longzan Luo, Xiaoqi Li, Pengwei Wang, Zhongyuan Wang, Renrui Zhang, Shanghang Zhang
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: 3D Vision, foundation model, Robotics
- Official paper: https://openaccess.thecvf.com/content/CVPR2025/html/Jia_Lift3D_Policy_Lifting_2D_Foundation_Models_for_Robust_3D_Robotic_CVPR_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2025/papers/Jia_Lift3D_Policy_Lifting_2D_Foundation_Models_for_Robust_3D_Robotic_CVPR_2025_paper.pdf
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0). 2026-11-24 요약·기여는 [이번 대조 판본](https://openaccess.thecvf.com/content/CVPR2025/papers/Jia_Lift3D_Policy_Lifting_2D_Foundation_Models_for_Robust_3D_Robotic_CVPR_2025_paper.pdf) 기준이다.

## Why This Paper Is Here

Lift3D는 2차원 사전학습 모형에 깊이 복원과 점군 입력을 도입해 로봇의 3차원 조작 표현을 학습한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Jia_Lift3D_Policy_Lifting_2D_Foundation_Models_for_Robust_3D_Robotic_CVPR_2025_paper.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D geometric information is essential for manipulation tasks, as robots need to perceive the 3D environment, reason about spatial relationships, and interact with intricate spatial ...
- **p. 1 / Abstract - extractive body cue:** Recent research has increasingly focused on the explicit extraction of 3D features, while still facing challenges such as the lack of large-scale robotic 3D data ...
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we propose the Lift3D framework, which progressively enhances 2D foundation models with implicit and explicit 3D robotic representations to construct a ...
- **p. 1 / Abstract - extractive body cue:** Specifically, we first design a task-aware masked autoencoder that masks task-relevant ∗:
- **p. 1 / Abstract - extractive body cue:** After self-supervised fine-tuning, we introduce a 2D model-lifting strategy that establishes a positional mapping between the input 3D points and the positional embeddings of the ...
- **p. 2 / 1. Introduction - extractive body cue:** However, the limited availability of large-scale robotic 3D data and foundational models constrains their generalization capabilities.
- **p. 2 / 1. Introduction - extractive body cue:** Building on the challenges in the aforementioned 3D policies, we raise a question: "Can we develop a 3D policy model that integrates large-scale pretrained knowledge ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are as follows: • We propose Lift3D, which elevates 2D foundation models 17348
- **p. 2 / 1. Introduction - extractive body cue:** Building on the challenges in the aforementioned 3D policies, we raise a question: "Can we develop a 3D policy model that integrates large-scale pretrained knowledge ...
- **p. 3 / 3. Lift3D Method - extractive body cue:** In Section 3.1, we introduce the problem statement of our proposed Lift3D framework.
- **p. 3 / 1. Introduction - extractive body cue:** to construct a 3D manipulation policy by systematically improving implicit and explicit 3D robotic representations. • For implicit 3D robotic representation, we design a taskaware ...
- **p. 4 / 3.3. 2D Model-lifting Strategy - extractive body cue:** After endowing the 2D foundation model with implicit 3D robotic awareness, we introduce a lifting strategy that en17350
- **p. 4 / 3.2. Task-aware Masked Autoencoder - extractive body cue:** Guide a) Implicit 3D robotic representation (Stage 1) Robot State Point Cloud CLIP Image Encoder CLIP Text Encoder Similarity matrix Text MAE Decoder 2D Foundation ...
- **p. 4 / 3.2. Task-aware Masked Autoencoder - extractive body cue:** Finally, to preserve the inherent capabilities of the foundation model, we introduce a distillation loss that constrains the distance between our model's visible token outputs ...
- **p. 5 / 3.3. 2D Model-lifting Strategy - extractive body cue:** The 3D tokenizer consists of farthest point sampling [51] for downsampling the number of points, the k-Nearest Neighbor algorithm for local aggregation, and learnable linear ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Finally, the output features from the 2D foundation model are processed through a policy head to predict the pose for imitation learning. masking strategy, where a large portion of the input image ... | image/video, language instruction, proprioception과 history | p. 4 (3.2. Task-aware Masked Autoencoder), p. 4 (3.2. Task-aware Masked Autoencoder) |
| State/latent | Finally, output, features, foundation, model, processed, through, policy, head, predict, pose, imitation | language-grounded task state와 action-policy context | p. 4 (3.2. Task-aware Masked Autoencoder), p. 4 (3.2. Task-aware Masked Autoencoder), p. 7 (Method) |
| Output/action | Guide a) Implicit 3D robotic representation (Stage 1) Robot State Point Cloud CLIP Image Encoder CLIP Text Encoder Similarity matrix Text MAE Decoder 2D Foundation Model Attention maps All tokens Visible tokens ... | continuous action, pose 또는 action chunk | p. 4 (3.2. Task-aware Masked Autoencoder), p. 7 (Method), p. 3 (3.1. Problem Statement) |
| Objective/outcome | Finally, to preserve the inherent capabilities of the foundation model, we introduce a distillation loss that constrains the distance between our model's visible token outputs and the corresponding features from the offthe-shelf ... | instruction following, task success, generalization과 latency | p. 4 (3.2. Task-aware Masked Autoencoder), p. 4 (3.2. Task-aware Masked Autoencoder), p. 5 (3.3. 2D Model-lifting Strategy) |

## Main Claims and Actual Contribution

- 작업에 관련된 영상 패치를 가린 뒤 깊이를 복원하고 점군 토큰의 공간 정보를 이용해 행동을 예측한다. [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Jia_Lift3D_Policy_Lifting_2D_Foundation_Models_for_Robust_3D_Robotic_CVPR_2025_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Jia_Lift3D_Policy_Lifting_2D_Foundation_Models_for_Robust_3D_Robotic_CVPR_2025_paper.pdf#page=5)
- 시뮬레이션과 실물 조작에서 과제 성공률을 평가하고 암시적·명시적 기하 표현을 학습하는 단계의 효과를 비교했다. [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Jia_Lift3D_Policy_Lifting_2D_Foundation_Models_for_Robust_3D_Robotic_CVPR_2025_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Jia_Lift3D_Policy_Lifting_2D_Foundation_Models_for_Robust_3D_Robotic_CVPR_2025_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Jia_Lift3D_Policy_Lifting_2D_Foundation_Models_for_Robust_3D_Robotic_CVPR_2025_paper.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (4.1. Simulation Experiment), p. 6 (4.1. Simulation Experiment) |
| Embodiment/environment | Comparison of manipulation success rates between Lift3D and 2D & 3D baselines in simulation benchmarks. ‘2D Rep.' and ‘3D Rep.' refer to robotic 2D representation and 3D representation methods, respectively. ‘PC' indicates ... | hardware/simulator version and reset protocol | p. 6 (4.1. Simulation Experiment), p. 5 (4.1. Simulation Experiment) |
| Dataset/benchmark | Additional details of the real-world dataset and assets are provided in Appendix A. | role, split, size and leakage | p. 6 (4.1. Simulation Experiment), p. 5 (4.1. Simulation Experiment), p. 6 (4.2. Real-World Experiment), p. 5 (4. Experiments) |
| Metric | In Table 1, Lift3D(CLIP) achieves an average success rate of 83.9 on the MetaWorld benchmark, with 78.8 accuracy on medium-level tasks and 82.0 accuracy on hard level tasks. | definition, denominator, direction and uncertainty | p. 6 (4.1. Simulation Experiment), p. 6 (4.1. Simulation Experiment), p. 8 (Figure/Table caption) |
| Baseline/ablation | In addition, compared to the previous SOTA 3D policy (DP3), Lift3D achieves an accuracy improvement of 18.6. | fair input/data/compute/action matching | p. 6 (4.1. Simulation Experiment), p. 6 (4.1. Simulation Experiment), p. 7 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion and Limitation - extractive body cue:** In terms of limitations, our Lift3D framework focuses on lifting 2D vision models to 3D manipulation tasks, which means it cannot comprehend language conditions.
- **p. 8 / 5. Conclusion and Limitation - extractive body cue:** In this paper, we introduce Lift3D, a novel framework that integrates large-scale pretrained 2D foundation models with robust 3D manipulation capabilities.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Lift3D empowers 2D foundation models with 3D manipulation capabilities by refining implicit 3D robotic representations through task-related affordance masking and depth reconstruction, while ...
- **p. 6 / 4.1. Simulation Experiment - extractive body cue:** These results demonstrate that Lift3D effectively enhances the 2D foundation model with robust manipulation capabilities, enabling a deeper understanding of robotic 3D scenes by leveraging ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 4 (3.2. Task-aware Masked Autoencoder), p. 5 (3.3. 2D Model-lifting Strategy), p. 3 (3.1. Problem Statement)이다.
