# Evaluation - V-HOP: Visuo-Haptic 6D Object Pose Tracking

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p037.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p037.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (experiment), p. 7 (experiment), p. 8 (B. Bimanual Handover Experiment), p. 8 (B. Bimanual Handover Experiment), p. 9 (C. Can-in-Mug Experiment), p. 5 (A. Multi-embodied Dataset)): Our results show that \V-HOP consistently outperforms FoundationPose in both ADD and ADD-S metrics under different levels of occlusion. ‘These results underscore the importance of integrating visual and haptic information ...

## Evaluation Body Digest

- **p. 5 / A. Multi-embodied Dataset - extractive body cue:** Our synthesized dataset exemplifies this principle and supports our robust real-world performance.
- **p. 5 / A. Multi-embodied Dataset - extractive body cue:** However, aas demonstrated in recent work [70], leveraging a large-scale synthetic dataset enriched with domain randomization can yield superior real-world performance compared to smallSeale real-world ...
- **p. 7 / experiment - extractive body cue:** To validate the real-world effectiveness of our approach, wwe perform sim-to-real experiments using our robot platform, (Fig.
- **p. 7 / experiment - extractive body cue:** ‘To evaluate the generalizability of V-HOP, we benchmark it against NeuralFels [54], a recently introduced optimizationbased visuo-tacile pose tracking approach, using their proposed Feelsight dataset.
- **p. 8 / B. Bimanual Handover Experiment - extractive body cue:** In this experiment, the robot performs bimanual manipulation to transport the target object to the box.
- **p. 8 / B. Bimanual Handover Experiment - extractive body cue:** haptic feedback, V-HOP accurately tracks the object's pose, allowing the robot to promptly detect and respond to changes, such as the object leaving the gripper.
- **p. 9 / C. Can-in-Mug Experiment - extractive body cue:** (Right) A human perturbs the object by moving it to a different position while the robot attempts to grasp it.
- **p. 9 / C. Can-in-Mug Experiment - extractive body cue:** (top) The robot grasps the can and inserts it into the mug.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** contact-rich manipulation scene.
- **Input boundary:** tactile image/force, vision과 proprioceptive history.
- **Output/decision under evaluation:** grasp/contact action, force command 또는 object motion.
- **Primary target:** slip/contact success, force/pose error와 robustness.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 5); A. Multi-embodied Dataset (p. 5); experiment (p. 7); A. Pose Tracking Experiments (p. 7); B. Bimanual Handover Experiment (p. 7); C. Can-in-Mug Experiment (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our results show that \V-HOP consistently outperforms FoundationPose in both ADD and ADD-S metrics under different levels of occlusion. ‘These results underscore the importance ... | p. 7 (experiment) |
| experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | V-HOP achieves 1 32% lower ADD-S error compared to NeuralFeels and has a similar ADD-S-0.1d score. | p. 7 (experiment) |
| B. Bimanual Handover Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | ‘TABLE VI: Success rate on bimanual handover task: | p. 8 (B. Bimanual Handover Experiment) |
| B. Bimanual Handover Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | VI, we show the success rate for each object for five trials. | p. 8 (B. Bimanual Handover Experiment) |
| C. Can-in-Mug Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | VII) demonstrate that V-HOP, by integrating visual and haptic inputs, delivers more stable tracking and a higher overall success rate | p. 9 (C. Can-in-Mug Experiment) |

## Dataset / Benchmark Role

