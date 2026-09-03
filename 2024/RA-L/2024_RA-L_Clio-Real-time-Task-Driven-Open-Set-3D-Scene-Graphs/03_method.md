# Method - Clio: Real-time Task-Driven Open-Set 3D Scene Graphs

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2404.13696; PDF retrieval source: https://arxiv.org/pdf/2404.13696. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (IV. TASK-DRIVEN CLUSTERING), p. 2 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 5 (IV. TASK-DRIVEN CLUSTERING), p. 4 (IV. TASK-DRIVEN CLUSTERING), p. 3 (I. INTRODUCTION)): In this section, we first provide relevant background on the Agglomerative IB, then present an incremental version of the Agglomerative IB algorithm to support real-time mapping, and lastly tailor the ...

## Method Body Digest

- **p. 4 / IV. TASK-DRIVEN CLUSTERING - extractive body cue:** In this section, we first provide relevant background on the Agglomerative IB, then present an incremental version of the Agglomerative IB algorithm to support real-time ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** These approaches use a class-agnostic segmentation network [10] (SegmentAnything or SAM) to generate fine-grained segments of the image and then apply a foundation model [11] ...
- **p. 3 / I. INTRODUCTION - extractive body cue:** Our first contribution (Section III) is to state the task-driven 3D scene understanding problem, where the robot is given a list of tasks, specified in ...
- **p. 5 / IV. TASK-DRIVEN CLUSTERING - extractive body cue:** Our key observation is that if the graph of primitives in input to the algorithm has multiple connected components (e.g., 3D object segments in different ...
- **p. 4 / IV. TASK-DRIVEN CLUSTERING - extractive body cue:** Towards this goal, we propose an incremental version of the algorithm that can be executed online as the robot explores
- **p. 3 / I. INTRODUCTION - extractive body cue:** Then, as the robot operates, Clio creates a hierarchical map, namely a 3D scene graph, of the environment in real-time, where the representation only retains ...
- **p. 5 / IV. TASK-DRIVEN CLUSTERING - extractive body cue:** Each track is then reconstructed into a 3D object primitive based on all frames in the track and a final CLIP feature is computed via ...
- **p. 4 / IV. TASK-DRIVEN CLUSTERING - extractive body cue:** As suggested in [14], at each iteration k, we also compute δ(k) = I( ˜Xk; Y ) -I( ˜Xk-1; Y ) I(X; Y ) (3) ...

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** We propose Clio, a novel approach for building task-driven 3D scene graphs in real-time with embedded open-set semantics.
- **p. 2 / Abstract - extractive body cue:** Our final contribution is an extensive experimental campaign showing that Clio not only allows real-time construction of compact open-set 3D scene graphs, but also improves ...
- **p. 3 / I. INTRODUCTION - extractive body cue:** Our third contribution (Section V) is to include the proposed task-driven clustering algorithm into a real-time system, named Clio (Fig.

## Source Evidence Cues

- **p. 4 / IV. TASK-DRIVEN CLUSTERING - extractive body cue:** In this section, we first provide relevant background on the Agglomerative IB, then present an incremental version of the Agglomerative IB algorithm to support real-time ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** These approaches use a class-agnostic segmentation network [10] (SegmentAnything or SAM) to generate fine-grained segments of the image and then apply a foundation model [11] ...
- **p. 3 / I. INTRODUCTION - extractive body cue:** Our first contribution (Section III) is to state the task-driven 3D scene understanding problem, where the robot is given a list of tasks, specified in ...
- **p. 5 / IV. TASK-DRIVEN CLUSTERING - extractive body cue:** Our key observation is that if the graph of primitives in input to the algorithm has multiple connected components (e.g., 3D object segments in different ...
- **p. 4 / IV. TASK-DRIVEN CLUSTERING - extractive body cue:** Towards this goal, we propose an incremental version of the algorithm that can be executed online as the robot explores
- **p. 3 / I. INTRODUCTION - extractive body cue:** Then, as the robot operates, Clio creates a hierarchical map, namely a 3D scene graph, of the environment in real-time, where the representation only retains ...
- **p. 5 / IV. TASK-DRIVEN CLUSTERING - extractive body cue:** Each track is then reconstructed into a 3D object primitive based on all frames in the track and a final CLIP feature is computed via ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | In this section, we first provide relevant background on the Agglomerative IB, then present an incremental version of the Agglomerative IB algorithm ... | p. 4 (IV. TASK-DRIVEN CLUSTERING), p. 2 (I. INTRODUCTION) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | These approaches use a class-agnostic segmentation network [10] (SegmentAnything or SAM) to generate fine-grained segments of the image and then apply a ... | p. 2 (I. INTRODUCTION), p. 3 (I. INTRODUCTION) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | Our first contribution (Section III) is to state the task-driven 3D scene understanding problem, where the robot is given a list of ... | p. 3 (I. INTRODUCTION), p. 5 (IV. TASK-DRIVEN CLUSTERING) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / IV. TASK-DRIVEN CLUSTERING - extractive body cue:** As suggested in [14], at each iteration k, we also compute δ(k) = I( ˜Xk; Y ) -I( ˜Xk-1; Y ) I(X; Y ) (3) ...
- **p. 3 / I. INTRODUCTION - extractive body cue:** In particular, we show how to obtain the probability densities required by the algorithm in [14] using CLIP embeddings, and show that the resulting algorithm ...
- **p. 4 / IV. TASK-DRIVEN CLUSTERING - extractive body cue:** Intuitively, the weight dij is a measure of the dissimilarity of the probability distributions of the two clusters.
- **p. 5 / IV. TASK-DRIVEN CLUSTERING - extractive body cue:** Given this choice of conditional probability, the Agglomerative IB computes the clusters ˜X.
- **p. 5 / IV. TASK-DRIVEN CLUSTERING - extractive body cue:** The Agglomerative IB algorithm requires defining the conditional probability p(y/x), which can be understood as the task-relevance of each primitive.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 4 (IV. TASK-DRIVEN CLUSTERING), p. 5 (IV. TASK-DRIVEN CLUSTERING).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | observation, graph, primitives, input, algorithm, multiple, connected, components, object, segments, different, rooms, then, clustering | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | observation, graph, primitives, input, algorithm, multiple, connected, components, object, segments | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | Clio, novel, building, task-driven, scene, graphs, real-time, embedded, open-set, semantics | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | suggested, iteration, compute, Xk-1, measure, fractional, loss, information, corresponding, merge | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / IV. TASK-DRIVEN CLUSTERING - extractive body cue:** Our key observation is that if the graph of primitives in input to the algorithm has multiple connected components (e.g., 3D object segments in different ...
- **p. 3 / I. INTRODUCTION - extractive body cue:** Our first contribution (Section III) is to state the task-driven 3D scene understanding problem, where the robot is given a list of tasks, specified in ...
- **p. 5 / IV. TASK-DRIVEN CLUSTERING - extractive body cue:** To obtain semantic features for the places, we compute a CLIP embedding vector for each input image provided to Clio.
- **p. 2 / Abstract - extractive body cue:** The first contribution of this paper is to propose a task-driven 3D scene understanding problem, where the robot is given a list of tasks in ...
- **p. 4 / IV. TASK-DRIVEN CLUSTERING - extractive body cue:** As suggested in [14], at each iteration k, we also compute δ(k) = I( ˜Xk; Y ) -I( ˜Xk-1; Y ) I(X; Y ) (3) ...
- **p. 3 / I. INTRODUCTION - extractive body cue:** We show that Spot is able to execute grasping commands, expressed in natural language, using Clio's task-driven 3D scene graph.
- **p. 4 / IV. TASK-DRIVEN CLUSTERING - extractive body cue:** Towards this goal, we propose an incremental version of the algorithm that can be executed online as the robot explores
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | Their performance difference is due to the fact that Clio-online is executed in real-time and might drop frames as required to keep ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | We include results for both Clio-batch, which takes in all primitives of a scene and is executed only once at the end ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | We use CLIP model ViT-L/14 and generate results with an RTX 3090 GPU and Intel i9-12900K CPU. | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / IV. TASK-DRIVEN CLUSTERING - extractive body cue:** Towards this goal, we propose an incremental version of the algorithm that can be executed online as the robot explores
- **p. 2 / Abstract - extractive body cue:** The third contribution is to integrate our task-driven clustering algorithm into a real-time pipeline, named Clio, that constructs a hierarchical 3D scene graph of the ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** section, first, provide, relevant, background, Agglomerative, then, present, incremental, version, algorithm, support, real-time, mapping, lastly, tailor, formulation, open-set, vision-language, features.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | During the experiments, the robot constructs a map with Clio in real-time while exploring a scene, and then is tasked to navigate ... | p. 8 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS) |
| Global / local decision | In particular, in some cases Clio retains an order of magnitude less objects compared to taskagnostic baselines (cf. with the number of ... | p. 6 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS) |
| Motion execution / recovery | Overall, we achieve a 57% success rate for the grasps and a 71% success rate if we disregard the cases where Spot ... | p. 8 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 6 / VI. EXPERIMENTS - extractive body cue:** In particular, in some cases Clio retains an order of magnitude less objects compared to taskagnostic baselines (cf. with the number of objects in ClioPrim, ...
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** To show the importance of being task-driven, we further include task-aware versions of the baselines: Khronos-task and ConceptGraphs-task that take the results of Khronos and ...
- **p. 8 / VII. LIMITATIONS - extractive body cue:** Despite the encouraging experimental results, our approach has multiple limitations.
- **p. 8 / VII. LIMITATIONS - extractive body cue:** First, while our method is zero-shot and is not bound to any particular foundation model, it does inherit some limitations from the foundation models used ...
- **p. 7 / VI. EXPERIMENTS - extractive body cue:** Closed-Set Object Evaluation While Clio is designed for open-set detection, we include results on the closed-set Replica [17] dataset using the evaluation method performed by ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (IV. TASK-DRIVEN CLUSTERING), p. 2 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 5 (IV. TASK-DRIVEN CLUSTERING), p. 4 (IV. TASK-DRIVEN CLUSTERING), p. 3 (I. INTRODUCTION), objective p. 4 (IV. TASK-DRIVEN CLUSTERING), p. 3 (I. INTRODUCTION), p. 4 (IV. TASK-DRIVEN CLUSTERING), p. 5 (IV. TASK-DRIVEN CLUSTERING), p. 5 (IV. TASK-DRIVEN CLUSTERING), temporal p. 7 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 8 (VI. EXPERIMENTS), p. 2 (Abstract), p. 6 (VI. EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** As suggested in [14], at each iteration k, we also compute δ(k) = I( ˜Xk; Y ) -I( ˜Xk-1; Y ) I(X; Y ) (3) as a measure of the ... (p. 4, IV. TASK-DRIVEN CLUSTERING).
- **Objective/update evidence:** As suggested in [14], at each iteration k, we also compute δ(k) = I( ˜Xk; Y ) -I( ˜Xk-1; Y ) I(X; Y ) (3) as a measure of the ... (p. 4, IV. TASK-DRIVEN CLUSTERING).
- **Temporal/runtime evidence:** Their performance difference is due to the fact that Clio-online is executed in real-time and might drop frames as required to keep up with the image stream. (p. 7, VI. EXPERIMENTS).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
