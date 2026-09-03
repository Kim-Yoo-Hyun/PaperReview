# Evaluation - Demonstrating OK-Robot: What Really Matters in Integrating Open-Knowledge Models for Robotics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p091.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p091.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (III. EXPERIMENTS), p. 1 (Figure/Table caption), p. 7 (III. EXPERIMENTS), p. 6 (III. EXPERIMENTS), p. 7 (III. EXPERIMENTS), p. 8 (III. EXPERIMENTS)): Results of home experiments Over the 10 home environment, OK-Robot achieved a 58.5% success rates in completing full pick-and-drops.

## Evaluation Body Digest

- **p. 7 / III. EXPERIMENTS - extractive body cue:** The three leading causes of failures are failing to retrieve the right object to navigate to from the semantic memory (9.3%), getting a difficult pose ...
- **p. 8 / III. EXPERIMENTS - extractive body cue:** Robot hardware limitations: While our robot of choice, a Hello Robot: Stretch, is able to pick-and-drop a variety of objects, certain hardware limitations also dictate ...
- **p. 8 / III. EXPERIMENTS - extractive body cue:** The robot hardware or the RealSense camera can occasionally get miscalibrated over time, especially during continuous home operations.
- **p. 6 / III. EXPERIMENTS - extractive body cue:** However, given only a scan, OK-Robot was able to successfully pick and drop objects like stuffed lion, plush cactus, toy drill, or green water bottle ...
- **p. 6 / III. EXPERIMENTS - extractive body cue:** In Appendix Figure 12, we show the robot performing pick-and-drop in these two environments.
- **p. 7 / III. EXPERIMENTS - extractive body cue:** Generally, this has been the case for scenes where there are multiple visually or semantically similar objects, as shown in the figure.
- **p. 7 / III. EXPERIMENTS - extractive body cue:** Similarly, as we clean up clutters from the environment, we find that the manipulation accuracy also improves and the error rates decrease from 25% to ...
- **p. 7 / III. EXPERIMENTS - extractive body cue:** As we can see from this breakdown, as we clean up the environment and remove the ambiguous objects, the navigation accuracy goes up, and the ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mobile base와 one/two-arm manipulation environment.
- **Input boundary:** egocentric RGB-D, language/task goal, base-arm proprioception.
- **Output/decision under evaluation:** base motion plus arm/gripper action.
- **Primary target:** long-horizon task success, reachability, collision과 recovery.
- **Detected evaluation headings:** III. EXPERIMENTS (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| III. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Results of home experiments Over the 10 home environment, OK-Robot achieved a 58.5% success rates in completing full pick-and-drops. | p. 6 (III. EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 1: OK-Robot is an Open Knowledge robotic system, which integrates a variety of learned models trained on publicly available data, to pick and ... | p. 1 (Figure/Table caption) |
| III. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Similarly, as we clean up clutters from the environment, we find that the manipulation accuracy also improves and the error rates decrease from 25% ... | p. 7 (III. EXPERIMENTS) |
| III. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Notably, this success rate is over novel objects sourced from each home with our zero-shot algorithm. | p. 6 (III. EXPERIMENTS) |
| III. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | II-A, outperforms other semantic memory modules by a small margin. | p. 7 (III. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 7 / III. EXPERIMENTS - extractive body cue:** The three leading causes of failures are failing to retrieve the right object to navigate to from the semantic memory (9.3%), getting a difficult pose ...
- **p. 8 / III. EXPERIMENTS - extractive body cue:** Robot hardware limitations: While our robot of choice, a Hello Robot: Stretch, is able to pick-and-drop a variety of objects, certain hardware limitations also dictate ...
- **p. 8 / III. EXPERIMENTS - extractive body cue:** The robot hardware or the RealSense camera can occasionally get miscalibrated over time, especially during continuous home operations.
- **p. 6 / III. EXPERIMENTS - extractive body cue:** However, given only a scan, OK-Robot was able to successfully pick and drop objects like stuffed lion, plush cactus, toy drill, or green water bottle ...
- **p. 6 / III. EXPERIMENTS - extractive body cue:** In Appendix Figure 12, we show the robot performing pick-and-drop in these two environments.
- **p. 7 / III. EXPERIMENTS - extractive body cue:** Generally, this has been the case for scenes where there are multiple visually or semantically similar objects, as shown in the figure.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: OK-Robot is an Open Knowledge robotic system, which integrates a variety of learned models trained on publicly available data, to pick and drop ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: Open-vocabulary, open knowledge object localization and navigation in the real-world. We use the VoxelMap [25] for localizing objects with natural language queries, and ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: Open-vocabulary grasping in the real world. From left to right, we show the (a) robot POV image, (b) all suggested grasps from AnyGrasp ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: All the success and failure cases in our home experiments, aggregated over all three cleaning phases, and broken down by mode of failure. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Ablation experiment using different semantic memory and grasping modules, with the bars showing average performance and the error bars showing standard deviation over ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: Failure modes of our method in novel homes, broken down by the failures of the three modules and the cleanup levels. of the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6. We see that generally, the leading cause of failure is our manipulation failure, which intuitively is the most difficult as well. However, at ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7: Samples of failed or ambiguous language queries into our semantic memory module. Since the memory module depends on pretrained large vision language model, ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The three leading causes of failures are failing to retrieve the right object to navigate to from the semantic memory (9.3%), getting a difficult ... | embodiment, simulator version and control stack | p. 7 (III. EXPERIMENTS), p. 8 (III. EXPERIMENTS) |
| Task/environment | Robot hardware limitations: While our robot of choice, a Hello Robot: Stretch, is able to pick-and-drop a variety of objects, certain hardware limitations also ... | reset, timeout, object/scene variation | p. 8 (III. EXPERIMENTS), p. 8 (III. EXPERIMENTS) |
| Observation/sensor | egocentric RGB-D, language/task goal, base-arm proprioception | calibration, preprocessing, privileged input | p. 2 (I. INTRODUCTION), p. 5 (II. TECHNICAL COMPONENTS AND METHOD) |
| Output/decision | base motion plus arm/gripper action | action frame, controller and termination | p. 3 (II. TECHNICAL COMPONENTS AND METHOD), p. 3 (II. TECHNICAL COMPONENTS AND METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Similarly, as we clean up clutters from the environment, we find that the manipulation accuracy also improves and the error rates decrease from 25% ... | definition/direction/unit from same section | p. 7 (III. EXPERIMENTS) |
| As we can see from this breakdown, as we clean up the environment and remove the ambiguous objects, the navigation accuracy goes up, and ... | definition/direction/unit from same section | p. 7 (III. EXPERIMENTS) |
| Notably, this success rate is over novel objects sourced from each home with our zero-shot algorithm. | definition/direction/unit from same section | p. 6 (III. EXPERIMENTS) |
| Results of home experiments Over the 10 home environment, OK-Robot achieved a 58.5% success rates in completing full pick-and-drops. | definition/direction/unit from same section | p. 6 (III. EXPERIMENTS) |
| Fig. 1: OK-Robot is an Open Knowledge robotic system, which integrates a variety of learned models trained on publicly available data, to pick and ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| This miscalibration can lead to manipulation errors since that module requires hand-eye coordination in the robot. | definition/direction/unit from same section | p. 8 (III. EXPERIMENTS) |
| Grasping models that generates a grasp trajectory as well as a pose may solve such issues. | definition/direction/unit from same section | p. 8 (III. EXPERIMENTS) |
| Fig. 2: Open-vocabulary, open knowledge object localization and navigation in the real-world. We use the VoxelMap [25] for localizing objects with natural language queries, ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 5: Ablation experiment using different semantic memory and grasping modules, with the bars showing average performance and the error bars showing standard deviation ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Both were larger compared to the average NY homes, requiring more robot motion to navigate to different goals. | comparison identity and matched condition | p. 6 (III. EXPERIMENTS) |
| II-A, outperforms other semantic memory modules by a small margin. | comparison identity and matched condition | p. 7 (III. EXPERIMENTS) |
| These homes were larger and more complex: a cluttered, actively-used home kitchen environment, and a large, controlled test apartment used in prior work [22, ... | comparison identity and matched condition | p. 6 (III. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablations over system components Apart from the navigation and manipulation strategies used in OK-Robot, we also evaluated a number of alternative open | component/input/data sensitivity | p. 6 (III. EXPERIMENTS) |
| As we can see from this breakdown, as we clean up the environment and remove the ambiguous objects, the navigation accuracy goes up, and ... | component/input/data sensitivity | p. 7 (III. EXPERIMENTS) |
| 5: Ablation experiment using different semantic memory and grasping modules, with the bars showing average performance and the error bars showing standard deviation over ... | component/input/data sensitivity | p. 7 (III. EXPERIMENTS) |
| 4) What are the failure modes of such a system and its individual components in real home environments? | component/input/data sensitivity | p. 6 (III. EXPERIMENTS) |
| Since the memory module depends on pretrained large vision language model, its performance shows susceptibility to particular "incantations" similar to current LLMs. | component/input/data sensitivity | p. 8 (III. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We present OK-Robot, an Open Knowledge Robot that integrates state-of-the-art VLMs with powerful robotics primitives for navigation and grasping to enable pick-and-drop. | Results of home experiments Over the 10 home environment, OK-Robot achieved a 58.5% success rates in completing full pick-and-drops. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (III. EXPERIMENTS), p. 1 (Figure/Table caption), p. 7 (III. EXPERIMENTS), p. 6 (III. EXPERIMENTS), p. 7 (III. EXPERIMENTS), p. 8 (III. EXPERIMENTS) |
| Primary metric/result | Fig. 1: OK-Robot is an Open Knowledge robotic system, which integrates a variety of learned models trained on publicly available data, to pick and ... | numeric claim only at cited anchor | p. 1 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 3 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** We do so by selecting top-10 points for query A and top-50 points for query B.
- **p. 5 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** Concurrently, we pick between 10-20 objects arbitrarily in each scene that can fit in the robot gripper.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Grasping module limitations: One failure mode of our manipulation module comes from executing grasps from a pre-trained manipulation model's output based on a single ... | p. 7 (III. EXPERIMENTS) |
| body limitation/failure cue | Robot hardware limitations: While our robot of choice, a Hello Robot: Stretch, is able to pick-and-drop a variety of objects, certain hardware limitations also ... | p. 8 (III. EXPERIMENTS) |
| body limitation/failure cue | 4) What are the failure modes of such a system and its individual components in real home environments? | p. 6 (III. EXPERIMENTS) |
| body limitation/failure cue | As a result, each success and failure of the robot tells us something interesting about applying open-knowledge models in robotics, which we analyze over ... | p. 6 (III. EXPERIMENTS) |
| body limitation/failure cue | However, at a closer look, we notice a long tail of failure causes presented in Figure 4. | p. 7 (III. EXPERIMENTS) |
| body limitation/failure cue | 8: Samples of failures of our manipulation module. | p. 8 (IV. RELATED WORKS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Finally, since the drop-module is agnostic 0 20 40 60 80 100 Percentage of trials high low none Cleanup level 82 71 58 4 ... | p. 7 (III. EXPERIMENTS) |
| The three leading causes of failures are failing to retrieve the right object to navigate to from the semantic memory (9.3%), getting a difficult ... | p. 7 (III. EXPERIMENTS) |
| The robot hardware or the RealSense camera can occasionally get miscalibrated over time, especially during continuous home operations. | p. 8 (III. EXPERIMENTS) |
| Robot hardware limitations: While our robot of choice, a Hello Robot: Stretch, is able to pick-and-drop a variety of objects, certain hardware limitations also ... | p. 8 (III. EXPERIMENTS) |
| Detecting objects: On each frame of the scan, we run an open-vocabulary object detector. | p. 3 (II. TECHNICAL COMPONENTS AND METHOD) |
| Given a language query, we first convert it to a semantic vector using the CLIP language encoder. | p. 3 (II. TECHNICAL COMPONENTS AND METHOD) |
| Then, we execute pick-and-drop on remaining objects sequentially without resets between trials. | p. 5 (II. TECHNICAL COMPONENTS AND METHOD) |
| Protocol for home experiments: To run our experiment in a novel home, we move the robot to a previously unobserved room. | p. 5 (II. TECHNICAL COMPONENTS AND METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / III. EXPERIMENTS - extractive body cue:** Grasping module limitations: One failure mode of our manipulation module comes from executing grasps from a pre-trained manipulation model's output based on a single RGB-D ...
- **p. 8 / III. EXPERIMENTS - extractive body cue:** Robot hardware limitations: While our robot of choice, a Hello Robot: Stretch, is able to pick-and-drop a variety of objects, certain hardware limitations also dictate ...
- **p. 6 / III. EXPERIMENTS - extractive body cue:** 4) What are the failure modes of such a system and its individual components in real home environments?
- **p. 6 / III. EXPERIMENTS - extractive body cue:** As a result, each success and failure of the robot tells us something interesting about applying open-knowledge models in robotics, which we analyze over the ...
- **p. 7 / III. EXPERIMENTS - extractive body cue:** However, at a closer look, we notice a long tail of failure causes presented in Figure 4.
- **p. 8 / IV. RELATED WORKS - extractive body cue:** 8: Samples of failures of our manipulation module.

- **Evidence anchors reviewed:** datasets p. 7 (III. EXPERIMENTS), p. 8 (III. EXPERIMENTS), p. 8 (III. EXPERIMENTS), p. 6 (III. EXPERIMENTS), p. 6 (III. EXPERIMENTS), p. 7 (III. EXPERIMENTS), metrics p. 7 (III. EXPERIMENTS), p. 7 (III. EXPERIMENTS), p. 6 (III. EXPERIMENTS), p. 6 (III. EXPERIMENTS), p. 1 (Figure/Table caption), p. 8 (III. EXPERIMENTS), baselines p. 7 (Figure/Table caption), p. 6 (III. EXPERIMENTS), p. 7 (III. EXPERIMENTS), p. 6 (III. EXPERIMENTS), results p. 6 (III. EXPERIMENTS), p. 1 (Figure/Table caption), p. 7 (III. EXPERIMENTS), p. 6 (III. EXPERIMENTS), p. 7 (III. EXPERIMENTS), p. 8 (III. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (27 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Results of home experiments Over the 10 home environment, OK-Robot achieved a 58.5% success rates in completing full pick-and-drops. (p. 6, III. EXPERIMENTS).
- **Metric evidence:** Similarly, as we clean up clutters from the environment, we find that the manipulation accuracy also improves and the error rates decrease from 25% to 16% and finally 13%. (p. 7, III. EXPERIMENTS).
- **Baseline/ablation evidence:** Both were larger compared to the average NY homes, requiring more robot motion to navigate to different goals. (p. 6, III. EXPERIMENTS).
- **Failure/negative evidence:** Grasping module limitations: One failure mode of our manipulation module comes from executing grasps from a pre-trained manipulation model's output based on a single RGB-D image. (p. 7, III. EXPERIMENTS).