- **p. 5 / A. Multi-embodied Dataset - extractive body cue:** Our synthesized dataset exemplifies this principle and supports our robust real-world performance.
- **p. 5 / A. Multi-embodied Dataset - extractive body cue:** However, aas demonstrated in recent work [70], leveraging a large-scale synthetic dataset enriched with domain randomization can yield superior real-world performance compared to smallSeale real-world ...
- **p. 7 / experiment - extractive body cue:** To validate the real-world effectiveness of our approach, wwe perform sim-to-real experiments using our robot platform, (Fig.
- **p. 7 / experiment - extractive body cue:** ‘To evaluate the generalizability of V-HOP, we benchmark it against NeuralFels [54], a recently introduced optimizationbased visuo-tacile pose tracking approach, using their proposed Feelsight dataset.
- **p. 8 / B. Bimanual Handover Experiment - extractive body cue:** In this experiment, the robot performs bimanual manipulation to transport the target object to the box.
- **p. 8 / B. Bimanual Handover Experiment - extractive body cue:** haptic feedback, V-HOP accurately tracks the object's pose, allowing the robot to promptly detect and respond to changes, such as the object leaving the gripper.
- **p. 9 / C. Can-in-Mug Experiment - extractive body cue:** (Right) A human perturbs the object by moving it to a different position while the robot attempts to grasp it.
- **p. 9 / C. Can-in-Mug Experiment - extractive body cue:** (top) The robot grasps the can and inserts it into the mug.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: Network design of Y-HOP. The visual modality, based on FoundationPose [70], uses a visual encoder to process
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: Dataset sample visualization. (Top row) Barrett Hand, Shadow Hand, Allegro Hand, SHUNK SVH. (Bottom row)
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4: Performance under various occlusion ratios. We use the direct ADD and ADD-S metrics (in meters) in this
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 5: Qualitative results of pose tracking sequences. We verify the performance in the real world using YCB objects. The cup and power drill are ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6: Bimanual handover experiment. In this experiment, the robot performs bimanual manipulation to transport the target object to the box. V-HOP integrates visual and ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 7: Robustness test for the bimanual handover task. (Left) The object is placed at various randomized positions. (Right) A human perturbs the object by ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 8: Can-in-Mug tasks. (top) The robot grasps the can and inserts it into the mug. (bottom) The robot uses bimanual 10 grasp the can ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 9: Weights of visual and haptic modalities to the final prediction. We overlay the modality weights calculated using GradCAM [51] in the top-right comer.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Our synthesized dataset exemplifies this principle and supports our robust real-world performance. | embodiment, simulator version and control stack | p. 5 (A. Multi-embodied Dataset), p. 5 (A. Multi-embodied Dataset) |
| Task/environment | However, aas demonstrated in recent work [70], leveraging a large-scale synthetic dataset enriched with domain randomization can yield superior real-world performance compared to smallSeale ... | reset, timeout, object/scene variation | p. 5 (A. Multi-embodied Dataset), p. 7 (experiment) |
| Observation/sensor | tactile image/force, vision과 proprioceptive history | calibration, preprocessing, privileged input | p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION) |
| Output/decision | grasp/contact action, force command 또는 object motion | action frame, controller and termination | p. 1 (1. INTRODUCTION), p. 3 (III. MeTHODOLOGY) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| ‘TABLE VI: Success rate on bimanual handover task: | definition/direction/unit from same section | p. 8 (B. Bimanual Handover Experiment) |
| VI, we show the success rate for each object for five trials. | definition/direction/unit from same section | p. 8 (B. Bimanual Handover Experiment) |
| VII) demonstrate that V-HOP, by integrating visual and haptic inputs, delivers more stable tracking and a higher overall success rate | definition/direction/unit from same section | p. 9 (C. Can-in-Mug Experiment) |
| V-HOP achieves 1 32% lower ADD-S error compared to NeuralFeels and has a similar ADD-S-0.1d score. | definition/direction/unit from same section | p. 7 (experiment) |
| Our results show that \V-HOP consistently outperforms FoundationPose in both ADD and ADD-S metrics under different levels of occlusion. ‘These results underscore the importance ... | definition/direction/unit from same section | p. 7 (experiment) |
| 7: Robustness test for the bimanual handover task. | definition/direction/unit from same section | p. 9 (C. Can-in-Mug Experiment) |
| V) demonstrate robust performance and eliminate the need for costly real-world data collection, | definition/direction/unit from same section | p. 5 (A. Multi-embodied Dataset) |
| However, aas demonstrated in recent work [70], leveraging a large-scale synthetic dataset enriched with domain randomization can yield superior real-world performance compared to smallSeale ... | definition/direction/unit from same section | p. 5 (A. Multi-embodied Dataset) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| V-HOP achieves 1 32% lower ADD-S error compared to NeuralFeels and has a similar ADD-S-0.1d score. | comparison identity and matched condition | p. 7 (experiment) |
| In terms of computational efficiency, V-HOP is appro: mately 10 times faster than NeuralFeels, achieving 32 FPS compared to NeuralFeels' 3 FPS on an ... | comparison identity and matched condition | p. 7 (experiment) |
| V-HOP has 40% higher success rate on average compared to FoundationPose. | comparison identity and matched condition | p. 8 (B. Bimanual Handover Experiment) |
| However, aas demonstrated in recent work [70], leveraging a large-scale synthetic dataset enriched with domain randomization can yield superior real-world performance compared to smallSeale ... | comparison identity and matched condition | p. 5 (A. Multi-embodied Dataset) |
| We selected graspable YCB object [5] and grippers used in prior works [9, 45]. | comparison identity and matched condition | p. 5 (A. Multi-embodied Dataset) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| For instance, a human may move the object during task execution, remove it from the gripper, or reposition it on the table (Fig. | component/input/data sensitivity | p. 7 (B. Bimanual Handover Experiment) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| First, we introduce a novel unified haptic representation that facilitates cross-embodiment learning. | Our results show that \V-HOP consistently outperforms FoundationPose in both ADD and ADD-S metrics under different levels of occlusion. ‘These results underscore the importance ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (experiment), p. 7 (experiment), p. 8 (B. Bimanual Handover Experiment), p. 8 (B. Bimanual Handover Experiment), p. 9 (C. Can-in-Mug Experiment), p. 5 (A. Multi-embodied Dataset) |
| Primary metric/result | V-HOP achieves 1 32% lower ADD-S error compared to NeuralFeels and has a similar ADD-S-0.1d score. | numeric claim only at cited anchor | p. 7 (experiment) |

- Numeric sentences retained from the body:
- **p. 7 / experiment - extractive body cue:** Maho GP Se ADDS // ADDSOIET ‘Neuralecls [54] zat 9895 vaor ous) / _x 146 98s
- **p. 7 / experiment - extractive body cue:** In terms of computational efficiency, V-HOP is appro: mately 10 times faster than NeuralFeels, achieving 32 FPS compared to NeuralFeels' 3 FPS on an NVIDIA ...
- **p. 7 / experiment - extractive body cue:** Our Barrett Hand has 4 degrees of freedom (DoF) and 96 taxels: 24 taxels on each fingertip and 24 taxels on the palm.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 1) If the grasp attempt fails, the robot must detect the failure based on the real-time object pose and reattempt the grasp. | p. 7 (B. Bimanual Handover Experiment) |
| body limitation/failure cue | Successful execution hinges on precise pose estimation for both objects, as any noise in their poses can lead to failure. | p. 8 (C. Can-in-Mug Experiment) |
| body limitation/failure cue | Inaccurate tracking results could lead to collision during the handover. | p. 7 (B. Bimanual Handover Experiment) |
| body limitation/failure cue | More recent works aim to overcome some of these limitations. | p. 9 (VI. RELATED Works) |
| body limitation/failure cue | While model-free approaches [65, 69, 54] exist, they fall outside the scope of this work. | p. 9 (VI. RELATED Works) |
| body limitation/failure cue | V) demonstrate robust performance and eliminate the need for costly real-world data collection, | p. 5 (A. Multi-embodied Dataset) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In terms of computational efficiency, V-HOP is appro: mately 10 times faster than NeuralFeels, achieving 32 FPS compared to NeuralFeels' 3 FPS on an ... | p. 7 (experiment) |
| VI, we show the success rate for each object for five trials. | p. 8 (B. Bimanual Handover Experiment) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / B. Bimanual Handover Experiment - extractive body cue:** 1) If the grasp attempt fails, the robot must detect the failure based on the real-time object pose and reattempt the grasp.
- **p. 8 / C. Can-in-Mug Experiment - extractive body cue:** Successful execution hinges on precise pose estimation for both objects, as any noise in their poses can lead to failure.
- **p. 7 / B. Bimanual Handover Experiment - extractive body cue:** Inaccurate tracking results could lead to collision during the handover.
- **p. 9 / VI. RELATED Works - extractive body cue:** More recent works aim to overcome some of these limitations.
- **p. 9 / VI. RELATED Works - extractive body cue:** While model-free approaches [65, 69, 54] exist, they fall outside the scope of this work.
- **p. 5 / A. Multi-embodied Dataset - extractive body cue:** V) demonstrate robust performance and eliminate the need for costly real-world data collection,

