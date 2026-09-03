# Method - Kestrel: 3D Multimodal LLM for Part-Aware Grounded Description

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Ahmed_Kestrel_3D_Multimodal_LLM_for_Part-Aware_Grounded_Description_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Ahmed_Kestrel_3D_Multimodal_LLM_for_Part-Aware_Grounded_Description_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (4.1. Kestrel), p. 4 (4.1. Kestrel), p. 3 (4. Method), p. 5 (4.1. Kestrel), p. 5 (4.2. Training Objective), p. 6 (Model)): As shown in Figure 2, Kestrel is composed of a point encoder, an LLM, a point feature propagation module (PFPM), and a segmentation decoder.

## Method Body Digest

- **p. 4 / 4.1. Kestrel - extractive body cue:** As shown in Figure 2, Kestrel is composed of a point encoder, an LLM, a point feature propagation module (PFPM), and a segmentation decoder.
- **p. 4 / 4.1. Kestrel - extractive body cue:** Each upsampled feature is combined with intermediate segmentation decoder queries, qi(i ↑{1, 2}), which will be projected through an MLP and then combined by a ...
- **p. 3 / 4. Method - extractive body cue:** 4.1, we formally introduce Kestrel as a part-aware point grounding 3D MLLM, followed by a detailed explanation of our training objective in Sec.
- **p. 5 / 4.1. Kestrel - extractive body cue:** This masked attention process allows each query to only attend to its relevant part features at each upsampled level, leading to accurate segmentation masks.
- **p. 5 / 4.2. Training Objective - extractive body cue:** The overall training loss for Kestrel is defined as Llang = wCE · LCE(ˆytxt, ytxt) (5) Lmask = wBCE · LBCE(ˆymask, ymask) +wDice · LDice(ˆymask, ...
- **p. 6 / Model - extractive body cue:** All attentions in the LLM are replaced by flash-attention [17] during training.
- **p. 6 / Model - extractive body cue:** We pass the projected segmentation queries from the MLLM to the Mask3D segmentation decoder as the positional query input for the model, instead of its ...
- **p. 5 / 4.2. Training Objective - extractive body cue:** To achieve this, we utilize an auto-regressive cross-entropy loss LCE for text generation, along with binary cross-entropy loss LBCE and Dice loss LDice [20] for ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are as follows: • We introduce Part-Aware Point Grounded Description (PaPGD), a novel task that challenges 3D MLLMs to achieve detailed ...
- **p. 2 / 1. Introduction - extractive body cue:** To tackle the challenges posed by PaPGD, we propose Kestrel, a novel part-aware 3D MLLM designed to capture the intricate spatial and compositional details required ...
- **p. 3 / 4. Method - extractive body cue:** To bridge this gap, we propose Kestrel, which combines a 3D MLLM with a query refinement mechanism to enable fine-grained part segmentation along with detailed ...

## Source Evidence Cues

- **p. 4 / 4.1. Kestrel - extractive body cue:** As shown in Figure 2, Kestrel is composed of a point encoder, an LLM, a point feature propagation module (PFPM), and a segmentation decoder.
- **p. 4 / 4.1. Kestrel - extractive body cue:** Each upsampled feature is combined with intermediate segmentation decoder queries, qi(i ↑{1, 2}), which will be projected through an MLP and then combined by a ...
- **p. 3 / 4. Method - extractive body cue:** 4.1, we formally introduce Kestrel as a part-aware point grounding 3D MLLM, followed by a detailed explanation of our training objective in Sec.
- **p. 5 / 4.1. Kestrel - extractive body cue:** This masked attention process allows each query to only attend to its relevant part features at each upsampled level, leading to accurate segmentation masks.
- **p. 5 / 4.2. Training Objective - extractive body cue:** The overall training loss for Kestrel is defined as Llang = wCE · LCE(ˆytxt, ytxt) (5) Lmask = wBCE · LBCE(ˆymask, ymask) +wDice · LDice(ˆymask, ...
- **p. 6 / Model - extractive body cue:** All attentions in the LLM are replaced by flash-attention [17] during training.
- **p. 6 / Model - extractive body cue:** We pass the projected segmentation queries from the MLLM to the Mask3D segmentation decoder as the positional query input for the model, instead of its ...
- **Detected method headings:** 4. Method (p. 3); Model (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | As shown in Figure 2, Kestrel is composed of a point encoder, an LLM, a point feature propagation module (PFPM), and a ... | p. 4 (4.1. Kestrel), p. 4 (4.1. Kestrel) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Each upsampled feature is combined with intermediate segmentation decoder queries, qi(i ↑{1, 2}), which will be projected through an MLP and then ... | p. 4 (4.1. Kestrel), p. 3 (4. Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | 4.1, we formally introduce Kestrel as a part-aware point grounding 3D MLLM, followed by a detailed explanation of our training objective in ... | p. 3 (4. Method), p. 5 (4.1. Kestrel) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4.2. Training Objective - extractive body cue:** To achieve this, we utilize an auto-regressive cross-entropy loss LCE for text generation, along with binary cross-entropy loss LBCE and Dice loss LDice [20] for ...
- **p. 3 / 4. Method - extractive body cue:** 4.1, we formally introduce Kestrel as a part-aware point grounding 3D MLLM, followed by a detailed explanation of our training objective in Sec.
- **p. 5 / 4.2. Training Objective - extractive body cue:** (7) In this formulation, wCE, wBCE, and wDice are the weights assigned to each loss term.
- **p. 4 / 4.1. Kestrel - extractive body cue:** We then incorporate the point feature propagation module (PFPM) [45] to progressively upsample the features from E to intermediate features fp1, fp2, and finally fp3, ...
- **p. 6 / Model - extractive body cue:** Additionally, we utilize AdamW [38] optimizer with the learning rate and weight decay set to 0.00009 and 0.0 respectively for the LLM and 0.0002, 0.0 ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (4. Method), p. 5 (4.2. Training Objective), p. 5 (4.2. Training Objective).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | point, encoder, LLM, take, point-aware, instruction, cloud, input, generating, detailed, part-level, description, Segmentation, Decoder | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | point, encoder, LLM, take, point-aware, instruction, cloud, input, generating, detailed | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summary, contributions, follows, introduce, Part-Aware, Point, Grounded, Description, PaPGD, novel | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | achieve, utilize, auto-regressive, cross-entropy, loss, LCE, text, generation, along, binary | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 4.1. Kestrel - extractive body cue:** The point encoder and LLM take a point-aware instruction and point cloud as input, generating a detailed part-level description of the point cloud.
- **p. 4 / 4. Method - extractive body cue:** The 3D Segmentation Decoder extracts the output embedding of the [SEG] token from the output hidden states of the 3D MLLM.
- **p. 2 / 1. Introduction - extractive body cue:** Recognizing that no existing dataset supports training and evaluating this fine-grained 3D vision-language understanding, we propose the 3DCoMPaT Grounded Instructions (3DCoMPaT-GrIn) dataset.
- **p. 1 / 1. Introduction - extractive body cue:** Given an input point cloud, the model is tasked with predicting a grounded description - text that provides a detailed interpretation of the 3D object.
- **p. 2 / 1. Introduction - extractive body cue:** The point encoder extracts detailed features from the input point cloud without relying on extensive global feature embeddings.
- **p. 1 / 1. Introduction - extractive body cue:** Each part-level phrase in this generated text (e.g., "backrest" and "seat support") is linked to a point-wise segmentation mask, challenging the model's capability for part-aware ...
- **p. 6 / Model - extractive body cue:** We pass the projected segmentation queries from the MLLM to the Mask3D segmentation decoder as the positional query input for the model, instead of its ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | VisionLLM [61] takes a step further by predicting object masks as polygons. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | These tasks are essential for evaluating the capability of 3D MLLMs to generate both fine-grained segmentation masks and comprehensive grounded descriptions, a ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | The training is done on 4 A100 GPUs for 5 epochs for all experiments with a batch size of 16. | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 4. Method - extractive body cue:** 4.1, we formally introduce Kestrel as a part-aware point grounding 3D MLLM, followed by a detailed explanation of our training objective in Sec.
- **p. 5 / 4.2. Training Objective - extractive body cue:** The overall training loss for Kestrel is defined as Llang = wCE · LCE(ˆytxt, ytxt) (5) Lmask = wBCE · LBCE(ˆymask, ymask) +wDice · LDice(ˆymask, ...
- **p. 6 / Model - extractive body cue:** All attentions in the LLM are replaced by flash-attention [17] during training.
- **p. 6 / Model - extractive body cue:** The training is done on 4 A100 GPUs for 5 epochs for all experiments with a batch size of 16.
- **p. 7 / 5.4. Application - extractive body cue:** We evaluate Kestrel's ability to generalize to new domains by testing it on Objaverse using a checkpoint trained only on 3DCoMPaT-GrIn.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Figure, Kestrel, composed, point, encoder, LLM, feature, propagation, module, PFPM, segmentation, decoder, upsampled, combined, intermediate, queries, will, projected, through, MLP.
- **Relevant PDF headings:** 4. Method (p. 3); Model (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | 5.4, we showcase the robustness and potential applications of Kestrel when the point cloud distribution deviates from the training data, including scenarios ... | p. 5 (5. Experiments), p. 5 (5. Experiments) |
| Semantic / temporal fusion | We conduct ablation experiments on our training strategy and Kestrel to explore the effects of design choices, as detailed in Sec. | p. 5 (5. Experiments), p. 6 (Figure/Table caption) |
| Robot query / planning handoff | 5.2 investigates the performance of Kestrel in single-part grounding from both direct segmentation (3DCoMPaT-GrIn and PartNetMobility [63]) and reasoning segmentation perspectives (3DCoMPaT-GrIn ... | p. 5 (5. Experiments), p. 5 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive body cue:** Table 5. Ablation on the query refinement levels. Evaluates the effect of changing the number of query refinement stages on the mIoU performance of each ...
- **p. 5 / 5. Experiments - extractive body cue:** We conduct ablation experiments on our training strategy and Kestrel to explore the effects of design choices, as detailed in Sec.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. 3D Composition-Aware Language Comprehension (3D-CALC). Part, material, and composition understanding eval- uated based on accuracy on 3DCoMPaT-GrIn. ing. We pretrain Kestrel on PointLLM's ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Part-Aware Point Grounded Description Results. Comparison of models on language understanding and multi-part grounding. Results marked with ! indicate metrics for the model ...
- **p. 8 / 6. Conclusion - extractive body cue:** Our work establishes a robust benchmark for part-aware 3D vision-language understanding, paving the way for future research in finegrained 3D object interaction and grounding.
- **p. 5 / 5. Experiments - extractive body cue:** 5.4, we showcase the robustness and potential applications of Kestrel when the point cloud distribution deviates from the training data, including scenarios where the point ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. Real-Word Demos. Kestrel shows a certain degree of robustness to noisy and incomplete real-world inputs. # Refinement Levels Grounded Desc. Direct Segmentation Reasoning ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (4.1. Kestrel), p. 4 (4.1. Kestrel), p. 3 (4. Method), p. 5 (4.1. Kestrel), p. 5 (4.2. Training Objective), p. 6 (Model), objective p. 5 (4.2. Training Objective), p. 3 (4. Method), p. 5 (4.2. Training Objective), p. 4 (4.1. Kestrel), p. 6 (Model), temporal p. 2 (2. Related Work), p. 2 (1. Introduction), p. 7 (5.2. Single-Part Segmentation Grounding), p. 8 (5.4. Application).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
