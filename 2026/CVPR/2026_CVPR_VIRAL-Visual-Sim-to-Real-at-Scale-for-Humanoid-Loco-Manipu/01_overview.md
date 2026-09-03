# VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/He_VIRAL_Visual_Sim-to-Real_at_Scale_for_Humanoid_Loco-Manipulation_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/He_VIRAL_Visual_Sim-to-Real_at_Scale_for_Humanoid_Loco-Manipulation_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: Robotics, humanoid, visual sim-to-real, loco-manipulation, teacher-student learning
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/He_VIRAL_Visual_Sim-to-Real_at_Scale_for_Humanoid_Loco-Manipulation_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/He_VIRAL_Visual_Sim-to-Real_at_Scale_for_Humanoid_Loco-Manipulation_CVPR_2026_paper.pdf
- Code/Project: https://openaccess.thecvf.com/content/CVPR2026/html/He_VIRAL_Visual_Sim-to-Real_at_Scale_for_Humanoid_Loco-Manipulation_CVPR_2026_paper.html
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 Yet, despite rapid progress in hardware and control, current humanoids have delivered limited real, sustained productivity outside of carefully engineered demos [21].를 문제로 두고, Proprioception consists of oprop-priv t = [vt, ωt, gt, at→1, qt, ˙qt, f finger t ] where vt, ωt are base linear and angular velocities, gt is base projected gravity, at→1 is ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** A key barrier to the real-world deployment of humanoid robots is the lack of autonomous loco-manipulation skills.
- **p. 1 / Abstract - extractive body cue:** We introduce VIRAL, a visual sim-to-real framework that learns humanoid loco-manipulation entirely in simulation and deploys it zero-shot to real hardware.
- **p. 1 / Abstract - extractive body cue:** VIRAL follows a teacher-student design: a privileged RL teacher, operating on full state, learns long-horizon loco-manipulation using a delta action space and reference state initialization.
- **p. 1 / Abstract - extractive body cue:** A vision-based student policy is then distilled from the teacher via large-scale simulation with tiled rendering, trained with a mixture of online DAgger and behavior ...
- **p. 1 / Abstract - extractive body cue:** We find that compute scale is critical: scaling simulation to tens of GPUs (up to 64) makes both teacher and student training reliable, while low-compute ...
- **p. 1 / 1. Introduction - extractive body cue:** Yet, despite rapid progress in hardware and control, current humanoids have delivered limited real, sustained productivity outside of carefully engineered demos [21].
- **p. 2 / 1. Introduction - extractive body cue:** In other words, if we treat humanoid mobile manipulation as "just another data problem," the required scale may be prohibitively expensive in practice.

## Core Idea

- **p. 3 / 2.1. Key Elements of Teacher Training - extractive body cue:** Proprioception consists of oprop-priv t = [vt, ωt, gt, at→1, qt, ˙qt, f finger t ] where vt, ωt are base linear and angular velocities, ...
- **p. 2 / 1. Introduction - extractive body cue:** Our goal is not to propose yet another novel RL or sim-to-real algorithm, but to provide a technical recipe on the full stack required to ...
- **p. 4 / 2.2. Key Elements of Student Training - extractive body cue:** For the student's vision backbone, we adopt a state-of-the-art image encoder [61] to extract high-quality RGB features, which are fused with proprioceptive to the policy ...
- **p. 3 / 2.1. Key Elements of Teacher Training - extractive body cue:** At time step t, the teacher ωteacher(at/opriv t ) outputs a high-level command for the low-level WBC policy given privileged observation.
- **p. 4 / 2.2. Key Elements of Student Training - extractive body cue:** This mixed-policy rollout combines the fast initialization of BC with the state-coverage benefits of DAgger, producing a more resilient vision-based controller.
- **p. 5 / 2.2. Key Elements of Student Training - extractive body cue:** We identify scaling up GPUs for both teacher and student training as critical in our ablation studies in Figure 14 and Figure 15.
- **p. 5 / 2.2. Key Elements of Student Training - extractive body cue:** This implementation preserves the simplicity of single-GPU training while enabling near-linear scaling to large clusters for high-throughput visual sim-to-real learning.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Phase 1: In simulation, a privileged RL teacher policy ωteacher receives full-state proprioception and exteroception of the task information and outputs WBC commands. | proprioception, reference pose/motion, visual or language command | p. 2 (1. Introduction), p. 3 (2.1. Key Elements of Teacher Training) |
| State/latent | Phase, simulation, privileged, teacher, policy, receives, full-state, proprioception, exteroception, task, information, outputs | whole-body pose, balance/contact state와 skill/mode | p. 2 (1. Introduction), p. 3 (2.1. Key Elements of Teacher Training), p. 2 (1. Introduction) |
| Output/action | At time step t, the teacher ωteacher(at/opriv t ) outputs a high-level command for the low-level WBC policy given privileged observation. | joint/whole-body action, motion target 또는 task trajectory | p. 3 (2.1. Key Elements of Teacher Training), p. 2 (1. Introduction), p. 3 (2.1. Key Elements of Teacher Training) |
| Objective/outcome | Therefore, we define four key rewards: 1. | tracking, balance, skill/task success와 recovery | p. 3 (2.1. Key Elements of Teacher Training), p. 3 (2.1. Key Elements of Teacher Training), p. 4 (2.1. Key Elements of Teacher Training) |

## Main Claims and Actual Contribution

