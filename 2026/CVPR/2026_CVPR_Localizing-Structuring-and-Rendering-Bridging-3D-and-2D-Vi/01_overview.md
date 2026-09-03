# Localizing, Structuring, and Rendering: Bridging 3D and 2D Vision-Language-Action Models for Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_Localizing_Structuring_and_Rendering_Bridging_3D_and_2D_Vision-Language-Action_Models_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_Localizing_Structuring_and_Rendering_Bridging_3D_and_2D_Vision-Language-Action_Models_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, 3D-2D alignment, Robotics
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_Localizing_Structuring_and_Rendering_Bridging_3D_and_2D_Vision-Language-Action_Models_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_Localizing_Structuring_and_Rendering_Bridging_3D_and_2D_Vision-Language-Action_Models_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 The key difficulty lies in coupling geometric reasoning with semantic perception-robots must not only reason about 3D spatial structures but also interpret visual cues in an interpretable, image-centric manner.를 문제로 두고, Our main contributions are as follows: • We propose DiffRender-VLA, a unified framework that bridges 3D spatial reasoning and 2D visual perception to transfer geometric understanding into imageinterpretable action policies. • We ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Robotic manipulation in complex 3D environments requires unifying spatial reasoning with intuitive visual perception, which is a capability that current Vision-Language-Action paradigms address separately.
- **p. 1 / Abstract - extractive body cue:** While 3D VLAs excel in geometric and physical reasoning, they lack intuitive, imagelevel understanding and dense visual semantics; conversely, 2D VLAs (even with depth image) ...
- **p. 1 / Abstract - extractive body cue:** We introduce DiffRender-VLA, a differentiable rendering-based framework that bridges 3D and 2D VisionLanguage-Action models through gradient-consistent visual mediation.
- **p. 1 / Abstract - extractive body cue:** It generates differentiable images by lo- *Corresponding author is Xiu Su and Xiaoheng Deng calizing the next end-effector target with a world-aligned cube marker, differentiably ...
- **p. 1 / Abstract - extractive body cue:** These differentiable images serve as visual bridges, embedding spatial semantics while allowing gradients from 2D VLAs to backpropagate into 3D representations, thereby coupling geometric reasoning ...
- **p. 2 / 1. Introduction - extractive body cue:** The key difficulty lies in coupling geometric reasoning with semantic perception-robots must not only reason about 3D spatial structures but also interpret visual cues in ...
- **p. 2 / 1. Introduction - extractive body cue:** Robotic manipulation in complex 3D environments remains a central challenge in artificial intelligence and robotics.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are as follows: • We propose DiffRender-VLA, a unified framework that bridges 3D spatial reasoning and 2D visual perception to transfer geometric ...
- **p. 3 / 3. Method - extractive body cue:** We present DiffRender-VLA, which, instead of choosing between image-based and 3D reasoning, enables gradient flow to transfer the 3D perception capabilities into 2D VLA models.
- **p. 4 / 3.2. Structuring Differential Spatial Information - extractive body cue:** As shown in Figure 3, our method creates differentiable point clouds with key properties: hue indicates spatial direction aligned with world axes; intensity encodes relative ...
- **p. 4 / 3.3. Rendering Adaptive Viewpoint - extractive body cue:** This enables joint reasoning about the target location and observation perspective as a coupling that is difficult to achieve through separate optimization.
- **p. 5 / 3.4. Fine-Grained Action Prediction - extractive body cue:** The bidirectional fusion enables both components to co-adapt during training.
- **p. 6 / 3.4. Fine-Grained Action Prediction - extractive body cue:** For gripper state, we use a binary classification head: Qgrip = hgrip(MaxPool(Zfused)), g = arg max Qgrip (7) The complete action is a = (p, ...
- **p. 5 / 3.4. Fine-Grained Action Prediction - extractive body cue:** We fuse VLA features with coarse spatial context through bidirectional cross-attention: Zfused = CrossAttn(Zcoarse, ZVLA)+CrossAttn(ZVLA, Zcoarse) (4) The first term guides VLA features toward spatially ...
- **p. 3 / 3.1. Localizing Coarse Target Region - extractive body cue:** Given a natural language instruction I which is transformed to elang by VLM, like [43], and multi-view RGB-D observations O = {oi}Mobs i=1 , our ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Given a natural language instruction I which is transformed to elang by VLM, like [43], and multi-view RGB-D observations O = {oi}Mobs i=1 , our final goal is to predict a 6-DoF ... | image/video, language instruction, proprioception과 history | p. 3 (3.1. Localizing Coarse Target Region), p. 2 (1. Introduction) |
| State/latent | Given, natural, language, instruction, transformed, elang, VLM, like, multi-view, RGB-D, observations, Mobs | language-grounded task state와 action-policy context | p. 3 (3.1. Localizing Coarse Target Region), p. 2 (1. Introduction), p. 6 (3.4. Fine-Grained Action Prediction) |
| Output/action | Our main contributions are as follows: • We propose DiffRender-VLA, a unified framework that bridges 3D spatial reasoning and 2D visual perception to transfer geometric understanding into imageinterpretable action policies. • We ... | continuous action, pose 또는 action chunk | p. 2 (1. Introduction), p. 6 (3.4. Fine-Grained Action Prediction), p. 2 (1. Introduction) |
| Objective/outcome | By learning viewpoints end-to-end through task loss, the model discovers task-relevant perspectives: clearly revealing color gradients from multiple faces (maximizing directional information), minimizing occlusions of the target end-eff ... | instruction following, task success, generalization과 latency | p. 4 (3.3. Rendering Adaptive Viewpoint), p. 4 (3.2. Structuring Differential Spatial Information), p. 3 (3. Method) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are as follows: • We propose DiffRender-VLA, a unified framework that bridges 3D spatial reasoning and 2D visual perception to transfer geometric ...
- **p. 3 / 3. Method - extractive body cue:** We present DiffRender-VLA, which, instead of choosing between image-based and 3D reasoning, enables gradient flow to transfer the 3D perception capabilities into 2D VLA models.
- **p. 4 / 3.2. Structuring Differential Spatial Information - extractive body cue:** As shown in Figure 3, our method creates differentiable point clouds with key properties: hue indicates spatial direction aligned with world axes; intensity encodes relative ...
- **p. 4 / 3.3. Rendering Adaptive Viewpoint - extractive body cue:** This enables joint reasoning about the target location and observation perspective as a coupling that is difficult to achieve through separate optimization.
- **p. 5 / 3.4. Fine-Grained Action Prediction - extractive body cue:** The bidirectional fusion enables both components to co-adapt during training.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 8. Beam parameters improvement for small objects. deployment confirm that color-encoded spatial beams and world-aligned cube markers generalize beyond synthetic environments. DiffRender-VLA substantially outperforms ...
- **p. 7 / 4.1. Simulation Results - extractive body cue:** DiffRender-VLA significantly outperforms 2D visual prompting approaches: TraceVLA (63.9%, +16.6%) and VLA-adapter (60.6%, +19.9%).
- **p. 7 / 4.1. Simulation Results - extractive body cue:** Task-specific improvements highlight spatial understanding capabilities: Occlusion Tasks: Average 91.7% success (+7.6% over GWM).

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 7 (4.1. Simulation Results) |
| Embodiment/environment | Real-World Deployment Situation. lation heatmaps Qcoarse, world-aligned cube markers with adaptive sizing (ℓcube = 10-15cm, scaled to 0.8× object size for small targets); (3) We render spatially-enriched images via differentiable beam e ... | hardware/simulator version and reset protocol | p. 7 (4. Experiments), p. 7 (4. Experiments) |
| Dataset/benchmark | Condition DiffRender-VLA RVT-2 [14] OpenVLA-OFT [23] Gap In-Domain 80.5 68.4 53.4 12.1/27.1 Novel Objects 74.2 (-6.3) 60.1 (-8.3) 43.7 (-9.7) 14.1/30.5 Novel Scenes 71.8 (-8.7) 58.6 (-9.8) 41.2 (-12.2) 13.2/30.6 Novel Lighting ... | role, split, size and leakage | p. 7 (4. Experiments), p. 7 (4. Experiments), p. 8 (4.3. Ablation Studies), p. 6 (4. Experiments) |
| Metric | Real-world: success rate, translation/rotation error, 20 trials/task. | definition, denominator, direction and uncertainty | p. 7 (4. Experiments), p. 6 (Figure/Table caption), p. 7 (4.1. Simulation Results) |
| Baseline/ablation | Best Baseline +10.0 +10.0 +25.0 +20.0 +20.0 +20.0 +17.5 (b) Visibility improvements (a) Camera Pose Density Figure 7. | fair input/data/compute/action matching | p. 7 (4.1. Simulation Results), p. 7 (4.2. Real-World Deployment Results), p. 8 (4.2. Real-World Deployment Results) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 4.3. Ablation Studies - extractive body cue:** (3) Two-stage training: 76.2% (-4.3%)-without end-to-end gradient flow, stages cannot co-adapt.
- **p. 8 / 4.3. Ablation Studies - extractive body cue:** (1) Non-differentiable beams: 74.8% (-5.7%)-beams provide visual cues but cannot optimize placement.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. Simulation Tasks for Occlusion and Clutter enviroments.
- **p. 7 / 4.1. Simulation Results - extractive body cue:** Task-specific improvements highlight spatial understanding capabilities: Occlusion Tasks: Average 91.7% success (+7.6% over GWM).

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 The key difficulty lies in coupling geometric reasoning with semantic perception-robots must not only reason about 3D spatial structures but also interpret visual cues in an interpretable, image-centric manner.를 문제로 두고, Our main contributions are as follows: • We propose DiffRender-VLA, a unified framework that bridges 3D spatial reasoning and 2D visual perception to transfer geometric understanding into imageinterpretable action policies. • We ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 6 (3.4. Fine-Grained Action Prediction), p. 5 (3.4. Fine-Grained Action Prediction), p. 3 (3.1. Localizing Coarse Target Region), p. 3 (3.1. Localizing Coarse Target Region) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
