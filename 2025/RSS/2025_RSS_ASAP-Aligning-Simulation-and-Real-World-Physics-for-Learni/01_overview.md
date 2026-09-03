# ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p066.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p066.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: Robotics, humanoid, whole-body control, sim-to-real, residual dynamics
- Official paper: https://www.roboticsproceedings.org/rss21/p066.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p066.pdf
- Code/Project: https://agile.human2humanoid.com/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 However, a successful backflip requires ‘mastering the landing first-if the policy cannot land correctly,를 문제로 두고, mnparal- or result in overly conservative policies that sacrifice a yaper, we present ASAP를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Humanoid robots hold the potential fr leled versatility for performing. hn
- **p. 1 / Abstract - extractive body cue:** mnparal- or result in overly conservative policies that sacrifice a yaper, we present ASAP
- **p. 1 / Abstract - extractive body cue:** red to tackle the dynamics ‘whole-body skis.
- **p. 1 / Abstract - extractive body cue:** between first stage, we prestrain motion trac such as using relargeted human motion data.
- **p. 1 / Abstract - extractive body cue:** In the second stage, we (DR) methods, often rely on labor-intensive parameter tuning deploy the in the real world and collect real-world data
- **p. 4 / B. Phase-based Motion Tracking Policy Training - extractive body cue:** However, a successful backflip requires ‘mastering the landing first-if the policy cannot land correctly,
- **p. 4 / B. Phase-based Motion Tracking Policy Training - extractive body cue:** Crucially, because the actor does not depend on position-based motion targets, ‘our approach eliminates the need for odometry during real world deployment-overcoming a well-documented challenge ...

## Core Idea

- **p. 1 / Abstract - extractive body cue:** mnparal- or result in overly conservative policies that sacrifice a yaper, we present ASAP
- **p. 2 / Abstract - extractive body cue:** To this end, we propose ASAP, a two-stage framework that aligns the dynamics mismatch between simulation and realworld physics, enabling agile humanoid whole-body skills ASAP ...
- **p. 3 / Abstract - extractive body cue:** 1) We introduce ASAP, a framework that bridges the simto-real gap by leveraging a delta action model trained via reinforcement learning (RL) with real-world data
- **p. 4 / B. Phase-based Motion Tracking Policy Training - extractive body cue:** To mitigate this issue, we introduce a termination curriculum that progressively refines the motion error tolerance throughout training, guiding the policy toward improved tracking performance, ...
- **p. 5 / C. Fine-tuning Motion Tracking Policy under New Dynamics - extractive body cue:** In this section, we present extensive experimental results oon three policy transfers: IsaaeGym [58] to IsaacSim [63], IsaaeGym to Genesis [6], and IsiaeGym to real-world ...
- **p. 4 / B. Phase-based Motion Tracking Policy Training - extractive body cue:** ‘The policy trained in the first stage can track the reference motion in the real-world but does not achieve high motion quality. ‘Thus, during the ...
- **p. 5 / B. Training Delta Action Model - extractive body cue:** As illustrated in Figure 2 (b), the delta action model is defined as Ady = (se, 44)» where the policy 77> leams to output corrective ...
- **p. 5 / B. Training Delta Action Model - extractive body cue:** The RL environment incorporates this delta action model by modifying the simulator dynamies as follows: sey1 F(se,a; + Nay) where f° represents the simulator's dynamics, ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | As illustrated in Figure 2 (b), the delta action model is defined as Ady = (se, 44)» where the policy 77> leams to output corrective actions based on the current state sy ... | proprioception, reference pose/motion, visual or language command | p. 5 (B. Training Delta Action Model), p. 2 (Abstract) |
| State/latent | illustrated, Figure, delta, action, model, defined, Ady, where, policy, leams, output, corrective | whole-body pose, balance/contact state와 skill/mode | p. 5 (B. Training Delta Action Model), p. 2 (Abstract), p. 2 (Abstract) |
| Output/action | Wwe tin the dea action model by minimizing the discrepancy between simulation sales; and real-world sates () Policy Fine-taning: We freeze the ‘eli action model incorporate ito the siilator o align the ... | joint/whole-body action, motion target 또는 task trajectory | p. 2 (Abstract), p. 2 (Abstract), p. 3 (Abstract) |
| Objective/outcome | We consider two RL-free methods: fixed-point iteration and gradient-based optimization, Fixed:-point iteration refines #(s) iteratively, while gradient-based optimization minimizes a loss function to achieve a better estimate. ‘These me ... | tracking, balance, skill/task success와 recovery | p. 10 (B. Different Usage of Delta Action Model), p. 4 (B. Phase-based Motion Tracking Policy Training), p. 5 (B. Training Delta Action Model) |

## Main Claims and Actual Contribution

