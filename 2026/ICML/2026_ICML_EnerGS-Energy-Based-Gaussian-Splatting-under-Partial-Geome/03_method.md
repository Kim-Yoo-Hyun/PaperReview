# Method - EnerGS: Energy-Based Gaussian Splatting under Partial Geometric Priors

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=ebt72acjt6; PDF retrieval source: https://openreview.net/pdf/bfce7f71c1e37001e68263ecce2837ec77904739.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3. Methodology), p. 3 (3.2. Probabilistic Geometric Field), p. 5 (3.5. Complexity and Implementation Efficiency), p. 5 (4.3. Optimization Stability), p. 4 (3.4. Discrete Pruning as Boundary Enforcement), p. 4 (3.5. Complexity and Implementation Efficiency)): Standard optimization updates all parameters Θi = {µi, Σi, αi, ci} by descending the gradient of the photometric loss Lphoto = λ1L1 + λ2LD-SSIM: Θ(t+1) i ←Θ(t) i -η ∂Lphoto ...

## Method Body Digest

- **p. 3 / 3. Methodology - extractive body cue:** Standard optimization updates all parameters Θi = {µi, Σi, αi, ci} by descending the gradient of the photometric loss Lphoto = λ1L1 + λ2LD-SSIM: Θ(t+1) ...
- **p. 3 / 3.2. Probabilistic Geometric Field - extractive body cue:** (4) This conditional independence assumption applies at the sensor-observation level: given the scene parameters Θ, RGB and LiDAR observations are modeled as independent sensing processes.
- **p. 5 / 3.5. Complexity and Implementation Efficiency - extractive body cue:** Experimentally, our geometric module incurs negligible overhead, allowing the framework to maintain the training efficiency characteristic of 3D Gaussian Splatting.
- **p. 5 / 4.3. Optimization Stability - extractive body cue:** We analyze the smoothness of the optimization trajectory by examining the Lipschitz properties of the driving force.
- **p. 4 / 3.4. Discrete Pruning as Boundary Enforcement - extractive body cue:** Every Tprune iterations, we verify the spatial state of all primitives: G ←G \ {Gi / dtrust(µi) > τmargin}.
- **p. 4 / 3.5. Complexity and Implementation Efficiency - extractive body cue:** During training, the geometric regularization operates with linear complexity relative to the number of primitives N.
- **p. 3 / 3.2. Probabilistic Geometric Field - extractive body cue:** Assuming the geometric prior is independent of the photometric appearance, our objective is to maximize the posterior: P(Θ/I, PLiDAR) ∝P(I/Θ) / {z } Photometry · ...
- **p. 4 / 3.3. Optimization via Gradient Decoupling - extractive body cue:** Directly minimizing Ltotal = Lphoto + λEgeom is suboptimal because the noisy photometric gradient ∂Lphoto ∂µ often contradicts the geometric gradient ∂Egeom ∂µ , leading ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are summarized as follows: • We introduce an energy field that unifies uncertainaware occupancy attraction (via a Welsch M-estimator) and free space exclusion ...
- **p. 2 / 1. Introduction - extractive body cue:** We propose Energy-Based Gaussian Splatting (EnerGS), a framework that reformulates 3DGS optimization as inference within a geometric energy field, as shown in Fig.
- **p. 3 / 3. Methodology - extractive body cue:** We present EnerGS, a framework that regularizes volumetric reconstruction by enforcing geometric priors derived from partially observed geometry information.

## Source Evidence Cues

