# Method - Search3D: Hierarchical Open-Vocabulary 3D Segmentation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2409.18431; PDF retrieval source: https://arxiv.org/pdf/2409.18431. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 4 (2) Computing open-vocabulary features for the scene repre), p. 1 (Abstract), p. 4 (2) Computing open-vocabulary features for the scene repre)): ACCEPTED JANUARY, 2025 Object-centric open-vocabulary 3D segmentation methods typically first extract a set of class-agnostic 3D object instance masks and then compute a feature representation per object, represented in the ...

## Method Body Digest

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** ACCEPTED JANUARY, 2025 Object-centric open-vocabulary 3D segmentation methods typically first extract a set of class-agnostic 3D object instance masks and then compute a feature representation ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** To summarize our key contributions: • We propose a hierarchical open-vocabulary 3D segmentation method capable of segmenting both entire objects and their parts given arbitrary ...
- **p. 3 / III. METHOD - extractive PDF cue:** We introduce a novel hierarchical 3D scene representation enabling open-vocabulary segmentation for scene entities at multiple granularities, including objects and their parts.
- **p. 4 / 2) Computing open-vocabulary features for the scene repre - extractive PDF cue:** These 2D segment crops are then passed through the SigLIP [32] image encoder, producing feature vectors of dimension D for each segment.
- **p. 1 / Abstract - extractive PDF cue:** In this work, we introduce Search3D, an approach to construct hierarchical open-vocabulary 3D scene representations, enabling 3D search at multiple levels of granularity: fine-grained object ...
- **p. 4 / 2) Computing open-vocabulary features for the scene repre - extractive PDF cue:** To address this challenge, we propose a method to extract pixel-aligned features capable of representing finer-grained scene entities.
- **p. 3 / 2) Computing open-vocabulary features for the scene repre - extractive PDF cue:** These masks represent the object nodes at the first level of our hierarchical scene representation.
- **p. 4 / 2) Computing open-vocabulary features for the scene repre - extractive PDF cue:** For each 3D segment, neighboring segments within the same object that exhibit similar features are identified and merged based on two constraints: 1) Proximity: The ...

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** To summarize our key contributions: • We propose a hierarchical open-vocabulary 3D segmentation method capable of segmenting both entire objects and their parts given arbitrary ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** To evaluate our method, we introduce a novel evaluation suite for open-vocabulary scene-scale 3D part segmentation based on MultiScan [16].
- **p. 3 / III. METHOD - extractive PDF cue:** We introduce a novel hierarchical 3D scene representation enabling open-vocabulary segmentation for scene entities at multiple granularities, including objects and their parts.