- **Evidence anchors reviewed:** datasets p. 5 (A. Multi-embodied Dataset), p. 5 (A. Multi-embodied Dataset), p. 7 (experiment), p. 7 (experiment), p. 8 (B. Bimanual Handover Experiment), p. 8 (B. Bimanual Handover Experiment), metrics p. 8 (B. Bimanual Handover Experiment), p. 8 (B. Bimanual Handover Experiment), p. 9 (C. Can-in-Mug Experiment), p. 7 (experiment), p. 7 (experiment), p. 9 (C. Can-in-Mug Experiment), baselines p. 7 (experiment), p. 7 (experiment), p. 8 (B. Bimanual Handover Experiment), p. 5 (A. Multi-embodied Dataset), p. 5 (A. Multi-embodied Dataset), results p. 7 (experiment), p. 7 (experiment), p. 8 (B. Bimanual Handover Experiment), p. 8 (B. Bimanual Handover Experiment), p. 9 (C. Can-in-Mug Experiment), p. 5 (A. Multi-embodied Dataset).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Our results show that \V-HOP consistently outperforms FoundationPose in both ADD and ADD-S metrics under different levels of occlusion. ‘These results underscore the importance of integrating visual and haptic information ... (p. 7, experiment).
- **Metric evidence:** V-HOP achieves 1 32% lower ADD-S error compared to NeuralFeels and has a similar ADD-S-0.1d score. (p. 7, experiment).
- **Baseline/ablation evidence:** V-HOP achieves 1 32% lower ADD-S error compared to NeuralFeels and has a similar ADD-S-0.1d score. (p. 7, experiment).
- **Failure/negative evidence:** 1) If the grasp attempt fails, the robot must detect the failure based on the real-time object pose and reattempt the grasp. (p. 7, B. Bimanual Handover Experiment).
