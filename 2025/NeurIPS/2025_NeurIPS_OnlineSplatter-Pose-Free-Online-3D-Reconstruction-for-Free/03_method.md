# Method - OnlineSplatter: Pose-Free Online 3D Reconstruction for Free-Moving Objects

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=Y9AdTCCEgI; PDF retrieval source: https://arxiv.org/pdf/2510.20605. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3 Method), p. 5 (3 Method), p. 7 (3 Method), p. 4 (3 Method), p. 7 (3 Method), p. 3 (3 Method)): These tokens are then fed into a transformer-based architecture, which directly reasons and outputs pixel-aligned 3D Gaussian representations in a canonical space.

## Method Body Digest

- **p. 4 / 3 Method - extractive body cue:** These tokens are then fed into a transformer-based architecture, which directly reasons and outputs pixel-aligned 3D Gaussian representations in a canonical space.
- **p. 5 / 3 Method - extractive body cue:** While our latent key, derived from tokenized features through end-to-end training with 3D reasoning objectives, captures both visual and geometric information, relying solely on latent ...
- **p. 7 / 3 Method - extractive body cue:** Specifically, we optimize the view encoder (EncoderI 1), positional and view embeddings (f emb pos and f emb view), OnlineSplatter transformer, and unpatchify decoder in ...
- **p. 4 / 3 Method - extractive body cue:** src embd ref embd mem embd mem embd pos pos pos pos pos pos pos pos pos pos pos pos value store decode unpatchify decode ...
- **p. 7 / 3 Method - extractive body cue:** (2) Main Training: We include the Object Memory module and train the entire network end-to-end, allowing the model to learn both reconstruction and memory simultaneously.
- **p. 3 / 3 Method - extractive body cue:** The masked frame V ′ t is then encoded into patch features via a hybrid strategy that concatenates two complementary encoders: fvt = Concat(EncoderI 1(V ...
- **p. 5 / 3 Method - extractive body cue:** To address this dual objective, we introduce a directional key that provides explicit spatial guidance for memory readout.
- **p. 7 / 3 Method - extractive body cue:** These objectives present a challenging optimization landscape, as the gradients for the second objective only become meaningful after the first objective reaches a certain level ...

## Design Rationale

- **p. 5 / 3 Method - extractive body cue:** To address these limitations, we propose a novel object-centric memory mechanism, Dual-Key 3D Object Memory, that consists of a key-value memory bank.
- **p. 4 / 3 Method - extractive body cue:** The input to our framework consists of a stream of RGB images {Vt}N t=0, where object masks {Mt}N t=0 are generated and applied to remove ...
- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are: (i) a novel feed-forward framework for object-centric online 3D reconstruction that operates on monocular RGB streams in real-time, eliminating the need for ...

## Source Evidence Cues

- **p. 4 / 3 Method - extractive body cue:** These tokens are then fed into a transformer-based architecture, which directly reasons and outputs pixel-aligned 3D Gaussian representations in a canonical space.
- **p. 5 / 3 Method - extractive body cue:** While our latent key, derived from tokenized features through end-to-end training with 3D reasoning objectives, captures both visual and geometric information, relying solely on latent ...
- **p. 7 / 3 Method - extractive body cue:** Specifically, we optimize the view encoder (EncoderI 1), positional and view embeddings (f emb pos and f emb view), OnlineSplatter transformer, and unpatchify decoder in ...
- **p. 4 / 3 Method - extractive body cue:** src embd ref embd mem embd mem embd pos pos pos pos pos pos pos pos pos pos pos pos value store decode unpatchify decode ...
- **p. 7 / 3 Method - extractive body cue:** (2) Main Training: We include the Object Memory module and train the entire network end-to-end, allowing the model to learn both reconstruction and memory simultaneously.
- **p. 3 / 3 Method - extractive body cue:** The masked frame V ′ t is then encoded into patch features via a hybrid strategy that concatenates two complementary encoders: fvt = Concat(EncoderI 1(V ...
- **p. 5 / 3 Method - extractive body cue:** To address this dual objective, we introduce a directional key that provides explicit spatial guidance for memory readout.
- **Detected method headings:** 3 Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | These tokens are then fed into a transformer-based architecture, which directly reasons and outputs pixel-aligned 3D Gaussian representations in a canonical space. | p. 4 (3 Method), p. 5 (3 Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | While our latent key, derived from tokenized features through end-to-end training with 3D reasoning objectives, captures both visual and geometric information, relying ... | p. 5 (3 Method), p. 7 (3 Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Specifically, we optimize the view encoder (EncoderI 1), positional and view embeddings (f emb pos and f emb view), OnlineSplatter transformer, and ... | p. 7 (3 Method), p. 4 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 7 / 3 Method - extractive body cue:** These objectives present a challenging optimization landscape, as the gradients for the second objective only become meaningful after the first objective reaches a certain level ...
- **p. 7 / 3 Method - extractive body cue:** First, the photometric loss Lphoto minimizes the MSE between the ground truth images and rendered images from predicted 3D Gaussian parameters at ground truth camera ...
- **p. 6 / 3 Method - extractive body cue:** Our OnlineSplatter model is trained to optimize two complementary objectives: (1) learning relative object-camera pose relationships and predicting pixel-aligned 3D Gaussian 6
- **p. 5 / 3 Method - extractive body cue:** To address this dual objective, we introduce a directional key that provides explicit spatial guidance for memory readout.
- **p. 5 / 3 Method - extractive body cue:** While our latent key, derived from tokenized features through end-to-end training with 3D reasoning objectives, captures both visual and geometric information, relying solely on latent ...
- **p. 3 / 3 Method - extractive body cue:** The term "online" implies that our approach processes incoming data causally, updating the reconstructed object representation incrementally as new frames become available.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 7 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 7 (3 Method), p. 4 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Moreover, control, memory, growth, observations, accumulate, attention-based, module, fuses, incoming, frame, features, compact, latent | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Moreover, control, memory, growth, observations, accumulate, attention-based, module, fuses, incoming | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | address, limitations, novel, object-centric, memory, mechanism, Dual-Key, Object, consists, key-value | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | objectives, present, challenging, optimization, landscape, gradients, second, objective, only, become | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive body cue:** Moreover, to control memory growth as observations accumulate, we propose an attention-based memory module that fuses incoming frame features with a compact latent state, eliminating ...
- **p. 5 / 3 Method - extractive body cue:** Specifically, a trainable value encoder (defined as EncoderV ) takes output tokens Tout src,t as input to produce the new value: v(L) t := f ...
- **p. 3 / 3 Method - extractive body cue:** After encoding the input image at each timestep, these features are input into our proposed OnlineSplatter Transformer, which is designed to process three distinct types ...
- **p. 4 / 3 Method - extractive body cue:** The input to our framework consists of a stream of RGB images {Vt}N t=0, where object masks {Mt}N t=0 are generated and applied to remove ...
- **p. 3 / 3 Method - extractive body cue:** The goal of our method is to perform an online reconstruction of a freely moving rigid object using monocular RGB images without relying on known ...
- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are: (i) a novel feed-forward framework for object-centric online 3D reconstruction that operates on monocular RGB streams in real-time, eliminating the need for ...
- **p. 4 / 3 Method - extractive body cue:** At each timestep t, OnlineSplatter processes the input frame Vt by first patchifying it into patch tokens.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Our contributions are: (i) a novel feed-forward framework for object-centric online 3D reconstruction that operates on monocular RGB streams in real-time, eliminating ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | After encoding the input image at each timestep, these features are input into our proposed OnlineSplatter Transformer, which is designed to process ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | Our contributions are: (i) a novel feed-forward framework for object-centric online 3D reconstruction that operates on monocular RGB streams in real-time, eliminating ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | To adapt it online, we introduce two frame selection strategies for each timestep: (1) rand4: randomly selects 4 frames from past observations ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3 Method - extractive body cue:** While our latent key, derived from tokenized features through end-to-end training with 3D reasoning objectives, captures both visual and geometric information, relying solely on latent ...
- **p. 7 / 3 Method - extractive body cue:** Specifically, we optimize the view encoder (EncoderI 1), positional and view embeddings (f emb pos and f emb view), OnlineSplatter transformer, and unpatchify decoder in ...
- **p. 4 / 3 Method - extractive body cue:** src embd ref embd mem embd mem embd pos pos pos pos pos pos pos pos pos pos pos pos value store decode unpatchify decode ...
- **p. 7 / 3 Method - extractive body cue:** (2) Main Training: We include the Object Memory module and train the entire network end-to-end, allowing the model to learn both reconstruction and memory simultaneously.
- **p. 9 / 4.2 Results - extractive body cue:** We visualize the results at inference timestep t = 4 and t = 16, which corresponds to the early-stage and late-stage settings, respectively.
- **p. 7 / 3 Method - extractive body cue:** We use 8x A100 GPUs for 250K steps with a batch size of 64 in the Warm-up Training stage and 500K steps with a batch ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** tokens, then, transformer-based, architecture, directly, reasons, outputs, pixel-aligned, Gaussian, representations, canonical, space, While, latent, derived, tokenized, features, through, end-to-end, training.
- **Relevant PDF headings:** 3 Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Second, we assess generalization to real-world monocular videos with occlusions using the HO3D dataset [10], which contains hand-object interaction sequences. | p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Semantic / temporal fusion | This section evaluates our approach by outlining the evaluation protocol, describing the datasets for training and testing, comparing against state-of-the-art baselines, and ... | p. 7 (4 Experiments), p. 8 (4.2 Results) |
| Robot query / planning handoff | Even with fewer than four observations, OnlineSplatter significantly outperforms all baselines. | p. 8 (4.2 Results), p. 7 (4 Experiments) |

## Failure and Ablation Link

- **p. 18 / Figure/Table caption - extractive body cue:** Figure 6: Visualization of the effect of without (top row) and with (bottom row) ray alignment loss Lray over 1K -10K training steps. The visualization ...
- **p. 7 / 4 Experiments - extractive body cue:** This section evaluates our approach by outlining the evaluation protocol, describing the datasets for training and testing, comparing against state-of-the-art baselines, and conducting ablation studies ...
- **p. 9 / 4.2 Results - extractive body cue:** 4.3 Ablations and Analysis In this section, we ablate different components of our method and analyze the results.
- **p. 9 / 4.2 Results - extractive body cue:** Variants Early-Stage Mid-Stage Late-Stage Mavg ↑ Mavg ↑ Mavg ↑ Ours 0.699 0.734 0.810 w/o staged training 0.545 0.582 0.588 w/o ray loss (Lray) 0.562 ...
- **p. 10 / 4.2 Results - extractive body cue:** 3.3) through ablation studies and show results in Table 3, demonstrating: Staged Training: Removing the twostage training (warm-up followed by main training) by using a ...
- **p. 10 / 4.2 Results - extractive body cue:** Loss Components: Removing the ray alignment (Lray) notably reduces convergence speed and stability, harming performance.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Overview of OnlineSplatter Pipeline. The input to our framework consists of a stream of RGB images {Vt}N t=0, where object masks {Mt}N t=0 ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3 Method), p. 5 (3 Method), p. 7 (3 Method), p. 4 (3 Method), p. 7 (3 Method), p. 3 (3 Method), objective p. 7 (3 Method), p. 7 (3 Method), p. 6 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 3 (3 Method), temporal p. 2 (1 Introduction), p. 3 (3 Method), p. 4 (3 Method), p. 4 (3 Method), p. 6 (3 Method), p. 8 (4 Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
