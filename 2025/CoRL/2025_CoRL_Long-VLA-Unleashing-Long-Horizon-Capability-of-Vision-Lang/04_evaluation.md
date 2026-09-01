# Evaluation - Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v305/fan25a.html; PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v305/main/assets/fan25a/fan25a.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4 Experiment), p. 6 (4 Experiment), p. 7 (4 Experiment), p. 8 (4 Experiment), p. 7 (4 Experiment), p. 8 (4 Experiment)): As shown in Figure 4, our model achieves performance improvements in the D→D and ABCD→D of the L-CALVIN benchmark.

## Evaluation Body Digest

- **p. 7 / 4 Experiment - extractive body cue:** In real-world robotic experiments, our method consistently outperforms the state-of-the-art algorithm π0 across the generalization task.
- **p. 6 / 4 Experiment - extractive body cue:** Lift the C cube Put in the bowl Lift the O cube Put in the bowl Lift the R cube Put in the bowl Put ...
- **p. 5 / 4 Experiment - extractive body cue:** In simulation and real-world environments, we select MDT [52] as our base policy.
- **p. 5 / 4 Experiment - extractive body cue:** We select CALVIN as our simulation platform due to its focus on long-horizon tasks, and introduce LCALVIN, a new benchmark that extends task sequences from ...
- **p. 6 / 4 Experiment - extractive body cue:** To further evaluate the performance in unseen scenarios, we additionally conducted tests in real-world environments with previously unseen settings.
- **p. 7 / 4 Experiment - extractive body cue:** Press blue button Grab the corn Put in the sink Press yellow button Unseen Type Method Tasks Completed in Sequence 1 2 3 4 Random ...
- **p. 8 / 4 Experiment - extractive body cue:** This versatility not only validates the robustness of our approach but also highlights its potential for integration with a wide range of existing VLA models, ...
- **p. 8 / 4 Experiment - extractive body cue:** This observation is fully consistent with the findings in RH20T-P [61], suggesting that adopting a decomposition strategy allows the model to efficiently correct task execution ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4 Experiment (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Figure 4, our model achieves performance improvements in the D→D and ABCD→D of the L-CALVIN benchmark. | p. 6 (4 Experiment) |
| 4 Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Figure 5, while the success rate of the base policy drops to zero after the seventh task, our approach is still ... | p. 6 (4 Experiment) |
| 4 Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Figure 6, our model achieves significant improvements over the base policy across all time horizons. | p. 7 (4 Experiment) |
| 4 Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | Performance significantly improves with input-level adaptation, mainly from adding detection data during movement for better control and removing unwanted third-person visual interference during interaction ... | p. 8 (4 Experiment) |
| 4 Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | SOTA As presented in Table 2 and Figure 7, our model achieves the best performance in both simulated and real-world experiments. | p. 7 (4 Experiment) |

## Dataset / Benchmark Role

- **p. 7 / 4 Experiment - extractive body cue:** In real-world robotic experiments, our method consistently outperforms the state-of-the-art algorithm π0 across the generalization task.
- **p. 6 / 4 Experiment - extractive body cue:** Lift the C cube Put in the bowl Lift the O cube Put in the bowl Lift the R cube Put in the bowl Put ...
- **p. 5 / 4 Experiment - extractive body cue:** In simulation and real-world environments, we select MDT [52] as our base policy.
- **p. 5 / 4 Experiment - extractive body cue:** We select CALVIN as our simulation platform due to its focus on long-horizon tasks, and introduce LCALVIN, a new benchmark that extends task sequences from ...
- **p. 6 / 4 Experiment - extractive body cue:** To further evaluate the performance in unseen scenarios, we additionally conducted tests in real-world environments with previously unseen settings.
- **p. 7 / 4 Experiment - extractive body cue:** Press blue button Grab the corn Put in the sink Press yellow button Unseen Type Method Tasks Completed in Sequence 1 2 3 4 Random ...
- **p. 8 / 4 Experiment - extractive body cue:** This versatility not only validates the robustness of our approach but also highlights its potential for integration with a wide range of existing VLA models, ...
- **p. 8 / 4 Experiment - extractive body cue:** This observation is fully consistent with the findings in RH20T-P [61], suggesting that adopting a decomposition strategy allows the model to efficiently correct task execution ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: In contrast to previous methods that (a) adopt a unified model but are limited to short- horizon tasks and fail to address skill ...
- **p. 3 / Figure/Table caption - extractive body cue:** Table 1: Comparison between MDT and MDT en- hanced with a Moving Policy (MP) across differ- ent task horizons.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Overview of Long-VLA. (a) Task decomposition with aligned visual observations and language annotations. (b) Phase-aware masking enables the model to selectively attend to ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Real-world setup. Simulation & Real-world Experi- ment. We select CALVIN as our sim- ulation platform due to its focus on long-horizon tasks, and ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Simulation performance on L-CALVIN. Lift the C cube Put in the bowl Lift the O cube Put in the bowl Lift the R ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: Real-world Performance on Sorting. inputs, as demonstrated by its performance in the CALVIN environments. In real-world settings, this decision is further supported by ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6: Real-world performance on cleaning. Evaluation on Real-World Scene (Cleaning). To provide a more rigor- ous evaluation, we propose a clean- ing task featuring ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Comparison with SOTA methods on L-CALVIN simulation benchmark. Train→Test

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In real-world robotic experiments, our method consistently outperforms the state-of-the-art algorithm π0 across the generalization task. | embodiment, simulator version and control stack | p. 7 (4 Experiment), p. 6 (4 Experiment) |
| Task/environment | Lift the C cube Put in the bowl Lift the O cube Put in the bowl Lift the R cube Put in the bowl ... | reset, timeout, object/scene variation | p. 6 (4 Experiment), p. 5 (4 Experiment) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 4 (3 Method), p. 5 (3 Method) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 5 (3 Method), p. 4 (3 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| As shown in Figure 5, while the success rate of the base policy drops to zero after the seventh task, our approach is still ... | definition/direction/unit from same section | p. 6 (4 Experiment) |
| Figure 8: Definition of VLA Models. VLA models generate sequences of actions conditioned on input language instructions and the current environmental state. A.2 Skill ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |
| These findings demonstrate that while foundational capabilities may suffice for single-step tasks, long-horizon tasks demand minimal error accumulation. | definition/direction/unit from same section | p. 7 (4 Experiment) |
| Figure 1: In contrast to previous methods that (a) adopt a unified model but are limited to short- horizon tasks and fail to address ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Lift the C cube Put in the bowl Lift the O cube Put in the bowl Lift the R cube Put in the bowl ... | definition/direction/unit from same section | p. 6 (4 Experiment) |
| This demonstrates the robustness of our method in handling long-horizon tasks. | definition/direction/unit from same section | p. 7 (4 Experiment) |
| In this manner, a shared policy can be trained across stages, effectively combining the data-driven advantages of endto-end VLA models with strategies for long-horizon ... | definition/direction/unit from same section | p. 8 (4 Experiment) |
| Performance significantly improves with input-level adaptation, mainly from adding detection data during movement for better control and removing unwanted third-person visual interference during interaction ... | definition/direction/unit from same section | p. 8 (4 Experiment) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In real-world robotic experiments, our method consistently outperforms the state-of-the-art algorithm π0 across the generalization task. | comparison identity and matched condition | p. 7 (4 Experiment) |
| RQ2: How does our Long-VLA compare with state-of-the-art (SOTA) methods? | comparison identity and matched condition | p. 5 (4 Experiment) |
| Since π0 [16] is not evaluated in the CALVIN environment, we use it as a baseline in real-world experiments. | comparison identity and matched condition | p. 6 (4 Experiment) |
| In addition, we include several baselines to more comprehensively evaluate the effectiveness of our method: video generation-based VLA models (GR-1 [58] and UP-VLA [59]) ... | comparison identity and matched condition | p. 6 (4 Experiment) |
| RandomLocation 1 2 3 4 0 25 50 75 100 Task completed (%) Random Location 1 2 3 4 5 6 7 8 0 ... | comparison identity and matched condition | p. 7 (4 Experiment) |
| Figure 1: In contrast to previous methods that (a) adopt a unified model but are limited to short- horizon tasks and fail to address ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 2: Overview of Long-VLA. (a) Task decomposition with aligned visual observations and language annotations. (b) Phase-aware masking enables the model to selectively attend ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| Figure 5: Real-world Performance on Sorting. inputs, as demonstrated by its performance in the CALVIN environments. In real-world settings, this decision is further supported ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| 4.4 Ablation Analyses We validate the key design elements of Long-VLA -decomposition strategy, input-level adaptation, and unified model-in Table 3. | component/input/data sensitivity | p. 7 (4 Experiment) |
| Real (Sorting) Real (Cleaning) Sim (D-D) ✗ ✗ ✓ 2.3 1.4 4.11 ✓ ✗ ✓ 3.6 (1.3 ↑) 1.7 (0.3 ↑) 4.42 (0.31 ↑) ... | component/input/data sensitivity | p. 8 (4 Experiment) |
| Figure 9: (a) Illustration of skill-chaining challenges like state mismatch in CALVIN benchmark. In the independent setting, each subtask starts from a state within ... | component/input/data sensitivity | p. 13 (Figure/Table caption) |
| Table 6: Ablation on Input Modality on CALVIN(D-D). d denotes detection information, s denotes static camera views, g denotes gripper camera views. Setting Moving ... | component/input/data sensitivity | p. 18 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To this end, we propose Long-VLA, the first end-to-end VLA model specifically designed for longhorizon robotic manipulation. | As shown in Figure 4, our model achieves performance improvements in the D→D and ABCD→D of the L-CALVIN benchmark. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4 Experiment), p. 6 (4 Experiment), p. 7 (4 Experiment), p. 8 (4 Experiment), p. 7 (4 Experiment), p. 8 (4 Experiment) |
| Primary metric/result | As shown in Figure 5, while the success rate of the base policy drops to zero after the seventh task, our approach is still ... | numeric claim only at cited anchor | p. 6 (4 Experiment) |

- Numeric sentences retained from the body:
- **p. 5 / 4 Experiment - extractive body cue:** We select CALVIN as our simulation platform due to its focus on long-horizon tasks, and introduce LCALVIN, a new benchmark that extends task sequences from ...
- **p. 7 / 4 Experiment - extractive body cue:** RandomLocation 1 2 3 4 0 25 50 75 100 Task completed (%) Random Location 1 2 3 4 5 6 7 8 0 25 ...
- **p. 3 / 3 Method - extractive body cue:** To ensure phase alignment, the cutting point is set 10-15 frames prior to the object's state change.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 12: Failure case of π0. Base Policy LongVLA Press blue button Grab the corn Put in the sink Press yellow button Fail to ... | p. 19 (Figure/Table caption) |
| body limitation/failure cue | Figure 1: In contrast to previous methods that (a) adopt a unified model but are limited to short- horizon tasks and fail to address ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | By segmenting each subtask into movement and interaction phases with targeted masking, Long-VLA mitigates distribution shifts and enhances subtask compatibility, enabling robust performance across ... | p. 8 (5 Conclusion) |
| body limitation/failure cue | This demonstrates the robustness of our method in handling long-horizon tasks. | p. 7 (4 Experiment) |
| body limitation/failure cue | (Left: cleaning; Right: sorting) These performance gains stem from two key factors: the robust capability of our base policy and the substantial enhancement provided ... | p. 7 (4 Experiment) |
| body limitation/failure cue | Performance significantly improves with input-level adaptation, mainly from adding detection data during movement for better control and removing unwanted third-person visual interference during interaction ... | p. 8 (4 Experiment) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We select CALVIN as our simulation platform due to its focus on long-horizon tasks, and introduce LCALVIN, a new benchmark that extends task sequences ... | p. 5 (4 Experiment) |
| (3) where α is a hyperparameter, which we set to 0.1. | p. 4 (3 Method) |
| This ensures that attention is only computed between active token pairs. | p. 4 (3 Method) |
| Further implementation details are provided in Appendix C.1. | p. 5 (3 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 19 / Figure/Table caption - extractive body cue:** Figure 12: Failure case of π0. Base Policy LongVLA Press blue button Grab the corn Put in the sink Press yellow button Fail to press ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: In contrast to previous methods that (a) adopt a unified model but are limited to short- horizon tasks and fail to address skill ...
- **p. 8 / 5 Conclusion - extractive body cue:** By segmenting each subtask into movement and interaction phases with targeted masking, Long-VLA mitigates distribution shifts and enhances subtask compatibility, enabling robust performance across complex ...
- **p. 7 / 4 Experiment - extractive body cue:** This demonstrates the robustness of our method in handling long-horizon tasks.
- **p. 7 / 4 Experiment - extractive body cue:** (Left: cleaning; Right: sorting) These performance gains stem from two key factors: the robust capability of our base policy and the substantial enhancement provided by ...
- **p. 8 / 4 Experiment - extractive body cue:** Performance significantly improves with input-level adaptation, mainly from adding detection data during movement for better control and removing unwanted third-person visual interference during interaction for ...

- **PDF anchors reviewed:** datasets p. 7 (4 Experiment), p. 6 (4 Experiment), p. 5 (4 Experiment), p. 5 (4 Experiment), p. 6 (4 Experiment), p. 7 (4 Experiment), metrics p. 6 (4 Experiment), p. 13 (Figure/Table caption), p. 7 (4 Experiment), p. 1 (Figure/Table caption), p. 6 (4 Experiment), p. 7 (4 Experiment), baselines p. 7 (4 Experiment), p. 5 (4 Experiment), p. 6 (4 Experiment), p. 6 (4 Experiment), p. 7 (4 Experiment), p. 1 (Figure/Table caption), results p. 6 (4 Experiment), p. 6 (4 Experiment), p. 7 (4 Experiment), p. 8 (4 Experiment), p. 7 (4 Experiment), p. 8 (4 Experiment).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
