# Method - Where2Act: From Pixels to Actions for Articulated 3D Objects

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2101.02692; PDF retrieval source: https://arxiv.org/pdf/2101.02692. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (4.1. Network Modules), p. 3 (4.1. Network Modules), p. 4 (4.3. Training and Losses), p. 4 (4.2. Collecting Training Data), p. 5 (4.3. Training and Losses), p. 5 (4.3. Training and Losses)): To decode the per-pixel actionable information, we propose three decoding heads: (c) an actionability scoring module Da that predicts a score ap ∈[0,1]; (d) an action proposal module Dr that ...

## Method Body Digest

- **p. 3 / 4.1. Network Modules - extractive body cue:** To decode the per-pixel actionable information, we propose three decoding heads: (c) an actionability scoring module Da that predicts a score ap ∈[0,1]; (d) an ...
- **p. 3 / 4.1. Network Modules - extractive body cue:** For the 3D experiments, we use PointNet++ segmentation network [34] and implementation [47] with 4 set abstraction layers with single-scale grouping for the encoder and ...
- **p. 4 / 4.3. Training and Losses - extractive body cue:** We empirically find it beneficial to first train the action scoring module Ds and then train the three decoders jointly.
- **p. 4 / 4.2. Collecting Training Data - extractive body cue:** We employ a hybrid data sampling strategy where we first sample large amount of offline random interaction trajectories to bootstrap the learning and then adaptively ...
- **p. 5 / 4.3. Training and Losses - extractive body cue:** We leverage the Min-of-N strategy [8] to train the action proposal module Dr, which is essentially a conditional generative model that maps a pixel p ...
- **p. 5 / 4.3. Training and Losses - extractive body cue:** Given a batch of B interaction data points {(Si, pi,Ri,ri)}i where ri = 1 (positive) and ri = 0 (negative) denote the ground-truth interaction outcome, ...
- **p. 5 / 4.3. Training and Losses - extractive body cue:** After adjusting the relative loss scales to the same level, we obtain the final objective function L = Ls +Lr +100×La.
- **p. 4 / 4.1. Network Modules - extractive body cue:** For an action proposal R at pixel p, we finally estimate a likelihood sR/p ∈[0,1] for the success of the interaction parametrized by tuple (p,R) ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are: • we formulate the task of inferring affordances for manipulating 3D articulated objects by predicting per-pixel action likelihoods and proposals; ...
- **p. 2 / 1. Introduction - extractive body cue:** We empirically show that our method successfully learns to predict possible actions for novel objects, and does so even for previously unseen categories.
- **p. 3 / 4. Method - extractive body cue:** We propose a learning-from-interaction approach to tackle this task.

## Source Evidence Cues

