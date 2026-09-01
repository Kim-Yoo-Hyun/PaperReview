# Method - DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/LRA.2020.2977257; PDF retrieval source: https://doi.org/10.1109/LRA.2020.2977257. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (I. INTRODUCTION), p. 1 (Abstract), p. 1 (I. INTRODUCTION)): To scale up tactile-MPC, we propose new approaches for dynamics model learning and task specification that dramatically reduce the computational cost.

## Method Body Digest

- **p. 2 / I. INTRODUCTION - extractive body cue:** To scale up tactile-MPC, we propose new approaches for dynamics model learning and task specification that dramatically reduce the computational cost.
- **p. 1 / Abstract - extractive body cue:** We demonstrate the capabilities of the DIGIT sensor by training deep neural network model-based controllers to manipulate glass marbles in-hand with a multi-finger robotic hand.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Forces are an important representation to understand and plan interactions with the environment - grasping a small screw, inserting a key, and manipulating a glass ...
- **p. 1 / Abstract - extractive body cue:** To provide the robotic community access to reliable and low-cost tactile sensors, we open-source the DIGIT design at www.digit.ml.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our new sensor, "DIGIT", introduces several critical improvements over past visionbased tactile sensors: a smaller form factor to enable inhand manipulation on multi-finger hands, a ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Second, we demonstrate the sensor by learning to manipulate small objects with a multi-finger hand from raw tactile inputs.
- **p. 1 / Abstract - extractive body cue:** One of the contributing factors that limit current robotic manipulation systems is the difficulty of precisely sensing contact forces - sensing and reasoning about contact ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** For this reason, in conjunction with this paper, we release the design of the sensor at www.digit.ml.

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** To better fulfill these requirements, in this paper, we present the design of a novel tactile sensor.
- **p. 1 / I. INTRODUCTION - extractive body cue:** First, we present the design and manufacturing process of DIGIT, and analyze the properties of the resulting sensor.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To scale up tactile-MPC, we propose new approaches for dynamics model learning and task specification that dramatically reduce the computational cost.

## Source Evidence Cues

