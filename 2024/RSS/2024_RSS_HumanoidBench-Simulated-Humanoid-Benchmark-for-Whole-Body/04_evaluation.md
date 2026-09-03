# Evaluation - HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p061.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p061.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (B. Results), p. 9 (B. Results), p. 8 (B. Results), p. 8 (B. Results), p. 7 (Figure/Table caption)): In Figure 9, our hierarchical architecture significantly outperforms the flat, end-to-end baselines on the push task, achieving very high success rates ‘with DreamerV3.

## Evaluation Body Digest

- **p. 7 / V. BENCHMARKING RESULTS - extractive body cue:** To identify the challenges in learning with humanoid robots, we benchmark reinforcement learning (RL) algorithms on HumanoidBench, which promises for robots to learn from
- **p. 8 / B. Results - extractive body cue:** To verify whether such difficulties stem from the dimensionality of the action space, we benchmark our full robot model, but fix the actuation of the ...
- **p. 7 / V. BENCHMARKING RESULTS - extractive body cue:** Remarkably, this class of algorithms requires limited domain expertise and does not necessarily rely fon expert demonstrations, which are not only expensive but also challenging ...
- **p. 9 / B. Results - extractive body cue:** For low-level reaching policy training, we employ a simplified Hi model that only considers collisions between feet and ground in the MuJoCo MIX environments, as ...
- **p. 8 / B. Results - extractive body cue:** Although the hands of the ‘humanoid robot are barely used for most locomotion tasks, the RL algorithms fail to ignore this information, which makes policy ...
- **p. 9 / B. Results - extractive body cue:** In the highbay task, the Unitree HI robot conservatively learns to maintain contact,
- **p. 8 / B. Results - extractive body cue:** We only run PPO on a subset of tasks (walk, kitchen, door, package), given its inferior performance without massive parallelization, Each of the environments is ...
- **p. 9 / B. Results - extractive body cue:** In Figure 9, our hierarchical architecture significantly outperforms the flat, end-to-end baselines on the push task, achieving very high success rates ‘with DreamerV3.

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** V. BENCHMARKING RESULTS (p. 7); B. Results (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| B. Results | BENCHMARK / DATASET | In Figure 9, our hierarchical architecture significantly outperforms the flat, end-to-end baselines on the push task, achieving very high success rates ‘with DreamerV3. | p. 9 (B. Results) |
| B. Results | BENCHMARK / DATASET | On the other hand, we note a less pronounced performance improvement in the more challenging package task. | p. 9 (B. Results) |
| B. Results | BENCHMARK / DATASET | The results in Figure 7 show that the presence of hands, with their additional joints and actuators, leads to a large decrease in performance ... | p. 8 (B. Results) |
| B. Results | BENCHMARK / DATASET | We only run PPO on a subset of tasks (walk, kitchen, door, package), given its inferior performance without massive parallelization, Each of the environments ... | p. 8 (B. Results) |
| Figure/Table caption | BENCHMARK / DATASET | Fig. 6: Learning curves of RL algorithms (manipulation). The curves are averaged over three random seeds and the shaded regions represent the standard deviation. ... | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / V. BENCHMARKING RESULTS - extractive body cue:** To identify the challenges in learning with humanoid robots, we benchmark reinforcement learning (RL) algorithms on HumanoidBench, which promises for robots to learn from
- **p. 8 / B. Results - extractive body cue:** To verify whether such difficulties stem from the dimensionality of the action space, we benchmark our full robot model, but fix the actuation of the ...
- **p. 7 / V. BENCHMARKING RESULTS - extractive body cue:** Remarkably, this class of algorithms requires limited domain expertise and does not necessarily rely fon expert demonstrations, which are not only expensive but also challenging ...
- **p. 9 / B. Results - extractive body cue:** For low-level reaching policy training, we employ a simplified Hi model that only considers collisions between feet and ground in the MuJoCo MIX environments, as ...
- **p. 8 / B. Results - extractive body cue:** Although the hands of the ‘humanoid robot are barely used for most locomotion tasks, the RL algorithms fail to ignore this information, which makes policy ...
- **p. 9 / B. Results - extractive body cue:** In the highbay task, the Unitree HI robot conservatively learns to maintain contact,

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: Example egocentric visual (top-left) and whole-body tactile (right) observations when the humanoid interacts with, a package in the truck environment. In the right ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: HumanoidBench manipulation task suite. We devise 15 benchmarking whole-body manipulation tasks that cover a wide variety of interactions and difficulties. This figure illustrates ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: HumanoidBench locomotion task
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Learning curves of RL algorithms (locomotion). The curves are averaged over three random seeds and the shaded
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: Learning curves of RL algorithms (manipulation). The curves are averaged over three random seeds and the shaded regions represent the standard deviation. The ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7: Performance with and without dexterous hands. The curves are averaged over three random seeds and the shaded regions represent the standard deviation.
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 8: Our hierarchical RL pipeline (a). (b) A robust low-level reaching policy is pretrained using PPO in a MuJoCo ‘MJX-based reaching environment, as shown ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 9: Comparison between flat policies and hierarchical policies. The curves are averaged over three random seeds and the shaded regions represent the standard deviation.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To identify the challenges in learning with humanoid robots, we benchmark reinforcement learning (RL) algorithms on HumanoidBench, which promises for robots to learn from | embodiment, simulator version and control stack | p. 7 (V. BENCHMARKING RESULTS), p. 8 (B. Results) |
| Task/environment | To verify whether such difficulties stem from the dimensionality of the action space, we benchmark our full robot model, but fix the actuation of ... | reset, timeout, object/scene variation | p. 8 (B. Results), p. 7 (V. BENCHMARKING RESULTS) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 3 (I. INTRODUCTION), p. 3 (I. INTRODUCTION) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 1 (I. INTRODUCTION), p. 1 (Abstract) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We only run PPO on a subset of tasks (walk, kitchen, door, package), given its inferior performance without massive parallelization, Each of the environments ... | definition/direction/unit from same section | p. 8 (B. Results) |
| In Figure 9, our hierarchical architecture significantly outperforms the flat, end-to-end baselines on the push task, achieving very high success rates ‘with DreamerV3. | definition/direction/unit from same section | p. 9 (B. Results) |
| Fig. 6: Learning curves of RL algorithms (manipulation). The curves are averaged over three random seeds and the shaded regions represent the standard deviation. ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| A detailed description of the reward functions used for each environment is available in Appendix, Section B. | definition/direction/unit from same section | p. 8 (B. Results) |
| On the other hand, we note a less pronounced performance improvement in the more challenging package task. | definition/direction/unit from same section | p. 9 (B. Results) |
| Fig. 3: HumanoidBench manipulation task suite. We devise 15 benchmarking whole-body manipulation tasks that cover a wide variety of interactions and difficulties. This figure ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In Figure 9, our hierarchical architecture significantly outperforms the flat, end-to-end baselines on the push task, achieving very high success rates ‘with DreamerV3. | comparison identity and matched condition | p. 9 (B. Results) |
| The results in Figure 7 show that the presence of hands, with their additional joints and actuators, leads to a large decrease in performance ... | comparison identity and matched condition | p. 8 (B. Results) |
| All the baseline algorithms perform below the success threshold on most tasks, particularly struggling on tasks that require long-horizon planning and intricate whole-body coordination ... | comparison identity and matched condition | p. 8 (B. Results) |
| Ona separate note, while our experiments above confirm that the on-policy PPO exhibits poor sample efficiency compared to the other off-policy algorithms, it is ... | comparison identity and matched condition | p. 9 (B. Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 7: Performance with and without dexterous hands. | component/input/data sensitivity | p. 8 (B. Results) |
| We observe similar trends in the more complex manipulation task, push, wihch presents substantially different dynamics in the task approach (e.g., pushing with and ... | component/input/data sensitivity | p. 8 (B. Results) |
| We also remove the hands from the model to further increase training efficiency. | component/input/data sensitivity | p. 9 (B. Results) |
| Low-level Reaching Policy Pretraining. | component/input/data sensitivity | p. 9 (B. Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To accelerate the progress of research for humanoid robots, We present the first-of-its-kind humanoid robot benchmark, HumanoidBench, with a diverse set of locomotion and ... | In Figure 9, our hierarchical architecture significantly outperforms the flat, end-to-end baselines on the push task, achieving very high success rates ‘with DreamerV3. | PDF body cue; verify exact table/figure and matched conditions | p. 9 (B. Results), p. 9 (B. Results), p. 8 (B. Results), p. 8 (B. Results), p. 7 (Figure/Table caption) |
| Primary metric/result | On the other hand, we note a less pronounced performance improvement in the more challenging package task. | numeric claim only at cited anchor | p. 9 (B. Results) |

- Numeric sentences retained from the body:
- **p. 8 / B. Results - extractive body cue:** We report benchmarking results in Figure 5 and Figure 6, where we ran each of the algorithms for approximately 48 hours, resulting in the visible ...
- **p. 8 / B. Results - extractive body cue:** training with a lange action space (ie., additional 42 dimensions with two dexterous Shadow Hands) on walk that does not necessarily require to control dexterous ...
- **p. 9 / B. Results - extractive body cue:** We train the cone-hand reaching policy for 2 billion steps (36 hours) and the two:hand reaching policy for 4 billion steps (60 hours) on 82, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our simulated humanoid benchmark demonstrates a variety of challenges in addressing learning for autonomous humanoid robots, such as the intricate control of robots with, complex ...
- **p. 4 / I. INTRODUCTION - extractive body cue:** For both position and torque control, the action space is 6-dimensional including the two hands, and controlled at 50 Hz.
- **p. 5 / IV. HuMANOIDBENcH - extractive body cue:** We benchmark 27 tasks, consisting of 12 locomotion tasks and 15 distinct manipulation tasks, as illustrated in Figure 4 and Figure 3.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In this subsection, we remark on notable challenges and com- ‘mon failures for some representative tasks in our benchmark, which denote the challenge in ... | p. 9 (B. Results) |
| body limitation/failure cue | Fig. 10: Failure Scenarios. This figure presents a selection of common failures that occur while training our benchmark tasks. | p. 10 (Figure/Table caption) |
| body limitation/failure cue | For low-level reaching policy training, we employ a simplified Hi model that only considers collisions between feet and ground in the MuJoCo MIX environments, ... | p. 9 (B. Results) |
| body limitation/failure cue | Remarkably, this class of algorithms requires limited domain expertise and does not necessarily rely fon expert demonstrations, which are not only expensive but also ... | p. 7 (V. BENCHMARKING RESULTS) |
| body limitation/failure cue | training with a lange action space (ie., additional 42 dimensions with two dexterous Shadow Hands) on walk that does not necessarily require to control ... | p. 8 (B. Results) |
| body limitation/failure cue | Although the hands of the ‘humanoid robot are barely used for most locomotion tasks, the RL algorithms fail to ignore this information, which makes ... | p. 8 (B. Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| mns represent the standard deviation, Returns are computed by summing the rewards at all timesteps of an episode. | p. 6 (IV. HuMANOIDBENcH) |
| The open-source code is available at ‘hupst//humanold-bench.github.io. | p. 1 (Abstract) |
| However, research in humanoid robots is often bottlenecked by the costly and fragile hardware setups. | p. 1 (Abstract) |
| This motivates us to implement a comprehensive simulated humanoid benchmark based on real-world hardware and consisting of a diverse set of whole-body control tasks ... | p. 2 (I. INTRODUCTION) |
| The implementation of such spatially distributed contact sensing required non-trivial mesh adaptations and refinements, which we detail in the appendix. | p. 3 (I. INTRODUCTION) |
| However, their form factor and hardware challenges make real-world research challenging, making simulation a crucial tool to advance algorithmic research in the field | p. 4 (IV. HuMANOIDBENcH) |
| + run: Run forward (in the global x-direction) at a speed of 5m/s. | p. 5 (IV. HuMANOIDBENcH) |
| The curves are averaged over three random seeds and the shaded | p. 6 (IV. HuMANOIDBENcH) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / B. Results - extractive body cue:** In this subsection, we remark on notable challenges and com- ‘mon failures for some representative tasks in our benchmark, which denote the challenge in learning ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 10: Failure Scenarios. This figure presents a selection of common failures that occur while training our benchmark tasks.
- **p. 9 / B. Results - extractive body cue:** For low-level reaching policy training, we employ a simplified Hi model that only considers collisions between feet and ground in the MuJoCo MIX environments, as ...
- **p. 7 / V. BENCHMARKING RESULTS - extractive body cue:** Remarkably, this class of algorithms requires limited domain expertise and does not necessarily rely fon expert demonstrations, which are not only expensive but also challenging ...
- **p. 8 / B. Results - extractive body cue:** training with a lange action space (ie., additional 42 dimensions with two dexterous Shadow Hands) on walk that does not necessarily require to control dexterous ...
- **p. 8 / B. Results - extractive body cue:** Although the hands of the ‘humanoid robot are barely used for most locomotion tasks, the RL algorithms fail to ignore this information, which makes policy ...

- **Evidence anchors reviewed:** datasets p. 7 (V. BENCHMARKING RESULTS), p. 8 (B. Results), p. 7 (V. BENCHMARKING RESULTS), p. 9 (B. Results), p. 8 (B. Results), p. 9 (B. Results), metrics p. 8 (B. Results), p. 9 (B. Results), p. 7 (Figure/Table caption), p. 8 (B. Results), p. 9 (B. Results), p. 4 (Figure/Table caption), baselines p. 9 (B. Results), p. 8 (B. Results), p. 8 (B. Results), p. 9 (B. Results), results p. 9 (B. Results), p. 9 (B. Results), p. 8 (B. Results), p. 8 (B. Results), p. 7 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (1 pages; pdftotext fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** The results in combination of dense rewards and sparse subtask completion Figure 7 show that the presence of hands, with their additional rewards, and for each of these we provide ... (p. 1, V. B ENCHMARKING R ESULTS).
- **Metric evidence:** The results in combination of dense rewards and sparse subtask completion Figure 7 show that the presence of hands, with their additional rewards, and for each of these we provide ... (p. 1, V. B ENCHMARKING R ESULTS).
- **Baseline/ablation evidence:** In Figure 9, our hierarchical MJX8 , which enables training PPO on thousands of parallel architecture significantly outperforms the flat, end-to-end environments. baselines on the push task, achieving very high ... (p. 1, V. B ENCHMARKING R ESULTS).
- **Failure/negative evidence:** Mobility Fellowship 211086, ONR MURI N00014-22-1-2773, Common Failure on door. (p. 1, V. B ENCHMARKING R ESULTS).
