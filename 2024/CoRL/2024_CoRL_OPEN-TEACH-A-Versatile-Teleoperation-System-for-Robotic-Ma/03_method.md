# Method - OPEN TEACH: A Versatile Teleoperation System for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v270/iyer25a.html; PDF retrieval source: https://arxiv.org/pdf/2403.07870. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (III. BACKGROUND ON IMITATION LEARNING), p. 3 (III. BACKGROUND ON IMITATION LEARNING), p. 5 (IV. OPEN TEACH), p. 5 (IV. OPEN TEACH), p. 2 (Abstract), p. 6 (4) How intuitive is the system for new users?)): For both of these methods, the first phase involves obtaining a non-parametric base-policy πb : Z →A with encoded representations z ∈Z and actions a ∈A.

## Method Body Digest

- **p. 3 / III. BACKGROUND ON IMITATION LEARNING - extractive body cue:** For both of these methods, the first phase involves obtaining a non-parametric base-policy πb : Z →A with encoded representations z ∈Z and actions a ...
- **p. 3 / III. BACKGROUND ON IMITATION LEARNING - extractive body cue:** Behavior Cloning Given a dataset of expert rollouts for a desired task in the form of observation and action pairs D == {(o, a)} ⊂O ...
- **p. 5 / IV. OPEN TEACH - extractive body cue:** We use different controllers for each.
- **p. 5 / IV. OPEN TEACH - extractive body cue:** For the Franka Emika Panda, we use the Deoxys controller [69].
- **p. 2 / Abstract - extractive body cue:** Further experiments exhibit that the collected data is compatible with policy learning on 10 dexterous and contactrich manipulation tasks.
- **p. 6 / 4) How intuitive is the system for new users? - extractive body cue:** The policies are trained using transformer-based BC with a GMM head [50] and action chunking [67].
- **p. 6 / 4) How intuitive is the system for new users? - extractive body cue:** The policies are trained using TAVI [20], a demonstration-guided residual RL algorithm that collects a few expert demonstrations and learns a robot policy using both ...
- **p. 3 / III. BACKGROUND ON IMITATION LEARNING - extractive body cue:** Following this convention, the objective of BC is to find the value θ that maximizes the probability of the observed data. θ∗= argmax θ Y ...

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** The contributions of this work is summarized as follows: 1) We present OPEN TEACH, an open-source system for plug-and-play teleoperation framework suitable for collecting demonstrations ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In this work, we present OPEN TEACH, an open-source framework for robot teleoperation that supports a variety of robots, including bimanual and multi-finger manipulation, all ...
- **p. 4 / IV. OPEN TEACH - extractive body cue:** In this section, we provide details about the VR-based teleoperation setup and the system design that enables data collection using this framework.

## Source Evidence Cues

