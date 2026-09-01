# Method - Unifying 2D and 3D Vision-Language Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=FcTeo26AfZ; PDF retrieval source: https://openreview.net/pdf/6306d082de46d27c14c27436e4597009a5c8371a.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (3. Method), p. 4 (3. Method), p. 4 (3. Method), p. 3 (3. Method), p. 5 (3.1. Supervision Objective), p. 5 (3.1. Supervision Objective)): Language Conditioned Mask Decoder: The mask decoder head takes as input the encoded visual features, their corresponding (relative) 3D coordinates, and the encoded language utterance; it outputs 3D segmentation masks ...

## Method Body Digest

- **p. 3 / 3. Method - extractive PDF cue:** Language Conditioned Mask Decoder: The mask decoder head takes as input the encoded visual features, their corresponding (relative) 3D coordinates, and the encoded language utterance; ...
- **p. 4 / 3. Method - extractive PDF cue:** The proposed decoder then iteratively updates a set of learnable queries as well as the 3D feature tokens though token - language - query attentions ...
- **p. 4 / 3. Method - extractive PDF cue:** The refined queries after each decoder layer Q(i+1) = X(i+1) 1:M are then used for mask prediction with the updated visual features and for language ...
- **p. 3 / 3. Method - extractive PDF cue:** The model takes as input a language query, N RGB images of shape N × H × W × 3, and an associated 3D pointmap ...
- **p. 5 / 3.1. Supervision Objective - extractive PDF cue:** To address this, we introduce a novel box loss.
- **p. 5 / 3.1. Supervision Objective - extractive PDF cue:** For ablations in Table 7 and 5, we use a 88M parameter Swin (Liu et al., 2021) image-encoder.
- **p. 5 / 3.1. Supervision Objective - extractive PDF cue:** We incorporate this box loss as an additional cost in both Hungarian matching and the final loss.
- **p. 5 / 3.1. Supervision Objective - extractive PDF cue:** Box Loss: We observe a failure mode in our model where, when trained with the aforementioned objectives, some masks include a small number of distant, ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** In summary, our contributions are: • Unified 2D-3D Visual Grounding: We propose a model that can consume and benefit from both 2D and 3D vision-language ...
- **p. 1 / 1. Introduction - extractive PDF cue:** In this paper, we introduce UniVLG, a unified 2D-3D visionlanguage model designed to improve 3D understanding by leveraging large-scale 2D data and pre-trained 2D models.
- **p. 5 / 3.1. Supervision Objective - extractive PDF cue:** To address this, we introduce a novel box loss.

## Source Evidence Cues

