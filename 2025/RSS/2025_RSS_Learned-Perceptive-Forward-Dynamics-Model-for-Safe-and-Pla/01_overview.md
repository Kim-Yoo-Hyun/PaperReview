# Learned Perceptive Forward Dynamics Model for Safe and Platform-aware Robotic Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p001.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p001.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: Robotics, world model, model predictive control, safe navigation, sim-to-real, legged
- Official paper: https://www.roboticsproceedings.org/rss21/p001.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p001.pdf
- Code/Project: https://github.com/leggedrobotics/fdm
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 locomotion 문제를 이해하기 위해 읽는다. 본문은 However, open challenges remain to incorporate 3) perception to target rough environments and the transfer from simulation to the real system.를 문제로 두고, To overcome these issues, we propose a novel learned perceptive를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Learned Perceptive Forward Dynamics Model for Safe
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** 1: Demonstration of the proposed perceptive Forward Dynamics Model for robust navigation in complex environments.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** The model, trained with real-world and simulation data, predicts the robots future states given a sequence of velocity actions.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** It takes as input the surrounding geometry in the form of a height scan, along with past states and proprioceptive measurements.
- **p. 2 / 1. Inrropucrion - extractive body cue:** However, open challenges remain to incorporate 3) perception to target rough environments and the transfer from simulation to the real system.
- **p. 2 / 1. Inrropucrion - extractive body cue:** However, training neural networks to represent robot dynamics often requires substantial amounts of state-action trajectories, motivating the use of synthetic data to mitigate the challenges ...

## Core Idea

- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** To overcome these issues, we propose a novel learned perceptive
- **p. 3 / B. Planning - extractive body cue:** Our method addresses domain discrepancies by incorporating real-world data into the ‘dynamics model while maintaining platform awareness through earning from past experiences.
- **p. 5 / B. Model Architecture - extractive body cue:** The Forward Dynamics Model loss £ consists of supervised terms for network outputs.
- **p. 2 / 1. Inrropucrion - extractive body cue:** The main contributions of this work are as follows:
- **p. 2 / 1. Inrropucrion - extractive body cue:** by reducing the need for extensive parameter tuning and providing a flexible solution for non-task-specific planning. ‘This enables zero-shot adaptation to new environments without requiring ...
- **p. 2 / A. Dynamics Modeling - extractive body cue:** Lately, world models have emerged, which encode system dynamics in a latent space, enabling policy optimization through imagined rollouts [19 20) Such models can also ...
- **p. 6 / B. Model Architecture - extractive body cue:** The FDM runs onboard using an NVIDIA Jetson Orin AGX, with the planner running at 7 Hz. using 2048 trajectories and a model inference time ...
- **p. 3 / A. Dynamics Modeling - extractive body cue:** To address this, we aim to learn an approximate dynamics model f that predicts a subset of state 5 based on the action a, and ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We define ihe state ¥ to be the tuple (p,r), where p © SE2 is the robot's pose and r < {0,1} is the failure risk of the trajectory where 0 indicates ... | proprioception, terrain/perception observation과 velocity command | p. 3 (A. Dynamics Modeling), p. 2 (A. Dynamics Modeling) |
| State/latent | define, state, tuple, where, SE2, robot, pose, failure, risk, trajectory, indicates, risk-free | body/contact state, foothold 또는 behavior mode | p. 3 (A. Dynamics Modeling), p. 2 (A. Dynamics Modeling), p. 3 (A. Dynamics Modeling) |
| Output/action | Lately, world models have emerged, which encode system dynamics in a latent space, enabling policy optimization through imagined rollouts [19 20) Such models can also be used to directly estimate the next ... | joint target, torque, footstep 또는 locomotion action | p. 2 (A. Dynamics Modeling), p. 3 (A. Dynamics Modeling), p. 5 (B. Model Architecture) |
| Objective/outcome | Consequently, the objective of the dynamics ‘model becomes minimizing a combined loss comprising pose prediction Cyoge and failure risk prediction Lyi | velocity/progress, stability, energy와 terrain generalization | p. 4 (A. Dynamics Modeling), p. 3 (B. Model Predictive Path Integral Control), p. 6 (B. Model Architecture) |

## Main Claims and Actual Contribution

- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** To overcome these issues, we propose a novel learned perceptive
- **p. 3 / B. Planning - extractive body cue:** Our method addresses domain discrepancies by incorporating real-world data into the ‘dynamics model while maintaining platform awareness through earning from past experiences.
- **p. 5 / B. Model Architecture - extractive body cue:** The Forward Dynamics Model loss £ consists of supervised terms for network outputs.
- **p. 2 / 1. Inrropucrion - extractive body cue:** The main contributions of this work are as follows:
- **p. 2 / 1. Inrropucrion - extractive body cue:** by reducing the need for extensive parameter tuning and providing a flexible solution for non-task-specific planning. ‘This enables zero-shot adaptation to new environments without requiring ...
- **p. 9 / C. Platform-aware Predictions - extractive body cue:** Il, our approach achieves the highest success rate across both environments.
- **p. 10 / C. Platform-aware Predictions - extractive body cue:** Moreover, our FDM integrated into an MPPI planner with simplified rewards achieves on average 81% goal success rate in complex environments.
- **p. 6 / B. Model Architecture - extractive body cue:** The simulation results are achieved by building upon the NVIDIA IsaacLab framework [44] with terain details and data augmentations provided in Appendix E.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (C. Platform-aware Predictions), p. 10 (C. Platform-aware Predictions) |
| Embodiment/environment | Second, the failure states observed in simulation environments do not perfectly translate to real-world failures, and real-world data lacks demonstrations. of collisions due to the risk of hardware damage, leaving fa persistent ... | hardware/simulator version and reset protocol | p. 10 (C. Platform-aware Predictions), p. 10 (C. Platform-aware Predictions) |
| Dataset/benchmark | In the planar environment, robot failures are rare (0.042%), likely caused by simulation instabilities that the model cannot predict, leading to low recall and precision scores. | role, split, size and leakage | p. 10 (C. Platform-aware Predictions), p. 10 (C. Platform-aware Predictions), p. 8 (B. Baseline Comparison), p. 6 (B. Model Architecture) |
| Metric | Moreover, our FDM integrated into an MPPI planner with simplified rewards achieves on average 81% goal success rate in complex environments. | definition, denominator, direction and uncertainty | p. 10 (C. Platform-aware Predictions), p. 7 (A. FDM Percepriveness), p. 8 (B. Baseline Comparison) |
| Baseline/ablation | Further, the better accuracy compared to the baselines becomes clearly | fair input/data/compute/action matching | p. 7 (B. Baseline Comparison), p. 7 (B. Baseline Comparison), p. 8 (B. Baseline Comparison) |

## Explicit Limitations and Failure Boundary

- **p. 7 / A. FDM Percepriveness - extractive body cue:** Specifically, the FDM can estimate failure states (eg., collisions) and adjust future poses based on the velocity ‘command tracking performance in rough terrain, To evaluate ...
- **p. 8 / B. Baseline Comparison - extractive body cue:** Moreover, demonstrates the most precise failure estimation, although it is less likely to detect all collisions compared to the more conservative baseline.
- **p. 8 / B. Baseline Comparison - extractive body cue:** In the planar environment, robot failures are rare (0.042%), likely caused by simulation instabilities that the model cannot predict, leading to low recall and precision ...
- **p. 10 / C. Platform-aware Predictions - extractive body cue:** The proposed FDM accurately predicts failures due to collisions and ealy path terminations caused by unlzaversable stars and ramps.
- **p. 10 / C. Platform-aware Predictions - extractive body cue:** As a resull, the simple combination of pose reward guiding the robot toward the goal and a failure reward preventing collisions proves sufficient for safe ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Demonstration of the proposed perceptive Forward Dynamics Model for robust navigation in complex environments. The model, trained with real-world and simulation data, predicts ...
- **p. 6 / B. Model Architecture - extractive body cue:** This redundancy increases robustness to isolated collision prediction errors.

## Why Read It

World models, safety, uncertainty, and recovery의 locomotion 문제를 이해하기 위해 읽는다. 본문은 However, open challenges remain to incorporate 3) perception to target rough environments and the transfer from simulation to the real system.를 문제로 두고, To overcome these issues, we propose a novel learned perceptive를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Inrropucrion), p. 2 (1. Inrropucrion), p. 1 (Body text (section boundary not confidently recovered)), p. 3 (B. Planning), p. 3 (A. Dynamics Modeling), p. 5 (B. Model Architecture) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, open challenges remain to incorporate 3) perception to target rough environments and the transfer from simulation to the real system. (p. 2, 1. Inrropucrion).
- **Actual contribution:** To overcome these issues, we propose a novel learned perceptive (p. 1, Body text (section boundary not confidently recovered)).
- **Evaluation boundary:** Trained with a mix of simulated and real-world data, the 'DM captures the complex dynamics of a quadrupedal robot and enables zero-shot adjustments of the planning objective. ‘The presented network ... (p. 10, C. Platform-aware Predictions).
- **Explicit failure boundary:** Second, the failure states observed in simulation environments do not perfectly translate to real-world failures, and real-world data lacks demonstrations. of collisions due to the risk of hardware damage, leaving ... (p. 10, C. Platform-aware Predictions).
