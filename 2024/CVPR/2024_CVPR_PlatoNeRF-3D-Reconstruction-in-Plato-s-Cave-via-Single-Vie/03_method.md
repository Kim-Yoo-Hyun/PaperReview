# Method - PlatoNeRF: 3D Reconstruction in Plato's Cave via Single-View Two-Bounce Lidar

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Klinghoffer_PlatoNeRF_3D_Reconstruction_in_Platos_Cave_via_Single-View_Two-Bounce_Lidar_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Klinghoffer_PlatoNeRF_3D_Reconstruction_in_Platos_Cave_via_Single-View_Two-Bounce_Lidar_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3.3. Implementation Details), p. 5 (3.3. Implementation Details)): As in NeRF, we use the Adam optimizer [15] and set an initial learning rate of 5 × 10-4, which decays exponentially over training.

## Method Body Digest

- **p. 5 / 3.3. Implementation Details - extractive body cue:** As in NeRF, we use the Adam optimizer [15] and set an initial learning rate of 5 × 10-4, which decays exponentially over training.
- **p. 5 / 3.3. Implementation Details - extractive body cue:** For the first 25,000 iterations of training, β is set to 0.
- **p. 5 / 3.3. Implementation Details - extractive body cue:** After 25,000 iterations, when an accurate initial estimate of the virtual detector xp is obtained, we set β to 1/6,000 in most experiments to encourage ...
- **p. 3 / 3.1. Notations and Problem Definition - extractive body cue:** Because l is modeled as a point light source, we neglect any diffraction effects and soft shadows that are common with area sources.
- **p. 5 / 3.3. Implementation Details - extractive body cue:** Our method requires five inputs per pixel: (1) sensor location op = xs and ray direction dp, (2) laser location xl, (3) distance from the ...
- **p. 1 / 1. Introduction - extractive body cue:** Approaches such as diffusion, generative adversarial networks, and transformers rely on data priors to exploit correlations between observations and a large corpus of training data.
- **p. 2 / 1. Introduction - extractive body cue:** While traditional lidar systems only exploit the first bounce of light from the scene back to the sensor, providing accurate absolute depth, recent work has ...
- **p. 3 / 3.1. Notations and Problem Definition - extractive body cue:** The lidar system consists of a SPAD sensor and pulsed laser at known positions xs and xl respectively.

## Design Rationale

- **p. 4 / 3.1. Notations and Problem Definition - extractive body cue:** Our method consists of three steps.
- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, using lidar allows our method to operate with higher ambient light and lower scene albedo than RGB methods that exploit shadows.
- **p. 2 / 1. Introduction - extractive body cue:** We use this data to evaluate our method and our baselines.

## Source Evidence Cues

