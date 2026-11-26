# FM-Steer: Enhance Generalist Policies with Value-Guided Cascaded Denoising

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Song_FM-Steer_Enhance_Generalist_Policies_with_Value-Guided_Cascaded_Denoising_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Song_FM-Steer_Enhance_Generalist_Policies_with_Value-Guided_Cascaded_Denoising_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: Haoming Song, Delin Qu, Yuanqi Yao, Qizhi Chen, Jiarui Li, Qi Lv, Yiwen Tang, Li Kang, Heng Zhou, Xianqiang Gao, Yuhang Tang, Xiaofan Li, Modi Shi, Guanghui Ren, Maoqing Yao, Bin Zhao, Dong Wang, Xuelong Li
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Robotics, VLA, test-time computation, value guidance, dexterous manipulation, real-time control, Flow Matching
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Song_FM-Steer_Enhance_Generalist_Policies_with_Value-Guided_Cascaded_Denoising_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Song_FM-Steer_Enhance_Generalist_Policies_with_Value-Guided_Cascaded_Denoising_CVPR_2026_paper.pdf
- Code/Project: https://hume-vla.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0). 2026-11-24 요약·기여는 [이번 대조 판본](https://openaccess.thecvf.com/content/CVPR2026/papers/Song_FM-Steer_Enhance_Generalist_Policies_with_Value-Guided_Cascaded_Denoising_CVPR_2026_paper.pdf) 기준이다.

## Why This Paper Is Here

FM-Steer는 흐름 기반 로봇 정책의 추론 중 중간 단계의 행동 후보에 가치를 매기고, 고른 후보를 빠르게 정제해 실행한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Song_FM-Steer_Enhance_Generalist_Policies_with_Value-Guided_Cascaded_Denoising_CVPR_2026_paper.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Humans naturally allocate more time before acting when handling complex tasks in the physical world.
- **p. 1 / Abstract - extractive body cue:** This paradigm has recently led to remarkable advances in boosting Large Language Models (LLMs) on complex tasks in digital domains.
- **p. 1 / Abstract - extractive body cue:** However, the potential of test-time computing remains largely unexplored for robotic foundation models that interact with the physical world.
- **p. 1 / Abstract - extractive body cue:** FM-Steer first introduces an intermediate flow verifier to estimate state-action values for candidate actions.
- **p. 1 / Abstract - extractive body cue:** At test time, the policy iteratively samples multiple noisy action proposals and retains the one with the highest predicted value, yielding value-aligned, high-quality actions without ...
- **p. 2 / 1. Introduction - extractive body cue:** However, robot control has stricter real-time requirements than text generation: extra inference computation can introduce delays, causing jitter or even task failure.
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we introduce FM-Steer, a framework that enhances flow-based VLA models at test time with value-guided test-time sampling and cascaded action denoising.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, the main contributions of this work are: • We propose FM-Steer, a test-time computing framework that enhances flow-based Vision-Language-Action models while improving the ...
- **p. 2 / 1. Introduction - extractive body cue:** To address this issue, we propose a cascaded action denoising mechanism that distributes the denoising computation across the original VLA and a separate Lite-Flow denoiser, ...
- **p. 3 / 3. Preliminaries - extractive body cue:** The model typically consists of a VLM backbone and a flow matching expert.
- **p. 3 / 3. Preliminaries - extractive body cue:** A flow-based VLA aims to model the data distribution p(At/ot), mapping the observation ot, which consists of images it, language instructions ℓt, and robot state ...
- **p. 6 / Model - extractive body cue:** We present the success rate (SR) and standard error for each method across four task suites.
- **p. 4 / 4.1. Value-Guided Test-Time Sampling - extractive body cue:** During training, we use the calibrated Q-learning [49] to optimize the intermediate flow verifier φ.
- **p. 4 / 4.2. Cascaded Action Denoising - extractive body cue:** For the k-th sub-action chunk Aτ ∗ t,k, it contains the noisy action from time step t + kh to t + (k + 1)h ...
- **p. 7 / 5.3. Efficiency Improvement - extractive body cue:** In other words, when FM-Steer enters an erroneous state, it can evaluate multiple candidate actions and select a better forward trajectory.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | A flow-based VLA aims to model the data distribution p(At/ot), mapping the observation ot, which consists of images it, language instructions ℓt, and robot state information st, to a sequence of H ... | observation, uncertainty/risk estimate와 task command | p. 3 (3. Preliminaries), p. 4 (4.2. Cascaded Action Denoising) |
| State/latent | flow-based, VLA, aims, model, data, distribution, At/ot, mapping, observation, consists, images, language | safe set, recovery state 또는 constraint margin | p. 3 (3. Preliminaries), p. 4 (4.2. Cascaded Action Denoising), p. 4 (4.1. Value-Guided Test-Time Sampling) |
| Output/action | For the k-th sub-action chunk Aτ ∗ t,k, it contains the noisy action from time step t + kh to t + (k + 1)h -1, and its corresponding observation is ot,k ... | shielded, recovery 또는 safe action | p. 4 (4.2. Cascaded Action Denoising), p. 4 (4.1. Value-Guided Test-Time Sampling), p. 2 (1. Introduction) |
| Objective/outcome | Due to the multiple Euler forward iterations required by flow-based VLA during inference, repeated action sampling leads to a significant increase in computational cost. | task return과 violation/failure probability | p. 3 (4.1. Value-Guided Test-Time Sampling), p. 4 (4.2. Cascaded Action Denoising), p. 4 (4.1. Value-Guided Test-Time Sampling) |

