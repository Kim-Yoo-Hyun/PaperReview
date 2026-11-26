# HumanPlus: Humanoid Shadowing and Imitation from Humans

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v270/fu25a.html.
> PDF retrieval source: https://arxiv.org/pdf/2406.10454. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CoRL
- Authors: Zipeng Fu, Qingqing Zhao, Qi Wu, Gordon Wetzstein, Chelsea Finn
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, humanoid, human-to-humanoid, Imitation Learning, teleoperation, Reinforcement Learning
- Official paper: https://proceedings.mlr.press/v270/fu25a.html
- Full-text retrieval: https://arxiv.org/pdf/2406.10454
- Code/Project: https://humanoid-ai.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

HumanPlus는 사람의 동작을 실시간 모방해 휴머노이드를 원격조작하고, 그렇게 모은 시연으로 자율 시각 정책을 학습한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/fu25a/fu25a.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** One of the key arguments for building robots that have similar form factors to human beings is that we can leverage the massive human data ...
- **p. 1 / Abstract - extractive body cue:** Yet, doing so has remained challenging in practice due to the complexities in humanoid perception and control, lingering physical gaps between humanoids and humans in ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce a full-stack system for humanoids to learn motion and autonomous skills from human data.
- **p. 1 / Abstract - extractive body cue:** We first train a low-level policy in simulation via reinforcement learning using existing 40-hour human motion datasets.
- **p. 1 / Abstract - extractive body cue:** This policy transfers to the real world and allows humanoid robots to follow hu1.
- **p. 2 / 1. Introduction - extractive body cue:** This problem is further exacerbated by the lack of off-the-shelf and integrated hardware platforms.
- **p. 2 / 1. Introduction - extractive body cue:** Traditional approaches, such as decoupling the problem into perception, planning and tracking, and separate modularization of control for arms and legs [10, 10, 23, 40], ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we present a full-stack system for humanoids to learn motion and autonomous skills from human data.
- **p. 3 / 1. Introduction - extractive body cue:** Core to this system is both (1) a real-time shadowing system that allows human operators to whole-body control humanoids using a single RGB camera and ...
- **p. 3 / 1. Introduction - extractive body cue:** Using forward dynamics prediction on image features, our method shows improved performance by regularizing on image feature spaces and preventing the vision-based skill policy from ...
- **p. 4 / 4. Human Body and Hand Data - extractive body cue:** Each of the humanoid hip and shoulder joints consists of 3 orthogonal revolute joints, so can be viewed as one spherical joints.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Our system enables robots to shadow fast, diverse motions from a human operator, including boxing and playing table tennis, and to learn autonomous skills like ...
- **p. 2 / 1. Introduction - extractive body cue:** We leverage this dataset by first retargeting human poses to humanoid poses and then training a task-agnostic low-level policy called Humanoid Shadowing Transformer conditioning on ...
- **p. 7 / 6. Imitation of Human Skills - extractive body cue:** In this work, we modify the Action Chunking Transformer [104] by removing its encoder-decoder architecture to develop a decoder-only Humanoid Imitation Transformer (HIT) for skill ...
- **p. 3 / 1. Introduction - extractive body cue:** We build upon the recent success of imitation learning from human-provided demonstrations [11, 104], and introduce a transformer-based architecture that blends action prediction and forward ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Using state-of-the-art human body and hand pose estimation algorithms [58, 81], we can estimate real-time human motion and retarget it to humanoid motion, which is passed as input to the low-level policy. | proprioception, reference pose/motion, visual or language command | p. 2 (1. Introduction), p. 5 (5. Shadowing of Human Motion) |
| State/latent | state-of-the-art, human, body, hand, pose, estimation, algorithms, estimate, real-time, motion, retarget, humanoid | whole-body pose, balance/contact state와 skill/mode | p. 2 (1. Introduction), p. 5 (5. Shadowing of Human Motion), p. 2 (1. Introduction) |
| Output/action | At each time step, the input to the policy is humanoid proprioception and a humanoid target pose. | joint/whole-body action, motion target 또는 task trajectory | p. 5 (5. Shadowing of Human Motion), p. 2 (1. Introduction), p. 3 (1. Introduction) |
| Objective/outcome | We use PPO [74] to train our Humanoid Shadowing Transformer in simulation by maximizing discounted expected return E hPT-1 t=0 γtrt i , where rt is the reward at time step t, ... | tracking, balance, skill/task success와 recovery | p. 6 (5. Shadowing of Human Motion), p. 2 (1. Introduction), p. 5 (4. Human Body and Hand Data) |

