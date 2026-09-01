# Method - ConceptFusion: Open-set Multimodal 3D Mapping

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2302.07241; PDF retrieval source: https://arxiv.org/pdf/2302.07241. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (IV. THE ConceptFusion APPROACH), p. 4 (IV. THE ConceptFusion APPROACH), p. 6 (IV. THE ConceptFusion APPROACH), p. 6 (IV. THE ConceptFusion APPROACH), p. 5 (IV. THE ConceptFusion APPROACH), p. 5 (IV. THE ConceptFusion APPROACH)): We then present our algorithm to compute pixel-aligned features zero-shot from off-the-shelf foundation models (such as CLIP [6], AudioCLIP [8], and variants).

## Method Body Digest

- **p. 4 / IV. THE ConceptFusion APPROACH - extractive body cue:** We then present our algorithm to compute pixel-aligned features zero-shot from off-the-shelf foundation models (such as CLIP [6], AudioCLIP [8], and variants).
- **p. 4 / IV. THE ConceptFusion APPROACH - extractive body cue:** To mitigate this, we introduce a novel mechanism to construct pixel-aligned features that combine global (image-level) context encapsulated in models like CLIP, with local (region-level) ...
- **p. 6 / IV. THE ConceptFusion APPROACH - extractive body cue:** Real-time inference: To optimize the performance and efficiency of the foundation models employed (SAM [57], DINO [7], and CLIP [6]), we use standard quantization and ...
- **p. 6 / IV. THE ConceptFusion APPROACH - extractive body cue:** For generating class-agnostic (generic) object masks, we use the Mask2Former [60] or the segment anything (SAM) [57] models for category-agnostic instance segmentation.
- **p. 5 / IV. THE ConceptFusion APPROACH - extractive body cue:** Building complex 3D spatial query modules Unique capabilities unlocked by fusing features into 3D space include the ability to reason about objects that were
- **p. 5 / IV. THE ConceptFusion APPROACH - extractive body cue:** Capturing long-tailed concepts: We find that our pixelaligned embeddings capture fine-grained and long-tailed concepts significantly better than approaches like LSeg [24] and OpenSeg [18], which ...
- **p. 3 / IV. THE ConceptFusion APPROACH - extractive body cue:** The open-set multimodal 3D mapping problem: Given a sequence of image (and depth) observations of an environment
- **p. 5 / IV. THE ConceptFusion APPROACH - extractive body cue:** The centroid of the point set returned by the query term refrigerator and television are shown as blue circles, and the estimated distance between them ...

## Design Rationale

- **p. 4 / IV. THE ConceptFusion APPROACH - extractive body cue:** To mitigate this, we introduce a novel mechanism to construct pixel-aligned features that combine global (image-level) context encapsulated in models like CLIP, with local (region-level) ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our key contributions are the following: • An approach to open-set multimodal 3D mapping that constructs map representations queryable by text, image, audio, and click ...
- **p. 4 / IV. THE ConceptFusion APPROACH - extractive body cue:** Given an input image X ∈R3×H×W , our method uses a foundation model F as a feature extractor to produce three types of embeddings, which ...

## Source Evidence Cues

