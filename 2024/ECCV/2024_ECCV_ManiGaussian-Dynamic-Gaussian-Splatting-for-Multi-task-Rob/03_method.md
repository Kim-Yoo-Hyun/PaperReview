# Method - ManiGaussian: Dynamic Gaussian Splatting for Multi-task Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5194_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05194.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 8 (3 Approach), p. 6 (3 Approach), p. 10 (3 Approach), p. 8 (3 Approach), p. 5 (3 Approach), p. 9 (3 Approach)): More specifically, the Gaussian world model contains a representation network qϕ that learns high-level visual features with rich semantics for the input observation, a Gaussian regressor gϕ that predicts the ...

## Method Body Digest

- **p. 8 / 3 Approach - extractive body cue:** More specifically, the Gaussian world model contains a representation network qϕ that learns high-level visual features with rich semantics for the input observation, a Gaussian ...
- **p. 6 / 3 Approach - extractive body cue:** 3.3 Dynamic Gaussian Splatting for Robotic Manipulation In order to capture the scene-level dynamics for general manipulation tasks, we propose a dynamic Gaussian Splatting framework ...
- **p. 10 / 3 Approach - extractive body cue:** In training, we set a warm-up phase that freezes the deformation predictor to learn a stable representation model and a Gaussian regressor during the first ...
- **p. 8 / 3 Approach - extractive body cue:** To achieve this goal, we introduce the consistency objective between the realistic current observation and the rendered according
- **p. 5 / 3 Approach - extractive body cue:** Existing methods leverage powerful visual representations to learn informative latent features for optimal action prediction.
- **p. 9 / 3 Approach - extractive body cue:** Specifically, the training objective aligns the predicted future scenes based on different observations and actions with the realistic ones, which can be formulated as follows: ...
- **p. 6 / 3 Approach - extractive body cue:** 2: The overall pipeline of ManiGaussian, which primarily consists of a dynamic Gaussian Splatting framework and a Gaussian world model.
- **p. 9 / 3 Approach - extractive body cue:** We employ a multi-modal transformer PerceiverIO [25] to infer the selection probability of different action candidates based on the Gaussian parameters and the human language ...

## Design Rationale

- **p. 3 / 1 Introduction - extractive body cue:** Our contributions can be summarized as follows: - We propose a dynamic Gaussian Splatting framework to learn the scenelevel spatiotemporal dynamics in general robotic manipulation ...
- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we propose a ManiGaussian method that leverages a dynamic Gassuain Splatting framework for multi-task robotic manipulation.
- **p. 2 / 1 Introduction - extractive body cue:** Different from conventional methods which only focus on semantic representation, our method mines the scene-level spatiotemporal dynamics via future scene reconstruction.

## Source Evidence Cues

