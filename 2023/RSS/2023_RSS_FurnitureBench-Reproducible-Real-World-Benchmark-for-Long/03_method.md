# Method - FurnitureBench: Reproducible Real-World Benchmark for Long-Horizon Complex Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (35 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2305.12821; PDF retrieval source: https://arxiv.org/pdf/2305.12821. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 7 (2) The furniture parts are rearranged using our provided)): The main contributions of this paper are as follows: • We introduce FurnitureBench, a real-world furniture assembly benchmark, which allows robotics researchers to investigate RL, IL, and TAMP algorithms on ...

## Method Body Digest

- **p. 2 / I. INTRODUCTION - extractive body cue:** The main contributions of this paper are as follows: • We introduce FurnitureBench, a real-world furniture assembly benchmark, which allows robotics researchers to investigate RL, ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Due to the limitations imposed by using a single robotic arm, we modify some furniture pieces feasible to be assembled with one hand. strations that ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** (Right) A suite of 8 furniture models in our benchmark.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** (Left) A decorated room in the real world with furniture models our robot assembled.
- **p. 7 / 2) The furniture parts are rearranged using our provided - extractive body cue:** 3) A policy controls the robot until it completes the task, stops motions for 5 sec, shows unsafe movements, exceeds 350 steps per skill, or ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our reproducible robot system (a) and visual observations from the front-view camera (b) and wrist camera (c). of long-horizon complex robotic manipulation tasks.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Benchmarking furniture assembly poses to address many robotic manipulation challenges: long-horizon planning, dexterous control, and visual perception.
- **p. 1 / Abstract - extractive body cue:** Reinforcement learning (RL), imitation learning (IL), and task and motion planning (TAMP) have demonstrated impressive performance across various robotic manipulation tasks.

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** The main contributions of this paper are as follows: • We introduce FurnitureBench, a real-world furniture assembly benchmark, which allows robotics researchers to investigate RL, ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To this end, we propose to focus on furniture assembly as the next milestone for complex, long-horizon robotic manipulation, and present FurnitureBench, a reproducible real-world ...
- **p. 1 / Abstract - extractive body cue:** To enable more complex, long-horizon behaviors of an autonomous robot, we propose to focus on real-world furniture assembly, a complex, longhorizon robot manipulation task that ...

## Source Evidence Cues

- **p. 2 / I. INTRODUCTION - extractive body cue:** The main contributions of this paper are as follows: • We introduce FurnitureBench, a real-world furniture assembly benchmark, which allows robotics researchers to investigate RL, ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Due to the limitations imposed by using a single robotic arm, we modify some furniture pieces feasible to be assembled with one hand. strations that ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** (Right) A suite of 8 furniture models in our benchmark.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** (Left) A decorated room in the real world with furniture models our robot assembled.
- **p. 7 / 2) The furniture parts are rearranged using our provided - extractive body cue:** 3) A policy controls the robot until it completes the task, stops motions for 5 sec, shows unsafe movements, exceeds 350 steps per skill, or ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | The main contributions of this paper are as follows: • We introduce FurnitureBench, a real-world furniture assembly benchmark, which allows robotics researchers ... | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | Due to the limitations imposed by using a single robotic arm, we modify some furniture pieces feasible to be assembled with one ... | p. 2 (I. INTRODUCTION), p. 1 (Body text (section boundary not confidently recovered)) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | (Right) A suite of 8 furniture models in our benchmark. | p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update PDF body cue not selected; no claim inferred - inspect equations and algorithm boxes
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | reproducible, robot, system, visual, observations, front-view, camera, wrist, long-horizon, complex, robotic, manipulation, tasks, policy | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | reproducible, robot, system, visual, observations, front-view, camera, wrist, long-horizon, complex | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | main, contributions, follows, introduce, FurnitureBench, real-world, furniture, assembly, benchmark, allows | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | not stated or recoverable in the selected PDF body | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our reproducible robot system (a) and visual observations from the front-view camera (b) and wrist camera (c). of long-horizon complex robotic manipulation tasks.
- **p. 7 / 2) The furniture parts are rearranged using our provided - extractive body cue:** 3) A policy controls the robot until it completes the task, stops motions for 5 sec, shows unsafe movements, exceeds 350 steps per skill, or ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Benchmarking furniture assembly poses to address many robotic manipulation challenges: long-horizon planning, dexterous control, and visual perception.
- **p. 1 / Abstract - extractive body cue:** Reinforcement learning (RL), imitation learning (IL), and task and motion planning (TAMP) have demonstrated impressive performance across various robotic manipulation tasks.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To this end, we propose to focus on furniture assembly as the next milestone for complex, long-horizon robotic manipulation, and present FurnitureBench, a reproducible real-world ...
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | The task horizon is approximately 500 timesteps. | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | A trained model is evaluated for 10 episodes, where their initial states are set following the provided task initialization guide tool. | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | A trained model is evaluated for 10 episodes, where their initial states are set following the provided task initialization guide tool. | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** Please refer to Section D for implementation details. • BC (Behavioral Cloning [48]) fits a policy to the demonstration state-action pairs (s, a) with supervised ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** main, contributions, follows, introduce, FurnitureBench, real-world, furniture, assembly, benchmark, allows, robotics, researchers, investigate, TAMP, algorithms, realistic, complex, task, beyond, pick-and-place.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | But, this benchmark environment and tasks can be also used for research in TAMP. | p. 7 (VI. BENCHMARKING RESULTS), p. 7 (VI. BENCHMARKING RESULTS) |
| Baseline harness | We evaluate our benchmark with imitation learning (BC) and the state-of-the-art offline RL (IQL) methods. | p. 6 (V. EXPERIMENTAL SETUP), p. 6 (V. EXPERIMENTAL SETUP) |
| Metric / failure reporting | The "pushing" skill in drawer achieves 30% success rate, which is slightly worse than that of the "grasping" skill (60%), with BC. | p. 7 (VI. BENCHMARKING RESULTS), p. 7 (VI. BENCHMARKING RESULTS) |

