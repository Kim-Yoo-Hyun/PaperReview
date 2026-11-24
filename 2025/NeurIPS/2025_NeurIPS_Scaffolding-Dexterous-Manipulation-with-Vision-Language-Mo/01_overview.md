# Scaffolding Dexterous Manipulation with Vision-Language Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (29 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://neurips.cc/virtual/2025/poster/118204.
> PDF retrieval source: https://arxiv.org/pdf/2506.19212.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: Vincent de Bakker, Joey Hejna, Tyler Ga Wei Lum, Onur Celik, Aleksandar Taranovic, Denis Blessing, Gerhard Neumann, Jeannette Bohg, Dorsa Sadigh
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Vision-Language Model, Robotics, Reinforcement Learning
- Official paper: https://neurips.cc/virtual/2025/poster/118204
- Full-text retrieval: https://arxiv.org/pdf/2506.19212.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (29 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

## Why This Paper Is Here

이 연구는 언어 지시와 장면으로부터 손과 물체의 대략적인 기준 궤적을 만든 뒤 잔차 강화학습으로 다지 손 조작을 정밀화한다. [PDF 1쪽](https://arxiv.org/pdf/2506.19212v3#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Dexterous robotic hands are essential for performing complex manipulation tasks, yet remain difficult to train due to the challenges of demonstration collection and high-dimensional control.
- **p. 1 / Abstract - extractive body cue:** While reinforcement learning (RL) can alleviate the data bottleneck by generating experience in simulation, it typically relies on carefully designed, task-specific reward functions, which hinder ...
- **p. 1 / Abstract - extractive body cue:** Thus, contemporary works in dexterous manipulation have often bootstrapped from reference trajectories.
- **p. 1 / Abstract - extractive body cue:** These trajectories specify target hand poses that guide the exploration of RL policies and object poses that enable dense, task-agnostic rewards.
- **p. 1 / Abstract - extractive body cue:** However, sourcing suitable trajectories-particularly for dexterous hands-remains a significant challenge.
- **p. 1 / 1 Introduction - extractive body cue:** To avoid both data scarcity and the embodiment gap, a combination of reinforcement learning (RL) and sim-to-real transfer has emerged as a promising approach by ...
- **p. 1 / 1 Introduction - extractive body cue:** The prevailing approach for training generalist policies - imitation learning from demonstrations [5, 49] - has achieved limited success with robot hands, primarily due to ...

## Core Idea

- **p. 1 / Abstract - extractive body cue:** Moreover, we showcase that our method transfers to realworld robotic hands without any human demonstrations or handcrafted rewards.
- **p. 2 / 1 Introduction - extractive body cue:** Building upon this insight, we introduce a framework for learning manipulation policies for dexterous robot hands with VLM-generated motion plans and residual RL.
- **p. 2 / 1 Introduction - extractive body cue:** Across 8 tasks, our method achieves close performance in both success rate and generalization to handcrafted, oracle plans despite requiring no manual reward engineering.
- **p. 1 / Abstract - extractive body cue:** Across a number of simulated tasks involving articulated objects and semantic understanding, we demonstrate that our method is able to learn robust dexterous manipulation policies.
- **p. 5 / 2. Plan Generation 𝜏 - extractive body cue:** 3D Proj. b) Inference 𝑥(1) board 𝑥(2) apple 𝑤1 wrist Environment (with keypoint tracking) Generate a motion trajectory for <task> with keypoints. 𝑥1:𝑇 1 𝑥1:𝑇 ...
- **p. 5 / 2. Plan Generation 𝜏 - extractive body cue:** In this section, we describe how we use the plan τ to further guide the learning and exploration of πl through the reward function, policy ...
- **p. 6 / 2. Plan Generation 𝜏 - extractive body cue:** Instead, we use ˜w1:T in the policy parameterization itself.
- **p. 6 / 2. Plan Generation 𝜏 - extractive body cue:** To further guide learning, we introduce a curriculum: the initial threshold δinit is linearly annealed to δinit/2 over the course of training.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 3D Proj. b) Inference 𝑥(1) board 𝑥(2) apple 𝑤1 wrist Environment (with keypoint tracking) Generate a motion trajectory for <task> with keypoints. 𝑥1:𝑇 1 𝑥1:𝑇 2 ෥𝑤1:𝑇 Action (𝑤𝑡+ Δ𝑤𝑡, 𝑞𝑡) Residual ... | image/video, language instruction, proprioception과 history | p. 5 (2. Plan Generation 𝜏), p. 5 (2. Plan Generation 𝜏) |
| State/latent | Proj, Inference, board, apple, wrist, Environment, keypoint, tracking, Generate, motion, trajectory, task | language-grounded task state와 action-policy context | p. 5 (2. Plan Generation 𝜏), p. 5 (2. Plan Generation 𝜏), p. 2 (1 Introduction) |
| Output/action | We learn πl using residual reinforcement learning [16, 26], which we formalize through a "plan" conditioned MDP on top of the low-level observation space Ol and action space A with horizon T. | continuous action, pose 또는 action chunk | p. 5 (2. Plan Generation 𝜏), p. 2 (1 Introduction), p. 6 (2. Plan Generation 𝜏) |
| Objective/outcome | So long as these motions generally encapsulate the desired behavior, RL can optimize per-timestep offsets and finger motions to maximize the tracking reward, ultimately surpassing human teleoperation in both performance and precision, ... | instruction following, task success, generalization과 latency | p. 2 (1 Introduction), p. 5 (2. Plan Generation 𝜏), p. 1 (1 Introduction) |

