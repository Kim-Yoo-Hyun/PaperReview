# Evaluation - CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2112.03227; PDF retrieval source: https://arxiv.org/pdf/2112.03227. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), p. 3 (Figure/Table caption), p. 5 (Figure/Table caption)): We observe that the baseline with images of the static camera achieves a success rate of 53.9% for the MTLC evaluation setting, when training and testing the 34 manipulation tasks ...

## Evaluation Body Digest

- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** MEES et al.: CALVIN: A BENCHMARK FOR LANGUAGE-CONDITIONED POLICY LEARNING FOR LONG-HORIZON ROBOT MANIPULATION TASKS 7 Input Train →Test MTLC LH-MTLC Static Camera Gripper Camera ...
- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** A qualitative analysis indicates that the performance depends significantly on the initial position of the robot, suggesting the agent relies on context rather than learning ...
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** We observe that the baseline with images of the static camera achieves a success rate of 53.9% for the MTLC evaluation setting, when training and ...
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** We note that there is no constraint to use imitation learning approaches to solve CALVIN tasks, as approaches that use reinforcement learning to learn language-conditioned ...
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** The success rate stays comparable when including a gripper camera, depth channels or tactile sensing.
- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** The best MCIL model achieves a success rate of 0.08% when following chains of five language instructions in a row when training and testing on ...
- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** 8: Baseline performance of MCIL [6] on the CALVIN Challenge for different combinations of training and test environments and sensor suites. global actions.
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 6: List of all 34 tasks with their respective success criteria. initial state and task, forcing the agent to rely entirely on language to ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** 2) CALVIN Dataset (p. 3); V. EXPERIMENTAL RESULTS (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| V. EXPERIMENTAL RESULTS | BENCHMARK / DATASET | We observe that the baseline with images of the static camera achieves a success rate of 53.9% for the MTLC evaluation setting, when training ... | p. 6 (V. EXPERIMENTAL RESULTS) |
| V. EXPERIMENTAL RESULTS | BENCHMARK / DATASET | The best MCIL model achieves a success rate of 0.08% when following chains of five language instructions in a row when training and testing ... | p. 7 (V. EXPERIMENTAL RESULTS) |
| V. EXPERIMENTAL RESULTS | BENCHMARK / DATASET | The success rate stays comparable when including a gripper camera, depth channels or tactile sensing. | p. 6 (V. EXPERIMENTAL RESULTS) |
| V. EXPERIMENTAL RESULTS | BENCHMARK / DATASET | A qualitative analysis indicates that the performance depends significantly on the initial position of the robot, suggesting the agent relies on context rather than ... | p. 7 (V. EXPERIMENTAL RESULTS) |
| Figure/Table caption | BENCHMARK / DATASET | Fig. 2: Observation and action spaces supported by CALVIN. only allow feasible sequences that can be achieved from a predefined initial environment state. The ... | p. 3 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** MEES et al.: CALVIN: A BENCHMARK FOR LANGUAGE-CONDITIONED POLICY LEARNING FOR LONG-HORIZON ROBOT MANIPULATION TASKS 7 Input Train →Test MTLC LH-MTLC Static Camera Gripper Camera ...
- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** A qualitative analysis indicates that the performance depends significantly on the initial position of the robot, suggesting the agent relies on context rather than learning ...
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** We observe that the baseline with images of the static camera achieves a success rate of 53.9% for the MTLC evaluation setting, when training and ...
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** We note that there is no constraint to use imitation learning approaches to solve CALVIN tasks, as approaches that use reinforcement learning to learn language-conditioned ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: CALVIN is a benchmark to learn many long-horizon language-conditioned tasks over a range of four manipulation environments, designed to be diverse yet carry ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: Observation and action spaces supported by CALVIN. only allow feasible sequences that can be achieved from a predefined initial environment state. The CALVIN ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 3: CALVIN supports a range of sensors commonly utilized for visuomotor control: RGB-D images from both a static and a gripper camera, proprioceptive information, ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4: Example crowd-sourced natural language instructions to specify manipulation tasks in CALVIN. data in four environments with a HTC Vive VR headset, spending an ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 5: Example long-horizon language tasks sequences evaluated in CALVIN. We show the abbreviated subtask names instead of the full language annotations due to space ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 6: List of all 34 tasks with their respective success criteria. initial state and task, forcing the agent to rely entirely on language to ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 7: Visualization of the subtask distribution across the 1000 instruction chains used for the Long Horizon MTLC evaluation. We show the percentage in which ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 8: Baseline performance of MCIL [6] on the CALVIN Challenge for different combinations of training and test environments and sensor suites. global actions. A ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | MEES et al.: CALVIN: A BENCHMARK FOR LANGUAGE-CONDITIONED POLICY LEARNING FOR LONG-HORIZON ROBOT MANIPULATION TASKS 7 Input Train →Test MTLC LH-MTLC Static Camera Gripper ... | embodiment, simulator version and control stack | p. 7 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS) |
| Task/environment | A qualitative analysis indicates that the performance depends significantly on the initial position of the robot, suggesting the agent relies on context rather than ... | reset, timeout, object/scene variation | p. 7 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 6 (IV. BASELINE MODELS), p. 3 (III. CALVIN) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 3 (3) CALVIN Challenge), p. 6 (IV. BASELINE MODELS) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The success rate stays comparable when including a gripper camera, depth channels or tactile sensing. | definition/direction/unit from same section | p. 6 (V. EXPERIMENTAL RESULTS) |
| We observe that the baseline with images of the static camera achieves a success rate of 53.9% for the MTLC evaluation setting, when training ... | definition/direction/unit from same section | p. 6 (V. EXPERIMENTAL RESULTS) |
| The best MCIL model achieves a success rate of 0.08% when following chains of five language instructions in a row when training and testing ... | definition/direction/unit from same section | p. 7 (V. EXPERIMENTAL RESULTS) |
| 8: Baseline performance of MCIL [6] on the CALVIN Challenge for different combinations of training and test environments and sensor suites. global actions. | definition/direction/unit from same section | p. 7 (V. EXPERIMENTAL RESULTS) |
| Fig. 6: List of all 34 tasks with their respective success criteria. initial state and task, forcing the agent to rely entirely on language ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We observe that the baseline with images of the static camera achieves a success rate of 53.9% for the MTLC evaluation setting, when training ... | comparison identity and matched condition | p. 6 (V. EXPERIMENTAL RESULTS) |
| 8: Baseline performance of MCIL [6] on the CALVIN Challenge for different combinations of training and test environments and sensor suites. global actions. | comparison identity and matched condition | p. 7 (V. EXPERIMENTAL RESULTS) |
| Besides, we did not use image data augmentations in the baselines to stay close to the original implementation, but we hypothesize this might be ... | comparison identity and matched condition | p. 7 (V. EXPERIMENTAL RESULTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Additionally, more elaborate sensor fusion approaches such as mixture of experts [33], [34] or view-invariant contrastive learning [35], [36] might be necessary to learn ... | component/input/data sensitivity | p. 7 (V. EXPERIMENTAL RESULTS) |
| In order to achieve better zero-shot generalization capabilities, additional techniques from the domain adaptation literature [36], better data augmentation and a stronger focus on ... | component/input/data sensitivity | p. 7 (V. EXPERIMENTAL RESULTS) |
| Fig. 2: Observation and action spaces supported by CALVIN. only allow feasible sequences that can be achieved from a predefined initial environment state. The ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we present CALVIN (Composing Actions from Language and Vision), an open-source simulated benchmark to learn longhorizon language-conditioned tasks. | We observe that the baseline with images of the static camera achieves a success rate of 53.9% for the MTLC evaluation setting, when training ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), p. 3 (Figure/Table caption), p. 5 (Figure/Table caption) |
| Primary metric/result | The best MCIL model achieves a success rate of 0.08% when following chains of five language instructions in a row when training and testing ... | numeric claim only at cited anchor | p. 7 (V. EXPERIMENTAL RESULTS) |

