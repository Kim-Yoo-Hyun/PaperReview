# Method - Geometry-aware RL for Manipulation of Varying Shapes and Deformable Objects

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (30 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=7BLXhmWvwF; PDF retrieval source: https://arxiv.org/pdf/2502.07005. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 3 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 6 (3 METHODOLOGY)): To handle the complexities of robotic manipulation, where actuators and objects play distinct roles, we propose the Heterogeneous Equivariant Policy (HEPi), which comprises three key components: • Equivariant MPN backbone: ...

## Method Body Digest

- **p. 3 / 3 METHODOLOGY - extractive body cue:** To handle the complexities of robotic manipulation, where actuators and objects play distinct roles, we propose the Heterogeneous Equivariant Policy (HEPi), which comprises three key ...
- **p. 5 / 3 METHODOLOGY - extractive body cue:** These node features may differ from those used in the policy network to capture task-specific observations.
- **p. 5 / 3 METHODOLOGY - extractive body cue:** Trust-Region Projection Layers Standard on-policy reinforcement learning approaches such as Proximal Policy Optimization (PPO) (Schulman et al., 2017), learn a policy by optimizing the surrogate ...
- **p. 3 / 3 METHODOLOGY - extractive body cue:** Problem Statement We aim to solve robotic manipulation problems using an on-policy actorcritic reinforcement learning approach.
- **p. 4 / 3 METHODOLOGY - extractive body cue:** Furthermore, to improve computational efficiency, the kernel function is factorized as: kθ([(pu, ou), (pv, ov)]) = K(3) θ k(2) θ (o⊤ v ou) k(1) θ ...
- **p. 6 / 3 METHODOLOGY - extractive body cue:** The variety of tasks highlights the need for policies that can understand the geometric structure in large observation and action spaces. for MPNN + VNLocal ...
- **p. 4 / 3 METHODOLOGY - extractive body cue:** While these operations guarantee equivariance, they also introduce high computational complexity, making them impractical for reinforcement learning settings.
- **p. 5 / 3 METHODOLOGY - extractive body cue:** TRPL projects policy parameters onto trust region boundaries using a differentiable convex optimization, ensuring stability by projecting both the mean and variance of the Gaussian ...

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To evaluate our approach and future advancements in this direction, we propose a novel suite of seven tasks, realized using NIVIDA IsaacLab (Mittal et al., ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The architecture's equivariance allows generalizing between poses and its heterogeneity enables us to include and exploit knowledge about the scene as well as the unactuated ...
- **p. 3 / 3 METHODOLOGY - extractive body cue:** To handle the complexities of robotic manipulation, where actuators and objects play distinct roles, we propose the Heterogeneous Equivariant Policy (HEPi), which comprises three key ...

## Source Evidence Cues

- **p. 3 / 3 METHODOLOGY - extractive body cue:** To handle the complexities of robotic manipulation, where actuators and objects play distinct roles, we propose the Heterogeneous Equivariant Policy (HEPi), which comprises three key ...
- **p. 5 / 3 METHODOLOGY - extractive body cue:** These node features may differ from those used in the policy network to capture task-specific observations.
- **p. 5 / 3 METHODOLOGY - extractive body cue:** Trust-Region Projection Layers Standard on-policy reinforcement learning approaches such as Proximal Policy Optimization (PPO) (Schulman et al., 2017), learn a policy by optimizing the surrogate ...
- **p. 3 / 3 METHODOLOGY - extractive body cue:** Problem Statement We aim to solve robotic manipulation problems using an on-policy actorcritic reinforcement learning approach.
- **p. 4 / 3 METHODOLOGY - extractive body cue:** Furthermore, to improve computational efficiency, the kernel function is factorized as: kθ([(pu, ou), (pv, ov)]) = K(3) θ k(2) θ (o⊤ v ou) k(1) θ ...
- **p. 6 / 3 METHODOLOGY - extractive body cue:** The variety of tasks highlights the need for policies that can understand the geometric structure in large observation and action spaces. for MPNN + VNLocal ...
- **p. 4 / 3 METHODOLOGY - extractive body cue:** While these operations guarantee equivariance, they also introduce high computational complexity, making them impractical for reinforcement learning settings.
- **Detected method headings:** 3 METHODOLOGY (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Data schema / normalization | heterogeneous robot trajectory를 공통 sample로 만든다 | observation, action, task와 embodiment metadata | sensor/action schema alignment, filtering, normalization을 수행 | shared dataset representation | To handle the complexities of robotic manipulation, where actuators and objects play distinct roles, we propose the Heterogeneous Equivariant Policy (HEPi), which ... | p. 3 (3 METHODOLOGY), p. 5 (3 METHODOLOGY) |
| Coverage / augmentation | task·embodiment·failure variation을 확장한다 | dataset과 metadata | retargeting, relabeling, synthetic/teleoperation augmentation 또는 sampling을 적용 | expanded data support | These node features may differ from those used in the policy network to capture task-specific observations. | p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY) |
| Downstream learning interface | 정규화된 data를 policy/representation이 사용한다 | shared observations/actions | pretraining, BC, action-token 또는 representation learning을 수행 | checkpoint/policy action | Trust-Region Projection Layers Standard on-policy reinforcement learning approaches such as Proximal Policy Optimization (PPO) (Schulman et al., 2017), learn a policy by ... | p. 5 (3 METHODOLOGY), p. 3 (3 METHODOLOGY) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3 METHODOLOGY - extractive body cue:** Trust-Region Projection Layers Standard on-policy reinforcement learning approaches such as Proximal Policy Optimization (PPO) (Schulman et al., 2017), learn a policy by optimizing the surrogate ...
- **p. 5 / 3 METHODOLOGY - extractive body cue:** TRPL projects policy parameters onto trust region boundaries using a differentiable convex optimization, ensuring stability by projecting both the mean and variance of the Gaussian ...
- **p. 3 / 3 METHODOLOGY - extractive body cue:** To handle the complexities of robotic manipulation, where actuators and objects play distinct roles, we propose the Heterogeneous Equivariant Policy (HEPi), which comprises three key ...
- **p. 4 / 3 METHODOLOGY - extractive body cue:** This leads to the convolutional message-passing update rule, f ′ v = P u∈N(v) k(xu -xv)fu.
- **p. 4 / 3 METHODOLOGY - extractive body cue:** Consider the message function in Equation 1, where ψ(f (k) v , f (k) u , euv) = k(xu-xv)fu is defined as a linear function ...
- **p. 6 / 3 METHODOLOGY - extractive body cue:** These tasks require precise control under complex geometric constraints, coordination between multiple actuators, and handling of intricate interactions between objects and actuators.
- **Formal bridge:** trajectory D with task/embodiment metadata -> normalized sample or downstream action -> coverage/data efficiency/transfer objective -> cross-domain transfer and task performance.
- **Equation/algorithm anchors:** p. 5 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 6 (3 METHODOLOGY), p. 3 (3 METHODOLOGY), p. 4 (3 METHODOLOGY).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Right, Overview, Heterogeneous, Equivariant, Policy, HEPi, consisting, multiple, Message, Passing, Networks, EMPNs, process, graph | multi-view observation, language/task label과 action trajectory | body cue; exact tensor/frame verify |
| State/latent | Right, Overview, Heterogeneous, Equivariant, Policy, HEPi, consisting, multiple, Message, Passing | shared representation, embodiment/task identity와 data distribution | body cue; notation verify |
| Action/output | evaluate, future, advancements, direction, novel, suite, seven, tasks, realized, NIVIDA | dataset sample 또는 learned policy action | body cue; unit/decoder verify |
| Objective/constraint | Trust-Region, Projection, Layers, Standard, on-policy, reinforcement, learning, approaches, Proximal, Policy | coverage/data efficiency/transfer objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Right: Overview of Heterogeneous Equivariant Policy (HEPi), consisting of multiple Equivariant Message Passing Networks (EMPNs) process the graph, and the outputs are aggregated to generate ...
- **p. 3 / 2 BACKGROUND - extractive body cue:** In MDPs with symmetries, both the transition distribution P(s′/s, a) and policy distribution π(a/s) are invariant under group transformations g ∈G via left-regular representation Lg ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** An exception is the recent Equibot (Yang et al., 2024), where the policy outputs velocity vectors rather than static end-effector poses, enabling success in more ...
- **p. 3 / 3 METHODOLOGY - extractive body cue:** Problem Statement We aim to solve robotic manipulation problems using an on-policy actorcritic reinforcement learning approach.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Yet, this representation results in high-dimensional observation and action spaces, which makes learning policies that generalize seamlessly to novel orientations, poses, and unseen geometries challenging.
- **p. 5 / 3 METHODOLOGY - extractive body cue:** These node features may differ from those used in the policy network to capture task-specific observations.
- **p. 5 / 3 METHODOLOGY - extractive body cue:** Value Function We employ DeepSets (Zaheer et al., 2017) with the same input structure as the policy to preserve permutation invariance of the node features, ...
- **Normalized interface:** observation=multi-view observation, language/task label과 action trajectory; state=shared representation, embodiment/task identity와 data distribution; output/action=dataset sample 또는 learned policy action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | trajectory demonstration horizon; training sample window와 deployment task horizon을 분리한다. | (2024) introduced the PONITA framework, an efficient equivariant message-passing approach. | episode/sequence/action-chunk boundary |
| Rate / latency | data recording/action sampling rate와 policy inference/control rate를 분리한다. | In this experiment, we examine the impact of adding attention as an aggregation function in Equation 1 to both homogeneous and heterogeneous ... | Hz/fps, inference time and control rate |
| Memory | trajectory, embodiment/task metadata와 dataset index. | not recovered | window and reset |
| Compute | data decoding, normalization/augmentation과 downstream training budget이 결정한다. | 4.2 RESULTS AND DISCUSSIONS In the main evaluations, we generate 1000 scenes per task (sampled according to Appendix B) and compute the ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3 METHODOLOGY - extractive body cue:** To handle the complexities of robotic manipulation, where actuators and objects play distinct roles, we propose the Heterogeneous Equivariant Policy (HEPi), which comprises three key ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Adding attention significantly increases the training time but does not improve performance, as shown on the right.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Additionally, adding attention significantly increases training time without improving performance, e.g., for HEPi it almost doubled.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** handle, complexities, robotic, manipulation, where, actuators, objects, play, distinct, roles, Heterogeneous, Equivariant, Policy, HEPi, comprises, three, components, MPN, backbone, efficient.
- **Relevant PDF headings:** 3 METHODOLOGY (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data schema / normalization | Overall, HEPi generalizes well to unseen objects, performs consistently across resolutions, and handles noise effectively, making it suitable for real-world tasks. | p. 8 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Coverage / augmentation | Figure 3: Evaluation curves for our seven manipulation tasks, comparing HEPi (ours), EMPN, and Transformer baselines. Results are averaged over 10 seeds, ... | p. 7 (Figure/Table caption), p. 7 (4 EXPERIMENTS) |
| Downstream learning interface | Figure 4: Performance of different models on the Cloth-Hanging task across varying sample spaces. Overall, performance improves as the sample space decreases. ... | p. 8 (Figure/Table caption), p. 25 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 26 / Figure/Table caption - extractive body cue:** Figure 23: Ablation on different k-nearest neighbors for obj-to-act edges in MPNN + VNLocal (in Section 3.3) updates, evaluated on the Rigid-Insertion task with varying ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** In addition, for the Cloth-Hanging task, we evaluate two additional baselines, Heterogeneous GNN (HeteroGNN) and a naive GNN to highlight the effectiveness of incorporating equivariant ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** GNNs naturally capture locality through message passing, allowing them to scale effectively to higher-resolution graphs without retraining (Li et al., 2020; Freymuth et al., 2023).
- **p. 25 / Figure/Table caption - extractive body cue:** Figure 21: Ablation on different k-nearest neighbors choices for obj-to-act edges in MPNN + VNLocal updates (in Section 3.3), evaluated across multiple tasks: rigid-insertion, rigid-insertion- ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Left: Analysis of noise sensitivity and scalability to high-resolution objects in the Rigid- Pushing task. Heatmaps show average returns under varying levels of ...
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** Next, Rigid-Pushing removes the physical connection between the actuator and the object, allowing the actuator to move freely in the x-y plane to push the ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** For final performance on rigid tasks, firstly in rigid-slding-2D and rigid-insertion-2D+z tasks, HEPi and Transformer policies perform comparably, suggesting that the limited task complexity does ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 3 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 6 (3 METHODOLOGY), objective p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 3 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 6 (3 METHODOLOGY), temporal p. 4 (3 METHODOLOGY), p. 9 (4 EXPERIMENTS), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
