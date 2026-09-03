# Method - S2GS: Streaming Semantic Gaussian Splatting for Online Scene Understanding and Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=CbWCaD8tRC; PDF retrieval source: https://openreview.net/pdf/fec4864d5571755c82ad1d076f9a8e3e4ca69cf8.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3.1. Overview and Online Setting), p. 4 (3.2. Causal Transformer for 3D Gaussian Regression), p. 5 (3.4. Language-driven Open-vocabulary Segmentation), p. 5 (3.4. Language-driven Open-vocabulary Segmentation), p. 4 (3.3. Online Instance Tracking and Semantic), p. 3 (3.2. Causal Transformer for 3D Gaussian Regression)): The model maintains a persistent 3D Gaussian scene representation and an instance-aware semantic state, enabling scalable long-horizon streaming inference.

## Method Body Digest

- **p. 3 / 3.1. Overview and Online Setting - extractive body cue:** The model maintains a persistent 3D Gaussian scene representation and an instance-aware semantic state, enabling scalable long-horizon streaming inference.
- **p. 4 / 3.2. Causal Transformer for 3D Gaussian Regression - extractive body cue:** A causal Transformer encoder, guided by geometric priors from a 3D foundation model, predicts camera parameters, depth, and Gaussian attributes to incrementally construct 3D Gaussian ...
- **p. 5 / 3.4. Language-driven Open-vocabulary Segmentation - extractive body cue:** To make the projection robust to such dynamics, we enforce instancelevel semantic invariance during training: supervised querylevel contrastive learning encourages embeddings corresponding to the same ...
- **p. 5 / 3.4. Language-driven Open-vocabulary Segmentation - extractive body cue:** To bridge this gap, we introduce a lightweight Query Semantic Projector gθ(·) that maps each per-frame query embedding to the 2D foundation vision model (Tschannen ...
- **p. 4 / 3.3. Online Instance Tracking and Semantic - extractive body cue:** A lightweight adapter (Chen et al., 2022) converts these features into multiscale representations, which are consumed by a query-based mask-classification decoder (Cheng et al., 2022).
- **p. 3 / 3.2. Causal Transformer for 3D Gaussian Regression - extractive body cue:** Causal Transformer with online state.
- **p. 2 / 4. Across multiple joint reconstruction-and-understanding - extractive body cue:** benchmarks and long-horizon online settings, S2GS achieves performance on par with or better than strong offline baselines, while significantly outperforming offline global paradigms in scalability ...
- **p. 3 / 3.2. Causal Transformer for 3D Gaussian Regression - extractive body cue:** Under the causal constraint, the Transformer aggregates information from {Iτ}τ≤t to form geometry features Ht.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** We propose S2GS, a strictly causal and reprocessing-free framework for online joint 3D reconstruction and scene understanding, which incrementally maintains scene geometry, appearance, and an ...
- **p. 5 / 3.4. Language-driven Open-vocabulary Segmentation - extractive body cue:** To bridge this gap, we introduce a lightweight Query Semantic Projector gθ(·) that maps each per-frame query embedding to the 2D foundation vision model (Tschannen ...
- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are summarized as follows: 1.

## Source Evidence Cues

- **p. 3 / 3.1. Overview and Online Setting - extractive body cue:** The model maintains a persistent 3D Gaussian scene representation and an instance-aware semantic state, enabling scalable long-horizon streaming inference.
- **p. 4 / 3.2. Causal Transformer for 3D Gaussian Regression - extractive body cue:** A causal Transformer encoder, guided by geometric priors from a 3D foundation model, predicts camera parameters, depth, and Gaussian attributes to incrementally construct 3D Gaussian ...
- **p. 5 / 3.4. Language-driven Open-vocabulary Segmentation - extractive body cue:** To make the projection robust to such dynamics, we enforce instancelevel semantic invariance during training: supervised querylevel contrastive learning encourages embeddings corresponding to the same ...
- **p. 5 / 3.4. Language-driven Open-vocabulary Segmentation - extractive body cue:** To bridge this gap, we introduce a lightweight Query Semantic Projector gθ(·) that maps each per-frame query embedding to the 2D foundation vision model (Tschannen ...
- **p. 4 / 3.3. Online Instance Tracking and Semantic - extractive body cue:** A lightweight adapter (Chen et al., 2022) converts these features into multiscale representations, which are consumed by a query-based mask-classification decoder (Cheng et al., 2022).
- **p. 3 / 3.2. Causal Transformer for 3D Gaussian Regression - extractive body cue:** Causal Transformer with online state.
- **p. 2 / 4. Across multiple joint reconstruction-and-understanding - extractive body cue:** benchmarks and long-horizon online settings, S2GS achieves performance on par with or better than strong offline baselines, while significantly outperforming offline global paradigms in scalability ...
- **Detected method headings:** 3. Method (p. 3); 82.49 Method (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | The model maintains a persistent 3D Gaussian scene representation and an instance-aware semantic state, enabling scalable long-horizon streaming inference. | p. 3 (3.1. Overview and Online Setting), p. 4 (3.2. Causal Transformer for 3D Gaussian Regression) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | A causal Transformer encoder, guided by geometric priors from a 3D foundation model, predicts camera parameters, depth, and Gaussian attributes to incrementally ... | p. 4 (3.2. Causal Transformer for 3D Gaussian Regression), p. 5 (3.4. Language-driven Open-vocabulary Segmentation) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | To make the projection robust to such dynamics, we enforce instancelevel semantic invariance during training: supervised querylevel contrastive learning encourages embeddings corresponding ... | p. 5 (3.4. Language-driven Open-vocabulary Segmentation), p. 5 (3.4. Language-driven Open-vocabulary Segmentation) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3.2. Causal Transformer for 3D Gaussian Regression - extractive body cue:** Under the causal constraint, the Transformer aggregates information from {Iτ}τ≤t to form geometry features Ht.
- **p. 4 / 3.3. Online Instance Tracking and Semantic - extractive body cue:** We optimize the supervised contrastive loss: Lcl = /Z/ X i=1 -1 /P(i)/ X p∈P(i) log exp(z⊤ i zp/τ) P a̸=i exp(z⊤ i za/τ), (4) ...
- **p. 3 / 3.2. Causal Transformer for 3D Gaussian Regression - extractive body cue:** We supervise the student by (i) an ℓ2 loss on depth over valid pixels and (ii) a Huber loss on the camera parameters, encouraging the ...
- **p. 5 / 3.4. Language-driven Open-vocabulary Segmentation - extractive body cue:** We then align the projected query embedding ut,n with vt,n using a cosine regression loss, so that projected queries become directly comparable to SigLIP2 text ...
- **p. 5 / 3.4. Language-driven Open-vocabulary Segmentation - extractive body cue:** At test time, given a text description r, we obtain a normalized text embedding er using the SigLIP2 (Tschannen et al., 2025) text encoder and ...
- **p. 4 / 3.2. Causal Transformer for 3D Gaussian Regression - extractive body cue:** S2GS processes an uncalibrated and unposed RGB image stream in a strictly causal manner.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (3.2. Causal Transformer for 3D Gaussian Regression), p. 3 (3.2. Causal Transformer for 3D Gaussian Regression), p. 4 (3.3. Online Instance Tracking and Semantic), p. 5 (3.4. Language-driven Open-vocabulary Segmentation), p. 4 (3.2. Causal Transformer for 3D Gaussian Regression), p. 5 (3.4. Language-driven Open-vocabulary Segmentation).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | naturally, imposes, causal, constraint, online, joint, reconstruction, understanding, time, step, model, only, rely, current | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | naturally, imposes, causal, constraint, online, joint, reconstruction, understanding, time, step | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | S2GS, strictly, causal, reprocessing-free, framework, online, joint, reconstruction, scene, understanding | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Under, causal, constraint, Transformer, aggregates, information, form, geometry, features, optimize | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** This naturally imposes a causal constraint on online joint reconstruction and understanding: at each time step, the model can only rely on the current observation ...
- **p. 1 / 1. Introduction - extractive body cue:** More fundamentally, in real-world online scenarios, inputs arrive sequentially over time and the system must update its state 1.
- **p. 5 / 3.4. Language-driven Open-vocabulary Segmentation - extractive body cue:** To provide a semantic teacher signal, we apply the predicted mask mt,n to the input image and encode the masked region using the frozen SigLIP2 ...
- **p. 2 / 1. Introduction - extractive body cue:** Based on the above gaps, we revisit online joint 3D reconstruction and semantic understanding for long input streams, and propose Streaming Semantic Gaussian Splatting (S2GS).
- **p. 3 / 3.2. Causal Transformer for 3D Gaussian Regression - extractive body cue:** Causal Transformer with online state.
- **p. 3 / 3.2. Causal Transformer for 3D Gaussian Regression - extractive body cue:** At inference, key/value tensors from past frames are cached and reused, enabling efficient long-horizon streaming without re-forwarding previous inputs.
- **p. 5 / 3.4. Language-driven Open-vocabulary Segmentation - extractive body cue:** In contrast, we focus on streaming inference, where queries are generated per frame and updated online over time, making global multi-view interaction infeasible.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | This naturally imposes a causal constraint on online joint reconstruction and understanding: at each time step, the model can only rely on ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | At each time step, a fixed set of learnable queries attends to the current frame to produce per-frame masks, class scores, and ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | While effective for short sequences, this paradigm scales poorly: both runtime and memory typically grow rapidly with the number of views, hindering ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3.1. Overview and Online Setting - extractive body cue:** The model maintains a persistent 3D Gaussian scene representation and an instance-aware semantic state, enabling scalable long-horizon streaming inference.
- **p. 5 / 3.4. Language-driven Open-vocabulary Segmentation - extractive body cue:** To make the projection robust to such dynamics, we enforce instancelevel semantic invariance during training: supervised querylevel contrastive learning encourages embeddings corresponding to the same ...
- **p. 3 / 3.2. Causal Transformer for 3D Gaussian Regression - extractive body cue:** Causal Transformer with online state.
- **p. 2 / 4. Across multiple joint reconstruction-and-understanding - extractive body cue:** benchmarks and long-horizon online settings, S2GS achieves performance on par with or better than strong offline baselines, while significantly outperforming offline global paradigms in scalability ...
- **p. 6 / 4.2. Results - extractive body cue:** Current-frame inference time and PGM under online streaming input.
- **p. 2 / 4. Across multiple joint reconstruction-and-understanding - extractive body cue:** benchmarks and long-horizon online settings, S2GS achieves performance on par with or better than strong offline baselines, while significantly outperforming offline global paradigms in scalability ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** model, maintains, persistent, Gaussian, scene, representation, instance-aware, semantic, state, enabling, scalable, long-horizon, streaming, inference, causal, Transformer, encoder, guided, geometric, priors.
- **Relevant PDF headings:** 3. Method (p. 3); 82.49 Method (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Comparison with feed-forward methods on the ScanNet (Dai et al., 2017) dataset under short-sequence inputs. "•", "†", and "⋆" denote reconstruction-only, understanding-only, ... | p. 6 (4.1. Experimental Setup), p. 7 (4.2. Results) |
| Semantic / temporal fusion | We also include widely used 2D semantic segmentation baselines, LSeg (Li et al., 2022) and Mask2Former (Cheng et al., 2022). | p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup) |
| Robot query / planning handoff | Nevertheless, as the number of input views increases (8/14/32), S2GS consistently improves and achieves strong performance in both reconstruction quality and temporal ... | p. 6 (4.2. Results), p. 8 (4.3. Ablation Studies) |

## Failure and Ablation Link

- **p. 8 / 4.2. Results - extractive body cue:** Ablation study on the effectiveness of query-level semantic-embedding contrastive learning.
- **p. 8 / 4.2. Results - extractive body cue:** Ablation study on the effectiveness of distilling the base model for the geometric backbone.
- **p. 6 / 4.2. Results - extractive body cue:** In contrast, S2GS is designed for streaming inputs and incrementally aggregates multi-view evidence as views arrive, without relying on global alignment.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Overview of S2GS. S2GS processes an uncalibrated and unposed RGB image stream in a strictly causal manner. A causal Transformer encoder, guided by ...
- **p. 6 / 4.2. Results - extractive body cue:** As shown in Table 2, under the extremely sparse 2-view setting, S2GS does not achieve the best PSNR/SSIM.
- **p. 6 / 4.2. Results - extractive body cue:** This is expected, since offline baselines can exploit non-causal cross-view aggregation over the full input set to better resolve view ambiguity and occlusions when observations ...
- **p. 8 / 4.2. Results - extractive body cue:** Nevertheless, under the same training configuration, S2GS achieves better reconstruction and semantic performance on both datasets, demonstrating stronger cross-dataset generalization and robustness.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3.1. Overview and Online Setting), p. 4 (3.2. Causal Transformer for 3D Gaussian Regression), p. 5 (3.4. Language-driven Open-vocabulary Segmentation), p. 5 (3.4. Language-driven Open-vocabulary Segmentation), p. 4 (3.3. Online Instance Tracking and Semantic), p. 3 (3.2. Causal Transformer for 3D Gaussian Regression), objective p. 3 (3.2. Causal Transformer for 3D Gaussian Regression), p. 4 (3.3. Online Instance Tracking and Semantic), p. 3 (3.2. Causal Transformer for 3D Gaussian Regression), p. 5 (3.4. Language-driven Open-vocabulary Segmentation), p. 5 (3.4. Language-driven Open-vocabulary Segmentation), p. 4 (3.2. Causal Transformer for 3D Gaussian Regression), temporal p. 2 (1. Introduction), p. 4 (3.3. Online Instance Tracking and Semantic), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (2. Related Work), p. 3 (3.2. Causal Transformer for 3D Gaussian Regression).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
