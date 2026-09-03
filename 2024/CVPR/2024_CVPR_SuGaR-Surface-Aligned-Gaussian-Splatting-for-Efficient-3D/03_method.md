# Method - SuGaR: Surface-Aligned Gaussian Splatting for Efficient 3D Mesh Reconstruction and High-Quality Mesh Rendering

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Guedon_SuGaR_Surface-Aligned_Gaussian_Splatting_for_Efficient_3D_Mesh_Reconstruction_and_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Guedon_SuGaR_Surface-Aligned_Gaussian_Splatting_for_Efficient_3D_Mesh_Reconstruction_and_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (4. Method), p. 5 (4.1. Aligning the Gaussians with the Surface), p. 4 (4.1. Aligning the Gaussians with the Surface), p. 5 (4.1. Aligning the Gaussians with the Surface), p. 6 (4.3. Binding New 3D Gaussians to the Mesh), p. 6 (4.2. Efficient Mesh Extraction)): We present our SuGaR in this section: • First, we detail our loss term that enforces the alignment of the 3D Gaussians with the surface of the scene during the ...

## Method Body Digest

- **p. 4 / 4. Method - extractive body cue:** We present our SuGaR in this section: • First, we detail our loss term that enforces the alignment of the 3D Gaussians with the surface ...
- **p. 5 / 4.1. Aligning the Gaussians with the Surface - extractive body cue:** (5) A first strategy to enforce our regularization is to add term /d(p) -¯d(p)/ to the optimization loss.
- **p. 4 / 4.1. Aligning the Gaussians with the Surface - extractive body cue:** As discussed in the introduction, to facilitate the creation of a mesh from the Gaussians, we introduce a regularization term into the Gaussian Splatting optimization ...
- **p. 5 / 4.1. Aligning the Gaussians with the Surface - extractive body cue:** To do so, we propose to use the depth maps of the Gaussians from the viewpoints used for training-these depth maps can be rendered efficiently ...
- **p. 6 / 4.3. Binding New 3D Gaussians to the Mesh - extractive body cue:** To do so, we slightly modify the structure of the original 3D Gaussian Splatting model.
- **p. 6 / 4.2. Efficient Mesh Extraction - extractive body cue:** To create a mesh from the Gaussians obtained after optimization using our regularization terms in Eq.
- **p. 4 / 4.1. Aligning the Gaussians with the Surface - extractive body cue:** By minimizing the difference between this SDF and the actual SDF computed for the Gaussians, we encourage the Gaussians to have these properties.
- **p. 5 / 4.1. Aligning the Gaussians with the Surface - extractive body cue:** While this approach works well to align Gaussians with the surface, we noticed that computing a slightly different loss relying on an SDF rather than ...

## Design Rationale

- **p. 4 / 4. Method - extractive body cue:** We present our SuGaR in this section: • First, we detail our loss term that enforces the alignment of the 3D Gaussians with the surface ...
- **p. 2 / 1. Introduction - extractive body cue:** To summarize, our contributions are: • a regularization term that makes the Gaussians capture accurately the geometry of the scene; • an efficient algorithm that ...
- **p. 2 / 1. Introduction - extractive body cue:** In fact, since we introduce a density function to evaluate our regularization term, a natural approach would be to extract level sets of this density ...

## Source Evidence Cues

