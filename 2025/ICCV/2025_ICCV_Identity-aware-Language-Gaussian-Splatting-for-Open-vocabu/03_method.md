# Method - Identity-aware Language Gaussian Splatting for Open-vocabulary 3D Semantic Segmentation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Jang_Identity-aware_Language_Gaussian_Splatting_for_Open-vocabulary_3D_Semantic_Segmentation_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Jang_Identity-aware_Language_Gaussian_Splatting_for_Open-vocabulary_3D_Semantic_Segmentation_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3.4. Loss Function), p. 4 (3.4. Loss Function), p. 4 (3.3. Progressive Mask Expanding), p. 3 (3.2. Identity-aware Semantic Consistency Learning), p. 5 (3.4. Loss Function), p. 3 (3.1. Preliminaries)): For stable optimization, we do not apply Lcons during the first 15,000 iterations, allowing the model to focus on learning by Lclip.

## Method Body Digest

- **p. 5 / 3.4. Loss Function - extractive PDF cue:** For stable optimization, we do not apply Lcons during the first 15,000 iterations, allowing the model to focus on learning by Lclip.
- **p. 4 / 3.4. Loss Function - extractive PDF cue:** The color reconstruction loss consists of L1 and D-SSIM terms, which measure the similarity of colors and structures between the rendered image ˆI and the ...
- **p. 4 / 3.3. Progressive Mask Expanding - extractive PDF cue:** We then Novel view Identity-aware language 3D Gaussian field Seed segment Final segment Progressive mask expanding Highest cosine similarity Text query Gundam Language feature map ...
- **p. 3 / 3.2. Identity-aware Semantic Consistency Learning - extractive PDF cue:** During training, we randomly select a subset of Gaussians and compute the identity-aware semantic consistency loss Lcons, which is defined as follows: Lcons = Lsame ...
- **p. 5 / 3.4. Loss Function - extractive PDF cue:** The CLIP loss Lclip is computed by using the L1 norm between rasterized language feature maps and CLIP feature maps by following the approach in ...
- **p. 3 / 3.1. Preliminaries - extractive PDF cue:** The covariance Σi is decomposed into a rotation matrix R and a scaling matrix S as Σi = RSS⊤R⊤, which improves numerical stability during optimization.
- **p. 4 / 3.2. Identity-aware Semantic Consistency Learning - extractive PDF cue:** The loss term Lsame enforces the consistency by maximizing the cosine similarity between language embeddings of Gaussians having the same identity.
- **p. 4 / 3.2. Identity-aware Semantic Consistency Learning - extractive PDF cue:** Meanwhile, Ldiff minimizes the cosine similarity between Gaussians with different identities.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** The main contribution of the proposed method can be summarized as follows: • We propose a novel framework that enforces language embeddings in the Gaussian ...
- **p. 2 / 1. Introduction - extractive PDF cue:** In this paper, we propose an identity-aware language Gaussian field to resolve the aforementioned problem in open-vocabulary 3D semantic segmentation.
- **p. 3 / 3.2. Identity-aware Semantic Consistency Learning - extractive PDF cue:** To address this issue, we introduce an identity-aware semantic consistency learning scheme.

## Source Evidence Cues