## Main Claims and Actual Contribution

- VLM이 과제와 관련된 키포인트 및 3차원 기준 움직임을 생성하고, 저수준 정책은 시뮬레이션에서 기준과 실제 움직임의 차이를 보정한다. [PDF 4쪽](https://arxiv.org/pdf/2506.19212v3#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2506.19212v3#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2506.19212v3#page=6)
- 다양한 관절 물체의 조작을 시뮬레이션에서 비교하고 실제 로봇 손에서 RGB-D 관측과 언어 지시로 같은 방식을 적용했다. [PDF 7쪽](https://arxiv.org/pdf/2506.19212v3#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2506.19212v3#page=8) · [PDF 9쪽](https://arxiv.org/pdf/2506.19212v3#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 23 (Figure/Table caption) |
| Embodiment/environment | The low-level policy is trained entirely in simulation using a digital twin of the real-world environment, and then executed in the real-world, conditioned on the generated trajectories. | hardware/simulator version and reset protocol | p. 9 (4 Experiments), p. 9 (4 Experiments) |
| Dataset/benchmark | 4.1 Experimental Setup Task Suite We construct an evaluation suite using the ManiSkill simulator [45, 62] and Allegro Hand model designed to evaluate four core dexterous manipulation capabilities for which motion planning ... | role, split, size and leakage | p. 9 (4 Experiments), p. 9 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Metric | Figure 9: Results on the simulation task suite. Success rate (in %) is averaged across three seeds; uncertainty reflects the standard error. Our method performs comparably to the oracle with perfectly scripted ... | definition, denominator, direction and uncertainty | p. 22 (Figure/Table caption), p. 23 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Baseline/ablation | Figure 3: A depiction of the eight tasks used for evaluation. Each task belongs to one of four overarching categories. Methods Given the novelty of our problem setting, there are few applicable ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 7 (4 Experiments), p. 22 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 4 Experiments - extractive body cue:** To comprehensively evaluate the failure modes of our pipeline across all tasks, we present a Sankey diagram in Fig.
- **p. 8 / 4 Experiments - extractive body cue:** Our analysis reveals that the most significant failure mode is incomplete trajectory tracking, occurring in 26% of the rollouts.
- **p. 22 / Figure/Table caption - extractive body cue:** Figure 9: Results on the simulation task suite. Success rate (in %) is averaged across three seeds; uncertainty reflects the standard error. Our method performs ...
- **p. 6 / 4 Experiments - extractive body cue:** We conduct a comprehensive suite of experiments to assess the effectiveness, generality, and robustness of our method across a diverse range of dexterous manipulation tasks.
- **p. 7 / 4 Experiments - extractive body cue:** 3) What causes VLM scaffolds to fail?
- **p. 7 / 4 Experiments - extractive body cue:** We compare against additional reinforcement learning and imitation learning baselines and additionally ablate adding systematic noise into VLM predictions in Section E We evaluate two ...
- **p. 9 / 4 Experiments - extractive body cue:** Robustness to discrepancies in physical parameters is achieved through domain randomization in simulation.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 Introduction), p. 2 (1 Introduction), p. 5 (2. Plan Generation 𝜏)이다.