- **p. 3 / 3. Methodology - extractive body cue:** Standard optimization updates all parameters Θi = {µi, Σi, αi, ci} by descending the gradient of the photometric loss Lphoto = λ1L1 + λ2LD-SSIM: Θ(t+1) ...
- **p. 3 / 3.2. Probabilistic Geometric Field - extractive body cue:** (4) This conditional independence assumption applies at the sensor-observation level: given the scene parameters Θ, RGB and LiDAR observations are modeled as independent sensing processes.
- **p. 5 / 3.5. Complexity and Implementation Efficiency - extractive body cue:** Experimentally, our geometric module incurs negligible overhead, allowing the framework to maintain the training efficiency characteristic of 3D Gaussian Splatting.
- **p. 5 / 4.3. Optimization Stability - extractive body cue:** We analyze the smoothness of the optimization trajectory by examining the Lipschitz properties of the driving force.
- **p. 4 / 3.4. Discrete Pruning as Boundary Enforcement - extractive body cue:** Every Tprune iterations, we verify the spatial state of all primitives: G ←G \ {Gi / dtrust(µi) > τmargin}.
- **p. 4 / 3.5. Complexity and Implementation Efficiency - extractive body cue:** During training, the geometric regularization operates with linear complexity relative to the number of primitives N.
- **Detected method headings:** 3. Methodology (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Standard optimization updates all parameters Θi = {µi, Σi, αi, ci} by descending the gradient of the photometric loss Lphoto = λ1L1 ... | p. 3 (3. Methodology), p. 3 (3.2. Probabilistic Geometric Field) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | (4) This conditional independence assumption applies at the sensor-observation level: given the scene parameters Θ, RGB and LiDAR observations are modeled as ... | p. 3 (3.2. Probabilistic Geometric Field), p. 5 (3.5. Complexity and Implementation Efficiency) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Experimentally, our geometric module incurs negligible overhead, allowing the framework to maintain the training efficiency characteristic of 3D Gaussian Splatting. | p. 5 (3.5. Complexity and Implementation Efficiency), p. 5 (4.3. Optimization Stability) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3. Methodology - extractive body cue:** Standard optimization updates all parameters Θi = {µi, Σi, αi, ci} by descending the gradient of the photometric loss Lphoto = λ1L1 + λ2LD-SSIM: Θ(t+1) ...
- **p. 3 / 3.2. Probabilistic Geometric Field - extractive body cue:** Assuming the geometric prior is independent of the photometric appearance, our objective is to maximize the posterior: P(Θ/I, PLiDAR) ∝P(I/Θ) / {z } Photometry · ...
- **p. 4 / 3.3. Optimization via Gradient Decoupling - extractive body cue:** Directly minimizing Ltotal = Lphoto + λEgeom is suboptimal because the noisy photometric gradient ∂Lphoto ∂µ often contradicts the geometric gradient ∂Egeom ∂µ , leading ...
- **p. 5 / 4.3. Optimization Stability - extractive body cue:** The geometric energy field Egeom induces a gradient field with a bounded Lipschitz constant, regularizing the optimization trajectory against high-frequency photometric noise.
- **p. 4 / 3.3. Optimization via Gradient Decoupling - extractive body cue:** We explicitly block the flow of photometric gradients to the mean position µ, while allowing them to update covariance and appearance.
- **p. 5 / 4.3. Optimization Stability - extractive body cue:** Photometric Field: The gradient derived from rasterization, ∂Lphoto ∂µ , contains discontinuities due to visibility jumps (occlusions) and sampling aliasing.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (3. Methodology), p. 4 (3.3. Optimization via Gradient Decoupling), p. 4 (3.5. Complexity and Implementation Efficiency), p. 3 (3. Methodology), p. 5 (4.3. Optimization Stability), p. 5 (4.3. Optimization Stability).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | contributions, summarized, follows, introduce, energy, field, unifies, uncertainaware, occupancy, attraction, Welsch, M-estimator, free, space | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | contributions, summarized, follows, introduce, energy, field, unifies, uncertainaware, occupancy, attraction | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | contributions, summarized, follows, introduce, energy, field, unifies, uncertainaware, occupancy, attraction | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Standard, optimization, updates, parameters, descending, gradient, photometric, loss, Lphoto, LD-SSIM | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are summarized as follows: • We introduce an energy field that unifies uncertainaware occupancy attraction (via a Welsch M-estimator) and free space exclusion ...
- **p. 3 / 3.2. Probabilistic Geometric Field - extractive body cue:** (4) This conditional independence assumption applies at the sensor-observation level: given the scene parameters Θ, RGB and LiDAR observations are modeled as independent sensing processes.
- **p. 4 / 3.4. Discrete Pruning as Boundary Enforcement - extractive body cue:** Every Tprune iterations, we verify the spatial state of all primitives: G ←G \ {Gi / dtrust(µi) > τmargin}.
- **p. 3 / 3.2. Probabilistic Geometric Field - extractive body cue:** Let I = {Iv}v denote the set of images, and let PLiDAR = {pk}k ⊂R3 denote a LiDAR point cloud.
- **p. 4 / 3.5. Complexity and Implementation Efficiency - extractive body cue:** In the initialization step, we compute the Euclidean Distance Transform [11] for the LiDAR point cloud and derive the gradient field ∇Egeom via central differences.
- **p. 1 / 1. Introduction - extractive body cue:** To constrain this ill-posedness, a common strategy is to incorporate depth priors directly into the optimization objective [8, 41, 40, 26].
- **p. 2 / 1. Introduction - extractive body cue:** Our key insight is that the geometric constraint must be adaptive: it should be rigid in regions with active sensor coverage to enforce physical validity, ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | We present EnerGS, a framework that regularizes volumetric reconstruction by enforcing geometric priors derived from partially observed geometry information. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | In the initialization step, we compute the Euclidean Distance Transform [11] for the LiDAR point cloud and derive the gradient field ∇Egeom ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.5. Complexity and Implementation Efficiency - extractive body cue:** Experimentally, our geometric module incurs negligible overhead, allowing the framework to maintain the training efficiency characteristic of 3D Gaussian Splatting.
- **p. 4 / 3.5. Complexity and Implementation Efficiency - extractive body cue:** During training, the geometric regularization operates with linear complexity relative to the number of primitives N.
- **p. 4 / 3.5. Complexity and Implementation Efficiency - extractive body cue:** This O(V 3) operation is performed once, avoiding expensive runtime differentiation and ensuring that complex geometric constraints are reduced to simple lookups.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Standard, optimization, updates, parameters, descending, gradient, photometric, loss, Lphoto, LD-SSIM, conditional, independence, assumption, applies, sensor-observation, level, given, scene, RGB, LiDAR.
- **Relevant PDF headings:** 3. Methodology (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Our study focuses exclusively on static scenes, and consequently, the evaluation excludes all dynamic objects. | p. 6 (5.1. Experimental Setup), p. 6 (5.3. Qualitative Results) |
| Semantic / temporal fusion | Our method renders significantly finer details in these areas compared to baselines, aligning with our theoretical expectation that the adaptive energy field ... | p. 7 (5.3. Qualitative Results), p. 8 (5.3. Qualitative Results) |
| Robot query / planning handoff | On KITTI, it attains the highest PSNR and OccCov together with the lowest Leak score, indicating improved alignment with occupied regions and ... | p. 6 (5.2. Quantitative Analysis), p. 6 (5.1. Experimental Setup) |

## Failure and Ablation Link

- **p. 8 / 5.4. Ablation Studies - extractive body cue:** Several ablation variants show reduced leakage ratios and increased margins while occupied coverage and surface alignment deteriorate.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2. Ablation Study on KITTI and Waymo Open Dataset. All values report differences (∆) relative to the full EnerGS model. Positive ∆indicates an increase ...
- **p. 5 / 4.4. Permissiveness via Asymptotic Variance Analysis - extractive body cue:** Finally, we demonstrate that the "Unknown" region naturally permits reconstruction driven by photometry, without requiring explicit heuristic switching.
- **p. 7 / 5.3. Qualitative Results - extractive body cue:** Our method renders significantly finer details in these areas compared to baselines, aligning with our theoretical expectation that the adaptive energy field facilitates robust reconstruction ...
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 6. Comparison of rendering results in LiDAR blind-spot regions (unobservable geometry), highlighting the effect of enabling the UNK field. B. Derivation and Interpretation of ...
- **p. 17 / Figure/Table caption - extractive body cue:** Table 3. Correspondence between paper components and code implementation. Paper Component Equation Implementation Occupied attraction Eocc Eq. (5) Listing 1, Line 2 Free space barrier ...
- **p. 8 / 6. Conclusion - extractive body cue:** It shows that degenerate solutions in free space cannot form stable equilibria and that the geometric update field is well-conditioned.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3. Methodology), p. 3 (3.2. Probabilistic Geometric Field), p. 5 (3.5. Complexity and Implementation Efficiency), p. 5 (4.3. Optimization Stability), p. 4 (3.4. Discrete Pruning as Boundary Enforcement), p. 4 (3.5. Complexity and Implementation Efficiency), objective p. 3 (3. Methodology), p. 3 (3.2. Probabilistic Geometric Field), p. 4 (3.3. Optimization via Gradient Decoupling), p. 5 (4.3. Optimization Stability), p. 4 (3.3. Optimization via Gradient Decoupling), p. 5 (4.3. Optimization Stability), temporal p. 3 (3. Methodology), p. 4 (3.5. Complexity and Implementation Efficiency), p. 5 (3.5. Complexity and Implementation Efficiency), p. 6 (5.1. Experimental Setup), p. 6 (5.1. Experimental Setup), p. 1 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
