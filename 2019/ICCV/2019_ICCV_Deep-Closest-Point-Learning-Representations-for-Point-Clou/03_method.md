# Method - Deep Closest Point: Learning Representations for Point Cloud Registration

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1905.03304; PDF retrieval source: https://arxiv.org/pdf/1905.03304. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (4.5. Loss), p. 5 (4.5. Loss)): The initial feature module (§4.1) and the attention module (§4.2) are both parameterized by a set of neural network weights, which must be learned during a training phase.

## Method Body Digest

- **p. 5 / 4.5. Loss - extractive body cue:** The initial feature module (§4.1) and the attention module (§4.2) are both parameterized by a set of neural network weights, which must be learned during ...
- **p. 5 / 4.5. Loss - extractive body cue:** We use the following loss function to measure our model's agreement to the ground-truth rigid motions: Loss = ∥R⊤ XYRg XY -I∥2 + ∥tXY -tg ...
- **p. 5 / 4.5. Loss - extractive body cue:** The third term denotes Tikhonov regularization of the DCP parameters θ, which serves to reduce the complexity of the network.
- **p. 2 / 1. Introduction - extractive body cue:** Our model consists of three parts: (1) We map the input point clouds to permutation/rigid-invariant embeddings that help identify matching pairs of points (we compare ...
- **p. 1 / 1. Introduction - extractive body cue:** Given these two observations, most algorithms alternate between these two steps to try to obtain a better result.
- **p. 2 / 1. Introduction - extractive body cue:** These algorithms are typically slower than ICP and still do not always provide acceptable output.
- **p. 3 / 3. Problem Statement - extractive body cue:** We use X and Y to denote two point clouds, where X = {x1, . . . , xi, . . . , xN} ⊂R3 ...
- **p. 5 / 4.5. Loss - extractive body cue:** Combined, the modules above map from a pair of point clouds X and Y to a rigid motion [RXY, tXY] that aligns them to each ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Contributions: Our contributions include the following: • We identify sub-network architectures designed to address difficulties in the classical ICP pipeline. • We propose a simple ...
- **p. 1 / 1. Introduction - extractive body cue:** However, only our method achieve satisfying alignment for objects with sharp features and large transformation. globally optimal alignment; similarly, computing matchings becomes easier given some ...
- **p. 2 / 1. Introduction - extractive body cue:** Our model consists of three parts: (1) We map the input point clouds to permutation/rigid-invariant embeddings that help identify matching pairs of points (we compare ...

## Source Evidence Cues

- **p. 5 / 4.5. Loss - extractive body cue:** The initial feature module (§4.1) and the attention module (§4.2) are both parameterized by a set of neural network weights, which must be learned during ...
- **p. 5 / 4.5. Loss - extractive body cue:** We use the following loss function to measure our model's agreement to the ground-truth rigid motions: Loss = ∥R⊤ XYRg XY -I∥2 + ∥tXY -tg ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | The initial feature module (§4.1) and the attention module (§4.2) are both parameterized by a set of neural network weights, which must ... | p. 5 (4.5. Loss), p. 5 (4.5. Loss) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | We use the following loss function to measure our model's agreement to the ground-truth rigid motions: Loss = ∥R⊤ XYRg XY -I∥2 ... | p. 5 (4.5. Loss) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | The initial feature module (§4.1) and the attention module (§4.2) are both parameterized by a set of neural network weights, which must ... | p. 5 (4.5. Loss) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4.5. Loss - extractive body cue:** We use the following loss function to measure our model's agreement to the ground-truth rigid motions: Loss = ∥R⊤ XYRg XY -I∥2 + ∥tXY -tg ...
- **p. 5 / 4.5. Loss - extractive body cue:** The third term denotes Tikhonov regularization of the DCP parameters θ, which serves to reduce the complexity of the network.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (4.5. Loss).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | model, consists, three, parts, input, point, clouds, permutation/rigid-invariant, embeddings, help, identify, matching, pairs, points | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | model, consists, three, parts, input, point, clouds, permutation/rigid-invariant, embeddings, help | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Contributions, include, following, identify, sub-network, architectures, designed, address, difficulties, classical | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | following, loss, function, measure, model, agreement, ground-truth, rigid, motions, XYRg | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** Our model consists of three parts: (1) We map the input point clouds to permutation/rigid-invariant embeddings that help identify matching pairs of points (we compare ...
- **p. 1 / 1. Introduction - extractive body cue:** Given these two observations, most algorithms alternate between these two steps to try to obtain a better result.
- **p. 2 / 1. Introduction - extractive body cue:** These algorithms are typically slower than ICP and still do not always provide acceptable output.
- **p. 3 / 3. Problem Statement - extractive body cue:** We use X and Y to denote two point clouds, where X = {x1, . . . , xi, . . . , xN} ⊂R3 ...
- **p. 5 / 4.5. Loss - extractive body cue:** Combined, the modules above map from a pair of point clouds X and Y to a rigid motion [RXY, tXY] that aligns them to each ...
- **p. 4 / 3. Problem Statement - extractive body cue:** Our goal is to use learned embeddings to recover a better matching m(·) and use that to compute a rigid transformation, which we will detail ...
- **p. 5 / 4.5. Loss - extractive body cue:** We employ a fairly straightforward strategy for training, measuring deviation of [RXY, tXY] from ground truth for synthetically-generated pairs of point clouds.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | We profile the inference time of different methods on a desktop computer with an Intel I7-7700 CPU, an Nvidia GTX 1070 GPU, ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Given these two observations, most algorithms alternate between these two steps to try to obtain a better result. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | We profile the inference time of different methods on a desktop computer with an Intel I7-7700 CPU, an Nvidia GTX 1070 GPU, ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | We profile the inference time of different methods on a desktop computer with an Intel I7-7700 CPU, an Nvidia GTX 1070 GPU, ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 4.5. Loss - extractive body cue:** The initial feature module (§4.1) and the attention module (§4.2) are both parameterized by a set of neural network weights, which must be learned during ...
- **p. 7 / 5.5. Efficiency - extractive body cue:** We profile the inference time of different methods on a desktop computer with an Intel I7-7700 CPU, an Nvidia GTX 1070 GPU, and 32G memory.
- **p. 6 / 5. Experiments - extractive body cue:** We divide the learning rate by 10 at epochs 75, 150, and 200, training for a total of 250 epochs.
- **p. 7 / 5.4. DCP Followed By ICP - extractive body cue:** Inference time (in seconds) Metrics PN+DCP-v1, DGCNN+DCP-v1 PN+DCP-v2 DGCNN+DCP-v2 MSE(R) 17.008427 6.480572 49.863022 1.307329 RMSE(R) 4.124127 2.545697 7.061375 1.143385 MAE(R) 2.800184 1.505548 4.485052 0.770573 MSE(t) ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** initial, feature, module, attention, parameterized, neural, network, weights, must, learned, during, training, phase, following, loss, function, measure, model, agreement, ground-truth.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | ModelNet40: Full Dataset Train & Test In our first experiment, we randomly divide all the point clouds in the ModelNet40 dataset into ... | p. 6 (5. Experiments), p. 6 (5. Experiments) |
| Semantic / temporal fusion | DCP-v1 already outperforms other methods under all the performance metrics, and DCP-v2 exhibits even stronger performance. | p. 6 (5. Experiments), p. 5 (5. Experiments) |
| Robot query / planning handoff | DCP-v1 already outperforms other methods under all the performance metrics, and DCP-v2 exhibits even stronger performance. | p. 6 (5. Experiments), p. 8 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 7 / Figure/Table caption - extractive body cue:** Table 5. Ablation study: PointNet or DGCNN? use ICP as a local algorithm by initializing ICP with a rigid transformation output from our DCP model. ...
- **p. 5 / 5. Experiments - extractive body cue:** We denote our model without attention (§4.2) as DCP-v1 and the full model with 5
- **p. 6 / 5. Experiments - extractive body cue:** We use LayerNorm [3] without Dropout [39].
- **p. 7 / Figure/Table caption - extractive body cue:** Table 7. Ablation study: Embedding dimension
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4. Results of DCP-v2. Top: inputs. Bottom: outputs of DCP-v2. lems as a drop-in replacement for ICP with improved behav- ior. Beyond its direct ...
- **p. 6 / 5.4. DCP Followed By ICP - extractive body cue:** In large part, this failure is due to the lack of a good initial guess.
- **p. 6 / 5.4. DCP Followed By ICP - extractive body cue:** Since our experiments involve point clouds whose initial poses are far from aligned, ICP fails nearly every experiment we have presented so far.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (4.5. Loss), p. 5 (4.5. Loss), objective p. 5 (4.5. Loss), p. 5 (4.5. Loss), temporal p. 7 (5.5. Efficiency), p. 1 (1. Introduction), p. 2 (2. Related Work), p. 2 (1. Introduction), p. 3 (2. Related Work), p. 3 (2. Related Work).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
