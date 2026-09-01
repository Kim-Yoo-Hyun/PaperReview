# Method - CLIP-Fields: Weakly Supervised Semantic Fields for Robotic Memory

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2210.05663; PDF retrieval source: https://arxiv.org/pdf/2210.05663. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (IV. APPROACH), p. 5 (IV. APPROACH), p. 4 (IV. APPROACH), p. 5 (IV. APPROACH), p. 3 (IV. APPROACH), p. 3 (IV. APPROACH)): We use a Multi-resolution Hash Encoder [20] to learn a low level spatial representation mapping R3 →Rd, which is then mapped to higher dimensions and trained with contrastive objectives.

## Method Body Digest

- **p. 4 / IV. APPROACH - extractive PDF cue:** We use a Multi-resolution Hash Encoder [20] to learn a low level spatial representation mapping R3 →Rd, which is then mapped to higher dimensions and ...
- **p. 5 / IV. APPROACH - extractive PDF cue:** semantic label, f = heads ◦g is the associated semantic encoding function, F is a pre-trained semantic language encoder, c is the confidence associated with ...
- **p. 4 / IV. APPROACH - extractive PDF cue:** We use the following training objectives: Semantic Label Embedding: This objective trains the function encoding the semantic information of a 3D point as a n-dimensional ...
- **p. 5 / IV. APPROACH - extractive PDF cue:** In this paper's experiments, we use the CLIP ViT-B/32 model embeddings, giving the visual features 512 dimensions.
- **p. 3 / IV. APPROACH - extractive PDF cue:** When no human annotations are available, we use web-image trained object detection models on our RGB images.
- **p. 3 / IV. APPROACH - extractive PDF cue:** To train our model, we first preprocess this set of RGB-D frames into a scene dataset (Fig.
- **p. 4 / IV. APPROACH - extractive PDF cue:** While training the contrastive loss objective, we also take into consideration the associated label weights.
- **p. 5 / IV. APPROACH - extractive PDF cue:** Similar to the previous objective, given CLIP visual embedding Cs associated with the points, the mapping h = headv◦g, the distance between camera and the ...

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** As a solution, we propose CLIP-Fields, which builds an implicit spatial semantic memory using webscale pretrained models as weak supervision.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** In this work, we introduce a method for building weakly supervised semantic neural fields, called CLIP-Fields, which combines the advantages of both of these lines ...

## Source Evidence Cues

- **p. 4 / IV. APPROACH - extractive PDF cue:** We use a Multi-resolution Hash Encoder [20] to learn a low level spatial representation mapping R3 →Rd, which is then mapped to higher dimensions and ...
- **p. 5 / IV. APPROACH - extractive PDF cue:** semantic label, f = heads ◦g is the associated semantic encoding function, F is a pre-trained semantic language encoder, c is the confidence associated with ...
- **p. 4 / IV. APPROACH - extractive PDF cue:** We use the following training objectives: Semantic Label Embedding: This objective trains the function encoding the semantic information of a 3D point as a n-dimensional ...
- **p. 5 / IV. APPROACH - extractive PDF cue:** In this paper's experiments, we use the CLIP ViT-B/32 model embeddings, giving the visual features 512 dimensions.
- **p. 3 / IV. APPROACH - extractive PDF cue:** When no human annotations are available, we use web-image trained object detection models on our RGB images.
- **p. 3 / IV. APPROACH - extractive PDF cue:** To train our model, we first preprocess this set of RGB-D frames into a scene dataset (Fig.
- **Detected method headings:** IV. APPROACH (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | We use a Multi-resolution Hash Encoder [20] to learn a low level spatial representation mapping R3 →Rd, which is then mapped to ... | p. 4 (IV. APPROACH), p. 5 (IV. APPROACH) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | semantic label, f = heads ◦g is the associated semantic encoding function, F is a pre-trained semantic language encoder, c is the ... | p. 5 (IV. APPROACH), p. 4 (IV. APPROACH) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | We use the following training objectives: Semantic Label Embedding: This objective trains the function encoding the semantic information of a 3D point ... | p. 4 (IV. APPROACH), p. 5 (IV. APPROACH) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / IV. APPROACH - extractive PDF cue:** While training the contrastive loss objective, we also take into consideration the associated label weights.
- **p. 5 / IV. APPROACH - extractive PDF cue:** Similar to the previous objective, given CLIP visual embedding Cs associated with the points, the mapping h = headv◦g, the distance between camera and the ...
- **p. 5 / IV. APPROACH - extractive PDF cue:** semantic label, f = heads ◦g is the associated semantic encoding function, F is a pre-trained semantic language encoder, c is the confidence associated with ...
- **p. 3 / IV. APPROACH - extractive PDF cue:** Segment a scene image by doing so for each pixel. • Object navigation: For a given semantic query qs (or a visual query qv) find ...
- **p. 4 / IV. APPROACH - extractive PDF cue:** CLIP-Fields are trained on a specific scene with a contrastive loss, similar to CLIP [22].
- **p. 3 / IV. APPROACH - extractive PDF cue:** Use the alignment between a label embedding and f(Pi) to find the label with the highest probability for that pixel.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 4 (IV. APPROACH), p. 5 (IV. APPROACH), p. 5 (IV. APPROACH), p. 4 (IV. APPROACH).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Concurrently, web-scale, weakly-supervised, vision-language, models, like, CLIP, have, ability, capture, powerful, semantic, abstractions, individual | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Concurrently, web-scale, weakly-supervised, vision-language, models, like, CLIP, have, ability, capture | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | solution, CLIP-Fields, builds, implicit, spatial, semantic, memory, webscale, pretrained, models | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | While, training, contrastive, loss, objective, take, consideration, associated, label, weights | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Concurrently, web-scale weakly-supervised vision-language models like CLIP [22] have shown that the ability to capture powerful semantic abstractions from individual 2D images.
- **p. 3 / IV. APPROACH - extractive PDF cue:** For ease of decoding, we constrain the output spaces of f, h to match the embedding space of pre-trained language and vision-language models, respectively.
- **p. 4 / IV. APPROACH - extractive PDF cue:** The objective-specific heads are simple two-layer MLPs with ReLU nonlinearities that map the 144 dimensional outputs of g into higher dimensions which depend on the ...
- **p. 4 / IV. APPROACH - extractive PDF cue:** These include heads that outputs a vector that matches a natural language description of what is at the point in space, and headv that matches ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Their applications have been limited, however, by the fact that these trained representations assume a single 2D image as input; it is an open question ...
- **p. 3 / IV. APPROACH - extractive PDF cue:** Problem Statement We aim to build a system that can connect points of a 3D scene with their visual and semantic meaning.
- **p. 2 / III. BACKGROUND - extractive PDF cue:** In this section, we provide descriptions of the recent advances in machine learning that makes CLIP-Fields possible. a) Contrastive Image-Language Pretraining: This pretraining method, colloquially ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | One notable consequence is that our approach integrates semantic information from multiple views into the spatial memory; for example in Figure 6 ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | Then, we show that, only using weak web-model supervision, CLIPFields can be used as a robot's spatial memory with semantic information. | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | One notable consequence is that our approach integrates semantic information from multiple views into the spatial memory; for example in Figure 6 ... | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / IV. APPROACH - extractive PDF cue:** We use a Multi-resolution Hash Encoder [20] to learn a low level spatial representation mapping R3 →Rd, which is then mapped to higher dimensions and ...
- **p. 5 / IV. APPROACH - extractive PDF cue:** semantic label, f = heads ◦g is the associated semantic encoding function, F is a pre-trained semantic language encoder, c is the confidence associated with ...
- **p. 4 / IV. APPROACH - extractive PDF cue:** We use the following training objectives: Semantic Label Embedding: This objective trains the function encoding the semantic information of a 3D point as a n-dimensional ...
- **p. 3 / IV. APPROACH - extractive PDF cue:** When no human annotations are available, we use web-image trained object detection models on our RGB images.
- **p. 3 / IV. APPROACH - extractive PDF cue:** To train our model, we first preprocess this set of RGB-D frames into a scene dataset (Fig.
- **p. 4 / IV. APPROACH - extractive PDF cue:** We use a Multi-resolution Hash Encoder [20] to learn a low level spatial representation mapping R3 →Rd, which is then mapped to higher dimensions and ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Multi-resolution, Hash, Encoder, learn, level, spatial, representation, mapping, then, mapped, higher, dimensions, trained, contrastive, objectives, semantic, label, heads, associated, encoding.
- **Relevant PDF headings:** IV. APPROACH (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Our visual segmentation experiments are performed on a subset of Habitat-Matterport 3D Semantic (HM3D semantics) [35] dataset, while our robot experiments were ... | p. 5 (V. EXPERIMENTAL EVALUATION), p. 7 (V. EXPERIMENTAL EVALUATION) |
| Global / local decision | In Figure 5, we see once again that CLIP-Fields outperforms the RGB-based models significantly, to the point where even with three labelled ... | p. 6 (V. EXPERIMENTAL EVALUATION), p. 5 (V. EXPERIMENTAL EVALUATION) |
| Motion execution / recovery | In Figure 5, we see once again that CLIP-Fields outperforms the RGB-based models significantly, to the point where even with three labelled ... | p. 6 (V. EXPERIMENTAL EVALUATION), p. 7 (V. EXPERIMENTAL EVALUATION) |

## Failure and Ablation Link

- **p. 5 / V. EXPERIMENTAL EVALUATION - extractive PDF cue:** We fine-tune the final layers of these pretrained models on each of our limited datasets, and then evaluate them on the held-out set.
- **p. 6 / V. EXPERIMENTAL EVALUATION - extractive PDF cue:** On this setting, we train CLIP-Fields with the provided instance segmented RGB-D images and the associated odometry data, and compare with the baseline pretrained 2D ...
- **p. 5 / V. EXPERIMENTAL EVALUATION - extractive PDF cue:** Detic is absent from the first two evaluations since it is a detection model and thus cannot be fine-tuned on segmentation labels.
- **p. 7 / V. EXPERIMENTAL EVALUATION - extractive PDF cue:** Semantic Navigation on Robot with CLIP-Fields as Semantic-Spatial Memory Training a CLIP-Fields with available data, whether they are labeled by humans or pretrained models, gives ...
- **p. 8 / VI. CONCLUSIONS AND FUTURE WORK - extractive PDF cue:** In future work, we hope to explore models that share parameters across scenes, and can handle dynamic scenes and objects.
- **p. 5 / V. EXPERIMENTAL EVALUATION - extractive PDF cue:** Detic is absent from the first two evaluations since it is a detection model and thus cannot be fine-tuned on segmentation labels.
- **p. 8 / V. EXPERIMENTAL EVALUATION - extractive PDF cue:** However, if an object was misidentified during data preparation, CLIP-Fields fails to correctly identify it as well.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (IV. APPROACH), p. 5 (IV. APPROACH), p. 4 (IV. APPROACH), p. 5 (IV. APPROACH), p. 3 (IV. APPROACH), p. 3 (IV. APPROACH), objective p. 4 (IV. APPROACH), p. 5 (IV. APPROACH), p. 5 (IV. APPROACH), p. 3 (IV. APPROACH), p. 4 (IV. APPROACH), p. 3 (IV. APPROACH), temporal p. 2 (II. RELATED WORK), p. 5 (V. EXPERIMENTAL EVALUATION), p. 5 (V. EXPERIMENTAL EVALUATION), p. 6 (V. EXPERIMENTAL EVALUATION), p. 7 (V. EXPERIMENTAL EVALUATION), p. 7 (V. EXPERIMENTAL EVALUATION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
