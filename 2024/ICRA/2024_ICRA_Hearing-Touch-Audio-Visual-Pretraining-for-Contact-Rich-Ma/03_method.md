# Method - Hearing Touch: Audio-Visual Pretraining for Contact-Rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2405.08576; PDF retrieval source: https://arxiv.org/pdf/2405.08576. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 2 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 2 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING)): To isolate the effect of large-scale pre-training for our audio encoder, we use R3M [1], a proven method for pre-training visual features in robotic applications, R3M, with a ResNet18 [38] ...

## Method Body Digest

- **p. 3 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive body cue:** To isolate the effect of large-scale pre-training for our audio encoder, we use R3M [1], a proven method for pre-training visual features in robotic applications, ...
- **p. 3 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive body cue:** We apply learned positional embeddings to each of the encoded representations and pass the result as input to a transformer decoder network similar to [6].
- **p. 2 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive body cue:** Sensors At each timestep, we collect image observations vt and two-second clips of contact audio at.
- **p. 2 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive body cue:** Image observations are obtained from a third-person view camera and audio is obtained by averaging the signal captured from four contact microphones mounted on the ...
- **p. 3 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive body cue:** We optimize the network to minimize the standard MSE loss ℓ= 1 H PH j=0(at+j-π(vt-i, . . . , vt, st)j)2.
- **p. 3 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive body cue:** Following [40], we keep both encoders unfrozen, continuing to update the weights during policy learning.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Initializing our encoder with AVID weights, we train a policy with behavior cloning that fuses visual and audio inputs with self-attention in order to predict ...
- **p. 3 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive body cue:** This approach allows the policy to remain responsive to subtle changes in the audio input while encouraging temporal action consistency and mitigating the effect of ...

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our method makes use of Audio-Visual Instance Discrimination (AVID) [14], a selfsupervised learning approach to learn audio-visual representations, pre-trained on Audioset [15], a dataset containing ...
- **p. 3 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive body cue:** Similar to [41], [42] our method is quasi open-loop-at time step t the policy predicts H steps of actions, of which h ≤H steps of ...
- **p. 3 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive body cue:** Audio and Visual Representation Pretraining Our method uses large-scale audio-visual pre-training to initialize our audio encoder and large-scale visual pretraining to initialize our visual encoder.

## Source Evidence Cues

