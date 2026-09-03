# Method - U-CAN: Unsupervised Point Cloud Denoising with Consistency-Aware Noise2Noise Matching

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=hVFtXE19Me; PDF retrieval source: https://arxiv.org/pdf/2510.25210. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction)): Our main contributions can be summarized as follows. • We introduce U-CAN, a novel framework for unsupervised point cloud denoising by leveraging a neural network to infer a multi-step denoising ...

## Method Body Digest

- **p. 2 / 1 Introduction - extractive body cue:** Our main contributions can be summarized as follows. • We introduce U-CAN, a novel framework for unsupervised point cloud denoising by leveraging a neural network ...
- **p. 1 / Abstract - extractive body cue:** We achieve this by a novel loss which enables statistical reasoning on multiple noisy point cloud observations.
- **p. 1 / Abstract - extractive body cue:** Previous works mostly focus on training neural networks with noisy-clean point cloud pairs for learning denoising priors, which requires extensively manual efforts.
- **p. 2 / 1 Introduction - extractive body cue:** This ambiguity can lead to unstable convergence due to inconsistencies in denoising results across different noisy observations.
- **p. 1 / Abstract - extractive body cue:** We further introduce a novel constraint on the denoised geometry consistency for learning consistency-aware denoising patterns.
- **p. 2 / 1 Introduction - extractive body cue:** precise clean point cloud while keeping high-fidelity local geometries due to the lack of sufficient constraints at local-level.
- **p. 2 / 1 Introduction - extractive body cue:** Extensive experiments demonstrate that the proposed U-CAN outperforms state-of-the-art methods in unsupervised point cloud denoising, upsampling and image denoising, where U-CAN even achieves comparable performances ...
- **p. 1 / Abstract - extractive body cue:** Our evaluations under the widely used benchmarks in point cloud denoising, upsampling and image denoising show significant improvement over the state-of-the-art unsupervised methods, where U-CAN ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** Our main contributions can be summarized as follows. • We introduce U-CAN, a novel framework for unsupervised point cloud denoising by leveraging a neural network ...
- **p. 2 / 1 Introduction - extractive body cue:** In response to this challenge, we introduce a novel consistency-aware constraint that specifically targets the denoising geometric consistency.
- **p. 1 / Abstract - extractive body cue:** We achieve this by a novel loss which enables statistical reasoning on multiple noisy point cloud observations.

## Source Evidence Cues

