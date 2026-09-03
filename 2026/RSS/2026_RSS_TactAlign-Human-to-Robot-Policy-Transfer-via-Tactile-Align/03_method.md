# Method - TactAlign: Human-to-Robot Policy Transfer via Tactile Alignment

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://roboticsconference.org/program/papers/6/; PDF retrieval source: https://roboticsconference.org/program/papers/6/. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 2 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY)): We use a learnable length-1 query between the encoder and decoder to produce a fixed-dimensional latent representation via cross-attention pooling.

## Method Body Digest

- **p. 3 / III. METHODOLOGY - extractive body cue:** We use a learnable length-1 query between the encoder and decoder to produce a fixed-dimensional latent representation via cross-attention pooling.
- **p. 3 / III. METHODOLOGY - extractive body cue:** A learnable length 1 query is implemented between the encoder and decoder to output a fixeddimensional latent representations after the cross-attention module.
- **p. 2 / III. METHODOLOGY - extractive body cue:** Problem Statement Our goal is to learn a latent-space mapping that transfers human tactile observations to robot tactile observations.
- **p. 4 / III. METHODOLOGY - extractive body cue:** First: Standard rectified flow [23] learns a low-cost transport between two distributions by training on random pairs.
- **p. 4 / III. METHODOLOGY - extractive body cue:** Both outputs ah t , ar t consist of action chunks specifying desired fingertip locations and wrist orientation with respect to the robot base frame.
- **p. 3 / III. METHODOLOGY - extractive body cue:** In step2, we aggregate the learned latents from both domains to construct pseudo-pairs (h∗, r∗), and learn a velocity field vθ that transports the glove ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** To accommodate the heterogeneous sensing modalities, we learn unique encoders and decoders for the human and robot tactile signals in a self-supervised manner, using a ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** (3) This process naturally performs latent "rewiring", effectively handling crossings and transport cost reductions while learned from noisy pairs as in Fig.

## Design Rationale

- **p. 3 / III. METHODOLOGY - extractive body cue:** Our method consists of two stages: self-supervised representation learning and cross-embodiment alignment via pseudo-pairs.
- **p. 2 / I. INTRODUCTION - extractive body cue:** The core contributions of our work are: • We propose TactAlign, a method for aligning crosssensor tactile data from unpaired demonstrations of the same task.
- **p. 2 / I. INTRODUCTION - extractive body cue:** TactAlign leverages rectified flow with noisy pseudo-pairs to learn a latent mapping that enables H2R policy transfer between humans and robots equipped with heterogeneous tactile ...

## Source Evidence Cues