- **p. 5 / 3.4. Loss Function - extractive PDF cue:** For stable optimization, we do not apply Lcons during the first 15,000 iterations, allowing the model to focus on learning by Lclip.
- **p. 4 / 3.4. Loss Function - extractive PDF cue:** The color reconstruction loss consists of L1 and D-SSIM terms, which measure the similarity of colors and structures between the rendered image ˆI and the ...
- **p. 4 / 3.3. Progressive Mask Expanding - extractive PDF cue:** We then Novel view Identity-aware language 3D Gaussian field Seed segment Final segment Progressive mask expanding Highest cosine similarity Text query Gundam Language feature map ...
- **p. 3 / 3.2. Identity-aware Semantic Consistency Learning - extractive PDF cue:** During training, we randomly select a subset of Gaussians and compute the identity-aware semantic consistency loss Lcons, which is defined as follows: Lcons = Lsame ...
- **p. 5 / 3.4. Loss Function - extractive PDF cue:** The CLIP loss Lclip is computed by using the L1 norm between rasterized language feature maps and CLIP feature maps by following the approach in ...
- **p. 3 / 3.1. Preliminaries - extractive PDF cue:** The covariance Σi is decomposed into a rotation matrix R and a scaling matrix S as Σi = RSS⊤R⊤, which improves numerical stability during optimization.
- **Detected method headings:** 3. Proposed Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | For stable optimization, we do not apply Lcons during the first 15,000 iterations, allowing the model to focus on learning by Lclip. | p. 5 (3.4. Loss Function), p. 4 (3.4. Loss Function) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | The color reconstruction loss consists of L1 and D-SSIM terms, which measure the similarity of colors and structures between the rendered image ... | p. 4 (3.4. Loss Function), p. 4 (3.3. Progressive Mask Expanding) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | We then Novel view Identity-aware language 3D Gaussian field Seed segment Final segment Progressive mask expanding Highest cosine similarity Text query Gundam ... | p. 4 (3.3. Progressive Mask Expanding), p. 3 (3.2. Identity-aware Semantic Consistency Learning) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.2. Identity-aware Semantic Consistency Learning - extractive PDF cue:** The loss term Lsame enforces the consistency by maximizing the cosine similarity between language embeddings of Gaussians having the same identity.
- **p. 3 / 3.2. Identity-aware Semantic Consistency Learning - extractive PDF cue:** During training, we randomly select a subset of Gaussians and compute the identity-aware semantic consistency loss Lcons, which is defined as follows: Lcons = Lsame ...
- **p. 4 / 3.2. Identity-aware Semantic Consistency Learning - extractive PDF cue:** Meanwhile, Ldiff minimizes the cosine similarity between Gaussians with different identities.
- **p. 5 / 3.4. Loss Function - extractive PDF cue:** After this warm-up phase, we remove Lclip and incorporate Lcons into the total loss for remaining iterations.
- **p. 5 / 3.4. Loss Function - extractive PDF cue:** To learn identity and language embeddings augmented to Gaussians, we utilize the 2D identity loss Lcls and the CLIP loss Lclip.
- **p. 3 / 3.1. Preliminaries - extractive PDF cue:** The covariance Σi is decomposed into a rotation matrix R and a scaling matrix S as Σi = RSS⊤R⊤, which improves numerical stability during optimization.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (3.2. Identity-aware Semantic Consistency Learning), p. 4 (3.2. Identity-aware Semantic Consistency Learning), p. 4 (3.2. Identity-aware Semantic Consistency Learning), p. 5 (3.4. Loss Function), p. 5 (3.4. Loss Function).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | makes, language, embeddings, consistent, same, object, even, different, views, masking, strategy, starts, most, relevant | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | makes, language, embeddings, consistent, same, object, even, different, views, masking | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | main, contribution, summarized, follows, novel, framework, enforces, language, embeddings, Gaussian | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | loss, term, Lsame, enforces, consistency, maximizing, cosine, similarity, between, language | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive PDF cue:** This approach makes language embeddings be consistent for the same object, even in different views. • We propose a masking strategy that starts with the ...
- **p. 4 / 3.2. Identity-aware Semantic Consistency Learning - extractive PDF cue:** By aligning language embeddings conditioned on the identity information, the proposed method yields the reliable segmentation result, which is well aligned with the input text ...
- **p. 1 / 1. Introduction - extractive PDF cue:** (b)(c) Results of the cosine similarity between the text embedding of the input query and language features by the previous method [20] and the proposed ...
- **p. 2 / 1. Introduction - extractive PDF cue:** For open-vocabulary 3D semantic segmentation, after training, CLIP features encoded from the input query are compared with the rasterized 2D language feature map via the ...
- **p. 4 / 3.3. Progressive Mask Expanding - extractive PDF cue:** Rasterized language and identity feature maps are used to compute the cosine similarity with the input text query.
- **p. 1 / 1. Introduction - extractive PDF cue:** This technique is able to handle open-ended language queries and segment corresponding regions in the 3D space, thus provides natural and flexible interactions for editing ...
- **p. 3 / 3.2. Identity-aware Semantic Consistency Learning - extractive PDF cue:** The overall framework of the proposed method is shown in Fig.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | The overall framework of the proposed method is shown in Fig. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Specifically, we incorporate the identity information into our framework, inspired by the concept of the identity encoding for segmentation and editing in ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | [24] proposed quantization-based language embedding in 3DGS, which reduced memory usage and preserved feature consistency. | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3.2. Identity-aware Semantic Consistency Learning - extractive PDF cue:** During training, we randomly select a subset of Gaussians and compute the identity-aware semantic consistency loss Lcons, which is defined as follows: Lcons = Lsame ...
- **p. 5 / 4.1. Training - extractive PDF cue:** Our model is trained on an AMD EPYC 7352 24-Core Processor CPU and a single NVIDIA A100 GPU.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** stable, optimization, apply, Lcons, during, first, iterations, allowing, model, focus, learning, Lclip, color, reconstruction, loss, consists, D-SSIM, terms, measure, similarity.
- **Relevant PDF headings:** 3. Proposed Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | The LERF dataset consists of 3D scenes in the wild, which are captured by using the Polycam application on the iPhone. | p. 5 (4.2. Datasets and Evaluation Metrics), p. 5 (4.2. Datasets and Evaluation Metrics) |
| Semantic / temporal fusion | Performance comparisons of novel view rendering on the LERF [10] dataset (the best results are shown in bold). can see that the ... | p. 7 (4.3. Performance Evaluation), p. 6 (4.3. Performance Evaluation) |
| Robot query / planning handoff | Specifically, the proposed method achieves 80.5 mIoU and 76.0 mBIoU on the LERF dataset, which outperforms the stateof-the-art methods by a considerable ... | p. 5 (4.3. Performance Evaluation), p. 5 (4.3. Performance Evaluation) |

