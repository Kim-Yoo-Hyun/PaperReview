# LaST$_{0}$: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=lwOoBzJykL.
> PDF retrieval source: https://openreview.net/pdf/0e9ec532d1e01f801ca9bc49e258c05cf3a207f5.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics
- Official paper: https://openreview.net/forum?id=lwOoBzJykL
- Full-text retrieval: https://openreview.net/pdf/0e9ec532d1e01f801ca9bc49e258c05cf3a207f5.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 1, unlike prior explicit CoT-based VLA methods, LaST0 performs reasoning in a compact latent space, enabling the capture of fine-grained physical and robotic dynamics that are difficult to verbalize, while supporting temporally ...를 문제로 두고, Our contributions are summarized as follows: • We propose LaST0, a unified VLA model that enables efficient reason-before-act behavior through a Latent SpatioTemporal CoT, performing reasoning in a compact latent space to ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-Language-Action (VLA) models have recently shown strong generalization, with some approaches seeking to explicitly generate linguistic reasoning traces or predict future observations prior to execution.
- **p. 1 / Abstract - extractive body cue:** However, explicit reasoning typically incurs non-negligible inference latency, which constrains the temporal resolution required for robotic manipulation.
- **p. 1 / Abstract - extractive body cue:** Moreover, such reasoning is confined to the linguistic space, imposing a representational bottleneck that struggles to faithfully capture ineffable physical attributes.
- **p. 1 / Abstract - extractive body cue:** 1State Key Laboratory of Multimedia Information Processing, School of Computer Science.
- **p. 1 / Abstract - extractive body cue:** Specifically, we introduce a token-efficient latent CoT space that models future visual dynamics, 3D structural information, and robot proprioceptive states, and further extends these representations ...
- **p. 2 / 1. Introduction - extractive body cue:** 1, unlike prior explicit CoT-based VLA methods, LaST0 performs reasoning in a compact latent space, enabling the capture of fine-grained physical and robotic dynamics that ...
- **p. 2 / 1. Introduction - extractive body cue:** Despite their demonstrated benefits, explicit CoT VLA methods remain constrained by two fundamental challenges in robotics manipulation.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are summarized as follows: • We propose LaST0, a unified VLA model that enables efficient reason-before-act behavior through a Latent SpatioTemporal CoT, performing ...
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we propose LaST0, a dual-system VLA model that enables efficient reason-before-act behavior through a Latent Spatio-Temporal Chain-of-Thought (CoT).
- **p. 3 / 3.1. Preliminaries - extractive body cue:** Specifically, this control vector consists of 3-DoF for relative positional offsets ([∆x, ∆y, ∆z] ∈R3), 3-DoF for rotation (represented as Euler angles [roll, pitch, yaw] ...
- **p. 3 / 3.2. LaST0 Architecture - extractive body cue:** In our framework, these encoded features fimg serve a dual purpose: the current frame acts as real-time contextual input to the MoT experts, while future ...
- **p. 4 / 3.2. LaST0 Architecture - extractive body cue:** Framework. a) We propose LaST0, a unified VLA model with a dual-system architecture.
- **p. 4 / 3.2. LaST0 Architecture - extractive body cue:** LaST0: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model QKV a) LaST𝟎Architecture QKV t𝒕"𝟏 t𝒕"𝟐 2D Visual Latent 3D Geometric Latent Robot Proprioception Latent LaST CoT ...
- **p. 4 / 3.2. LaST0 Architecture - extractive body cue:** The fast acting expert operates at a higher frequency and generates actions via flow matching, conditioned on high-frequency observations and periodically updated latent representations. b) ...
- **p. 5 / 3.3. Latent Spatio-Temporal Chain-of-Thought - extractive body cue:** To better organize LaST CoT reasoning and action generation, we introduce three special tokens: <latent start>, <latent end>, and a placeholder token <latent pad>.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The fast acting expert operates at a higher frequency and generates actions via flow matching, conditioned on high-frequency observations and periodically updated latent representations. b) We design a spatio-temporal latent space, wher ... | image/video, language instruction, proprioception과 history | p. 4 (3.2. LaST0 Architecture), p. 4 (3.2. LaST0 Architecture) |
| State/latent | fast, acting, expert, operates, higher, frequency, generates, actions, flow, matching, conditioned, high-frequency | language-grounded task state와 action-policy context | p. 4 (3.2. LaST0 Architecture), p. 4 (3.2. LaST0 Architecture), p. 3 (3.1. Preliminaries) |
| Output/action | LaST0: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model QKV a) LaST𝟎Architecture QKV t𝒕"𝟏 t𝒕"𝟐 2D Visual Latent 3D Geometric Latent Robot Proprioception Latent LaST CoT t𝒕"𝑯 "Scoop the egg out of the ... | continuous action, pose 또는 action chunk | p. 4 (3.2. LaST0 Architecture), p. 3 (3.1. Preliminaries), p. 5 (3.4. Dual-System Coordination) |
| Objective/outcome | Specifically, the slow reasoning expert is trained by minimizing the Latent CoT regression loss Llatent, aligning its latent representations with domain5 | instruction following, task success, generalization과 latency | p. 5 (3.5. Training Recipe), p. 5 (3.3. Latent Spatio-Temporal Chain-of-Thought), p. 4 (3.2. LaST0 Architecture) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are summarized as follows: • We propose LaST0, a unified VLA model that enables efficient reason-before-act behavior through a Latent SpatioTemporal CoT, performing ...
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we propose LaST0, a dual-system VLA model that enables efficient reason-before-act behavior through a Latent Spatio-Temporal Chain-of-Thought (CoT).
- **p. 3 / 3.1. Preliminaries - extractive body cue:** Specifically, this control vector consists of 3-DoF for relative positional offsets ([∆x, ∆y, ∆z] ∈R3), 3-DoF for rotation (represented as Euler angles [roll, pitch, yaw] ...
- **p. 3 / 3.2. LaST0 Architecture - extractive body cue:** In our framework, these encoded features fimg serve a dual purpose: the current frame acts as real-time contextual input to the MoT experts, while future ...
- **p. 4 / 3.2. LaST0 Architecture - extractive body cue:** Framework. a) We propose LaST0, a unified VLA model with a dual-system architecture.
- **p. 8 / 4.3. Real-World Experiment - extractive body cue:** As shown in Table 3, LaST0 achieves the best overall performance on realworld manipulation tasks, with a mean success rate of 72% (±3) on Franka ...
- **p. 7 / 15.4 Hz - extractive body cue:** In this suite, LaST0 achieves a 95.6% success rate, outperforming strong baselines such as OpenVLA-OFT (94.5%) and π0.5 (92.4%).
- **p. 7 / 15.4 Hz - extractive body cue:** As shown in Table 2, LaST0 consistently outperforms all baselines, achieving a SOTA mean success rate of 98.1%.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (4.3. Real-World Experiment), p. 7 (15.4 Hz) |
| Embodiment/environment | For the LIBERO (Liu et al., 2024) benchmark, our evaluation leverages its four specialized dataset suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-Long. | hardware/simulator version and reset protocol | p. 6 (4.1. Simulation Experiment), p. 8 (4.3. Real-World Experiment) |
| Dataset/benchmark | For the RLBench benchmark, we evaluate on a diverse set of 10 tasks, conducted in the CoppeliaSim simulation environment. | role, split, size and leakage | p. 6 (4.1. Simulation Experiment), p. 8 (4.3. Real-World Experiment), p. 6 (4.1. Simulation Experiment), p. 8 (4.3. Real-World Experiment) |
| Metric | Beyond the overall average, LaST0 attains the highest success rate on 7 out of 10 tasks, indicating consistent performance gains across diverse manipulation skills. | definition, denominator, direction and uncertainty | p. 6 (4.1. Simulation Experiment), p. 6 (4.1. Simulation Experiment), p. 7 (15.4 Hz) |
| Baseline/ablation | In this suite, LaST0 achieves a 95.6% success rate, outperforming strong baselines such as OpenVLA-OFT (94.5%) and π0.5 (92.4%). | fair input/data/compute/action matching | p. 7 (15.4 Hz), p. 8 (4.3. Real-World Experiment), p. 7 (15.4 Hz) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 4.3. Real-World Experiment - extractive body cue:** We show more comprehensive visualizations in Appendix G and supplementary video, and failure cases in Appendix H.
- **p. 21 / Figure/Table caption - extractive body cue:** Figure 11. Visualization of failure cases on different robot platforms, the task progresses from left to right, and red box highlights the failure positions. H. ...
- **p. 22 / Figure/Table caption - extractive body cue:** Figure 12. Visualization of complete task execution processes by real-world tasks (from left to right). 3) The failure in the third case in the dexterous ...
- **p. 9 / 6. Limitations and Future Work - extractive body cue:** Finally, we will explore reinforcement learning for post-training to enhance the robustness.
- **p. 8 / 4.2. Ablation Study - extractive body cue:** Due to our fast-slow system design, extending the temporal horizon of the latent space does not significantly affect action generation speed.
- **p. 8 / 4.2. Ablation Study - extractive body cue:** Since adding further coverage beyond 4 steps does not significantly improve performance, we chose 4 steps as the final latent temporal coverage.
- **p. 7 / 15.4 Hz - extractive body cue:** While other methods fail to aggregate features from the manipulated objects and the robot, LaST0 exhibits a highly concentrated attention pattern, highlighting its superior spatio-temporal ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 1, unlike prior explicit CoT-based VLA methods, LaST0 performs reasoning in a compact latent space, enabling the capture of fine-grained physical and robotic dynamics that are difficult to verbalize, while supporting temporally ...를 문제로 두고, Our contributions are summarized as follows: • We propose LaST0, a unified VLA model that enables efficient reason-before-act behavior through a Latent SpatioTemporal CoT, performing reasoning in a compact latent space to ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Preliminaries), p. 3 (3.1. Preliminaries), p. 4 (3.2. LaST0 Architecture), p. 4 (3.2. LaST0 Architecture) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
