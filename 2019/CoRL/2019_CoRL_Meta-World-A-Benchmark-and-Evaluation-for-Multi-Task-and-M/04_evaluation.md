# Evaluation - Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v100/yu20a.html; PDF retrieval source: https://proceedings.mlr.press/v100/yu20a.html. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 1 (1 Introduction), p. 13 (Figure/Table caption), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract)): Figure 5: Quantitative results on MT10, MT50, ML10, and ML45. Note that, even on the challenging ML10 and ML45 benchmarks, current methods already exhibit some degree of generalization, but meta-training ...

## Evaluation Body Digest

- **p. 1 / Abstract - extractive PDF cue:** For example, a commonly used meta-reinforcement learning benchmark uses different running velocities for a simulated robot as different tasks.
- **p. 1 / Abstract - extractive PDF cue:** In this paper, we propose an open-source simulated benchmark for meta-reinforcement learning and multitask learning consisting of 50 distinct robotic manipulation tasks.
- **p. 2 / 1 Introduction - extractive PDF cue:** To this end, we present a benchmark of simulated manipulation tasks with everyday objects, all of which are contained in a shared, table-top environment with ...
- **p. 2 / 1 Introduction - extractive PDF cue:** By providing a large set of distinct tasks that share common environment and control structure, we believe that this benchmark will allow researchers to test ...
- **p. 13 / Figure/Table caption - extractive PDF cue:** Figure 8: Learning curves of all methods on MT10, ML10, MT50, and ML45 benchmarks. Y- axis represents success rate averaged over tasks in percentage (%). ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5: Quantitative results on MT10, MT50, ML10, and ML45. Note that, even on the challenging ML10 and ML45 benchmarks, current methods already exhibit some ...
- **p. 11 / Figure/Table caption - extractive PDF cue:** Table 1: A list of all of the Meta-World tasks and a description of each task. B Task Rewards and Success Metrics The form of ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Figure 6: Performance of independent policies trained on individual tasks using soft actor-critic (SAC) and proximal policy optimization (PPO). We verify that SAC can solve ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** C Benchmark Verification with Single-Task Learning (p. 12).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | BENCHMARK / DATASET | Figure 5: Quantitative results on MT10, MT50, ML10, and ML45. Note that, even on the challenging ML10 and ML45 benchmarks, current methods already exhibit ... | p. 8 (Figure/Table caption) |
| 1 Introduction | BENCHMARK / DATASET | While reinforcement learning (RL) has achieved some success in domains such as assembly [1], ping pong [2], in-hand manipulation [3], and hockey [4], state-of-the-art ... | p. 1 (1 Introduction) |
| Figure/Table caption | BENCHMARK / DATASET | Figure 8: Learning curves of all methods on MT10, ML10, MT50, and ML45 benchmarks. Y- axis represents success rate averaged over tasks in percentage ... | p. 13 (Figure/Table caption) |
| 1 Introduction | BENCHMARK / DATASET | By doing so, we can enable meaningful generalization across many tasks and achieve the full potential of meta-learning as a means of incorporating past ... | p. 2 (1 Introduction) |
| 1 Introduction | BENCHMARK / DATASET | By providing a large set of distinct tasks that share common environment and control structure, we believe that this benchmark will allow researchers to ... | p. 2 (1 Introduction) |

## Dataset / Benchmark Role

