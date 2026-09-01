# PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_PALM_Progress-Aware_Policy_Learning_via_Affordance_Reasoning_for_Long-Horizon_Robotic_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_PALM_Progress-Aware_Policy_Learning_via_Affordance_Reasoning_for_Long-Horizon_Robotic_CVPR_2026_paper.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, VLA, affordance, progress estimation, long-horizon manipulation
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_PALM_Progress-Aware_Policy_Learning_via_Affordance_Reasoning_for_Long-Horizon_Robotic_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_PALM_Progress-Aware_Policy_Learning_via_Affordance_Reasoning_for_Long-Horizon_Robotic_CVPR_2026_paper.pdf
- Code/Project: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_PALM_Progress-Aware_Policy_Learning_via_Affordance_Reasoning_for_Long-Horizon_Robotic_CVPR_2026_paper.html
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 In addition, existing VLAs lack mechanisms for continuously estimating progress within a subtask.를 문제로 두고, Our contributions are as follows: • We introduce PALM, a unified VLA framework that integrates structured affordance reasoning and progress-aware policy generation to enable reliable execution across longhorizon, contact-rich manipulati ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recent advancements in vision-language-action (VLA) models have shown promise in robotic manipulation, yet they continue to struggle with long-horizon, multi-step tasks.
- **p. 1 / Abstract - extractive body cue:** Existing methods lack internal reasoning mechanisms that can identify task-relevant interaction cues or track progress within a subtask, leading to critical execution errors such as ...
- **p. 1 / Abstract - extractive body cue:** To address these challenges, we introduce PALM, a VLA framework that structures policy learning around interaction-centric affordance reasoning and subtask progress cues.
- **p. 1 / Abstract - extractive body cue:** PALM distills complementary affordance representations that capture object relevance, contact geometry, spatial placements, and motion dynamics, and serve as task-relevant anchors for visuomotor control.
- **p. 1 / Abstract - extractive body cue:** To further stabilize long-horizon execution, PALM predicts continuous within-subtask progress, enabling seamless subtask transitions.
- **p. 2 / 1. Introduction - extractive body cue:** In addition, existing VLAs lack mechanisms for continuously estimating progress within a subtask.
- **p. 2 / 1. Introduction - extractive body cue:** Although existing models may infer the final goal and produce intermediate actions [18, 38, 112, 143, 146, 148], they lack internal representations that disambiguate which ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are as follows: • We introduce PALM, a unified VLA framework that integrates structured affordance reasoning and progress-aware policy generation to enable reliable ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these gaps, we introduce PALM, a novel end-to-end framework for learning scalable, long-horizon manipulation.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** At time t, given observations ot "O, and task specification ⌧"T , and conditioned on the predicted affordance latent, the policy jointly decodes an action ...
- **p. 5 / 3.4. Progress-aware Policy via Inverse Dynamics - extractive body cue:** In addition to predicting where to act via affordances, we introduce a progress-aware prediction task that estimates how far execution has advanced within the current ...
- **p. 3 / 3.2. PALM Architecture - extractive body cue:** Building on prior inverse-dynamics formulations [18, 38, 112], these queries aggregate current observations with the predicted affordance latent to infer action sequences that align with ...
- **p. 5 / 3.4. Progress-aware Policy via Inverse Dynamics - extractive body cue:** This explicit progress signal reduces ambiguity in long-horizon control: visually similar observations may correspond to different actions depending on stage, and pt disambiguates these cases ...
- **p. 4 / 3.2. PALM Architecture - extractive body cue:** Affordance Queries Action-progress Queries Multi-Modal Encoders Affordance prediction Frozen Trainable Unidirectional Attention Action-progress <Global> <Local> <Spatial> <Dynamic> T S V G
- **p. 5 / 3.4. Progress-aware Policy via Inverse Dynamics - extractive body cue:** We instantiate finv as a denoising diffusion transformer that conditions on the current observation ot, the instruction l, the robot state st, and the predicted ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | PALM processes three synchronized inputs: a language instruction l, an image observation ot, and a robot state st. | image/video, language instruction, proprioception과 history | p. 3 (3.2. PALM Architecture), p. 5 (3.4. Progress-aware Policy via Inverse Dynamics) |
| State/latent | PALM, processes, three, synchronized, inputs, language, instruction, image, observation, robot, state, explicit | language-grounded task state와 action-policy context | p. 3 (3.2. PALM Architecture), p. 5 (3.4. Progress-aware Policy via Inverse Dynamics), p. 2 (1. Introduction) |
| Output/action | This explicit progress signal reduces ambiguity in long-horizon control: visually similar observations may correspond to different actions depending on stage, and pt disambiguates these cases by providing a continuous indicator of "wher ... | continuous action, pose 또는 action chunk | p. 5 (3.4. Progress-aware Policy via Inverse Dynamics), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Objective/outcome | Training follows the standard diffusion objective: ˜yt⇥t+n-1,td = ‘ ¯↵td yt⇥t+n-1 + ‘ 1 -¯↵td ✏ (9) LDiT = Etd, ✏æ✏-✏✓(˜yt⇥t+n-1,td ∑l, ot, st, ˆFt+n, td⌥æ 2 2 (10) where yt⇥t+n-1 is ... | instruction following, task success, generalization과 latency | p. 5 (3.4. Progress-aware Policy via Inverse Dynamics), p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are as follows: • We introduce PALM, a unified VLA framework that integrates structured affordance reasoning and progress-aware policy generation to enable reliable ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these gaps, we introduce PALM, a novel end-to-end framework for learning scalable, long-horizon manipulation.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** At time t, given observations ot "O, and task specification ⌧"T , and conditioned on the predicted affordance latent, the policy jointly decodes an action ...
- **p. 5 / 3.4. Progress-aware Policy via Inverse Dynamics - extractive body cue:** In addition to predicting where to act via affordances, we introduce a progress-aware prediction task that estimates how far execution has advanced within the current ...
- **p. 6 / 4.1. Simulation Experiments - extractive body cue:** Moreover, as shown in Table 2, across all four LIBERO suites, PALM achieves state-of-the-art performance with an average success rate of 94.5%.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. LIBERO experimental results. For each task suite (Spatial, Object, Goal, Long), we report the average success rate and standard error across 3 seeds ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. CALVIN ABC→D experimental results. We group the baselines into four types and report the average success rate of the top three checkpoints, computed ...
- **p. 8 / 4.3. Real-World Experiments - extractive body cue:** We report the success rate (SR) and average length for each task over 20 real-world rollouts.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (4.1. Simulation Experiments), p. 7 (Figure/Table caption) |
| Embodiment/environment | For pre-training, we utilize a mixed dataset from the DROID [54] and BridgeData V2 [113] datasets, which together provide large-scale, in-the-wild robotic arm demonstrations to build a foundational understanding of diverse real-world ... | hardware/simulator version and reset protocol | p. 5 (4. Experiments), p. 8 (4.3. Real-World Experiments) |
| Dataset/benchmark | Additionally, we compare against Octo [111], which pre-trains robot policies on diverse datasets to enhance generalization. | role, split, size and leakage | p. 5 (4. Experiments), p. 8 (4.3. Real-World Experiments), p. 6 (4.1. Simulation Experiments), p. 7 (4.2. Ablation Studies) |
| Metric | For each task suite (Spatial, Object, Goal, Long), we report the average success rate and standard error across 3 seeds with 500 episodes each. | definition, denominator, direction and uncertainty | p. 7 (4.2. Ablation Studies), p. 6 (4.1. Simulation Experiments), p. 6 (4.1. Simulation Experiments) |
| Baseline/ablation | PALM consistently and substantially outperforms all baselines. | fair input/data/compute/action matching | p. 6 (4.1. Simulation Experiments), p. 6 (4.1. Simulation Experiments), p. 8 (4.3. Real-World Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** PALM achieves stateof-the-art results on two benchmarks, with a 12.5% improvement on CALVIN ABC→D and 91.8% success on LIBEROLONG, and shows significant robustness in real-world ...
- **p. 8 / 4.3. Real-World Experiments - extractive body cue:** As shown in Table 5, results demonstrate PALM's superior generalization over baselines as the task sequence length increases, showing its robustness in longhorizon settings.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 In addition, existing VLAs lack mechanisms for continuously estimating progress within a subtask.를 문제로 두고, Our contributions are as follows: • We introduce PALM, a unified VLA framework that integrates structured affordance reasoning and progress-aware policy generation to enable reliable execution across longhorizon, contact-rich manipulati ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation), p. 3 (3.2. PALM Architecture), p. 5 (3.4. Progress-aware Policy via Inverse Dynamics), p. 4 (3.2. PALM Architecture) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
