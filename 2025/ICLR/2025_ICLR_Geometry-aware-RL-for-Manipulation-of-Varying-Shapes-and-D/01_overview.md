# Geometry-aware RL for Manipulation of Varying Shapes and Deformable Objects

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (30 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=7BLXhmWvwF.
> PDF retrieval source: https://arxiv.org/pdf/2502.07005. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Robotics, Reinforcement Learning, SE(3) equivariance, deformable manipulation
- Official paper: https://openreview.net/forum?id=7BLXhmWvwF
- Full-text retrieval: https://arxiv.org/pdf/2502.07005
- Code/Project: https://thobotics.github.io/hepi
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (30 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 robot_data 문제를 이해하기 위해 읽는다. 본문은 They are designed to highlight the role of geometric structure in manipulation tasks, with a progressive increase in difficulty, from simple rigid-body manipulation with diverse objects to more challenging tasks involving multiple ...를 문제로 두고, To evaluate our approach and future advancements in this direction, we propose a novel suite of seven tasks, realized using NIVIDA IsaacLab (Mittal et al., 2023) to utilize its GPU-based simulation engine.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Manipulating objects with varying geometries and deformable objects is a major challenge in robotics.
- **p. 1 / ABSTRACT - extractive body cue:** Tasks such as insertion with different objects or cloth hanging require precise control and effective modelling of complex dynamics.
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we frame this problem through the lens of a heterogeneous graph that comprises smaller sub-graphs, such as actuators and objects, accompanied by ...
- **p. 1 / ABSTRACT - extractive body cue:** This graph representation serves as a unified structure for both rigid and deformable objects tasks, and can be extended further to tasks comprising multiple actuators.
- **p. 1 / ABSTRACT - extractive body cue:** To evaluate this setup, we present a novel and challenging reinforcement learning benchmark, including rigid insertion of diverse objects, as well as rope and cloth ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** They are designed to highlight the role of geometric structure in manipulation tasks, with a progressive increase in difficulty, from simple rigid-body manipulation with diverse ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Unlike supervised imitation, training policies with reinforcement learning presents additional challenges, particularly due to the need for high-frequency data collection and efficient adaptation to new ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To evaluate our approach and future advancements in this direction, we propose a novel suite of seven tasks, realized using NIVIDA IsaacLab (Mittal et al., ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The architecture's equivariance allows generalizing between poses and its heterogeneity enables us to include and exploit knowledge about the scene as well as the unactuated ...
- **p. 3 / 3 METHODOLOGY - extractive body cue:** To handle the complexities of robotic manipulation, where actuators and objects play distinct roles, we propose the Heterogeneous Equivariant Policy (HEPi), which comprises three key ...
- **p. 5 / 3 METHODOLOGY - extractive body cue:** For actuator nodes, the output consists of both a scalar c and a vector vout, where the final output vector is computed as vout = ...
- **p. 4 / 3 METHODOLOGY - extractive body cue:** Our approach captures these roles by first processing local information within the object and actuator clusters and then aggregating it globally to the actuators via ...
- **p. 5 / 3 METHODOLOGY - extractive body cue:** These node features may differ from those used in the policy network to capture task-specific observations.
- **p. 5 / 3 METHODOLOGY - extractive body cue:** Trust-Region Projection Layers Standard on-policy reinforcement learning approaches such as Proximal Policy Optimization (PPO) (Schulman et al., 2017), learn a policy by optimizing the surrogate ...
- **p. 3 / 3 METHODOLOGY - extractive body cue:** Problem Statement We aim to solve robotic manipulation problems using an on-policy actorcritic reinforcement learning approach.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Right: Overview of Heterogeneous Equivariant Policy (HEPi), consisting of multiple Equivariant Message Passing Networks (EMPNs) process the graph, and the outputs are aggregated to generate the final action. to reinforcement learning. | multi-view observation, language/task label과 action trajectory | p. 2 (1 INTRODUCTION), p. 3 (2 BACKGROUND) |
| State/latent | Right, Overview, Heterogeneous, Equivariant, Policy, HEPi, consisting, multiple, Message, Passing, Networks, EMPNs | shared representation, embodiment/task identity와 data distribution | p. 2 (1 INTRODUCTION), p. 3 (2 BACKGROUND), p. 1 (1 INTRODUCTION) |
| Output/action | In MDPs with symmetries, both the transition distribution P(s′/s, a) and policy distribution π(a/s) are invariant under group transformations g ∈G via left-regular representation Lg and Kg for state and action, respectively, ... | dataset sample 또는 learned policy action | p. 3 (2 BACKGROUND), p. 1 (1 INTRODUCTION), p. 3 (3 METHODOLOGY) |
| Objective/outcome | Trust-Region Projection Layers Standard on-policy reinforcement learning approaches such as Proximal Policy Optimization (PPO) (Schulman et al., 2017), learn a policy by optimizing the surrogate objective θk+1 = arg max θ E(s,a)∼πθk ... | coverage, cross-embodiment transfer, data efficiency와 task success | p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 3 (3 METHODOLOGY) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To evaluate our approach and future advancements in this direction, we propose a novel suite of seven tasks, realized using NIVIDA IsaacLab (Mittal et al., ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The architecture's equivariance allows generalizing between poses and its heterogeneity enables us to include and exploit knowledge about the scene as well as the unactuated ...
- **p. 3 / 3 METHODOLOGY - extractive body cue:** To handle the complexities of robotic manipulation, where actuators and objects play distinct roles, we propose the Heterogeneous Equivariant Policy (HEPi), which comprises three key ...
- **p. 5 / 3 METHODOLOGY - extractive body cue:** For actuator nodes, the output consists of both a scalar c and a vector vout, where the final output vector is computed as vout = ...
- **p. 4 / 3 METHODOLOGY - extractive body cue:** Our approach captures these roles by first processing local information within the object and actuator clusters and then aggregating it globally to the actuators via ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Performance of different models on the Cloth-Hanging task across varying sample spaces. Overall, performance improves as the sample space decreases. In terms of ...
- **p. 25 / Figure/Table caption - extractive body cue:** Figure 20: Performance of different models on the Cloth-Hanging task across various sample spaces. Assuming the global scene located at r = [0, 1, 0]T ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Adding attention significantly increases the training time but does not improve performance, as shown on the right.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 25 (Figure/Table caption) |
| Embodiment/environment | Overall, HEPi generalizes well to unseen objects, performs consistently across resolutions, and handles noise effectively, making it suitable for real-world tasks. | hardware/simulator version and reset protocol | p. 8 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Dataset/benchmark | We then introduce a novel task, Rope-Shaping, which increases complexity by requiring the rope to form a specific shape (a "W" from the LASA dataset (Khansari-Zadeh & Billard, 2011)) to a desired ... | role, split, size and leakage | p. 8 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Metric | Full task details, including reward definitions, are provided in Appendix B. | definition, denominator, direction and uncertainty | p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Baseline/ablation | Figure 3: Evaluation curves for our seven manipulation tasks, comparing HEPi (ours), EMPN, and Transformer baselines. Results are averaged over 10 seeds, using IQM with 95% confidence intervals. HEPi consistently outperforms EMPN ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 6 CONCLUSION - extractive body cue:** Limitation In our current setup, we abstract away the robot body, focusing solely on end-effector movements.
- **p. 10 / 6 CONCLUSION - extractive body cue:** This limitation could be addressed by integrating state-of-the-art computer vision techniques to extract keypoints from cameras (Tumanyan et al., 2024; Hou et al., 2024), using ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** As shown in Figure 5 (left), HEPi maintains high performance across resolutions with only mild degradation at higher noise levels, demonstrating its scalability and robustness ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Overall, as depicted in Figure 8, in tasks requiring high exploration such as cloth-hanging-3D, PPO struggles to maintain conservative updates, often resulting in unstable performance.
- **p. 26 / Figure/Table caption - extractive body cue:** Figure 23: Ablation on different k-nearest neighbors for obj-to-act edges in MPNN + VNLocal (in Section 3.3) updates, evaluated on the Rigid-Insertion task with varying ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** For final performance on rigid tasks, firstly in rigid-slding-2D and rigid-insertion-2D+z tasks, HEPi and Transformer policies perform comparably, suggesting that the limited task complexity does ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** However, as shown in Figure 7, attention does not provide any noticeable benefit across the tasks.

## Why Read It

Manipulation, contact, tactile, and dexterity의 robot_data 문제를 이해하기 위해 읽는다. 본문은 They are designed to highlight the role of geometric structure in manipulation tasks, with a progressive increase in difficulty, from simple rigid-body manipulation with diverse objects to more challenging tasks involving multiple ...를 문제로 두고, To evaluate our approach and future advancements in this direction, we propose a novel suite of seven tasks, realized using NIVIDA IsaacLab (Mittal et al., 2023) to utilize its GPU-based simulation engine.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 3 (2 BACKGROUND), p. 3 (3 METHODOLOGY) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