- **p. 4 / IV. THE ConceptFusion APPROACH - extractive body cue:** We then present our algorithm to compute pixel-aligned features zero-shot from off-the-shelf foundation models (such as CLIP [6], AudioCLIP [8], and variants).
- **p. 4 / IV. THE ConceptFusion APPROACH - extractive body cue:** To mitigate this, we introduce a novel mechanism to construct pixel-aligned features that combine global (image-level) context encapsulated in models like CLIP, with local (region-level) ...
- **p. 6 / IV. THE ConceptFusion APPROACH - extractive body cue:** Real-time inference: To optimize the performance and efficiency of the foundation models employed (SAM [57], DINO [7], and CLIP [6]), we use standard quantization and ...
- **p. 6 / IV. THE ConceptFusion APPROACH - extractive body cue:** For generating class-agnostic (generic) object masks, we use the Mask2Former [60] or the segment anything (SAM) [57] models for category-agnostic instance segmentation.
- **p. 5 / IV. THE ConceptFusion APPROACH - extractive body cue:** Building complex 3D spatial query modules Unique capabilities unlocked by fusing features into 3D space include the ability to reason about objects that were
- **p. 5 / IV. THE ConceptFusion APPROACH - extractive body cue:** Capturing long-tailed concepts: We find that our pixelaligned embeddings capture fine-grained and long-tailed concepts significantly better than approaches like LSeg [24] and OpenSeg [18], which ...
- **p. 3 / IV. THE ConceptFusion APPROACH - extractive body cue:** The open-set multimodal 3D mapping problem: Given a sequence of image (and depth) observations of an environment
- **Detected method headings:** IV. THE ConceptFusion APPROACH (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | We then present our algorithm to compute pixel-aligned features zero-shot from off-the-shelf foundation models (such as CLIP [6], AudioCLIP [8], and variants). | p. 4 (IV. THE ConceptFusion APPROACH), p. 4 (IV. THE ConceptFusion APPROACH) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | To mitigate this, we introduce a novel mechanism to construct pixel-aligned features that combine global (image-level) context encapsulated in models like CLIP, ... | p. 4 (IV. THE ConceptFusion APPROACH), p. 6 (IV. THE ConceptFusion APPROACH) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | Real-time inference: To optimize the performance and efficiency of the foundation models employed (SAM [57], DINO [7], and CLIP [6]), we use ... | p. 6 (IV. THE ConceptFusion APPROACH), p. 6 (IV. THE ConceptFusion APPROACH) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / IV. THE ConceptFusion APPROACH - extractive body cue:** The centroid of the point set returned by the query term refrigerator and television are shown as blue circles, and the estimated distance between them ...
- **p. 6 / IV. THE ConceptFusion APPROACH - extractive body cue:** Our set of 3DSCs all take on the relation signature RELATION(QUERYa, QUERYb) and return a scalar or boolean value as appropriate.
- **p. 6 / IV. THE ConceptFusion APPROACH - extractive body cue:** Real-time inference: To optimize the performance and efficiency of the foundation models employed (SAM [57], DINO [7], and CLIP [6]), we use standard quantization and ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | open-set, multimodal, mapping, problem, Given, sequence, image, depth, observations, environment, IV-B, compute, semantic, context | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | open-set, multimodal, mapping, problem, Given, sequence, image, depth, observations, environment | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | mitigate, introduce, novel, mechanism, construct, pixel-aligned, features, combine, global, image-level | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | centroid, point, returned, query, term, refrigerator, television, blue, circles, estimated | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / IV. THE ConceptFusion APPROACH - extractive body cue:** The open-set multimodal 3D mapping problem: Given a sequence of image (and depth) observations of an environment
- **p. 4 / IV. THE ConceptFusion APPROACH - extractive body cue:** IV-B, we compute the semantic context embedding fP u,v,t ∈fP Xt for each pixel in the input image Xt.
- **p. 4 / IV. THE ConceptFusion APPROACH - extractive body cue:** Given an input image X ∈R3×H×W , our method uses a foundation model F as a feature extractor to produce three types of embeddings, which ...
- **p. 6 / IV. THE ConceptFusion APPROACH - extractive body cue:** The pixel-aligned feature extraction processes run offline (10-15 seconds / image) on an NVIDIA RTX 3090 GPU.
- **p. 2 / I. INTRODUCTION - extractive body cue:** This does not allow for the level of precise (pixel-level or objectlevel) reasoning robotic perception systems need across a wide range of concepts, particularly for ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We demonstrate that pixel-level foundation features may be fused into 3D maps by leveraging precisely the same surface fusion techniques as for fusing depth or ...
- **p. 5 / IV. THE ConceptFusion APPROACH - extractive body cue:** 3) Image query: qimage is computed as the image-level CLIP embedding of the query image.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | Our odometry and mapping approaches run at frame-rate (15 Hz). | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | On outdoor datasets (SemanticKITTI [68], self-captured autonomous driving sequences), we incrementally register pointclouds into a global frame using the LegoLOAM [70] technique ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | Our odometry and mapping approaches run at frame-rate (15 Hz). | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / IV. THE ConceptFusion APPROACH - extractive body cue:** Real-time inference: To optimize the performance and efficiency of the foundation models employed (SAM [57], DINO [7], and CLIP [6]), we use standard quantization and ...
- **p. 5 / IV. THE ConceptFusion APPROACH - extractive body cue:** Capturing long-tailed concepts: We find that our pixelaligned embeddings capture fine-grained and long-tailed concepts significantly better than approaches like LSeg [24] and OpenSeg [18], which ...
- **p. 8 / 4) What previously infeasible downstream use-cases can - extractive body cue:** Of the approaches presented here, LSeg requires per-pixel CLIP features as labels, OpenSeg leverages per-image captions for labels, and CLIPSeg trains a shallow decoder atop ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** then, present, algorithm, compute, pixel-aligned, features, zero-shot, off-the-shelf, foundation, models, CLIP, AudioCLIP, variants, mitigate, introduce, novel, mechanism, construct, combine, global.
- **Relevant PDF headings:** IV. THE ConceptFusion APPROACH (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | This real-world dataset comprises 3D scans of 78 commonly found household and office objects on a tabletop surface (see Fig. | p. 7 (4) What previously infeasible downstream use-cases can), p. 8 (4) What previously infeasible downstream use-cases can) |
| Global / local decision | Fig. 7: Text queries over ScanNet [61]: ConceptFusion is able to handle long-form text queries and accurately localize objects referenced by the ... | p. 7 (Figure/Table caption), p. 8 (4) What previously infeasible downstream use-cases can) |
| Motion execution / recovery | By applying both quantization and tracing techniques to our models, we are able to achieve significant improvements in their efficiency, without compromising ... | p. 6 (IV. THE ConceptFusion APPROACH), p. 10 (4) What previously infeasible downstream use-cases can) |

