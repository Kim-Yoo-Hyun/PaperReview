# Evaluation - Prompting with the Future: Open-World Model Predictive Control with Interactive Digital Twins

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (11 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p145.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p145.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (B. Quantitative results), p. 8 (B. Quantitative results), p. 6 (B. Quantitative results), p. 8 (B. Quantitative results), p. 5 (A. Experimental setup), p. 5 (B. Quantitative results)): As shown in Table Ill, while performance varies across df= ferent tasks due to their diverse requirements, our full method achieves the best results in most of the tasks.

## Evaluation Body Digest

- **p. 5 / A. Experimental setup - extractive body cue:** MOKA [13] chooses the 2D keypoints as intermediate representations for VLM to predict, which are then converted into actions based on the depth information from ...
- **p. 6 / B. Quantitative results - extractive body cue:** As for OpenVLA, and 79, while they can perform zero-shot on simple tasks due to their training on large-scale robotic datasets, their generalization is limited ...
- **p. 5 / A. Experimental setup - extractive body cue:** For each task, we construct five manipulation scenes, featuring randomized object layouts and different distractors.
- **p. 6 / B. Quantitative results - extractive body cue:** By mirroring possible interactions in the simulated world, our framework provides a flexible and effective way for VLMSs to guide the motion of the robot ...
- **p. 8 / B. Quantitative results - extractive body cue:** + Planning error: When subtasks are not properly defined or the model fails to recognize the current stage, the robot may execute actions incorrectly.
- **p. 8 / B. Quantitative results - extractive body cue:** For example, the robot may attempt to move the gripper directly to the drum without first picking up the drumstick.
- **p. 5 / A. Experimental setup - extractive body cue:** We use the success rate as the evaluation metric.
- **p. 5 / B. Quantitative results - extractive body cue:** ‘Table II compares the success rates of our method against those of the baselines.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** A. Experimental setup (p. 5); B. Quantitative results (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| B. Quantitative results | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table Ill, while performance varies across df= ferent tasks due to their diverse requirements, our full method achieves the best results ... | p. 6 (B. Quantitative results) |
| B. Quantitative results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Lastly, the CEM process significantly improves sampling efficiency, producing action distributions that better align with the goal, which in general contributes the most to ... | p. 8 (B. Quantitative results) |
| B. Quantitative results | EMPIRICAL / REAL-ROBOT OR HARDWARE | PWTF better leverages the reasoning ability of VLM and improves the performance ‘on most of the tasks. | p. 6 (B. Quantitative results) |
| B. Quantitative results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Subtask division improves the performance on tasks that require multi-stage planning. | p. 8 (B. Quantitative results) |
| A. Experimental setup | EMPIRICAL / REAL-ROBOT OR HARDWARE | We use the success rate as the evaluation metric. | p. 5 (A. Experimental setup) |

## Dataset / Benchmark Role

- **p. 5 / A. Experimental setup - extractive body cue:** MOKA [13] chooses the 2D keypoints as intermediate representations for VLM to predict, which are then converted into actions based on the depth information from ...
- **p. 6 / B. Quantitative results - extractive body cue:** As for OpenVLA, and 79, while they can perform zero-shot on simple tasks due to their training on large-scale robotic datasets, their generalization is limited ...
- **p. 5 / A. Experimental setup - extractive body cue:** For each task, we construct five manipulation scenes, featuring randomized object layouts and different distractors.
- **p. 6 / B. Quantitative results - extractive body cue:** By mirroring possible interactions in the simulated world, our framework provides a flexible and effective way for VLMSs to guide the motion of the robot ...
- **p. 8 / B. Quantitative results - extractive body cue:** + Planning error: When subtasks are not properly defined or the model fails to recognize the current stage, the robot may execute actions incorrectly.
- **p. 8 / B. Quantitative results - extractive body cue:** For example, the robot may attempt to move the gripper directly to the drum without first picking up the drumstick.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: Construction of interactive digital twins. Starting from a video scan of the environment, we construct an interactive digital twin that combines mesh-based simulation ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Model Predictive Control through Simulation-Informed Prompting. Given a free-form instrition, our framework first performs high-level planning by generating structured subtasks from multi-view observations. ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: Example on action optimization. We show the action ‘optimization results of one planning step in subtask "wipe the spilled tea", Our digital twin ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: E We highlight some key steps where VLM aligning the gripper from different perspes
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6: Failure analysis. Our main failure cases can be divided into four categories. We show the percentage and provide an ‘example for each failure ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | MOKA [13] chooses the 2D keypoints as intermediate representations for VLM to predict, which are then converted into actions based on the depth information ... | embodiment, simulator version and control stack | p. 5 (A. Experimental setup), p. 6 (B. Quantitative results) |
| Task/environment | As for OpenVLA, and 79, while they can perform zero-shot on simple tasks due to their training on large-scale robotic datasets, their generalization is ... | reset, timeout, object/scene variation | p. 6 (B. Quantitative results), p. 5 (A. Experimental setup) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 3 (III. PROBLEM FORMULATION), p. 4 (A. Construction of Interactive Digital Twins) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 4 (A. Construction of Interactive Digital Twins), p. 5 (C. Motion Planning via Simulation-Informed Prompting) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We use the success rate as the evaluation metric. | definition/direction/unit from same section | p. 5 (A. Experimental setup) |
| ‘Table II compares the success rates of our method against those of the baselines. | definition/direction/unit from same section | p. 5 (B. Quantitative results) |
| + Reconstruction error: ‘The quality of our digital twin depends on the accuracy of camera pose estimation and 3D reconstruction. | definition/direction/unit from same section | p. 8 (B. Quantitative results) |
| ‘Sampling error Execution error Fig. | definition/direction/unit from same section | p. 8 (B. Quantitative results) |
| We show the action ‘optimization results of one planning step in subtask "wipe the spilled tea", Our digital twin could simulate diverse results with ... | definition/direction/unit from same section | p. 6 (B. Quantitative results) |
| PWTF better leverages the reasoning ability of VLM and improves the performance ‘on most of the tasks. | definition/direction/unit from same section | p. 6 (B. Quantitative results) |
| Fig. 2: Construction of interactive digital twins. Starting from a video scan of the environment, we construct an interactive digital twin that combines mesh-based ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We adopt GPT-4o [1] for both our method and the baselines. | comparison identity and matched condition | p. 5 (A. Experimental setup) |
| ‘Table II compares the success rates of our method against those of the baselines. | comparison identity and matched condition | p. 5 (B. Quantitative results) |
| In the "wio CEM" setting, we simply take the mean value of the selected actions without optimizing the action distribution or resampling, | comparison identity and matched condition | p. 6 (B. Quantitative results) |
| For example, the robot may attempt to move the gripper directly to the drum without first picking up the drumstick. | comparison identity and matched condition | p. 8 (B. Quantitative results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To assess the contribution of each component in our frame- ‘work, we begin with the full system and systematically remove each component in turn. | component/input/data sensitivity | p. 6 (B. Quantitative results) |
| In the "wio CEM" setting, we simply take the mean value of the selected actions without optimizing the action distribution or resampling, | component/input/data sensitivity | p. 6 (B. Quantitative results) |
| We validate the effectiveness of our components. | component/input/data sensitivity | p. 8 (B. Quantitative results) |
| For example, the robot may attempt to move the gripper directly to the drum without first picking up the drumstick. | component/input/data sensitivity | p. 8 (B. Quantitative results) |
| For both OpenVLA and 79, we report their performances under a zero-shot setting and after task-specific fine-tuning on 20 expert demonstrations for each task. | component/input/data sensitivity | p. 5 (A. Experimental setup) |
| MOKA [13] chooses the 2D keypoints as intermediate representations for VLM to predict, which are then converted into actions based on the depth information ... | component/input/data sensitivity | p. 5 (A. Experimental setup) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To validate the effectiveness of our framework, in this section, we design eight real-world manipulation tasks that require 6 DoF control, semantic understanding, and ... | As shown in Table Ill, while performance varies across df= ferent tasks due to their diverse requirements, our full method achieves the best results ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (B. Quantitative results), p. 8 (B. Quantitative results), p. 6 (B. Quantitative results), p. 8 (B. Quantitative results), p. 5 (A. Experimental setup), p. 5 (B. Quantitative results) |
| Primary metric/result | Lastly, the CEM process significantly improves sampling efficiency, producing action distributions that better align with the goal, which in general contributes the most to ... | numeric claim only at cited anchor | p. 8 (B. Quantitative results) |

- Numeric sentences retained from the body:
- **p. 5 / A. Experimental setup - extractive body cue:** For the CEM optimization, we use 3 iterations with 90 samples per iteration.
- **p. 5 / A. Experimental setup - extractive body cue:** The planning policies are rolled out twice per scene to consider the randomness in VLM planning, resulting in 10 trials per task in total.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | A task is considered a failure if the robot causes imeversible results or if the maximum step budget or time limit is reached. ‘The ... | p. 5 (A. Experimental setup) |
| body limitation/failure cue | Since Voxposer and MOKA rely on ‘open-vocabulary detectors to detect objects before manipula tion, they fail when the perception system cannot recognize specific object ... | p. 5 (B. Quantitative results) |
| body limitation/failure cue | The failure cases can be categorized into four groups: | p. 8 (B. Quantitative results) |
| body limitation/failure cue | Our main failure cases can be divided into four categories. | p. 8 (B. Quantitative results) |
| body limitation/failure cue | We show the action ‘optimization results of one planning step in subtask "wipe the spilled tea", Our digital twin could simulate diverse results with ... | p. 6 (B. Quantitative results) |
| body limitation/failure cue | We visualize the action optimization process for a single planning step in the "clean up" task in Figure 4, Initially, the digital twin simulates ... | p. 6 (B. Quantitative results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The planning policies are rolled out twice per scene to consider the randomness in VLM planning, resulting in 10 trials per task in total. | p. 5 (A. Experimental setup) |
| We do not assume access to task-specific training data, in-context ‘examples, or hard-coded motion primitives as used in prior work (20, 27, 13, 25]. | p. 3 (III. PROBLEM FORMULATION) |
| Additional implementation details are provided in the supplementary material. | p. 4 (A. Construction of Interactive Digital Twins) |
| Physical simulation: Finally, we integrate a physics simulator 'S [17] equipped with the robot's URDF U to model dynamics lunder interaction, The simulator computes ... | p. 4 (A. Construction of Interactive Digital Twins) |
| We highlight key planning steps where VLM chooses to change the observation view to better assess the results, showing the benefits of our adaptive ... | p. 6 (B. Quantitative results) |
| By mirroring possible interactions in the simulated world, our framework provides a flexible and effective way for VLMSs to guide the motion of the ... | p. 6 (B. Quantitative results) |
| Planning steps __ [=] VIM changes view to cross-vaidate the optimal ation t | p. 7 (B. Quantitative results) |
| 5: E We highlight some key steps where VLM aligning the gripper from different perspes | p. 7 (B. Quantitative results) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / A. Experimental setup - extractive body cue:** A task is considered a failure if the robot causes imeversible results or if the maximum step budget or time limit is reached. ‘The task ...
- **p. 5 / B. Quantitative results - extractive body cue:** Since Voxposer and MOKA rely on ‘open-vocabulary detectors to detect objects before manipula tion, they fail when the perception system cannot recognize specific object parts, ...
- **p. 8 / B. Quantitative results - extractive body cue:** The failure cases can be categorized into four groups:
- **p. 8 / B. Quantitative results - extractive body cue:** Our main failure cases can be divided into four categories.
- **p. 6 / B. Quantitative results - extractive body cue:** We show the action ‘optimization results of one planning step in subtask "wipe the spilled tea", Our digital twin could simulate diverse results with accurate ...
- **p. 6 / B. Quantitative results - extractive body cue:** We visualize the action optimization process for a single planning step in the "clean up" task in Figure 4, Initially, the digital twin simulates a ...

- **PDF anchors reviewed:** datasets p. 5 (A. Experimental setup), p. 6 (B. Quantitative results), p. 5 (A. Experimental setup), p. 6 (B. Quantitative results), p. 8 (B. Quantitative results), p. 8 (B. Quantitative results), metrics p. 5 (A. Experimental setup), p. 5 (B. Quantitative results), p. 8 (B. Quantitative results), p. 8 (B. Quantitative results), p. 6 (B. Quantitative results), p. 6 (B. Quantitative results), baselines p. 5 (A. Experimental setup), p. 5 (B. Quantitative results), p. 6 (B. Quantitative results), p. 8 (B. Quantitative results), results p. 6 (B. Quantitative results), p. 8 (B. Quantitative results), p. 6 (B. Quantitative results), p. 8 (B. Quantitative results), p. 5 (A. Experimental setup), p. 5 (B. Quantitative results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
