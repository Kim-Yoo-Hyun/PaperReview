# Method - Sensor-Invariant Tactile Representation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=RnJY9WcpA3; PDF retrieval source: https://arxiv.org/pdf/2502.19638. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 14 (A.1.2 ARCHITECTURE), p. 15 (A.1.2 ARCHITECTURE), p. 14 (A.1.2 ARCHITECTURE), p. 15 (A.1.2 ARCHITECTURE), p. 24 (A.6.1 CONTRIBUTION OF LOSS TERMS), p. 24 (A.6.1 CONTRIBUTION OF LOSS TERMS)): Classification Decoders We use Cross Entropy Loss for this task. • SITR: We unpatchify the output tokens xi to a feature map and pass it through a ResNet-18 network.

## Method Body Digest

- **p. 14 / A.1.2 ARCHITECTURE - extractive body cue:** Classification Decoders We use Cross Entropy Loss for this task. • SITR: We unpatchify the output tokens xi to a feature map and pass it ...
- **p. 15 / A.1.2 ARCHITECTURE - extractive body cue:** Pose Estimation Decoders We use MSE loss for this task. • SITR: We pass 2 tactile images x1 and x2 into the network separately.
- **p. 14 / A.1.2 ARCHITECTURE - extractive body cue:** SITR Training Decoders: During the pre-training phase for SITR, we use two decoders: • Normal Map Reconstruction Decoder: We apply a simple linear projection to ...
- **p. 15 / A.1.2 ARCHITECTURE - extractive body cue:** We also find that unfreezing the ViT pre-trained weights during training improves performance. • T3: We unpatchify the output tokens to a feature map and ...
- **p. 24 / A.6.1 CONTRIBUTION OF LOSS TERMS - extractive body cue:** This evaluation is conducted on the dataset visualized in Figure 6, further highlighting how these two loss terms synergize to improve representation learning.
- **p. 24 / A.6.1 CONTRIBUTION OF LOSS TERMS - extractive body cue:** As shown in Table 5, either loss term independently serves as an effective supervision signal.
- **p. 24 / A.6.1 CONTRIBUTION OF LOSS TERMS - extractive body cue:** We conduct an ablation study to evaluate the contributions of the normal map loss and SCL loss to SITR's performance.
- **p. 14 / A.1.2 ARCHITECTURE - extractive body cue:** We supervise with MSE loss λnormal against the ground truth normal map. • Class Token Decoder: The class token is passed through a linear projection ...

## Design Rationale

- **p. 3 / 1 INTRODUCTION - extractive body cue:** In this section, we introduce our framework for training Sensor-Invariant Tactile Representation (SITR).
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We introduce a novel framework for generating sensor-invariant feature representations from highresolution tactile readings, enabling zero-shot transfer to unseen sensors across multiple downstream tasks.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our framework introduces a novel combination of geometry-preserving supervision, supervised contrastive learning, and sensor-specific calibration images.

## Source Evidence Cues

