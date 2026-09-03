# Method - BeliefMapNav: 3D Voxel-Based Belief Map for Zero-Shot Object Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=7AMriz7I3K; PDF retrieval source: https://arxiv.org/pdf/2506.06487.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 9 (3 Method), p. 7 (3 Method)): At each timestep, the system takes as input the current RGB-D observation It, the agent's pose st, and the text-specified target c, and outputs a navigation action at ∈A from ...

## Method Body Digest

- **p. 3 / 3 Method - extractive body cue:** At each timestep, the system takes as input the current RGB-D observation It, the agent's pose st, and the text-specified target c, and outputs a ...
- **p. 4 / 3 Method - extractive body cue:** The observation-based belief planning module selects the next goal based on this belief and outputs navigation actions.
- **p. 5 / 3 Method - extractive body cue:** We use CLIP [33] to extract visual features vk h,w for each patch and each patch P k h,w is processed by the Segment Anything ...
- **p. 5 / 3 Method - extractive body cue:** The module operates in three stages: 1) Multi-scale feature extraction: Extract image CLIP features from multi-scale RGB images and spatial information from the depth images.
- **p. 9 / 3 Method - extractive body cue:** However, CLIP demonstrates stronger generalization to out-of-distribution data and supports efficient inference via independent encoders and pre-computed features.
- **p. 7 / 3 Method - extractive body cue:** Before each action, the agent selects the first frontier in the optimized sequence π∗as the next navigation target and replans at every step with the ...
- **p. 4 / 3 Method - extractive body cue:** The frontier observation belief estimation module computes frontier observation belief from the belief, frontiers, and visibility maps via FOV-based aggregation.
- **p. 7 / 3 Method - extractive body cue:** The proposed objective improves search efficiency by minimizing exploration cost with A*-optimized paths and prioritizing high-belief frontiers via observation-weighted costs.

## Design Rationale

- **p. 3 / 1 Introduction - extractive body cue:** The contributions of our method are mainly summarized as follows: 1)We propose BeliefMapNav, an efficient zero-shot object navigation system that accurately predicts target location through ...
- **p. 2 / 1 Introduction - extractive body cue:** To enable more precise and accurate predictions of the target object's location within 3D space, we propose a novel 3D voxel-based belief map that considers ...
- **p. 1 / 1 Introduction - extractive body cue:** Zero-shot object navigation(ZSON) enables robots to locate targets in novel environments through natural language instructions (e.g., "find the red sofa"), eliminating reliance on pre-mapped scenes ...

## Source Evidence Cues

- **p. 3 / 3 Method - extractive body cue:** At each timestep, the system takes as input the current RGB-D observation It, the agent's pose st, and the text-specified target c, and outputs a ...
- **p. 4 / 3 Method - extractive body cue:** The observation-based belief planning module selects the next goal based on this belief and outputs navigation actions.
- **p. 5 / 3 Method - extractive body cue:** We use CLIP [33] to extract visual features vk h,w for each patch and each patch P k h,w is processed by the Segment Anything ...
- **p. 5 / 3 Method - extractive body cue:** The module operates in three stages: 1) Multi-scale feature extraction: Extract image CLIP features from multi-scale RGB images and spatial information from the depth images.
- **p. 9 / 3 Method - extractive body cue:** However, CLIP demonstrates stronger generalization to out-of-distribution data and supports efficient inference via independent encoders and pre-computed features.
- **p. 7 / 3 Method - extractive body cue:** Before each action, the agent selects the first frontier in the optimized sequence π∗as the next navigation target and replans at every step with the ...
- **p. 4 / 3 Method - extractive body cue:** The frontier observation belief estimation module computes frontier observation belief from the belief, frontiers, and visibility maps via FOV-based aggregation.
- **Detected method headings:** 3 Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | At each timestep, the system takes as input the current RGB-D observation It, the agent's pose st, and the text-specified target c, ... | p. 3 (3 Method), p. 4 (3 Method) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | The observation-based belief planning module selects the next goal based on this belief and outputs navigation actions. | p. 4 (3 Method), p. 5 (3 Method) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | We use CLIP [33] to extract visual features vk h,w for each patch and each patch P k h,w is processed by ... | p. 5 (3 Method), p. 5 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 7 / 3 Method - extractive body cue:** The proposed objective improves search efficiency by minimizing exploration cost with A*-optimized paths and prioritizing high-belief frontiers via observation-weighted costs.
- **p. 7 / 3 Method - extractive body cue:** The optimal exploration strategy seeks a permutation of frontier visiting sequence π = [fπ1, fπ2, . . . , fπn] that minimizes the expected search ...
- **p. 4 / 3 Method - extractive body cue:** 3.5, which selects the next navigation point by optimizing expected distance cost to detect the object.
- **p. 8 / 3 Method - extractive body cue:** While InstructNav prioritizes SR with a dense search strategy, our approach maintains high success rates and boosts search efficiency by generating more accurate target position ...
- **p. 4 / 3 Method - extractive body cue:** 3.3.1 3D Hierarchical semantic mapping The 3D hierarchical semantic voxel map Mc represents the environment across three levels, Ls = {scene, region, object}, with progressively ...
- **p. 5 / 3 Method - extractive body cue:** Multi-scale CLIP image features are extracted, and the top features selected by hierarchical feature scorers update the hierarchical 3D semantic map.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 7 (3 Method), p. 7 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | timestep, system, takes, input, current, RGB-D, observation, agent, pose, text-specified, target, outputs, navigation, action | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | timestep, system, takes, input, current, RGB-D, observation, agent, pose, text-specified | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | contributions, mainly, summarized, follows, BeliefMapNav, efficient, zero-shot, object, navigation, system | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | objective, improves, search, efficiency, minimizing, exploration, cost, optimized, paths, prioritizing | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3 Method - extractive body cue:** At each timestep, the system takes as input the current RGB-D observation It, the agent's pose st, and the text-specified target c, and outputs a ...
- **p. 4 / 3 Method - extractive body cue:** The observation-based belief planning module selects the next goal based on this belief and outputs navigation actions.
- **p. 6 / 3 Method - extractive body cue:** This fusion enables more dynamic and accurate estimation of the belief of detecting the target from each frontier's FOV by combining spatial priors belief map ...
- **p. 2 / 1 Introduction - extractive body cue:** 2)The frontier observation belief estimation module combines the belief map with a visibility map, which encodes real-time observation feedback likelihood, to produce posterior beliefs of ...
- **p. 3 / 3 Method - extractive body cue:** At each timestep t, the agent receives RGB-D observations It = (Irgb t , Idepth t ), where Irgb t ∈RH×W ×3 and Idepth t ...
- **p. 4 / 3 Method - extractive body cue:** During exploration, the 3D voxel-based belief mapping module fuses sensor input, the 3D hierarchical semantic map, and landmarks to create a belief map.
- **p. 5 / 3 Method - extractive body cue:** The module operates in three stages: 1) Multi-scale feature extraction: Extract image CLIP features from multi-scale RGB images and spatial information from the depth images.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | At each timestep t, the agent receives RGB-D observations It = (Irgb t , Idepth t ), where Irgb t ∈RH×W ×3 ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | At each timestep, the system takes as input the current RGB-D observation It, the agent's pose st, and the text-specified target c, ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | Implementation details: We limit navigation to 500 steps, defining success as stopping within 0.1m of the target. | hardware, batch and throughput |

