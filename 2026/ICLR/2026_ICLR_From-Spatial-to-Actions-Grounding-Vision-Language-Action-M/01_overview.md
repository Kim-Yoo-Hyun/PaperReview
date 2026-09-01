# From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=fzmittHfq3.
> PDF retrieval source: https://openreview.net/pdf/d6aae457099a5d9e50bba1a6bbc48d8756a15c91.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2026 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, Vision-Language Model, Robotics, 3D Vision
- Official paper: https://openreview.net/forum?id=fzmittHfq3
- Full-text retrieval: https://openreview.net/pdf/d6aae457099a5d9e50bba1a6bbc48d8756a15c91.pdf
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-02 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 This discrepancy results in a critical gap: current VLAs lack reliable 3D spatial understanding, leading to persistent challenges in generalization and adaptability.를 문제로 두고, We propose FALCON (From Spatial to Action), a novel paradigm that integrates richer and more representative 3D spatial tokens into VLAs through an improved injection scheme.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Existing vision-language-action (VLA) models act in 3D real-world but are typically built on 2D encoders, leaving a spatial reasoning gap that limits generalization and adaptability.
- **p. 1 / Abstract - extractive body cue:** Recent 3D integration techniques for VLAs either require specialized sensors and transfer poorly across modalities, or inject weak cues that lack geometry and degrade vision-language ...
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce FALCON (From Spatial to Action), a novel paradigm that injects rich 3D spatial tokens into the action head.
- **p. 1 / Abstract - extractive body cue:** FALCON leverages spatial foundation models to deliver strong geometric priors from RGB alone, and includes an Embodied Spatial Model that can optionally fuse depth, or ...
- **p. 1 / Abstract - extractive body cue:** To preserve language reasoning, spatial tokens are consumed by a Spatial-Enhanced Action Head rather than being concatenated into the vision-language backbone.
- **p. 2 / 1 Introduction - extractive body cue:** This discrepancy results in a critical gap: current VLAs lack reliable 3D spatial understanding, leading to persistent challenges in generalization and adaptability.
- **p. 2 / 1 Introduction - extractive body cue:** These limitations now form a major bottleneck in developing reliable generalist robot policies.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** We propose FALCON (From Spatial to Action), a novel paradigm that integrates richer and more representative 3D spatial tokens into VLAs through an improved injection ...
- **p. 2 / 1 Introduction - extractive body cue:** Overall Benchmark Bridge Calvin (Zero-shot) Google Robot Calvin Real-World Real-World (Few-Shot) Figure 1 We propose FALCON, a vision-language-action model that achieves robust 3D spatial understanding ...
- **p. 3 / 1 Introduction - extractive body cue:** For limitation (2) of poor modality transferability, we introduce an Embodied Spatial Model that can optionally integrate extra 3D modalities (e.g., depth, poses).
- **p. 4 / 3 Methodology - extractive body cue:** We introduce a lightweight fusion mechanism that aligns and combines these complementary representations (see Sec.
- **p. 4 / 3 Methodology - extractive body cue:** To this end, we propose FALCON, a generalist robot policy that overcomes limitations of prior VLAs by integrating rich geometric priors from spatial foundation models ...
- **p. 6 / 3 Methodology - extractive body cue:** These are then concatenated with a learnable camera token tcam ∈RDs and fed into a Spatial Encoder Espl(·), which consists of N cross-attention and self-attention ...
- **p. 4 / 3 Methodology - extractive body cue:** 2, FALCON is an end-to-end VLA consists of three core components: (1) a 2D VLM for multimodal semantic representation, (2) an ESM for extracting 3D ...
- **p. 6 / 3 Methodology - extractive body cue:** To address this limitation, we propose an Embodied Spatial Model that injects 3D conditions (i.e., depth, pose) to build more accurate spatial representations, enabling our ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 3.1 Problem Definition We study the problem of task-oriented robot control, where a robot must interpret visual observations Ot = {I1 t , . . . , In t } at time ... | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (3 Methodology), p. 5 (3 Methodology) |
| State/latent | Problem, Definition, study, task-oriented, robot, control, where, must, interpret, visual, observations, time | geometry, map, object/relationship state | p. 4 (3 Methodology), p. 5 (3 Methodology), p. 4 (3 Methodology) |
| Output/action | At timestep t, the VLM processes visual observations Ot and language instructions L to produce a semantic action token ˆtact. | point map, pose, scene graph, affordance 또는 query result | p. 5 (3 Methodology), p. 4 (3 Methodology), p. 5 (3 Methodology) |
| Objective/outcome | 3.3 Training Objective During the training process of FALCON, the objective for action sequence generation is formulated as the minimization of a composite loss function over the predicted action horizon. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3 Methodology), p. 5 (3 Methodology), p. 6 (3 Methodology) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** We propose FALCON (From Spatial to Action), a novel paradigm that integrates richer and more representative 3D spatial tokens into VLAs through an improved injection ...
- **p. 2 / 1 Introduction - extractive body cue:** Overall Benchmark Bridge Calvin (Zero-shot) Google Robot Calvin Real-World Real-World (Few-Shot) Figure 1 We propose FALCON, a vision-language-action model that achieves robust 3D spatial understanding ...
- **p. 3 / 1 Introduction - extractive body cue:** For limitation (2) of poor modality transferability, we introduce an Embodied Spatial Model that can optionally integrate extra 3D modalities (e.g., depth, poses).
- **p. 4 / 3 Methodology - extractive body cue:** We introduce a lightweight fusion mechanism that aligns and combines these complementary representations (see Sec.
- **p. 4 / 3 Methodology - extractive body cue:** To this end, we propose FALCON, a generalist robot policy that overcomes limitations of prior VLAs by integrating rich geometric priors from spatial foundation models ...
- **p. 8 / 4 Experiments - extractive body cue:** 3, FALCON achieves the highest average success rate of 70.0% across all nine task suites, outperforming the advanced method SpatialVLA [31] (44.4%) by 25.6%.
- **p. 7 / 4 Experiments - extractive body cue:** Our method achieves SOTA performance in both the ABC→D and ABCD→D settings, significantly outperforming all 7
- **p. 9 / 4 Experiments - extractive body cue:** 4, FALCON achieves the highest performance across all settings, significantly outperforming the second-best model by 27.5% in Simple and 27% in Unseen Average.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (4 Experiments), p. 7 (4 Experiments) |
| Embodiment/environment | All models are initially pre-trained on a mixture of the Open X-Embodiment dataset [29] and then fine-tuned with multi-task real-robot data. | hardware/simulator version and reset protocol | p. 8 (4 Experiments), p. 10 (4 Experiments) |
| Dataset/benchmark | Base Tasks contains a total of nine distinct task suites, encompassing language grounding (cluttered scenes with random distractors) and semantic understanding (unseen object poses). | role, split, size and leakage | p. 8 (4 Experiments), p. 10 (4 Experiments), p. 9 (4 Experiments), p. 8 (4 Experiments) |
| Metric | In contrast, our method exhibits strong robustness to scale variations, avoiding these issues and achieving the highest success rates in both scenarios. | definition, denominator, direction and uncertainty | p. 9 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Baseline/ablation | 2 reports the results on the Bridge-WidowX setup, where FALCON consistently outperforms all baselines and achieves best performance. | fair input/data/compute/action matching | p. 8 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 4 Experiments - extractive body cue:** For larger blocks, collisions frequently occur during the placement of the blue block, while smaller blocks are prematurely released before placement, leading to task failure.
- **p. 11 / 5 Conclusion - extractive body cue:** In this work, we introduce FALCON, a vision-language-action model that augments generalist robot policies with robust 3D spatial understanding.
- **p. 11 / 5 Conclusion - extractive body cue:** Experiments across both simulation and real-world tasks show that FALCON consistently surpasses existing VLA methods, achieving state-of-the-art performance and robustness on spatially demanding tasks.
- **p. 7 / 4 Experiments - extractive body cue:** For real-world tasks, we design settings that span from simple interactions (e.g., lifting a yellow pepper) to long-horizon, spatially demanding activities (e.g., placing a red ...
- **p. 9 / 4 Experiments - extractive body cue:** In contrast, our method exhibits strong robustness to scale variations, avoiding these issues and achieving the highest success rates in both scenarios.
- **p. 10 / 4 Experiments - extractive body cue:** 4, this approach results in significant performance degradation compared to the standard FALCON paradigm.

## Why Read It

VLA and generalist robot policies의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 This discrepancy results in a critical gap: current VLAs lack reliable 3D spatial understanding, leading to persistent challenges in generalization and adaptability.를 문제로 두고, We propose FALCON (From Spatial to Action), a novel paradigm that integrates richer and more representative 3D spatial tokens into VLAs through an improved injection scheme.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 6 (3 Methodology), p. 4 (3 Methodology) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