- **p. 14 / A.1.2 ARCHITECTURE - extractive body cue:** Classification Decoders We use Cross Entropy Loss for this task. • SITR: We unpatchify the output tokens xi to a feature map and pass it ...
- **p. 15 / A.1.2 ARCHITECTURE - extractive body cue:** Pose Estimation Decoders We use MSE loss for this task. • SITR: We pass 2 tactile images x1 and x2 into the network separately.
- **p. 14 / A.1.2 ARCHITECTURE - extractive body cue:** SITR Training Decoders: During the pre-training phase for SITR, we use two decoders: • Normal Map Reconstruction Decoder: We apply a simple linear projection to ...
- **p. 15 / A.1.2 ARCHITECTURE - extractive body cue:** We also find that unfreezing the ViT pre-trained weights during training improves performance. • T3: We unpatchify the output tokens to a feature map and ...
- **p. 24 / A.6.1 CONTRIBUTION OF LOSS TERMS - extractive body cue:** This evaluation is conducted on the dataset visualized in Figure 6, further highlighting how these two loss terms synergize to improve representation learning.
- **p. 24 / A.6.1 CONTRIBUTION OF LOSS TERMS - extractive body cue:** As shown in Table 5, either loss term independently serves as an effective supervision signal.
- **Detected method headings:** A.1.2 ARCHITECTURE (p. 14)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multi-modal contact encoding | vision과 touch를 contact feature로 결합한다 | tactile image/force, vision, proprioception | tactile encoder, calibration, fusion 또는 temporal feature extraction을 수행 | contact feature/state | Classification Decoders We use Cross Entropy Loss for this task. • SITR: We unpatchify the output tokens xi to a feature map ... | p. 14 (A.1.2 ARCHITECTURE), p. 15 (A.1.2 ARCHITECTURE) |
| Contact / dynamics inference | contact mode와 object response를 추정한다 | contact feature와 action history | mode classifier, force/dynamics model 또는 state estimator를 update | contact/force prediction | Pose Estimation Decoders We use MSE loss for this task. • SITR: We pass 2 tactile images x1 and x2 into the ... | p. 15 (A.1.2 ARCHITECTURE), p. 14 (A.1.2 ARCHITECTURE) |
| Force-aware action correction | interaction feedback으로 command를 보정한다 | predicted contact와 current wrench/touch | policy/control law가 action, force 또는 grasp를 재계산 | contact-safe action/torque | SITR Training Decoders: During the pre-training phase for SITR, we use two decoders: • Normal Map Reconstruction Decoder: We apply a simple ... | p. 14 (A.1.2 ARCHITECTURE), p. 15 (A.1.2 ARCHITECTURE) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 14 / A.1.2 ARCHITECTURE - extractive body cue:** Classification Decoders We use Cross Entropy Loss for this task. • SITR: We unpatchify the output tokens xi to a feature map and pass it ...
- **p. 24 / A.6.1 CONTRIBUTION OF LOSS TERMS - extractive body cue:** As shown in Table 5, either loss term independently serves as an effective supervision signal.
- **p. 24 / A.6.1 CONTRIBUTION OF LOSS TERMS - extractive body cue:** We conduct an ablation study to evaluate the contributions of the normal map loss and SCL loss to SITR's performance.
- **p. 14 / A.1.2 ARCHITECTURE - extractive body cue:** We supervise with MSE loss λnormal against the ground truth normal map. • Class Token Decoder: The class token is passed through a linear projection ...
- **p. 15 / A.1.2 ARCHITECTURE - extractive body cue:** Pose Estimation Decoders We use MSE loss for this task. • SITR: We pass 2 tactile images x1 and x2 into the network separately.
- **Formal bridge:** visual/tactile/proprioceptive contact history -> contact-aware action/force -> contact prediction/control error -> slip/contact success and safe interaction.
- **Equation/algorithm anchors:** p. 14 (A.1.2 ARCHITECTURE), p. 14 (A.1.2 ARCHITECTURE), p. 15 (A.1.2 ARCHITECTURE), p. 24 (A.6.1 CONTRIBUTION OF LOSS TERMS), p. 24 (A.6.1 CONTRIBUTION OF LOSS TERMS).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | subtract, sensor, background, input, images, pixel-wise, color, change, described, Section, NETWORK, ARCHITECTURE, tactile, image | tactile image/force, vision과 proprioceptive history | body cue; exact tensor/frame verify |
| State/latent | subtract, sensor, background, input, images, pixel-wise, color, change, described, Section | contact geometry, force state 또는 latent dynamics | body cue; notation verify |
| Action/output | section, introduce, framework, training, Sensor-Invariant, Tactile, Representation, SITR, novel, generating | grasp/contact action, force command 또는 object motion | body cue; unit/decoder verify |
| Objective/constraint | Classification, Decoders, Cross, Entropy, Loss, task, SITR, unpatchify, output, tokens | contact prediction/control error | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 1 INTRODUCTION - extractive body cue:** We subtract the sensor background from all the input images to get the pixel-wise color change as described in Section 3.1.
- **p. 4 / 1 INTRODUCTION - extractive body cue:** 3.2 NETWORK ARCHITECTURE Input: We use the tactile image and a set of calibration images for the sensor as inputs for the network.
- **p. 14 / A.1.2 ARCHITECTURE - extractive body cue:** We reshape and unpatchify the output to create a feature image map.
- **p. 14 / A.1.2 ARCHITECTURE - extractive body cue:** SITR Training Decoders: During the pre-training phase for SITR, we use two decoders: • Normal Map Reconstruction Decoder: We apply a simple linear projection to ...
- **p. 6 / 1 INTRODUCTION - extractive body cue:** For the classification task, we select 16 objects and press them against the sensor in various poses and depths, recording 1K tactile images for each ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Differences in the optical design or manufacturing process can result in significant discrepancies in sensor output.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We highlight in grey the concatenation of the output class token and patch tokens as our Sensor-Invariant Tactile Representation (SITR) for downstream tasks.
- **Normalized interface:** observation=tactile image/force, vision과 proprioceptive history; state=contact geometry, force state 또는 latent dynamics; output/action=grasp/contact action, force command 또는 object motion.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | contact episode 또는 action chunk horizon; contact event timing이 핵심이다. | This section outlines the detailed implementation steps, including pre-processing, architecture, training settings, and decoder choices for all models. | episode/sequence/action-chunk boundary |
| Rate / latency | tactile sampling/control loop가 visual policy rate와 다를 수 있다; numeric values 확인 필요. | Our framework incorporates three core innovations: 1. | Hz/fps, inference time and control rate |
| Memory | recent tactile/force history와 visual state; recurrent memory 여부 확인 필요. | not recovered | window and reset |
| Compute | sensor fusion, contact inference와 high-frequency correction이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 14 / A.1.2 ARCHITECTURE - extractive body cue:** SITR Training Decoders: During the pre-training phase for SITR, we use two decoders: • Normal Map Reconstruction Decoder: We apply a simple linear projection to ...
- **p. 15 / A.1.2 ARCHITECTURE - extractive body cue:** We also find that unfreezing the ViT pre-trained weights during training improves performance. • T3: We unpatchify the output tokens to a feature map and ...
- **p. 14 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** This section outlines the detailed implementation steps, including pre-processing, architecture, training settings, and decoder choices for all models.
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** For each downstream task, we freeze the SITR encoder and only train the downstream task-specific decoder on a single sensor.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** We freeze our SITR encoder and train the downstream classifier using crossentropy loss.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** We separately feed 2 tactile images of the same object into the frozen SITR encoder, concatenate their features, and train a decoder to learn the ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Classification, Decoders, Cross, Entropy, Loss, task, SITR, unpatchify, output, tokens, feature, pass, through, ResNet-18, network, Pose, Estimation, MSE, tactile, images.
- **Relevant PDF headings:** A.1.2 ARCHITECTURE (p. 14).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multi-modal contact encoding | 5.3 OBJECT CLASSIFICATION We compare SITR with baselines using our real-world classification dataset from Section 4.2 and report top-1 accuracy. | p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Contact / dynamics inference | As shown in Table 1, SITR outperforms all baselines by a large margin regarding classification accuracy when transferred across sensors. | p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Force-aware action correction | Table 1: Results of object classification accuracy on 16 classes for model transfer and no-transfer performance. We report the mean and standard ... | p. 8 (Figure/Table caption), p. 10 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 9 / 5 EXPERIMENTS - extractive body cue:** 6.2 CONTRASTIVE LOSS AND TEMPERATURE We conduct an ablation study to assess the effect of SCL and varying contrastive temperatures τ on SITR's performance.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** 6 ABLATIONS 6.1 NUMBER AND TYPE OF CALIBRATION IMAGES Figure 7: Ablation study on the number and type of calibration images used in SITR, showing ...
- **p. 24 / Figure/Table caption - extractive body cue:** Table 5: Ablation study showing the impact of different loss terms on classification accuracy trans- ferability. A.6.2 CHOICE OF SUPERVISION SIGNAL There are alternative supervisions ...
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** Though, these reconstructions are naturally constrained by the resolution and sensitivity limitations of the sensors.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** Baseline: We compare our SITR with ViTs that are either trained from scratch or fine-tuned from ImageNet weights to show the effectiveness of our method.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** This indicates that SITR successfully aligns the tactile signals from different sensors, highlighting its capacity to eliminate sensor-variant features.
- **p. 24 / Figure/Table caption - extractive body cue:** Table 6: Comparison of MAE, VQGAN, and SITR performance on intra-sensor and inter-sensor classification tasks (%) and inter-sensor pose estimation (mm) A.6.3 EFFECT OF SIMULATION ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 14 (A.1.2 ARCHITECTURE), p. 15 (A.1.2 ARCHITECTURE), p. 14 (A.1.2 ARCHITECTURE), p. 15 (A.1.2 ARCHITECTURE), p. 24 (A.6.1 CONTRIBUTION OF LOSS TERMS), p. 24 (A.6.1 CONTRIBUTION OF LOSS TERMS), objective p. 14 (A.1.2 ARCHITECTURE), p. 24 (A.6.1 CONTRIBUTION OF LOSS TERMS), p. 24 (A.6.1 CONTRIBUTION OF LOSS TERMS), p. 14 (A.1.2 ARCHITECTURE), p. 15 (A.1.2 ARCHITECTURE), temporal p. 14 (A.1 IMPLEMENTATION DETAILS), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (1 INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