- **p. 3 / 2.1. Key Elements of Teacher Training - extractive body cue:** Proprioception consists of oprop-priv t = [vt, ωt, gt, at→1, qt, ˙qt, f finger t ] where vt, ωt are base linear and angular velocities, ...
- **p. 2 / 1. Introduction - extractive body cue:** Our goal is not to propose yet another novel RL or sim-to-real algorithm, but to provide a technical recipe on the full stack required to ...
- **p. 6 / 3.1. Robustness - extractive body cue:** These results show that although expert-level success remains challenging, VIRAL achieves near-expert success performance while being faster than the expert, and it substantially outperforms non-experts ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 8. Real-world generalization of VIRAL RGB-based policy under variations in tray and object position, robot start pose, table height and type, tablecloth color, lighting, ...
- **p. 5 / 3. Real-World Results of VIRAL - extractive body cue:** In this section, we present real-world humanoid locomanipulation results achieved by VIRAL.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 15. Scaling compute for student policy training. Distil- lation loss (left) and success rate (right) when training with 1-64 GPUs. Larger GPU counts provide ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 14. Scaling compute for teacher training. Rewards (left) and success rates (right) for 1-16 GPUs. More GPUs yield faster convergence and better asymptotic performance.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 7. Real-world performance comparison: VIRAL matches expert-level reliability, outperforms non-experts, and op- erates faster than the expert teleoperator. ure 3) to ensure that the ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (3.1. Robustness), p. 6 (Figure/Table caption) |
| Embodiment/environment | We assess real-world generalization by systematically varying the environment along multiple factors, including tray start position, robot start pose, table height, lighting, table cloth, table type and color, and object category (Figur ... | hardware/simulator version and reset protocol | p. 6 (3.2. Generalization), p. 6 (3.1. Robustness) |
| Dataset/benchmark | In this section, we present real-world humanoid locomanipulation results achieved by VIRAL. | role, split, size and leakage | p. 6 (3.2. Generalization), p. 6 (3.1. Robustness), p. 5 (3. Real-World Results of VIRAL), p. 5 (3.1. Robustness) |
| Metric | Figure 14. Scaling compute for teacher training. Rewards (left) and success rates (right) for 1-16 GPUs. More GPUs yield faster convergence and better asymptotic performance. | definition, denominator, direction and uncertainty | p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 6 (3.1. Robustness) |
| Baseline/ablation | These results show that although expert-level success remains challenging, VIRAL achieves near-expert success performance while being faster than the expert, and it substantially outperforms non-experts in both reliability and efficienc ... | fair input/data/compute/action matching | p. 6 (3.1. Robustness), p. 5 (Figure/Table caption), p. 6 (3.2. Generalization) |

## Explicit Limitations and Failure Boundary

- **p. 3 / 2.1. Key Elements of Teacher Training - extractive body cue:** Note that VIRAL framework does not have designs overfitting to specific WBC policy, and can be extended to other humanoid WBC controllers [44, 78].
- **p. 3 / 2.1. Key Elements of Teacher Training - extractive body cue:** With a stable and robust WBC policy as an API layer, the action space of VIRAL policy is limited to a safe and reliable region ...
- **p. 4 / 2.1. Key Elements of Teacher Training - extractive body cue:** Visual randomization on image, lighting, material, and camera-extrinsics randomization for sim-to-real robustness.
- **p. 4 / 2.2. Key Elements of Student Training - extractive body cue:** The distinction between DAgger and BC lies solely in the source of observations: teacher rollouts provide clean, near-optimal demonstrations that rapidly imprint strong priors on ...
- **p. 5 / 2.3. Key Elements of Sim-to-Real Transfer - extractive body cue:** To enhance robustness and improve sim-toreal transfer, we apply extensive visual and physical randomization during training (Figure 3).
- **p. 5 / 2.3. Key Elements of Sim-to-Real Transfer - extractive body cue:** We randomize image quality (brightness, contrast, hue, saturation, Gaussian noise, and blur), camera extrinsics to account for small pose shifts, and camera latency to model ...
- **p. 6 / 3.2. Generalization - extractive body cue:** Across these variations, VIRAL consistently completes the task without additional tuning, indicating strong robustness.

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 Yet, despite rapid progress in hardware and control, current humanoids have delivered limited real, sustained productivity outside of carefully engineered demos [21].를 문제로 두고, Proprioception consists of oprop-priv t = [vt, ωt, gt, at→1, qt, ˙qt, f finger t ] where vt, ωt are base linear and angular velocities, gt is base projected gravity, at→1 is ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (2.1. Key Elements of Teacher Training), p. 4 (2.2. Key Elements of Student Training), p. 3 (2.1. Key Elements of Teacher Training) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** In other words, if we treat humanoid mobile manipulation as "just another data problem," the required scale may be prohibitively expensive in practice. (p. 2, 1. Introduction).
- **Actual contribution:** Our goal is not to propose yet another novel RL or sim-to-real algorithm, but to provide a technical recipe on the full stack required to make RGBbased humanoid loco-manipulation work ... (p. 2, 1. Introduction).
- **Evaluation boundary:** Figure 8. Real-world generalization of VIRAL RGB-based policy under variations in tray and object position, robot start pose, table height and type, tablecloth color, lighting, and object category. Videos are ... (p. 6, Figure/Table caption).
- **Explicit failure boundary:** We find that compute scale is critical: scaling simulation to tens of GPUs (up to 64) makes both teacher and student training reliable, while low-compute regimes often fail. (p. 1, Abstract).
