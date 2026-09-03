# Evaluation - Pushing the Limits of Cross-Embodiment Learning for Manipulation and Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p093.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p093.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 9 (VI. ANALYSIS), p. 7 (Figure/Table caption), p. 8 (VI. ANALYSIS), p. 7 (VI. ANALYSIS), p. 5 (V. EVALUATION)): Fig. 6: Does manipulation help navigation? Across three different robots in challenging indoor and outdoor environments, adding manipulation datasets leads to 5 -7% improvement in navigation performance (success % on ...

## Evaluation Body Digest

- **p. 8 / VI. ANALYSIS - extractive body cue:** Across three different robots in challenging indoor and outdoor environments, adding manipulation datasets leads to 5 -7% improvement in navigation performance (success % on y-axis).
- **p. 7 / VI. ANALYSIS - extractive body cue:** Each dataset mixture was evaluated on four different robots across two indoor domains, then averaged to get a success rate.
- **p. 7 / VI. ANALYSIS - extractive body cue:** Three of these robots-the LoCoBot, Jackal, and Unitree Go1-were present in the training dataset, while the DJI Tello is a novel embodiment.
- **p. 9 / VI. ANALYSIS - extractive body cue:** By training our policies with both manipulation and navigation data, heterogeneous cross-embodiment policies can allow robots that require both manipulation and navigation to leverage preexisting ...
- **p. 5 / V. EVALUATION - extractive body cue:** Our goal is to evaluate the performance of heterogeneous cross-embodiment policies in solving real-world manipulation and navigation tasks on a variety of embodiments.
- **p. 9 / VI. ANALYSIS - extractive body cue:** However, small changes in the mobile base can elicit large changes in position of the robot arm with respect to the scene, and the robot ...
- **p. 8 / VI. ANALYSIS - extractive body cue:** We ablate which datasets inside of GNM [5] we co-train with to investigate which types of navigation environments are more conducive to transfer to manipulation.
- **p. 7 / VI. ANALYSIS - extractive body cue:** Training our policy on a manipulation and navigation data split had a 20% greater success rate over 5 tasks compared to training only on manipulation ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mobile base와 one/two-arm manipulation environment.
- **Input boundary:** egocentric RGB-D, language/task goal, base-arm proprioception.
- **Output/decision under evaluation:** base motion plus arm/gripper action.
- **Primary target:** long-horizon task success, reachability, collision과 recovery.
- **Detected evaluation headings:** V. EVALUATION (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 6: Does manipulation help navigation? Across three different robots in challenging indoor and outdoor environments, adding manipulation datasets leads to 5 -7% improvement ... | p. 8 (Figure/Table caption) |
| VI. ANALYSIS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Despite the fact that neither the table nor the egg was seen in the training data of the policy, the robot achieves a 50% ... | p. 9 (VI. ANALYSIS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 5: Does navigation help manipulation? By aligning action coordinate frames, training on navigation and driving datasets results in a 20% improvement across five ... | p. 7 (Figure/Table caption) |
| VI. ANALYSIS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our results show a positive correlation between ratio of the coefficient of determination between data splits and the ratio of the success rates on ... | p. 8 (VI. ANALYSIS) |
| VI. ANALYSIS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Each dataset mixture was evaluated on four different robots across two indoor domains, then averaged to get a success rate. | p. 7 (VI. ANALYSIS) |

## Dataset / Benchmark Role

- **p. 8 / VI. ANALYSIS - extractive body cue:** Across three different robots in challenging indoor and outdoor environments, adding manipulation datasets leads to 5 -7% improvement in navigation performance (success % on y-axis).
- **p. 7 / VI. ANALYSIS - extractive body cue:** Each dataset mixture was evaluated on four different robots across two indoor domains, then averaged to get a success rate.
- **p. 7 / VI. ANALYSIS - extractive body cue:** Three of these robots-the LoCoBot, Jackal, and Unitree Go1-were present in the training dataset, while the DJI Tello is a novel embodiment.
- **p. 9 / VI. ANALYSIS - extractive body cue:** By training our policies with both manipulation and navigation data, heterogeneous cross-embodiment policies can allow robots that require both manipulation and navigation to leverage preexisting ...
- **p. 5 / V. EVALUATION - extractive body cue:** Our goal is to evaluate the performance of heterogeneous cross-embodiment policies in solving real-world manipulation and navigation tasks on a variety of embodiments.
- **p. 9 / VI. ANALYSIS - extractive body cue:** However, small changes in the mobile base can elicit large changes in position of the robot arm with respect to the scene, and the robot ...
- **p. 8 / VI. ANALYSIS - extractive body cue:** We ablate which datasets inside of GNM [5] we co-train with to investigate which types of navigation environments are more conducive to transfer to manipulation.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Heterogeneous cross-embodiment learning. We test the limits of cross-embodiment learning by training a single goal-conditioned policy across 18 manipulation, navigation, and driving datasets. ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: Unifying Manipulation and Navigation. Despite having fundamentally different objectives, similar actions lead to similar transformations in the egocentric observations for both manipulators and ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Policy Architecture. We use separate observation and goal convolutional encoders to tokenize visual observations, which are passed through a Transformer block. The resulting ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: Qualitative examples of the same policy checkpoint deployed on a tabletop manipulator solving the "Cluttered Grasp" task (top), a quadruped navigating to a ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Does navigation help manipulation? By aligning action coordinate frames, training on navigation and driving datasets results in a 20% improvement across five challenging ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6: Does manipulation help navigation? Across three different robots in challenging indoor and outdoor environments, adding manipulation datasets leads to 5 -7% improvement in ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 7: What type of navigation data helps positive transfer? Manipulation policies co-trained with indoor and outdoor navigation data on sidewalks perform better than policies ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 8: Our cross-embodiment policy trained on manipulation and navigation data zero-shot generalizes to a mobile manipulator, suc- ceeding in the "Egg Nav/Pick/Place" task. Datasets ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Across three different robots in challenging indoor and outdoor environments, adding manipulation datasets leads to 5 -7% improvement in navigation performance (success % on ... | embodiment, simulator version and control stack | p. 8 (VI. ANALYSIS), p. 7 (VI. ANALYSIS) |
| Task/environment | Each dataset mixture was evaluated on four different robots across two indoor domains, then averaged to get a success rate. | reset, timeout, object/scene variation | p. 7 (VI. ANALYSIS), p. 7 (VI. ANALYSIS) |
| Observation/sensor | egocentric RGB-D, language/task goal, base-arm proprioception | calibration, preprocessing, privileged input | p. 3 (III. PRELIMINARIES), p. 3 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING) |
| Output/decision | base motion plus arm/gripper action | action frame, controller and termination | p. 5 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 7 (VI. ANALYSIS) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 6: Does manipulation help navigation? Across three different robots in challenging indoor and outdoor environments, adding manipulation datasets leads to 5 -7% improvement ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Each dataset mixture was evaluated on four different robots across two indoor domains, then averaged to get a success rate. | definition/direction/unit from same section | p. 7 (VI. ANALYSIS) |
| Training our policy on a manipulation and navigation data split had a 20% greater success rate over 5 tasks compared to training only on ... | definition/direction/unit from same section | p. 7 (VI. ANALYSIS) |
| Our results show a positive correlation between ratio of the coefficient of determination between data splits and the ratio of the success rates on ... | definition/direction/unit from same section | p. 8 (VI. ANALYSIS) |
| Despite the fact that neither the table nor the egg was seen in the training data of the policy, the robot achieves a 50% ... | definition/direction/unit from same section | p. 9 (VI. ANALYSIS) |
| Our goal is to evaluate the performance of heterogeneous cross-embodiment policies in solving real-world manipulation and navigation tasks on a variety of embodiments. | definition/direction/unit from same section | p. 5 (V. EVALUATION) |
| Fig. 3: Policy Architecture. We use separate observation and goal convolutional encoders to tokenize visual observations, which are passed through a Transformer block. The ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Fig. 2: Unifying Manipulation and Navigation. Despite having fundamentally different objectives, similar actions lead to similar transformations in the egocentric observations for both manipulators ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Training our policy on a manipulation and navigation data split had a 20% greater success rate over 5 tasks compared to training only on ... | comparison identity and matched condition | p. 7 (VI. ANALYSIS) |
| There is a 30% higher gap in performance between goal-conditioned (GC) co-trained policies and manipulation-only policies compared to unconditioned (UC). | comparison identity and matched condition | p. 9 (VI. ANALYSIS) |
| To further examine whether information from the goal image is essential to transferring navigation data to manipulation, we ran an ablation of our method ... | comparison identity and matched condition | p. 8 (VI. ANALYSIS) |
| Due to a difference in the camera lens used by the DJI tello, we noticed that the performance of the drone degraded significantly in ... | comparison identity and matched condition | p. 7 (VI. ANALYSIS) |
| Operating under the assumption that the diffusion policy is powerful enough to model the different possible tasks from the current observation without conditioning on ... | comparison identity and matched condition | p. 8 (VI. ANALYSIS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To further examine whether information from the goal image is essential to transferring navigation data to manipulation, we ran an ablation of our method ... | component/input/data sensitivity | p. 8 (VI. ANALYSIS) |
| Due to a difference in the camera lens used by the DJI tello, we noticed that the performance of the drone degraded significantly in ... | component/input/data sensitivity | p. 7 (VI. ANALYSIS) |
| For the Cluttered Grasp tasks, the gap in performance between the joint navigation-manipulation policy is larger in the out-of-distribution variant than the in-distribution variant. | component/input/data sensitivity | p. 7 (VI. ANALYSIS) |
| Operating under the assumption that the diffusion policy is powerful enough to model the different possible tasks from the current observation without conditioning on ... | component/input/data sensitivity | p. 8 (VI. ANALYSIS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| While the particular training methodology and model architecture are based on prior techniques, the empirical findings are a novel contribution of our work, demonstrating ... | Fig. 6: Does manipulation help navigation? Across three different robots in challenging indoor and outdoor environments, adding manipulation datasets leads to 5 -7% improvement ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 9 (VI. ANALYSIS), p. 7 (Figure/Table caption), p. 8 (VI. ANALYSIS), p. 7 (VI. ANALYSIS), p. 5 (V. EVALUATION) |
| Primary metric/result | Despite the fact that neither the table nor the egg was seen in the training data of the policy, the robot achieves a 50% ... | numeric claim only at cited anchor | p. 9 (VI. ANALYSIS) |

- Numeric sentences retained from the body:
- **p. 7 / VI. ANALYSIS - extractive body cue:** Training our policy on a manipulation and navigation data split had a 20% greater success rate over 5 tasks compared to training only on manipulation ...
- **p. 6 / 6) Can heterogeneous cross-embodiment policies generalize - extractive body cue:** Goal 3 2 1 Robot's Observations Robot's Trajectory
- **p. 6 / 6) Can heterogeneous cross-embodiment policies generalize - extractive body cue:** We evaluate our method on 5 tasks outlined below.
- **p. 6 / 4) Toy Kitchen. A more semantically meaningful environ - extractive body cue:** For navigation, we create a topological map M by recording the robot's observations with a frequency of 4 Hz while moving the robot base throughout ...
- **p. 7 / 4) Toy Kitchen. A more semantically meaningful environ - extractive body cue:** This entire dataset spans 400 trajectories collected over the course of 8 hours.
- **p. 7 / VI. ANALYSIS - extractive body cue:** Training our policy on a manipulation and navigation data split had a 20% greater success rate over 5 tasks compared to training only on manipulation ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Gauging object distance is analogous to testing the robustness to a change in table height in tabletop manipulation, which previous works have identified as ... | p. 7 (VI. ANALYSIS) |
| body limitation/failure cue | This requires the robot to avoid colliding with the shelf as well as gauge its distance to the object, which is fundamentally similar to ... | p. 7 (VI. ANALYSIS) |
| body limitation/failure cue | While we qualitatively observed that these policies had better estimates for the closest node and had less collision with the environment, we acknowledge that ... | p. 8 (VI. ANALYSIS) |
| body limitation/failure cue | However, small changes in the mobile base can elicit large changes in position of the robot arm with respect to the scene, and the ... | p. 9 (VI. ANALYSIS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The action prediction is reshaped into a tensor of size (b, n, 7), while the distance prediction is reshaped into a tensor of size ... | p. 5 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING) |
| While these domains seemingly differ significantly in terms of hardware, observations, and action representations, they contain many similar sensorimotor principles. | p. 2 (I. INTRODUCTION) |
| We use separate observation and goal convolutional encoders to tokenize visual observations, which are passed through a Transformer block. | p. 4 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING) |
| In addition, dt denotes the distance in timesteps from the current observation and goal observation. | p. 5 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING) |
| 4: Qualitative examples of the same policy checkpoint deployed on a tabletop manipulator solving the "Cluttered Grasp" task (top), a quadruped navigating to a ... | p. 6 (6) Can heterogeneous cross-embodiment policies generalize) |
| Note that while goal-conditioned experiments record the proportion of trials in which the robot grasped the correct object, the unconditioned experiments record the proportion ... | p. 8 (VI. ANALYSIS) |
| To investigate our hypothesis that navigation data can help a manipulator understand its position with respect to its goal, we collected a small dataset ... | p. 8 (VI. ANALYSIS) |
| We threshold the magnitude of the policy's action prediction to determine when to run the manipulation policy. | p. 9 (VI. ANALYSIS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / VI. ANALYSIS - extractive body cue:** Gauging object distance is analogous to testing the robustness to a change in table height in tabletop manipulation, which previous works have identified as a ...
- **p. 7 / VI. ANALYSIS - extractive body cue:** This requires the robot to avoid colliding with the shelf as well as gauge its distance to the object, which is fundamentally similar to the ...
- **p. 8 / VI. ANALYSIS - extractive body cue:** While we qualitatively observed that these policies had better estimates for the closest node and had less collision with the environment, we acknowledge that the ...
- **p. 9 / VI. ANALYSIS - extractive body cue:** However, small changes in the mobile base can elicit large changes in position of the robot arm with respect to the scene, and the robot ...