## Training vs Inference

- **p. 9 / 3 Method - extractive body cue:** However, CLIP demonstrates stronger generalization to out-of-distribution data and supports efficient inference via independent encoders and pre-computed features.
- **p. 9 / 3 Method - extractive body cue:** However, CLIP demonstrates stronger generalization to out-of-distribution data and supports efficient inference via independent encoders and pre-computed features.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** timestep, system, takes, input, current, RGB-D, observation, agent, pose, text-specified, target, outputs, navigation, action, discrete, observation-based, belief, planning, module, selects.
- **Relevant PDF headings:** 3 Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | HSSD, a synthetic dataset with scenes based on real house layouts, contains 40 validation scenes, 1,248 navigation episodes, and 6 object categories. | p. 7 (3 Method), p. 7 (3 Method) |
| Global / local decision | As shown in Table 1, our method outperforms all existing zero-shot baselines, achieving significant improvements across multiple benchmarks. | p. 8 (3 Method), p. 8 (3 Method) |
| Motion execution / recovery | On the HM3D dataset, our method improves SPL by 46.4% compared to the zero-shot method InstructNav [9], which achieves the highest SR. | p. 8 (3 Method), p. 8 (3 Method) |

## Failure and Ablation Link

- **p. 8 / 3 Method - extractive body cue:** 4.3 Ablative study To evaluate the effectiveness of each module in our system, we conduct an ablation study on 400 randomly sampled episodes from the ...
- **p. 9 / 3 Method - extractive body cue:** Effectiveness of hierarchical landmarks: As shown in Table 4, without landmarks, we retrieve directly using the object name in the hierarchical 3D semantic map.
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4: Visualization of the prior belief map, visibility map, and the posterior belief map, with an enlarged section highlighting the target object. Effectiveness of ...
- **p. 7 / 3 Method - extractive body cue:** Ablation studies assess each component's contribution.
- **p. 7 / 3 Method - extractive body cue:** Baseline summaries and HM3D failure analyses appear in Appendix A.6 and A.7, respectively.
- **p. 8 / 3 Method - extractive body cue:** Across all datasets, the performance limitations of the local planner in [7] lead to significant degradation, especially in narrow areas.
- **p. 8 / 3 Method - extractive body cue:** Second, a lot of mesh "holes" in MP3D, which allow the agent to see through obstacles, causing it to mistakenly prioritize these holes as targets, ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 9 (3 Method), p. 7 (3 Method), objective p. 7 (3 Method), p. 7 (3 Method), p. 4 (3 Method), p. 8 (3 Method), p. 4 (3 Method), p. 5 (3 Method), temporal p. 3 (3 Method), p. 3 (3 Method), p. 7 (3 Method), p. 4 (3 Method), p. 4 (3 Method), p. 6 (3 Method).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
