# Method - Dens3R: A Foundation Model for 3D Geometry Prediction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=kxVjQhkAWz; PDF retrieval source: https://openreview.net/pdf/f8af5ab61a9d33b6aaa32fa274fb76ff5e2fd0dd.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 7 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 8 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD)): Specifically, we introduce high-quality normal supervision based on the first stage's point map, and jointly fine-tune the encoder-decoder module, point map prediction head, and newly added normal prediction head to ...

## Method Body Digest

- **p. 7 / 3 METHOD - extractive PDF cue:** Specifically, we introduce high-quality normal supervision based on the first stage's point map, and jointly fine-tune the encoder-decoder module, point map prediction head, and newly ...
- **p. 5 / 3 METHOD - extractive PDF cue:** (2025a;b), we first employ a sharedweight encoder to process input image sequences and extract image features Feai, which are then fed into the decoder.
- **p. 6 / 3 METHOD - extractive PDF cue:** Suppose ˆ M = (i, j) is the set of ground-truth correspondences where the ith pixel in the first image matches the jth pixel in ...
- **p. 8 / 3 METHOD - extractive PDF cue:** In practice, we first compute matches in a one-versus-all strategy using our model, and then triangulate these matches to obtain multi-view point clouds, following the ...
- **p. 5 / 3 METHOD - extractive PDF cue:** Given the need to predict a wider range of geometric outputs, this design also significantly reduces memory and computational overhead, keeping the training and inference ...
- **p. 6 / 3 METHOD - extractive PDF cue:** For a predicted camera, we use the local 3D regression loss to quantify the pointmap in its own coordinate frame.
- **p. 7 / 3 METHOD - extractive PDF cue:** To further improve the performance of Dens3R on high-resolution inputs, we introduce a coarse-tofine training strategy.
- **p. 6 / 3 METHOD - extractive PDF cue:** This loss function simultaneously optimizes for two objectives.

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** For the training strategy, we propose a novel two-staged approach.
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** In contrast, our method allows the communication between 3D geometric representation and normal prediction without known camera poses.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** In this paper, we present Dens3R, a foundation model for high-quality geometric prediction.

## Source Evidence Cues

