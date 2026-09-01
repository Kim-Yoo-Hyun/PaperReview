# Method - RoboNet: Large-Scale Multi-Robot Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v100/dasari20a.html; PDF retrieval source: https://proceedings.mlr.press/v100/dasari20a.html. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 13 (C Database Implementation Details), p. 13 (C Database Implementation Details), p. 12 (C Database Implementation Details), p. 12 (C Database Implementation Details)): We collected 300 new trajectories with a Robotiq 2-finger gripper, which differs significantly in visual appearance and dimensions from the Weiss Robotics gripper used in all other Sawyer trajectories (see ...

## Method Body Digest

- **p. 13 / C Database Implementation Details - extractive PDF cue:** We collected 300 new trajectories with a Robotiq 2-finger gripper, which differs significantly in visual appearance and dimensions from the Weiss Robotics gripper used in ...
- **p. 13 / C Database Implementation Details - extractive PDF cue:** executing the action sequences computed by the algorithm the remaining distance to the goal is measured using a tape, and success is determined by human ...
- **p. 12 / C Database Implementation Details - extractive PDF cue:** New trajectory attributes can be added easily.
- **p. 12 / C Database Implementation Details - extractive PDF cue:** The database stores every trajectory as a separate entity with a set of attributes that can be filtered.
- **p. 1 / 1 Introduction - extractive PDF cue:** Inspired by the breadth of the ImageNet dataset [8], we introduce RoboNet, a dataset containing roughly 162,000 trajectories with video and action sequences recorded from ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Visual foresight uses an action-conditioned video prediction model trained on the collected data to plan actions that achieve user-specified goals.
- **p. 2 / 1 Introduction - extractive PDF cue:** Second, we study deep inverse models that are trained to predict the action taken to reach one image from another image, and can be used ...
- **p. 13 / C Database Implementation Details - extractive PDF cue:** However, these results do demonstrate that visual foresight models can adapt to moderate morphological changes using a modest amount of data. t = 0 t ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive PDF cue:** Our main contributions therefore consist of the RoboNet dataset, and an experimental evaluation that studies our framework for multi-robot, multi-domain model-based reinforcement learning based on ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Instead, we propose the opposite - using dramatically larger and more varied datasets collected in the real world.
- **p. 1 / 1 Introduction - extractive PDF cue:** Inspired by the breadth of the ImageNet dataset [8], we introduce RoboNet, a dataset containing roughly 162,000 trajectories with video and action sequences recorded from ...

## Source Evidence Cues

- **p. 13 / C Database Implementation Details - extractive PDF cue:** We collected 300 new trajectories with a Robotiq 2-finger gripper, which differs significantly in visual appearance and dimensions from the Weiss Robotics gripper used in ...
- **p. 13 / C Database Implementation Details - extractive PDF cue:** executing the action sequences computed by the algorithm the remaining distance to the goal is measured using a tape, and success is determined by human ...
- **p. 12 / C Database Implementation Details - extractive PDF cue:** New trajectory attributes can be added easily.
- **p. 12 / C Database Implementation Details - extractive PDF cue:** The database stores every trajectory as a separate entity with a set of attributes that can be filtered.
- **Detected method headings:** A.1 Action conditioned video-prediction model (p. 11)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Data schema / normalization | heterogeneous robot trajectory를 공통 sample로 만든다 | observation, action, task와 embodiment metadata | sensor/action schema alignment, filtering, normalization을 수행 | shared dataset representation | We collected 300 new trajectories with a Robotiq 2-finger gripper, which differs significantly in visual appearance and dimensions from the Weiss Robotics ... | p. 13 (C Database Implementation Details), p. 13 (C Database Implementation Details) |
| Coverage / augmentation | task·embodiment·failure variation을 확장한다 | dataset과 metadata | retargeting, relabeling, synthetic/teleoperation augmentation 또는 sampling을 적용 | expanded data support | executing the action sequences computed by the algorithm the remaining distance to the goal is measured using a tape, and success is ... | p. 13 (C Database Implementation Details), p. 12 (C Database Implementation Details) |
| Downstream learning interface | 정규화된 data를 policy/representation이 사용한다 | shared observations/actions | pretraining, BC, action-token 또는 representation learning을 수행 | checkpoint/policy action | New trajectory attributes can be added easily. | p. 12 (C Database Implementation Details), p. 12 (C Database Implementation Details) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** trajectory D with task/embodiment metadata -> normalized sample or downstream action -> coverage/data efficiency/transfer objective -> cross-domain transfer and task performance.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Inspired, breadth, ImageNet, dataset, introduce, RoboNet, containing, roughly, trajectories, video, action, sequences, recorded, robots | multi-view observation, language/task label과 action trajectory | body cue; exact tensor/frame verify |
| State/latent | Inspired, breadth, ImageNet, dataset, introduce, RoboNet, containing, roughly, trajectories, video | shared representation, embodiment/task identity와 data distribution | body cue; notation verify |
| Action/output | main, contributions, therefore, consist, RoboNet, dataset, experimental, evaluation, studies, framework | dataset sample 또는 learned policy action | body cue; unit/decoder verify |
| Objective/constraint | not recovered | coverage/data efficiency/transfer objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1 Introduction - extractive PDF cue:** Inspired by the breadth of the ImageNet dataset [8], we introduce RoboNet, a dataset containing roughly 162,000 trajectories with video and action sequences recorded from ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Visual foresight uses an action-conditioned video prediction model trained on the collected data to plan actions that achieve user-specified goals.
- **p. 2 / 1 Introduction - extractive PDF cue:** Second, we study deep inverse models that are trained to predict the action taken to reach one image from another image, and can be used ...
- **p. 13 / C Database Implementation Details - extractive PDF cue:** executing the action sequences computed by the algorithm the remaining distance to the goal is measured using a tape, and success is determined by human ...
- **p. 13 / C Database Implementation Details - extractive PDF cue:** However, these results do demonstrate that visual foresight models can adapt to moderate morphological changes using a modest amount of data. t = 0 t ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Instead, we propose the opposite - using dramatically larger and more varied datasets collected in the real world.
- **p. 12 / C Database Implementation Details - extractive PDF cue:** Data is stored in the widely adopted hdf5-format, and videos are encoded via MP4 for efficiency reasons.
- **Normalized interface:** observation=multi-view observation, language/task label과 action trajectory; state=shared representation, embodiment/task identity와 data distribution; output/action=dataset sample 또는 learned policy action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | trajectory demonstration horizon; training sample window와 deployment task horizon을 분리한다. | Inspired by the breadth of the ImageNet dataset [8], we introduce RoboNet, a dataset containing roughly 162,000 trajectories with video and action ... | episode/sequence/action-chunk boundary |
| Rate / latency | data recording/action sampling rate와 policy inference/control rate를 분리한다. | executing the action sequences computed by the algorithm the remaining distance to the goal is measured using a tape, and success is ... | Hz/fps, inference time and control rate |
| Memory | trajectory, embodiment/task metadata와 dataset index. | This avoids the need to calibrate the camera, but requires any model to infer the relative positioning between the camera and the ... | window and reset |
| Compute | data decoding, normalization/augmentation과 downstream training budget이 결정한다. | Inspired by the breadth of the ImageNet dataset [8], we introduce RoboNet, a dataset containing roughly 162,000 trajectories with video and action ... | hardware, batch and throughput |

