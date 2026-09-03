# Method - NeuS: Learning Neural Implicit Surfaces by Volume Rendering for Multi-view Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2106.10689; PDF retrieval source: https://arxiv.org/pdf/2106.10689. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3 Method), p. 7 (3 Method), p. 4 (3 Method), p. 4 (3 Method), p. 3 (3 Method), p. 6 (3 Method)): (1) In order to apply a volume rendering method to training the SDF network, we first introduce a probability density function φs(f(x)), called S-density, where f(x), x ∈R3, is the ...

## Method Body Digest

- **p. 3 / 3 Method - extractive body cue:** (1) In order to apply a volume rendering method to training the SDF network, we first introduce a probability density function φs(f(x)), called S-density, where ...
- **p. 7 / 3 Method - extractive body cue:** (15) Same as IDR[49], we empirically choose R as L1 loss, which in our observation is robust to outliers and stable in training.
- **p. 4 / 3 Method - extractive body cue:** Note that the standard deviation of φs(x) is given by 1/s, which is also a trainable parameter, that is, 1/s approaches to zero as the ...
- **p. 4 / 3 Method - extractive body cue:** Upon successful minimization of a loss function based on this supervision, the zero-level set of the network-encoded SDF is expected to represent an accurately reconstructed ...
- **p. 3 / 3 Method - extractive body cue:** 3.1 Rendering Procedure Scene representation.
- **p. 6 / 3 Method - extractive body cue:** The following theorem states that in general cases (i.e., including both single surface intersection and multiple surface intersections) the weight function defined by Eqn.
- **p. 7 / 3 Method - extractive body cue:** The loss function is defined as L = Lcolor + λLreg + βLmask.
- **p. 7 / 3 Method - extractive body cue:** (16) The optional mask loss Lmask is defined as Lmask = BCE(Mk, ˆOk), (17) where ˆOk = Pn i=1 Tk,iαk,i is the sum of weights ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** Therefore we propose a novel volume rendering scheme to ensure unbiased surface reconstruction in the first-order approximation of SDF.
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we present a new neural rendering scheme, called NeuS, for multi-view surface reconstruction.
- **p. 3 / 1 Introduction - extractive body cue:** On the contrary, our method performs well for such challenging cases without the need of masks.

## Source Evidence Cues

