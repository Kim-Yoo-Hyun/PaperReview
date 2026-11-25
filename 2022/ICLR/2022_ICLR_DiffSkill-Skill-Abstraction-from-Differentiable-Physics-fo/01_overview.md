# DiffSkill: Skill Abstraction from Differentiable Physics for Deformable Object Manipulations with Tools

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2203.17275.
> PDF retrieval source: https://arxiv.org/pdf/2203.17275. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / ICLR
- Authors: Xingyu Lin, Zhiao Huang, Yunzhu Li, Joshua B. Tenenbaum, David Held, Chuang Gan
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, deformable object, tool use, differentiable physics, skill abstraction, Planning
- Official paper: https://arxiv.org/abs/2203.17275
- Full-text retrieval: https://arxiv.org/pdf/2203.17275
- Code/Project: https://xingyu-lin.github.io/diffskill/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

DiffSkill은 미분 가능한 물리 시뮬레이터에서 찾은 짧은 도구 사용 기술을 조합해 긴 변형 물체 조작을 해결한다. [PDF 1쪽](https://arxiv.org/pdf/2203.17275#page=1)

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** We consider the problem of sequential robotic manipulation of deformable objects using tools.
- **p. 1 / ABSTRACT - extractive body cue:** Previous works have shown that differentiable physics simulators provide gradients to the environment state and help trajectory optimization to converge orders of magnitude faster than ...
- **p. 1 / ABSTRACT - extractive body cue:** However, such gradient-based trajectory optimization typically requires access to the full simulator states and can only solve short-horizon, single-skill tasks due to local optima.
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we propose a novel framework, named DiffSkill, that uses a differentiable physics simulator for skill abstraction to solve long-horizon deformable object manipulation ...
- **p. 1 / ABSTRACT - extractive body cue:** In particular, we first obtain short-horizon skills using individual tools from a gradient-based optimizer, using the full state information in a differentiable simulator; we then ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** These differentiable simulators have facilitated gradient-based trajectory optimizers to find a motion trajectory with much fewer samples, compared with black box optimizers such as CEM ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** This work aims to narrow the gap and develop a method named DiffSkill that learns to use tools like a rolling pin, spatula, knife, etc., ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our method consists of three components, (1) a trajectory optimizer that acts as an expert that applies gradient-based optimization on the differentiable simulator to obtain ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To extend the use of differentiable physics models to these long-horizon tasks and enable the agent to directly consume visual observations, we propose DiffSkill: a ...
- **p. 4 / 2 METHOD - extractive body cue:** As such, we propose to learn a neural skill abstractor that learns skills from the demonstration videos of a trajectory optimizer; we will then leverage ...
- **p. 4 / 2 METHOD - extractive body cue:** Our neural skill abstraction consists of a goal-conditioned policy that takes a sensory observation (RGB-D images in our case) as input, a feasibility and reward ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** The recent development of differentiable physics simulators for deformable objects has shown promising results for solving soft-body control problems (Hu et al., 2019b; Murthy et ...
- **p. 3 / 2 METHOD - extractive body cue:** Given an initial state s0, a goal state sg and the transition dynamics p of a differentiable simulator, we use gradient-based trajectory optimization to solve ...
- **p. 2 / 2 METHOD - extractive body cue:** Since it is not feasible to directly use a standalone differentiable physics solver to find an optimal solution for long-horizontal tasks, we propose to first ...
- **p. 4 / 2 METHOD - extractive body cue:** We use an MSE loss Lfea for model training, which was shown empirically to work better than a cross-entropy loss.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our neural skill abstraction consists of a goal-conditioned policy that takes a sensory observation (RGB-D images in our case) as input, a feasibility and reward predictor, as well as a variational auto-encoder ... | RGB-D/point cloud, object state와 contact/task observation | p. 4 (2 METHOD), p. 2 (1 INTRODUCTION) |
| State/latent | neural, skill, abstraction, consists, goal-conditioned, policy, takes, sensory, observation, RGB-D, images, case | object geometry, affordance, contact mode 또는 end-effector state | p. 4 (2 METHOD), p. 2 (1 INTRODUCTION), p. 2 (2 METHOD) |
| Output/action | Our method consists of three components, (1) a trajectory optimizer that acts as an expert that applies gradient-based optimization on the differentiable simulator to obtain demonstration trajectories, which requires the full state ... | grasp, pose, force 또는 end-effector trajectory | p. 2 (1 INTRODUCTION), p. 2 (2 METHOD), p. 4 (2 METHOD) |
| Objective/outcome | Model parameter Value dimension of latent space 8 MLP hidden node number 1024 Training parameters Value learning rate 0.001 batch size 128 optimizer Adam beta1 0.9 beta2 0.999 weight decay 0 hindsight ... | task completion, contact success, pose/force error와 generalization | p. 14 (A IMPLEMENTATION DETAILS), p. 5 (2 METHOD), p. 5 (2 METHOD) |

## Main Claims and Actual Contribution

- 시뮬레이터 전체 상태로 도구별 궤적을 최적화하고 그 시연으로 RGB-D에서 사용할 신경망 기술 모델을 학습한다. [PDF 3쪽](https://arxiv.org/pdf/2203.17275#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2203.17275#page=4)
- 중간 목표와 기술 순서를 계획해 단일 기술로 끝낼 수 없는 장기 도구 사용 과제에서 평가했다. [PDF 5쪽](https://arxiv.org/pdf/2203.17275#page=5) · [PDF 8쪽](https://arxiv.org/pdf/2203.17275#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 7 (3 EXPERIMENTS), p. 7 (3 EXPERIMENTS) |
| Embodiment/environment | We build our simulation environments on top of PlasticineLab (Huang et al., 2021), a differentiable physics benchmark using the DiffTaichi system (Hu et al., 2019a) that could simulate plasticine-like objects based on ... | hardware/simulator version and reset protocol | p. 5 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS) |
| Dataset/benchmark | We found behavior cloning to be sufficient for learning short-horizon skills from the demonstration dataset. | role, split, size and leakage | p. 5 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS), p. 5 (3 EXPERIMENTS) |
| Metric | After training, we find the feasibility and score predictor to perform well on the held out trajectories, achieving a L2 error of less than 0.05 for the score predictor and an accuracy ... | definition, denominator, direction and uncertainty | p. 6 (3 EXPERIMENTS), p. 7 (Figure/Table caption), p. 6 (3 EXPERIMENTS) |
| Baseline/ablation | 3.3 BASELINES We compare with three strong baselines: Model-free Reinforcement Learning (RL) We compare with two model-free RL methods: TD3 (Fujimoto et al., 2018) and SAC (Haarnoja et al., 2018). | fair input/data/compute/action matching | p. 6 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS), p. 2 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 3 EXPERIMENTS - extractive body cue:** In Table 3, we can see that the learned skills (labeled as Behavior Cloning) approach the normalized performance of the trajectory optimization (Trajectory Opt) on ...
- **p. 7 / 3 EXPERIMENTS - extractive body cue:** 3.4 RESULT ANALYSIS We show that DiffSkill is able to solve the challenging long-horizon, tool-use tasks from the sensory observation (RGB-D) while the baselines cannot.
- **p. 8 / 3 EXPERIMENTS - extractive body cue:** On the other hand, if we do not optimize for the intermediate goals, we also cannot determine which tools to use at evaluation time, since ...
- **p. 6 / 3 EXPERIMENTS - extractive body cue:** In this way, a normalized performance of 0 representing a policy that does nothing and a normalized performance of 1 representing an upper bound of ...
- **p. 7 / 3 EXPERIMENTS - extractive body cue:** This is because the trajectory optimizer is more reliable at finding partial solutions that transport part of the dough to the target locations but does ...
- **p. 9 / 4 RELATED WORK - extractive body cue:** There are a few interesting directions for future work.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (2 METHOD), p. 2 (2 METHOD)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** The recent development of differentiable physics simulators for deformable objects has shown promising results for solving soft-body control problems (Hu et al., 2019b; Murthy et al., 2020; Heiden et al., ... (p. 1, 1 INTRODUCTION).
- **Actual contribution:** To extend the use of differentiable physics models to these long-horizon tasks and enable the agent to directly consume visual observations, we propose DiffSkill: a novel framework where the agent ... (p. 2, 1 INTRODUCTION).
- **Evaluation boundary:** Method Task LiftSpread GatherTransport CutRearrange No Discrete Planning 0.758 / 20% 0.312 / 0% 0.118 / 0% Direct Execution (Random) 0.593 / 15% 0.369 / 0% 0.018 / 2.5% Direct ... (p. 8, 3 EXPERIMENTS).
- **Explicit failure boundary:** This threshold is manually picked by observing the performance gap between successful and failed trajectories. (p. 6, 3 EXPERIMENTS).

## 원문과 공개 자료

- 코드 · 저자 분할 배포 중 과제·미분 시뮬레이션 구성요소 · core/diffskill/env_spec.py [배포 파일](https://raw.githubusercontent.com/Xingyu-Lin/DiffSkill/0cdb1271c7757d94269afb0066e1ce43002b34b5/core/diffskill/env_spec.py)
- 데이터 · 변형체 실험의 초기·목표 구성 · datasets.zip [배포 파일](https://drive.google.com/file/d/11XZw-p2FX-yvoHMnc_yNO5x7iiLxwlwB/view)