- **p. 3 / III. METHODOLOGY - extractive body cue:** We use a learnable length-1 query between the encoder and decoder to produce a fixed-dimensional latent representation via cross-attention pooling.
- **p. 3 / III. METHODOLOGY - extractive body cue:** A learnable length 1 query is implemented between the encoder and decoder to output a fixeddimensional latent representations after the cross-attention module.
- **p. 2 / III. METHODOLOGY - extractive body cue:** Problem Statement Our goal is to learn a latent-space mapping that transfers human tactile observations to robot tactile observations.
- **p. 4 / III. METHODOLOGY - extractive body cue:** First: Standard rectified flow [23] learns a low-cost transport between two distributions by training on random pairs.
- **p. 4 / III. METHODOLOGY - extractive body cue:** Both outputs ah t , ar t consist of action chunks specifying desired fingertip locations and wrist orientation with respect to the robot base frame.
- **Detected method headings:** III. METHODOLOGY (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multi-modal contact encoding | vision과 touch를 contact feature로 결합한다 | tactile image/force, vision, proprioception | tactile encoder, calibration, fusion 또는 temporal feature extraction을 수행 | contact feature/state | We use a learnable length-1 query between the encoder and decoder to produce a fixed-dimensional latent representation via cross-attention pooling. | p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |
| Contact / dynamics inference | contact mode와 object response를 추정한다 | contact feature와 action history | mode classifier, force/dynamics model 또는 state estimator를 update | contact/force prediction | A learnable length 1 query is implemented between the encoder and decoder to output a fixeddimensional latent representations after the cross-attention module. | p. 3 (III. METHODOLOGY), p. 2 (III. METHODOLOGY) |
| Force-aware action correction | interaction feedback으로 command를 보정한다 | predicted contact와 current wrench/touch | policy/control law가 action, force 또는 grasp를 재계산 | contact-safe action/torque | Problem Statement Our goal is to learn a latent-space mapping that transfers human tactile observations to robot tactile observations. | p. 2 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / III. METHODOLOGY - extractive body cue:** In step2, we aggregate the learned latents from both domains to construct pseudo-pairs (h∗, r∗), and learn a velocity field vθ that transports the glove ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** To accommodate the heterogeneous sensing modalities, we learn unique encoders and decoders for the human and robot tactile signals in a self-supervised manner, using a ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** First: Standard rectified flow [23] learns a low-cost transport between two distributions by training on random pairs.
- **p. 4 / III. METHODOLOGY - extractive body cue:** (3) This process naturally performs latent "rewiring", effectively handling crossings and transport cost reductions while learned from noisy pairs as in Fig.
- **Formal bridge:** visual/tactile/proprioceptive contact history -> contact-aware action/force -> contact prediction/control error -> slip/contact success and safe interaction.
- **Equation/algorithm anchors:** p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | However, most, existing, human-to-robot, H2R, approaches, omit, tactile, feedback, entirely, instead, focus, transferring, more | tactile image/force, vision과 proprioceptive history | body cue; exact tensor/frame verify |
| State/latent | However, most, existing, human-to-robot, H2R, approaches, omit, tactile, feedback, entirely | contact geometry, force state 또는 latent dynamics | body cue; notation verify |
| Action/output | consists, stages, self-supervised, representation, learning, cross-embodiment, alignment, pseudo-pairs, core, contributions | grasp/contact action, force command 또는 object motion | body cue; unit/decoder verify |
| Objective/constraint | step2, aggregate, learned, latents, domains, construct, pseudo-pairs, learn, velocity, field | contact prediction/control error | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / I. INTRODUCTION - extractive body cue:** However, most existing human-to-robot (H2R) approaches omit tactile feedback entirely and instead focus on transferring more readily available observations such as egocentric vision or state-action ...
- **p. 2 / III. METHODOLOGY - extractive body cue:** Problem Statement Our goal is to learn a latent-space mapping that transfers human tactile observations to robot tactile observations.
- **p. 2 / I. INTRODUCTION - extractive body cue:** TactAlign leverages rectified flow with noisy pseudo-pairs to learn a latent mapping that enables H2R policy transfer between humans and robots equipped with heterogeneous tactile ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** Both outputs ah t , ar t consist of action chunks specifying desired fingertip locations and wrist orientation with respect to the robot base frame.
- **p. 3 / III. METHODOLOGY - extractive body cue:** We construct the pseudo pairs from Ah and Ar between human-robot demonstrations from the same task, object, reset state and goal state.
- **p. 3 / III. METHODOLOGY - extractive body cue:** We use f g i , pg i and f r j , pr j to denote the tactile observation and pose of a single ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** We retain only pseudo pairs that map contact-to-contact and non-contact-tonon-contact states.
- **Normalized interface:** observation=tactile image/force, vision과 proprioceptive history; state=contact geometry, force state 또는 latent dynamics; output/action=grasp/contact action, force command 또는 object motion.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | contact episode 또는 action chunk horizon; contact event timing이 핵심이다. | At each time step t, tactile observations and poses from all K fingertips are represented as Ft = (ft,1, . . . ... | episode/sequence/action-chunk boundary |
| Rate / latency | tactile sampling/control loop가 visual policy rate와 다를 수 있다; numeric values 확인 필요. | Each human trajectory is represented as T h = {(F h 1 , P h 1 , wh 1), . . . ... | Hz/fps, inference time and control rate |
| Memory | recent tactile/force history와 visual state; recurrent memory 여부 확인 필요. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | sensor fusion, contact inference와 high-frequency correction이 latency를 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / III. METHODOLOGY - extractive body cue:** First: Standard rectified flow [23] learns a low-cost transport between two distributions by training on random pairs.
- **p. 5 / IV. EXPERIMENTS AND RESULTS - extractive body cue:** 1) Tactile self-supervised learning: Both human and robot tactile encoders are trained using a combination of play data (≈10 minutes) and an in-domain tactile alignment ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** 2 left) is based on JEPA [2] with the decoder adapted from the online probe module in [13, 34].

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** learnable, length-1, query, between, encoder, decoder, produce, fixed-dimensional, latent, representation, cross-attention, pooling, length, implemented, output, fixeddimensional, representations, after, module, Problem.
- **Relevant PDF headings:** III. METHODOLOGY (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multi-modal contact encoding | The dataset includes 1,472 robot force samples (24:1 train:test split) and 1,527 human force samples used only for evaluation. | p. 5 (IV. EXPERIMENTS AND RESULTS), p. 5 (IV. EXPERIMENTS AND RESULTS) |
| Contact / dynamics inference | Fig. 10: ℓ1 force prediction error (mean ± std) along each axis, averaged over five evaluations. G →R evaluates force prediction on ... | p. 8 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Force-aware action correction | Fig. 8: Lid Closing Task. With randomized grasps, the policy uses touch to perform search, alignment, and closing between the lid and ... | p. 7 (Figure/Table caption), p. 5 (IV. EXPERIMENTS AND RESULTS) |

## Failure and Ablation Link

- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 6: Pivoting Task. The task begins in a non-contact state and transitions to pivoting upon contact detection via tactile feedback, with the goal of ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 10: ℓ1 force prediction error (mean ± std) along each axis, averaged over five evaluations. G →R evaluates force prediction on the robot using ...
- **p. 8 / V. LIMITATION - extractive body cue:** Moreover, tactile alignment alone does not address visual discrepancies between human and robot embodiments.
- **p. 8 / V. LIMITATION - extractive body cue:** Incorporating vision and other modalities into a unified multi-modal policy is also an important direction for future work.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Red and blue indicate two subsets of the source distribution. The left side of each of the three panels shows the provided training ...
- **p. 5 / IV. EXPERIMENTS AND RESULTS - extractive body cue:** We use Manus glove [25] with OSMO tactile sensors [45] for robust hand pose estimation under visual occlusions from the lamp shade and light bulb.
- **p. 5 / IV. EXPERIMENTS AND RESULTS - extractive body cue:** We record fingertip poses only, as the Manus glove does not provide wrist pose information.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 2 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), objective p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), temporal p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 5 (IV. EXPERIMENTS AND RESULTS), p. 1 (I. INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** A learnable length 1 query is implemented between the encoder and decoder to output a fixeddimensional latent representations after the cross-attention module. (p. 3, III. METHODOLOGY).
- **Objective/update evidence:** In step2, we aggregate the learned latents from both domains to construct pseudo-pairs (h∗, r∗), and learn a velocity field vθ that transports the glove latent distribution to the robot ... (p. 3, III. METHODOLOGY).
- **Temporal/runtime evidence:** At each time step t, tactile observations and poses from all K fingertips are represented as Ft = (ft,1, . . . , ft,K), Pt = (pt,1, . . . ... (p. 3, III. METHODOLOGY).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
