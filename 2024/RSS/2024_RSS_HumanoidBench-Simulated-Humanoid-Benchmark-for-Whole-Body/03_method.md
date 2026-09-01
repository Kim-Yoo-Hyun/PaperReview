# Method - HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (13 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p061.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p061.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 1 (I. INTRODUCTION), p. 1 (Abstract), p. 2 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): In this paper, we present extensive benchmarking results of the state-of-the-art reinforcement leaning (RL) algorithms, which do not require extensive domain knowledge, and a hierarchical RL approach,

## Method Body Digest

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present extensive benchmarking results of the state-of-the-art reinforcement leaning (RL) algorithms, which do not require extensive domain knowledge, and a hierarchical ...
- **p. 1 / Abstract - extractive body cue:** To aecelerate algorithmic research in humanoid robots, we present a high-dimensional, simulated robot learning henchmark, HumanoidBench, featuring a humanoid robot equipped with dexterous hands and ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** The benchmarking results on this task suite show how the state-ofthe-art RL algorithms struggle with controlling the complex humanoid robot dynamics and solving the most ...
- **p. 3 / I. INTRODUCTION - extractive body cue:** We use two dexterous Shadow Hands*, which also have model files freely available®, and have shown impressive manipulation capabilities both in simulation [67] and in ...
- **p. 3 / I. INTRODUCTION - extractive body cue:** Although other sensory inputs are available from the environment, to investigate challenges in whole-body control of humanoid robots, we first focus on the state-based environment ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** This motivates us to implement a comprehensive simulated humanoid benchmark based on real-world hardware and consisting of a diverse set of whole-body control tasks with ...
- **p. 5 / IV. HuMANOIDBENcH - extractive body cue:** On the other hand, wholebody manipulation tasks render a comprehensive evaluation of the state-of-the-art algorithms on challenging tasks with unique challenges that require coordination across ...
- **p. 6 / IV. HuMANOIDBENcH - extractive body cue:** mns represent the standard deviation, Returns are computed by summing the rewards at all timesteps of an episode.

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** To accelerate the progress of research for humanoid robots, We present the first-of-its-kind humanoid robot benchmark, HumanoidBench, with a diverse set of locomotion and manipulation ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present extensive benchmarking results of the state-of-the-art reinforcement leaning (RL) algorithms, which do not require extensive domain knowledge, and a hierarchical ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** 4, 42, 29, 17, 30, 48] In the context of humanoids, we propose an HRL paradigm