- **p. 7 / 3 METHOD - extractive PDF cue:** Specifically, we introduce high-quality normal supervision based on the first stage's point map, and jointly fine-tune the encoder-decoder module, point map prediction head, and newly ...
- **p. 5 / 3 METHOD - extractive PDF cue:** (2025a;b), we first employ a sharedweight encoder to process input image sequences and extract image features Feai, which are then fed into the decoder.
- **p. 6 / 3 METHOD - extractive PDF cue:** Suppose ˆ M = (i, j) is the set of ground-truth correspondences where the ith pixel in the first image matches the jth pixel in ...
- **p. 8 / 3 METHOD - extractive PDF cue:** In practice, we first compute matches in a one-versus-all strategy using our model, and then triangulate these matches to obtain multi-view point clouds, following the ...
- **p. 5 / 3 METHOD - extractive PDF cue:** Given the need to predict a wider range of geometric outputs, this design also significantly reduces memory and computational overhead, keeping the training and inference ...
- **p. 6 / 3 METHOD - extractive PDF cue:** For a predicted camera, we use the local 3D regression loss to quantify the pointmap in its own coordinate frame.
- **p. 7 / 3 METHOD - extractive PDF cue:** To further improve the performance of Dens3R on high-resolution inputs, we introduce a coarse-tofine training strategy.
- **Detected method headings:** 3 METHOD (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Specifically, we introduce high-quality normal supervision based on the first stage's point map, and jointly fine-tune the encoder-decoder module, point map prediction ... | p. 7 (3 METHOD), p. 5 (3 METHOD) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | (2025a;b), we first employ a sharedweight encoder to process input image sequences and extract image features Feai, which are then fed into ... | p. 5 (3 METHOD), p. 6 (3 METHOD) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Suppose ˆ M = (i, j) is the set of ground-truth correspondences where the ith pixel in the first image matches the ... | p. 6 (3 METHOD), p. 8 (3 METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 3 METHOD - extractive PDF cue:** This loss function simultaneously optimizes for two objectives.
- **p. 6 / 3 METHOD - extractive PDF cue:** With the above losses, we summarize the training objective as: Lstage1 = Lpts loc + η1Lpts glb + η2Lpts n + η3Lmatch, (8) where the ...
- **p. 7 / 3 METHOD - extractive PDF cue:** However, naively removing the loss without additional constraints leads to degraded performance, since previous models rely heavily on confidence weighting for point-view regression.
- **p. 7 / 3 METHOD - extractive PDF cue:** The complete training objective for training stage 2 is as follows: Lstage2 = Lpts loc + λ1Lpts glb + λ2Lpts n + λ3Ln, (11) where ...
- **p. 5 / 3 METHOD - extractive PDF cue:** (2024), we adopted (1) local 3D regression loss Lpts loc , (2) Global 3D Regression Loss Lpts glb , (3) Pointmap Normal Loss Lpts n, ...
- **p. 8 / 3 METHOD - extractive PDF cue:** (2024), and is trained jointly within our multitask objective.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 6 (3 METHOD), p. 6 (3 METHOD), p. 7 (3 METHOD), p. 7 (3 METHOD), p. 5 (3 METHOD), p. 8 (3 METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | normal, prediction, head, connected, after, initial, point, training, completed, allowing, model, consistently, output, coherent | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | normal, prediction, head, connected, after, initial, point, training, completed, allowing | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | training, strategy, novel, two-staged, contrast, allows, communication, between, geometric, representation | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | loss, function, simultaneously, optimizes, objectives, above, losses, summarize, training, objective | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 7 / 3 METHOD - extractive PDF cue:** The normal prediction head is connected after the initial point map training is completed, allowing the model to consistently output coherent normal mappings from the ...
- **p. 5 / 3 METHOD - extractive PDF cue:** Given an image pair of image sequence (Ii)2 i=1 ∈R3×H×W , Dens3R's dense visual transformer is a function f that maps the input to a ...
- **p. 4 / 1 INTRODUCTION - extractive PDF cue:** (2024) proposes to directly map two input images in a single forward pass, leading to a more straightforward geometry representation.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Therefore, the direct application of diffusion models in geometric regression tasks faces significant challenges, especially in such tasks where a strict one-to-one correspondence between input ...
- **p. 5 / 3 METHOD - extractive PDF cue:** Meanwhile, extending the model inputs to multi-view images in the inference stage significantly improves the overall inference quality.
- **p. 7 / 3 METHOD - extractive PDF cue:** Apart from the intrinsic-invariant pointmap, we also design a normal head to predict the view-space normal of each frame in input image pairs.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** This raises a key issue: while image generation tasks typically benefit from their inherent ambiguity and multi-modal output characteristics, geometric prediction is fundamentally different.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Given an image pair of image sequence (Ii)2 i=1 ∈R3×H×W , Dens3R's dense visual transformer is a function f that maps the ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | That is: R′(x, m) = R(x, mL L′ ), (2) where m is the position index and L′ is the longer sequence. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 3 METHOD - extractive PDF cue:** Specifically, we introduce high-quality normal supervision based on the first stage's point map, and jointly fine-tune the encoder-decoder module, point map prediction head, and newly ...
- **p. 5 / 3 METHOD - extractive PDF cue:** Given the need to predict a wider range of geometric outputs, this design also significantly reduces memory and computational overhead, keeping the training and inference ...
- **p. 7 / 3 METHOD - extractive PDF cue:** To further improve the performance of Dens3R on high-resolution inputs, we introduce a coarse-tofine training strategy.
- **p. 20 / A.3 IMPLEMENTATION DETAILS - extractive PDF cue:** As for model inference, our model only requires a single Nvidia RTX3090 GPU for 1024-resolution image inputs.
- **p. 7 / 3 METHOD - extractive PDF cue:** Specifically, we introduce high-quality normal supervision based on the first stage's point map, and jointly fine-tune the encoder-decoder module, point map prediction head, and newly ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Specifically, introduce, high-quality, normal, supervision, first, stage, point, jointly, fine-tune, encoder-decoder, module, prediction, head, newly, added, achieve, end-to-end, optimization, employ.
- **Relevant PDF headings:** 3 METHOD (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | 4.1 NORMAL AND MATCHING PREDICTION We evaluate our Dens3R on several surface normal prediction datasets that include both indoor and outdoor scenes. | p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Semantic / temporal fusion | Figure 12: Limitations. Despite that our method outperforms previous methods in geometric pre- dictions, the prediction quality for thin structures still require ... | p. 24 (Figure/Table caption), p. 9 (4 EXPERIMENTS) |
| Robot query / planning handoff | Figure 4: Qualitative comparison of normal prediction. Dens3R generates more accurate and de- tailed normal maps than previous methods for both object-centric ... | p. 8 (Figure/Table caption), p. 24 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 18 / Figure/Table caption - extractive PDF cue:** Table 4: Ablation on shared encoder-decoder structure. We conduct experiments for both of the model on image pairs with 512 resolution. With the shared encoder-decoder ...
- **p. 24 / Figure/Table caption - extractive PDF cue:** Figure 12: Limitations. Despite that our method outperforms previous methods in geometric pre- dictions, the prediction quality for thin structures still require further improvement. inputs ...
- **p. 17 / Figure/Table caption - extractive PDF cue:** Table 3: Normal quantitative metrics for ablation. We demonstrate that both the intrinsic-invariant training and coarse-to-fine strategy contributes to accurate normal predictions.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Our method achieves high-quality pointmap prediction and depth estimation with the intrinsic-invariant pointmap and the novel training strategy.
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Overview of Dens3R. We propose Dens3R, a dense visual transformer backbone featuring a shared encoder-decoder architecture and multiple task-specific heads for geometric prediction. ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 3: Normal comparison. We demonstrate that the normal derived directly from the scale- invariant pointmap and MoGe both are not accurate enough. tasks-particularly surface ...
- **p. 19 / Figure/Table caption - extractive PDF cue:** Figure 8: Ablation and downstream applications. A.2 DOWNSTREAM APPLICATIONS Segmentation Head Training. Dens3R serves as a visual foundation model that can be finetuned for several ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 7 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 8 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), objective p. 6 (3 METHOD), p. 6 (3 METHOD), p. 7 (3 METHOD), p. 7 (3 METHOD), p. 5 (3 METHOD), p. 8 (3 METHOD), temporal p. 5 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 6 (3 METHOD), p. 7 (3 METHOD), p. 8 (3 METHOD).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
