# FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_FLARE_A_Failure-Aware_Framework_for_Autonomous_Correction_and_Recovery_in_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_FLARE_A_Failure-Aware_Framework_for_Autonomous_Correction_and_Recovery_in_CVPR_2026_paper.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: Robotics, VLA, failure recovery, retry, reset, contact-rich manipulation, safety
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_FLARE_A_Failure-Aware_Framework_for_Autonomous_Correction_and_Recovery_in_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_FLARE_A_Failure-Aware_Framework_for_Autonomous_Correction_and_Recovery_in_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: system
- Source audit: full-text PDF body checked on 2026-09-02 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 We formalize this challenge by introducing a taxonomy of failure states.를 문제로 두고, To this end, we propose FLARE, a Failure-Aware Retry/Reset framework designed to transform brittle VLAs into resilient embodied agents (Fig.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-Language-Action Models (VLAs) have demonstrated significant promise in generalizing to complex, longhorizon robotic manipulation tasks.
- **p. 1 / Abstract - extractive body cue:** However, their performance remains brittle, as they are typically trained on trajectory-monotonic, failure-free demonstrations.
- **p. 1 / Abstract - extractive body cue:** This reliance on "perfect" data leaves them unable to recover from common execution errors, such as a missed grasp, a dropped object, or an unexpected ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose FLARE, a novel framework that endows VLAs with robust error recovery capabilities through a "Retry" and "Reset" paradigm.
- **p. 1 / Abstract - extractive body cue:** First, we introduce a "Retry" mechanism by injecting perturbation and bridging segments that decouple robot pose from environment state into demonstrations, enabling the policy to ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** We formalize this challenge by introducing a taxonomy of failure states.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** This leads to a critical failure: when a minor perturbation creates a state with a valid se t but a novel sr t, the policy ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose FLARE, a Failure-Aware Retry/Reset framework designed to transform brittle VLAs into resilient embodied agents (Fig.
- **p. 2 / 1. Introduction - extractive body cue:** We introduce a perturbation-bridging augmentation strategy that injects random pose perturbations between task segments, followed by a bridging segments that reconnects them.
- **p. 3 / 3. Methodology - extractive body cue:** Our method provides a distinct solution for each case, training a unified VLA system to handle both (Fig.
- **p. 3 / 3. Methodology - extractive body cue:** We introduce the Retry/Reset framework, a unified approach built upon a taxonomy of failures as either In-Distribution (ID) or Out-of-Distribution (OOD) errors.
- **p. 5 / 3.4. Unified Training and Closed-Loop Inference - extractive body cue:** This design allows each policy to achieve high performance on its specific task while enabling straightforward systemlevel scaling.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** Following modern VLA architectures [4, 15, 18], the policy is Markovian-lacking history-and predicts an action chunk at based on the current visual observation ot ∈O ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** This policy, which outputs a distribution over action sequences at ∈AK (where K is the chunk length and A is the action space), is written ...
- **p. 5 / 3.4. Unified Training and Closed-Loop Inference - extractive body cue:** Instead of training a single, monolithic model prone to task interference, we adopt a modular and scalable expert policy library approach.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Following modern VLA architectures [4, 15, 18], the policy is Markovian-lacking history-and predicts an action chunk at based on the current visual observation ot ∈O and language instruction I. | observation, uncertainty/risk estimate와 task command | p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation) |
| State/latent | Following, modern, VLA, architectures, policy, Markovian-lacking, history-and, predicts, action, chunk, current, visual | safe set, recovery state 또는 constraint margin | p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation), p. 5 (3.4. Unified Training and Closed-Loop Inference) |
| Output/action | This policy, which outputs a distribution over action sequences at ∈AK (where K is the chunk length and A is the action space), is written as: at ∼πθ(·/ot, I). | shielded, recovery 또는 safe action | p. 3 (3.1. Problem Formulation), p. 5 (3.4. Unified Training and Closed-Loop Inference), p. 1 (1. Introduction) |
| Objective/outcome | For example, the "reset cup" adapter is trained exclusively on its corresponding reset demonstrations, using the prompt Ireset = "reset the cup." This modular approach prevents the conflicting gradients that can arise ... | task return과 violation/failure probability | p. 5 (3.4. Unified Training and Closed-Loop Inference), p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose FLARE, a Failure-Aware Retry/Reset framework designed to transform brittle VLAs into resilient embodied agents (Fig.
- **p. 2 / 1. Introduction - extractive body cue:** We introduce a perturbation-bridging augmentation strategy that injects random pose perturbations between task segments, followed by a bridging segments that reconnects them.
- **p. 3 / 3. Methodology - extractive body cue:** Our method provides a distinct solution for each case, training a unified VLA system to handle both (Fig.
- **p. 3 / 3. Methodology - extractive body cue:** We introduce the Retry/Reset framework, a unified approach built upon a taxonomy of failures as either In-Distribution (ID) or Out-of-Distribution (OOD) errors.
- **p. 5 / 3.4. Unified Training and Closed-Loop Inference - extractive body cue:** This design allows each policy to achieve high performance on its specific task while enabling straightforward systemlevel scaling.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Our method achieves state-of-the-art performance on 8 out of 9 tasks. On the remaining task, Threading D0, although we do not obtain the ...
- **p. 6 / 4. Experiment - extractive body cue:** In this case, our method still achieves comparable performance, even when multiple baselines (PhoenixHuman, π0.5) reach a 100% success rate.
- **p. 7 / 5.1. Analysis of Perturbation & Bridging - extractive body cue:** The best performance is achieved when r = 30◦and t = 0.7 in 0 10 20 30 40 50 60 70 80 Rotation Angle (degrees) ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (Figure/Table caption), p. 6 (4. Experiment) |
| Embodiment/environment | Real-world Validation To verify FLARE's effectiveness and address concerns about privileged simulation states, we conducted real-world experiments on a Piper arm with RealSense D435i (top/wrist views) across two challenging tasks: Stack ... | hardware/simulator version and reset protocol | p. 7 (4. Experiment), p. 6 (4. Experiment) |
| Dataset/benchmark | Success rates of real-world manipulation tasks. | role, split, size and leakage | p. 7 (4. Experiment), p. 6 (4. Experiment), p. 7 (4. Experiment), p. 6 (4. Experiment) |
| Metric | Table 1. Our method achieves state-of-the-art performance on 8 out of 9 tasks. On the remaining task, Threading D0, although we do not obtain the best result, our approach still (1) substantially ... | definition, denominator, direction and uncertainty | p. 6 (Figure/Table caption), p. 8 (5.2. Ablations and Analysis for Reset skills learning), p. 8 (Figure/Table caption) |
| Baseline/ablation | More notably, our method even outperforms Phoenix-Human, demonstrating the comprehensive advantage of our framework over prior selfreflection approaches-even when compared to a baseline supplied with correct human guidance. | fair input/data/compute/action matching | p. 6 (4. Experiment), p. 7 (4. Experiment), p. 6 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. The overall framework of our method. We first collect the failure data with the VLA model trained with regular demonstrations. Then we perform ...
- **p. 8 / 6. Conclusion - extractive body cue:** We presented FLARE, a failure-aware framework that endows VLA agents with robust autonomy through a dual Retry/Reset paradigm.
- **p. 8 / 6. Conclusion - extractive body cue:** While current hardware limits the correction of highly complex object poses, our findings confirm that treating failure recovery as a distinct, learned capability is essential ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. FLARE: Failure-Aware Resilience in VLA. Previous methods are brittle, failing from minor perturbations (ID errors) or catastrophic states (OOD errors), and do not ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Comparison of experimental results across 9 manipulation tasks in RoboMimic Simulation. The ‘D' suffix in the task names denotes the range of object ...
- **p. 6 / 4. Experiment - extractive body cue:** For "reset" skills, we used Gemini-2.5-Pro to analyze failure videos.
- **p. 7 / 5.1. Analysis of Perturbation & Bridging - extractive body cue:** The failure case for Coffee and ThreePieceAssembly respectively.

## Why Read It

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 We formalize this challenge by introducing a taxonomy of failure states.를 문제로 두고, To this end, we propose FLARE, a Failure-Aware Retry/Reset framework designed to transform brittle VLAs into resilient embodied agents (Fig.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
