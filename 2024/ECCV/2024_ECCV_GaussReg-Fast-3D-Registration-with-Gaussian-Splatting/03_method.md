# Method - GaussReg: Fast 3D Registration with Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/2380_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/02380.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 6 (3 Method), p. 7 (3 Method), p. 8 (3 Method), p. 6 (3 Method), p. 8 (3 Method), p. 7 (3 Method)): Our key idea is to first locate overlapping region between scene A and B and render some training images covering the region to support more precise geometric features for fine ...

## Method Body Digest

- **p. 6 / 3 Method - extractive body cue:** Our key idea is to first locate overlapping region between scene A and B and render some training images covering the region to support more ...
- **p. 7 / 3 Method - extractive body cue:** Without loss of generality, we use scene A as an example in the following description.
- **p. 8 / 3 Method - extractive body cue:** Our loss function mainly consists of two parts, depth loss and registration loss.
- **p. 6 / 3 Method - extractive body cue:** We apply two loss functions (overlap-aware circle loss and point matching loss) from the GeoTransformer [27] to constrain our coarse registration network.
- **p. 8 / 3 Method - extractive body cue:** Training Strategy and Loss Function Overlap Image Selection is not involved in the training of the fine registration network.
- **p. 7 / 3 Method - extractive body cue:** First, we input IA into a 2D CNN to get features RefA, {Srck A}n k=0, which turn into the cost volume CostA according to the ...
- **p. 5 / 3 Method - extractive body cue:**   {(  ,  )}  I3D Feature Extraction Superpoint Match Point Match 
- **p. 7 / 3 Method - extractive body cue:** Followed by the 3DCNN regularization, the probability volume PA ∈RD×H×W and feature volume FA ∈RC×D×H×W are obtained from the cost volumes, where C is the ...

## Design Rationale

- **p. 3 / 1 Introduction - extractive body cue:** The main contributions can be summarized as: • To the best of our knowledge, we are the first to explore the registration of 3D scenes ...
- **p. 3 / 1 Introduction - extractive body cue:** Ultimately, we propose a novel coarse-to-fine GS registration framework: GaussReg.
- **p. 2 / 1 Introduction - extractive body cue:** 1: The purpose of our method is to register scenes A and B with Gaussian Splatting [17] models, and then combine A with B to ...

## Source Evidence Cues