- **p. 2 / I. INTRODUCTION - extractive body cue:** To scale up tactile-MPC, we propose new approaches for dynamics model learning and task specification that dramatically reduce the computational cost.
- **p. 1 / Abstract - extractive body cue:** We demonstrate the capabilities of the DIGIT sensor by training deep neural network model-based controllers to manipulate glass marbles in-hand with a multi-finger robotic hand.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Forces are an important representation to understand and plan interactions with the environment - grasping a small screw, inserting a key, and manipulating a glass ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multi-modal contact encoding | vision과 touch를 contact feature로 결합한다 | tactile image/force, vision, proprioception | tactile encoder, calibration, fusion 또는 temporal feature extraction을 수행 | contact feature/state | To scale up tactile-MPC, we propose new approaches for dynamics model learning and task specification that dramatically reduce the computational cost. | p. 2 (I. INTRODUCTION), p. 1 (Abstract) |
| Contact / dynamics inference | contact mode와 object response를 추정한다 | contact feature와 action history | mode classifier, force/dynamics model 또는 state estimator를 update | contact/force prediction | We demonstrate the capabilities of the DIGIT sensor by training deep neural network model-based controllers to manipulate glass marbles in-hand with a ... | p. 1 (Abstract), p. 1 (I. INTRODUCTION) |
| Force-aware action correction | interaction feedback으로 command를 보정한다 | predicted contact와 current wrench/touch | policy/control law가 action, force 또는 grasp를 재계산 | contact-safe action/torque | Forces are an important representation to understand and plan interactions with the environment - grasping a small screw, inserting a key, and ... | p. 1 (I. INTRODUCTION) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / Abstract - extractive body cue:** To provide the robotic community access to reliable and low-cost tactile sensors, we open-source the DIGIT design at www.digit.ml.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our new sensor, "DIGIT", introduces several critical improvements over past visionbased tactile sensors: a smaller form factor to enable inhand manipulation on multi-finger hands, a ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To scale up tactile-MPC, we propose new approaches for dynamics model learning and task specification that dramatically reduce the computational cost.
- **Formal bridge:** visual/tactile/proprioceptive contact history -> contact-aware action/force -> contact prediction/control error -> slip/contact success and safe interaction.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Second, demonstrate, sensor, learning, manipulate, small, objects, multi-finger, hand, tactile, inputs, One, contributing, factors | tactile image/force, vision과 proprioceptive history | body cue; exact tensor/frame verify |
| State/latent | Second, demonstrate, sensor, learning, manipulate, small, objects, multi-finger, hand, tactile | contact geometry, force state 또는 latent dynamics | body cue; notation verify |
| Action/output | better, fulfill, requirements, present, design, novel, tactile, sensor, First, manufacturing | grasp/contact action, force command 또는 object motion | body cue; unit/decoder verify |
| Objective/constraint | provide, robotic, community, access, reliable, low-cost, tactile, sensors, open-source, DIGIT | contact prediction/control error | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / I. INTRODUCTION - extractive body cue:** Second, we demonstrate the sensor by learning to manipulate small objects with a multi-finger hand from raw tactile inputs.
- **p. 1 / Abstract - extractive body cue:** One of the contributing factors that limit current robotic manipulation systems is the difficulty of precisely sensing contact forces - sensing and reasoning about contact ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** For this reason, in conjunction with this paper, we release the design of the sensor at www.digit.ml.
- **p. 2 / I. INTRODUCTION - extractive body cue:** ACCEPTED JANUARY, 2020 touch sensor, we are interested in handling multiple touch sensors from different fingers.
- **Normalized interface:** observation=tactile image/force, vision과 proprioceptive history; state=contact geometry, force state 또는 latent dynamics; output/action=grasp/contact action, force command 또는 object motion.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | contact episode 또는 action chunk horizon; contact event timing이 핵심이다. | At each time step, an optimizer is used to find the best sequences of actions a∗ t:t+T -1 that moves the marble ... | episode/sequence/action-chunk boundary |
| Rate / latency | tactile sampling/control loop가 visual policy rate와 다를 수 있다; numeric values 확인 필요. | In our multi-finger marble manipulation setup, MPC optimization is difficult and computationally demanding, requiring 250 particles with a planning horizon of 10 ... | Hz/fps, inference time and control rate |
| Memory | recent tactile/force history와 visual state; recurrent memory 여부 확인 필요. | not recovered | window and reset |
| Compute | sensor fusion, contact inference와 high-frequency correction이 latency를 결정한다. | In both datasets, we use 64 × 64 images and compare prediction performance with CDNA [35] used for tactile servoing in [17] ... | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / Abstract - extractive body cue:** We demonstrate the capabilities of the DIGIT sensor by training deep neural network model-based controllers to manipulate glass marbles in-hand with a multi-finger robotic hand.
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** In both datasets, we use 64 × 64 images and compare prediction performance with CDNA [35] used for tactile servoing in [17] in terms of ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** scale, tactile-MPC, approaches, dynamics, model, learning, task, specification, dramatically, reduce, computational, cost, demonstrate, capabilities, DIGIT, sensor, training, deep, neural, network.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multi-modal contact encoding | To validate our modeling choices, we measure the prediction error on a standard benchmark for video prediction, the BAIR robot pushing dataset ... | p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS) |
| Contact / dynamics inference | However, compared to our MPC approach which is virtually parameters-free, this proved significantly more challenging. | p. 7 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS) |
| Force-aware action correction | This result is in agreement with previous results in [17], where learned models outperform simple handtuned controllers. | p. 7 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS) |

## Failure and Ablation Link

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 4: DIGIT supports different types of elastomers which can be rapidly replaced thanks to its mechanical design. Here we show readings when touching an ...
- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** This is a very challenging task because it requires controlling the slipping and rolling dynamics of the marble over the small and deformable DIGIT surfaces ...
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** 3) and the robustness of the gel (Section III-D), we now evaluate the DIGIT in the complex in-hand tactile manipulation task described in Section IV.
- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** (Bottom) Due to control noise, potential planning inaccuracies and the challenging nature of this task, the hand tends to drop marbles over time.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (I. INTRODUCTION), p. 1 (Abstract), p. 1 (I. INTRODUCTION), objective p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), temporal p. 5 (II. RELATED WORK), p. 6 (V. EXPERIMENTAL RESULTS), p. 5 (II. RELATED WORK), p. 6 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