## Source Evidence Cues

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present extensive benchmarking results of the state-of-the-art reinforcement leaning (RL) algorithms, which do not require extensive domain knowledge, and a hierarchical ...
- **p. 1 / Abstract - extractive body cue:** To aecelerate algorithmic research in humanoid robots, we present a high-dimensional, simulated robot learning henchmark, HumanoidBench, featuring a humanoid robot equipped with dexterous hands and ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** The benchmarking results on this task suite show how the state-ofthe-art RL algorithms struggle with controlling the complex humanoid robot dynamics and solving the most ...
- **p. 3 / I. INTRODUCTION - extractive body cue:** We use two dexterous Shadow Hands*, which also have model files freely available®, and have shown impressive manipulation capabilities both in simulation [67] and in ...
- **p. 3 / I. INTRODUCTION - extractive body cue:** Although other sensory inputs are available from the environment, to investigate challenges in whole-body control of humanoid robots, we first focus on the state-based environment ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** This motivates us to implement a comprehensive simulated humanoid benchmark based on real-world hardware and consisting of a diverse set of whole-body control tasks with ...
- **p. 5 / IV. HuMANOIDBENcH - extractive body cue:** On the other hand, wholebody manipulation tasks render a comprehensive evaluation of the state-of-the-art algorithms on challenging tasks with unique challenges that require coordination across ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | In this paper, we present extensive benchmarking results of the state-of-the-art reinforcement leaning (RL) algorithms, which do not require extensive domain knowledge, ... | p. 1 (I. INTRODUCTION), p. 1 (Abstract) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | To aecelerate algorithmic research in humanoid robots, we present a high-dimensional, simulated robot learning henchmark, HumanoidBench, featuring a humanoid robot equipped with ... | p. 1 (Abstract), p. 2 (I. INTRODUCTION) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | The benchmarking results on this task suite show how the state-ofthe-art RL algorithms struggle with controlling the complex humanoid robot dynamics and ... | p. 2 (I. INTRODUCTION), p. 3 (I. INTRODUCTION) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / IV. HuMANOIDBENcH - extractive body cue:** mns represent the standard deviation, Returns are computed by summing the rewards at all timesteps of an episode.
- **p. 1 / Abstract - extractive body cue:** However, research in humanoid robots is often bottlenecked by the costly and fragile hardware setups.
- **p. 1 / I. INTRODUCTION - extractive body cue:** still challenging and has been delayed mainly due to such robots' costly and unsafe real-world experimental setups,
- **p. 2 / I. INTRODUCTION - extractive body cue:** While bimanual ‘manipulation is one of the key objectives of humanoid robots, ‘most benchmarks in humanoid research have so far focused on the locomotion challenges ...
- **p. 3 / I. INTRODUCTION - extractive body cue:** In our statebased environment, we maintain the robot observations the same across tasks to minimize domain knowledge, in contrast to tailoring it to the specific ...
- **p. 5 / IV. HuMANOIDBENcH - extractive body cue:** Further details about each of the tasks, including task initialization and reward functions, are provided in Appendix, Section B-E.
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** p. 2 (I. INTRODUCTION).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Proprioceptive, robot, state, joint, angles, velocities, task-relevant, environment, observations, object, poses, Although, other, sensory | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | Proprioceptive, robot, state, joint, angles, velocities, task-relevant, environment, observations, object | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | accelerate, progress, research, humanoid, robots, present, first-of-its-kind, robot, benchmark, HumanoidBench | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | represent, standard, deviation, Returns, computed, summing, rewards, timesteps, episode, However | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / I. INTRODUCTION - extractive body cue:** + Proprioceptive robot state (i, joint angles and velocities) and task-relevant environment observations (ie, object, poses and velocities)
- **p. 3 / I. INTRODUCTION - extractive body cue:** Although other sensory inputs are available from the environment, to investigate challenges in whole-body control of humanoid robots, we first focus on the state-based environment ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present extensive benchmarking results of the state-of-the-art reinforcement leaning (RL) algorithms, which do not require extensive domain knowledge, and a hierarchical ...
- **p. 1 / Abstract - extractive body cue:** To aecelerate algorithmic research in humanoid robots, we present a high-dimensional, simulated robot learning henchmark, HumanoidBench, featuring a humanoid robot equipped with dexterous hands and ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** This motivates us to implement a comprehensive simulated humanoid benchmark based on real-world hardware and consisting of a diverse set of whole-body control tasks with ...
- **p. 4 / I. INTRODUCTION - extractive body cue:** For both position and torque control, the action space is 6-dimensional including the two hands, and controlled at 50 Hz.
- **p. 2 / I. INTRODUCTION - extractive body cue:** horizon task with a large action space.
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | mns represent the standard deviation, Returns are computed by summing the rewards at all timesteps of an episode. | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | still challenging and has been delayed mainly due to such robots' costly and unsafe real-world experimental setups, | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not recovered | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | For both position and torque control, the action space is 6-dimensional including the two hands, and controlled at 50 Hz. | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** present, extensive, benchmarking, state-of-the-art, reinforcement, leaning, algorithms, require, domain, knowledge, hierarchical, aecelerate, algorithmic, research, humanoid, robots, high-dimensional, simulated, robot, learning.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | To identify the challenges in learning with humanoid robots, we benchmark reinforcement learning (RL) algorithms on HumanoidBench, which promises for robots to ... | p. 7 (V. BENCHMARKING RESULTS), p. 8 (B. Results) |
| Baseline harness | In Figure 9, our hierarchical architecture significantly outperforms the flat, end-to-end baselines on the push task, achieving very high success rates ‘with ... | p. 9 (B. Results), p. 8 (B. Results) |
| Metric / failure reporting | In Figure 9, our hierarchical architecture significantly outperforms the flat, end-to-end baselines on the push task, achieving very high success rates ‘with ... | p. 9 (B. Results), p. 9 (B. Results) |

## Failure and Ablation Link

- **p. 8 / B. Results - extractive body cue:** 7: Performance with and without dexterous hands.
- **p. 8 / B. Results - extractive body cue:** We observe similar trends in the more complex manipulation task, push, wihch presents substantially different dynamics in the task approach (e.g., pushing with and without ...
- **p. 9 / B. Results - extractive body cue:** We also remove the hands from the model to further increase training efficiency.
- **p. 9 / B. Results - extractive body cue:** Low-level Reaching Policy Pretraining.
- **p. 9 / B. Results - extractive body cue:** In this subsection, we remark on notable challenges and com- ‘mon failures for some representative tasks in our benchmark, which denote the challenge in learning ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 10: Failure Scenarios. This figure presents a selection of common failures that occur while training our benchmark tasks.
- **p. 9 / B. Results - extractive body cue:** For low-level reaching policy training, we employ a simplified Hi model that only considers collisions between feet and ground in the MuJoCo MIX environments, as ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 1 (I. INTRODUCTION), p. 1 (Abstract), p. 2 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), objective p. 6 (IV. HuMANOIDBENcH), p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 5 (IV. HuMANOIDBENcH), temporal p. 6 (IV. HuMANOIDBENcH), p. 1 (I. INTRODUCTION), p. 1 (Front matter), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (I. INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
