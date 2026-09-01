# Method - Semantically Consistent Language Gaussian Splatting for 3D Point-Level Open-Vocabulary Querying

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html; PDF retrieval source: https://arxiv.org/pdf/2503.21767. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (IV. METHOD), p. 5 (IV. METHOD), p. 5 (IV. METHOD), p. 4 (IV. METHOD)): This is done by masking out the image It using the extracted masklet and then passing it to CLIP's image encoder: ¯ϕr = T X t=1 ωt · CLIPimg(It ⊙˜Sr[t]), ...

## Method Body Digest

- **p. 4 / IV. METHOD - extractive PDF cue:** This is done by masking out the image It using the extracted masklet and then passing it to CLIP's image encoder: ¯ϕr = T X ...
- **p. 5 / IV. METHOD - extractive PDF cue:** Given the CLIP feature of a text query q ∈R512, we first apply a low threshold to filter out invalid prompts.
- **p. 5 / IV. METHOD - extractive PDF cue:** We then retrieve the most similar average feature (GT for distillation) over all regions feature ¯ϕ∗ r ≜ arg max r∈{r′/Cos( ¯ϕ′r,q)≥threshold} Cos(¯ϕr, q).
- **p. 4 / IV. METHOD - extractive PDF cue:** IT ] with camera poses, we aim to construct a better ground-truth feature LOurs t for each of the frames to train LangSplat's parameters by ...
- **p. 4 / IV. METHOD - extractive PDF cue:** III, a tracking module takes a sequence of images and regions of interest as input to track masks of the same region.
- **p. 4 / IV. METHOD - extractive PDF cue:** If the proposed region has not been tracked, we run the tracking model and add the output masklets to the set of tracked masklets ˜S1:T ...
- **p. 2 / III. PRELIMINARIES - extractive PDF cue:** This language embedding can then be rendered into a language field ˆLπ ∈RH×W ×D, where H and W correspond to the height and width of ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Querying open-vocabulary objects in 3D scenes, i.e., identifying and isolating scene components based on natural language descriptions, is a fundamental capability necessary to advance robotic ...

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Our contributions are as follows: • We introduce tracking for generating semantic and 3DarXiv:2503.21767v2 [cs.CV] 26 Sep 2025
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** We observe that it does not have a consistent optimal threshold for all queries. consistent ground-truth to train language-aware Gaussians, which improves the distillation quality. ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** To mitigate this difficulty, we propose a novel Ground-Truth Anchored (GT-Anchored) querying method, which computes the threshold relative to, "anchored", ground-truth (GT) used in the ...

## Source Evidence Cues