- **p. 5 / 3.3. Implementation Details - extractive body cue:** As in NeRF, we use the Adam optimizer [15] and set an initial learning rate of 5 × 10-4, which decays exponentially over training.
- **p. 5 / 3.3. Implementation Details - extractive body cue:** For the first 25,000 iterations of training, β is set to 0.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | As in NeRF, we use the Adam optimizer [15] and set an initial learning rate of 5 × 10-4, which decays exponentially ... | p. 5 (3.3. Implementation Details), p. 5 (3.3. Implementation Details) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | For the first 25,000 iterations of training, β is set to 0. | p. 5 (3.3. Implementation Details) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | As in NeRF, we use the Adam optimizer [15] and set an initial learning rate of 5 × 10-4, which decays exponentially ... | p. 5 (3.3. Implementation Details) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.3. Implementation Details - extractive body cue:** After 25,000 iterations, when an accurate initial estimate of the virtual detector xp is obtained, we set β to 1/6,000 in most experiments to encourage ...
- **p. 5 / 3.3. Implementation Details - extractive body cue:** As in NeRF, we use the Adam optimizer [15] and set an initial learning rate of 5 × 10-4, which decays exponentially over training.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3.3. Implementation Details).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Because, modeled, point, light, source, neglect, diffraction, effects, soft, shadows, common, area, sources, requires | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Because, modeled, point, light, source, neglect, diffraction, effects, soft, shadows | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | consists, three, steps, Furthermore, lidar, allows, operate, higher, ambient, light | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | After, iterations, when, accurate, initial, estimate, virtual, detector, obtained, most | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.1. Notations and Problem Definition - extractive body cue:** Because l is modeled as a point light source, we neglect any diffraction effects and soft shadows that are common with area sources.
- **p. 5 / 3.3. Implementation Details - extractive body cue:** Our method requires five inputs per pixel: (1) sensor location op = xs and ray direction dp, (2) laser location xl, (3) distance from the ...
- **p. 1 / 1. Introduction - extractive body cue:** Approaches such as diffusion, generative adversarial networks, and transformers rely on data priors to exploit correlations between observations and a large corpus of training data.
- **p. 2 / 1. Introduction - extractive body cue:** While traditional lidar systems only exploit the first bounce of light from the scene back to the sensor, providing accurate absolute depth, recent work has ...
- **p. 3 / 3.1. Notations and Problem Definition - extractive body cue:** The lidar system consists of a SPAD sensor and pulsed laser at known positions xs and xl respectively.
- **p. 4 / 3.1. Notations and Problem Definition - extractive body cue:** The one-bounce and twobounce signals provide information about objects that are visible to the sensor, and the shadows provide information about occluded portions of the ...
- **p. 2 / 1. Introduction - extractive body cue:** predict relative depth, rather than absolute depth, which is important for many applications.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Then, we share our results, comparisons, and ablations on spatial and temporal resolution, ambient light, low-albedo backgrounds, non-planar backgrounds, and number of ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Our scene is measured using a 512×512 SPAD with a temporal resolution of 128 ps (3.84 cm). | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Our scene is measured using a 512×512 SPAD with a temporal resolution of 128 ps (3.84 cm). | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.3. Implementation Details - extractive body cue:** As in NeRF, we use the Adam optimizer [15] and set an initial learning rate of 5 × 10-4, which decays exponentially over training.
- **p. 5 / 3.3. Implementation Details - extractive body cue:** For the first 25,000 iterations of training, β is set to 0.
- **p. 5 / 3.3. Implementation Details - extractive body cue:** As in NeRF, we use the Adam optimizer [15] and set an initial learning rate of 5 × 10-4, which decays exponentially over training.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** NeRF, Adam, optimizer, initial, learning, rate, decays, exponentially, over, training, first, iterations, After, when, accurate, estimate, virtual, detector, obtained, most.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We create datasets of four scenes of a room with either a chair, bunny, dragon, or occluded bunny in a chair, shown ... | p. 5 (4.1. Datasets), p. 5 (4. Experiments) |
| Semantic / temporal fusion | Figure 5. Real-World Results. (a) Captured scene (stars are illumi- nation spots), (b) BF Lidar result, (c) PlatoNeRF result. Our method yields ... | p. 7 (Figure/Table caption), p. 7 (4.3. Ablations) |
| Robot query / planning handoff | PlatoNeRF method achieves competitive performance. | p. 7 (4.2. Results), p. 7 (4.2. Results) |

## Failure and Ablation Link

- **p. 5 / 4. Experiments - extractive body cue:** Then, we share our results, comparisons, and ablations on spatial and temporal resolution, ambient light, low-albedo backgrounds, non-planar backgrounds, and number of illumination points.
- **p. 6 / 4.2. Results - extractive body cue:** We compare our work with two methods, one that uses two-bounce lidar for single-view 3D reconstruction without learning and one that uses shadows measured by ...
- **p. 7 / 4.3. Ablations - extractive body cue:** All ablations are done on the chair scene.
- **p. 8 / 4.3. Ablations - extractive body cue:** For our illumination spot ablation, we reduce Figure 6.
- **p. 8 / 4.3. Ablations - extractive body cue:** Quantitative results for these ablations are reported in Tab.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Ablations on Lidar Sensor. Lidars on consumer devices have lower spatial- and temporal-resolution than research-grade lidars. We ablate the impact of these sensor ...
- **p. 8 / 5. Conclusion - extractive body cue:** Our method has a couple limitations.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3.3. Implementation Details), p. 5 (3.3. Implementation Details), objective p. 5 (3.3. Implementation Details), p. 5 (3.3. Implementation Details), temporal p. 5 (4. Experiments), p. 6 (4.1. Datasets), p. 7 (4.3. Ablations), p. 7 (4.3. Ablations), p. 8 (4.3. Ablations), p. 8 (4.3. Ablations).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
