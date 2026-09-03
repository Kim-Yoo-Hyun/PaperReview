# TIC-VLA: A Think-in-Control Vision-Language-Action Model for Robot Navigation in Dynamic Environments

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=9wYjjPydfe.
> PDF retrieval source: https://openreview.net/pdf/111f8ac3ef90d847bb2191b2bd71a573458c6810.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics, Navigation, Reinforcement Learning
- Official paper: https://openreview.net/forum?id=9wYjjPydfe
- Full-text retrieval: https://openreview.net/pdf/111f8ac3ef90d847bb2191b2bd71a573458c6810.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, existing VLA systems rely on a hidden and impractical assumption: reasoning and control are temporally aligned.를 문제로 두고, To this end, we introduce Think-in-Control (TIC)-VLA, a latency-aware framework that explicitly exposes inference delay to the control policy.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Robots in dynamic, human-centric environments must follow language instructions while maintaining real-time reactive control.
- **p. 1 / Abstract - extractive body cue:** Vision-languageaction (VLA) models offer a promising framework, but they assume temporally aligned reasoning and control, despite semantic inference being inherently delayed relative to real-time action.
- **p. 1 / Abstract - extractive body cue:** We introduce Think-in-Control (TIC)-VLA, a latency-aware framework that explicitly models delayed semantic reasoning during action generation.
- **p. 1 / Abstract - extractive body cue:** TIC-VLA defines a delayed semanticcontrol interface that conditions action generation on delayed vision-language semantic states and explicit latency metadata, in addition to current observations, enabling ...
- **p. 1 / Abstract - extractive body cue:** We further propose a latency-consistent training pipeline that injects reasoning inference delays during imitation learning and online reinforcement learning, aligning training with asynchronous deployment.
- **p. 1 / 1. Introduction - extractive body cue:** However, existing VLA systems rely on a hidden and impractical assumption: reasoning and control are temporally aligned.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** As a result, semantic outputs may become temporally misaligned with the agent's current observations and state, creating a key challenge for real-time navigation.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To this end, we introduce Think-in-Control (TIC)-VLA, a latency-aware framework that explicitly exposes inference delay to the control policy.
- **p. 1 / 1. Introduction - extractive body cue:** TIC-VLA enables real-time, language-conditioned navigation by decoupling slow vision-language reasoning from fast reactive control via a delayed semantic-control interface.
- **p. 2 / 1. Introduction - extractive body cue:** The primary contributions can be summarized as:
- **p. 4 / 3.2. Think-in-Control VLA - extractive body cue:** This latency-aware semantic-control coupling enables robust navigation despite asynchronous and delayed reasoning updates.
- **p. 4 / 3.2. Think-in-Control VLA - extractive body cue:** Crucially, rather than treating this as an architectural contribution, we explicitly model the resulting inference delay as part of the control problem.
- **p. 5 / 3.3. Latency-Consistent Training Pipeline - extractive body cue:** Pooling Concatenate Value State + Goal MLP MLP (a) (b) +++ Asynchronous Inference in Closed-loop Multi-stage Training IL with Delayed Inference VLM SFT (d) (c) ...
- **p. 5 / 3.3. Latency-Consistent Training Pipeline - extractive body cue:** The value network, shown in Figure 3(b), takes as input the current image tokens, the goal position, and the robot state, and outputs the Pos.
- **p. 4 / 3.2. Think-in-Control VLA - extractive body cue:** Visual tokens and VLM cache features are first projected into a shared latent space via MLP layers, while the robot state and latency metadata are ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Specifically, we sample reasoning delays ∆t uniformly from [0, 10] seconds and condition the policy on: (1) the current image input and robot state, (2) KV cache features from the delayed VLM ... | camera/depth stream, pose, map와 language goal | p. 5 (3.3. Latency-Consistent Training Pipeline), p. 3 (3.1. Problem Formulation) |
| State/latent | Specifically, sample, reasoning, delays, uniformly, seconds, condition, policy, current, image, input, robot | robot pose, free-space/semantic map와 local goal | p. 5 (3.3. Latency-Consistent Training Pipeline), p. 3 (3.1. Problem Formulation), p. 5 (3.3. Latency-Consistent Training Pipeline) |
| Output/action | At each control timestep t, the agent receives: (1) a natural language instruction and context I, specifying the navigation goal and historical trajectory; (2) an egocentric observation history Ot = {x0, . ... | collision-free trajectory 또는 velocity command | p. 3 (3.1. Problem Formulation), p. 5 (3.3. Latency-Consistent Training Pipeline), p. 3 (3.1. Problem Formulation) |
| Objective/outcome | We optimize the standard autoregressive crossentropy loss over the target token sequence: Ll = -1 Nl Nl X t=1 log pϕ(yt / y<t, I, V), (3) where yt denotes the t-th token ... | goal reach, safety, localization error와 replanning latency | p. 5 (3.3. Latency-Consistent Training Pipeline), p. 5 (3.3. Latency-Consistent Training Pipeline), p. 3 (3.1. Problem Formulation) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** To this end, we introduce Think-in-Control (TIC)-VLA, a latency-aware framework that explicitly exposes inference delay to the control policy.
- **p. 1 / 1. Introduction - extractive body cue:** TIC-VLA enables real-time, language-conditioned navigation by decoupling slow vision-language reasoning from fast reactive control via a delayed semantic-control interface.
- **p. 2 / 1. Introduction - extractive body cue:** The primary contributions can be summarized as:
- **p. 4 / 3.2. Think-in-Control VLA - extractive body cue:** This latency-aware semantic-control coupling enables robust navigation despite asynchronous and delayed reasoning updates.
- **p. 4 / 3.2. Think-in-Control VLA - extractive body cue:** Crucially, rather than treating this as an architectural contribution, we explicitly model the resulting inference delay as part of the control problem.
- **p. 7 / 4.2. Simulation Testing - extractive body cue:** After RL fine-tuning, TICVLA achieves the highest success rate and the lowest collision rate, indicating improved closed-loop robustness in dynamic scenes.
- **p. 8 / 4.2. Simulation Testing - extractive body cue:** The effect of VLM asynchronous reasoning inference latency in TIC-VLA on task performance. fine-tuned policy maintains consistently higher success rates across all latency settings, demonstrating ...
- **p. 8 / 4.2. Simulation Testing - extractive body cue:** As shown in Table 2, using KV-cache features significantly improves navigation success, and latencyawareness enhances performance under asynchronous inference.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (4.2. Simulation Testing), p. 8 (4.2. Simulation Testing) |
| Embodiment/environment | We train the model using three datasets featuring dynamic human-robot interactions: (1) SCAND (Karnan et al., 2022), which contains 8.7 hours of robot-driven trajectories across diverse social environments; (2) GND (Liang et ... | hardware/simulator version and reset protocol | p. 6 (4.1. Experimental Setup), p. 9 (4.4. Ablation Study) |
| Dataset/benchmark | The navigation policy is executed on a Unitree Go2 quadruped robot in real-world navigation tasks. | role, split, size and leakage | p. 6 (4.1. Experimental Setup), p. 9 (4.4. Ablation Study), p. 7 (4.1. Experimental Setup), p. 8 (4.3. Real-world Testing) |
| Metric | TIC-VLA demonstrates effective semantic reasoning while producing reactive navigation actions in dynamic scenarios. the agent and the goal; (2) Success Rate (SR): the percentage of episodes in which the agent stops within ... | definition, denominator, direction and uncertainty | p. 7 (4.1. Experimental Setup), p. 9 (4.4. Ablation Study), p. 9 (4.4. Ablation Study) |
| Baseline/ablation | Without RL finetuning, TIC-VLA is competitive with NavDP, a point-goal method with privileged state access, and outperforms the vanilla BC and RL baselines. | fair input/data/compute/action matching | p. 7 (4.2. Simulation Testing), p. 7 (4.2. Simulation Testing), p. 6 (4.1. Experimental Setup) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.1. Experimental Setup - extractive body cue:** An episode is considered a failure if manual intervention is required to prevent collisions.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Although the non-reasoning variant has a lower collision rate, this mainly reflects reduced activity and more frequent failure rather than safer navigation.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. The effect of VLM asynchronous reasoning inference latency in TIC-VLA on task performance. fine-tuned policy maintains consistently higher success rates across all latency ...
- **p. 9 / 5. Conclusions - extractive body cue:** TIC-VLA has three main limitations.
- **p. 7 / 4.2. Simulation Testing - extractive body cue:** After RL fine-tuning, TICVLA achieves the highest success rate and the lowest collision rate, indicating improved closed-loop robustness in dynamic scenes.
- **p. 9 / 5. Conclusions - extractive body cue:** Third, extending beyond navigation to domains such as robotic manipulation remains future work.
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 10. Online reinforcement learning tasks used to train TIC-VLA across three environments and tasks. The weights for the reward function (Equation (5)) are set ...

## Why Read It

VLA and generalist robot policies의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, existing VLA systems rely on a hidden and impractical assumption: reasoning and control are temporally aligned.를 문제로 두고, To this end, we introduce Think-in-Control (TIC)-VLA, a latency-aware framework that explicitly exposes inference delay to the control policy.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 3 (3.1. Problem Formulation), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.3. Latency-Consistent Training Pipeline) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
