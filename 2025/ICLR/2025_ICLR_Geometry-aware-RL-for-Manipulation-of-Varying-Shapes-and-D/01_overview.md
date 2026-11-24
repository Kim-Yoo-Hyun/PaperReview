# Geometry-aware RL for Manipulation of Varying Shapes and Deformable Objects

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (30 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2025/hash/7571c9d44179c7988178593c5b62a9b6-Abstract-Conference.html.
> PDF retrieval source: https://arxiv.org/pdf/2502.07005. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: Tai Hoang, Huy Le, Philipp Becker, Vien A Ngo, Gerhard Neumann
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Robotics, Reinforcement Learning, SE(3) equivariance, deformable manipulation
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2025/hash/7571c9d44179c7988178593c5b62a9b6-Abstract-Conference.html
- Full-text retrieval: https://arxiv.org/pdf/2502.07005
- Code/Project: https://thobotics.github.io/hepi
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (30 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

HEPi는 구동기와 물체의 서로 다른 상호작용을 그래프로 나타내 강체·변형체의 3차원 조작 정책을 학습한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/7571c9d44179c7988178593c5b62a9b6-Paper-Conference.pdf#page=1)

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

- 노드와 간선 유형별로 구분한 메시지 전달에 SE(3) 등변성을 부여해 장면의 회전·이동에 대응한다. [PDF 2쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/7571c9d44179c7988178593c5b62a9b6-Paper-Conference.pdf#page=2) · [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/7571c9d44179c7988178593c5b62a9b6-Paper-Conference.pdf#page=4)
- 다양한 형상의 삽입과 밧줄·천 조작으로 평가 환경을 구성해 여러 정책의 학습 효율과 반환값을 비교한다. [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/7571c9d44179c7988178593c5b62a9b6-Paper-Conference.pdf#page=6) · [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/7571c9d44179c7988178593c5b62a9b6-Paper-Conference.pdf#page=7)

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

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 3 (2 BACKGROUND), p. 3 (3 METHODOLOGY)이다.
