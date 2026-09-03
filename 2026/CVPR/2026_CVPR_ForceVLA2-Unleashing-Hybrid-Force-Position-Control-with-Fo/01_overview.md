# ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Li_ForceVLA2_Unleashing_Hybrid_Force-Position_Control_with_Force_Awareness_for_Contact-Rich_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_ForceVLA2_Unleashing_Hybrid_Force-Position_Control_with_Force_Awareness_for_Contact-Rich_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, VLA, force sensing, hybrid force-position control, contact-rich manipulation
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Li_ForceVLA2_Unleashing_Hybrid_Force-Position_Control_with_Force_Awareness_for_Contact-Rich_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_ForceVLA2_Unleashing_Hybrid_Force-Position_Control_with_Force_Awareness_for_Contact-Rich_CVPR_2026_paper.pdf
- Code/Project: https://openaccess.thecvf.com/content/CVPR2026/html/Li_ForceVLA2_Unleashing_Hybrid_Force-Position_Control_with_Force_Awareness_for_Contact-Rich_CVPR_2026_paper.html
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 tactile 문제를 이해하기 위해 읽는다. 본문은 However, current VLAs still lack the ability to reason about physical dynamics and fine-grained contact interactions, which are essential for real-world, contact-rich manipulation.를 문제로 두고, Our contributions are summarized as follows: • We introduce ForceVLA2, the first end-to-end hybrid force-position control framework with force awareness for VLAs, enhancing contact-rich manipulation by integrating force-prompt-driven VL ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Embodied intelligence for contact-rich manipulation has predominantly relied on position control, while explicit awareness and regulation of interaction forces remain under-explored, limiting stability, precision, and ...
- **p. 1 / Abstract - extractive body cue:** We propose ForceVLA2, an end-to-end vision-language-action framework that equips robots with hybrid force-position control and explicit force awareness.
- **p. 1 / Abstract - extractive body cue:** ForceVLA2 introduces force-based prompts into the VLM expert to construct force-aware task concepts across stages, and employs a Cross-Scale Mixture-of-Experts (MoE) in the action expert ...
- **p. 1 / Abstract - extractive body cue:** To support learning and evaluation, we construct ForceVLA2-Dataset, containing 1,000 trajectories over 5 contact-rich tasks, including wiping, pressing, and assembling, with multi-view images, task prompts, ...
- **p. 1 / Abstract - extractive body cue:** Extensive experiments show that ForceVLA2 substantially improves success rates and reliability in contact-rich manipulation, outperforming π0 and π0.5 by 48.0% and 35.0%, respectively, across the ...
- **p. 2 / 1. Introduction - extractive body cue:** However, current VLAs still lack the ability to reason about physical dynamics and fine-grained contact interactions, which are essential for real-world, contact-rich manipulation.
- **p. 2 / 1. Introduction - extractive body cue:** Current VLAs, however, still lack mechanisms to reason about the spatiotemporal relationships required across different task stages and to integrate force perception with active force-position ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are summarized as follows: • We introduce ForceVLA2, the first end-to-end hybrid force-position control framework with force awareness for VLAs, enhancing contact-rich manipulation ...
- **p. 2 / 1. Introduction - extractive body cue:** To overcome these limitations, we propose ForceVLA2, a novel framework that equips VLAs with active hybrid force-position control with force awareness to enhance contact-rich manipulation, ...
- **p. 1 / Abstract - extractive body cue:** We propose ForceVLA2, an end-to-end vision-language-action framework that equips robots with hybrid force-position control and explicit force awareness.
- **p. 3 / 3.1. Long-Horizon Force Awareness via Prompting - extractive body cue:** To address this, we introduce force prompts as textual cues that indicate the current subtask and encode stage-specific physical context, thereby constructing force-aware task concepts.
- **p. 3 / 3. ForceVLA2 Framework - extractive body cue:** Building upon these principles, we propose the ForceVLA2 architecture, which integrates multi-scale perception, contextual reasoning, and force-aware manipulation into a unified VLA framework.
- **p. 4 / 3.2. Short-Horizon Force-to-Control Loop - extractive body cue:** (3) The encoded EE 6D pose and force tokens are concatenated to form a multi-modal state representation, Estate = [EP ; EF ], which is ...
- **p. 5 / 3.2.2. Adaptive Routing and Decoding - extractive body cue:** By conditioning the denoising process on the fused visual-language-force representation, the model achieves closed-loop, context-aware control that adapts fluidly to contact-rich interaction.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Contact-rich manipulation requires force regulation, beyond visual and state observations (left).

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | A 6D force/torque sensor attached to the end-effector recorded interaction forces at 300 Hz, while the robot joint states and end-effector (EE) 6D poses were logged synchronously. | tactile image/force, vision과 proprioceptive history | p. 5 (4. ForceVLA2-Dataset), p. 4 (3.1. Long-Horizon Force Awareness via Prompting) |
| State/latent | force/torque, sensor, attached, end-effector, recorded, interaction, forces, while, robot, joint, states, poses | contact geometry, force state 또는 latent dynamics | p. 5 (4. ForceVLA2-Dataset), p. 4 (3.1. Long-Horizon Force Awareness via Prompting), p. 3 (3. ForceVLA2 Framework) |
| Output/action | ForceVLA2 takes multi-view images, task and force prompts, and proprioceptive states (EE pose and force) as input. | grasp/contact action, force command 또는 object motion | p. 4 (3.1. Long-Horizon Force Awareness via Prompting), p. 3 (3. ForceVLA2 Framework), p. 3 (3.1. Long-Horizon Force Awareness via Prompting) |
| Objective/outcome | In parallel, force observation bypasses high-level fusion and modulates the action expert via a direct gradient pathway, enabling a reactive response to observed force during contact (Sec. | slip/contact success, force/pose error와 robustness | p. 3 (3. ForceVLA2 Framework), p. 4 (3.2. Short-Horizon Force-to-Control Loop), p. 5 (3.2.2. Adaptive Routing and Decoding) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are summarized as follows: • We introduce ForceVLA2, the first end-to-end hybrid force-position control framework with force awareness for VLAs, enhancing contact-rich manipulation ...
- **p. 2 / 1. Introduction - extractive body cue:** To overcome these limitations, we propose ForceVLA2, a novel framework that equips VLAs with active hybrid force-position control with force awareness to enhance contact-rich manipulation, ...
- **p. 1 / Abstract - extractive body cue:** We propose ForceVLA2, an end-to-end vision-language-action framework that equips robots with hybrid force-position control and explicit force awareness.
- **p. 3 / 3.1. Long-Horizon Force Awareness via Prompting - extractive body cue:** To address this, we introduce force prompts as textual cues that indicate the current subtask and encode stage-specific physical context, thereby constructing force-aware task concepts.
- **p. 3 / 3. ForceVLA2 Framework - extractive body cue:** Building upon these principles, we propose the ForceVLA2 architecture, which integrates multi-scale perception, contextual reasoning, and force-aware manipulation into a unified VLA framework.
- **p. 6 / 5.2. Main Experiment Results - extractive body cue:** 1, ForceVLA2 significantly outperforms all baselines, achieving a 66% average success rate across all tasks.
- **p. 7 / 5.2. Main Experiment Results - extractive body cue:** The ACP achieves a success rate of only 16.0%, primarily due to its limited generalization capabilities.
- **p. 6 / 5. Experiments - extractive body cue:** The experiments address the following research questions: • Q1: How does ForceVLA2 perform in real-world contact-rich manipulation tasks, and what specific advantages and technical benefits ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (5.2. Main Experiment Results), p. 7 (5.2. Main Experiment Results) |
| Embodiment/environment | Our experimental benchmark consists of 5 contact-rich manipulation tasks within the proposed ForceVLA2-Dataset: Press the bottle, Clean the vase, Clean the board, Retrieve the plate, and Assemble gears. | hardware/simulator version and reset protocol | p. 6 (5.1. Experiment Setting), p. 5 (4. ForceVLA2-Dataset) |
| Dataset/benchmark | The collected dataset constitutes a multi-modal corpus encompassing visual, proprioceptive, task-prompt, force-prompt, and force modalities. | role, split, size and leakage | p. 6 (5.1. Experiment Setting), p. 5 (4. ForceVLA2-Dataset), p. 5 (4. ForceVLA2-Dataset), p. 6 (4. ForceVLA2-Dataset) |
| Metric | 1, ForceVLA2 significantly outperforms all baselines, achieving a 66% average success rate across all tasks. | definition, denominator, direction and uncertainty | p. 6 (5.2. Main Experiment Results), p. 6 (5.1. Experiment Setting), p. 7 (5.2. Main Experiment Results) |
| Baseline/ablation | 1, ForceVLA2 significantly outperforms all baselines, achieving a 66% average success rate across all tasks. | fair input/data/compute/action matching | p. 6 (5.2. Main Experiment Results), p. 8 (5.2. Main Experiment Results), p. 6 (5.2. Main Experiment Results) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 6. Conclusion - extractive body cue:** The model also consistently reduces failures caused by arm overload and unstable contact, and ablation studies show monotonically improved performance as force prompts, the CrossScale ...
- **p. 8 / 5.2. Main Experiment Results - extractive body cue:** In contrast, other VLAs slowly chase the new EE 6D pose, leading to failure to maintain stable contact.
- **p. 7 / 5.2. Main Experiment Results - extractive body cue:** ForceVLA2 exhibits robust position and orientation following, and in object search tasks, it can still perform successful re-grasps even when visual observations fail. on force-sensitive ...

## Why Read It

Manipulation, contact, tactile, and dexterity의 tactile 문제를 이해하기 위해 읽는다. 본문은 However, current VLAs still lack the ability to reason about physical dynamics and fine-grained contact interactions, which are essential for real-world, contact-rich manipulation.를 문제로 두고, Our contributions are summarized as follows: • We introduce ForceVLA2, the first end-to-end hybrid force-position control framework with force awareness for VLAs, enhancing contact-rich manipulation by integrating force-prompt-driven VL ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. Short-Horizon Force-to-Control Loop) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (10 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, these models remain confined to virtual domains, lacking the embodiment necessary for authentic physical understanding and interaction in real-world settings. (p. 1, 1. Introduction).
- **Actual contribution:** To overcome these limitations, we propose ForceVLA2, a novel framework that equips VLAs with active hybrid force-position control with force awareness to enhance contact-rich manipulation, as shown in Fig. (p. 2, 1. Introduction).
- **Evaluation boundary:** Entries indicate success rate (%). gray : baseline results. (p. 8, 5.2. Main Experiment Results).
- **Explicit failure boundary:** ForceVLA2 exhibits robust position and orientation following, and in object search tasks, it can still perform successful re-grasps even when visual observations fail. on force-sensitive tasks such as object search, ... (p. 7, 5.2. Main Experiment Results).
