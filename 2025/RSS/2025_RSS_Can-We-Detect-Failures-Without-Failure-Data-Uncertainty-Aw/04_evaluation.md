# Evaluation - Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for Imitation Learning Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p073.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p073.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 14 (Figure/Table caption)): Fig. 5: Quantitative results for the robot hardware experiments across two tasks with policies trained using FM and DP. We consider two different ways to compute the CP band: "setting-lependent" ...

## Evaluation Body Digest

- **p. 7 / V. EXPERIMENTS - extractive body cue:** significantly fewer rollouts in the robot hardware tasks (i.e., 50 rollouts) compared to the simulation tasks (i.e., 2000 rollouts)
- **p. 5 / V. EXPERIMENTS - extractive body cue:** We test our two-stage failure detection framework in both simulation and on robot hardware.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** In the robot hardware experiments, we consider two tasks on a bimanual Franka Emika Panda robot station that are significantly more challenging: FoldRedTowel and CleanUpSpill ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Due to the long STAC inference time (even after parallelization) and resulting high system latency, we omit its comparison on the two robot hardware tasks.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** 5: Quantitative results for the robot hardware experiments across two tasks with policies trained using FM and DP.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** 4: Quantitative failure detection results for simulation tasks on FM policy (best, second) third); results with TPR and TNR are in Fig.
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: Robot hardware experiment scenarios. (Top row) FoldRedTowel with Disturbance: In (b), the human pulls the towel from the position in (a) towards the ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Instead, we incorporate their proposed OOD detection method as a post-hoc scalar score in the first stage of FAIL-Detect to construct a fair baseline.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** V. EXPERIMENTS (p. 5); C. Experimental Details (p. 13); evaluation (p. 16).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 5: Quantitative results for the robot hardware experiments across two tasks with policies trained using FM and DP. We consider two different ways ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 4: Quantitative failure detection results for simulation tasks on FM policy (best, second) third); results with TPR and TNR are in Fig. 11 ... | p. 6 (Figure/Table caption) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | We omit comparison against ensembles [31], a popular OOD detection technique, die to RND having shown improved performance ‘over ensembles in prior work {13} ... | p. 7 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | {ask as both FM and DP policies achieve 100% soces, 5 for Can, which hes the shortest ask completion time. | p. 5 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The learned methods also achieve the fastest detection time, with one ofthe learned methods always getting the best overall detection time in all but ... | p. 6 (V. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 7 / V. EXPERIMENTS - extractive body cue:** significantly fewer rollouts in the robot hardware tasks (i.e., 50 rollouts) compared to the simulation tasks (i.e., 2000 rollouts)
- **p. 5 / V. EXPERIMENTS - extractive body cue:** We test our two-stage failure detection framework in both simulation and on robot hardware.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** In the robot hardware experiments, we consider two tasks on a bimanual Franka Emika Panda robot station that are significantly more challenging: FoldRedTowel and CleanUpSpill ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Due to the long STAC inference time (even after parallelization) and resulting high system latency, we omit its comparison on the two robot hardware tasks.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** 5: Quantitative results for the robot hardware experiments across two tasks with policies trained using FM and DP.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** 4: Quantitative failure detection results for simulation tasks on FM policy (best, second) third); results with TPR and TNR are in Fig.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: Robot hardware experiment scenarios. (Top row) FoldRedTowel with Disturbance: In (b), the human pulls the towel from the position in (a) towards the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: Quantitative failure detection results for simulation tasks on FM policy (best, second) third); results with TPR and TNR are in Fig. 11 ‘and ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Quantitative results for the robot hardware experiments across two tasks with policies trained using FM and DP. We consider two different ways to ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6: Qualitative results of failure detection scores overlaid with CP bands. The curves are colored by the ground truth success/ailure status
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 7: Physical interpretation of logy, the most successful and robust learned score method. Failed trajectory scores are in red and successful ones are in ...
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 8: The on-robot experimental setings. (Top row) FoldRedTowek: starting with a flat towel, the two arms need to frst fold the towel along the ...
- **p. 15 / Figure/Table caption - extractive body cue:** Fig. 9: Qualitative results of detection scores overlaid with CP hands on the real FoldRedTowel OOD task. The layout is the same as
- **p. 15 / Figure/Table caption - extractive body cue:** Fig. 6. We notice that spikes of scores computed on filed trajectories are more evident for the learnt logp20 and RND than for the post-hoc ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | significantly fewer rollouts in the robot hardware tasks (i.e., 50 rollouts) compared to the simulation tasks (i.e., 2000 rollouts) | embodiment, simulator version and control stack | p. 7 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Task/environment | We test our two-stage failure detection framework in both simulation and on robot hardware. | reset, timeout, object/scene variation | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 1 (1. INTRODUCTION), p. 3 (III. PROBLEM FORMULATION) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 1 (1. INTRODUCTION), p. 3 (III. PROBLEM FORMULATION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 4: Quantitative failure detection results for simulation tasks on FM policy (best, second) third); results with TPR and TNR are in Fig. 11 ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Fig. 3: Robot hardware experiment scenarios. (Top row) FoldRedTowel with Disturbance: In (b), the human pulls the towel from the position in (a) towards ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Instead, we incorporate their proposed OOD detection method as a post-hoc scalar score in the first stage of FAIL-Detect to construct a fair baseline. | definition/direction/unit from same section | p. 6 (V. EXPERIMENTS) |
| Weighted accuracy represents how well a method matches the true success / failure distibution. | definition/direction/unit from same section | p. 7 (V. EXPERIMENTS) |
| The balanced accuracy metric equally represents classes in an imbalanced dataset (eg. few successful rollouts in an OOD setting). | definition/direction/unit from same section | p. 7 (V. EXPERIMENTS) |
| We refer to Appendix C for more details 6n policy training, the CP band calibration procedure, and the learned scalar score architectures. | definition/direction/unit from same section | p. 5 (V. EXPERIMENTS) |
| Fig. 6: Qualitative results of failure detection scores overlaid with CP bands. The curves are colored by the ground truth success/ailure status | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Fig. 7: Physical interpretation of logy, the most successful and robust learned score method. Failed trajectory scores are in red and successful ones are ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 5: Quantitative results for the robot hardware experiments across two tasks with policies trained using FM and DP. We consider two different ways ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| In comparison, the baselines STAC and PCA-kmeans reach top-1 performance in 3/16 and 0/16 cases, respectively. | comparison identity and matched condition | p. 6 (V. EXPERIMENTS) |
| »b) Baselines: We baseline FAIL-Detect against STAC [1] and PCA-kmeans [34] as SOTA approaches in success-based failure detection for generative imitation learning policies STAC ... | comparison identity and matched condition | p. 6 (V. EXPERIMENTS) |
| Due to the high human time cost of performing realrobot rollouts, we evaluate FAIL-Detect and the baselines on | comparison identity and matched condition | p. 7 (V. EXPERIMENTS) |
| Fig. 3: Robot hardware experiment scenarios. (Top row) FoldRedTowel with Disturbance: In (b), the human pulls the towel from the position in (a) towards ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We did not employ the VLM component of the STAC failure detector to remain as real-time feasible as possible. | component/input/data sensitivity | p. 6 (V. EXPERIMENTS) |
| visual encoded features jointly trained with the policy on the demonstration data, PCA-kmeans first uses PCA to embed the training features and then applies ... | component/input/data sensitivity | p. 7 (V. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Aside from being performant, our method enables faster inference than prior work [1], which requires sampling, ‘multiple robot actions during inference. | Fig. 5: Quantitative results for the robot hardware experiments across two tasks with policies trained using FM and DP. We consider two different ways ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 14 (Figure/Table caption) |
| Primary metric/result | Fig. 4: Quantitative failure detection results for simulation tasks on FM policy (best, second) third); results with TPR and TNR are in Fig. 11 ... | numeric claim only at cited anchor | p. 6 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 7 / V. EXPERIMENTS - extractive body cue:** significantly fewer rollouts in the robot hardware tasks (i.e., 50 rollouts) compared to the simulation tasks (i.e., 2000 rollouts)

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 3: Robot hardware experiment scenarios. (Top row) FoldRedTowel with Disturbance: In (b), the human pulls the towel from the position in (a) towards ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | This performance shows the capacity of failure-free failure detection methods to robustly identify failures across many scenarios. | p. 7 (C. Do failure detections align with human intuition?) |
| body limitation/failure cue | 2) Calibrate time-varying thresholds 1, based on a CP band. ‘The final decision D(r:8) = 1(Dry(Ar.Or:6) > me) raises a failure flag if the ... | p. 3 (IV. FAILURE DETECTION FRAMEWORK) |
| body limitation/failure cue | How performant is failure detection without failure data? | p. 7 (C. Do failure detections align with human intuition?) |
| body limitation/failure cue | and higher failure/suecess separation. | p. 8 (C. Do failure detections align with human intuition?) |
| body limitation/failure cue | What is the impact of leamed vs. post-hoc scores on failure detection? | p. 8 (C. Do failure detections align with human intuition?) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Due to the long STAC inference time (even after parallelization) and resulting high system latency, we omit its comparison on the two robot hardware ... | p. 6 (V. EXPERIMENTS) |
| Note we do not present STAC here as it was slow to run on hardware in real-time. | p. 7 (V. EXPERIMENTS) |
| visual encoded features jointly trained with the policy on the demonstration data, PCA-kmeans first uses PCA to embed the training features and then applies ... | p. 7 (V. EXPERIMENTS) |
| We test our two-stage failure detection framework in both simulation and on robot hardware. | p. 5 (V. EXPERIMENTS) |
| In the robot hardware experiments, we consider two tasks on a bimanual Franka Emika Panda robot station that are significantly more challenging: FoldRedTowel and ... | p. 5 (V. EXPERIMENTS) |
| We reproduce the method and adopt hyperparameters used in their push-T example, where we generate a batch of 256 action predictions per time step. | p. 6 (V. EXPERIMENTS) |
| Let g(Ar / Or) denote the generator, where O, represents the environment observation (e.g. image features and robot states) at time f, and g ... | p. 3 (III. PROBLEM FORMULATION) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: Robot hardware experiment scenarios. (Top row) FoldRedTowel with Disturbance: In (b), the human pulls the towel from the position in (a) towards the ...
- **p. 7 / C. Do failure detections align with human intuition? - extractive body cue:** This performance shows the capacity of failure-free failure detection methods to robustly identify failures across many scenarios.
- **p. 3 / IV. FAILURE DETECTION FRAMEWORK - extractive body cue:** 2) Calibrate time-varying thresholds 1, based on a CP band. ‘The final decision D(r:8) = 1(Dry(Ar.Or:6) > me) raises a failure flag if the sealar ...
- **p. 7 / C. Do failure detections align with human intuition? - extractive body cue:** How performant is failure detection without failure data?
- **p. 8 / C. Do failure detections align with human intuition? - extractive body cue:** and higher failure/suecess separation.
- **p. 8 / C. Do failure detections align with human intuition? - extractive body cue:** What is the impact of leamed vs. post-hoc scores on failure detection?

- **PDF anchors reviewed:** datasets p. 7 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), metrics p. 6 (Figure/Table caption), p. 5 (Figure/Table caption), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), baselines p. 7 (Figure/Table caption), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 5 (Figure/Table caption), results p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 14 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