- **p. 3 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive body cue:** To isolate the effect of large-scale pre-training for our audio encoder, we use R3M [1], a proven method for pre-training visual features in robotic applications, ...
- **p. 3 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive body cue:** We apply learned positional embeddings to each of the encoded representations and pass the result as input to a transformer decoder network similar to [6].
- **p. 2 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive body cue:** Sensors At each timestep, we collect image observations vt and two-second clips of contact audio at.
- **p. 2 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive body cue:** Image observations are obtained from a third-person view camera and audio is obtained by averaging the signal captured from four contact microphones mounted on the ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multi-modal contact encoding | vision과 touch를 contact feature로 결합한다 | tactile image/force, vision, proprioception | tactile encoder, calibration, fusion 또는 temporal feature extraction을 수행 | contact feature/state | To isolate the effect of large-scale pre-training for our audio encoder, we use R3M [1], a proven method for pre-training visual features ... | p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING) |
| Contact / dynamics inference | contact mode와 object response를 추정한다 | contact feature와 action history | mode classifier, force/dynamics model 또는 state estimator를 update | contact/force prediction | We apply learned positional embeddings to each of the encoded representations and pass the result as input to a transformer decoder network ... | p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 2 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING) |
| Force-aware action correction | interaction feedback으로 command를 보정한다 | predicted contact와 current wrench/touch | policy/control law가 action, force 또는 grasp를 재계산 | contact-safe action/torque | Sensors At each timestep, we collect image observations vt and two-second clips of contact audio at. | p. 2 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 2 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive body cue:** We optimize the network to minimize the standard MSE loss ℓ= 1 H PH j=0(at+j-π(vt-i, . . . , vt, st)j)2.
- **p. 3 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive body cue:** Following [40], we keep both encoders unfrozen, continuing to update the weights during policy learning.
- **Formal bridge:** visual/tactile/proprioceptive contact history -> contact-aware action/force -> contact prediction/control error -> slip/contact success and safe interaction.
- **Equation/algorithm anchors:** p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Initializing, encoder, AVID, weights, train, policy, behavior, cloning, fuses, visual, audio, inputs, self-attention, order | tactile image/force, vision과 proprioceptive history | body cue; exact tensor/frame verify |
| State/latent | Initializing, encoder, AVID, weights, train, policy, behavior, cloning, fuses, visual | contact geometry, force state 또는 latent dynamics | body cue; notation verify |
| Action/output | makes, Audio-Visual, Instance, Discrimination, AVID, selfsupervised, learning, learn, representations, pre-trained | grasp/contact action, force command 또는 object motion | body cue; unit/decoder verify |
| Objective/constraint | optimize, network, minimize, standard, MSE, loss, vt-i, Following, keep, encoders | contact prediction/control error | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / I. INTRODUCTION - extractive body cue:** Initializing our encoder with AVID weights, we train a policy with behavior cloning that fuses visual and audio inputs with self-attention in order to predict ...
- **p. 3 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive body cue:** This approach allows the policy to remain responsive to subtle changes in the audio input while encouraging temporal action consistency and mitigating the effect of ...
- **p. 3 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive body cue:** In particular, the final component of our network is a multi-layer perceptron that outputs actions at, . . . , at+h over a short horizon ...
- **p. 2 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive body cue:** Sensors At each timestep, we collect image observations vt and two-second clips of contact audio at.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Two key components consistently improve the performance of robotic manipulation: (1) pre-training on a large amount of data [1]-[5] and (2) using multisensory input, especially ...
- **p. 2 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive body cue:** Image observations are obtained from a third-person view camera and audio is obtained by averaging the signal captured from four contact microphones mounted on the ...
- **Normalized interface:** observation=tactile image/force, vision과 proprioceptive history; state=contact geometry, force state 또는 latent dynamics; output/action=grasp/contact action, force command 또는 object motion.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | contact episode 또는 action chunk horizon; contact event timing이 핵심이다. | In particular, the final component of our network is a multi-layer perceptron that outputs actions at, . . . , at+h over ... | episode/sequence/action-chunk boundary |
| Rate / latency | tactile sampling/control loop가 visual policy rate와 다를 수 있다; numeric values 확인 필요. | At each timestep, the policy takes in a two-second audio clip st and a sequence of i images vt-i, . . . ... | Hz/fps, inference time and control rate |
| Memory | recent tactile/force history와 visual state; recurrent memory 여부 확인 필요. | not recovered | window and reset |
| Compute | sensor fusion, contact inference와 high-frequency correction이 latency를 결정한다. | We use contact microphones as an alternative tactile sensor, which are relatively inexpensive in comparison to common tactile sensors and can record ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive body cue:** To isolate the effect of large-scale pre-training for our audio encoder, we use R3M [1], a proven method for pre-training visual features in robotic applications, ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** 2) Scaling Performance: We run evaluations on the scooping task for models trained with dataset sizes 50% (30 demos) and 150% (90 demos) of the ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** The results show that keeping the pre-trained audio encoder weights frozen during policy learning only slightly diminishes the performance of our method and still outperforms ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** isolate, effect, large-scale, pre-training, audio, encoder, R3M, proven, visual, features, robotic, applications, ResNet18, pre-trained, Ego4D, human, video, dataset, time, contrastive.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multi-modal contact encoding | 2) Scaling Performance: We run evaluations on the scooping task for models trained with dataset sizes 50% (30 demos) and 150% (90 ... | p. 5 (IV. EXPERIMENTS), p. 3 (IV. EXPERIMENTS) |
| Contact / dynamics inference | Our method, shown in blue, outperforms baselines in all but one setup of the zipping task. | p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |
| Force-aware action correction | Flipping Scooping Zipping Success % Reward Success % Reward Success % Ours 50.0% 15.4 78.1% 8.9 88.9% BYOL-A 25.0% 2.3 25.0% 3.8 ... | p. 4 (IV. EXPERIMENTS), p. 4 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 6: Ablations. We evaluate the zero-shot transfer of frozen pre-trained audio representations (a), the effect of dataset size (b), the generalization ability of our ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** We use different methods of pretraining in order to measure the effect of large-scale audio-visual pretraining on learning a useful contact audio representation for manipulation.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** 4) Architecture Ablation: We replace the transformer with an MLP including an added additional linear layer to ensure the resultant network has approximately the same ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** This baseline compares the effect of large-scale audio-visual pre-training to in-domain audio pre-training, with an emphasis on the amount of pre-training data.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Ablation Studies 1) Zero-Shot Transfer: To get a better sense of how relevant pre-trained AVID weights are to downstream manipulation tasks, we train a version ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** (a) Zero-Shot Transfer (b) Scaling Performance (c) Generalization (d) Architecture Ablation Fig.
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: Two-stage model training. AVID and R3M pretraining leverages the large scale of internet video data (blue dashed box). We initialize the vision and ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 2 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 2 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), objective p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), temporal p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 1 (I. INTRODUCTION), p. 2 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 2 (II. RELATED WORK), p. 4 (IV. EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