## Training vs Inference

- **p. 13 / C Database Implementation Details - extractive PDF cue:** We collected 300 new trajectories with a Robotiq 2-finger gripper, which differs significantly in visual appearance and dimensions from the Weiss Robotics gripper used in ...
- **p. 12 / C Database Implementation Details - extractive PDF cue:** We provide code infrastructure that allows a user to filter certain subsets of attributes for training and testing.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** collected, trajectories, Robotiq, finger, gripper, differs, significantly, visual, appearance, dimensions, Weiss, Robotics, other, Sawyer, Figure, data, evaluate, four, different, models.
- **Relevant PDF headings:** A.1 Action conditioned video-prediction model (p. 11).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data schema / normalization | However, these results do demonstrate that visual foresight models can adapt to moderate morphological changes using a modest amount of data. t ... | p. 13 (C Database Implementation Details), p. 13 (C Database Implementation Details) |
| Coverage / augmentation | Table 4: Results for adapta- tion to an unseen Franka robot. The model pre-trained on RoboNet without the Franka, R3, and Fetch ... | p. 6 (Figure/Table caption), p. 13 (Figure/Table caption) |
| Downstream learning interface | Table 5: Evaluation results for adaptation to an unseen Baxter robot. The model pre-trained on RoboNet's Sawyer data, achieves the best performance ... | p. 6 (Figure/Table caption), p. 7 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 4: Results for adapta- tion to an unseen Franka robot. The model pre-trained on RoboNet without the Franka, R3, and Fetch data, achieves the ...
- **p. 13 / Figure/Table caption - extractive PDF cue:** Figure 8: Example task of pushing an object with an unseen gripper, in this case the Robotiq gripper. Avg. distance (cm) zero-shot 15.5 ± 2.6 ...
- **p. 13 / C Database Implementation Details - extractive PDF cue:** Avg. distance (cm) zero-shot 15.5 ± 2.6 without pretraining 17 ± 1.8 pretraining on Sawyer-only 9.8 ± 2.1 pretraining on all of RoboNet 14.7 ± ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4: Example task of grasping and moving a thin plastic cup with the Franka robot, using visual foresight pre-trained on RoboNet w/o Franka and ...
- **p. 8 / 6 Discussion - extractive PDF cue:** Next, we discuss limitations of the dataset and evaluation, and additional directions for future work.
- **p. 8 / 6 Discussion - extractive PDF cue:** While our results demonstrated a large degree of generalization, a number of important limitations remain, which we aim to study in future work.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 13 (C Database Implementation Details), p. 13 (C Database Implementation Details), p. 12 (C Database Implementation Details), p. 12 (C Database Implementation Details), objective 본문 anchor 없음, temporal p. 1 (1 Introduction), p. 13 (C Database Implementation Details), p. 4 (2 Related Work), p. 1 (Front matter), p. 2 (1 Introduction), p. 2 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
