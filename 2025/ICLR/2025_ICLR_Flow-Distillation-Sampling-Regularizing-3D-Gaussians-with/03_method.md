# Method - Flow Distillation Sampling: Regularizing 3D Gaussians with Pre-trained Matching Priors

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=BzsjHiBfLk; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/113507. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3 METHOD), p. 4 (3 METHOD), p. 3 (3 METHOD)): Our FDS regulates the optimization of Gaussian radiance field by incorporating matching priors from the pretrained deep model.

## Method Body Digest

- **p. 3 / 3 METHOD - extractive body cue:** Our FDS regulates the optimization of Gaussian radiance field by incorporating matching priors from the pretrained deep model.
- **p. 4 / 3 METHOD - extractive body cue:** 3.2 FLOW DISTILLATION SAMPLING Given a collection of images {Ii}i=1,2,...N, Gaussian Radiance Field typically employs the following loss function for rendering optimization: L = 1
- **p. 3 / 3 METHOD - extractive body cue:** The generation of Radiance Flow and our proposed FDS loss, along with the equipped camera sampling scheme, are detailed in Sec.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our contributions are summarized as follows: • FDS leverages matching prior information to recover absolute scale, significantly enhancing the geometric quality of the Gaussian radiance ...
- **p. 4 / 3 METHOD - extractive body cue:** As mentioned above, we can project pixel x = (u1, v1) in m-th view image to the n-th view by its corresponding depth and their ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In addition, a camera sampling scheme is proposed to adaptively control the overlap between input view and sampled view for better Prior Flow calculation, which ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** To mitigate the issue, recent research efforts (Li et al., 2024; Paliwal et al., 2024; Turkulainen et al., 2025) have focused on incorporating geometric priors ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** 3D Gaussian Splatting (3DGS) (Kerbl et al., 2023) has been widely applied to the field of 3D reconstruction and rendering, including novel view synthesis of ...

## Design Rationale

- **p. 1 / 1 INTRODUCTION - extractive body cue:** In this paper, we introduce Flow Distillation Sampling (FDS), an online method for distilling matching prior from a pre-trained optical flow model into the 3DGS ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our contributions are summarized as follows: • FDS leverages matching prior information to recover absolute scale, significantly enhancing the geometric quality of the Gaussian radiance ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** 3D Gaussian Splatting (3DGS) (Kerbl et al., 2023) has been widely applied to the field of 3D reconstruction and rendering, including novel view synthesis of ...

## Source Evidence Cues

