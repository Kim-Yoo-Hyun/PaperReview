# SoftGym: Benchmarking Deep Reinforcement Learning for Deformable Object Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2011.07215.
> PDF retrieval source: https://arxiv.org/pdf/2011.07215. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2020 / CoRL
- Authors: Xingyu Lin, Yufei Wang, Jake Olkin, David Held
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, deformable object, Benchmark, Reinforcement Learning, simulation
- Official paper: https://arxiv.org/abs/2011.07215
- Full-text retrieval: https://arxiv.org/pdf/2011.07215
- Code/Project: https://sites.google.com/view/softgym/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

SoftGym은 변형 물체 조작에서 관측 방식과 제어 알고리즘의 영향을 비교하는 시뮬레이션 벤치마크다. [PDF 1쪽](https://proceedings.mlr.press/v155/lin21a/lin21a.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Manipulating deformable objects has long been a challenge in robotics due to its high dimensional state representation and complex dynamics.
- **p. 1 / Abstract - extractive body cue:** Recent success in deep reinforcement learning provides a promising direction for learning to manipulate deformable objects with data driven methods.
- **p. 1 / Abstract - extractive body cue:** However, existing reinforcement learning benchmarks only cover tasks with direct state observability and simple low-dimensional dynamics or with relatively simple image-based environments, such as those ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we present SoftGym, a set of open-source simulated benchmarks for manipulating deformable objects, with a standard OpenAI Gym API and a Python ...
- **p. 1 / Abstract - extractive body cue:** Our benchmark will enable reproducible research in this important area.
- **p. 1 / 1 Introduction - extractive body cue:** However, such low-dimensional sufficient state representations are difficult to perceive (or sometimes even define) for many deformable object tasks, such as laundry folding or dough ...
- **p. 2 / 1 Introduction - extractive body cue:** These environments highlight the difficulty in performing robot manipulation tasks in environments that have complex visual observations with partial observability and an inherently high dimensional ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we present SoftGym, a set of open-source simulated benchmarks for manipulating deformable objects, with a standard OpenAI Gym API and Python interface ...
- **p. 3 / 1 Introduction - extractive body cue:** SoftGym consists of three parts: SoftGym-Medium, SoftGym-Hard and SoftGym-Robot, visualized in Figure 1.
- **p. 3 / 1 Introduction - extractive body cue:** 4 SoftGym To advance research in reinforcement learning in complex environments with an inherently high dimensional state, we propose SoftGym.
- **p. 2 / 1 Introduction - extractive body cue:** As such, we believe that SoftGym would be a unique and valuable contribution to the reinforcement learning and robotics communities, by enabling new methods to ...
- **p. 4 / 1 Introduction - extractive body cue:** This action space is designed to enable the user to focus on the challenges of high-level planning and to abstract away the low-level manipulation.
- **p. 2 / 1 Introduction - extractive body cue:** Due to the large number of samples required by reinforcement learning, as well as the difficulty in specifying a reward function, all these works start ...
- **p. 2 / 1 Introduction - extractive body cue:** We benchmark a range of algorithms on these environments assuming different observation spaces for the policy, including full knowledge of the ground-truth state of the ...
- **p. 5 / 1 Introduction - extractive body cue:** 5.2 State Oracle Many robotic systems follow the paradigm of first performing state estimation and then using the estimated state as input to a policy.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We benchmark a range of algorithms on these environments assuming different observation spaces for the policy, including full knowledge of the ground-truth state of the deformable object, a lowdimension state representation, and ... | standardized observation, action, task state와 evaluation split | p. 2 (1 Introduction), p. 5 (1 Introduction) |
| State/latent | benchmark, range, algorithms, environments, assuming, different, observation, spaces, policy, including, full, knowledge | benchmark state/goal와 method decision | p. 2 (1 Introduction), p. 5 (1 Introduction), p. 5 (1 Introduction) |
| Output/action | 5.2 State Oracle Many robotic systems follow the paradigm of first performing state estimation and then using the estimated state as input to a policy. | policy/controller trajectory 또는 measured result | p. 5 (1 Introduction), p. 5 (1 Introduction), p. 6 (1 Introduction) |
| Objective/outcome | Given this information, we can use gradient free optimization to maximize the return. | success metric, robustness, generalization과 reproducibility | p. 5 (1 Introduction), p. 6 (1 Introduction), p. 2 (1 Introduction) |

## Main Claims and Actual Contribution

- 천·밧줄·유체 등의 상이한 동역학을 가진 과제를 공통 Gym 인터페이스로 제공한다. [PDF 3쪽](https://proceedings.mlr.press/v155/lin21a/lin21a.pdf#page=3) · [PDF 4쪽](https://proceedings.mlr.press/v155/lin21a/lin21a.pdf#page=4)
- 완전 상태와 부분 관측 등 조건을 나눠 여러 강화학습 방법을 평가하고 고차원 상태에서 남는 어려움을 분석했다. [PDF 5쪽](https://proceedings.mlr.press/v155/lin21a/lin21a.pdf#page=5) · [PDF 7쪽](https://proceedings.mlr.press/v155/lin21a/lin21a.pdf#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 7 (6 Experiments), p. 7 (6 Experiments) |
| Embodiment/environment | Thus, this evaluation points to a clear need for new methods development for image-based robot manipulation of deformable objects. | hardware/simulator version and reset protocol | p. 7 (6 Experiments), p. 8 (6 Experiments) |
| Dataset/benchmark | We set up a real world cloth manipulation environment with a Sawyer robot with a Weiss gripper, as shown in Figure 4. | role, split, size and leakage | p. 7 (6 Experiments), p. 8 (6 Experiments), p. 8 (6 Experiments), p. 6 (6 Experiments) |
| Metric | Table 3: Task specific planning horizon for CEM B.2 SAC and CURL-SAC We use the CURL-SAC implementation from the released code3. Both Q-value network and the policy network are MLPs with 2 ... | definition, denominator, direction and uncertainty | p. 16 (Figure/Table caption), p. 16 (Figure/Table caption), p. 6 (6 Experiments) |
| Baseline/ablation | While it outperforms the rest of the baselines due to the use of the segmentation map and a better action space for exploration, the result shows that there still exists a large ... | fair input/data/compute/action matching | p. 7 (6 Experiments), p. 7 (6 Experiments), p. 15 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 6 Experiments - extractive body cue:** from a policy that always does nothing.
- **p. 7 / 6 Experiments - extractive body cue:** On the other hand, this method does not perform very well on the FoldCloth task.
- **p. 17 / Figure/Table caption - extractive body cue:** Table 7: Architecture of the deconvolutional neural network (VAE decoder) in PlaNet. We use a GRU [56] with 200 hidden nodes as the deterministic path ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, programming a robot to perform these tasks has long been a challenge in robotics due to the high dimensional state representation and complex dynamics [1, 2, 3]. (p. 1, 1 Introduction).
- **Actual contribution:** In this paper, we present SoftGym, a set of open-source simulated benchmarks for manipulating deformable objects, with a standard OpenAI Gym API and Python interface for creating new environments. (p. 2, 1 Introduction).
- **Evaluation boundary:** 6.2 Benchmarking results on SoftGym-Medium A summary of the final normalized performance of all baselines on the evaluation set is shown in Figure 2. (p. 7, 6 Experiments).
- **Explicit failure boundary:** We do not include the latent over-shooting in our experiment as it does not improve much over the one-step case. (p. 17, B.4 PlaNet).

## 원문과 공개 자료

- 코드 · 변형체 벤치마크의 옷감 펼치기 환경 구현 · softgym/envs/cloth_flatten.py [배포 파일](https://raw.githubusercontent.com/Xingyu-Lin/softgym/bb383f64cd488062587714abbae38f27ed9f2457/softgym/envs/cloth_flatten.py)
- 데이터 · 배포한 시뮬레이션 환경 초기 상태 · rope_configuration.pkl [배포 파일](https://drive.google.com/file/d/1f3FK_7gwnJLVm3VaSacvYS7o-19-XPrr/view)
