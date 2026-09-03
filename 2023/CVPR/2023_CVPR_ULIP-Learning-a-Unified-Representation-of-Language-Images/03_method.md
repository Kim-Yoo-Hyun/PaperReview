# Method - ULIP: Learning a Unified Representation of Language, Images, and Point Clouds for 3D Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2212.05171; PDF retrieval source: https://arxiv.org/pdf/2212.05171. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 6 (Model), p. 3 (3.1. Creating Training Triplets for ULIP), p. 5 (4.3. Implementation Details), p. 5 (4.3. Implementation Details), p. 8 (4.7. Cross-Modal Retrieval), p. 3 (3.1. Creating Training Triplets for ULIP)): It conducts zero-shot 3D classification by first converting a 3D point cloud into 6 orthogonal depth maps, then using CLIP's image encoder to get ensembled depth map features, and finally ...

## Method Body Digest

- **p. 6 / Model - extractive body cue:** It conducts zero-shot 3D classification by first converting a 3D point cloud into 6 orthogonal depth maps, then using CLIP's image encoder to get ensembled ...
- **p. 3 / 3.1. Creating Training Triplets for ULIP - extractive body cue:** Then a 3D encoder takes the augmented point cloud Pi as input and outputs its 3D representation hP i via
- **p. 5 / 4.3. Implementation Details - extractive body cue:** We use our pre-trained models as they are when performing zero-shot classification.
- **p. 5 / 4.3. Implementation Details - extractive body cue:** On ModelNet40, we use the learning rate as 0.00015 and fine-tune our model for 200 epochs, with the batch size as 24 for PointNet++.
- **p. 8 / 4.7. Cross-Modal Retrieval - extractive body cue:** We use our pre-trained ULIP with PointBERT as the 3D encoder directly.
- **p. 3 / 3.1. Creating Training Triplets for ULIP - extractive body cue:** During each iteration of pre-training, we randomly select one image or depth map from each CAD model's 60 renderred candidates as Ii and take Ii ...
- **p. 6 / 4.6. Analyses - extractive body cue:** 5, ULIP by default aligns the 3D representation with both the text and image representations during pre-training.
- **p. 5 / 4.3. Implementation Details - extractive body cue:** We use 64 as the batch size, 10-3 as the learning rate, and AdamW as the optimizer.

## Design Rationale

- **p. 5 / 4.4. Standard 3D Classification - extractive body cue:** We present the standard 3D classification performances of our baselines and our methods on ScanObjectNN in Table 7.
- **p. 2 / 1. Introduction - extractive body cue:** An illustration of our framework is shown in Figure 1.
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we propose Learning a Unified Representation of Language, Images, and Point Clouds (ULIP).

## Source Evidence Cues

