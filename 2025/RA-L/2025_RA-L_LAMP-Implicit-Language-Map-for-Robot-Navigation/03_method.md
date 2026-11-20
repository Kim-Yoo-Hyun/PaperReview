# Method - LAMP: Implicit Language Map for Robot Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2602.11862; PDF retrieval source: https://arxiv.org/pdf/2602.11862. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD)): We introduce a map representation that continuously encodes language features within a large-scale space, ensuring memory efficiency and enabling fine-grained path planning.

## Method Body Digest

- **p. 2 / III. METHOD - extractive body cue:** We introduce a map representation that continuously encodes language features within a large-scale space, ensuring memory efficiency and enabling fine-grained path planning.
- **p. 3 / III. METHOD - extractive body cue:** Our neural network FΘ then maps x to a d-dimensional CLIP embedding: FΘ(x) = z ∈Rd, where z captures the language features observed in the ...
- **p. 3 / III. METHOD - extractive body cue:** We enforce this unit-length condition by ℓ2-normalising every CLIP feature and network output, so cosine similarity is a true metric and the embeddings reside on ...
- **p. 4 / III. METHOD - extractive body cue:** (2), the posterior over the network parameters θ is proportional to: p(θ / x, zobs) ∝p(zobs / FΘ(x)) p(κΘ(x)), (3) and we train the network ...
- **p. 4 / III. METHOD - extractive body cue:** Let us denote the network outputs as (µΘ(x), κΘ(x)) = FΘ(x).
- **p. 5 / III. METHOD - extractive body cue:** The top row displays large objects (volume ≥1 m3) such as statues and a red oak tree, while the bottom row shows smaller objects (volume ...
- **p. 3 / III. METHOD - extractive body cue:** The objective is to generate a two-stage path: first, a coarse path γc = (x0, . . . , xc) obtained by searching over the ...
- **p. 4 / III. METHOD - extractive body cue:** (4) This loss function trains the network to produce parameters (µΘ(x), κΘ(x)) that balance closeness to the observed embedding zobs with regularization from the Gamma ...

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** We summarize our main contributions of LAMP (Language Map) as follows: • We introduce LAMP, the first implicit language map leveraging a language-driven continuous field ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To address this gap, we propose an implicit language map representation that continuously models language vectors from RGB-only input, facilitating memoryefficient path planning that supports ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Building on the strengths of our implicit language map, we propose methods to construct and utilize this representation more effectively.

## Source Evidence Cues

- **p. 2 / III. METHOD - extractive body cue:** We introduce a map representation that continuously encodes language features within a large-scale space, ensuring memory efficiency and enabling fine-grained path planning.
- **p. 3 / III. METHOD - extractive body cue:** Our neural network FΘ then maps x to a d-dimensional CLIP embedding: FΘ(x) = z ∈Rd, where z captures the language features observed in the ...
- **p. 3 / III. METHOD - extractive body cue:** We enforce this unit-length condition by ℓ2-normalising every CLIP feature and network output, so cosine similarity is a true metric and the embeddings reside on ...
- **p. 4 / III. METHOD - extractive body cue:** (2), the posterior over the network parameters θ is proportional to: p(θ / x, zobs) ∝p(zobs / FΘ(x)) p(κΘ(x)), (3) and we train the network ...
- **p. 4 / III. METHOD - extractive body cue:** Let us denote the network outputs as (µΘ(x), κΘ(x)) = FΘ(x).
- **p. 5 / III. METHOD - extractive body cue:** The top row displays large objects (volume ≥1 m3) such as statues and a red oak tree, while the bottom row shows smaller objects (volume ...
- **Detected method headings:** III. METHOD (p. 2); 1) Comparison of Language Map Representation Methods (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | We introduce a map representation that continuously encodes language features within a large-scale space, ensuring memory efficiency and enabling fine-grained path planning. | p. 2 (III. METHOD), p. 3 (III. METHOD) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | Our neural network FΘ then maps x to a d-dimensional CLIP embedding: FΘ(x) = z ∈Rd, where z captures the language features ... | p. 3 (III. METHOD), p. 3 (III. METHOD) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | We enforce this unit-length condition by ℓ2-normalising every CLIP feature and network output, so cosine similarity is a true metric and the ... | p. 3 (III. METHOD), p. 4 (III. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / III. METHOD - extractive body cue:** (2), the posterior over the network parameters θ is proportional to: p(θ / x, zobs) ∝p(zobs / FΘ(x)) p(κΘ(x)), (3) and we train the network ...
- **p. 3 / III. METHOD - extractive body cue:** The objective is to generate a two-stage path: first, a coarse path γc = (x0, . . . , xc) obtained by searching over the ...
- **p. 4 / III. METHOD - extractive body cue:** (4) This loss function trains the network to produce parameters (µΘ(x), κΘ(x)) that balance closeness to the observed embedding zobs with regularization from the Gamma ...
- **p. 3 / III. METHOD - extractive body cue:** (c) Fine Path Generation: We then generate the pose using FΘ to maximize cosine similarity, moving from the coarse pose to a fine pose that ...
- **p. 5 / III. METHOD - extractive body cue:** The top row displays large objects (volume ≥1 m3) such as statues and a red oak tree, while the bottom row shows smaller objects (volume ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | address, implicit, language, representation, continuously, models, vectors, RGB-only, input, facilitating, memoryefficient, path, planning, supports | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | address, implicit, language, representation, continuously, models, vectors, RGB-only, input, facilitating | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | summarize, main, contributions, LAMP, Language, Map, follows, introduce, first, implicit | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | posterior, over, network, parameters, proportional, zobs, train, minimizing, negative, logposterior | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / I. INTRODUCTION - extractive body cue:** To address this gap, we propose an implicit language map representation that continuously models language vectors from RGB-only input, facilitating memoryefficient path planning that supports ...
- **p. 3 / III. METHOD - extractive body cue:** Our neural network FΘ then maps x to a d-dimensional CLIP embedding: FΘ(x) = z ∈Rd, where z captures the language features observed in the ...
- **p. 3 / III. METHOD - extractive body cue:** (a) Implicit Language Map Construction: The robot traverses the environment and collects pairs of camera poses x and corresponding images I.
- **p. 4 / III. METHOD - extractive body cue:** To implement this, we define our network FΘ to output the two parameters of the vMF distribution for a given pose x: the mean direction ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** 1, (a) the grid-based method leverages depth images and a Visual Language Model [5], [21] to integrate language information into a 3D representation, which is ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We summarize our main contributions of LAMP (Language Map) as follows: • We introduce LAMP, the first implicit language map leveraging a language-driven continuous field ...
- **p. 4 / III. METHOD - extractive body cue:** Let us denote the network outputs as (µΘ(x), κΘ(x)) = FΘ(x).
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | We introduce a map representation that continuously encodes language features within a large-scale space, ensuring memory efficiency and enabling fine-grained path planning. | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | To address this limitation, we introduce the first approach that implicitly represents space for memory efficiency and leverages this implicit map in ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | We introduce a map representation that continuously encodes language features within a large-scale space, ensuring memory efficiency and enabling fine-grained path planning. | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / III. METHOD - extractive body cue:** (2), the posterior over the network parameters θ is proportional to: p(θ / x, zobs) ∝p(zobs / FΘ(x)) p(κΘ(x)), (3) and we train the network ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** introduce, representation, continuously, encodes, language, features, within, large-scale, space, ensuring, memory, efficiency, enabling, fine-grained, path, planning, neural, network, then, maps.
- **Relevant PDF headings:** III. METHOD (p. 2); 1) Comparison of Language Map Representation Methods (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | In the following subsections, Section IV-A describes the dataset configuration and implementation details, Section IV-B presents the experimental results obtained in the ... | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Global / local decision | Fig. 1. Comparison of three language map representation methods. (a) The grid-based approach struggles to accurately represent objects at coarse resolutions and ... | p. 2 (Figure/Table caption), p. 5 (Figure/Table caption) |
| Motion execution / recovery | First, success rate is computed considering only the top 1% of the predictions; a trial is deemed successful if the robot ends ... | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3. Examples of objects used in our simulation navigation experiments. The top row displays large objects (volume ≥1 m3) such as statues and a ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1. Comparison of three language map representation methods. (a) The grid-based approach struggles to accurately represent objects at coarse resolutions and requires excessive memory ...
- **p. 6 / 1) Comparison of Language Map Representation Methods - extractive body cue:** In the Extinguisher scene, the node-based method fails because it does not directly observe the goal, whereas our method correctly identifies the target by leveraging ...
- **p. 5 / 1) Comparison of Language Map Representation Methods - extractive body cue:** Even with this increased memory usage, the grid-based approach captures large objects but fails to detect smaller ones.
- **p. 5 / 1) Comparison of Language Map Representation Methods - extractive body cue:** In contrast, the node-based method needs about 70 times more memory than our method to reach a similar success rate, yet its performance in the ...
- **p. 6 / 1) Comparison of Language Map Representation Methods - extractive body cue:** Finally, in the Boxes scene, the grid-based method is hindered by z-axis projection artifacts, while the node-based method detects the boxes but fails to plan ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD), objective p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 5 (III. METHOD), temporal p. 2 (III. METHOD), p. 2 (II. RELATED WORK), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