## Source Evidence Cues

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** ACCEPTED JANUARY, 2025 Object-centric open-vocabulary 3D segmentation methods typically first extract a set of class-agnostic 3D object instance masks and then compute a feature representation ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** To summarize our key contributions: • We propose a hierarchical open-vocabulary 3D segmentation method capable of segmenting both entire objects and their parts given arbitrary ...
- **p. 3 / III. METHOD - extractive PDF cue:** We introduce a novel hierarchical 3D scene representation enabling open-vocabulary segmentation for scene entities at multiple granularities, including objects and their parts.
- **p. 4 / 2) Computing open-vocabulary features for the scene repre - extractive PDF cue:** These 2D segment crops are then passed through the SigLIP [32] image encoder, producing feature vectors of dimension D for each segment.
- **p. 1 / Abstract - extractive PDF cue:** In this work, we introduce Search3D, an approach to construct hierarchical open-vocabulary 3D scene representations, enabling 3D search at multiple levels of granularity: fine-grained object ...
- **p. 4 / 2) Computing open-vocabulary features for the scene repre - extractive PDF cue:** To address this challenge, we propose a method to extract pixel-aligned features capable of representing finer-grained scene entities.
- **p. 3 / 2) Computing open-vocabulary features for the scene repre - extractive PDF cue:** These masks represent the object nodes at the first level of our hierarchical scene representation.
- **Detected method headings:** III. METHOD (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | ACCEPTED JANUARY, 2025 Object-centric open-vocabulary 3D segmentation methods typically first extract a set of class-agnostic 3D object instance masks and then compute ... | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | To summarize our key contributions: • We propose a hierarchical open-vocabulary 3D segmentation method capable of segmenting both entire objects and their ... | p. 2 (I. INTRODUCTION), p. 3 (III. METHOD) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | We introduce a novel hierarchical 3D scene representation enabling open-vocabulary segmentation for scene entities at multiple granularities, including objects and their parts. | p. 3 (III. METHOD), p. 4 (2) Computing open-vocabulary features for the scene repre) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 2) Computing open-vocabulary features for the scene repre - extractive PDF cue:** For each 3D segment, neighboring segments within the same object that exhibit similar features are identified and merged based on two constraints: 1) Proximity: The ...
- **p. 4 / 2) Computing open-vocabulary features for the scene repre - extractive PDF cue:** This refinement updates the 3D segments in the hierarchical scene representation, reflecting the semantic merging.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (2) Computing open-vocabulary features for the scene repre), p. 1 (I. INTRODUCTION), p. 4 (2) Computing open-vocabulary features for the scene repre).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | representation, built, upon, scenes, reconstructed, posed, RGB-D, image, sequences, Fig, enables, searching, across, objects | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | representation, built, upon, scenes, reconstructed, posed, RGB-D, image, sequences, Fig | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summarize, contributions, hierarchical, open-vocabulary, segmentation, capable, segmenting, entire, objects, parts | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | segment, neighboring, segments, within, same, object, exhibit, similar, features, identified | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. METHOD - extractive PDF cue:** This representation is built upon 3D scenes reconstructed using posed RGB-D image sequences, as shown in Fig.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** This enables searching across objects, parts, and attributes matching any given user query (right). critical to scene interaction.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Ultimately, systems designed for such real-world interactions must be able to identify scene entities based on flexible and user-defined descriptions.
- **p. 3 / 2) Computing open-vocabulary features for the scene repre - extractive PDF cue:** Given the 3D scene Pscene ∈RN×3 where N is the number of points, it outputs M binary instance masks M = Fobj(Pscene) = {m3D 1 ...
- **p. 4 / 2) Computing open-vocabulary features for the scene repre - extractive PDF cue:** Given an input query such as "seat of a chair", we first encode the query using the SigLIP text encoder to obtain an embedding vector ...
- **p. 4 / 2) Computing open-vocabulary features for the scene repre - extractive PDF cue:** Object-features 4 are extracted using a method inspired by [7] and [8], leveraging class-agnostic object masks to identify optimal views for semantic feature extraction.
- **p. 5 / IV. DATA - extractive PDF cue:** Using the SceneFun3D annotation tool [5], we performed fine-grained semantic annotation on high-resolution point clouds, and extended it to incorporate object-part hierarchy information.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | The rightmost column shows whether there is a direct proportionality relationship between the total time per scene, vs. other parameters such as ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | This representation is built upon 3D scenes reconstructed using posed RGB-D image sequences, as shown in Fig. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Once this representation is built, inference 6⃝, i.e., 3D search based on user input queries can be performed at around 1-2 FPS. | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** ACCEPTED, JANUARY, Object-centric, open-vocabulary, segmentation, methods, typically, first, extract, class-agnostic, object, instance, masks, then, compute, feature, representation, represented, joint, vision-language.
- **Relevant PDF headings:** III. METHOD (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | 3D Material Segmentation Next, we perform an analysis on 3D material segmentation task using the object-level material annotations from the 3RScan dataset ... | p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |
| Semantic / temporal fusion | First, we evaluate the quality of our segment features for identifying object parts using an oracle mask experiment, isolating feature quality from ... | p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Robot query / planning handoff | It demonstrates the strong open-vocabulary part-segmentation performance of our segment-level features, with at least + 13.8 AP improvement over baseline methods. | p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 6 / V. EXPERIMENTS - extractive PDF cue:** Aggr. search AP AP50 AP25 (1) Ours ✓ 4.7 8.2 17.6 (2) Ours ✓ ✓ 6.6 11.4 23.7 (3) Ours ✓ ✓ ✓(max.) 7.5 13.5 ...
- **p. 5 / V. EXPERIMENTS - extractive PDF cue:** First, we evaluate the quality of our segment features for identifying object parts using an oracle mask experiment, isolating feature quality from the effect of ...
- **p. 5 / V. EXPERIMENTS - extractive PDF cue:** Additionally, we validate our design choices through corresponding ablation studies.
- **p. 6 / V. EXPERIMENTS - extractive PDF cue:** IV emphasize the importance of those components.
- **p. 7 / V. EXPERIMENTS - extractive PDF cue:** Nevertheless, there are limitations to the geometrical segmentation method we employ for part segmentation, as it relies on surface normals.
- **p. 7 / V. EXPERIMENTS - extractive PDF cue:** Discussion and Limitations One limitation of our work is the reliance on a simple geometrical over-segmentation method for identifying object parts.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 4 (2) Computing open-vocabulary features for the scene repre), p. 1 (Abstract), p. 4 (2) Computing open-vocabulary features for the scene repre), objective p. 4 (2) Computing open-vocabulary features for the scene repre), p. 4 (2) Computing open-vocabulary features for the scene repre), temporal p. 7 (V. EXPERIMENTS), p. 3 (III. METHOD), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 4 (2) Computing open-vocabulary features for the scene repre), p. 4 (2) Computing open-vocabulary features for the scene repre).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
