# Method - 3D-AffordanceLLM: Harnessing Large Language Models for Open-Vocabulary Affordance Detection in 3D Worlds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=GThTiuXgDC; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/114156. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 6 (3 METHOD), p. 7 (3 METHOD)): 2, our 3D AffordanceLLM consists of the following modules: a pre-trained point cloud encoder fpe,a projector fproj, a point backbone fPB, an affordance decoder fAFD and a pre-trained large language ...

## Method Body Digest

- **p. 4 / 3 METHOD - extractive body cue:** 2, our 3D AffordanceLLM consists of the following modules: a pre-trained point cloud encoder fpe,a projector fproj, a point backbone fPB, an affordance decoder fAFD ...
- **p. 4 / 3 METHOD - extractive body cue:** 2, primarily consists of two main components: (1) a point cloud multimodal model which is trained to accept point cloud and text inputs and generate ...
- **p. 5 / 3 METHOD - extractive body cue:** Building on the success of learnable query-based methods in object segmentation, we introduce an Affordance Decoder Module (AFD) that leverages a set of learnable output ...
- **p. 6 / 3 METHOD - extractive body cue:** In addition, due to the varying scales of target affordance regions, we propose a sample unbalanced loss factor to enhance the model's learning effectiveness and ...
- **p. 6 / 3 METHOD - extractive body cue:** 3 (a), the object point cloud is processed by a trainable backbone to extract point features fPcloud.The object part descriptions are encoded using a frozen ...
- **p. 7 / 3 METHOD - extractive body cue:** To compute Lmask, we use a combination of per-pixel BCE loss and DICE Loss, with weights λbce and λdice.
- **p. 7 / 3 METHOD - extractive body cue:** Specifically, during IRAS fine-tuning: we use the pretrained checkpoint WfPB and WfMD to initialize the modules fPB and fAFD in our framework 3D-ADLLM as shown ...
- **p. 7 / 3 METHOD - extractive body cue:** The overall objective L is the weighted sum of these losses, determined by λtxt and λmask: L = λtxtLtxt + λmaskLmask.

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** By reforming the label-based semantic segmentation task in the traditional affordance detection paradigm into a natural language-driven reasoning affordance segmentation task, our model enables more ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Specifically, we introduce an additional token, <AFF>, into the original LLM vocabulary.
- **p. 3 / 3 METHOD - extractive body cue:** To address these limitations, we introduce a new paradigm formulated as an Instruction Reasoning Affordance Segmentation (IRAS) task as depicted in Fig.

## Source Evidence Cues

