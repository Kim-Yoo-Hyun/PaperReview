# Method - ScanQA: 3D Question Answering for Spatial Scene Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2112.10482; PDF retrieval source: https://arxiv.org/pdf/2112.10482. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (4. ScanQA Model), p. 5 (4. ScanQA Model), p. 5 (4. ScanQA Model), p. 6 (Model), p. 6 (Model), p. 7 (Model)): Inspired by the architecture of deep modular co-attention networks of MCAN [51], often used for VQA, we use transformer blocks [44] to represent the relationships between object proposals and between ...

## Method Body Digest

- **p. 4 / 4. ScanQA Model - extractive PDF cue:** Inspired by the architecture of deep modular co-attention networks of MCAN [51], often used for VQA, we use transformer blocks [44] to represent the relationships ...
- **p. 5 / 4. ScanQA Model - extractive PDF cue:** In addition, we use transformer decoder layers to represent the features of object proposals related to the question words by using the final output of ...
- **p. 5 / 4. ScanQA Model - extractive PDF cue:** Given a point cloud and RGB frame sequence that capture indoor scenes, the QA model outputs a corresponding answer by fusing 3D and language information ...
- **p. 6 / Model - extractive PDF cue:** We used a bottom-up top-down attention model [4] to extract the appearance features of the objects.
- **p. 6 / Model - extractive PDF cue:** The proposed method uses some of the modules used in MCAN, such as transformer encoder and decoder layers, to create 3D and language features.
- **p. 7 / Model - extractive PDF cue:** Thus, we used a pretrained ScanRefer model to identify the object corresponding to the question and then applied 2D-QA (MCAN) to the image surrounding the ...
- **p. 4 / 4. ScanQA Model - extractive PDF cue:** The 3D & language fusion layer combines multiple 3D object features guided by language information using transformerbased encoder and decoder layers [44, 51].
- **p. 5 / 4. ScanQA Model - extractive PDF cue:** To consider multiple answers, we compute final scores with the binary cross-entropy (BCE) loss function to train the module.

## Design Rationale

- **p. 1 / 1. Introduction - extractive PDF cue:** We introduce the new task of question answering for 3D modeling.
- **p. 2 / 1. Introduction - extractive PDF cue:** We present the overview of the task in Fig.
- **p. 2 / 1. Introduction - extractive PDF cue:** In this paper, we propose a 3D question answering (3DQA) task that uses 3D spatial information instead of 2D images to comprehend real-world information through ...

## Source Evidence Cues

