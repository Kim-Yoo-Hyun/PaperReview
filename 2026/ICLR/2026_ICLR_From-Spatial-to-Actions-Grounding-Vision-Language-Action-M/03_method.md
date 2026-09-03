# Method - From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=fzmittHfq3; PDF retrieval source: https://openreview.net/pdf/d6aae457099a5d9e50bba1a6bbc48d8756a15c91.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 6 (3 Methodology), p. 4 (3 Methodology), p. 6 (3 Methodology), p. 4 (3 Methodology), p. 5 (3 Methodology), p. 5 (3 Methodology)): These are then concatenated with a learnable camera token tcam ∈RDs and fed into a Spatial Encoder Espl(·), which consists of N cross-attention and self-attention blocks: (Tspl,ˆtcam) = Espl(Tvis, tcam).

## Method Body Digest

- **p. 6 / 3 Methodology - extractive body cue:** These are then concatenated with a learnable camera token tcam ∈RDs and fed into a Spatial Encoder Espl(·), which consists of N cross-attention and self-attention ...
- **p. 4 / 3 Methodology - extractive body cue:** 2, FALCON is an end-to-end VLA consists of three core components: (1) a 2D VLM for multimodal semantic representation, (2) an ESM for extracting 3D ...
- **p. 6 / 3 Methodology - extractive body cue:** To address this limitation, we propose an Embodied Spatial Model that injects 3D conditions (i.e., depth, pose) to build more accurate spatial representations, enabling our ...
- **p. 4 / 3 Methodology - extractive body cue:** To this end, we propose FALCON, a generalist robot policy that overcomes limitations of prior VLAs by integrating rich geometric priors from spatial foundation models ...
- **p. 5 / 3 Methodology - extractive body cue:** 3.3 Training Objective During the training process of FALCON, the objective for action sequence generation is formulated as the minimization of a composite loss function ...
- **p. 5 / 3 Methodology - extractive body cue:** The overall loss function is defined as: L = t+C-1 X i=t MSE(ˆai,pose, ai,pose) + λ · BCE(ˆai,gripper, ai,gripper), (2) where the MSE term penalizes ...
- **p. 7 / 3 Methodology - extractive body cue:** We explore two distinct architectures for this predictor: An MLP-based predictor directly maps the current fused feature vector to an action output: At = π(f ...
- **p. 5 / 3 Methodology - extractive body cue:** The weighting factor λ balances the contributions of the two loss terms, ensuring stable and representative learning across heterogeneous action components.

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** We propose FALCON (From Spatial to Action), a novel paradigm that integrates richer and more representative 3D spatial tokens into VLAs through an improved injection ...
- **p. 2 / 1 Introduction - extractive body cue:** Overall Benchmark Bridge Calvin (Zero-shot) Google Robot Calvin Real-World Real-World (Few-Shot) Figure 1 We propose FALCON, a vision-language-action model that achieves robust 3D spatial understanding ...
- **p. 3 / 1 Introduction - extractive body cue:** For limitation (2) of poor modality transferability, we introduce an Embodied Spatial Model that can optionally integrate extra 3D modalities (e.g., depth, poses).

## Source Evidence Cues

- **p. 6 / 3 Methodology - extractive body cue:** These are then concatenated with a learnable camera token tcam ∈RDs and fed into a Spatial Encoder Espl(·), which consists of N cross-attention and self-attention ...
- **p. 4 / 3 Methodology - extractive body cue:** 2, FALCON is an end-to-end VLA consists of three core components: (1) a 2D VLM for multimodal semantic representation, (2) an ESM for extracting 3D ...
- **p. 6 / 3 Methodology - extractive body cue:** To address this limitation, we propose an Embodied Spatial Model that injects 3D conditions (i.e., depth, pose) to build more accurate spatial representations, enabling our ...
- **p. 4 / 3 Methodology - extractive body cue:** To this end, we propose FALCON, a generalist robot policy that overcomes limitations of prior VLAs by integrating rich geometric priors from spatial foundation models ...
- **p. 5 / 3 Methodology - extractive body cue:** 3.3 Training Objective During the training process of FALCON, the objective for action sequence generation is formulated as the minimization of a composite loss function ...
- **p. 5 / 3 Methodology - extractive body cue:** The overall loss function is defined as: L = t+C-1 X i=t MSE(ˆai,pose, ai,pose) + λ · BCE(ˆai,gripper, ai,gripper), (2) where the MSE term penalizes ...
- **p. 7 / 3 Methodology - extractive body cue:** We explore two distinct architectures for this predictor: An MLP-based predictor directly maps the current fused feature vector to an action output: At = π(f ...
- **Detected method headings:** 3 Methodology (p. 4); A.2 Embodied Spatial Model Training Paradigm (p. 16)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | These are then concatenated with a learnable camera token tcam ∈RDs and fed into a Spatial Encoder Espl(·), which consists of N ... | p. 6 (3 Methodology), p. 4 (3 Methodology) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | 2, FALCON is an end-to-end VLA consists of three core components: (1) a 2D VLM for multimodal semantic representation, (2) an ESM ... | p. 4 (3 Methodology), p. 6 (3 Methodology) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | To address this limitation, we propose an Embodied Spatial Model that injects 3D conditions (i.e., depth, pose) to build more accurate spatial ... | p. 6 (3 Methodology), p. 4 (3 Methodology) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3 Methodology - extractive body cue:** 3.3 Training Objective During the training process of FALCON, the objective for action sequence generation is formulated as the minimization of a composite loss function ...
- **p. 5 / 3 Methodology - extractive body cue:** The weighting factor λ balances the contributions of the two loss terms, ensuring stable and representative learning across heterogeneous action components.
- **p. 6 / 3 Methodology - extractive body cue:** As for supervision, we follow VGGT [40] to adopt depth, point map, and pose losses to formulate multi-task supervision.
- **p. 6 / 3 Methodology - extractive body cue:** After obtaining the GT pose token tgt-cam and depth tokens Tdpt, our objective is not only to achieve accurate reconstruction through the reconstruction head under ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3 Methodology), p. 5 (3 Methodology), p. 6 (3 Methodology), p. 6 (3 Methodology).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Problem, Definition, study, task-oriented, robot, control, where, must, interpret, visual, observations, time, step, natural | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Problem, Definition, study, task-oriented, robot, control, where, must, interpret, visual | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | FALCON, Spatial, Action, novel, paradigm, integrates, richer, more, representative, tokens | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Training, Objective, During, process, FALCON, action, sequence, generation, formulated, minimization | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3 Methodology - extractive body cue:** 3.1 Problem Definition We study the problem of task-oriented robot control, where a robot must interpret visual observations Ot = {I1 t , . . ...
- **p. 5 / 3 Methodology - extractive body cue:** At timestep t, the VLM processes visual observations Ot and language instructions L to produce a semantic action token ˆtact.
- **p. 4 / 3 Methodology - extractive body cue:** A learnable action token tact is appended to it, and the corresponding output hidden state ˆtact ∈RDact, where Dact represents the feature dimension, is extracted ...
- **p. 5 / 3 Methodology - extractive body cue:** Depth Inject x L Blocks Image Depth Camera Output Embodied Spatial Model Spatial-Enhanced Action Head Spatial Token Image Enc.
- **p. 6 / 3 Methodology - extractive body cue:** 2, the proposed Spatial-Enhanced Action Head integrates geometric representations Tspl from the ESM with semantic features ˆtact from the VLM, enabling more accurate and spatially-aware ...
- **p. 1 / 1 Introduction - extractive body cue:** Recent advances in vision-language-action models (VLAs) have significantly advanced the pursuit of generalist robotics, enabling robots to interpret natural language instructions and execute intricate action ...
- **p. 7 / 3 Methodology - extractive body cue:** We explore two distinct architectures for this predictor: An MLP-based predictor directly maps the current fused feature vector to an action output: At = π(f ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | 3.1 Problem Definition We study the problem of task-oriented robot control, where a robot must interpret visual observations Ot = {I1 t ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | For long-horizon robotic tasks that involve sequential decision-making, we employ a predictor based on the long short-term memory (LSTM) network [8, 11] ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | For long-horizon robotic tasks that involve sequential decision-making, we employ a predictor based on the long short-term memory (LSTM) network [8, 11] ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Each task is evaluated over 10 different scene layouts with 10 trials, resulting in a total of 90 rollouts. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3 Methodology - extractive body cue:** 3.3 Training Objective During the training process of FALCON, the objective for action sequence generation is formulated as the minimization of a composite loss function ...
- **p. 9 / 4 Experiments - extractive body cue:** Each task is evaluated over 10 different scene layouts with 10 trials, resulting in a total of 90 rollouts.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** then, concatenated, learnable, camera, token, tcam, RDs, Spatial, Encoder, Espl, consists, cross-attention, self-attention, blocks, Tspl, Tvis, FALCON, end-to-end, VLA, three.
- **Relevant PDF headings:** 3 Methodology (p. 4); A.2 Embodied Spatial Model Training Paradigm (p. 16).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | All models are initially pre-trained on a mixture of the Open X-Embodiment dataset [29] and then fine-tuned with multi-task real-robot data. | p. 8 (4 Experiments), p. 10 (4 Experiments) |
| Semantic / temporal fusion | 2 reports the results on the Bridge-WidowX setup, where FALCON consistently outperforms all baselines and achieves best performance. | p. 8 (4 Experiments), p. 7 (4 Experiments) |
| Robot query / planning handoff | 3, FALCON achieves the highest average success rate of 70.0% across all nine task suites, outperforming the advanced method SpatialVLA [31] (44.4%) ... | p. 8 (4 Experiments), p. 7 (4 Experiments) |

## Failure and Ablation Link

- **p. 10 / 4 Experiments - extractive body cue:** To verify the effectiveness of our strategy for injecting 3D information into the action head, we evaluate a variant following the approach of most 3D-based ...
- **p. 11 / 4 Experiments - extractive body cue:** Kosmos-VLA (w/ rgb-d) is a point cloud-based variant where the ESM is replaced by a lightweight point cloud encoder [46] while retaining other parts.
- **p. 9 / 4 Experiments - extractive body cue:** Success rates for individual variants and sub-tasks are provided in Appendix I.2.
- **p. 10 / 4 Experiments - extractive body cue:** 4.3 In-Depth Analysis Table 4 Ablation studies on spatial token injection methods and fusion strategies.
- **p. 11 / 4 Experiments - extractive body cue:** Kosmos-VLA (w/ rgb) is a 2D VLA without ESM.
- **p. 8 / 4 Experiments - extractive body cue:** All models are initially pre-trained on a mixture of the Open X-Embodiment dataset [29] and then fine-tuned with multi-task real-robot data.
- **p. 9 / 4 Experiments - extractive body cue:** For larger blocks, collisions frequently occur during the placement of the blue block, while smaller blocks are prematurely released before placement, leading to task failure.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 6 (3 Methodology), p. 4 (3 Methodology), p. 6 (3 Methodology), p. 4 (3 Methodology), p. 5 (3 Methodology), p. 5 (3 Methodology), objective p. 5 (3 Methodology), p. 5 (3 Methodology), p. 6 (3 Methodology), p. 6 (3 Methodology), temporal p. 4 (3 Methodology), p. 7 (3 Methodology), p. 7 (3 Methodology), p. 4 (3 Methodology), p. 5 (3 Methodology), p. 5 (3 Methodology).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (27 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** A learnable action token tact is appended to it, and the corresponding output hidden state ˆtact ∈RDact, where Dact represents the feature dimension, is extracted as the semantic action representation, ... (p. 4, 3 Methodology).
- **Objective/update evidence:** 3.3 Training Objective During the training process of FALCON, the objective for action sequence generation is formulated as the minimization of a composite loss function over the predicted action horizon. (p. 5, 3 Methodology).
- **Temporal/runtime evidence:** For long-horizon robotic tasks that involve sequential decision-making, we employ a predictor based on the long short-term memory (LSTM) network [8, 11] that utilizes a history of feature representations. (p. 7, 3 Methodology).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