- **p. 3 / 4.1. Network Modules - extractive body cue:** To decode the per-pixel actionable information, we propose three decoding heads: (c) an actionability scoring module Da that predicts a score ap ∈[0,1]; (d) an ...
- **p. 3 / 4.1. Network Modules - extractive body cue:** For the 3D experiments, we use PointNet++ segmentation network [34] and implementation [47] with 4 set abstraction layers with single-scale grouping for the encoder and ...
- **p. 4 / 4.3. Training and Losses - extractive body cue:** We empirically find it beneficial to first train the action scoring module Ds and then train the three decoders jointly.
- **p. 4 / 4.2. Collecting Training Data - extractive body cue:** We employ a hybrid data sampling strategy where we first sample large amount of offline random interaction trajectories to bootstrap the learning and then adaptively ...
- **p. 5 / 4.3. Training and Losses - extractive body cue:** We leverage the Min-of-N strategy [8] to train the action proposal module Dr, which is essentially a conditional generative model that maps a pixel p ...
- **p. 5 / 4.3. Training and Losses - extractive body cue:** Given a batch of B interaction data points {(Si, pi,Ri,ri)}i where ri = 1 (positive) and ri = 0 (negative) denote the ground-truth interaction outcome, ...
- **Detected method headings:** 4. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | To decode the per-pixel actionable information, we propose three decoding heads: (c) an actionability scoring module Da that predicts a score ap ... | p. 3 (4.1. Network Modules), p. 3 (4.1. Network Modules) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | For the 3D experiments, we use PointNet++ segmentation network [34] and implementation [47] with 4 set abstraction layers with single-scale grouping for ... | p. 3 (4.1. Network Modules), p. 4 (4.3. Training and Losses) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | We empirically find it beneficial to first train the action scoring module Ds and then train the three decoders jointly. | p. 4 (4.3. Training and Losses), p. 4 (4.2. Collecting Training Data) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4.3. Training and Losses - extractive body cue:** After adjusting the relative loss scales to the same level, we obtain the final objective function L = Ls +Lr +100×La.
- **p. 5 / 4.3. Training and Losses - extractive body cue:** Given a batch of B interaction data points {(Si, pi,Ri,ri)}i where ri = 1 (positive) and ri = 0 (negative) denote the ground-truth interaction outcome, ...
- **p. 4 / 4.1. Network Modules - extractive body cue:** For an action proposal R at pixel p, we finally estimate a likelihood sR/p ∈[0,1] for the success of the interaction parametrized by tuple (p,R) ...
- **p. 4 / 4.2. Collecting Training Data - extractive body cue:** Then, we sample one position p∗ to conduct an additional interaction trial (p∗,R) according to the SoftMax normalized probability distribution over all possible interaction positions.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (4.3. Training and Losses), p. 5 (4.3. Training and Losses).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Taking, input, single, RGB, image, partial, point, cloud, employ, encoder-decoder, backbone, extract, per-pixel, features | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Taking, input, single, RGB, image, partial, point, cloud, employ, encoder-decoder | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summary, contributions, formulate, task, inferring, affordances, manipulating, articulated, objects, predicting | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | After, adjusting, relative, loss, scales, same, level, obtain, final, objective | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 4. Method - extractive body cue:** Taking as input a single RGB image or a partial 3D point cloud, we employ an encoder-decoder backbone to extract per-pixel features and design three ...
- **p. 1 / 1. Introduction - extractive body cue:** Given as input an articulated 3D object, we learn to propose the actionable information for different robotic manipulation primitives (e.g. pushing, pulling): (a) the predicted ...
- **p. 2 / 1. Introduction - extractive body cue:** We therefore propose an on-policy data sampling strategy to alleviate this issue - by biasing the sampling towards actions the agents thinks are likely to ...
- **p. 3 / 4.1. Network Modules - extractive body cue:** The network outputs one scalar ap after applying the Sigmoid function, where a higher score indicates a higher chance for successful interaction.
- **p. 4 / 4.1. Network Modules - extractive body cue:** Given an input tuple (fp,R), we produce a scalar sR/p ∈[0,1], sR/p = Ds (fp,R), (3) where sR/p > 0.5 indicates a positive action proposal ...
- **p. 2 / 1. Introduction - extractive body cue:** We therefore limit our work to considering the plausible short-term interactions that an agent can perform given the current state of the object.
- **p. 4 / 4.2. Collecting Training Data - extractive body cue:** 3 (b)) with pre-programmed interaction trajectories, each of which is parameterized by the gripper pose (p,R) ∈SE(3) at the beginning.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | (a) Our interactive simulation environment: we show the local gripper frame by the red, green and blue axes, which corresponds to the ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | We propose a learning-from-interaction framework with an online data sampling strategy that allows us to train the network in simulation (SAPIEN) and ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 4.1. Network Modules - extractive body cue:** To decode the per-pixel actionable information, we propose three decoding heads: (c) an actionability scoring module Da that predicts a score ap ∈[0,1]; (d) an ...
- **p. 4 / 4.3. Training and Losses - extractive body cue:** We empirically find it beneficial to first train the action scoring module Ds and then train the three decoders jointly.
- **p. 4 / 4.2. Collecting Training Data - extractive body cue:** We employ a hybrid data sampling strategy where we first sample large amount of offline random interaction trajectories to bootstrap the learning and then adaptively ...
- **p. 5 / 4.3. Training and Losses - extractive body cue:** We leverage the Min-of-N strategy [8] to train the action proposal module Dr, which is essentially a conditional generative model that maps a pixel p ...
- **p. 5 / 4.3. Training and Losses - extractive body cue:** Given a batch of B interaction data points {(Si, pi,Ri,ri)}i where ri = 1 (positive) and ri = 0 (negative) denote the ground-truth interaction outcome, ...
- **p. 4 / 4.3. Training and Losses - extractive body cue:** We empirically find it beneficial to first train the action scoring module Ds and then train the three decoders jointly.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** decode, per-pixel, actionable, information, three, decoding, heads, actionability, scoring, module, predicts, score, action, proposal, proposes, multiple, gripper, orientations, Rz/p, sampled.
- **Relevant PDF headings:** 4. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Equipped with a large-scale PartNetMobility dataset, SAPIEN [49] provides a physics-rich simulation environment that supports robot actuators interacting with 2,346 3D CAD ... | p. 5 (5.1. Framework and Settings), p. 5 (5.1. Framework and Settings) |
| Semantic / temporal fusion | We propose two quantitative metrics for evaluating performance of our proposed method, compared with three baseline methods and one ablated version of ... | p. 6 (5.2. Metrics and Baselines), p. 6 (5.2. Metrics and Baselines) |
| Robot query / planning handoff | We observe that 3D-ours achieves the best performance. validates that our network learns geometric features more than local normals and curvatures. | p. 7 (5.2. Metrics and Baselines), p. 7 (5.2. Metrics and Baselines) |

## Failure and Ablation Link

- **p. 6 / 5.2. Metrics and Baselines - extractive body cue:** To validate the effectiveness of the proposed method and provide benchmarks for the proposed task, we compare to three baseline methods and one ablated version ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Ablation Study. We compare our method to an ablated version, where we remove the online adaptive sampling. It is clear to see that ...
- **p. 6 / 5.2. Metrics and Baselines - extractive body cue:** We define the final measure as below. ssr = # successful proposals # total proposals (8) Baselines and Ablation Study.
- **p. 7 / 5.3. Results and Analysis - extractive body cue:** The ablation study shown in Table 3 further validates that the online data sampling (OS) strategy helps boost the performance.
- **p. 5 / 5.1. Framework and Settings - extractive body cue:** We conduct our experiments using 15 selected object categories in the PartNet-Mobility dataset, after removing the objects that are either too small (e.g. pens, USB ...
- **p. 12 / Figure/Table caption - extractive body cue:** Figure 7. Failure Cases. We visualize some interesting failure cases, which demonstrate the difficulty of the task and some am- biguous cases that are hard ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. We visualize (a) the actionability scoring and (b) the action proposal predictions on an example cabinet with a door that can be slipped ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (4.1. Network Modules), p. 3 (4.1. Network Modules), p. 4 (4.3. Training and Losses), p. 4 (4.2. Collecting Training Data), p. 5 (4.3. Training and Losses), p. 5 (4.3. Training and Losses), objective p. 5 (4.3. Training and Losses), p. 5 (4.3. Training and Losses), p. 4 (4.1. Network Modules), p. 4 (4.2. Collecting Training Data), temporal p. 4 (4.1. Network Modules), p. 1 (Abstract), p. 4 (4.2. Collecting Training Data), p. 6 (5.2. Metrics and Baselines), p. 6 (5.2. Metrics and Baselines), p. 7 (5.2. Metrics and Baselines).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
