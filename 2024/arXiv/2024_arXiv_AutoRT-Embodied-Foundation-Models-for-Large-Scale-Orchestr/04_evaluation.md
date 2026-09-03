# Evaluation - AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://deepmind.google/research/publications/48151/; PDF retrieval source: https://deepmind.google/research/publications/48151/. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 9 (3. Place the napkin onto), p. 10 (3. Place the napkin onto), p. 8 (3. Place the napkin onto), p. 8 (3. Place the napkin onto), p. 9 (3. Place the napkin onto)): Table 1: AutoRT data, split by collect policy used. Scripted policy was used most frequently, while teleoperation had the highest success rate. Collect Method Average Language L2 Dist Lang. Table ...

## Evaluation Body Digest

- **p. 9 / 3. Place the napkin onto - extractive body cue:** First, 5 test scenes were set up with objects that the robot should not interact with, including lifelike toy animals, sharp items, and people.
- **p. 10 / 3. Place the napkin onto - extractive body cue:** This "sparse" data presents a harder learning problem than the datasets used in existing state of the art robot learning methods like Brohan et al.
- **p. 10 / 3. Place the napkin onto - extractive body cue:** If these policies only handle simpler tasks or have lower success rates in unseen settings, it lowers the throughput of successful episodes.
- **p. 8 / 3. Place the napkin onto - extractive body cue:** Accuracy of AutoRT Task Generation: Across a sample of 64 scenes, we consider all 259 tasks generated and label whether each task is safe and ...
- **p. 8 / 3. Place the napkin onto - extractive body cue:** 5.3 AFFORDANCE AND ROBOT CONSTITUTION In this section we study the effect of constitutional prompting and LLM self-critiquing on identifying safe and feasible tasks.
- **p. 9 / 3. Place the napkin onto - extractive body cue:** We demonstrated that this approach results in useful, diverse, and large-scale data - leading to 77k realworld demonstrations collected by over 20 robots in 7 ...
- **p. 11 / 3. Place the napkin onto - extractive body cue:** AUTHOR CONTRIBUTIONS Author Model Training & Eval Navigation & Scene Description Task Generation & Filtering Collect Methods Data Leadership Paper Writing Michael Ahn ✓ Debidatta ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: AutoRT data, split by collect policy used. Scripted policy was used most frequently, while teleoperation had the highest success rate. Collect Method Average ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** multi-robot demonstration/dataset ecosystem.
- **Input boundary:** multi-view observation, language/task label과 action trajectory.
- **Output/decision under evaluation:** dataset sample 또는 learned policy action.
- **Primary target:** coverage, cross-embodiment transfer, data efficiency와 task success.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 1: AutoRT data, split by collect policy used. Scripted policy was used most frequently, while teleoperation had the highest success rate. Collect Method ... | p. 7 (Figure/Table caption) |
| 3. Place the napkin onto | SYSTEM / EVALUATION SCOPE UNRESOLVED | These increases are modest, but we note that the focus of AutoRT was on collecting diverse data, not on achieving high success rates. | p. 9 (3. Place the napkin onto) |
| 3. Place the napkin onto | SYSTEM / EVALUATION SCOPE UNRESOLVED | If these policies only handle simpler tasks or have lower success rates in unseen settings, it lowers the throughput of successful episodes. | p. 10 (3. Place the napkin onto) |
| 3. Place the napkin onto | SYSTEM / EVALUATION SCOPE UNRESOLVED | Injecting the high-level guidance into the LLM prompt improves the relevance of generated tasks. | p. 8 (3. Place the napkin onto) |
| 3. Place the napkin onto | SYSTEM / EVALUATION SCOPE UNRESOLVED | Using an LLM at all improves both feasibility and relevance thanks to common-sense inherited from Internet-scale data. | p. 8 (3. Place the napkin onto) |

## Dataset / Benchmark Role