## Failure and Ablation Link

- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 3. This progressive expanding scheme helps the model con- sider the local relationship between segments in the same target, which ensures to extract segmentation ...
- **p. 7 / 4.3. Performance Evaluation - extractive PDF cue:** Performance comparisons of novel view rendering on the LERF [10] dataset (the best results are shown in bold). can see that the proposed method is ...
- **p. 7 / 4.4. Ablation Study - extractive PDF cue:** As can be seen, the performance of open-vocabulary 3D semantic segmentation is considerably improved as each component is added to the baseline.
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** Consequently, synergy among the proposed components yields superior performance in openvocabulary 3D semantic segmentation.
- **p. 5 / 4.3. Performance Evaluation - extractive PDF cue:** Furthermore, we also evaluate the performance of the proposed method with photometric metrics, such as peak signal-to-noise ratio (PSNR), structural similarity index (SSIM) [27], and ...
- **p. 6 / 4.3. Performance Evaluation - extractive PDF cue:** In addition, previous methods often fail to extract boundaries accurately due to the use of fixed threshold values in generating semantic segmentation masks(see Fig.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3.4. Loss Function), p. 4 (3.4. Loss Function), p. 4 (3.3. Progressive Mask Expanding), p. 3 (3.2. Identity-aware Semantic Consistency Learning), p. 5 (3.4. Loss Function), p. 3 (3.1. Preliminaries), objective p. 4 (3.2. Identity-aware Semantic Consistency Learning), p. 3 (3.2. Identity-aware Semantic Consistency Learning), p. 4 (3.2. Identity-aware Semantic Consistency Learning), p. 5 (3.4. Loss Function), p. 5 (3.4. Loss Function), p. 3 (3.1. Preliminaries), temporal p. 3 (3.2. Identity-aware Semantic Consistency Learning), p. 3 (3.2. Identity-aware Semantic Consistency Learning), p. 5 (4.1. Training), p. 2 (2.1. 3D Scene Representations), p. 2 (2.2. Open-Vocabulary 3D Semantic Segmentation).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
