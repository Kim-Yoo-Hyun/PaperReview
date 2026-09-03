# Method - VITaL Pretraining: Visuo-Tactile Pretraining for Tactile and Non-Tactile Manipulation Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.proceedings.com/content/081/081087webtoc.pdf; PDF retrieval source: https://arxiv.org/pdf/2403.11898v2. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (III. METHODS), p. 3 (III. METHODS), p. 2 (1) Action), p. 2 (1) Action), p. 4 (III. METHODS), p. 4 (III. METHODS)): A vision projection head, pϕV : Z →L, and a tactile projection head, qϕT : Z, P →L, each of which consists of a single layer MLP, map the encoders' ...

## Method Body Digest

- **p. 3 / III. METHODS - extractive body cue:** A vision projection head, pϕV : Z →L, and a tactile projection head, qϕT : Z, P →L, each of which consists of a single ...
- **p. 3 / III. METHODS - extractive body cue:** First, we replaced the stock Resnet vision encoder with the vision encoder from the contrastive pretraining step and added a separate tactile encoder (also from ...
- **p. 2 / 1) Action - extractive body cue:** Chunking Transformers: Action Chunking Transformers (ACT) [10] train a Conditional Variational Auto Encoder (CVAE) built upon a transformer backbone to predict a series of actions ...
- **p. 2 / 1) Action - extractive body cue:** 2) Diffusion Policy: To address the challenge of complex multi-modal action spaces, Diffusion Policy [11] formulates control policies as Denoising Diffusion Probabilistic Models (DDPM) [35], ...
- **p. 4 / III. METHODS - extractive body cue:** We use an observation horizon of 1 and an action prediction horizon of 20.
- **p. 4 / III. METHODS - extractive body cue:** We use the CNN-based implementation of this model, where a 1D temporal CNN models the conditional action distribution.
- **p. 3 / III. METHODS - extractive body cue:** The encoders (and the projection heads) are then trained to maximize the cross-modality dot-product similarity of latent representations from the same scene while minimizing the ...
- **p. 2 / 1) Action - extractive body cue:** This network is trained to predict noise added to action sequence samples from the training dataset, minimizing the loss function: Loss = MSE(ϵk, ϵθ(Ot, At ...

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** Next, we propose a new methodology for using tactile data in imitation learning: VITaL (Vison-only Imitation using Tactile Latent) pretraining, in which we discard the ...
- **p. 3 / III. METHODS - extractive body cue:** A vision projection head, pϕV : Z →L, and a tactile projection head, qϕT : Z, P →L, each of which consists of a single ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our primary contribution is a pretraining strategy for these SOTA imitation learning frameworks, leveraging the multimodal nature of our data to incorporate a temporalbased visual-tactile ...

## Source Evidence Cues

- **p. 3 / III. METHODS - extractive body cue:** A vision projection head, pϕV : Z →L, and a tactile projection head, qϕT : Z, P →L, each of which consists of a single ...
- **p. 3 / III. METHODS - extractive body cue:** First, we replaced the stock Resnet vision encoder with the vision encoder from the contrastive pretraining step and added a separate tactile encoder (also from ...
- **p. 2 / 1) Action - extractive body cue:** Chunking Transformers: Action Chunking Transformers (ACT) [10] train a Conditional Variational Auto Encoder (CVAE) built upon a transformer backbone to predict a series of actions ...
- **p. 2 / 1) Action - extractive body cue:** 2) Diffusion Policy: To address the challenge of complex multi-modal action spaces, Diffusion Policy [11] formulates control policies as Denoising Diffusion Probabilistic Models (DDPM) [35], ...
- **p. 4 / III. METHODS - extractive body cue:** We use an observation horizon of 1 and an action prediction horizon of 20.
- **p. 4 / III. METHODS - extractive body cue:** We use the CNN-based implementation of this model, where a 1D temporal CNN models the conditional action distribution.
- **Detected method headings:** III. METHODS (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multi-modal contact encoding | vision과 touch를 contact feature로 결합한다 | tactile image/force, vision, proprioception | tactile encoder, calibration, fusion 또는 temporal feature extraction을 수행 | contact feature/state | A vision projection head, pϕV : Z →L, and a tactile projection head, qϕT : Z, P →L, each of which consists ... | p. 3 (III. METHODS), p. 3 (III. METHODS) |
| Contact / dynamics inference | contact mode와 object response를 추정한다 | contact feature와 action history | mode classifier, force/dynamics model 또는 state estimator를 update | contact/force prediction | First, we replaced the stock Resnet vision encoder with the vision encoder from the contrastive pretraining step and added a separate tactile ... | p. 3 (III. METHODS), p. 2 (1) Action) |
| Force-aware action correction | interaction feedback으로 command를 보정한다 | predicted contact와 current wrench/touch | policy/control law가 action, force 또는 grasp를 재계산 | contact-safe action/torque | Chunking Transformers: Action Chunking Transformers (ACT) [10] train a Conditional Variational Auto Encoder (CVAE) built upon a transformer backbone to predict a ... | p. 2 (1) Action), p. 2 (1) Action) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / III. METHODS - extractive body cue:** The encoders (and the projection heads) are then trained to maximize the cross-modality dot-product similarity of latent representations from the same scene while minimizing the ...
- **p. 2 / 1) Action - extractive body cue:** This network is trained to predict noise added to action sequence samples from the training dataset, minimizing the loss function: Loss = MSE(ϵk, ϵθ(Ot, At ...
- **p. 3 / III. METHODS - extractive body cue:** During training, the contrastive loss between tactile and visual embeddings is calculated separately for each camera observation, and the resulting losses are combined and used ...
- **p. 2 / 1) Action - extractive body cue:** A strong KL divergence term in the loss function encourages the network to avoid over-reliance on the latent variable.
- **p. 4 / III. METHODS - extractive body cue:** We use an observation horizon of 1 and an action prediction horizon of 20.
- **p. 4 / III. METHODS - extractive body cue:** The network is queried each timestep, and all action predictions for that timestep are ensembled using a weighted average.
- **Formal bridge:** visual/tactile/proprioceptive contact history -> contact-aware action/force -> contact prediction/control error -> slip/contact success and safe interaction.
- **Equation/algorithm anchors:** p. 3 (III. METHODS), p. 2 (1) Action), p. 2 (1) Action), p. 3 (III. METHODS).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Chunking, Transformers, Action, ACT, train, Conditional, Variational, Auto, Encoder, CVAE, built, upon, transformer, backbone | tactile image/force, vision과 proprioceptive history | body cue; exact tensor/frame verify |
| State/latent | Chunking, Transformers, Action, ACT, train, Conditional, Variational, Auto, Encoder, CVAE | contact geometry, force state 또는 latent dynamics | body cue; notation verify |
| Action/output | Next, methodology, tactile, data, imitation, learning, VITaL, Vison-only, Latent, pretraining | grasp/contact action, force command 또는 object motion | body cue; unit/decoder verify |
| Objective/constraint | encoders, projection, heads, then, trained, maximize, cross-modality, dot-product, similarity, latent | contact prediction/control error | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1) Action - extractive body cue:** Chunking Transformers: Action Chunking Transformers (ACT) [10] train a Conditional Variational Auto Encoder (CVAE) built upon a transformer backbone to predict a series of actions ...
- **p. 4 / III. METHODS - extractive body cue:** 2) Diffusion Policy: Our approach to diffusion policy was based on the implementation by [11] that generates action sequences conditioned on observations with DDPM.
- **p. 2 / 1) Action - extractive body cue:** 2) Diffusion Policy: To address the challenge of complex multi-modal action spaces, Diffusion Policy [11] formulates control policies as Denoising Diffusion Probabilistic Models (DDPM) [35], ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this step, a tactile encoder and an image encoder are trained to project their respective input modalities onto a shared latent space, with the ...
- **p. 4 / III. METHODS - extractive body cue:** Previous works using GelSight as a control policy input found that using processed data, such as strain information, out-performed directly using RGB images [39].
- **p. 3 / III. METHODS - extractive body cue:** Imitation Learning Frameworks We implemented two imitation learning frameworks to study the impact of visuo-tactile pretraining on learning manipulation tasks: Action Chunking Transformer (ACT) [10] ...
- **p. 5 / III. METHODS - extractive body cue:** GelSight sensor outputs, showing the RGB images from the GelSight's camera and the processed strain data for both the covered and uncovered gelsight.
- **Normalized interface:** observation=tactile image/force, vision과 proprioceptive history; state=contact geometry, force state 또는 latent dynamics; output/action=grasp/contact action, force command 또는 object motion.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | contact episode 또는 action chunk horizon; contact event timing이 핵심이다. | A series of visual observations V1, V2, ..., VN and tactile observations T1, T2, ..., TN are collected, and the vision encoder ... | episode/sequence/action-chunk boundary |
| Rate / latency | tactile sampling/control loop가 visual policy rate와 다를 수 있다; numeric values 확인 필요. | ACT (left) is trained as an autoencoder, predicting a sequence of actions at each timestep (at). | Hz/fps, inference time and control rate |
| Memory | recent tactile/force history와 visual state; recurrent memory 여부 확인 필요. | not recovered | window and reset |
| Compute | sensor fusion, contact inference와 high-frequency correction이 latency를 결정한다. | The data collection system was run at 10 Hz. | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / III. METHODS - extractive body cue:** First, we replaced the stock Resnet vision encoder with the vision encoder from the contrastive pretraining step and added a separate tactile encoder (also from ...
- **p. 2 / 1) Action - extractive body cue:** Chunking Transformers: Action Chunking Transformers (ACT) [10] train a Conditional Variational Auto Encoder (CVAE) built upon a transformer backbone to predict a series of actions ...
- **p. 6 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** We used the same run parameters as the cable plugging task, with 100 demos collected, an 80/20 train/test split, and noise added to the predicted ...
- **p. 3 / III. METHODS - extractive body cue:** A series of visual observations V1, V2, ..., VN and tactile observations T1, T2, ..., TN are collected, and the vision encoder and tactile encoder ...
- **p. 2 / 1) Action - extractive body cue:** The use of an auto-encoder for this task helps to reduce the negative effects of multi-modal distributions in the training data, as the latent variable ...
- **p. 2 / 1) Action - extractive body cue:** Chunking Transformers: Action Chunking Transformers (ACT) [10] train a Conditional Variational Auto Encoder (CVAE) built upon a transformer backbone to predict a series of actions ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** vision, projection, head, tactile, consists, single, layer, MLP, encoders, feature, vectors, shared, latent, space, R512, First, replaced, stock, Resnet, encoder.
- **Relevant PDF headings:** III. METHODS (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multi-modal contact encoding | In this task, the robot has to navigate to a USB cable, unplug it from its holder, and plug it into the ... | p. 5 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION) |
| Contact / dynamics inference | Interestingly, the nonpretrained ACT model outperformed the pretrained model in this task. | p. 5 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION) |
| Force-aware action correction | This is significantly higher than the 20% and 45% success rates that learning from vision only with ACT and diffusion policy (respectively) ... | p. 5 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION) |