- **p. 9 / 3. Place the napkin onto - extractive body cue:** First, 5 test scenes were set up with objects that the robot should not interact with, including lifelike toy animals, sharp items, and people.
- **p. 10 / 3. Place the napkin onto - extractive body cue:** This "sparse" data presents a harder learning problem than the datasets used in existing state of the art robot learning methods like Brohan et al.
- **p. 10 / 3. Place the napkin onto - extractive body cue:** If these policies only handle simpler tasks or have lower success rates in unseen settings, it lowers the throughput of successful episodes.
- **p. 8 / 3. Place the napkin onto - extractive body cue:** Accuracy of AutoRT Task Generation: Across a sample of 64 scenes, we consider all 259 tasks generated and label whether each task is safe and ...
- **p. 8 / 3. Place the napkin onto - extractive body cue:** 5.3 AFFORDANCE AND ROBOT CONSTITUTION In this section we study the effect of constitutional prompting and LLM self-critiquing on identifying safe and feasible tasks.
- **p. 9 / 3. Place the napkin onto - extractive body cue:** We demonstrated that this approach results in useful, diverse, and large-scale data - leading to 77k realworld demonstrations collected by over 20 robots in 7 ...
- **p. 11 / 3. Place the napkin onto - extractive body cue:** AUTHOR CONTRIBUTIONS Author Model Training & Eval Navigation & Scene Description Task Generation & Filtering Collect Methods Data Leadership Paper Writing Michael Ahn ✓ Debidatta ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 1: System diagram for AutoRT. Each robot explores the environment, sampling a random navigation target close to objects. The scene and objects in it ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 2: Examples of robot collect environments used. These environments have a variety of surfaces and semantically different objects to practice manipulation on, along with ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: On the left is AutoRT robot usage and on the right is t-SNE visualization of tasks, colored by collect policy used. Each point ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: AutoRT episodes collected and unique tasks over time 5.1 DIVERSITY SCORING Given a fixed budget of human oversight and a fleet of robots, ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: AutoRT data, split by collect policy used. Scripted policy was used most frequently, while teleoperation had the highest success rate. Collect Method Average ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Diversity of language embeddings from task generators. AutoRT generates language embeddings that are further apart. consider two different axes of diversity: visual diversity ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Visual diversity visualizations for AutoRT, as scored by distance to closest k-means centroid. Left: Histogram of 1000 random successes per collect policy (or ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: Example last-frame images (color corrected) from RT-1 (left) and AutoRT (right) are shown in Table 3. We find that AutoRT's tasks (guided and ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | First, 5 test scenes were set up with objects that the robot should not interact with, including lifelike toy animals, sharp items, and people. | embodiment, simulator version and control stack | p. 9 (3. Place the napkin onto), p. 10 (3. Place the napkin onto) |
| Task/environment | This "sparse" data presents a harder learning problem than the datasets used in existing state of the art robot learning methods like Brohan et ... | reset, timeout, object/scene variation | p. 10 (3. Place the napkin onto), p. 10 (3. Place the napkin onto) |
| Observation/sensor | multi-view observation, language/task label과 action trajectory | calibration, preprocessing, privileged input | p. 5 (3. Place the napkin onto), p. 5 (3. Place the napkin onto) |
| Output/decision | dataset sample 또는 learned policy action | action frame, controller and termination | p. 2 (1 INTRODUCTION), p. 7 (3. Place the napkin onto) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 1: AutoRT data, split by collect policy used. Scripted policy was used most frequently, while teleoperation had the highest success rate. Collect Method ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| These increases are modest, but we note that the focus of AutoRT was on collecting diverse data, not on achieving high success rates. | definition/direction/unit from same section | p. 9 (3. Place the napkin onto) |
| If these policies only handle simpler tasks or have lower success rates in unseen settings, it lowers the throughput of successful episodes. | definition/direction/unit from same section | p. 10 (3. Place the napkin onto) |
| Figure 5: Visual diversity visualizations for AutoRT, as scored by distance to closest k-means centroid. Left: Histogram of 1000 random successes per collect policy ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 1: System diagram for AutoRT. Each robot explores the environment, sampling a random navigation target close to objects. The scene and objects in ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Accuracy of AutoRT Task Generation: Across a sample of 64 scenes, we consider all 259 tasks generated and label whether each task is safe ... | definition/direction/unit from same section | p. 8 (3. Place the napkin onto) |
| Figure 4: AutoRT episodes collected and unique tasks over time 5.1 DIVERSITY SCORING Given a fixed budget of human oversight and a fleet of ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Table 2: Diversity of language embeddings from task generators. AutoRT generates language embeddings that are further apart. consider two different axes of diversity: visual ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 9: Hours of data collected per policy per day. We aimed for teleop collect throughput to exceed a simple 1 person:1 robot baseline. ... | comparison identity and matched condition | p. 26 (Figure/Table caption) |
| As noted by prior work (Ahn et al., 2022; Mees et al., 2023; Gao et al., 2023), foundation models also face challenges in reasoning ... | comparison identity and matched condition | p. 10 (3. Place the napkin onto) |
| Aditionally we find that all 14 errors occurred during teleop task sampling, attributable to forcing teleop task Table 3: Comparison of task generation methods ... | comparison identity and matched condition | p. 8 (3. Place the napkin onto) |
| Table 3: Comparison of task generation methods at generating completable tasks and relevant tasks. Injecting the high-level guidance into the LLM prompt improves the ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| As a sanity check on the usefulness of the data, we run a training comparison with the RT-1 model. | comparison identity and matched condition | p. 9 (3. Place the napkin onto) |
| We additionally include an ablation where we train from only the teleoperated segment of AutoRT data. | comparison identity and matched condition | p. 9 (3. Place the napkin onto) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 5.3 AFFORDANCE AND ROBOT CONSTITUTION In this section we study the effect of constitutional prompting and LLM self-critiquing on identifying safe and feasible tasks. | component/input/data sensitivity | p. 8 (3. Place the napkin onto) |
| Table 4: Effect of constitutional prompting on safety of proposed tasks Task Generation Unsafe prompting Minimal prompting Constitutional prompting Filter % Safe Recall | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| Adversarial Testing of Constitutional Prompting: To measure the effect of constitutional prompting, we set up deliberately adversarial scenes, and ablate our rules from the ... | component/input/data sensitivity | p. 9 (3. Place the napkin onto) |
| Table 6: Tasks used to evaluate training ablations Task Group Tasks Picking pick utensil, pick office supplies, pick chips, pick bag, pick coffee cup, ... | component/input/data sensitivity | p. 22 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we propose AutoRT, a system that leverages existing foundation models to scale up the deployment of operational robots in completely unseen ... | Table 1: AutoRT data, split by collect policy used. Scripted policy was used most frequently, while teleoperation had the highest success rate. Collect Method ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 9 (3. Place the napkin onto), p. 10 (3. Place the napkin onto), p. 8 (3. Place the napkin onto), p. 8 (3. Place the napkin onto), p. 9 (3. Place the napkin onto) |
| Primary metric/result | These increases are modest, but we note that the focus of AutoRT was on collecting diverse data, not on achieving high success rates. | numeric claim only at cited anchor | p. 9 (3. Place the napkin onto) |

- Numeric sentences retained from the body:
- **p. 8 / 3. Place the napkin onto - extractive body cue:** We find that AutoRT's tasks (guided and unguided) are 1.5x more likely to be feasible than templated language.
- **p. 8 / 3. Place the napkin onto - extractive body cue:** Accuracy of AutoRT Task Generation: Across a sample of 64 scenes, we consider all 259 tasks generated and label whether each task is safe and ...
- **p. 8 / 3. Place the napkin onto - extractive body cue:** In this sample, we found 31 tasks that outght to have been rejected, giving a base rate of 228/259 = 88% acceptable tasks.
- **p. 9 / 3. Place the napkin onto - extractive body cue:** We demonstrated that this approach results in useful, diverse, and large-scale data - leading to 77k realworld demonstrations collected by over 20 robots in 7 ...
- **p. 1 / ABSTRACT - extractive body cue:** We demonstrate AutoRT proposing instructions to over 20 robots across multiple buildings and collecting 77k real robot episodes via both teleoperation and autonomous robot policies.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We describe the AutoRT system, instantiate it with a fleet of real-world mobile manipulators, and present the results of an extensive real-world evaluation over 7 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Failures of perception such as hallucination of objects, lack of generalization to novel environments, and motion blur can introduce and propagate failures in the ... | p. 10 (3. Place the napkin onto) |
| body limitation/failure cue | Despite the promise of AutoRT, the current approach comes with a number of limitations. | p. 10 (3. Place the napkin onto) |
| body limitation/failure cue | How often does the LLM reject (or fail to reject) tasks that should be rejected? | p. 8 (3. Place the napkin onto) |
| body limitation/failure cue | Additionally constitutional prompting is able to achieve high recall when given unsafe tasks. | p. 9 (3. Place the napkin onto) |
| body limitation/failure cue | Table 4: Effect of constitutional prompting on safety of proposed tasks Task Generation Unsafe prompting Minimal prompting Constitutional prompting Filter % Safe Recall | p. 9 (Figure/Table caption) |
| body limitation/failure cue | Table 9: Tasks generated in Section 5.3 experiments. We present an image the robot sees, tasks generated by the unsafe task generation prompt, and ... | p. 24 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We describe the AutoRT system, instantiate it with a fleet of real-world mobile manipulators, and present the results of an extensive real-world evaluation over ... | p. 2 (1 INTRODUCTION) |
| Valid tasks are run by the robot, the episodes are scored, and the process repeats. | p. 4 (3. Place the napkin onto) |
| No part of this requires advance knowledge of the layout of the environment or objects it contains, making it easy to run on a ... | p. 4 (3. Place the napkin onto) |
| The scripted pick policy pseudocode is provided in Appendix H. | p. 5 (3. Place the napkin onto) |
| For a breakdown of throughput by collect policy, or visualization of action trajectories, see Appendix I. | p. 5 (3. Place the napkin onto) |
| This influenced our decision to run RT-2 less frequently. | p. 6 (3. Place the napkin onto) |
| These robots were easier to supervise due to their smaller range of motion, and were run with 1 human watching up to 8 robots. | p. 6 (3. Place the napkin onto) |
| Robot episodes are first embedded by a visual encoder, then k-means unsupervised clustering is done in the space. | p. 7 (3. Place the napkin onto) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 3. Place the napkin onto - extractive body cue:** Failures of perception such as hallucination of objects, lack of generalization to novel environments, and motion blur can introduce and propagate failures in the system.
- **p. 10 / 3. Place the napkin onto - extractive body cue:** Despite the promise of AutoRT, the current approach comes with a number of limitations.
- **p. 8 / 3. Place the napkin onto - extractive body cue:** How often does the LLM reject (or fail to reject) tasks that should be rejected?
- **p. 9 / 3. Place the napkin onto - extractive body cue:** Additionally constitutional prompting is able to achieve high recall when given unsafe tasks.
- **p. 9 / Figure/Table caption - extractive body cue:** Table 4: Effect of constitutional prompting on safety of proposed tasks Task Generation Unsafe prompting Minimal prompting Constitutional prompting Filter % Safe Recall
- **p. 24 / Figure/Table caption - extractive body cue:** Table 9: Tasks generated in Section 5.3 experiments. We present an image the robot sees, tasks generated by the unsafe task generation prompt, and the ...

- **Evidence anchors reviewed:** datasets p. 9 (3. Place the napkin onto), p. 10 (3. Place the napkin onto), p. 10 (3. Place the napkin onto), p. 8 (3. Place the napkin onto), p. 8 (3. Place the napkin onto), p. 9 (3. Place the napkin onto), metrics p. 7 (Figure/Table caption), p. 9 (3. Place the napkin onto), p. 10 (3. Place the napkin onto), p. 8 (Figure/Table caption), p. 4 (Figure/Table caption), p. 8 (3. Place the napkin onto), baselines p. 26 (Figure/Table caption), p. 10 (3. Place the napkin onto), p. 8 (3. Place the napkin onto), p. 8 (Figure/Table caption), p. 9 (3. Place the napkin onto), p. 9 (3. Place the napkin onto), results p. 7 (Figure/Table caption), p. 9 (3. Place the napkin onto), p. 10 (3. Place the napkin onto), p. 8 (3. Place the napkin onto), p. 8 (3. Place the napkin onto), p. 9 (3. Place the napkin onto).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (26 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Figure 7: Robot environments before and after adjusting scene based on visual diversity. Note the unconventional arrangement of objects, surfaces, and distractors. F MODEL IMPROVEMENT EVALUATION TASKS For picking from ... (p. 21, Figure/Table caption).
- **Metric evidence:** Figure 5: Visual diversity visualizations for AutoRT, as scored by distance to closest k-means centroid. Left: Histogram of 1000 random successes per collect policy (or all successes from RT-2 collect). ... (p. 8, Figure/Table caption).
- **Baseline/ablation evidence:** As a sanity check on the usefulness of the data, we run a training comparison with the RT-1 model. (p. 9, 3. Place the napkin onto).
- **Failure/negative evidence:** Failures of perception such as hallucination of objects, lack of generalization to novel environments, and motion blur can introduce and propagate failures in the system. (p. 10, 3. Place the napkin onto).
