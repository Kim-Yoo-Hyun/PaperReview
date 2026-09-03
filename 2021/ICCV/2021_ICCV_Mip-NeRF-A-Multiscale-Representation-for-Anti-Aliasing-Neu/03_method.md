# Method - Mip-NeRF: A Multiscale Representation for Anti-Aliasing Neural Radiance Fields

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2103.13415; PDF retrieval source: https://arxiv.org/pdf/2103.13415. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3. Method), p. 6 (3.2. Architecture), p. 5 (3.1. Cone Tracing and Positional Encoding), p. 5 (3.1. Cone Tracing and Positional Encoding), p. 4 (3.1. Cone Tracing and Positional Encoding), p. 6 (3.2. Architecture)): This use of conical frustums and IPE features also allows us to reduce NeRF's two separate "coarse" and "fine" MLPs into a single multiscale MLP, which increases training and evaluation ...

## Method Body Digest

- **p. 4 / 3. Method - extractive body cue:** This use of conical frustums and IPE features also allows us to reduce NeRF's two separate "coarse" and "fine" MLPs into a single multiscale MLP, ...
- **p. 6 / 3.2. Architecture - extractive body cue:** Our optimization problem is: \ u n der s e t {\modelwei gh ts }{\ op eratorname { mi n}} \, \ sum _{\ray \in ...
- **p. 5 / 3.1. Cone Tracing and Positional Encoding - extractive body cue:** To accomplish this, it is helpful to first rewrite the PE in Equation 1 as a Fourier feature [35, 44]:
- **p. 5 / 3.1. Cone Tracing and Positional Encoding - extractive body cue:** IPE features behave intuitively: If a particular frequency in the positional encoding has a period that is larger than the width of the interval being ...
- **p. 4 / 3.1. Cone Tracing and Positional Encoding - extractive body cue:** Ideally, this featurized representation should be of a similar form to the positional encoding features used in NeRF, as Mildenhall et al. show that this ...
- **p. 6 / 3.2. Architecture - extractive body cue:** This was necessary in NeRF because its PE features meant that its MLPs were only able to learn a model of the scene for one ...
- **p. 6 / 3.2. Architecture - extractive body cue:** Rendering in mip-NeRF follows Equation 3.
- **p. 6 / 3.2. Architecture - extractive body cue:** But our cone casting and IPE features allow us to explicitly encode scale into our input features and thereby enable an MLP to learn a ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** To encode a 3D position and its surrounding Gaussian region, we propose a new feature representation: an integrated positional encoding (IPE).
- **p. 2 / 1. Introduction - extractive body cue:** On a challenging multiresolution benchmark we present, mip-NeRF is able to reduce error rates relative to NeRF by 60% on average (see Figure 2 for ...
- **p. 6 / 3.2. Architecture - extractive body cue:** See the supplement for additional details and some additional differences between JaxNeRF and mip-NeRF that do not affect performance significantly and are incidental to our ...

## Source Evidence Cues

- **p. 4 / 3. Method - extractive body cue:** This use of conical frustums and IPE features also allows us to reduce NeRF's two separate "coarse" and "fine" MLPs into a single multiscale MLP, ...
- **p. 6 / 3.2. Architecture - extractive body cue:** Our optimization problem is: \ u n der s e t {\modelwei gh ts }{\ op eratorname { mi n}} \, \ sum _{\ray \in ...
- **p. 5 / 3.1. Cone Tracing and Positional Encoding - extractive body cue:** To accomplish this, it is helpful to first rewrite the PE in Equation 1 as a Fourier feature [35, 44]:
- **p. 5 / 3.1. Cone Tracing and Positional Encoding - extractive body cue:** IPE features behave intuitively: If a particular frequency in the positional encoding has a period that is larger than the width of the interval being ...
- **p. 4 / 3.1. Cone Tracing and Positional Encoding - extractive body cue:** Ideally, this featurized representation should be of a similar form to the positional encoding features used in NeRF, as Mildenhall et al. show that this ...
- **p. 6 / 3.2. Architecture - extractive body cue:** This was necessary in NeRF because its PE features meant that its MLPs were only able to learn a model of the scene for one ...
- **Detected method headings:** 3. Method (p. 4); 3.2. Architecture (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | This use of conical frustums and IPE features also allows us to reduce NeRF's two separate "coarse" and "fine" MLPs into a ... | p. 4 (3. Method), p. 6 (3.2. Architecture) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Our optimization problem is: \ u n der s e t {\modelwei gh ts }{\ op eratorname { mi n}} \, \ ... | p. 6 (3.2. Architecture), p. 5 (3.1. Cone Tracing and Positional Encoding) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | To accomplish this, it is helpful to first rewrite the PE in Equation 1 as a Fourier feature [35, 44]: | p. 5 (3.1. Cone Tracing and Positional Encoding), p. 5 (3.1. Cone Tracing and Positional Encoding) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 3.2. Architecture - extractive body cue:** Our optimization problem is: \ u n der s e t {\modelwei gh ts }{\ op eratorname { mi n}} \, \ sum _{\ray \in ...
- **p. 5 / 3.1. Cone Tracing and Positional Encoding - extractive body cue:** To accomplish this, it is helpful to first rewrite the PE in Equation 1 as a Fourier feature [35, 44]:
- **p. 6 / 3.2. Architecture - extractive body cue:** Rendering in mip-NeRF follows Equation 3.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3.1. Cone Tracing and Positional Encoding), p. 6 (3.2. Architecture), p. 6 (3.2. Architecture).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | But, cone, casting, IPE, features, allow, explicitly, encode, scale, input, thereby, enable, MLP, learn | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | But, cone, casting, IPE, features, allow, explicitly, encode, scale, input | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | encode, position, surrounding, Gaussian, region, feature, representation, integrated, positional, encoding | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | optimization, problem, modelwei, eratorname, mathcal, Big, lossmult, trueCol, Col, modelweights | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / 3.2. Architecture - extractive body cue:** But our cone casting and IPE features allow us to explicitly encode scale into our input features and thereby enable an MLP to learn a ...
- **p. 6 / 3.2. Architecture - extractive body cue:** By integrating PE features over each interval, the high frequency dimensions of IPE features shrink towards zero when the period of the frequency is small ...
- **p. 1 / 1. Introduction - extractive body cue:** NeRF replaces traditional discrete sampled geometry with a continuous volumetric function, parameterized as a multilayer perceptron (MLP) that maps from an input 5D coordinate (3D ...
- **p. 2 / 1. Introduction - extractive body cue:** The input to mip-NeRF is a 3D Gaussian that represents the region over which the radiance field should be integrated.
- **p. 1 / 1. Introduction - extractive body cue:** A mipmap represents a signal (typically an image or a texture map) at a set of different discrete downsampling scales and selects the appropriate scale ...
- **p. 4 / 3.1. Cone Tracing and Positional Encoding - extractive body cue:** The apex of that cone lies at o, and the radius of the cone at the image plane o + d is parameterized as ˙r.
- **p. 4 / 3.1. Cone Tracing and Positional Encoding - extractive body cue:** As in NeRF, images in mipNeRF are rendered one pixel at a time, so we can describe our procedure in terms of an individual pixel ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | We can transform this Gaussian from the coordinate frame of the conical frustum into world coordinates as follows: \ b old s ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | (10) The final step in producing an IPE feature is computing the expectation over this lifted multivariate Gaussian, modulated by the sine ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3. Method - extractive body cue:** This use of conical frustums and IPE features also allows us to reduce NeRF's two separate "coarse" and "fine" MLPs into a single multiscale MLP, ...
- **p. 6 / 3.2. Architecture - extractive body cue:** We follow NeRF's training procedure: 1 million iterations of Adam [19] with a batch size of 4096 and a learning rate that is annealed logarithmically ...
- **p. 8 / 4. Results - extractive body cue:** Training times taken from prior work (when available) are indicated in gray, as they are not directly comparable. put due to its changing tensor sizes ...
- **p. 8 / 4. Results - extractive body cue:** We report times for rendering the test set, normalized to seconds-permegapixel (training times are the same as Tables 1 and 2). versions of full-resolution images, ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** conical, frustums, IPE, features, allows, reduce, NeRF, separate, coarse, fine, MLPs, single, multiscale, MLP, increases, training, evaluation, speed, reduces, model.
- **Relevant PDF headings:** 3. Method (p. 4); 3.2. Architecture (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | 0.709 0.910 0.931 0.663 0.863 0.959 0.971 0.881 0.940 0.979 0.989 0.978 0.448 0.562 0.696 0.906 0.525 0.633 0.794 0.918 0.785 0.837 ... | p. 7 (4. Results), p. 6 (4. Results) |
| Semantic / temporal fusion | Table 2: A comparison of mip-NeRF and its ablations against several baseline algorithms and variants of NeRF on the single-scale Blender dataset ... | p. 8 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Robot query / planning handoff | [30], mip-NeRF significantly outperforms NeRF and our improved version of NeRF, particularly on small or thin objects such as the holes of ... | p. 8 (4. Results), p. 7 (4. Results) |

## Failure and Ablation Link

- **p. 7 / 4. Results - extractive body cue:** We also evaluate against several ablations of mip-NeRF: "w/o Misc" removes those small changes, "w/o Single MLP" uses NeRF's two-MLP training scheme from Equation 4, ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: A quantitative comparison of mip-NeRF and its ablations against NeRF and several NeRF variants on the test set of our multiscale Blender dataset. ...
- **p. 8 / 4. Results - extractive body cue:** We evaluate against the baselines used by NeRF, NSVF [24], and the same variants and ablations that were used previously (excluding "Area Loss", which is ...
- **p. 8 / 4. Results - extractive body cue:** 33.04 0.960 0.043 0.0162 2.89 ± 0.01 612K Mip-NeRF w/o Single MLP 32.71 0.959 0.044 0.0168 3.63 ± 0.02 1,191K Mip-NeRF w/o IPE 32.48 0.958 ...
- **p. 6 / 4. Results - extractive body cue:** We additionally report runtimes (median and median absolute deviation of wall time) as well as the number of network parameters for each variant of NeRF ...
- **p. 6 / 4. Results - extractive body cue:** We evaluate mip-NeRF on the Blender dataset presented in the original NeRF paper [30] and also on a simple multiscale variant of that dataset designed ...
- **p. 12 / Figure/Table caption - extractive body cue:** Figure 7: PSNRs for NeRF and mip-NeRF on the test set of the lego scene, as we vary the positional encoding degree L. In NeRF, ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3. Method), p. 6 (3.2. Architecture), p. 5 (3.1. Cone Tracing and Positional Encoding), p. 5 (3.1. Cone Tracing and Positional Encoding), p. 4 (3.1. Cone Tracing and Positional Encoding), p. 6 (3.2. Architecture), objective p. 6 (3.2. Architecture), p. 5 (3.1. Cone Tracing and Positional Encoding), p. 6 (3.2. Architecture), temporal p. 5 (3.1. Cone Tracing and Positional Encoding), p. 5 (3.1. Cone Tracing and Positional Encoding), p. 6 (3.2. Architecture), p. 6 (3.2. Architecture), p. 2 (1. Introduction), p. 2 (2. Related Work).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
