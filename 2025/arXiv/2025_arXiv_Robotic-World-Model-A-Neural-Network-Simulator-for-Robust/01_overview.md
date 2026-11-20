# Robotic World Model: A Neural Network Simulator for Robust Policy Optimization in Robotics

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2501.10100.
> PDF retrieval source: https://arxiv.org/pdf/2501.10100. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / arXiv
- Authors: Chenhao Li, Andreas Krause, Marco Hutter
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: Robotics, world model, policy optimization, simulation, robustness
- Official paper: https://arxiv.org/abs/2501.10100
- Full-text retrieval: https://arxiv.org/pdf/2501.10100
- Code/Project: not identified
- Paper type: system
- Source audit: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotic World Model은 여러 스텝에 걸쳐 정확한 예측을 유지하는 로봇 동역학 모델로 정책을 최적화한다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Learning robust and generalizable world models is crucial for enabling efficient and scalable robotic control in real-world environments.
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce a novel framework for learning world models that accurately capture complex, partially observable, and stochastic dynamics.
- **p. 1 / Abstract - extractive body cue:** The proposed method employs a dual-autoregressive mechanism and self-supervised training to achieve reliable long-horizon predictions without relying on domain-specific inductive biases, ensuring adaptability across diverse ...
- **p. 1 / Abstract - extractive body cue:** We further propose a policy optimization framework that leverages world models for efficient training in imagined environments and seamless deployment in real-world systems.
- **p. 1 / Abstract - extractive body cue:** This work advances model-based reinforcement learning by addressing the challenges of long-horizon prediction, error accumulation, and sim-to-real transfer.
- **p. 1 / 1 Introduction - extractive body cue:** A prevalent limitation in many approaches is the lack of adaptation and learning once the policy is deployed on the real system [5, 6, 7, ...
- **p. 3 / 1 Introduction - extractive body cue:** By addressing the challenges associated with learning world models, this work contributes toward bridging the gap between data-driven modeling and real-world deployment.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are summarized as follows: (i) We introduce a novel network architecture and training framework that enables the learning of reliable world models capable ...
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we present a novel approach for learning world models that emphasizes robustness and accuracy over long-horizon predictions.
- **p. 4 / 3 Approach - extractive body cue:** To address this gap, we propose Robotic World Model (RWM), a novel framework for learning robust world models in partially observable and dynamically complex environments.
- **p. 4 / 3 Approach - extractive body cue:** The input to the world model consists of a sequence of observation-action pairs spanning M historical steps.
- **p. 5 / 3 Approach - extractive body cue:** Our framework introduces a dualautoregressive mechanism: (i) Inner autoregression updates GRU hidden states autoregressively after each historical step within the context horizon M.
- **p. 6 / 3 Approach - extractive body cue:** Algorithm 1 Policy optimization with RWM 1: Initialize policy πθ, world model pϕ, and replay buffer D 2: for learning iterations = 1, 2, . ...
- **p. 4 / 3 Approach - extractive body cue:** World models [14] approximate the environment dynamics and facilitate policy optimization by enabling simulated environment interactions in imagination [16].
- **p. 5 / 3 Approach - extractive body cue:** The approach combines model-based imagination with model-free RL to achieve efficient and robust policy optimization, as outlined in Algorithm 1.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 3.1 Reinforcement Learning and World Models We formulate the problem by modeling the environment as a Partially Observable Markov Decision Process (POMDP) [40], defined by the tuple (S, A, O, T, R, ... | simulated state, geometry, contact와 control input | p. 4 (3 Approach), p. 4 (3 Approach) |
| State/latent | Reinforcement, Learning, World, Models, formulate, problem, modeling, environment, Partially, Observable, Markov, Decision | dynamics/contact state 또는 learned simulator representation | p. 4 (3 Approach), p. 4 (3 Approach), p. 5 (3 Approach) |
| Output/action | The input to the world model consists of a sequence of observation-action pairs spanning M historical steps. | simulation step, trajectory 또는 environment query | p. 4 (3 Approach), p. 5 (3 Approach), p. 6 (3 Approach) |
| Objective/outcome | The agent seeks to learn a policy πθ : O →A that maximizes the expected discounted return Eπθ hP t≥0 γtrt i , where rt is the reward at time t and ... | physical plausibility, speed, reproducibility와 task utility | p. 4 (3 Approach), p. 19 (A.4.3 Collision Handling and Model Pretraining), p. 4 (3 Approach) |

## Main Claims and Actual Contribution

- 서로 다른 수준의 자기회귀 갱신으로 긴 시간의 예측을 구성한다.
- 학습한 모델로 정책 최적화가 가능한지 평가한다.

[저자 원문](https://arxiv.org/abs/2501.10100)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (4 Experiments), p. 8 (4 Experiments) |
| Embodiment/environment | The experiments are designed to assess the accuracy and robustness of RWM, evaluate its architectural and training design choices, and demonstrate its effectiveness across diverse robotic tasks in Isaac Lab [43] and ... | hardware/simulator version and reset protocol | p. 6 (4 Experiments), p. 9 (4 Experiments) |
| Dataset/benchmark | These results underline the effectiveness of RWM and MBPO-PPO in enabling robust and scalable policy deployment for real-world robotic systems. | role, split, size and leakage | p. 6 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 6 (4 Experiments) |
| Metric | 0 1000 2000 Training Iterations 0 10 20 30 40 50 e SHAC Dreamer MBPO-PPO 0 1000 2000 Training Iterations 30 20 10 0 10 20 30 r ground truth prediction 0 ... | definition, denominator, direction and uncertainty | p. 8 (4 Experiments), p. 8 (Figure/Table caption), p. 6 (4 Experiments) |
| Baseline/ablation | Figure 4: Autoregressive trajectory prediction errors across diverse robotic environments and network architectures. RWM trained with autoregressive training (RWM-AR) consistently outperforms baseline methods, including MLP, recurrent s ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 7 (4 Experiments), p. 7 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 4 Experiments - extractive body cue:** In contrast, SHAC fails to converge, producing unstable behaviors that degrade both policy and model quality.
- **p. 9 / 4 Experiments - extractive body cue:** 5 Limitations The policy learned with RWM and MBPO-PPO surpasses existing MBRL methods in both robustness and generalization.
- **p. 10 / 6 Conclusion - extractive body cue:** In this work, we present RWM, a robust and scalable framework for learning world models tailored to complex robotic tasks.
- **p. 10 / 6 Conclusion - extractive body cue:** The results highlight RWM 's potential to enable adaptive, robust, and high-performing robotic systems, setting a foundation for broader adoption of model-based approaches in real-world ...
- **p. 7 / 4 Experiments - extractive body cue:** Grey curves represent the MLP baseline, which exhibits significantly higher error accumulation and reduced robustness to noise.
- **p. 7 / 4 Experiments - extractive body cue:** To assess the robustness of RWM, we analyze its performance under Gaussian noise perturbations applied to both observations and actions.
- **p. 8 / 4 Experiments - extractive body cue:** On the other hand, training transformer architectures with autoregressive training does not scale effectively, as the multi-step gradient propagation in autoregressive forecasting leads to GPU ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 6 (3 Approach)이다.