- **p. 4 / 4. Method - extractive body cue:** We present our SuGaR in this section: • First, we detail our loss term that enforces the alignment of the 3D Gaussians with the surface ...
- **p. 5 / 4.1. Aligning the Gaussians with the Surface - extractive body cue:** (5) A first strategy to enforce our regularization is to add term /d(p) -¯d(p)/ to the optimization loss.
- **p. 4 / 4.1. Aligning the Gaussians with the Surface - extractive body cue:** As discussed in the introduction, to facilitate the creation of a mesh from the Gaussians, we introduce a regularization term into the Gaussian Splatting optimization ...
- **p. 5 / 4.1. Aligning the Gaussians with the Surface - extractive body cue:** To do so, we propose to use the depth maps of the Gaussians from the viewpoints used for training-these depth maps can be rendered efficiently ...
- **p. 6 / 4.3. Binding New 3D Gaussians to the Mesh - extractive body cue:** To do so, we slightly modify the structure of the original 3D Gaussian Splatting model.
- **p. 6 / 4.2. Efficient Mesh Extraction - extractive body cue:** To create a mesh from the Gaussians obtained after optimization using our regularization terms in Eq.
- **Detected method headings:** 4. Method (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | We present our SuGaR in this section: • First, we detail our loss term that enforces the alignment of the 3D Gaussians ... | p. 4 (4. Method), p. 5 (4.1. Aligning the Gaussians with the Surface) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | (5) A first strategy to enforce our regularization is to add term /d(p) -¯d(p)/ to the optimization loss. | p. 5 (4.1. Aligning the Gaussians with the Surface), p. 4 (4.1. Aligning the Gaussians with the Surface) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | As discussed in the introduction, to facilitate the creation of a mesh from the Gaussians, we introduce a regularization term into the ... | p. 4 (4.1. Aligning the Gaussians with the Surface), p. 5 (4.1. Aligning the Gaussians with the Surface) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4.1. Aligning the Gaussians with the Surface - extractive body cue:** (5) A first strategy to enforce our regularization is to add term /d(p) -¯d(p)/ to the optimization loss.
- **p. 4 / 4. Method - extractive body cue:** We present our SuGaR in this section: • First, we detail our loss term that enforces the alignment of the 3D Gaussians with the surface ...
- **p. 4 / 4.1. Aligning the Gaussians with the Surface - extractive body cue:** By minimizing the difference between this SDF and the actual SDF computed for the Gaussians, we encourage the Gaussians to have these properties.
- **p. 5 / 4.1. Aligning the Gaussians with the Surface - extractive body cue:** While this approach works well to align Gaussians with the surface, we noticed that computing a slightly different loss relying on an SDF rather than ...
- **p. 6 / 4.2. Efficient Mesh Extraction - extractive body cue:** Right: Mesh before and after joint refinement. define as the normalized analytical gradient of the density ∇d(ˆp) ∥∇d(ˆp)∥2 .
- **p. 6 / 4.2. Efficient Mesh Extraction - extractive body cue:** To create a mesh from the Gaussians obtained after optimization using our regularization terms in Eq.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (4. Method), p. 5 (4.1. Aligning the Gaussians with the Surface), p. 5 (4.1. Aligning the Gaussians with the Surface), p. 6 (4.2. Efficient Mesh Extraction), p. 4 (4.1. Aligning the Gaussians with the Surface).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Value, taken, distance, between, intersection, line, sight, depth, maps, Gaussians, viewpoints, training-these, rendered, efficiently | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Value, taken, distance, between, intersection, line, sight, depth, maps, Gaussians | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | present, SuGaR, section, First, detail, loss, term, enforces, alignment, Gaussians | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | first, strategy, enforce, regularization, term, optimization, loss, present, SuGaR, section | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 4.1. Aligning the Gaussians with the Surface - extractive body cue:** Value ˆf(p) is taken as the 3D distance between p and the intersection between the line of sight for p and the depth map.
- **p. 5 / 4.1. Aligning the Gaussians with the Surface - extractive body cue:** To do so, we propose to use the depth maps of the Gaussians from the viewpoints used for training-these depth maps can be rendered efficiently ...
- **p. 6 / 4.2. Efficient Mesh Extraction - extractive body cue:** We first randomly sample pixels from each depth map.
- **p. 6 / 4.2. Efficient Mesh Extraction - extractive body cue:** Formally, we sample n points p + tiv, where p is the 3D point in the depth map that reprojects on pixel m, v is ...
- **p. 2 / 1. Introduction - extractive body cue:** Our scalable extraction method obtains a mesh even without our regularization term.
- **p. 2 / 1. Introduction - extractive body cue:** As illustrated in Figures 2 and 4, our method produces without our regularization term with our regularization term zoom on Gaussians mesh with mesh with ...
- **p. 3 / 1. Introduction - extractive body cue:** 3D Gaussian Splatting, describe SuGaR, and compare it to the state of the art.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Right: Comparison between the extracted mesh without (left) and with (right) our refinement step. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | However, most of these methods do not target real-time rendering. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | However, the original NeRF is computationally expensive and memory intensive. | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 4.1. Aligning the Gaussians with the Surface - extractive body cue:** To do so, we propose to use the depth maps of the Gaussians from the viewpoints used for training-these depth maps can be rendered efficiently ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** present, SuGaR, section, First, detail, loss, term, enforces, alignment, Gaussians, surface, scene, during, optimization, Gaussian, Splatting, then, exploits, extracting, highly.
- **Relevant PDF headings:** 4. Method (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | For evaluating our model, we follow the approach from the original 3D Gaussian Splatting paper [15] and compare the performance of several ... | p. 7 (5.2. Real-Time Rendering of Real Scenes), p. 7 (5.2. Real-Time Rendering of Real Scenes) |
| Semantic / temporal fusion | Moreover, SuGaR even reaches performance similar to state-of-the-art models for rendering quality [2, 15] on some of the scenes used for evaluation. | p. 7 (5.2. Real-Time Rendering of Real Scenes), p. 7 (5.2. Real-Time Rendering of Real Scenes) |
| Robot query / planning handoff | Even though SuGaR focuses on aligning 3D Gaussians for reconstructing a high quality mesh during the first stage of its optimization, it ... | p. 7 (5.2. Real-Time Rendering of Real Scenes), p. 7 (5.2. Real-Time Rendering of Real Scenes) |

## Failure and Ablation Link

- **p. 7 / 5.1. Implementation details - extractive body cue:** For all experiments except the ablation presented in Table 2, we extract the λ-level set of the density function for λ = 0.3.
- **p. 7 / 5.1. Implementation details - extractive body cue:** For all scenes, we start by optimizing a Gaussian Splatting with no regularization for 7,000 iterations to let the 3D Gaussians position themselves without any ...
- **p. 8 / 5.4. Mesh Rendering Ablation - extractive body cue:** Ablation for different mesh extraction methods on the Mip-NeRF360 dataset [2] after applying our regularization term.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Our algorithm can extract a highly detailed mesh from any 3D Gaussian Splatting scene [15] within minutes on a single GPU (top: Renderings ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 3. Extracting a mesh from Gaussians. Without regular- ization, the Gaussians have no special arrangement after optimiza- tion, which makes extracting a mesh very ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 6. Sampling points on a level set for Poisson reconstruc- tion. Left: We sample points on the depth maps of the Gaussians and refine ...
- **p. 8 / 5.4. Mesh Rendering Ablation - extractive body cue:** For fair comparison, we only use the diffuse spherical harmonics component when rendering images with SuGaR.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (4. Method), p. 5 (4.1. Aligning the Gaussians with the Surface), p. 4 (4.1. Aligning the Gaussians with the Surface), p. 5 (4.1. Aligning the Gaussians with the Surface), p. 6 (4.3. Binding New 3D Gaussians to the Mesh), p. 6 (4.2. Efficient Mesh Extraction), objective p. 5 (4.1. Aligning the Gaussians with the Surface), p. 4 (4. Method), p. 4 (4.1. Aligning the Gaussians with the Surface), p. 5 (4.1. Aligning the Gaussians with the Surface), p. 6 (4.2. Efficient Mesh Extraction), p. 6 (4.2. Efficient Mesh Extraction), temporal p. 6 (4.1. Aligning the Gaussians with the Surface), p. 3 (2. Related Work), p. 3 (2. Related Work), p. 4 (3. 3D Gaussian Splatting).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