- **p. 3 / 3. Method - extractive PDF cue:** Language Conditioned Mask Decoder: The mask decoder head takes as input the encoded visual features, their corresponding (relative) 3D coordinates, and the encoded language utterance; ...
- **p. 4 / 3. Method - extractive PDF cue:** The proposed decoder then iteratively updates a set of learnable queries as well as the 3D feature tokens though token - language - query attentions ...
- **p. 4 / 3. Method - extractive PDF cue:** The refined queries after each decoder layer Q(i+1) = X(i+1) 1:M are then used for mask prediction with the updated visual features and for language ...
- **p. 3 / 3. Method - extractive PDF cue:** The model takes as input a language query, N RGB images of shape N × H × W × 3, and an associated 3D pointmap ...
- **p. 5 / 3.1. Supervision Objective - extractive PDF cue:** To address this, we introduce a novel box loss.
- **p. 5 / 3.1. Supervision Objective - extractive PDF cue:** For ablations in Table 7 and 5, we use a 88M parameter Swin (Liu et al., 2021) image-encoder.
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Language Conditioned Mask Decoder: The mask decoder head takes as input the encoded visual features, their corresponding (relative) 3D coordinates, and the ... | p. 3 (3. Method), p. 4 (3. Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | The proposed decoder then iteratively updates a set of learnable queries as well as the 3D feature tokens though token - language ... | p. 4 (3. Method), p. 4 (3. Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | The refined queries after each decoder layer Q(i+1) = X(i+1) 1:M are then used for mask prediction with the updated visual features ... | p. 4 (3. Method), p. 3 (3. Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.1. Supervision Objective - extractive PDF cue:** We incorporate this box loss as an additional cost in both Hungarian matching and the final loss.
- **p. 5 / 3.1. Supervision Objective - extractive PDF cue:** Box Loss: We observe a failure mode in our model where, when trained with the aforementioned objectives, some masks include a small number of distant, ...
- **p. 3 / 3. Method - extractive PDF cue:** In datasets such as ScanNet, we obtain the 3D pointmap by unprojecting the sensed depth images using the camera parameters and standard pinhole-camera equations.
- **p. 4 / 3. Method - extractive PDF cue:** Next, the visual tokens from the backbone are updated by crossattending to the updated object and text tokens.
- **p. 4 / 3. Method - extractive PDF cue:** The refined queries after each decoder layer Q(i+1) = X(i+1) 1:M are then used for mask prediction with the updated visual features and for language ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3.1. Supervision Objective), p. 3 (3. Method), p. 5 (3.1. Supervision Objective), p. 4 (3. Method), p. 4 (3. Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Example, task, inputs/outputs, UniVLG, visual, features, language, instructions, ground, objects, mentioned, input, Conditioned, Mask | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Example, task, inputs/outputs, UniVLG, visual, features, language, instructions, ground, objects | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summary, contributions, Unified, D-3D, Visual, Grounding, model, consume, benefit, vision-language | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | incorporate, loss, additional, cost, Hungarian, matching, final, Box, observe, failure | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive PDF cue:** (D) Example task inputs/outputs for UniVLG. on both visual features and language instructions to ground objects mentioned in the language input.
- **p. 3 / 3. Method - extractive PDF cue:** Language Conditioned Mask Decoder: The mask decoder head takes as input the encoded visual features, their corresponding (relative) 3D coordinates, and the encoded language utterance; ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Unlike models that operate directly on 3D point clouds, UniVLG processes RGB and RGB-D images-natural sensory inputs for embodied agents-and supports both single-view RGB images ...
- **p. 2 / 1. Introduction - extractive PDF cue:** In summary, our contributions are: • Unified 2D-3D Visual Grounding: We propose a model that can consume and benefit from both 2D and 3D vision-language ...
- **p. 3 / 3. Method - extractive PDF cue:** The model takes as input a language query, N RGB images of shape N × H × W × 3, and an associated 3D pointmap ...
- **p. 4 / 3. Method - extractive PDF cue:** The proposed decoder then iteratively updates a set of learnable queries as well as the 3D feature tokens though token - language - query attentions ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Today's real-world embodied systems rely on depth sensors and egocentric, calibrated camera setups for navigation and interaction with their surroundings (Ahn et al., 2022; Chiang ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | For 3D scenes, we compute CLIP embeddings for all images and captions and use this to select 5 relevant frames, with an ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | We concatenate these object queries with the language tokens along the sequence dimension. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | For 3D scenes, we compute CLIP embeddings for all images and captions and use this to select 5 relevant frames, with an ... | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 4.1. Evaluation on 3D Referential Grounding - extractive PDF cue:** Similarly, PQ3D adds the Multi3DRefer (Zhang et al., 2023) and Scan2Cap datasets (Chen et al., 2020b), but also utilizes a point encoder that was trained ...
- **p. 5 / 3.1. Supervision Objective - extractive PDF cue:** Implementation details: UniVLG consists of 108M trainable parameters along with a frozen 220M parameter textencoder (Koukounas et al., 2024) and a 304M parameter image-encoder (Oquab ...
- **p. 5 / 3.1. Supervision Objective - extractive PDF cue:** We train in data-parallel across 32 A100 80G GPUs with an effective batch size of 64.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Language, Conditioned, Mask, Decoder, head, takes, input, encoded, visual, features, corresponding, relative, coordinates, utterance, outputs, segmentation, masks, mentioned, objects, text.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | For example, 3D-VisTA (Zhu et al., 2023b) trains on the previously mentioned 3D datasets that we use but also includes 3RScan (1500 ... | p. 6 (4.1. Evaluation on 3D Referential Grounding), p. 6 (4.1. Evaluation on 3D Referential Grounding) |
| Semantic / temporal fusion | UniVLG outperforms all prior baselines on both benchmarks. | p. 7 (4.3. Evaluation on 3D Question Answering), p. 7 (4.1. Evaluation on 3D Referential Grounding) |
| Robot query / planning handoff | We observe that incorporating 2D data improves performance in both scenarios, but our approach of lifting 2D images to 3D achieves the ... | p. 8 (1. Lifting 2D datasets to 3D improves 3D performance), p. 7 (4.1. Evaluation on 3D Referential Grounding) |

## Failure and Ablation Link

- **p. 8 / 1. Lifting 2D datasets to 3D improves 3D performance - extractive PDF cue:** In Table 6, we compare three variants of our model: one trained only on 3D data, one trained with 3D data and 2D images without ...
- **p. 18 / Figure/Table caption - extractive PDF cue:** Table 11. Ablation of visual backbones on 3D language grounding. We evaluate top-1 accuracy on the official validation set without assuming ground-truth proposals (Det).
- **p. 17 / Figure/Table caption - extractive PDF cue:** Table 10. Effect of Fine-tuning 2D backbones of UniVLG for Acc@25 in DetSetup. SR3D and NR3D are in-domain and Scan- Refer is out-of-domain
- **p. 7 / 4.2. Evaluation on Out-of-Domain 3D Referential - extractive PDF cue:** We show the results of our model, both a 3D-only variant and our full model w/2D data + lifting in Table 2.
- **p. 7 / 4.1. Evaluation on 3D Referential Grounding - extractive PDF cue:** Even without our joint 2D training strategy-and with less 3D data than prior methods-UniVLG-3D-only significantly outperforms all prior methods.
- **p. 8 / 4.4. Evaluation on 2D Referential Grounding - extractive PDF cue:** As we show in our experiments, this approach leads to significant improvements in 3D performance without negatively affecting 2D performance.
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 7. Ablations Acc@25 in DetSetup

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (3. Method), p. 4 (3. Method), p. 4 (3. Method), p. 3 (3. Method), p. 5 (3.1. Supervision Objective), p. 5 (3.1. Supervision Objective), objective p. 5 (3.1. Supervision Objective), p. 5 (3.1. Supervision Objective), p. 3 (3. Method), p. 4 (3. Method), p. 4 (3. Method), temporal p. 5 (3.1. Supervision Objective), p. 4 (3. Method), p. 4 (3. Method), p. 5 (3.1. Supervision Objective), p. 2 (1. Introduction), p. 2 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