- **p. 3 / 3 Method - extractive body cue:** (1) In order to apply a volume rendering method to training the SDF network, we first introduce a probability density function φs(f(x)), called S-density, where ...
- **p. 7 / 3 Method - extractive body cue:** (15) Same as IDR[49], we empirically choose R as L1 loss, which in our observation is robust to outliers and stable in training.
- **p. 4 / 3 Method - extractive body cue:** Note that the standard deviation of φs(x) is given by 1/s, which is also a trainable parameter, that is, 1/s approaches to zero as the ...
- **p. 4 / 3 Method - extractive body cue:** Upon successful minimization of a loss function based on this supervision, the zero-level set of the network-encoded SDF is expected to represent an accurately reconstructed ...
- **p. 3 / 3 Method - extractive body cue:** 3.1 Rendering Procedure Scene representation.
- **p. 6 / 3 Method - extractive body cue:** The following theorem states that in general cases (i.e., including both single surface intersection and multiple surface intersections) the weight function defined by Eqn.
- **p. 7 / 3 Method - extractive body cue:** The loss function is defined as L = Lcolor + λLreg + βLmask.
- **Detected method headings:** 3 Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | (1) In order to apply a volume rendering method to training the SDF network, we first introduce a probability density function φs(f(x)), ... | p. 3 (3 Method), p. 7 (3 Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | (15) Same as IDR[49], we empirically choose R as L1 loss, which in our observation is robust to outliers and stable in ... | p. 7 (3 Method), p. 4 (3 Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Note that the standard deviation of φs(x) is given by 1/s, which is also a trainable parameter, that is, 1/s approaches to ... | p. 4 (3 Method), p. 4 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3 Method - extractive body cue:** Upon successful minimization of a loss function based on this supervision, the zero-level set of the network-encoded SDF is expected to represent an accurately reconstructed ...
- **p. 7 / 3 Method - extractive body cue:** (16) The optional mask loss Lmask is defined as Lmask = BCE(Mk, ˆOk), (17) where ˆOk = Pn i=1 Tk,iαk,i is the sum of weights ...
- **p. 3 / 3 Method - extractive body cue:** In order to learn the weights of the neural network, we developed a novel volume rendering method to render images from the implicit SDF and ...
- **p. 6 / 3 Method - extractive body cue:** sides of this equation yields T(t) = Φs(f(p(t))).
- **p. 6 / 3 Method - extractive body cue:** (10) Based on this equation, the weight function w(t) can be computed with standard volume rendering as in Eqn.
- **p. 7 / 3 Method - extractive body cue:** The loss function is defined as L = Lcolor + λLreg + βLmask.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 7 (3 Method), p. 7 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | order, learn, weights, neural, network, developed, novel, volume, rendering, render, images, implicit, SDF, minimize | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | order, learn, weights, neural, network, developed, novel, volume, rendering, render | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Therefore, novel, volume, rendering, scheme, ensure, unbiased, surface, reconstruction, first-order | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Upon, successful, minimization, loss, function, supervision, zero-level, network-encoded, SDF, expected | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3 Method - extractive body cue:** In order to learn the weights of the neural network, we developed a novel volume rendering method to render images from the implicit SDF and ...
- **p. 4 / 3 Method - extractive body cue:** Intuitively, the main idea of NeuS is that, with the aid of the S-density field φs(f(x)), volume rendering is used to train the SDF network ...
- **p. 4 / 3 Method - extractive body cue:** The key to learn an accurate SDF representation from 2D images is to build an appropriate connection between output colors and SDF, i.e., to derive ...
- **p. 2 / 1 Introduction - extractive body cue:** Point- and surface-based reconstruction methods estimate the depth map of each pixel by exploiting inter-image photometric consistency [8] and then fuse the depth maps into ...
- **p. 3 / 3 Method - extractive body cue:** Given a set of posed images {Ik} of a 3D object, our goal is to reconstruct the surface S of it.
- **p. 1 / 1 Introduction - extractive body cue:** To train their neural models, these methods use a differentiable surface rendering method to render a 3D object into images and compare them against input ...
- **p. 2 / 1 Introduction - extractive body cue:** This volume rendering approach samples multiple points along each ray and perform α-composition of the colors of the sampled points to produce the output pixel ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | 4 using the framework of volume rendering. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Some methods enforce 3D understanding in a deep learning framework by introducing inductive biases. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | We sample 512 rays per batch and train our model for 300k iterations for 14 hours (for the ‘w/ mask' setting) and ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3 Method - extractive body cue:** (1) In order to apply a volume rendering method to training the SDF network, we first introduce a probability density function φs(f(x)), called S-density, where ...
- **p. 7 / 3 Method - extractive body cue:** (15) Same as IDR[49], we empirically choose R as L1 loss, which in our observation is robust to outliers and stable in training.
- **p. 4 / 3 Method - extractive body cue:** Note that the standard deviation of φs(x) is given by 1/s, which is also a trainable parameter, that is, 1/s approaches to zero as the ...
- **p. 8 / 4 Experiments - extractive body cue:** We sample 512 rays per batch and train our model for 300k iterations for 14 hours (for the ‘w/ mask' setting) and 16 hours (for ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** order, apply, volume, rendering, training, SDF, network, first, introduce, probability, density, function, called, S-density, where, signed, distance, Same, IDR, empirically.
- **Relevant PDF headings:** 3 Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We further tested on 7 challenging scenes from the low-res set of the BlendedMVS dataset [48](CC-4 License). | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Semantic / temporal fusion | (1) The state-of-the-art surface rendering approach - IDR [49]: IDR can reconstruct surface with high quality but requires foreground masks as supervision; ... | p. 7 (4 Experiments), p. 8 (4 Experiments) |
| Robot query / planning handoff | COLMAP results are achieved by trim=0. | p. 8 (4 Experiments), p. 8 (4 Experiments) |

## Failure and Ablation Link

- **p. 9 / 4 Experiments - extractive body cue:** To evaluate the effect of the weight calculation, we test three different kinds of weight constructions described in Sec.
- **p. 10 / 4 Experiments - extractive body cue:** We also studied the effect of Eikonal regularization [10] and geometric initialization [1].
- **p. 7 / 4 Experiments - extractive body cue:** Each scene was tested with and without foreground masks provided by IDR [49].
- **p. 8 / 4 Experiments - extractive body cue:** 4.2 Comparisons We conducted the comparisons in two settings, with mask supervision (w/ mask) and without mask supervision (w/o mask).
- **p. 9 / 4 Experiments - extractive body cue:** (e) Full Model Reference Image Chamfer Distance 0.59 0.62 1.49 (a) Naive Solution (b) Direct Solution 4.45 (c) w/o Eikonal 0.64 MAE 6.19 0.93 44.34 ...
- **p. 10 / 4 Experiments - extractive body cue:** Without Eikonal regularization or geometric initialization, the result on Chamfer distance is on par with that of the full model.
- **p. 20 / Figure/Table caption - extractive body cue:** Table 4: Quantitative comparisons with NeRF on the task of novel view synthesis without mask supervision. E.2 Novel View Synthesis In this experiment, we held ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3 Method), p. 7 (3 Method), p. 4 (3 Method), p. 4 (3 Method), p. 3 (3 Method), p. 6 (3 Method), objective p. 4 (3 Method), p. 7 (3 Method), p. 3 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 7 (3 Method), temporal p. 5 (3 Method), p. 3 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
