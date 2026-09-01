# Insights — HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (13 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p061.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p061.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / I. INTRODUCTION - extractive body cue:** To accelerate the progress of research for humanoid robots, We present the first-of-its-kind humanoid robot benchmark, HumanoidBench, with a diverse set of locomotion and manipulation ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present extensive benchmarking results of the state-of-the-art reinforcement leaning (RL) algorithms, which do not require extensive domain knowledge, and a hierarchical ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** 4, 42, 29, 17, 30, 48] In the context of humanoids, we propose an HRL paradigm
- **p. 3 / I. INTRODUCTION - extractive body cue:** While this is not currently a realistic model, we anticipate the trend in the industry towards developing slimmer, human-like hhands (e-g., Tesla Optimus, Figure 01) ...
- **p. 4 / I. INTRODUCTION - extractive body cue:** Torque-based control is also supported but we found that position control is generally more stable and allows for lower control frequency than torque control.
- **p. 1 / Abstract - extractive body cue:** To aecelerate algorithmic research in humanoid robots, we present a high-dimensional, simulated robot learning henchmark, HumanoidBench, featuring a humanoid robot equipped with dexterous hands and ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** The benchmarking results on this task suite show how the state-ofthe-art RL algorithms struggle with controlling the complex humanoid robot dynamics and solving the most ...
- **Contribution anchor:** p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 4 (I. INTRODUCTION), p. 1 (Abstract)

### Strongest assumption and failure boundary

- **p. 2 / I. INTRODUCTION - extractive body cue:** However, all these works focus fon demonstrating their approaches on specific humanoid tasks and lack a diversity of tasks.
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, most of these benchmarks use a singlearm manipulation setup with either a parallel gripper or a dexterous hand [9, 49], limiting the types of ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our simulated humanoid benchmark demonstrates a variety of challenges in addressing learning for autonomous humanoid robots, such as the intricate control of robots with, complex ...
- **p. 3 / I. INTRODUCTION - extractive body cue:** Although other sensory inputs are available from the environment, to investigate challenges in whole-body control of humanoid robots, we first focus on the state-based environment ...
- **p. 4 / I. INTRODUCTION - extractive body cue:** We devise 15 benchmarking whole-body manipulation tasks that cover a wide variety of interactions and difficulties.
- **p. 9 / B. Results - extractive body cue:** In this subsection, we remark on notable challenges and com- ‘mon failures for some representative tasks in our benchmark, which denote the challenge in learning ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 10: Failure Scenarios. This figure presents a selection of common failures that occur while training our benchmark tasks.
- **Boundary to test:** In this subsection, we remark on notable challenges and com- ‘mon failures for some representative tasks in our benchmark, which denote the challenge in learning with high-dimensional action spaces and limited planning ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To accelerate the progress of research for humanoid robots, We present the first-of-its-kind humanoid robot benchmark, HumanoidBench, with a diverse set of locomotion and manipulation tasks. | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Reported outcome | In Figure 9, our hierarchical architecture significantly outperforms the flat, end-to-end baselines on the push task, achieving very high success rates ‘with DreamerV3. | p. 9 (B. Results), p. 9 (B. Results) |
| Failure/limitation | In this subsection, we remark on notable challenges and com- ‘mon failures for some representative tasks in our benchmark, which denote the challenge in learning with high-dimensional action spaces and limited planning ... | p. 9 (B. Results), p. 10 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `standardized observation, action, task state와 evaluation split → benchmark state/goal와 method decision → policy/controller trajectory 또는 measured result`.
- 이 논문의 재사용 가능한 지점은 + Proprioceptive robot state (i, joint angles and velocities) and task-relevant environment observations (ie, object, poses and velocities)를 Although other sensory inputs are available from the environment, to investigate challenges in whole-body control of humanoid robots, we first focus on the state-based environment setup, where proprioceptive robot states and object ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 benchmark state/goal와 method decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 In this subsection, we remark on notable challenges and com- ‘mon failures for some representative tasks in our benchmark, which denote the challenge in learning with high-dimensional action spaces and limited planning ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To accelerate the progress of research for humanoid robots, We present the first-of-its-kind humanoid robot benchmark, HumanoidBench, with a diverse set of locomotion and manipulation tasks.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, humanoid, Benchmark, whole-body control, loco-manipulation`.
- **Reading predecessor in the generated track queue:** ANYmal Parkour: Learning Agile Navigation for Quadrupedal Robots (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In this subsection, we remark on notable challenges and com- ‘mon failures for some representative tasks in our benchmark, which denote the challenge in learning with high-dimensional action spaces and limited planning ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: To identify the challenges in learning with humanoid robots, we benchmark reinforcement learning (RL) algorithms on HumanoidBench, which promises for robots to learn from.
3. Compare against the body-reported baseline or a matched simpler baseline: In Figure 9, our hierarchical architecture significantly outperforms the flat, end-to-end baselines on the push task, achieving very high success rates ‘with DreamerV3..
4. Report the body metric and its denominator/aggregation: We only run PPO on a subset of tasks (walk, kitchen, door, package), given its inferior performance without massive parallelization, Each of the environments is evaluated with a combination of dense rewards ....
5. Re-run the body-reported ablation/failure condition: 7: Performance with and without dexterous hands..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 1 (I. INTRODUCTION), p. 1 (Abstract), p. 2 (I. INTRODUCTION); the primary result is directionally consistent at p. 9 (B. Results), p. 9 (B. Results), p. 8 (B. Results); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 accelerate, progress, research mechanism이 In Figure 9, our hierarchical architecture significantly outperforms the flat, end-to-end baselines on the push task, ... 대비 We only run PPO on a subset of tasks (walk, kitchen, door, package), given its inferior performance without ...을 개선하고, In this subsection, we remark on notable challenges and com- ‘mon failures for some representative tasks ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