## Main Claims and Actual Contribution

- 사람의 전신·손 자세를 RGB 카메라로 추정하고 시뮬레이션에서 훈련한 저수준 제어기로 실물 동작을 추종한다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/fu25a/fu25a.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/fu25a/fu25a.pdf#page=4)
- 원격조작 시연의 1인칭 영상과 행동으로 기술 정책을 모방학습하고 실제 작업별 성공을 평가한다. [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/fu25a/fu25a.pdf#page=5) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/fu25a/fu25a.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 10 (9. Experiments on Imitation), p. 9 (Figure/Table caption) |
| Embodiment/environment | Shown in Table 5, we compare our imitation learning method Humanoid Imitation Transformer with three baseline methods: HIT policies with monocular inputs (Monocular), ACT [104], and Open-loop trajectory replay, across all tasks: ... | hardware/simulator version and reset protocol | p. 10 (9. Experiments on Imitation), p. 10 (8.1. Comparisons with Other Teleoperation) |
| Dataset/benchmark | The participants are tasked to perform the Rearrange Objects task and its variant, Rearrange Lower Objects, where an object is placed on a lower table of height 0.55m, requiring the robot to ... | role, split, size and leakage | p. 10 (9. Experiments on Imitation), p. 10 (8.1. Comparisons with Other Teleoperation), p. 9 (8.1. Comparisons with Other Teleoperation), p. 9 (8.1. Comparisons with Other Teleoperation) |
| Metric | In contrast, our system has the lowest timeto-completion, has the highest success rate of stable standing, and is the only method that can be used for whole-body teleoperation, solving the Rearrange Lower ... | definition, denominator, direction and uncertainty | p. 10 (8.1. Comparisons with Other Teleoperation), p. 9 (8.1. Comparisons with Other Teleoperation), p. 9 (8. Experiments on Shadowing) |
| Baseline/ablation | Overall HIT (Ours) outperforms others. | fair input/data/compute/action matching | p. 9 (8. Experiments on Shadowing), p. 9 (8.1. Comparisons with Other Teleoperation), p. 10 (9. Experiments on Imitation) |

## Explicit Limitations and Failure Boundary

- **p. 8 / Figure/Table caption - extractive body cue:** Table 4: Robustness Evaluation. Our low-level policy (Ours) can withstand large disturbance forces, has a shorter recovery time, and enables more whole-body skills than the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3: Teleop Comparisons & User Studies. We report averaged completion time for 6 participants on 2 tasks. target poses while saving energy and avoiding ...
- **p. 10 / 9. Experiments on Imitation - extractive body cue:** Throughout the development of our system, we encountered several limitations.
- **p. 10 / 9. Experiments on Imitation - extractive body cue:** It fails the Wear a Shoe and Walk task completely, where depth perception is crucial.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 3 (1. Introduction), p. 7 (6. Imitation of Human Skills), p. 5 (4. Human Body and Hand Data)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** This problem is further exacerbated by the lack of off-the-shelf and integrated hardware platforms. (p. 2, 1. Introduction).
- **Actual contribution:** In this paper, we present a full-stack system for humanoids to learn motion and autonomous skills from human data. (p. 2, 1. Introduction).
- **Evaluation boundary:** Shown in Table 5, we compare our imitation learning method Humanoid Imitation Transformer with three baseline methods: HIT policies with monocular inputs (Monocular), ACT [104], and Open-loop trajectory replay, across ... (p. 10, 9. Experiments on Imitation).
- **Explicit failure boundary:** It fails the Wear a Shoe and Walk task completely, where depth perception is crucial. (p. 10, 9. Experiments on Imitation).
