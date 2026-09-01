# Method - RLBench: The Robot Learning Benchmark & Learning Environment

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1909.12271; PDF retrieval source: https://arxiv.org/pdf/1909.12271. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 1 (I. INTRODUCTION), p. 3 (III. BENCHMARK PROPERTIES), p. 4 (IV. RLBENCH), p. 1 (I. INTRODUCTION), p. 4 (IV. RLBENCH), p. 5 (IV. RLBENCH)): Robot manipulation systems broadly fall somewhere on a spectrum ranging from traditional, modular methods, that include object recognition, state estimation, and planning, to fully end-to-end approaches that leverage deep learning ...

## Method Body Digest

- **p. 1 / I. INTRODUCTION - extractive body cue:** Robot manipulation systems broadly fall somewhere on a spectrum ranging from traditional, modular methods, that include object recognition, state estimation, and planning, to fully end-to-end ...
- **p. 3 / III. BENCHMARK PROPERTIES - extractive body cue:** We therefore wanted to have a range of tasks, including both easy tasks, such as reaching, which would be well suited to new and emerging ...
- **p. 4 / IV. RLBENCH - extractive body cue:** Formally, we define an episode trajectory τ to consist of a series of observations o and actions a: τ = [(o1, a1), . . . ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To summarise, RLBench has the following 3 key aims: • Provide a benchmark and learning environment for both ‘robot learning' and ‘traditional' methods. • Provide ...
- **p. 4 / IV. RLBENCH - extractive body cue:** The environment API, which Figure 5 demonstrates, is modelled after a typical agent-environment reinforcement learning setup.
- **p. 5 / IV. RLBENCH - extractive body cue:** 5: Example usage of the RLBench Environment for training a reinforcement learning agent.
- **p. 5 / IV. RLBENCH - extractive body cue:** 1 from rlbench.environment import Environment 2 from rlbench.action_modes import ActionMode 3 from rlbench.tasks import ReachTarget 4 5 DATASET = 'path/to/demo/dataset' 6 7 env = Environment( ...
- **p. 4 / IV. RLBENCH - extractive body cue:** Each variation comes with a list of textual descriptions that describes the objective.

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** To that end, we present RLBench, which is an ambitious large-scale benchmark and learning environment designed to facilitate research in a number of both classical ...
- **p. 1 / Abstract - extractive body cue:** With the benchmark's breadth of tasks and demonstrations, we propose the first large-scale fewshot challenge in robotics.
- **p. 4 / IV. RLBENCH - extractive body cue:** Each task consists of one or more variations, and from each variation, an infinite number of episodes can be drawn.

## Source Evidence Cues

- **p. 1 / I. INTRODUCTION - extractive body cue:** Robot manipulation systems broadly fall somewhere on a spectrum ranging from traditional, modular methods, that include object recognition, state estimation, and planning, to fully end-to-end ...
- **p. 3 / III. BENCHMARK PROPERTIES - extractive body cue:** We therefore wanted to have a range of tasks, including both easy tasks, such as reaching, which would be well suited to new and emerging ...
- **p. 4 / IV. RLBENCH - extractive body cue:** Formally, we define an episode trajectory τ to consist of a series of observations o and actions a: τ = [(o1, a1), . . . ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To summarise, RLBench has the following 3 key aims: • Provide a benchmark and learning environment for both ‘robot learning' and ‘traditional' methods. • Provide ...
- **p. 4 / IV. RLBENCH - extractive body cue:** The environment API, which Figure 5 demonstrates, is modelled after a typical agent-environment reinforcement learning setup.
- **p. 5 / IV. RLBENCH - extractive body cue:** 5: Example usage of the RLBench Environment for training a reinforcement learning agent.
- **p. 5 / IV. RLBENCH - extractive body cue:** 1 from rlbench.environment import Environment 2 from rlbench.action_modes import ActionMode 3 from rlbench.tasks import ReachTarget 4 5 DATASET = 'path/to/demo/dataset' 6 7 env = Environment( ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | Robot manipulation systems broadly fall somewhere on a spectrum ranging from traditional, modular methods, that include object recognition, state estimation, and planning, ... | p. 1 (I. INTRODUCTION), p. 3 (III. BENCHMARK PROPERTIES) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | We therefore wanted to have a range of tasks, including both easy tasks, such as reaching, which would be well suited to ... | p. 3 (III. BENCHMARK PROPERTIES), p. 4 (IV. RLBENCH) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | Formally, we define an episode trajectory τ to consist of a series of observations o and actions a: τ = [(o1, a1), ... | p. 4 (IV. RLBENCH), p. 1 (I. INTRODUCTION) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / IV. RLBENCH - extractive body cue:** Each variation comes with a list of textual descriptions that describes the objective.
- **p. 4 / IV. RLBENCH - extractive body cue:** Each task has a completely sparse reward of +1 which is given only on task completion.
- **p. 5 / IV. RLBENCH - extractive body cue:** 1 from rlbench.environment import Environment 2 from rlbench.action_modes import ActionMode 3 from rlbench.tasks import ReachTarget 4 5 DATASET = 'path/to/demo/dataset' 6 7 env = Environment( ...
- **p. 1 / Abstract - extractive body cue:** This large-scale benchmark aims to accelerate progress in a number of vision-guided manipulation research areas, including: reinforcement learning, imitation learning, multi-task learning, geometric computer vision, ...
- **p. 5 / IV. RLBENCH - extractive body cue:** This function returns a list of strings which provide descriptions that could be associated with this variation of the task; an analysis of the frequency ...
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** p. 4 (IV. RLBENCH).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Robot, manipulation, systems, broadly, fall, somewhere, spectrum, ranging, traditional, modular, methods, include, object, recognition | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | Robot, manipulation, systems, broadly, fall, somewhere, spectrum, ranging, traditional, modular | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | present, RLBench, ambitious, large-scale, benchmark, learning, environment, designed, facilitate, research | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | variation, comes, list, textual, descriptions, describes, objective, task, completely, sparse | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / I. INTRODUCTION - extractive body cue:** Robot manipulation systems broadly fall somewhere on a spectrum ranging from traditional, modular methods, that include object recognition, state estimation, and planning, to fully end-to-end ...
- **p. 4 / IV. RLBENCH - extractive body cue:** Formally, we define an episode trajectory τ to consist of a series of observations o and actions a: τ = [(o1, a1), . . . ...
- **p. 3 / III. BENCHMARK PROPERTIES - extractive body cue:** 3: A sample of the visual observations given from both the over-the-shoulder stereo and eye-in-hand monocular cameras, which supply rgb, depth, and mask images. d) ...
- **p. 4 / IV. RLBENCH - extractive body cue:** In addition to visual observations, robot proprioceptive data can be retrieved, which includes joint angles, velocities, and torques, along with the end-effector pose.
- **p. 1 / Abstract - extractive body cue:** We provide an array of both proprioceptive observations and visual observations, which include rgb, depth, and segmentation masks from an over-the-shoulder stereo camera and an ...
- **p. 5 / IV. RLBENCH - extractive body cue:** 1 from rlbench.environment import Environment 2 from rlbench.action_modes import ActionMode 3 from rlbench.tasks import ReachTarget 4 5 DATASET = 'path/to/demo/dataset' 6 7 env = Environment( ...
- **p. 3 / III. BENCHMARK PROPERTIES - extractive body cue:** We therefore wanted to have a range of tasks, including both easy tasks, such as reaching, which would be well suited to new and emerging ...
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | 1 from rlbench.environment import Environment 2 from rlbench.action_modes import ActionMode 3 from rlbench.tasks import ReachTarget 4 5 DATASET = 'path/to/demo/dataset' 6 7 ... | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | The tasks lengths vary from 100 to 1000 timesteps. | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not recovered | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | 1 from rlbench.environment import Environment 2 from rlbench.action_modes import ActionMode 3 from rlbench.tasks import ReachTarget 4 5 DATASET = 'path/to/demo/dataset' 6 7 ... | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / I. INTRODUCTION - extractive body cue:** To summarise, RLBench has the following 3 key aims: • Provide a benchmark and learning environment for both ‘robot learning' and ‘traditional' methods. • Provide ...
- **p. 5 / IV. RLBENCH - extractive body cue:** 5: Example usage of the RLBench Environment for training a reinforcement learning agent.
- **p. 5 / IV. RLBENCH - extractive body cue:** 1 from rlbench.environment import Environment 2 from rlbench.action_modes import ActionMode 3 from rlbench.tasks import ReachTarget 4 5 DATASET = 'path/to/demo/dataset' 6 7 env = Environment( ...
- **p. 5 / IV. RLBENCH - extractive body cue:** 1 from rlbench.environment import Environment 2 from rlbench.action_modes import ActionMode 3 from rlbench.tasks import ReachTarget 4 5 DATASET = 'path/to/demo/dataset' 6 7 env = Environment( ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Robot, manipulation, systems, broadly, fall, somewhere, spectrum, ranging, traditional, modular, methods, include, object, recognition, state, estimation, planning, fully, end-to-end, approaches.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | However, with the rise of deep-learning methods becoming more prominent in robotics, we believe it is important to find the potential and ... | p. 3 (III. BENCHMARK PROPERTIES), p. 3 (III. BENCHMARK PROPERTIES) |
| Baseline harness | We therefore wanted to have a range of tasks, including both easy tasks, such as reaching, which would be well suited to ... | p. 3 (III. BENCHMARK PROPERTIES), p. 6 (Figure/Table caption) |
| Metric / failure reporting | Fig. 6: An example of a task python file. When using the task building tool, users are able to simultaneously edit the ... | p. 5 (Figure/Table caption), p. 3 (III. BENCHMARK PROPERTIES) |

## Failure and Ablation Link

- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 7: Top shows the frequency of words in the variation descriptions with function words removed, leaving only content words. Bottom shows the average length ...
- **p. 3 / III. BENCHMARK PROPERTIES - extractive body cue:** We therefore wanted to have a range of tasks, including both easy tasks, such as reaching, which would be well suited to new and emerging ...
- **p. 3 / III. BENCHMARK PROPERTIES - extractive body cue:** We therefore wanted to have a range of tasks, including both easy tasks, such as reaching, which would be well suited to new and emerging ...
- **p. 5 / IV. RLBENCH - extractive body cue:** Once a task has been created, we provide a task validation tool, that attempts to collect a number of demonstrations of the designed task in ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 1 (I. INTRODUCTION), p. 3 (III. BENCHMARK PROPERTIES), p. 4 (IV. RLBENCH), p. 1 (I. INTRODUCTION), p. 4 (IV. RLBENCH), p. 5 (IV. RLBENCH), objective p. 4 (IV. RLBENCH), p. 4 (IV. RLBENCH), p. 5 (IV. RLBENCH), p. 1 (Abstract), p. 5 (IV. RLBENCH), temporal p. 5 (IV. RLBENCH), p. 6 (V. THE RLBENCH FEW-SHOT CHALLENGE (v 1.0)), p. 1 (Front matter), p. 2 (II. RELATED WORK), p. 2 (II. RELATED WORK), p. 3 (III. BENCHMARK PROPERTIES).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