- **p. 3 / III. BACKGROUND ON IMITATION LEARNING - extractive body cue:** For both of these methods, the first phase involves obtaining a non-parametric base-policy πb : Z →A with encoded representations z ∈Z and actions a ...
- **p. 3 / III. BACKGROUND ON IMITATION LEARNING - extractive body cue:** Behavior Cloning Given a dataset of expert rollouts for a desired task in the form of observation and action pairs D == {(o, a)} ⊂O ...
- **p. 5 / IV. OPEN TEACH - extractive body cue:** We use different controllers for each.
- **p. 5 / IV. OPEN TEACH - extractive body cue:** For the Franka Emika Panda, we use the Deoxys controller [69].
- **p. 2 / Abstract - extractive body cue:** Further experiments exhibit that the collected data is compatible with policy learning on 10 dexterous and contactrich manipulation tasks.
- **p. 6 / 4) How intuitive is the system for new users? - extractive body cue:** The policies are trained using transformer-based BC with a GMM head [50] and action chunking [67].
- **p. 6 / 4) How intuitive is the system for new users? - extractive body cue:** The policies are trained using TAVI [20], a demonstration-guided residual RL algorithm that collects a few expert demonstrations and learns a robot policy using both ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Data schema / normalization | heterogeneous robot trajectory를 공통 sample로 만든다 | observation, action, task와 embodiment metadata | sensor/action schema alignment, filtering, normalization을 수행 | shared dataset representation | For both of these methods, the first phase involves obtaining a non-parametric base-policy πb : Z →A with encoded representations z ∈Z ... | p. 3 (III. BACKGROUND ON IMITATION LEARNING), p. 3 (III. BACKGROUND ON IMITATION LEARNING) |
| Coverage / augmentation | task·embodiment·failure variation을 확장한다 | dataset과 metadata | retargeting, relabeling, synthetic/teleoperation augmentation 또는 sampling을 적용 | expanded data support | Behavior Cloning Given a dataset of expert rollouts for a desired task in the form of observation and action pairs D == ... | p. 3 (III. BACKGROUND ON IMITATION LEARNING), p. 5 (IV. OPEN TEACH) |
| Downstream learning interface | 정규화된 data를 policy/representation이 사용한다 | shared observations/actions | pretraining, BC, action-token 또는 representation learning을 수행 | checkpoint/policy action | We use different controllers for each. | p. 5 (IV. OPEN TEACH), p. 5 (IV. OPEN TEACH) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / III. BACKGROUND ON IMITATION LEARNING - extractive body cue:** Following this convention, the objective of BC is to find the value θ that maximizes the probability of the observed data. θ∗= argmax θ Y ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** The aforementioned devices are cost-effective and easy to set up.
- **p. 2 / Abstract - extractive body cue:** However, existing data collection platforms are often proprietary, costly, or tailored to specific robotic morphologies.
- **p. 3 / III. BACKGROUND ON IMITATION LEARNING - extractive body cue:** The reward for learning the residual policy through inverse RL is obtained through optimal transport based trajectory matching [21, 12].
- **p. 5 / IV. OPEN TEACH - extractive body cue:** This significantly reduces the initial setup cost as compared to prior exoskeleton-based teleoperation frameworks like GELLO [61] and AirExo [14].
- **p. 6 / 4) How intuitive is the system for new users? - extractive body cue:** The primary idea behind OPEN TEACH is that given any robotic setup, a user can purchase an affordable off-the-shelf VR headset (in this case, Quest ...
- **Formal bridge:** trajectory D with task/embodiment metadata -> normalized sample or downstream action -> coverage/data efficiency/transfer objective -> cross-domain transfer and task performance.
- **Equation/algorithm anchors:** p. 3 (III. BACKGROUND ON IMITATION LEARNING), p. 2 (I. INTRODUCTION).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Behavior, Cloning, Given, dataset, expert, rollouts, desired, task, form, observation, action, pairs, aims, learn | multi-view observation, language/task label과 action trajectory | body cue; exact tensor/frame verify |
| State/latent | Behavior, Cloning, Given, dataset, expert, rollouts, desired, task, form, observation | shared representation, embodiment/task identity와 data distribution | body cue; notation verify |
| Action/output | contributions, summarized, follows, present, OPEN, TEACH, open-source, system, plug-and-play, teleoperation | dataset sample 또는 learned policy action | body cue; unit/decoder verify |
| Objective/constraint | Following, convention, objective, find, value, maximizes, probability, observed, data, argmax | coverage/data efficiency/transfer objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. BACKGROUND ON IMITATION LEARNING - extractive body cue:** Behavior Cloning Given a dataset of expert rollouts for a desired task in the form of observation and action pairs D == {(o, a)} ⊂O ...
- **p. 3 / III. BACKGROUND ON IMITATION LEARNING - extractive body cue:** For both of these methods, the first phase involves obtaining a non-parametric base-policy πb : Z →A with encoded representations z ∈Z and actions a ...
- **p. 6 / 4) How intuitive is the system for new users? - extractive body cue:** This underscores the effectiveness of OPEN TEACH in collecting data for policy learning.
- **p. 6 / 4) How intuitive is the system for new users? - extractive body cue:** The policies are trained using transformer-based BC with a GMM head [50] and action chunking [67].
- **p. 8 / 4) How intuitive is the system for new users? - extractive body cue:** This observation highlights two factors: (1) the inherent variation in abilities among individuals, and (2) while our system is intuitive for new users, prolonged training ...
- **p. 4 / III. BACKGROUND ON IMITATION LEARNING - extractive body cue:** Human-to-Robot Retargeting Hardware Network Server Hand Pose Detection Pose Detection Wrist Pose Detection Camera Stream Visual Feedback Oculus Passthrough Fig.
- **p. 5 / IV. OPEN TEACH - extractive body cue:** To mitigate steady-state error, we include a gravity compensation module to compute offset torques.
- **Normalized interface:** observation=multi-view observation, language/task label과 action trajectory; state=shared representation, embodiment/task identity와 data distribution; output/action=dataset sample 또는 learned policy action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | trajectory demonstration horizon; training sample window와 deployment task horizon을 분리한다. | The framework has been designed for simple integration with any robot setup, allowing robot teleoperation with real-time streaming (up to 90Hz) and ... | episode/sequence/action-chunk boundary |
| Rate / latency | data recording/action sampling rate와 policy inference/control rate를 분리한다. | In this work, we introduce OPEN TEACH, an open-source unified framework designed to facilitate low-latency, highfrequency robot teleoperation. | Hz/fps, inference time and control rate |
| Memory | trajectory, embodiment/task metadata와 dataset index. | not recovered | window and reset |
| Compute | data decoding, normalization/augmentation과 downstream training budget이 결정한다. | The framework has been designed for simple integration with any robot setup, allowing robot teleoperation with real-time streaming (up to 90Hz) and ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / III. BACKGROUND ON IMITATION LEARNING - extractive body cue:** Behavior Cloning Given a dataset of expert rollouts for a desired task in the form of observation and action pairs D == {(o, a)} ⊂O ...
- **p. 6 / 4) How intuitive is the system for new users? - extractive body cue:** The policies are trained using transformer-based BC with a GMM head [50] and action chunking [67].
- **p. 6 / 4) How intuitive is the system for new users? - extractive body cue:** The policies are trained using TAVI [20], a demonstration-guided residual RL algorithm that collects a few expert demonstrations and learns a robot policy using both ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** methods, first, phase, involves, obtaining, non-parametric, base-policy, encoded, representations, actions, Behavior, Cloning, Given, dataset, expert, rollouts, desired, task, form, observation.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data schema / normalization | The primary idea behind OPEN TEACH is that given any robotic setup, a user can purchase an affordable off-the-shelf VR headset (in ... | p. 6 (4) How intuitive is the system for new users?), p. 6 (V. EXPERIMENTAL EVALUATION) |
| Coverage / augmentation | On these tasks, OPEN TEACH demonstrates a higher success rate along with significantly reduced median time to complete tasks compared to the ... | p. 8 (4) How intuitive is the system for new users?), p. 5 (Figure/Table caption) |
| Downstream learning interface | Overall, the learned policies achieve an average success rate of 86% across all tasks and robot morphologies. | p. 6 (4) How intuitive is the system for new users?), p. 6 (4) How intuitive is the system for new users?) |