- **p. 8 / 3 Approach - extractive body cue:** More specifically, the Gaussian world model contains a representation network qϕ that learns high-level visual features with rich semantics for the input observation, a Gaussian ...
- **p. 6 / 3 Approach - extractive body cue:** 3.3 Dynamic Gaussian Splatting for Robotic Manipulation In order to capture the scene-level dynamics for general manipulation tasks, we propose a dynamic Gaussian Splatting framework ...
- **p. 10 / 3 Approach - extractive body cue:** In training, we set a warm-up phase that freezes the deformation predictor to learn a stable representation model and a Gaussian regressor during the first ...
- **p. 8 / 3 Approach - extractive body cue:** To achieve this goal, we introduce the consistency objective between the realistic current observation and the rendered according
- **p. 5 / 3 Approach - extractive body cue:** Existing methods leverage powerful visual representations to learn informative latent features for optimal action prediction.
- **p. 9 / 3 Approach - extractive body cue:** Specifically, the training objective aligns the predicted future scenes based on different observations and actions with the realistic ones, which can be formulated as follows: ...
- **p. 6 / 3 Approach - extractive body cue:** 2: The overall pipeline of ManiGaussian, which primarily consists of a dynamic Gaussian Splatting framework and a Gaussian world model.
- **Detected method headings:** 3 Approach (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | More specifically, the Gaussian world model contains a representation network qϕ that learns high-level visual features with rich semantics for the input ... | p. 8 (3 Approach), p. 6 (3 Approach) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | 3.3 Dynamic Gaussian Splatting for Robotic Manipulation In order to capture the scene-level dynamics for general manipulation tasks, we propose a dynamic ... | p. 6 (3 Approach), p. 10 (3 Approach) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | In training, we set a warm-up phase that freezes the deformation predictor to learn a stable representation model and a Gaussian regressor ... | p. 10 (3 Approach), p. 8 (3 Approach) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 9 / 3 Approach - extractive body cue:** We employ a multi-modal transformer PerceiverIO [25] to infer the selection probability of different action candidates based on the Gaussian parameters and the human language ...
- **p. 8 / 3 Approach - extractive body cue:** 3.4 Learning Objectives Current Scene Consistency Loss.
- **p. 9 / 3 Approach - extractive body cue:** The overall objective for our ManiGaussian agent is written as a weighted combination of different loss terms: \mat h cal {L}= \ mathcal { L}_{\text ...
- **p. 6 / 3 Approach - extractive body cue:** GS regressor 𝑔𝜙 Lifting PerceiverIO 𝑎𝑡𝑟𝑎𝑛𝑠 𝑎𝑟𝑜𝑡 𝑎𝑜𝑝𝑒𝑛 𝑎𝑐𝑜𝑙 Text Instruction 𝑎(𝑡) 𝑜(𝑡) = 𝐶(𝑡), 𝐷(𝑡), 𝑃(𝑡) Single-view RGB-D Voxelizing Robot action 𝑎(𝑡) Gaussian World ...
- **p. 8 / 3 Approach - extractive body cue:** To achieve this goal, we introduce the consistency objective between the realistic current observation and the rendered according
- **p. 5 / 3 Approach - extractive body cue:** Existing methods leverage powerful visual representations to learn informative latent features for optimal action prediction.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 8 (3 Approach), p. 9 (3 Approach), p. 6 (3 Approach), p. 8 (3 Approach), p. 9 (3 Approach).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | learn, manipulation, policy, effectively, expert, demonstrations, offline, datasets, provided, imitation, learning, where, sample, triplets | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | learn, manipulation, policy, effectively, expert, demonstrations, offline, datasets, provided, imitation | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | contributions, summarized, follows, dynamic, Gaussian, Splatting, framework, learn, scenelevel, spatiotemporal | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | employ, multi-modal, transformer, PerceiverIO, infer, selection, probability, different, action, candidates | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3 Approach - extractive body cue:** To learn the manipulation policy effectively, expert demonstrations as offline datasets are provided for imitation learning, where the sample triplets contain the visual input, language ...
- **p. 5 / 3 Approach - extractive body cue:** Based on the visual input o(t) and the language instructions, the agent is required to generate the optimal action for the robot arm and grippers ...
- **p. 8 / 3 Approach - extractive body cue:** More specifically, the Gaussian world model contains a representation network qϕ that learns high-level visual features with rich semantics for the input observation, a Gaussian ...
- **p. 8 / 3 Approach - extractive body cue:** For our robotic manipulation tasks, we instantiate the current state in the world model as the visual observation in the current step, and actions refer ...
- **p. 3 / 1 Introduction - extractive body cue:** Our contributions can be summarized as follows: - We propose a dynamic Gaussian Splatting framework to learn the scenelevel spatiotemporal dynamics in general robotic manipulation ...
- **p. 2 / 1 Introduction - extractive body cue:** For the first regard, semantic features extracted by perceptive models are directly leveraged to predict the robot actions according to the visual input such as ...
- **p. 9 / 3 Approach - extractive body cue:** Specifically, the training objective aligns the predicted future scenes based on different observations and actions with the realistic ones, which can be formulated as follows: ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Ours Observation Ground-truth Ours Ground-truth GNFactor PSNR=21.32 PSNR=24.59 (a) Front view (c) Novel view at future time step (b) Novel view at ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | For dynamic Gaussian Splatting, we leverage a Gaussian regressor to infer the Gaussian distribution of geometric and semantic features in the scene ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | An episode is considered successful if the agent completes the goal specified in natural language within a maximum of 25 steps. | hardware, batch and throughput |

## Training vs Inference

- **p. 10 / 3 Approach - extractive body cue:** In training, we set a warm-up phase that freezes the deformation predictor to learn a stable representation model and a Gaussian regressor during the first ...
- **p. 9 / 3 Approach - extractive body cue:** Specifically, the training objective aligns the predicted future scenes based on different observations and actions with the realistic ones, which can be formulated as follows: ...
- **p. 10 / 4 Experiments - extractive body cue:** All the compared methods are trained on two NVIDIA RTX 4090 GPUs for 100k iterations with a batch size of 2.
- **p. 12 / 4 Experiments - extractive body cue:** We first implement a vanilla baseline without any proposed technique, where we directly train the representation model and the action decoder to predict the robot ...
- **p. 13 / 4 Experiments - extractive body cue:** Both the compared methods get convergence within 100k training steps.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** More, specifically, Gaussian, world, model, contains, representation, network, learns, high-level, visual, features, rich, semantics, input, observation, regressor, predicts, parameters, different.
- **Relevant PDF headings:** 3 Approach (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | On the contrary, our ManiGaussian learns the scene dynamics with the proposed dynamic Gaussian Splatting framework, so that the robotic agent can ... | p. 11 (4 Experiments), p. 10 (4 Experiments) |
| Semantic / temporal fusion | Fig. 4: Case Study. The red mark signifies the pose deviates severely from the ex- pert demonstration, whereas the green mark indicates ... | p. 13 (Figure/Table caption), p. 11 (4 Experiments) |
| Robot query / planning handoff | Our method achieves the best performance with an average success rate of 44.8%, which is state-of-the-art, outperforming the previous arts including both ... | p. 11 (4 Experiments), p. 12 (4 Experiments) |

## Failure and Ablation Link

- **p. 10 / 4 Experiments - extractive body cue:** Then we compare our method with the state-of-the-art approaches to show the superiority in success rate (Section 4.2), and conduct an ablation study to verify ...
- **p. 12 / 4 Experiments - extractive body cue:** We conduct an ablation study to verify the effectiveness of each presented component in Table 2.
- **p. 12 / 4 Experiments - extractive body cue:** We first implement a vanilla baseline without any proposed technique, where we directly train the representation model and the action decoder to predict the robot ...
- **p. 14 / 4 Experiments - extractive body cue:** We remove the action loss here for better visualization.
- **p. 14 / 5 Conclusion - extractive body cue:** The limitations stem from the necessity of multiple view supervision with camera calibration for the Gaussian Splatting framework.
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: Consider the human instruction "stack two rose blocks", where the task is con- sidered successful if two rose blocks are stacked upon the ...
- **p. 14 / 4 Experiments - extractive body cue:** First, based on the front view observation where the gripper shape cannot be seen, our ManiGaussian offers superior detail in modeling cubes in novel views.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 8 (3 Approach), p. 6 (3 Approach), p. 10 (3 Approach), p. 8 (3 Approach), p. 5 (3 Approach), p. 9 (3 Approach), objective p. 9 (3 Approach), p. 8 (3 Approach), p. 9 (3 Approach), p. 6 (3 Approach), p. 8 (3 Approach), p. 5 (3 Approach), temporal p. 14 (4 Experiments), p. 6 (3 Approach), p. 10 (4 Experiments), p. 12 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
