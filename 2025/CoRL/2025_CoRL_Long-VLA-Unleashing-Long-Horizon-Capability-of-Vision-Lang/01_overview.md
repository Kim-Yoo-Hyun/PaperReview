# Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v305/fan25a.html.
> PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v305/main/assets/fan25a/fan25a.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, Planning, Robotics
- Official paper: https://proceedings.mlr.press/v305/fan25a.html
- Full-text retrieval: https://raw.githubusercontent.com/mlresearch/v305/main/assets/fan25a/fan25a.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, most existing VLA frameworks are tailored for short-horizon tasks, leaving the challenge of long-horizon task execution largely unresolved.를 문제로 두고, To this end, we propose Long-VLA, the first end-to-end VLA model specifically designed for longhorizon robotic manipulation.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-Language-Action (VLA) models have become a cornerstone in robotic policy learning, leveraging large-scale multimodal data for robust and scalable control.
- **p. 1 / Abstract - extractive body cue:** However, existing VLA frameworks primarily address short-horizon tasks, and their effectiveness on long-horizon, multi-step robotic manipulation remains limited due to challenges in skill chaining and ...
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce Long-VLA, the first end-to-end VLA model specifically designed for long-horizon robotic tasks.
- **p. 1 / Abstract - extractive body cue:** Our approach features a novel phase-aware input masking strategy that adaptively segments each subtask into moving and interaction phases, enabling the model to focus on ...
- **p. 1 / Abstract - extractive body cue:** This unified strategy preserves the scalability and data efficiency of VLA training, and our architecture-agnostic module can be seamlessly integrated into existing VLA models.
- **p. 2 / 1 Introduction - extractive body cue:** However, most existing VLA frameworks are tailored for short-horizon tasks, leaving the challenge of long-horizon task execution largely unresolved.
- **p. 2 / 1 Introduction - extractive body cue:** Therefore, solving the skill chaining problem in long-horizon tasks while preserving the scalability and data efficiency of VLA models remains a fundamental and open challenge.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** To this end, we propose Long-VLA, the first end-to-end VLA model specifically designed for longhorizon robotic manipulation.
- **p. 2 / 1 Introduction - extractive body cue:** Finally, we present L-CALVIN and show that Long-VLA outperforms state-of-the-art methods on simulated and real-world robotic tasks, with robust performance on diverse long-horizon tasks.
- **p. 3 / 3 Method - extractive body cue:** To address this limitation, we propose Long-VLA, a unified end-to-end VLA model that leverages phase-specific data more effectively.
- **p. 3 / 3 Method - extractive body cue:** 3.1 Revisiting Decomposition Strategy Before introducing our method, we first investigate whether decomposition is essential for VLA models.
- **p. 4 / 3 Method - extractive body cue:** Based on these observations, we propose an input-level adaptation strategy that dynamically adjusts visual inputs according to the current task phase.
- **p. 4 / 3 Method - extractive body cue:** Static Cam 𝒔𝒔𝒃𝒃 𝒕𝒕 Gripper Cam 𝒔𝒔𝒈𝒈𝒕𝒕 … … Multimodal Transformer Encoder … Noise 𝝈𝝈 𝛥𝛥𝑇𝑇 𝛥𝛥𝑅𝑅 𝑠𝑠𝑔𝑔 𝑠𝑠𝑝𝑝 Detection 𝒅𝒅𝒕𝒕 … Action 𝒂𝒂𝒕𝒕 masking ...
- **p. 5 / 3 Method - extractive body cue:** 3.2.2 Model Achitecture Long-VLA policy πθ(at / st, dt, g) predicts the action at conditioned on the current observation st, the detection input dt associated ...
- **p. 3 / 3 Method - extractive body cue:** To enable training and inference within a unified end-to-end VLA framework, we extend the original action representation by adding a one-dimensional phase identifier sp, which ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Static Cam 𝒔𝒔𝒃𝒃 𝒕𝒕 Gripper Cam 𝒔𝒔𝒈𝒈𝒕𝒕 … … Multimodal Transformer Encoder … Noise 𝝈𝝈 𝛥𝛥𝑇𝑇 𝛥𝛥𝑅𝑅 𝑠𝑠𝑔𝑔 𝑠𝑠𝑝𝑝 Detection 𝒅𝒅𝒕𝒕 … Action 𝒂𝒂𝒕𝒕 masking move to the top side of the ... | image/video, language instruction, proprioception과 history | p. 4 (3 Method), p. 5 (3 Method) |
| State/latent | Static, Cam, Gripper, Multimodal, Transformer, Encoder, Noise, Detection, Action, masking, move, side | language-grounded task state와 action-policy context | p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method) |
| Output/action | 3.2.2 Model Achitecture Long-VLA policy πθ(at / st, dt, g) predicts the action at conditioned on the current observation st, the detection input dt associated with st, and the latent goal g, ... | continuous action, pose 또는 action chunk | p. 5 (3 Method), p. 5 (3 Method), p. 4 (3 Method) |
| Objective/outcome | Using the decomposition dataset, the model is trained with a single score matching loss that jointly supervises both the moving and interaction phases: LDiff = Ea∼pdataEn∼N(0,σ2I)∥Dθ(˜at, epost, σt) -at∥2 2, (2) where ... | instruction following, task success, generalization과 latency | p. 4 (3 Method), p. 4 (3 Method), p. 3 (3 Method) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** To this end, we propose Long-VLA, the first end-to-end VLA model specifically designed for longhorizon robotic manipulation.
- **p. 2 / 1 Introduction - extractive body cue:** Finally, we present L-CALVIN and show that Long-VLA outperforms state-of-the-art methods on simulated and real-world robotic tasks, with robust performance on diverse long-horizon tasks.
- **p. 3 / 3 Method - extractive body cue:** To address this limitation, we propose Long-VLA, a unified end-to-end VLA model that leverages phase-specific data more effectively.
- **p. 3 / 3 Method - extractive body cue:** 3.1 Revisiting Decomposition Strategy Before introducing our method, we first investigate whether decomposition is essential for VLA models.
- **p. 4 / 3 Method - extractive body cue:** Based on these observations, we propose an input-level adaptation strategy that dynamically adjusts visual inputs according to the current task phase.
- **p. 6 / 4 Experiment - extractive body cue:** As shown in Figure 4, our model achieves performance improvements in the D→D and ABCD→D of the L-CALVIN benchmark.
- **p. 6 / 4 Experiment - extractive body cue:** As shown in Figure 5, while the success rate of the base policy drops to zero after the seventh task, our approach is still able ...
- **p. 7 / 4 Experiment - extractive body cue:** As shown in Figure 6, our model achieves significant improvements over the base policy across all time horizons.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (4 Experiment), p. 6 (4 Experiment) |
| Embodiment/environment | In real-world robotic experiments, our method consistently outperforms the state-of-the-art algorithm π0 across the generalization task. | hardware/simulator version and reset protocol | p. 7 (4 Experiment), p. 6 (4 Experiment) |
| Dataset/benchmark | In simulation and real-world environments, we select MDT [52] as our base policy. | role, split, size and leakage | p. 7 (4 Experiment), p. 6 (4 Experiment), p. 5 (4 Experiment), p. 5 (4 Experiment) |
| Metric | As shown in Figure 5, while the success rate of the base policy drops to zero after the seventh task, our approach is still able to achieve a success rate of nearly ... | definition, denominator, direction and uncertainty | p. 6 (4 Experiment), p. 13 (Figure/Table caption), p. 7 (4 Experiment) |
| Baseline/ablation | In real-world robotic experiments, our method consistently outperforms the state-of-the-art algorithm π0 across the generalization task. | fair input/data/compute/action matching | p. 7 (4 Experiment), p. 5 (4 Experiment), p. 6 (4 Experiment) |