## Failure and Ablation Link

- **p. 6 / 4) How intuitive is the system for new users? - extractive body cue:** Each setup is a combination of a variant of a robot arm with either an Allegro Hand or a 2-fingered gripper.
- **p. 6 / 4) How intuitive is the system for new users? - extractive body cue:** The primary idea behind OPEN TEACH is that given any robotic setup, a user can purchase an affordable off-the-shelf VR headset (in this case, Quest ...
- **p. 8 / VI. LIMITATIONS AND DISCUSSION - extractive body cue:** However, we recognize a few limitations in this work: (a) OPEN TEACH relies on the accuracy of the in-built hand pose detection in the VR ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: The demonstration collection process as viewed from within the VR application. Shown here is one task being performed for each real-world setup. High ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (III. BACKGROUND ON IMITATION LEARNING), p. 3 (III. BACKGROUND ON IMITATION LEARNING), p. 5 (IV. OPEN TEACH), p. 5 (IV. OPEN TEACH), p. 2 (Abstract), p. 6 (4) How intuitive is the system for new users?), objective p. 3 (III. BACKGROUND ON IMITATION LEARNING), p. 2 (I. INTRODUCTION), p. 2 (Abstract), p. 3 (III. BACKGROUND ON IMITATION LEARNING), p. 5 (IV. OPEN TEACH), p. 6 (4) How intuitive is the system for new users?), temporal p. 5 (IV. OPEN TEACH), p. 8 (VI. LIMITATIONS AND DISCUSSION), p. 1 (Front matter), p. 1 (Front matter), p. 2 (I. INTRODUCTION), p. 3 (III. BACKGROUND ON IMITATION LEARNING).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
