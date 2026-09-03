# Method - Open-Vocabulary 3D Semantic Segmentation with Text-to-Image Diffusion Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/4252_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/04252.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (1 Introduction), p. 4 (X. Zhu et al), p. 1 (4 HKUST), p. 3 (1 Introduction), p. 8 (X. Zhu et al), p. 2 (1 Introduction)): In summary, we make the following contributions: - To the best of our knowledge, we are the first to leverage text-image diffusion to perform open-vocabulary 3D semantic segmentation. - We ...

## Method Body Digest

- **p. 3 / 1 Introduction - extractive body cue:** In summary, we make the following contributions: - To the best of our knowledge, we are the first to leverage text-image diffusion to perform open-vocabulary ...
- **p. 4 / X. Zhu et al - extractive body cue:** (b) Directly using a 3D mask proposal network trained on labeled 3D data to produce class-agnostic masks, and then pool corresponding representations from the CLIP ...
- **p. 1 / 4 HKUST - extractive body cue:** We propose a novel method, namely Diff2Scene, which leverages frozen representations from text-image generative models, along with salient-aware and geometric-aware masks, for open-vocabulary 3D semantic ...
- **p. 3 / 1 Introduction - extractive body cue:** The frozen features extracted from the decoder of the U-Net in the diffusion model are trained with generative objectives, and cannot be directly used for ...
- **p. 8 / X. Zhu et al - extractive body cue:** It serves as an implicit distillation objective to make the 3D model learn high-resolution, semantically-rich feature representations.
- **p. 2 / 1 Introduction - extractive body cue:** These lifted feature representations for 3D points can then be used to query with open-vocabulary descriptions, achieving semantic understanding in 3D.
- **p. 7 / X. Zhu et al - extractive body cue:** First of all, our 2D semantic understanding model uses a mask-based segmentation head which does not provide semantically-rich features in the pixel level.
- **p. 4 / X. Zhu et al - extractive body cue:** LP D and LMD denote point-based distillation loss and mask-based distillation loss.

## Design Rationale

- **p. 3 / 1 Introduction - extractive body cue:** In summary, we make the following contributions: - To the best of our knowledge, we are the first to leverage text-image diffusion to perform open-vocabulary ...
- **p. 3 / 1 Introduction - extractive body cue:** To mitigate these issues, we propose a novel mask distillation method tailored to distill knowledge from the Mask2Former style 2D branch [10, 87] to the ...
- **p. 1 / 4 HKUST - extractive body cue:** We propose Diff2Scene, a 3D model that performs open-vocabulary semantic segmentation and visual grounding tasks given novel text prompts, without relying on any annotated 3D ...

## Source Evidence Cues

