# Method - VGGT: Visual Geometry Grounded Transformer

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2503.11651; PDF retrieval source: https://arxiv.org/pdf/2503.11651. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3.3. Prediction heads), p. 3 (3.1. Problem definition and notation), p. 3 (3.1. Problem definition and notation), p. 10 (Method), p. 6 (3.4. Training), p. 5 (3.3. Prediction heads)): In order to implement the tracking module T , we use the CoTracker2 architecture [57], which takes the dense tracking features Ti as input.

## Method Body Digest

- **p. 5 / 3.3. Prediction heads - extractive body cue:** In order to implement the tracking module T , we use the CoTracker2 architecture [57], which takes the dense tracking features Ti as input.
- **p. 3 / 3.1. Problem definition and notation - extractive body cue:** The network architecture is designed to be permutation equivariant for all but the first frame.
- **p. 3 / 3.1. Problem definition and notation - extractive body cue:** It ingests the query point yq and the dense tracking features Ti output by the transformer f and then computes the track.
- **p. 10 / Method - extractive body cue:** Our backbone predicts the tracking features Ti, which replace the outputs of the feature extractor and later enter the rest of the CoTracker2 architecture, that ...
- **p. 6 / 3.4. Training - extractive body cue:** The model consists of approximately 1.2 billion parameters in total.
- **p. 5 / 3.3. Prediction heads - extractive body cue:** 3.4, the uncertainty maps are used in the loss and, after training, are proportional to the model's confidence in the predictions.
- **p. 6 / 3.4. Training - extractive body cue:** We train the model by optimizing the training loss (2) with the AdamW optimizer for 160K iterations.
- **p. 6 / 3.4. Training - extractive body cue:** Additionally, following CoTracker2 [57], we apply a visibility loss (binary cross-entropy) to estimate whether a point is visible in a given frame.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** To summarize, we make the following contributions: (1) We introduce VGGT, a large feed-forward transformer that, given one, a few, or even hundreds of images ...
- **p. 3 / 3. Method - extractive body cue:** We introduce VGGT, a large transformer that ingests a set of images as input and produces a variety of 3D quantities as output.
- **p. 4 / 3.1. Problem definition and notation - extractive body cue:** In the second row, our method correctly recovers a 3D scene from two images with no overlap, while DUSt3R fails.

## Source Evidence Cues