- **p. 4 / 3 METHOD - extractive body cue:** 2, our 3D AffordanceLLM consists of the following modules: a pre-trained point cloud encoder fpe,a projector fproj, a point backbone fPB, an affordance decoder fAFD ...
- **p. 4 / 3 METHOD - extractive body cue:** 2, primarily consists of two main components: (1) a point cloud multimodal model which is trained to accept point cloud and text inputs and generate ...
- **p. 5 / 3 METHOD - extractive body cue:** Building on the success of learnable query-based methods in object segmentation, we introduce an Affordance Decoder Module (AFD) that leverages a set of learnable output ...
- **p. 6 / 3 METHOD - extractive body cue:** In addition, due to the varying scales of target affordance regions, we propose a sample unbalanced loss factor to enhance the model's learning effectiveness and ...
- **p. 6 / 3 METHOD - extractive body cue:** 3 (a), the object point cloud is processed by a trainable backbone to extract point features fPcloud.The object part descriptions are encoded using a frozen ...
- **p. 7 / 3 METHOD - extractive body cue:** To compute Lmask, we use a combination of per-pixel BCE loss and DICE Loss, with weights λbce and λdice.
- **p. 7 / 3 METHOD - extractive body cue:** Specifically, during IRAS fine-tuning: we use the pretrained checkpoint WfPB and WfMD to initialize the modules fPB and fAFD in our framework 3D-ADLLM as shown ...
- **Detected method headings:** 3 METHOD (p. 3); A.1 BASELINE MODELS DETAILS (p. 14)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | 2, our 3D AffordanceLLM consists of the following modules: a pre-trained point cloud encoder fpe,a projector fproj, a point backbone fPB, an ... | p. 4 (3 METHOD), p. 4 (3 METHOD) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | 2, primarily consists of two main components: (1) a point cloud multimodal model which is trained to accept point cloud and text ... | p. 4 (3 METHOD), p. 5 (3 METHOD) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Building on the success of learnable query-based methods in object segmentation, we introduce an Affordance Decoder Module (AFD) that leverages a set ... | p. 5 (3 METHOD), p. 6 (3 METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 7 / 3 METHOD - extractive body cue:** The overall objective L is the weighted sum of these losses, determined by λtxt and λmask: L = λtxtLtxt + λmaskLmask.
- **p. 7 / 3 METHOD - extractive body cue:** Specifically, Ltxt is the auto-regressive cross-entropy loss for text generation, and Lmask is the mask loss for high-quality segmentation.
- **p. 6 / 3 METHOD - extractive body cue:** Thus, we solely employ Dice Loss and Binary CrossEntropy (BCE) loss to guide the segmentation mask prediction.
- **p. 6 / 3 METHOD - extractive body cue:** Finally, f ′Qpart and fPcloud are passed into the Mask Decoder to generate the final part mask Mpart, formulated as: Mpart = MaskDecoder(f ′ Qpart, ...
- **p. 15 / A.4 TRAINING DETAILS - extractive body cue:** To balance training costs with model performance, we selectively sampled a subset of the data based on categories to obtain general segmentation knowledge for objects.
- **p. 5 / 3 METHOD - extractive body cue:** The final prediction ˜zi for the i-th token is the word in the vocabulary with the highest probability, expressed as: ˜zi = arg max w∈vocab ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 7 (3 METHOD), p. 6 (3 METHOD), p. 6 (3 METHOD), p. 7 (3 METHOD), p. 5 (3 METHOD), p. 5 (3 METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Given, complex, reasoning, instruction, query, Qaff, point, cloud, input, Pcloud, feed, them, multimodal, clouds | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Given, complex, reasoning, instruction, query, Qaff, point, cloud, input, Pcloud | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | reforming, label-based, semantic, segmentation, task, traditional, affordance, detection, paradigm, natural | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | overall, objective, weighted, losses, determined, mask, txtLtxt, maskLmask, Specifically, Ltxt | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3 METHOD - extractive body cue:** Given a complex reasoning instruction query Qaff and a point cloud input Pcloud, we feed them into the multimodal point clouds LLM F3D-ADLLM, which outputs ...
- **p. 4 / 3 METHOD - extractive body cue:** Given the input point cloud and query reasoning instruction, the point cloud multimodal model is trained with lora to predict special token <AFF>.
- **p. 5 / 3 METHOD - extractive body cue:** Most current 3D LLM (such as 3D-LLM (Hong et al., 2023a), ShapeLLM (Qi et al., 2024) support 3D scenes or objects and text as input, ...
- **p. 3 / 3 METHOD - extractive body cue:** Given a query reasoning instruction Qa and an object point cloud Pc ∈Rn×3 with N points, the goal of IRAS is to predict a binary ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The IRAS task is designed to output an affordance mask region in response to complex, reasoning-based query text, overcoming the limitations of fixed affordance labels ...
- **p. 4 / 3 METHOD - extractive body cue:** 2, primarily consists of two main components: (1) a point cloud multimodal model which is trained to accept point cloud and text inputs and generate ...
- **p. 14 / A.1 BASELINE MODELS DETAILS - extractive body cue:** For IAGNet (Yang et al., 2023), an affordance detection method that utilizes paired image-point cloud data as input.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | It has been deemed as a critical step in bridging perception and manipulation in the physical world for embodied agents. | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Our framework, 3D AffordanceLLM, as illustrated in Fig. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3 METHOD - extractive body cue:** 2, our 3D AffordanceLLM consists of the following modules: a pre-trained point cloud encoder fpe,a projector fproj, a point backbone fPB, an affordance decoder fAFD ...
- **p. 4 / 3 METHOD - extractive body cue:** 2, primarily consists of two main components: (1) a point cloud multimodal model which is trained to accept point cloud and text inputs and generate ...
- **p. 6 / 3 METHOD - extractive body cue:** 3 (a), the object point cloud is processed by a trainable backbone to extract point features fPcloud.The object part descriptions are encoded using a frozen ...
- **p. 7 / 3 METHOD - extractive body cue:** Specifically, during IRAS fine-tuning: we use the pretrained checkpoint WfPB and WfMD to initialize the modules fPB and fAFD in our framework 3D-ADLLM as shown ...
- **p. 7 / 4 EXPERIMENT - extractive body cue:** For the point encoder (fpe), we adopt Point-BERT (Yu et al., 2022), pre-trained with ULIP-2 (Xue et al., 2024) in the ModelNet dataset (Vishwanath et ...
- **p. 8 / 4 EXPERIMENT - extractive body cue:** In particular, we compare 2 different implementations: (1) w/o PC removes the pre-trained weights fPB and fAFD, directly training our 3D-ADLLM; (2) w/o UL removes ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** AffordanceLLM, consists, following, modules, pre-trained, point, cloud, encoder, projector, fproj, backbone, fPB, affordance, decoder, fAFD, large, language, model, LLM, fllm.
- **Relevant PDF headings:** 3 METHOD (p. 3); A.1 BASELINE MODELS DETAILS (p. 14).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | 3.3, our training data is made up of two types of task data: (1) Referring Object Part Segmentation Dataset: we build this ... | p. 7 (4 EXPERIMENT), p. 7 (4 EXPERIMENT) |
| Action / skill decoding | Detailed baseline model explanation for experiments can be found in Appendix Sect. | p. 7 (4 EXPERIMENT), p. 8 (4 EXPERIMENT) |
| Receding execution / feedback | Notably, 3D AffordanceLLM significantly outperforms the runner-up model (LASO) in terms of mIoU, with improvements of 8.02% and 7.19% on the full ... | p. 8 (4 EXPERIMENT), p. 10 (4 EXPERIMENT) |

## Failure and Ablation Link

- **p. 8 / 4 EXPERIMENT - extractive body cue:** 4.3 ABLATION STUDY Effects of Different Components.
- **p. 8 / 4 EXPERIMENT - extractive body cue:** To investigate the effectiveness of each component in 3DADLLM, we conduct experiments with different variants of 3D-ADLLM.
- **p. 9 / 4 EXPERIMENT - extractive body cue:** Method mIoUi mAcci mPreci mReci mAPi 50 OpenAD-PointNet++ 7.61 65.13 22.47 13.01 0.37 OpenAD-DGCNN 8.02 66.76 15.83 13.52 0.39 LASO 34.49 77.12 56.04 37.88 8.40 ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 6: Results of 3D-ADLLM variants with removing different components.(full-view)
- **p. 9 / 4 EXPERIMENT - extractive body cue:** Once it is removed, the performance, there is a noticeable reduction in the model's performance.
- **p. 15 / A.3 DATA ANALYSIS - extractive body cue:** Full-view: Given an object as 3D point cloud without knowing the affordances supported by the object, the full-shape affordance estimation task aims to estimate the ...
- **p. 7 / 4 EXPERIMENT - extractive body cue:** For pretraining, we split it into single-part segmentation instances.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 6 (3 METHOD), p. 7 (3 METHOD), objective p. 7 (3 METHOD), p. 7 (3 METHOD), p. 6 (3 METHOD), p. 6 (3 METHOD), p. 15 (A.4 TRAINING DETAILS), p. 5 (3 METHOD), temporal p. 3 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 6 (3 METHOD).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