## Main Claims and Actual Contribution

- 중간 잡음 상태의 행동에 가치 추정기를 학습시켜 여러 후보 중 사용할 행동을 결정한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Song_FM-Steer_Enhance_Generalist_Policies_with_Value-Guided_Cascaded_Denoising_CVPR_2026_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Song_FM-Steer_Enhance_Generalist_Policies_with_Value-Guided_Cascaded_Denoising_CVPR_2026_paper.pdf#page=4)
- 후보 선택과 경량 Lite-Flow의 잡음 제거를 비동기로 수행하고 실제 로봇에서 행동 빈도와 조작 성과를 평가했다. [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Song_FM-Steer_Enhance_Generalist_Policies_with_Value-Guided_Cascaded_Denoising_CVPR_2026_paper.pdf#page=4) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Song_FM-Steer_Enhance_Generalist_Policies_with_Value-Guided_Cascaded_Denoising_CVPR_2026_paper.pdf#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (Figure/Table caption), p. 1 (Figure/Table caption) |
| Embodiment/environment | We study FM-Steer across diverse simulated and real-world robotic platforms, including humanoid robots, and compare it with previous state-of-the-art generalist policies, including prior test-time computing frameworks. | hardware/simulator version and reset protocol | p. 5 (5. Experiments), p. 5 (5. Experiments) |
| Dataset/benchmark | We study FM-Steer across diverse simulated and real-world robotic platforms, including humanoid robots, and compare it with previous state-of-the-art generalist policies, including prior test-time computing frameworks. | role, split, size and leakage | p. 5 (5. Experiments), p. 5 (5. Experiments) |
| Metric | Table 1. LIBERO Benchmark Results. We present the success rate (SR) and standard error for each method across four task suites. FM-Steer (π0) achieves the highest average success rate and ranking, followed ... | definition, denominator, direction and uncertainty | p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 1 (Figure/Table caption) |
| Baseline/ablation | We study FM-Steer across diverse simulated and real-world robotic platforms, including humanoid robots, and compare it with previous state-of-the-art generalist policies, including prior test-time computing frameworks. | fair input/data/compute/action matching | p. 5 (5. Experiments), p. 1 (Figure/Table caption), p. 7 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 6. Conclusion - extractive body cue:** The gains are especially clear on complex tasks that require failure recovery, highlighting a promising direction for generalist robot policies.
- **p. 8 / 6. Conclusion - extractive body cue:** FM-Steer combines valueguided test-time sampling with effective best-of-N selection and cascaded action denoising, integrating the original VLA with a lightweight denoiser to achieve rapid and ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Overview of FM-Steer. FM-Steer augments a flow-based VLA with two modules: the intermediate flow verifier and the Lite- Flow denoiser. Given an observation, ...
- **p. 5 / 5.1. Implementation Details - extractive body cue:** FMSteer sets the noise-level bound T in the range of 0.7 to 0.9 and selects N = 5 candidates from the original VLA at each ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Experimental setups on WidowX, AgiBot G-1, and Franka. We evaluate FM-Steer across 3 simulation environments and 3 different real-world robotic platforms, covering 15 ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Visualization of value-guided test-time sampling and cascaded action denoising. Panel (a) shows value maps of can- didate actions, where the ground-truth actions lie ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 4 (4.1. Value-Guided Test-Time Sampling), p. 4 (4.2. Cascaded Action Denoising), p. 7 (5.3. Efficiency Improvement), p. 3 (4.1. Value-Guided Test-Time Sampling)이다.