- **p. 4 / IV. METHOD - extractive PDF cue:** This is done by masking out the image It using the extracted masklet and then passing it to CLIP's image encoder: ¯ϕr = T X ...
- **p. 5 / IV. METHOD - extractive PDF cue:** Given the CLIP feature of a text query q ∈R512, we first apply a low threshold to filter out invalid prompts.
- **p. 5 / IV. METHOD - extractive PDF cue:** We then retrieve the most similar average feature (GT for distillation) over all regions feature ¯ϕ∗ r ≜ arg max r∈{r′/Cos( ¯ϕ′r,q)≥threshold} Cos(¯ϕr, q).
- **p. 4 / IV. METHOD - extractive PDF cue:** IT ] with camera poses, we aim to construct a better ground-truth feature LOurs t for each of the frames to train LangSplat's parameters by ...
- **Detected method headings:** IV. METHOD (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | This is done by masking out the image It using the extracted masklet and then passing it to CLIP's image encoder: ¯ϕr ... | p. 4 (IV. METHOD), p. 5 (IV. METHOD) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Given the CLIP feature of a text query q ∈R512, we first apply a low threshold to filter out invalid prompts. | p. 5 (IV. METHOD), p. 5 (IV. METHOD) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | We then retrieve the most similar average feature (GT for distillation) over all regions feature ¯ϕ∗ r ≜ arg max r∈{r′/Cos( ¯ϕ′r,q)≥threshold} ... | p. 5 (IV. METHOD), p. 4 (IV. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / IV. METHOD - extractive PDF cue:** IT ] with camera poses, we aim to construct a better ground-truth feature LOurs t for each of the frames to train LangSplat's parameters by ...
- **p. 5 / IV. METHOD - extractive PDF cue:** We then retrieve the most similar average feature (GT for distillation) over all regions feature ¯ϕ∗ r ≜ arg max r∈{r′/Cos( ¯ϕ′r,q)≥threshold} Cos(¯ϕr, q).
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (IV. METHOD), p. 5 (IV. METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | III, tracking, module, takes, sequence, images, regions, interest, input, track, masks, same, region, been | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | III, tracking, module, takes, sequence, images, regions, interest, input, track | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | contributions, follows, introduce, tracking, generating, semantic, DarXiv, Sep, observe, does | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | camera, poses, construct, better, ground-truth, feature, LOurs, frames, train, LangSplat | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / IV. METHOD - extractive PDF cue:** III, a tracking module takes a sequence of images and regions of interest as input to track masks of the same region.
- **p. 4 / IV. METHOD - extractive PDF cue:** If the proposed region has not been tracked, we run the tracking model and add the output masklets to the set of tracked masklets ˜S1:T ...
- **p. 2 / III. PRELIMINARIES - extractive PDF cue:** This language embedding can then be rendered into a language field ˆLπ ∈RH×W ×D, where H and W correspond to the height and width of ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Querying open-vocabulary objects in 3D scenes, i.e., identifying and isolating scene components based on natural language descriptions, is a fundamental capability necessary to advance robotic ...
- **p. 3 / III. PRELIMINARIES - extractive PDF cue:** IV-A, we present a masklet extraction algorithm (Alg.
- **p. 2 / III. PRELIMINARIES - extractive PDF cue:** Let ˆLπt denote the rendering of the scene from the camera pose πt associated with image It.
- **p. 3 / III. PRELIMINARIES - extractive PDF cue:** OpenGaussian [29] proposes to directly query the 3D Gaussians with natural language.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Constructing consistent language supervision Given a sequence of frames [I1, . . . | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | These results validate our framework as a promising step toward open-vocabulary understanding in realworld robotic systems. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | As in LangSplat, to reduce the GPU memory usage, we train a light-weight autoencoder consisting of an encoder E and a decoder ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Pretraining the standard 3D Gaussian Splatting takes 30,000 steps. | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / IV. METHOD - extractive PDF cue:** IT ] with camera poses, we aim to construct a better ground-truth feature LOurs t for each of the frames to train LangSplat's parameters by ...
- **p. 6 / V. EXPERIMENTS - extractive PDF cue:** Pretraining the standard 3D Gaussian Splatting takes 30,000 steps.
- **p. 5 / IV. METHOD - extractive PDF cue:** As in LangSplat, to reduce the GPU memory usage, we train a light-weight autoencoder consisting of an encoder E and a decoder D.
- **p. 5 / IV. METHOD - extractive PDF cue:** With the retrieved GT ¯ϕ∗ r, we compress it into lower dimension with the pretrained encoder E.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** done, masking, image, extracted, masklet, then, passing, CLIP, encoder, CLIPimg, where, denotes, represented, tensor, ratio, pixels, total, pixel, count, Given.
- **Relevant PDF headings:** IV. METHOD (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Following LangSplat [23], we conduct experiments on the further annotated LERF [12] dataset that contains a set of in-the-wild scenes and on ... | p. 5 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |
| Semantic / temporal fusion | Acc, significantly outperforming baseline methods. | p. 7 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Robot query / planning handoff | We observe that Ours consistently outperforms LangSplat-m and, on average, is better than OpenGaussian, achieving an improvement of +4.14 in mIoU and ... | p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 7 / V. EXPERIMENTS - extractive PDF cue:** We also studied the effectiveness of our method without DBSCAN [5] and evaluated the performance of canonical querying from LERF [12] on the task of ...
- **p. 7 / V. EXPERIMENTS - extractive PDF cue:** We conduct ablation studies to validate the efficacy of each proposed component of our method and report the performance in Tab.
- **p. 6 / V. EXPERIMENTS - extractive PDF cue:** Pretraining the standard 3D Gaussian Splatting takes 30,000 steps.
- **p. 7 / V. EXPERIMENTS - extractive PDF cue:** Note that all four methods encounter a common failure mode of empty query, i.e., no valid Gaussians are returned for a text query, resulting in ...
- **p. 6 / V. EXPERIMENTS - extractive PDF cue:** Acc, a query is considered correct if the center of the queried mask's exterior bounding box falls within the bounding box of the ground-truth.
- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 2: IoU metric per query vs. cosine similarity thresholds for the standard querying method. We observe that it does not have a consistent optimal ...
- **p. 5 / IV. METHOD - extractive PDF cue:** (11) As ¯ϕr is obtained as a weighted average of CLIP image embeddings and q comes from CLIP text embeddings, a direct comparison between them ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (IV. METHOD), p. 5 (IV. METHOD), p. 5 (IV. METHOD), p. 4 (IV. METHOD), objective p. 4 (IV. METHOD), p. 5 (IV. METHOD), temporal p. 4 (IV. METHOD), p. 1 (Abstract), p. 4 (IV. METHOD), p. 5 (IV. METHOD), p. 5 (IV. METHOD), p. 6 (V. EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