## Explicit Limitations and Failure Boundary

- **p. 19 / Figure/Table caption - extractive body cue:** Figure 12: Failure case of π0. Base Policy LongVLA Press blue button Grab the corn Put in the sink Press yellow button Fail to press ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: In contrast to previous methods that (a) adopt a unified model but are limited to short- horizon tasks and fail to address skill ...
- **p. 8 / 5 Conclusion - extractive body cue:** By segmenting each subtask into movement and interaction phases with targeted masking, Long-VLA mitigates distribution shifts and enhances subtask compatibility, enabling robust performance across complex ...
- **p. 7 / 4 Experiment - extractive body cue:** This demonstrates the robustness of our method in handling long-horizon tasks.
- **p. 7 / 4 Experiment - extractive body cue:** (Left: cleaning; Right: sorting) These performance gains stem from two key factors: the robust capability of our base policy and the substantial enhancement provided by ...
- **p. 8 / 4 Experiment - extractive body cue:** Performance significantly improves with input-level adaptation, mainly from adding detection data during movement for better control and removing unwanted third-person visual interference during interaction for ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, most existing VLA frameworks are tailored for short-horizon tasks, leaving the challenge of long-horizon task execution largely unresolved.를 문제로 두고, To this end, we propose Long-VLA, the first end-to-end VLA model specifically designed for longhorizon robotic manipulation.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (3 Method), p. 5 (3 Method), p. 3 (3 Method), p. 5 (3 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (20 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, most existing VLA frameworks are tailored for short-horizon tasks, leaving the challenge of long-horizon task execution largely unresolved. (p. 2, 1 Introduction).
- **Actual contribution:** To this end, we propose Long-VLA, the first end-to-end VLA model specifically designed for longhorizon robotic manipulation. (p. 2, 1 Introduction).
- **Evaluation boundary:** Figure 7: Comparison with SOTA method on real-world scenarios. (Left: cleaning; Right: sorting) These performance gains stem from two key factors: the robust capability of our base policy and the ... (p. 7, Figure/Table caption).
- **Explicit failure boundary:** While our model mitigates the initial state gap, it does not address execution failures under precise initial conditions. (p. 9, Limitation).