- **p. 4 / 4. ScanQA Model - extractive PDF cue:** Inspired by the architecture of deep modular co-attention networks of MCAN [51], often used for VQA, we use transformer blocks [44] to represent the relationships ...
- **p. 5 / 4. ScanQA Model - extractive PDF cue:** In addition, we use transformer decoder layers to represent the features of object proposals related to the question words by using the final output of ...
- **p. 5 / 4. ScanQA Model - extractive PDF cue:** Given a point cloud and RGB frame sequence that capture indoor scenes, the QA model outputs a corresponding answer by fusing 3D and language information ...
- **p. 6 / Model - extractive PDF cue:** We used a bottom-up top-down attention model [4] to extract the appearance features of the objects.
- **p. 6 / Model - extractive PDF cue:** The proposed method uses some of the modules used in MCAN, such as transformer encoder and decoder layers, to create 3D and language features.
- **p. 7 / Model - extractive PDF cue:** Thus, we used a pretrained ScanRefer model to identify the object corresponding to the question and then applied 2D-QA (MCAN) to the image surrounding the ...
- **p. 4 / 4. ScanQA Model - extractive PDF cue:** The 3D & language fusion layer combines multiple 3D object features guided by language information using transformerbased encoder and decoder layers [44, 51].
- **Detected method headings:** 4. ScanQA Model (p. 4); Model (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Inspired by the architecture of deep modular co-attention networks of MCAN [51], often used for VQA, we use transformer blocks [44] to ... | p. 4 (4. ScanQA Model), p. 5 (4. ScanQA Model) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | In addition, we use transformer decoder layers to represent the features of object proposals related to the question words by using the ... | p. 5 (4. ScanQA Model), p. 5 (4. ScanQA Model) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Given a point cloud and RGB frame sequence that capture indoor scenes, the QA model outputs a corresponding answer by fusing 3D ... | p. 5 (4. ScanQA Model), p. 6 (Model) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4. ScanQA Model - extractive PDF cue:** To consider multiple answers, we compute final scores with the binary cross-entropy (BCE) loss function to train the module.
- **p. 5 / 4. ScanQA Model - extractive PDF cue:** To answer the 3D scene content, we additionally use the answer loss Lans of the answer classification module.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (4. ScanQA Model), p. 5 (4. ScanQA Model).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | D-QA, formalized, follows, given, inputs, point, cloud, question, about, scene, model, aims, output, semantically | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | D-QA, formalized, follows, given, inputs, point, cloud, question, about, scene | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | introduce, task, question, answering, modeling, present, overview, Fig, DQA, uses | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | consider, multiple, answers, compute, final, scores, binary, cross-entropy, BCE, loss | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 4. ScanQA Model - extractive PDF cue:** The 3D-QA is formalized as follows: given inputs of the point cloud p ∈P and question q ∈Q about the 3D scene, the 3D-QA model ...
- **p. 4 / 4. ScanQA Model - extractive PDF cue:** We project a series of output states from the LSTM using a nonlinear layer with GELUs [21] activation to obtain the contextualized word representation Q′ ...
- **p. 5 / 4. ScanQA Model - extractive PDF cue:** Given a point cloud and RGB frame sequence that capture indoor scenes, the QA model outputs a corresponding answer by fusing 3D and language information ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Given inputs of an entire 3D modeling and a linguistic question, models predict an answer phrase and the corresponding 3D-bounding boxes. suitcase located?", the existing ...
- **p. 5 / 4. ScanQA Model - extractive PDF cue:** Subsequently, the final outputs of the transformer layers Qenc and V dec are fused by a fusion layer that uses twolayer multi-layer perceptron (MLP) with ...
- **p. 7 / Model - extractive PDF cue:** Specifically, the input to the method is the object proposal feature of ScanRefer for VQA models; subsequently, the model predicts answers based on object box ...
- **p. 7 / Model - extractive PDF cue:** Unlike the ScanQA model, this uses the output of VoteNet separately for object localization and QA modules (although the information for both tasks is mutually ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | This layer encodes the question words {wi}nq i=1 using GloVe [36], and we obtain word representation Q ∈Rnq×300, where nq is the ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Given a point cloud and RGB frame sequence that capture indoor scenes, the QA model outputs a corresponding answer by fusing 3D ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | This layer encodes the question words {wi}nq i=1 using GloVe [36], and we obtain word representation Q ∈Rnq×300, where nq is the ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | We trained the model for 30 epochs until it converged and decreased the learning rate by 0.2 times after 15 epochs. | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / Model - extractive PDF cue:** Thus, we used a pretrained ScanRefer model to identify the object corresponding to the question and then applied 2D-QA (MCAN) to the image surrounding the ...
- **p. 5 / 5.1. Experimental Setup - extractive PDF cue:** To train the ScanQA model, we used Adam [26], a batch size of 16, and an initial learning rate of 5e-4.
- **p. 5 / 5.1. Experimental Setup - extractive PDF cue:** We trained the model for 30 epochs until it converged and decreased the learning rate by 0.2 times after 15 epochs.
- **p. 6 / Model - extractive PDF cue:** We applied pretrained 2D-QA models to these images and computed the answer scores for each image.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Inspired, architecture, deep, modular, co-attention, networks, MCAN, often, VQA, transformer, blocks, represent, relationships, between, object, proposals, question, words, addition, decoder.
- **Relevant PDF headings:** 4. ScanQA Model (p. 4); Model (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | However, as the object IDs for the test set of ScanRefer are not publicly available, we further split the validation set of ... | p. 4 (3.3. Dataset Statistics), p. 3 (3.2. Question-Answer Collection) |
| Semantic / temporal fusion | We compared our ScanQA model with competitive baselines VoteNet+MCAN, ScanRefer+MCAN (pipeline), and ScanRefer+MCAN (end-to-end). | p. 7 (5.2. Quantitative Analysis), p. 7 (5.2. Quantitative Analysis) |
| Robot query / planning handoff | The results indicated that our ScanQA method significantly outperformed all baselines across all data splits over all evaluation metrics. | p. 7 (5.2. Quantitative Analysis), p. 7 (5.2. Quantitative Analysis) |

## Failure and Ablation Link

- **p. 13 / Figure/Table caption - extractive PDF cue:** Table 7. Feature ablation results on ScanQA (multiple) calization scores with the ground true boxes and consider positive predictions for the box with the highest ...
- **p. 7 / 5.2. Quantitative Analysis - extractive PDF cue:** We will clarify this point in the section on the ablation study.
- **p. 7 / 5.2. Quantitative Analysis - extractive PDF cue:** In addition, we observed that our 3D-QA model, ScanQA, is superior to a 2D-QA model, RandomImage+MCAN, which uses an effective pretrained model.
- **p. 3 / 3.2. Question-Answer Collection - extractive PDF cue:** Therefore, we decided to remove such questions as much as possible.
- **p. 3 / 3.1. 3D-QA Task - extractive PDF cue:** This prevents models from answering questions by relying on the textual priors of the trained questions without examining the scene.
- **p. 4 / 3.3. Dataset Statistics - extractive PDF cue:** Therefore, the ScanQA dataset includes two test sets with and without object annotations.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 5. Feature ablation results ground-truth answers. We also included sentence evalua- tion metrics frequently used for image captioning models because some of the questions ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (4. ScanQA Model), p. 5 (4. ScanQA Model), p. 5 (4. ScanQA Model), p. 6 (Model), p. 6 (Model), p. 7 (Model), objective p. 5 (4. ScanQA Model), p. 5 (4. ScanQA Model), temporal p. 4 (4. ScanQA Model), p. 5 (4. ScanQA Model), p. 1 (1. Introduction), p. 4 (4. ScanQA Model).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