## Failure and Ablation Link

- **p. 6 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** This result illustrates the key benefit of using visuo-tactile pretraining on a vision-only agent: the agent gains a significant performance boost from tactile data without ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4. Expermental Setup. A GelSight captures tactile observations, while 6 Realsense cameras observe the scene (only two can be seen above; three are out ...
- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** Finally, we evaluated the models without vision input (only tactile and positional data).
- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** Interestingly, the nonpretrained ACT model outperformed the pretrained model in this task.
- **p. 6 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** Block Stacking In addition to cable plugging, we also evaluated our pretraining strategy on two block-stacking tasks to see how well the system performed on ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Diagram of our approach. First, a vision encoder and a tactile encoder are pretrained on the collected demonstrations using a temporally informed multi-modal ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. Contrastive loss visualization. A series of visual observations V1, V2, ..., VN and tactile observations T1, T2, ..., TN are collected, and the ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (III. METHODS), p. 3 (III. METHODS), p. 2 (1) Action), p. 2 (1) Action), p. 4 (III. METHODS), p. 4 (III. METHODS), objective p. 3 (III. METHODS), p. 2 (1) Action), p. 3 (III. METHODS), p. 2 (1) Action), p. 4 (III. METHODS), p. 4 (III. METHODS), temporal p. 3 (III. METHODS), p. 4 (III. METHODS), p. 5 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION), p. 1 (I. INTRODUCTION), p. 2 (1) Action).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