- **p. 6 / Model - extractive body cue:** It conducts zero-shot 3D classification by first converting a 3D point cloud into 6 orthogonal depth maps, then using CLIP's image encoder to get ensembled ...
- **p. 3 / 3.1. Creating Training Triplets for ULIP - extractive body cue:** Then a 3D encoder takes the augmented point cloud Pi as input and outputs its 3D representation hP i via
- **p. 5 / 4.3. Implementation Details - extractive body cue:** We use our pre-trained models as they are when performing zero-shot classification.
- **p. 5 / 4.3. Implementation Details - extractive body cue:** On ModelNet40, we use the learning rate as 0.00015 and fine-tune our model for 200 epochs, with the batch size as 24 for PointNet++.
- **p. 8 / 4.7. Cross-Modal Retrieval - extractive body cue:** We use our pre-trained ULIP with PointBERT as the 3D encoder directly.
- **p. 3 / 3.1. Creating Training Triplets for ULIP - extractive body cue:** During each iteration of pre-training, we randomly select one image or depth map from each CAD model's 60 renderred candidates as Ii and take Ii ...
- **p. 6 / 4.6. Analyses - extractive body cue:** 5, ULIP by default aligns the 3D representation with both the text and image representations during pre-training.
- **Detected method headings:** Model (p. 5); Model (p. 6); Model (p. 7)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | It conducts zero-shot 3D classification by first converting a 3D point cloud into 6 orthogonal depth maps, then using CLIP's image encoder ... | p. 6 (Model), p. 3 (3.1. Creating Training Triplets for ULIP) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Then a 3D encoder takes the augmented point cloud Pi as input and outputs its 3D representation hP i via | p. 3 (3.1. Creating Training Triplets for ULIP), p. 5 (4.3. Implementation Details) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | We use our pre-trained models as they are when performing zero-shot classification. | p. 5 (4.3. Implementation Details), p. 5 (4.3. Implementation Details) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4.3. Implementation Details - extractive body cue:** We use 64 as the batch size, 10-3 as the learning rate, and AdamW as the optimizer.
- **p. 5 / 4.3. Implementation Details - extractive body cue:** As mentioned in Section 3.2, we freeze the image and text encoders and only update the 3D encoder's parameters during pre-training.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (4.3. Implementation Details).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Then, encoder, takes, augmented, point, cloud, input, outputs, representation, During, iteration, pre-training, randomly, select | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Then, encoder, takes, augmented, point, cloud, input, outputs, representation, During | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | present, standard, classification, performances, baselines, methods, ScanObjectNN, Table, illustration, framework | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | batch, size, learning, rate, AdamW, optimizer, mentioned, Section, freeze, image | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.1. Creating Training Triplets for ULIP - extractive body cue:** Then a 3D encoder takes the augmented point cloud Pi as input and outputs its 3D representation hP i via
- **p. 3 / 3.1. Creating Training Triplets for ULIP - extractive body cue:** During each iteration of pre-training, we randomly select one image or depth map from each CAD model's 60 renderred candidates as Ii and take Ii ...
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we propose Learning a Unified Representation of Language, Images, and Point Clouds (ULIP).
- **p. 6 / Model - extractive body cue:** It conducts zero-shot 3D classification by first converting a 3D point cloud into 6 orthogonal depth maps, then using CLIP's image encoder to get ensembled ...
- **p. 2 / 1. Introduction - extractive body cue:** To circumvent the lack of triplet data, we take advantage of a vision-language model pretrained on massive imagetext pairs, and align the feature space of ...
- **p. 5 / 4.3. Implementation Details - extractive body cue:** The inputs of image and text modalities are generated as described in Section 3.1.
- **p. 1 / 1. Introduction - extractive body cue:** ULIP improves 3D understanding by aligning features from images, texts, and point clouds in the same space.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | We experiment with the following 3D backbone networks under our framework. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Since the structure of the 3D backbone is unchanged, our framework does not introduce extra latency during inference time. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | For PointBERT, we use the learning rate of 0.0002 and finetune for 300 epochs with batch size 32. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 4.3. Implementation Details - extractive body cue:** We use our pre-trained models as they are when performing zero-shot classification.
- **p. 5 / 4.3. Implementation Details - extractive body cue:** On ModelNet40, we use the learning rate as 0.00015 and fine-tune our model for 200 epochs, with the batch size as 24 for PointNet++.
- **p. 8 / 4.7. Cross-Modal Retrieval - extractive body cue:** We use our pre-trained ULIP with PointBERT as the 3D encoder directly.
- **p. 3 / 3.1. Creating Training Triplets for ULIP - extractive body cue:** During each iteration of pre-training, we randomly select one image or depth map from each CAD model's 60 renderred candidates as Ii and take Ii ...
- **p. 6 / 4.6. Analyses - extractive body cue:** 5, ULIP by default aligns the 3D representation with both the text and image representations during pre-training.
- **p. 5 / 4.3. Implementation Details - extractive body cue:** For PointMLP, we set the learning rate as 0.1 and fine-tune the model for 300 epochs, with the batch size as 32.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** conducts, zero-shot, classification, first, converting, point, cloud, orthogonal, depth, maps, then, CLIP, image, encoder, ensembled, features, finally, match, text, takes.
- **Relevant PDF headings:** Model (p. 5); Model (p. 6); Model (p. 7).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | ModelNet40 is a synthetic dataset of 3D CAD models. | p. 4 (4.2. Downstream Datasets), p. 4 (4.2. Downstream Datasets) |
| Semantic / temporal fusion | Table 1. 3D classification results on ScanObjectNN. ULIP signifi- cantly improves our baselines. Our best result outperforms SOTA largely by around 3% ... | p. 5 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Robot query / planning handoff | Table 2. Standard 3D classification results on ModelNet40. ULIP significantly improves our baselines. Our best number achieves new SOTA. * means a ... | p. 6 (Figure/Table caption), p. 7 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 5 / 4.3. Implementation Details - extractive body cue:** 3We used the variants provided by [58] in our experiments.
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1. 3D classification results on ScanObjectNN. ULIP signifi- cantly improves our baselines. Our best result outperforms SOTA largely by around 3% on Overall Acc. ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 9. ModelNet40 Medium Set. Hard Set: We remove both extract category names and their synonyms in our pre-training dataset. The final Hard Set is ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 8. ModelNet40 All Set. Medium Set: We remove categories whose exact category names exist in our pre-training dataset. The resulting cate- gories in this ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Illustration of our method. The inputs of multimodal pre-training (Left) are a batch of objects represented as triplets (image, text, point cloud). Image ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 6. Analysis of aligning three vs. two modalities on zero-shot 3D classification on ScanObjectNN. Results show that aligning representations of three modalities always produces ...
- **p. 5 / 4.3. Implementation Details - extractive body cue:** During pre-training, we utilize an advanced version of CLIP, namely SLIP [32], that shows superior performance as our image-text encoders.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 6 (Model), p. 3 (3.1. Creating Training Triplets for ULIP), p. 5 (4.3. Implementation Details), p. 5 (4.3. Implementation Details), p. 8 (4.7. Cross-Modal Retrieval), p. 3 (3.1. Creating Training Triplets for ULIP), objective p. 5 (4.3. Implementation Details), p. 5 (4.3. Implementation Details), temporal p. 4 (4.1. 3D Backbone Networks), p. 5 (4.4. Standard 3D Classification), p. 1 (Abstract), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Learning a Unified Representation of Lan).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