## Failure and Ablation Link

- **p. 7 / VI. BENCHMARKING RESULTS - extractive body cue:** 3This paper focuses on benchmarking end-to-end learning approaches since engineering furniture assembly procedures using TAMP without having access to state information is beyond the scope ...
- **p. 8 / VI. BENCHMARKING RESULTS - extractive body cue:** This result means that the policies mostly fail to grasp the table leg without the wrist camera.
- **p. 8 / VI. BENCHMARKING RESULTS - extractive body cue:** Without the wrist camera input, the performance drops significantly from 3.8 and 3.0 to 2.0 and 1.3 on the low and medium randomness levels, respectively.
- **p. 15 / Figure/Table caption - extractive body cue:** Fig. 13: AprilTag placeholder. For easy and accurate marker placement, all 3D models have AprilTag placeholders on their surfaces with corresponding AprilTag IDs. of our ...
- **p. 18 / Figure/Table caption - extractive body cue:** Fig. 17: Furniture 3D models. IKEA model furniture (left), 3D furniture model (middle), and 3D printed furniture model (right). Each furniture model introduces unique interactions ...
- **p. 7 / VI. BENCHMARKING RESULTS - extractive body cue:** The failure of these algorithms to even attach a pair of furniture parts despite the high-quality demonstration dataset highlights the need for further algorithmic improvements ...
- **p. 7 / VI. BENCHMARKING RESULTS - extractive body cue:** On the other hand, both algorithms struggle at "inserting" skill, which shows from 0% to 20% success rates. "Inserting" requires precise control to correctly align ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 7 (2) The furniture parts are rearranged using our provided), objective 본문 anchor 없음, temporal p. 7 (VI. BENCHMARKING RESULTS), p. 6 (V. EXPERIMENTAL SETUP), p. 6 (V. EXPERIMENTAL SETUP), p. 3 (II. RELATED WORK), p. 3 (II. RELATED WORK), p. 5 (II. RELATED WORK).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (35 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Reinforcement learning (RL), imitation learning (IL), and task and motion planning (TAMP) have demonstrated impressive performance across various robotic manipulation tasks. (p. 1, Abstract).
- **Objective/update evidence:** (Right) A suite of 8 furniture models in our benchmark. (p. 1, Body text (section boundary not confidently recovered)).
- **Temporal/runtime evidence:** A trained model is evaluated for 10 episodes, where their initial states are set following the provided task initialization guide tool. (p. 6, V. EXPERIMENTAL SETUP).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