- **p. 3 / 3 METHOD - extractive body cue:** Our FDS regulates the optimization of Gaussian radiance field by incorporating matching priors from the pretrained deep model.
- **p. 4 / 3 METHOD - extractive body cue:** 3.2 FLOW DISTILLATION SAMPLING Given a collection of images {Ii}i=1,2,...N, Gaussian Radiance Field typically employs the following loss function for rendering optimization: L = 1
- **p. 3 / 3 METHOD - extractive body cue:** The generation of Radiance Flow and our proposed FDS loss, along with the equipped camera sampling scheme, are detailed in Sec.
- **Detected method headings:** 3 METHOD (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Our FDS regulates the optimization of Gaussian radiance field by incorporating matching priors from the pretrained deep model. | p. 3 (3 METHOD), p. 4 (3 METHOD) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | 3.2 FLOW DISTILLATION SAMPLING Given a collection of images {Ii}i=1,2,...N, Gaussian Radiance Field typically employs the following loss function for rendering optimization: ... | p. 4 (3 METHOD), p. 3 (3 METHOD) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | The generation of Radiance Flow and our proposed FDS loss, along with the equipped camera sampling scheme, are detailed in Sec. | p. 3 (3 METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3 METHOD - extractive body cue:** 3.2 FLOW DISTILLATION SAMPLING Given a collection of images {Ii}i=1,2,...N, Gaussian Radiance Field typically employs the following loss function for rendering optimization: L = 1
- **p. 3 / 3 METHOD - extractive body cue:** The generation of Radiance Flow and our proposed FDS loss, along with the equipped camera sampling scheme, are detailed in Sec.
- **p. 3 / 3 METHOD - extractive body cue:** Our FDS regulates the optimization of Gaussian radiance field by incorporating matching priors from the pretrained deep model.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (3 METHOD), p. 4 (3 METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | contributions, summarized, follows, FDS, leverages, matching, prior, information, recover, absolute, scale, significantly, enhancing, geometric | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | contributions, summarized, follows, FDS, leverages, matching, prior, information, recover, absolute | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | introduce, Flow, Distillation, Sampling, FDS, online, distilling, matching, prior, pre-trained | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | FLOW, DISTILLATION, SAMPLING, Given, collection, images, Gaussian, Radiance, Field, typically | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our contributions are summarized as follows: • FDS leverages matching prior information to recover absolute scale, significantly enhancing the geometric quality of the Gaussian radiance ...
- **p. 4 / 3 METHOD - extractive body cue:** As mentioned above, we can project pixel x = (u1, v1) in m-th view image to the n-th view by its corresponding depth and their ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In addition, a camera sampling scheme is proposed to adaptively control the overlap between input view and sampled view for better Prior Flow calculation, which ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** To mitigate the issue, recent research efforts (Li et al., 2024; Paliwal et al., 2024; Turkulainen et al., 2025) have focused on incorporating geometric priors ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** 3D Gaussian Splatting (3DGS) (Kerbl et al., 2023) has been widely applied to the field of 3D reconstruction and rendering, including novel view synthesis of ...
- **p. 3 / 3 METHOD - extractive body cue:** The generation of Radiance Flow and our proposed FDS loss, along with the equipped camera sampling scheme, are detailed in Sec.
- **p. 4 / 3 METHOD - extractive body cue:** Similarly, the depth of pixel x is rendered using alpha blending.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | In the future, we plan to explore the potential of FDS in monocular video reconstruction tasks, using only a single input image ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | The entire framework is implemented in PyTorch (Paszke et al., 2019), and all experiments are conducted on a single NVIDIA 4090D GPU. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3 METHOD - extractive body cue:** Our FDS regulates the optimization of Gaussian radiance field by incorporating matching priors from the pretrained deep model.
- **p. 8 / 4.2 RESULTS - extractive body cue:** On the Mushroom dataset, adding the FDS loss increases the training time by half an hour, which maintains the same level as baseline.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** FDS, regulates, optimization, Gaussian, radiance, field, incorporating, matching, priors, pretrained, deep, model, FLOW, DISTILLATION, SAMPLING, Given, collection, images, typically, employs.
- **Relevant PDF headings:** 3 METHOD (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | 4.1.2 DATASETS AND METRICS We evaluate our method for 3D reconstruction and novel view synthesis tasks on Mushroom (Ren et al., 2024), ... | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Semantic / temporal fusion | With the integration of FDS, the mesh quality is significantly enhanced compared to the baseline, featuring fewer floaters and more well-defined shapes. | p. 9 (4.2 RESULTS), p. 8 (4.2 RESULTS) |
| Robot query / planning handoff | We found that Sea Raft (Wang et al., 2024) outperforms Raft (Teed and Deng, 2020) on FDS, indicating that a better optical ... | p. 8 (4.2 RESULTS), p. 9 (4.2 RESULTS) |

## Failure and Ablation Link

- **p. 9 / 4.2 RESULTS - extractive body cue:** Ablation study on FDS: In this section, we present the design of our FDS method through an ablation study on the Mushroom dataset to validate ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** We removed the depth distortion loss in 2DGS because we found that it degrades its results in indoor scenes.
- **p. 9 / 4.2 RESULTS - extractive body cue:** Using Ii instead of Ci help us to remove the 9
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3. Comparison of depth reconstruction on Mushroom and ScanNet datasets. The original 3DGS or 2DGS model equipped with FDS can remove unwanted floaters and ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 4. Ablation study on FDS strategies. Mθ(X, Cs) Loss Metric X = Ci X = Ii Next Input view Sampled view
- **p. 10 / 4.2 RESULTS - extractive body cue:** For example, in the third row, we use the next training input view as the sampling view, and replace the render result of next training ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Explanation of depth-adaptive translation radius. A fixed-radius camera sampling scheme may result in significantly different flow values (Flow 1 and Flow 2) in ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3 METHOD), p. 4 (3 METHOD), p. 3 (3 METHOD), objective p. 4 (3 METHOD), p. 3 (3 METHOD), p. 3 (3 METHOD), temporal p. 10 (4.2 RESULTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 10 (4.2 RESULTS), p. 1 (1 INTRODUCTION), p. 3 (2 RELATED WORK).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
