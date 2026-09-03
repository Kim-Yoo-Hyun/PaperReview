# Scaffolding Dexterous Manipulation with Vision-Language Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (29 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=PdRf0O7baQ.
> PDF retrieval source: https://arxiv.org/pdf/2506.19212.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Vision-Language Model, Robotics, Reinforcement Learning
- Official paper: https://openreview.net/forum?id=PdRf0O7baQ
- Full-text retrieval: https://arxiv.org/pdf/2506.19212.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (29 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 To avoid both data scarcity and the embodiment gap, a combination of reinforcement learning (RL) and sim-to-real transfer has emerged as a promising approach by enabling large-scale experience generation [3].를 문제로 두고, Moreover, we showcase that our method transfers to realworld robotic hands without any human demonstrations or handcrafted rewards.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 1 / Abstract - extractive body cue:** Moreover, we showcase that our method transfers to realworld robotic hands without any human demonstrations or handcrafted rewards.
- **p. 2 / 1 Introduction - extractive body cue:** Building upon this insight, we introduce a framework for learning manipulation policies for dexterous robot hands with VLM-generated motion plans and residual RL.
- **p. 2 / 1 Introduction - extractive body cue:** Across 8 tasks, our method achieves close performance in both success rate and generalization to handcrafted, oracle plans despite requiring no manual reward engineering.
- **p. 1 / Abstract - extractive body cue:** Across a number of simulated tasks involving articulated objects and semantic understanding, we demonstrate that our method is able to learn robust dexterous manipulation policies.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: (Left) The performance of our method as we iteratively refine the high-level policy πh by providing successful plans τ in-context. (Right) The projected ...
- **p. 23 / Figure/Table caption - extractive body cue:** Figure 11: Effect of Gaussian noise on VLM predictions in the simulation task suite. Success rate (in %) is averaged across three seeds; uncertainty indicates ...
- **p. 9 / 4 Experiments - extractive body cue:** The resulting improvements vary across tasks: in the drawer task, the Traj. oracle achieves near perfect performance indicating planning was the bottleneck, however, in the ...
- **p. 8 / 4 Experiments - extractive body cue:** After iterative refinement, the overall success rate improves to 81%.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 To avoid both data scarcity and the embodiment gap, a combination of reinforcement learning (RL) and sim-to-real transfer has emerged as a promising approach by enabling large-scale experience generation [3].를 문제로 두고, Moreover, we showcase that our method transfers to realworld robotic hands without any human demonstrations or handcrafted rewards.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (2. Plan Generation 𝜏), p. 5 (2. Plan Generation 𝜏) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