- **p. 3 / 1 Introduction - extractive body cue:** In summary, we make the following contributions: - To the best of our knowledge, we are the first to leverage text-image diffusion to perform open-vocabulary ...
- **p. 4 / X. Zhu et al - extractive body cue:** (b) Directly using a 3D mask proposal network trained on labeled 3D data to produce class-agnostic masks, and then pool corresponding representations from the CLIP ...
- **p. 1 / 4 HKUST - extractive body cue:** We propose a novel method, namely Diff2Scene, which leverages frozen representations from text-image generative models, along with salient-aware and geometric-aware masks, for open-vocabulary 3D semantic ...
- **p. 3 / 1 Introduction - extractive body cue:** The frozen features extracted from the decoder of the U-Net in the diffusion model are trained with generative objectives, and cannot be directly used for ...
- **p. 8 / X. Zhu et al - extractive body cue:** It serves as an implicit distillation objective to make the 3D model learn high-resolution, semantically-rich feature representations.
- **p. 2 / 1 Introduction - extractive body cue:** These lifted feature representations for 3D points can then be used to query with open-vocabulary descriptions, achieving semantic understanding in 3D.
- **p. 7 / X. Zhu et al - extractive body cue:** First of all, our 2D semantic understanding model uses a mask-based segmentation head which does not provide semantically-rich features in the pixel level.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | In summary, we make the following contributions: - To the best of our knowledge, we are the first to leverage text-image diffusion ... | p. 3 (1 Introduction), p. 4 (X. Zhu et al) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | (b) Directly using a 3D mask proposal network trained on labeled 3D data to produce class-agnostic masks, and then pool corresponding representations ... | p. 4 (X. Zhu et al), p. 1 (4 HKUST) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | We propose a novel method, namely Diff2Scene, which leverages frozen representations from text-image generative models, along with salient-aware and geometric-aware masks, for ... | p. 1 (4 HKUST), p. 3 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 1 Introduction - extractive body cue:** The frozen features extracted from the decoder of the U-Net in the diffusion model are trained with generative objectives, and cannot be directly used for ...
- **p. 4 / X. Zhu et al - extractive body cue:** LP D and LMD denote point-based distillation loss and mask-based distillation loss.
- **p. 4 / X. Zhu et al - extractive body cue:** As [19] pointed out, the projection from 3D to 2D has information loss and the solution is suboptimal.
- **p. 5 / X. Zhu et al - extractive body cue:** A neural network is trained to associate the 3D point cloud with these pseudo labels through contrastive loss.
- **p. 7 / X. Zhu et al - extractive body cue:** On the other hand, the pointbased feature representations from 2D foundation model can be naively distilled by minimizing the per-point feature distance.
- **p. 8 / X. Zhu et al - extractive body cue:** We propose a multimodal mask distillation loss to train our 3D mask generator:
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (1 Introduction), p. 4 (X. Zhu et al), p. 4 (X. Zhu et al), p. 5 (X. Zhu et al), p. 8 (X. Zhu et al), p. 8 (X. Zhu et al).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | takes, posed, RGB, images, reconstructed, point, cloud, model, inputs, Open-Vocabulary, Inference, During, Diff2Scene, multiview | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | takes, posed, RGB, images, reconstructed, point, cloud, model, inputs, Open-Vocabulary | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summary, make, following, contributions, best, knowledge, first, leverage, text-image, diffusion | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | frozen, features, extracted, decoder, U-Net, diffusion, model, trained, generative, objectives | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / X. Zhu et al - extractive body cue:** It takes posed RGB images and the reconstructed 3D point cloud as model inputs.
- **p. 8 / X. Zhu et al - extractive body cue:** 3.4 Open-Vocabulary Inference During inference, Diff2Scene takes a 3D point cloud and its multiview 2D images as inputs.
- **p. 3 / 1 Introduction - extractive body cue:** In summary, we make the following contributions: - To the best of our knowledge, we are the first to leverage text-image diffusion to perform open-vocabulary ...
- **p. 5 / X. Zhu et al - extractive body cue:** As a result, researchers have applied it to many understanding tasks such as image classification [46], object detection [9], image semantic segmentation [6,38,87], instance segmentation ...
- **p. 3 / 1 Introduction - extractive body cue:** Specifically, we design our 3D branch to take a 3D point cloud as input and to predict their 3D features.
- **p. 6 / X. Zhu et al - extractive body cue:** The 3D branch utilizes the point cloud and 2D mask embeddings as input.
- **p. 6 / X. Zhu et al - extractive body cue:** The 3D branch takes the point cloud and the 2D mask embeddings as inputs.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Text-to-Image Diffusion U-Net 2D Mask Generator Diffusion Mask Embeddings 3D Sparse Convolutional U-Net Multimodal Mask Distillation ❆ ❆ 3D Geometric-Aware Masks Add ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | The popular frameworks for contrastive representation learning include CLIP [65] and ALIGN [40]. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | The 3D point cloud is quantized into voxels by averaging the pixels within each voxel to save memory and reduce computes. | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 1 Introduction - extractive body cue:** In summary, we make the following contributions: - To the best of our knowledge, we are the first to leverage text-image diffusion to perform open-vocabulary ...
- **p. 4 / X. Zhu et al - extractive body cue:** (b) Directly using a 3D mask proposal network trained on labeled 3D data to produce class-agnostic masks, and then pool corresponding representations from the CLIP ...
- **p. 3 / 1 Introduction - extractive body cue:** The frozen features extracted from the decoder of the U-Net in the diffusion model are trained with generative objectives, and cannot be directly used for ...
- **p. 3 / 1 Introduction - extractive body cue:** The frozen features extracted from the decoder of the U-Net in the diffusion model are trained with generative objectives, and cannot be directly used for ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** summary, make, following, contributions, best, knowledge, first, leverage, text-image, diffusion, perform, open-vocabulary, semantic, segmentation, novel, mask, distillation, train, prediction, model.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | It splits 61 scenes for training, 11 scenes for validation and 18 for testing. | p. 9 (4 Experiment), p. 9 (4 Experiment) |
| Semantic / temporal fusion | Table 1: Comparison to state-of-the-art models. We report mIoU for all benchmarks. Best results in zero-shot, open-vocabulary setting are shown in bold. ... | p. 10 (Figure/Table caption), p. 13 (Figure/Table caption) |
| Robot query / planning handoff | Table 3: Performance of different model ablations. We observe that each com- ponent of our model gains consistent improvements. | p. 12 (Figure/Table caption), p. 9 (4 Experiment) |

## Failure and Ablation Link

- **p. 9 / 4 Experiment - extractive body cue:** We then perform comprehensive ablation studies to validate our designs.
- **p. 9 / 4 Experiment - extractive body cue:** Except for Replica, point clouds and multi-view images in the training split without ground truth annotations are used for model training.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Illustration of open-vocabulary 3D semantic scene understanding. We propose Diff2Scene, a 3D model that performs open-vocabulary semantic segmentation and visual grounding tasks given ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 3: Performance of different model ablations. We observe that each com- ponent of our model gains consistent improvements.
- **p. 12 / Figure/Table caption - extractive body cue:** Table 2: Effectiveness of Different Distillation Settings. We report mIoU of different methods on the Replica [77] dataset. Setting Distillation Type Head Tail All fine-tuned ...
- **p. 13 / Figure/Table caption - extractive body cue:** Fig. 4: Qualitative results from our model and OpenScene on zero-shot se- mantic segmentation. We visualize the segmentation results on the validation set of ScanNet200 ...
- **p. 13 / 5 Conclusion - extractive body cue:** There are several limitations of the proposed model.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (1 Introduction), p. 4 (X. Zhu et al), p. 1 (4 HKUST), p. 3 (1 Introduction), p. 8 (X. Zhu et al), p. 2 (1 Introduction), objective p. 3 (1 Introduction), p. 4 (X. Zhu et al), p. 4 (X. Zhu et al), p. 5 (X. Zhu et al), p. 7 (X. Zhu et al), p. 8 (X. Zhu et al), temporal p. 6 (X. Zhu et al), p. 7 (X. Zhu et al), p. 8 (X. Zhu et al), p. 11 (X. Zhu et al).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