- **Evidence anchors reviewed:** datasets p. 8 (VI. ANALYSIS), p. 7 (VI. ANALYSIS), p. 7 (VI. ANALYSIS), p. 9 (VI. ANALYSIS), p. 5 (V. EVALUATION), p. 9 (VI. ANALYSIS), metrics p. 8 (Figure/Table caption), p. 7 (VI. ANALYSIS), p. 7 (VI. ANALYSIS), p. 8 (VI. ANALYSIS), p. 9 (VI. ANALYSIS), p. 5 (V. EVALUATION), baselines p. 7 (VI. ANALYSIS), p. 9 (VI. ANALYSIS), p. 8 (VI. ANALYSIS), p. 7 (VI. ANALYSIS), p. 8 (VI. ANALYSIS), results p. 8 (Figure/Table caption), p. 9 (VI. ANALYSIS), p. 7 (Figure/Table caption), p. 8 (VI. ANALYSIS), p. 7 (VI. ANALYSIS), p. 5 (V. EVALUATION).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Fig. 5: Does navigation help manipulation? By aligning action coordinate frames, training on navigation and driving datasets results in a 20% improvement across five challenging tabletop manipulation tasks (success % ... (p. 7, Figure/Table caption).
- **Metric evidence:** Our goal is to evaluate the performance of heterogeneous cross-embodiment policies in solving real-world manipulation and navigation tasks on a variety of embodiments. (p. 5, V. EVALUATION).
- **Baseline/ablation evidence:** To further examine whether information from the goal image is essential to transferring navigation data to manipulation, we ran an ablation of our method without goalconditioning. (p. 8, VI. ANALYSIS).
- **Failure/negative evidence:** Gauging object distance is analogous to testing the robustness to a change in table height in tabletop manipulation, which previous works have identified as a common distribution shift artifact leading ... (p. 7, VI. ANALYSIS).
