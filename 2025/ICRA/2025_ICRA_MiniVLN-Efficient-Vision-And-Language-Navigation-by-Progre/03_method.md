# Method - MiniVLN: Efficient Vision-And-Language Navigation by Progressive Knowledge Distillation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.proceedings.com/content/081/081087webtoc.pdf; PDF retrieval source: https://arxiv.org/pdf/2409.18800v1. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (IV. METHOD), p. 4 (IV. METHOD), p. 3 (IV. METHOD), p. 3 (IV. METHOD), p. 5 (IV. METHOD), p. 5 (IV. METHOD)): The MSE loss between the outputs of the teacher and student models for this panoramic observation is computed as: Lpano = MSE(hT t , hS t Wr) (7) where Wr ...

## Method Body Digest

- **p. 4 / IV. METHOD - extractive PDF cue:** The MSE loss between the outputs of the teacher and student models for this panoramic observation is computed as: Lpano = MSE(hT t , hS ...
- **p. 4 / IV. METHOD - extractive PDF cue:** Distillation Loss The language encoder and panorama encoder in Scalepre consists of NL = 9 and NP = 2 transformer blocks respectively.
- **p. 3 / IV. METHOD - extractive PDF cue:** Knowledge Distillation During Pretraining Phase In order to distill knowledge encapsulated within the teacher model's learned features, we conduct Embedding Distillation, Attention-based Distillation, and Hidden ...
- **p. 3 / IV. METHOD - extractive PDF cue:** On this premise, we propose MiniVLN with two distinct distillation strategies tailored for each training phase.
- **p. 5 / IV. METHOD - extractive PDF cue:** Compared to TinyBERT, the distillation method proposed in this paper includes certain optimizations.
- **p. 5 / IV. METHOD - extractive PDF cue:** Finally, the overall knowledge distillation loss Lft kd is the sum of these three types of distillation losses: Lft kd = Ltxt + Lpano + ...
- **p. 5 / IV. METHOD - extractive PDF cue:** Method Val Unseen Test Unseen Param(M)↓ SR↑ SPL↑ SR↑ SPL↑ PREVALENT [10] 57 53 54 51 209.83 RecBERT [12] 63 57 63 57 159.99 HAMT ...
- **p. 3 / IV. METHOD - extractive PDF cue:** Embedding Distillation involves calculating the Mean Squared Error (MSE) loss between the embedding layers of the teacher model and the student model: Lemb = MSE(Etea, ...

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** In this work, our main contributions are: • We introduce MiniVLN, a high-performance and lowcomplexity model specifically designed for deployment on resource-constrained devices. • To ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Our method incorporates knowledge distillation in both the pre-training and fine-tuning stages, leading to the final student model MiniVLN.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** In contrast to approaches [14], [32] that apply distillation solely during the pre-training phase or only during the finetuning phase, we introduce a two-stage distillation ...

## Source Evidence Cues

- **p. 4 / IV. METHOD - extractive PDF cue:** The MSE loss between the outputs of the teacher and student models for this panoramic observation is computed as: Lpano = MSE(hT t , hS ...
- **p. 4 / IV. METHOD - extractive PDF cue:** Distillation Loss The language encoder and panorama encoder in Scalepre consists of NL = 9 and NP = 2 transformer blocks respectively.
- **p. 3 / IV. METHOD - extractive PDF cue:** Knowledge Distillation During Pretraining Phase In order to distill knowledge encapsulated within the teacher model's learned features, we conduct Embedding Distillation, Attention-based Distillation, and Hidden ...
- **p. 3 / IV. METHOD - extractive PDF cue:** On this premise, we propose MiniVLN with two distinct distillation strategies tailored for each training phase.
- **p. 5 / IV. METHOD - extractive PDF cue:** Compared to TinyBERT, the distillation method proposed in this paper includes certain optimizations.
- **p. 5 / IV. METHOD - extractive PDF cue:** Finally, the overall knowledge distillation loss Lft kd is the sum of these three types of distillation losses: Lft kd = Ltxt + Lpano + ...
- **Detected method headings:** IV. METHOD (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | The MSE loss between the outputs of the teacher and student models for this panoramic observation is computed as: Lpano = MSE(hT ... | p. 4 (IV. METHOD), p. 4 (IV. METHOD) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | Distillation Loss The language encoder and panorama encoder in Scalepre consists of NL = 9 and NP = 2 transformer blocks respectively. | p. 4 (IV. METHOD), p. 3 (IV. METHOD) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | Knowledge Distillation During Pretraining Phase In order to distill knowledge encapsulated within the teacher model's learned features, we conduct Embedding Distillation, Attention-based ... | p. 3 (IV. METHOD), p. 3 (IV. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / IV. METHOD - extractive PDF cue:** Method Val Unseen Test Unseen Param(M)↓ SR↑ SPL↑ SR↑ SPL↑ PREVALENT [10] 57 53 54 51 209.83 RecBERT [12] 63 57 63 57 159.99 HAMT ...
- **p. 3 / IV. METHOD - extractive PDF cue:** Embedding Distillation involves calculating the Mean Squared Error (MSE) loss between the embedding layers of the teacher model and the student model: Lemb = MSE(Etea, ...
- **p. 4 / IV. METHOD - extractive PDF cue:** The loss function is then designed as: Lfuse = CE Ztea t , Zstu t  (8)
- **p. 4 / IV. METHOD - extractive PDF cue:** Distillation Loss The language encoder and panorama encoder in Scalepre consists of NL = 9 and NP = 2 transformer blocks respectively.
- **p. 5 / IV. METHOD - extractive PDF cue:** Finally, the overall knowledge distillation loss Lft kd is the sum of these three types of distillation losses: Lft kd = Ltxt + Lpano + ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 3 (IV. METHOD), p. 4 (IV. METHOD), p. 4 (IV. METHOD), p. 5 (IV. METHOD), p. 5 (IV. METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | agent, must, learn, policy, predicts, next, action, instruction, navigation, history, current, observation, process, formulated | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | agent, must, learn, policy, predicts, next, action, instruction, navigation, history | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | main, contributions, introduce, MiniVLN, high-performance, lowcomplexity, model, specifically, designed, deployment | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | Val, Unseen, Test, Param, SPL, PREVALENT, RecBERT, HAMT, ADAPT, DUET | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. PRELIMINARIES - extractive PDF cue:** The agent must learn a policy π that predicts the next action based on the instruction I, the agent's navigation history, and the current observation ...
- **p. 2 / III. PRELIMINARIES - extractive PDF cue:** This process is formulated as a partially observable Markov decision process (POMDP), where the agent's future observations are conditionally independent of past observations given the ...
- **p. 3 / IV. METHOD - extractive PDF cue:** While in the fine-tuning phase, the agent iteratively predicts actions according to the instruction and its actual navigation Fig.
- **p. 4 / IV. METHOD - extractive PDF cue:** Hidden States-based Distillation aims to enable the student model to distill knowledge from the output features of teacher model's transformer block: Lhidn = MSE(HT , ...
- **p. 4 / IV. METHOD - extractive PDF cue:** The MSE loss between the outputs of the teacher and student models for this panoramic observation is computed as: Lpano = MSE(hT t , hS ...
- **p. 2 / III. PRELIMINARIES - extractive PDF cue:** The goal of the agent is to interpret a given natural language instruction I = {wi}L i=1, where L is the length of the instruction, ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** ScaleVLN [37], leveraging 1200+ environments and synthesizing 4.9 million instruction-trajectory pairs, exhibits significant improvements in generalization and achieves stateof-the-art results.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | At time step t, the agent receives a panoramic observation Ot = {ot,i, at,i}K i=1 from its current viewpoint Vt. | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | Panorama Encoder At time step t, a pre-trained vision transformer (ViT) [7] is first applied to extract feature vectors Ev from panoramic ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | For instance, RecBERT [12] utilizes the [CLS] token within the transformer as a recurrent state to record navigation history, while HAMT [4] ... | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / IV. METHOD - extractive PDF cue:** Knowledge Distillation During Pretraining Phase In order to distill knowledge encapsulated within the teacher model's learned features, we conduct Embedding Distillation, Attention-based Distillation, and Hidden ...
- **p. 3 / IV. METHOD - extractive PDF cue:** On this premise, we propose MiniVLN with two distinct distillation strategies tailored for each training phase.
- **p. 6 / V. EXPERIMENTS - extractive PDF cue:** The inference time comparison between ScaleVLN and MiniVLN with CPU.
- **p. 6 / V. EXPERIMENTS - extractive PDF cue:** Deployment To simulate deployment, we run the complete inference process of the model on the Intel i9-14900HX CPU of a mobile laptop.
- **p. 5 / V. EXPERIMENTS - extractive PDF cue:** 3) Training Details: We trained on the R2R dataset for 200,000 iterations with a batch size of 16, and on the REVERIE dataset for 20,000 ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** MSE, loss, between, outputs, teacher, student, models, panoramic, observation, computed, Lpano, where, another, learned, weight, matrix, adapts, model, representation, match.
- **Relevant PDF headings:** IV. METHOD (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | On the R2R datasets, the results, as shown in Figure 4, reveal that the non-distilled model achieves an SR of only 74.16 ... | p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Global / local decision | Fig. 1. Model parameters versus accuracy comparison on R2R dataset among state-of-the-art VLN methods. Compared to other student models, MiniVLN achieves the ... | p. 1 (Figure/Table caption), p. 5 (V. EXPERIMENTS) |
| Motion execution / recovery | 2) Evaluation Metrics: We assess agent performance using standard VLN metrics, including Success Rate (SR) and Success weighted by Path Length (SPL). | p. 5 (V. EXPERIMENTS), p. 1 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 6 / V. EXPERIMENTS - extractive PDF cue:** Additionally, ablation experiments on the REVERIE dataset, detailed in Table III, illustrate the contributions of each stage of the distillation process, highlighting the effectiveness of ...
- **p. 5 / V. EXPERIMENTS - extractive PDF cue:** Ablation Study 1) The Effect of Two-Stage Distillation: To demonstrate the effectiveness of our two-stage distillation process, we conduct experiments using TinyBERT with the model ...
- **p. 6 / V. EXPERIMENTS - extractive PDF cue:** Method Validation Unseen Test Unseen Param(M)↓ SR↑ SPL↑ RGS↑ RGSPL↑ SR↑ SPL↑ RGS↑ RGSPL↑ HAMT [4] 32.95 30.20 18.92 17.28 30.40 26.67 14.88 13.08 170.39 ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 4. Ablation of two-stage distillation on the R2R dataset. MiniVLN maintains performance comparable to the teacher model while achieving approximately 4% higher performance than ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2. The overview of two-stage knowledge distillation process for VLN. In the pre-training phase, fine-grained knowledge is distilled, while navigation-specific knowledge is learned during ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 3. Overall framework of MiniVLN. The yellow box represents the teacher model, while the blue box denotes the student model. The orange arrows represent ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (IV. METHOD), p. 4 (IV. METHOD), p. 3 (IV. METHOD), p. 3 (IV. METHOD), p. 5 (IV. METHOD), p. 5 (IV. METHOD), objective p. 5 (IV. METHOD), p. 3 (IV. METHOD), p. 4 (IV. METHOD), p. 4 (IV. METHOD), p. 5 (IV. METHOD), temporal p. 2 (III. PRELIMINARIES), p. 3 (III. PRELIMINARIES), p. 2 (II. RELATED WORK), p. 3 (IV. METHOD), p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