- **p. 5 / 3.3. Prediction heads - extractive body cue:** In order to implement the tracking module T , we use the CoTracker2 architecture [57], which takes the dense tracking features Ti as input.
- **p. 3 / 3.1. Problem definition and notation - extractive body cue:** The network architecture is designed to be permutation equivariant for all but the first frame.
- **p. 3 / 3.1. Problem definition and notation - extractive body cue:** It ingests the query point yq and the dense tracking features Ti output by the transformer f and then computes the track.
- **p. 10 / Method - extractive body cue:** Our backbone predicts the tracking features Ti, which replace the outputs of the feature extractor and later enter the rest of the CoTracker2 architecture, that ...
- **p. 6 / 3.4. Training - extractive body cue:** The model consists of approximately 1.2 billion parameters in total.
- **p. 5 / 3.3. Prediction heads - extractive body cue:** 3.4, the uncertainty maps are used in the loss and, after training, are proportional to the model's confidence in the predictions.
- **p. 6 / 3.4. Training - extractive body cue:** We train the model by optimizing the training loss (2) with the AdamW optimizer for 160K iterations.
- **Detected method headings:** 3. Method (p. 3); Method (p. 10)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | In order to implement the tracking module T , we use the CoTracker2 architecture [57], which takes the dense tracking features Ti ... | p. 5 (3.3. Prediction heads), p. 3 (3.1. Problem definition and notation) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | The network architecture is designed to be permutation equivariant for all but the first frame. | p. 3 (3.1. Problem definition and notation), p. 3 (3.1. Problem definition and notation) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | It ingests the query point yq and the dense tracking features Ti output by the transformer f and then computes the track. | p. 3 (3.1. Problem definition and notation), p. 10 (Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 3.4. Training - extractive body cue:** We train the model by optimizing the training loss (2) with the AdamW optimizer for 160K iterations.
- **p. 6 / 3.4. Training - extractive body cue:** Additionally, following CoTracker2 [57], we apply a visibility loss (binary cross-entropy) to estimate whether a point is visible in a given frame.
- **p. 5 / 3.3. Prediction heads - extractive body cue:** 3.4, the uncertainty maps are used in the loss and, after training, are proportional to the model's confidence in the predictions.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3.3. Prediction heads), p. 6 (3.4. Training), p. 6 (3.4. Training).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | introduce, VGGT, large, transformer, ingests, images, input, produces, variety, quantities, output, Additionally, DPT, head | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | introduce, VGGT, large, transformer, ingests, images, input, produces, variety, quantities | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summarize, make, following, contributions, introduce, VGGT, large, feed-forward, transformer, given | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | train, model, optimizing, training, loss, AdamW, optimizer, iterations, Additionally, following | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3. Method - extractive body cue:** We introduce VGGT, a large transformer that ingests a set of images as input and produces a variety of 3D quantities as output.
- **p. 5 / 3.3. Prediction heads - extractive body cue:** Additionally, the DPT head also outputs dense features Ti ∈RC×H×W , which serve as input to the tracking head.
- **p. 5 / 3.3. Prediction heads - extractive body cue:** The output image tokens ˆtI i are used to predict the dense outputs, i.e., the depth maps Di, point maps Pi, and tracking features Ti.
- **p. 6 / 3.3. Prediction heads - extractive body cue:** Note that, similar to VGGSfM [125], our tracker does not assume any temporal ordering of the input frames and, hence, can be applied to any ...
- **p. 3 / 3.1. Problem definition and notation - extractive body cue:** The input is a sequence (Ii)N i=1 of N RGB images Ii ∈ R3×H×W , observing the same 3D scene.
- **p. 4 / 3.2. Feature Backbone - extractive body cue:** To this end, each input image I is initially patchified into a set of K tokens1 tI ∈RK×C through DINO [78].
- **p. 4 / 3.3. Prediction heads - extractive body cue:** First, for each input image Ii, we augment the corresponding image tokens tI i with an additional camera token tg i ∈R1×C′ and four register ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | The order of the images in the input sequence is arbitrary, except that the first image is chosen as the reference frame. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | VGGT's transformer is a function that maps this sequence to a corresponding set of 3D annotations, one per frame: f  (Ii)N i=1 ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | We do not include examples with more than 32 frames, as DUSt3R runs out of memory beyond this limit. | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | We do not include examples with more than 32 frames, as DUSt3R runs out of memory beyond this limit. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.3. Prediction heads - extractive body cue:** 3.4, the uncertainty maps are used in the loss and, after training, are proportional to the model's confidence in the predictions.
- **p. 6 / 3.4. Training - extractive body cue:** We train the model by optimizing the training loss (2) with the AdamW optimizer for 160K iterations.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** order, implement, tracking, module, CoTracker2, architecture, takes, dense, features, input, network, designed, permutation, equivariant, first, frame, ingests, query, point, output.
- **Relevant PDF headings:** 3. Method (p. 3); Method (p. 10).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | It represents a specific case of rigid point tracking, which is restricted to only two views, and hence a suitable evaluation benchmark ... | p. 8 (4.4. Image Matching), p. 6 (4.1. Camera Pose Estimation) |
| Semantic / temporal fusion | Although our tracking head is not specialized for the twoview setting, it outperforms the state-of-the-art two-view matching method Roma. | p. 7 (4.1. Camera Pose Estimation), p. 9 (4.5. Ablation Studies) |
| Robot query / planning handoff | Table 10. Camera Pose Estimation on IMC [54]. Our method achieves state-of-the-art performance on the challenging pho- totropism data, outperforming VGGSfMv2 [125] ... | p. 12 (Figure/Table caption), p. 8 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive body cue:** Table 5. Ablation Study for Transformer Backbone on ETH3D. We compare our alternating-attention architecture against two variants: one using only global self-attention and another employ- ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 6. Ablation Study for Multi-task Learning, which shows that simultaneous training with camera, depth and track estimation yields the highest accuracy in point map ...
- **p. 7 / 4.2. Multi-view Depth Estimation - extractive body cue:** 2, DUSt3R and our VGGT are the only two methods operating without the knowledge of ground truth cameras.
- **p. 7 / 4.1. Camera Pose Estimation - extractive body cue:** Compared to concurrent works [111, 127, 141, 156] (indicated by ‡), our method demonstrates significant performance advantages, with speed similar to the fastest variant Fast3R ...
- **p. 9 / 4.5. Ablation Studies - extractive body cue:** 5 demonstrate that our Alternating-Attention architecture outperforms both baseline variants by a clear margin.
- **p. 10 / Figure/Table caption - extractive body cue:** Table 8. Dynamic Point Tracking Results on the TAP-Vid benchmarks. Although our model was not designed for dynamic scenes, simply fine-tuning CoTracker with our pretrained ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. VGGT is a large feed-forward transformer with minimal 3D-inductive biases trained on a trove of 3D-annotated data. It accepts up to hundreds of ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3.3. Prediction heads), p. 3 (3.1. Problem definition and notation), p. 3 (3.1. Problem definition and notation), p. 10 (Method), p. 6 (3.4. Training), p. 5 (3.3. Prediction heads), objective p. 6 (3.4. Training), p. 6 (3.4. Training), p. 5 (3.3. Prediction heads), temporal p. 3 (3.1. Problem definition and notation), p. 3 (3.1. Problem definition and notation), p. 4 (3.1. Problem definition and notation), p. 6 (3.3. Prediction heads), p. 4 (3.2. Feature Backbone), p. 5 (3.3. Prediction heads).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
