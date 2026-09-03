# Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=5i888dLp8N.
> PDF retrieval source: https://openreview.net/pdf/95685162fa940bca32702d659b96eebf84138a75.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, Vision-Language Model, Robotics, 3D Vision
- Official paper: https://openreview.net/forum?id=5i888dLp8N
- Full-text retrieval: https://openreview.net/pdf/95685162fa940bca32702d659b96eebf84138a75.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Without a mechanism to maintain a persistent spatial representation of the scene, the perception-action loop becomes strictly viewdependent: when a target object is not observed, the model lacks the necessary context to ...를 문제로 두고, Based on these insights, we introduce SOMA, a VLA framework for out-of-vision manipulation that equips the robot with persistent spatial memory for reasoning and action.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We introduce SOMA, the Spatial memory framework for Out-of-Vision Manipulation in VisionLanguage-Action (VLA) models.
- **p. 1 / Abstract - extractive body cue:** Most existing VLAs implicitly assume that task-relevant objects are always visible, leading to brittle and reactive behaviors when targets fall outside the camera's field of ...
- **p. 1 / Abstract - extractive body cue:** SOMA addresses this limitation by equipping VLAs with a persistent, spatial memory constructed from multi-view observations acquired via a movable head camera, enabling reasoning beyond ...
- **p. 1 / Abstract - extractive body cue:** The framework consists of three components: Spatial Memory Construction for aggregating angular-wise observations into a unified spatial-semantic representation by scanning, Dynamic Memory Refinement for maintaining ...
- **p. 1 / Abstract - extractive body cue:** We evaluate SOMA on five self-designed challenging real-world OOV manipulation tasks, including multi-step and dualarm scenarios, where target objects are initially invisible.
- **p. 2 / 1. Introduction - extractive body cue:** Without a mechanism to maintain a persistent spatial representation of the scene, the perception-action loop becomes strictly viewdependent: when a target object is not observed, ...
- **p. 2 / 1. Introduction - extractive body cue:** Addressing this gap requires mechanisms that both acquire spatial evidence beyond the current view and retain it in a persistent scene representation.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Based on these insights, we introduce SOMA, a VLA framework for out-of-vision manipulation that equips the robot with persistent spatial memory for reasoning and action.
- **p. 2 / 1. Introduction - extractive body cue:** In particular, integrating angular-wise observations into a coherent spatial-semantic memory enables globally consistent reasoning and effective manipulation even when task-relevant objects are temporarily out of ...
- **p. 3 / 3. Method - extractive body cue:** By maintaining a globally consistent spatial memory, SOMA enables robust reasoning and manipulation even when task-relevant objects lie outside the current field of view.
- **p. 1 / 1. Introduction - extractive body cue:** However, most existing VLAs are developed under fixedview tabletop manipulation setups, typically relying on a single static camera or a third-person viewpoint.
- **p. 1 / 1. Introduction - extractive body cue:** The development of VLAs have become a central direction in robotic action modeling research (Zhao et al., 2025; Chen et al., 2025c; Kim et al., ...
- **p. 3 / 3.1. Spatial Memory Construction - extractive body cue:** Each sampled frame fi ∈˜V is processed by a unified perception pipeline consisting of: (1) a geometry prior network (VGGT (Wang et al., 2025b)) for ...
- **p. 3 / 3. Method - extractive body cue:** During manipulation, the model receives the current observation ot c, the user instruction, robot states, and a noised action sequence, where c ∈{l, r, h} ...
- **p. 4 / 3.1. Spatial Memory Construction - extractive body cue:** Dynamic Memory Refinement ··· ··· ··· Instruction: "Pick the pink cup and place it in the basket." Text Tokenizer VLM Robot State: {%% ", %& ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | These systems typically extend large-scale pre-trained Multimodal Large Language Models (MLLMs) (Bjorck et al., 2025; Yang et al., 2025a) with an action head or specialized action module that maps multimodal inputs-such as ... | image/video, language instruction, proprioception과 history | p. 1 (1. Introduction), p. 3 (3. Method) |
| State/latent | systems, typically, extend, large-scale, pre-trained, Multimodal, Large, Language, Models, MLLMs, Bjorck, Yang | language-grounded task state와 action-policy context | p. 1 (1. Introduction), p. 3 (3. Method), p. 4 (3.1. Spatial Memory Construction) |
| Output/action | During manipulation, the model receives the current observation ot c, the user instruction, robot states, and a noised action sequence, where c ∈{l, r, h} denotes the left arm, right arm, and ... | continuous action, pose 또는 action chunk | p. 3 (3. Method), p. 4 (3.1. Spatial Memory Construction), p. 6 (3.3. Contextual Memory Retrieval) |
| Objective/outcome | New observations from the head view ot h are incorporated to update M0 into ˆ Mt through Dynamic Memory Refinement, which performs similarity-aware fusion to preserve global consistency while accommodating newly observed ... | instruction following, task success, generalization과 latency | p. 3 (3. Method), p. 4 (3.1. Spatial Memory Construction), p. 4 (3.1. Spatial Memory Construction) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Based on these insights, we introduce SOMA, a VLA framework for out-of-vision manipulation that equips the robot with persistent spatial memory for reasoning and action.
- **p. 2 / 1. Introduction - extractive body cue:** In particular, integrating angular-wise observations into a coherent spatial-semantic memory enables globally consistent reasoning and effective manipulation even when task-relevant objects are temporarily out of ...
- **p. 3 / 3. Method - extractive body cue:** By maintaining a globally consistent spatial memory, SOMA enables robust reasoning and manipulation even when task-relevant objects lie outside the current field of view.
- **p. 1 / 1. Introduction - extractive body cue:** However, most existing VLAs are developed under fixedview tabletop manipulation setups, typically relying on a single static camera or a third-person viewpoint.
- **p. 1 / 1. Introduction - extractive body cue:** The development of VLAs have become a central direction in robotic action modeling research (Zhao et al., 2025; Chen et al., 2025c; Kim et al., ...
- **p. 7 / 4.3. Real World Results - extractive body cue:** In Figure 4, SOMA achieves the highest success rates across all five real-world out-of-vision (OOV) manipulation tasks.
- **p. 7 / 4.3. Real World Results - extractive body cue:** It demonstrates that SOMA's advantages go beyond improved success rates and manifest as qualitatively different execution behavior.
- **p. 8 / 4.4. Simulation Results - extractive body cue:** Overall, SOMA achieves the highest average performance of 52.0% with 300 demos and maintains competitive results across all data regimes, surpassing strong baselines such as ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (4.3. Real World Results), p. 7 (4.3. Real World Results) |
| Embodiment/environment | SimplerEnv offers a standardized real-to-sim benchmark for evaluating policy success rates across simulated environments reflecting real-world robotic systems (Zitkovich et al., 2023). | hardware/simulator version and reset protocol | p. 6 (4.1. Benchmarks), p. 6 (4.1. Benchmarks) |
| Dataset/benchmark | Performance comparison via SR (%) across task categories on the Robocasa Tabletop GR1 benchmarks with varying numbers of demonstrations per task. | role, split, size and leakage | p. 6 (4.1. Benchmarks), p. 6 (4.1. Benchmarks), p. 8 (4.3. Real World Results), p. 7 (4.2. Implementation) |
| Metric | Table 10. Detailed Ablation studies on Robocasa Tabletop GR-1 benchmark. We compare different Update Strategies, Retrieval Modules, and Memory Representations. Reported values are success rates (%). "SimEMA" denotes the normal EMA updat ... | definition, denominator, direction and uncertainty | p. 18 (Figure/Table caption), p. 7 (4.3. Real World Results), p. 6 (4.1. Benchmarks) |
| Baseline/ablation | Table 5. Ablation study on different components of the proposed memory design. "Geo." and "Obj." denote Geometric cues and object semantics, respectively. SimplerEnv Results. Table 4 reports the performance com- parison across ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 8 (4.4. Simulation Results), p. 7 (4.3. Real World Results) |

## Explicit Limitations and Failure Boundary

- **p. 20 / Figure/Table caption - extractive body cue:** Table 15. Failure mode analysis on the fully observable RoboCasa Tabletop GR1 simulation (50 sampled failures, 10 per category). Under full observability, failures reflect limitations ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Illustration of the Out-of-Vision (OOV) limitation in existing VLA models. Most VLAs rely on purely reactive percep- tion-actions are driven only by what ...
- **p. 8 / 5. Conclusion - extractive body cue:** We propose SOMA, a spatial memory framework for VisionLanguage-Action models that addresses the fundamental limitation of view-bound perception in out-of-vision manip8
- **p. 20 / Figure/Table caption - extractive body cue:** Table 14. Failure mode analysis on real-world OOV tasks (25 sampled failed episodes, 5 per task). Failures predominantly arise when translating reliable spatial localization into ...
- **p. 7 / 4.2. Implementation - extractive body cue:** If the target cannot be localized, SOMA initiates an active head-scanning procedure along a predefined trajectory to construct the spatial memory.
- **p. 7 / 4.3. Real World Results - extractive body cue:** Scan-only SOMA further improves success rates by leveraging multi-view scanning to construct a more complete initial memory, but still falls short of the full model.
- **p. 6 / 3.3. Contextual Memory Retrieval - extractive body cue:** The original vision-language tokens, robot state, and noised action embeddings are directly fed into the DiT, where Xboost serves as global context that modulates token ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Without a mechanism to maintain a persistent spatial representation of the scene, the perception-action loop becomes strictly viewdependent: when a target object is not observed, the model lacks the necessary context to ...를 문제로 두고, Based on these insights, we introduce SOMA, a VLA framework for out-of-vision manipulation that equips the robot with persistent spatial memory for reasoning and action.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.1. Spatial Memory Construction), p. 3 (3. Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (24 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, most existing VLAs are developed under fixedview tabletop manipulation setups, typically relying on a single static camera or a third-person viewpoint. (p. 1, 1. Introduction).
- **Actual contribution:** Based on these insights, we introduce SOMA, a VLA framework for out-of-vision manipulation that equips the robot with persistent spatial memory for reasoning and action. (p. 2, 1. Introduction).
- **Evaluation boundary:** Table 5. Ablation study on different components of the proposed memory design. "Geo." and "Obj." denote Geometric cues and object semantics, respectively. SimplerEnv Results. Table 4 reports the performance com- ... (p. 8, Figure/Table caption).
- **Explicit failure boundary:** The fixed-head variant fails once either the target or the goal leaves the field of view, confirming the brittleness of view-bound policies under partial observability. (p. 7, 4.3. Real World Results).