- **p. 6 / 3 Method - extractive body cue:** Our key idea is to first locate overlapping region between scene A and B and render some training images covering the region to support more ...
- **p. 7 / 3 Method - extractive body cue:** Without loss of generality, we use scene A as an example in the following description.
- **p. 8 / 3 Method - extractive body cue:** Our loss function mainly consists of two parts, depth loss and registration loss.
- **p. 6 / 3 Method - extractive body cue:** We apply two loss functions (overlap-aware circle loss and point matching loss) from the GeoTransformer [27] to constrain our coarse registration network.
- **p. 8 / 3 Method - extractive body cue:** Training Strategy and Loss Function Overlap Image Selection is not involved in the training of the fine registration network.
- **p. 7 / 3 Method - extractive body cue:** First, we input IA into a 2D CNN to get features RefA, {Srck A}n k=0, which turn into the cost volume CostA according to the ...
- **p. 5 / 3 Method - extractive body cue:**   {(  ,  )}  I3D Feature Extraction Superpoint Match Point Match 
- **Detected method headings:** 3 Method (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Our key idea is to first locate overlapping region between scene A and B and render some training images covering the region ... | p. 6 (3 Method), p. 7 (3 Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Without loss of generality, we use scene A as an example in the following description. | p. 7 (3 Method), p. 8 (3 Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Our loss function mainly consists of two parts, depth loss and registration loss. | p. 8 (3 Method), p. 6 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 7 / 3 Method - extractive body cue:** Followed by the 3DCNN regularization, the probability volume PA ∈RD×H×W and feature volume FA ∈RC×D×H×W are obtained from the cost volumes, where C is the ...
- **p. 8 / 3 Method - extractive body cue:** Depth loss is a cross-entropy loss to supervise the probability volume: \labe l
- **p. 6 / 3 Method - extractive body cue:** We apply two loss functions (overlap-aware circle loss and point matching loss) from the GeoTransformer [27] to constrain our coarse registration network.
- **p. 6 / 3 Method - extractive body cue:** 3.3 Image-Guided Fine Registration Since the GS model doesn't impose specific geometric constraints during training, resulting point clouds may exhibit some distortion.
- **p. 7 / 3 Method - extractive body cue:** Without loss of generality, we use scene A as an example in the following description.
- **p. 8 / 3 Method - extractive body cue:** Our loss function mainly consists of two parts, depth loss and registration loss.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 6 (3 Method), p. 6 (3 Method), p. 7 (3 Method), p. 8 (3 Method), p. 8 (3 Method), p. 7 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | coarse, registration, accepts, PointsA, PointsB, input, output, transformation, Training, Strategy, Loss, Function, Due, scale | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | coarse, registration, accepts, PointsA, PointsB, input, output, transformation, Training, Strategy | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | main, contributions, summarized, best, knowledge, first, explore, registration, scenes, considering | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Followed, DCNN, regularization, probability, volume, feature, obtained, cost, volumes, where | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3 Method - extractive body cue:** The coarse registration accepts PointsA and PointsB as input, and output a coarse transformation {sc, Rc, Tc}.
- **p. 6 / 3 Method - extractive body cue:** Training Strategy and Loss Function Due to the scale uncertainty in monocular video reconstruction, we performed data augmentation not only on rotation and translation but ...
- **p. 7 / 3 Method - extractive body cue:** Image-Guided 3D Feature Extraction As shown in Figure 3, we adopt the principle of multi-view stereo (MVS) to estimate depth and extract volumetric features.
- **p. 6 / 3 Method - extractive body cue:** Even though we normalized the scale of input point clouds within a certain range, such data augmentation still preserves the diversity of relative scale differences.
- **p. 5 / 3 Method - extractive body cue:** After that, an Image-Guided 3D (I3D) Feature Extraction is adopted to obtain volumetric features from images, which are used for subsequent matching, achieving the final ...
- **p. 7 / 3 Method - extractive body cue:** Under the selected cameras, the image sets IA and IB are rendered from GaussianA and GaussianB to be fed into the next feature extraction stage.
- **p. 2 / 1 Introduction - extractive body cue:** The mainstream methods typically involve extracting features from point clouds and locating matching points to calculate the transformation between the two input scenes.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Specifically, in Figure 2, our Image-Guided Fine Registration primarily involves two steps: 1) Efficiently and accurately selecting highly overlapping cameras and rendering ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Our selection follows 3 steps: 1) For every pair (Ca i , ˆCb j), we calculate the cosine value of the angle ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Our selection follows 3 steps: 1) For every pair (Ca i , ˆCb j), we calculate the cosine value of the angle ... | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 3 Method - extractive body cue:** Our key idea is to first locate overlapping region between scene A and B and render some training images covering the region to support more ...
- **p. 6 / 3 Method - extractive body cue:** We apply two loss functions (overlap-aware circle loss and point matching loss) from the GeoTransformer [27] to constrain our coarse registration network.
- **p. 8 / 3 Method - extractive body cue:** Training Strategy and Loss Function Overlap Image Selection is not involved in the training of the fine registration network.
- **p. 11 / 4 Experiment - extractive body cue:** Both networks are trained separately for 40 epochs with a batch size of 1.
- **p. 10 / 4 Experiment - extractive body cue:** Implementation Details Our GaussReg is merely trained on the ScanNetGSReg training set and evaluated on the ScanNet-GSReg test set, Objaverse test set, and GSReg dataset.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** idea, first, locate, overlapping, region, between, scene, render, some, training, images, covering, support, more, precise, geometric, features, fine, alignment, Without.
- **Relevant PDF headings:** 3 Method (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Furthermore, to validate the generalization of our method, we collected 10 real-world scenes for testing, called GSReg dataset, which includes 6 indoor ... | p. 10 (4 Experiment), p. 10 (4 Experiment) |
| Semantic / temporal fusion | Therefore, we select the current SOTA method, HLoc [28] (SuperPoint [10] + SuperGlue [29]), as the baseline for comparison on ScanNet. | p. 11 (4 Experiment), p. 12 (4 Experiment) |
| Robot query / planning handoff | Moreover, our method (ours) significantly outperforms our coarse registration (ours w./o. fine), proving the effectiveness of our fine registration. | p. 12 (4 Experiment), p. 11 (4 Experiment) |

## Failure and Ablation Link

- **p. 12 / 4 Experiment - extractive body cue:** 4.3 Ablation Study To deeply analyze GaussReg, we conduct detailed ablation studies on the ScanNetGSReg dataset to evaluate the effectiveness of the proposed components.
- **p. 12 / 4 Experiment - extractive body cue:** As shown in Table 2, our method achieves registration results close to HLoc without fine-tuning, proving the strong generalizability of our approach.
- **p. 13 / 4 Experiment - extractive body cue:** GaussReg 13 Table 5: Ablation study with different k in overlap image selection on ScanNetGSReg. ↓means lower is better.
- **p. 13 / 4 Experiment - extractive body cue:** I3D 3.169 0.036 0.061 0.066 6 Ours 2.827 0.042 0.032 0.080 As shown in Table 6, in Index-5, we remove the image-guided 3D (I3D) feature ...
- **p. 13 / 5 Discussion - extractive body cue:** Limitations and Future Work We only adopt a simple strategy to fuse and filter two GS models.
- **p. 11 / 4 Experiment - extractive body cue:** For indoor scenes in ScanNetGSReg, SuperPoint [10] sometimes fails to extract effective keypoints, leading to registration failures.
- **p. 13 / 5 Discussion - extractive body cue:** Future work can further explore to address this issue.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 6 (3 Method), p. 7 (3 Method), p. 8 (3 Method), p. 6 (3 Method), p. 8 (3 Method), p. 7 (3 Method), objective p. 7 (3 Method), p. 8 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 7 (3 Method), p. 8 (3 Method), temporal p. 6 (3 Method), p. 7 (3 Method), p. 7 (3 Method), p. 9 (4 Experiment), p. 9 (4 Experiment), p. 10 (4 Experiment).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