- **p. 1 / Abstract - extractive PDF cue:** For example, a commonly used meta-reinforcement learning benchmark uses different running velocities for a simulated robot as different tasks.
- **p. 1 / Abstract - extractive PDF cue:** In this paper, we propose an open-source simulated benchmark for meta-reinforcement learning and multitask learning consisting of 50 distinct robotic manipulation tasks.
- **p. 2 / 1 Introduction - extractive PDF cue:** To this end, we present a benchmark of simulated manipulation tasks with everyday objects, all of which are contained in a shared, table-top environment with ...
- **p. 2 / 1 Introduction - extractive PDF cue:** By providing a large set of distinct tasks that share common environment and control structure, we believe that this benchmark will allow researchers to test ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Meta-World contains 50 manipulation tasks, designed to be diverse yet carry shared structure that can be leveraged for efficient multi-task RL and transfer ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. Introducing this parametric variability not only creates a substantially larger (infinite) variety of tasks, but also makes it substantially more practical to expect ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: Visualization of three of our multi-task and meta-learning evaluation protocols, ranging from within task adaptation in ML1, to multi-task training across 10 distinct ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4: Comparison on our simplest meta-RL evaluation, ML1. We show results of the simplest meta-learning evaluation mode, ML1, in Figure 7. We find that ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5: Quantitative results on MT10, MT50, ML10, and ML45. Note that, even on the challenging ML10 and ML45 benchmarks, current methods already exhibit some ...
- **p. 11 / Figure/Table caption - extractive PDF cue:** Table 1: A list of all of the Meta-World tasks and a description of each task. B Task Rewards and Success Metrics The form of ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Figure 6: Performance of independent policies trained on individual tasks using soft actor-critic (SAC) and proximal policy optimization (PPO). We verify that SAC can solve ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Figure 6. We indeed find that SAC can learn to perform all of the 50 tasks to some degree, while PPO can solve a large ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For example, a commonly used meta-reinforcement learning benchmark uses different running velocities for a simulated robot as different tasks. | embodiment, simulator version and control stack | p. 1 (Abstract), p. 1 (Abstract) |
| Task/environment | In this paper, we propose an open-source simulated benchmark for meta-reinforcement learning and multitask learning consisting of 50 distinct robotic manipulation tasks. | reset, timeout, object/scene variation | p. 1 (Abstract), p. 2 (1 Introduction) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 1 (Abstract), p. 1 (1 Introduction) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 2 (1 Introduction), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 8: Learning curves of all methods on MT10, ML10, MT50, and ML45 benchmarks. Y- axis represents success rate averaged over tasks in percentage ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |
| Figure 5: Quantitative results on MT10, MT50, ML10, and ML45. Note that, even on the challenging ML10 and ML45 benchmarks, current methods already exhibit ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Table 1: A list of all of the Meta-World tasks and a description of each task. B Task Rewards and Success Metrics The form ... | definition/direction/unit from same section | p. 11 (Figure/Table caption) |
| Figure 6: Performance of independent policies trained on individual tasks using soft actor-critic (SAC) and proximal policy optimization (PPO). We verify that SAC can ... | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| Our aim is to make it possible to develop algorithms that generalize to accelerate the acquisition of entirely new, held-out tasks. | definition/direction/unit from same section | p. 1 (Abstract) |
| Surprisingly, while each task and its variations (e.g., with different object positions) can be learned with reasonable success, these algorithms struggle to learn with ... | definition/direction/unit from same section | p. 1 (Abstract) |
| We provide an evaluation protocol with evaluation modes of varying difficulty, and observe that current methods only show success in the easiest modes. | definition/direction/unit from same section | p. 2 (1 Introduction) |
| Our empirical evaluation of existing methods on this benchmark reveals that, despite some impressive progress in multi-task and meta-reinforcement learning over the past few ... | definition/direction/unit from same section | p. 2 (1 Introduction) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We evaluate 6 state-of-the-art meta-reinforcement learning and multi-task learning algorithms on these tasks. | comparison identity and matched condition | p. 1 (Abstract) |
| While reinforcement learning (RL) has achieved some success in domains such as assembly [1], ping pong [2], in-hand manipulation [3], and hockey [4], state-of-the-art ... | comparison identity and matched condition | p. 1 (1 Introduction) |
| Figure 2. Introducing this parametric variability not only creates a substantially larger (infinite) variety of tasks, but also makes it substantially more practical to ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |
| Figure 4: Comparison on our simplest meta-RL evaluation, ML1. We show results of the simplest meta-learning evaluation mode, ML1, in Figure 7. We find ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Figure 7: Comparison of PEARL, MAML, and RL2 learning curves on the simplest evaluation, ML1, where the methods need to adapt quickly to new ... | comparison identity and matched condition | p. 13 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 2. Introducing this parametric variability not only creates a substantially larger (infinite) variety of tasks, but also makes it substantially more practical to ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| Table 1: A list of all of the Meta-World tasks and a description of each task. B Task Rewards and Success Metrics The form ... | component/input/data sensitivity | p. 11 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To this end, we present a benchmark of simulated manipulation tasks with everyday objects, all of which are contained in a shared, table-top environment ... | Figure 5: Quantitative results on MT10, MT50, ML10, and ML45. Note that, even on the challenging ML10 and ML45 benchmarks, current methods already exhibit ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 1 (1 Introduction), p. 13 (Figure/Table caption), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract) |
| Primary metric/result | While reinforcement learning (RL) has achieved some success in domains such as assembly [1], ping pong [2], in-hand manipulation [3], and hockey [4], state-of-the-art ... | numeric claim only at cited anchor | p. 1 (1 Introduction) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 5: Quantitative results on MT10, MT50, ML10, and ML45. Note that, even on the challenging ML10 and ML45 benchmarks, current methods already exhibit ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | When policies are meta-trained on such narrow task distributions, they cannot possibly generalize to more quickly acquire entirely new tasks. | p. 1 (Abstract) |
| body limitation/failure cue | Our experiments show that current meta-RL methods in fact cannot yet generalize effectively to entirely new tasks and do not even learn the meta-training ... | p. 7 (2 Related Work) |
| body limitation/failure cue | This opens the door for future developments in multi-task and meta reinforcement learning: instead of focusing on further increasing performance on current narrow task ... | p. 2 (1 Introduction) |
| body limitation/failure cue | This suggests a number of directions for future work, which we describe below. | p. 7 (2 Related Work) |
| body limitation/failure cue | We leave these directions for future work, either to be done by ourselves or in the form of open-source contributions. | p. 8 (2 Related Work) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| no implementation/reproducibility sentence selected | verify appendix and code/project |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5: Quantitative results on MT10, MT50, ML10, and ML45. Note that, even on the challenging ML10 and ML45 benchmarks, current methods already exhibit some ...
- **p. 1 / Abstract - extractive PDF cue:** When policies are meta-trained on such narrow task distributions, they cannot possibly generalize to more quickly acquire entirely new tasks.
- **p. 7 / 2 Related Work - extractive PDF cue:** Our experiments show that current meta-RL methods in fact cannot yet generalize effectively to entirely new tasks and do not even learn the meta-training tasks ...
- **p. 2 / 1 Introduction - extractive PDF cue:** This opens the door for future developments in multi-task and meta reinforcement learning: instead of focusing on further increasing performance on current narrow task suites, ...
- **p. 7 / 2 Related Work - extractive PDF cue:** This suggests a number of directions for future work, which we describe below.
- **p. 8 / 2 Related Work - extractive PDF cue:** We leave these directions for future work, either to be done by ourselves or in the form of open-source contributions.

- **PDF anchors reviewed:** datasets p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction), metrics p. 13 (Figure/Table caption), p. 8 (Figure/Table caption), p. 11 (Figure/Table caption), p. 12 (Figure/Table caption), p. 1 (Abstract), p. 1 (Abstract), baselines p. 1 (Abstract), p. 1 (1 Introduction), p. 4 (Figure/Table caption), p. 7 (Figure/Table caption), p. 13 (Figure/Table caption), results p. 8 (Figure/Table caption), p. 1 (1 Introduction), p. 13 (Figure/Table caption), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