- Numeric sentences retained from the body:
- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** MEES et al.: CALVIN: A BENCHMARK FOR LANGUAGE-CONDITIONED POLICY LEARNING FOR LONG-HORIZON ROBOT MANIPULATION TASKS 7 Input Train →Test MTLC LH-MTLC Static Camera Gripper Camera ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| no explicit failure cue selected | unreported; domain stress test remains open | verify Discussion/Conclusion |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Besides, we did not use image data augmentations in the baselines to stay close to the original implementation, but we hypothesize this might be ... | p. 7 (V. EXPERIMENTAL RESULTS) |
| We train the agent with the Adam optimizer and a learning rate of 10-4. | p. 6 (IV. BASELINE MODELS) |
| We note that the same training hyperparameters are used for all splits. | p. 6 (IV. BASELINE MODELS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- explicit limitation/failure sentence not stated or recoverable in the selected PDF body

- **Evidence anchors reviewed:** datasets p. 7 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), metrics p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), p. 5 (Figure/Table caption), baselines p. 6 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), results p. 6 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), p. 3 (Figure/Table caption), p. 5 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (10 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** We observe that the baseline with images of the static camera achieves a success rate of 53.9% for the MTLC evaluation setting, when training and testing the 34 manipulation tasks ... (p. 6, V. EXPERIMENTAL RESULTS).
- **Metric evidence:** We observe that the baseline with images of the static camera achieves a success rate of 53.9% for the MTLC evaluation setting, when training and testing the 34 manipulation tasks ... (p. 6, V. EXPERIMENTAL RESULTS).
- **Baseline/ablation evidence:** We observe that the baseline with images of the static camera achieves a success rate of 53.9% for the MTLC evaluation setting, when training and testing the 34 manipulation tasks ... (p. 6, V. EXPERIMENTAL RESULTS).
- **Failure/negative evidence:** For the Long-Horizon MTLC evaluation we observe that the agents perform poorly on CALVIN's long-horizon tasks with high-dimensional state spaces. (p. 7, V. EXPERIMENTAL RESULTS).