## Failure and Ablation Link

- **p. 10 / 4) What previously infeasible downstream use-cases can - extractive body cue:** The "Remove uniqueness term..." variant fuses features computed from individual masks with those computed over the entire image, but does not account for mask uniqueness ...
- **p. 6 / IV. THE ConceptFusion APPROACH - extractive body cue:** However, for all other results presented in this paperunless otherwise specified-the language queries are directly fed into the CLIP text encoder without any preprocessing.
- **p. 6 / IV. THE ConceptFusion APPROACH - extractive body cue:** By applying both quantization and tracing techniques to our models, we are able to achieve significant improvements in their efficiency, without compromising their accuracy.
- **p. 9 / 4) What previously infeasible downstream use-cases can - extractive body cue:** Ablation analyses Pixel-alignment design choices: We evaluate the design choices made in our pixel-alignment scheme on the Scan
- **p. 10 / VI. OUTLOOK - extractive body cue:** Ablation performed on the Replica [63] dataset.
- **p. 11 / VI. OUTLOOK - extractive body cue:** 11: The zero-shot nature of our approach allows integration with newer off-the-shelf foundation models without the need for finetuning.
- **p. 9 / 4) What previously infeasible downstream use-cases can - extractive body cue:** Other components of the autonomy stack include a shortest-path global planner, a Frenet [71] local planner for obstacle avoidance, and a Stanley-Controller [72] for trajectory ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (IV. THE ConceptFusion APPROACH), p. 4 (IV. THE ConceptFusion APPROACH), p. 6 (IV. THE ConceptFusion APPROACH), p. 6 (IV. THE ConceptFusion APPROACH), p. 5 (IV. THE ConceptFusion APPROACH), p. 5 (IV. THE ConceptFusion APPROACH), objective p. 5 (IV. THE ConceptFusion APPROACH), p. 6 (IV. THE ConceptFusion APPROACH), p. 6 (IV. THE ConceptFusion APPROACH), temporal p. 6 (IV. THE ConceptFusion APPROACH), p. 12 (VII. CONCLUSION), p. 12 (VII. CONCLUSION), p. 1 (Front matter), p. 3 (IV. THE ConceptFusion APPROACH), p. 3 (II. RELATED WORK).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