- **p. 2 / 1 Introduction - extractive body cue:** Our main contributions can be summarized as follows. • We introduce U-CAN, a novel framework for unsupervised point cloud denoising by leveraging a neural network ...
- **p. 1 / Abstract - extractive body cue:** We achieve this by a novel loss which enables statistical reasoning on multiple noisy point cloud observations.
- **p. 1 / Abstract - extractive body cue:** Previous works mostly focus on training neural networks with noisy-clean point cloud pairs for learning denoising priors, which requires extensively manual efforts.
- **p. 2 / 1 Introduction - extractive body cue:** This ambiguity can lead to unstable convergence due to inconsistencies in denoising results across different noisy observations.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Our main contributions can be summarized as follows. • We introduce U-CAN, a novel framework for unsupervised point cloud denoising by leveraging ... | p. 2 (1 Introduction), p. 1 (Abstract) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | We achieve this by a novel loss which enables statistical reasoning on multiple noisy point cloud observations. | p. 1 (Abstract), p. 1 (Abstract) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Previous works mostly focus on training neural networks with noisy-clean point cloud pairs for learning denoising priors, which requires extensively manual efforts. | p. 1 (Abstract), p. 2 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 1 Introduction - extractive body cue:** Our main contributions can be summarized as follows. • We introduce U-CAN, a novel framework for unsupervised point cloud denoising by leveraging a neural network ...
- **p. 1 / Abstract - extractive body cue:** We achieve this by a novel loss which enables statistical reasoning on multiple noisy point cloud observations.
- **p. 1 / Abstract - extractive body cue:** We further introduce a novel constraint on the denoised geometry consistency for learning consistency-aware denoising patterns.
- **p. 2 / 1 Introduction - extractive body cue:** precise clean point cloud while keeping high-fidelity local geometries due to the lack of sufficient constraints at local-level.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | main, contributions, summarized, follows, introduce, U-CAN, novel, framework, unsupervised, point, cloud, denoising, leveraging, neural | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | main, contributions, summarized, follows, introduce, U-CAN, novel, framework, unsupervised, point | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | main, contributions, summarized, follows, introduce, U-CAN, novel, framework, unsupervised, point | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | main, contributions, summarized, follows, introduce, U-CAN, novel, framework, unsupervised, point | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive body cue:** Our main contributions can be summarized as follows. • We introduce U-CAN, a novel framework for unsupervised point cloud denoising by leveraging a neural network ...
- **p. 2 / 1 Introduction - extractive body cue:** Extensive experiments demonstrate that the proposed U-CAN outperforms state-of-the-art methods in unsupervised point cloud denoising, upsampling and image denoising, where U-CAN even achieves comparable performances ...
- **p. 1 / Abstract - extractive body cue:** Our evaluations under the widely used benchmarks in point cloud denoising, upsampling and image denoising show significant improvement over the state-of-the-art unsupervised methods, where U-CAN ...
- **p. 1 / Abstract - extractive body cue:** We achieve this by a novel loss which enables statistical reasoning on multiple noisy point cloud observations.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Our main contributions can be summarized as follows. • We introduce U-CAN, a novel framework for unsupervised point cloud denoising by leveraging ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | This is particularly clear in areas of high-frequency information, such as edges, textures, and intricate patterns, where our method maintains the integrity ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Dataset: PU 10K, 1% 10K, 2% 10K, 3% Ablation CD P2M CD P2M CD P2M 1 step 2.676 1.046 3.903 1.700 5.251 ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1 Introduction - extractive body cue:** Our main contributions can be summarized as follows. • We introduce U-CAN, a novel framework for unsupervised point cloud denoising by leveraging a neural network ...
- **p. 1 / Abstract - extractive body cue:** Previous works mostly focus on training neural networks with noisy-clean point cloud pairs for learning denoising priors, which requires extensively manual efforts.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** main, contributions, summarized, follows, introduce, U-CAN, novel, framework, unsupervised, point, cloud, denoising, leveraging, neural, network, infer, multi-step, path, noisy, observation.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | 4.2 Point Cloud Denoising on Scanned Data For demonstrating the capability of U-CAN to handle real-world point cloud noises, we conduct evaluations ... | p. 8 (4 Experiments), p. 6 (4 Experiments) |
| Semantic / temporal fusion | We provide the visual comparison among the state-of-the-art supervised and unsupervised point cloud denoising methods in Fig. | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Robot query / planning handoff | 3, where our method significantly outperforms DMR-TTD and ScoreDenoise-TTD, and also achieve better performance than the supervised method PU-Net designed for the ... | p. 9 (4 Experiments), p. 7 (4 Experiments) |

## Failure and Ablation Link

- **p. 9 / 4 Experiments - extractive body cue:** Without LDC, performance significantly drops (e.g., CD Table 4: Ablation studies on the framework and loss designs.
- **p. 9 / 4 Experiments - extractive body cue:** To justify the effectiveness of constraint LDC, we remove it and vary the underlying distance metric.
- **p. 7 / 4 Experiments - extractive body cue:** Traditional optimization-based point cloud denoising methods rely heavily on geometric priors to inform their smoothing algorithms and show increased sensitivity to noises with unseen variances, ...
- **p. 8 / 4 Experiments - extractive body cue:** We directly leverage the U-CAN model trained on PUNet dataset for evaluating, without requiring extra training.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: Illustrations on the effect of proposed constraint on denoising consistency. The noise errors indicate the Chamfer distance between the denoised and the clean ...
- **p. 7 / 4 Experiments - extractive body cue:** The unsupervised versions of DMR [28] and ScoreDenoise [29] which leverage the same constraint as TTD, share same limitations of TTD and presents sub-optimal performance ...
- **p. 7 / 4 Experiments - extractive body cue:** For unsupervised denoising, the TTD [14] fails to produce high-fidelity local geometries with only the global constraints.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction), objective p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction), temporal p. 2 (1 Introduction), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 3 (2 Related Work), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