- **p. 1 / Abstract - extractive body cue:** mnparal- or result in overly conservative policies that sacrifice a yaper, we present ASAP
- **p. 2 / Abstract - extractive body cue:** To this end, we propose ASAP, a two-stage framework that aligns the dynamics mismatch between simulation and realworld physics, enabling agile humanoid whole-body skills ASAP ...
- **p. 3 / Abstract - extractive body cue:** 1) We introduce ASAP, a framework that bridges the simto-real gap by leveraging a delta action model trained via reinforcement learning (RL) with real-world data
- **p. 4 / B. Phase-based Motion Tracking Policy Training - extractive body cue:** To mitigate this issue, we introduce a termination curriculum that progressively refines the motion error tolerance throughout training, guiding the policy toward improved tracking performance, ...
- **p. 5 / C. Fine-tuning Motion Tracking Policy under New Dynamics - extractive body cue:** In this section, we present extensive experimental results oon three policy transfers: IsaaeGym [58] to IsaacSim [63], IsaaeGym to Genesis [6], and IsiaeGym to real-world ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 10. Analysis of dataset size, waning horizon, and scion aorm on the performance of x. (a) Dataset Size: Mean Per Joint Position Eror (MPIPE) ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 10 (Figure/Table caption) |
| Embodiment/environment | This process ensures accurate motion retargeting and produces the cleuned robot trajectory dataset DG as shown in Figure 3 (). | hardware/simulator version and reset protocol | p. 3 (3) Extensive experiments in both simulation and real-world), p. 3 (3) Extensive experiments in both simulation and real-world) |
| Dataset/benchmark | This process ensures accurate motion retargeting and produces the cleuned robot trajectory dataset DG as shown in Figure 3 (). | role, split, size and leakage | p. 3 (3) Extensive experiments in both simulation and real-world), p. 3 (3) Extensive experiments in both simulation and real-world) |
| Metric | settings demonstrate that ASAP effectively reduces dyrnamies mismatch, enabling highly agile motions on robots and significantly reducing motion tracking errors. | definition, denominator, direction and uncertainty | p. 3 (3) Extensive experiments in both simulation and real-world), p. 3 (3) Extensive experiments in both simulation and real-world), p. 1 (Figure/Table caption) |
| Baseline/ablation | Fig. 10. Analysis of dataset size, waning horizon, and scion aorm on the performance of x. (a) Dataset Size: Mean Per Joint Position Eror (MPIPE) is evaluted for both in-distbution (grea) and ... | fair input/data/compute/action matching | p. 10 (Figure/Table caption), p. 10 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 11 / C. Does ASAP Fine-Tuning Outperform Random Action Noise - extractive body cue:** Such structured discrepancies cannot be effectively captured by merely adding uniform action noise.
- **p. 12 / B. Offine and Online System Identification for Roboties - extractive body cue:** + Hardware Constraints: Agile whole-body motions exert significant stress on robots, leading to motor overheating, and hardware failure during data collection.
- **p. 12 / B. Offine and Online System Identification for Roboties - extractive body cue:** While ASAP demonstrates promising results in bridging the sim-to-real gap for agile humanoid control, our framework has several real-world limitations that highlights critical challenges in ...
- **p. 11 / C. Does ASAP Fine-Tuning Outperform Random Action Noise - extractive body cue:** However, the performance of the action noise approach (MPJPE of 150) does not match the precision achieved by ASAP (MPIPE of 126).
- **p. 10 / A. Key Factors in Training Delta Action Models - extractive body cue:** However, this trend ‘does not consistently extend to closed-loop performance.
- **p. 3 / 3) Extensive experiments in both simulation and real-world - extractive body cue:** b) Simulation-based Data Cleaning: Since the reconstruction process can introduce noise and errors [25], some estimated motions may not be physically feasible, making them unsuitable ...
- **p. 10 / A. Key Factors in Training Delta Action Models - extractive body cue:** As shown in Figure 10 (a), increasing the dataset size improves 74's generalization, evidenced by reduced errors in ‘out-of-distribution evaluations.

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 However, a successful backflip requires ‘mastering the landing first-if the policy cannot land correctly,를 문제로 두고, mnparal- or result in overly conservative policies that sacrifice a yaper, we present ASAP를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 4 (B. Phase-based Motion Tracking Policy Training), p. 4 (B. Phase-based Motion Tracking Policy Training), p. 2 (Abstract), p. 2 (Abstract), p. 3 (Abstract), p. 4 (B. Phase-based Motion Tracking Policy Training) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, a successful backflip requires ‘mastering the landing first-if the policy cannot land correctly, (p. 4, B. Phase-based Motion Tracking Policy Training).
- **Actual contribution:** Primarily leveraging reinforcement learning algorithms [80] within physics simulators [58, 63, 88], humanoid robots have earned a wide range of skills, including robust locomo (p. 11, A. Learning-based Methods for Humanoid Control).
- **Evaluation boundary:** This process ensures accurate motion retargeting and produces the cleuned robot trajectory dataset DG as shown in Figure 3 (). (p. 3, 3) Extensive experiments in both simulation and real-world).
- **Explicit failure boundary:** For instance, when imitating a jumping motion, the policy often fails early in training and learns 10 remain on the ground to avoid landing penalties. (p. 4, B. Phase-based Motion Tracking Policy Training).
