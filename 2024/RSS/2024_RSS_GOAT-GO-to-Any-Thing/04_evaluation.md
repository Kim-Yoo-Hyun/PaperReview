# Evaluation - GOAT: GO to Any Thing

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p073.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p073.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (V. RESULTS), p. 5 (V. RESULTS), p. 8 (Figure/Table caption), p. 4 (Figure/Table caption)): GOAT w/o memory achieves 61% success rate with an SPL of only 0.19 compared to the 0.64 of GOAT.

## Evaluation Body Digest

- **p. 5 / V. RESULTS - extractive body cue:** We evaluate the ability of the GOAT agent to tackle the GOAT task, i.e., reach a sequence of unseen multimodal object instances in unseen environments.
- **p. 5 / V. RESULTS - extractive body cue:** To generate an episode within a home, we sampled a random sequence of 5-10 goals split equally among language, image, and category goals among all ...
- **p. 5 / V. RESULTS - extractive body cue:** GOAT w/o memory achieves 61% success rate with an SPL of only 0.19 compared to the 0.64 of GOAT.
- **p. 5 / V. RESULTS - extractive body cue:** It has to re-explore the environment with every goal, explaining the low SPL and low success rate due to many time-outs.
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6. Navigation performance based on sequential goal count. GOAT performance improves with experience in the environment: from a 60% success rate (0.2 SPL) at ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 7. Online evaluation qualitative trajectories. We compare methods on the same sequence of 5 goals (top) in the same environment. GOAT localizes all goals ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3. Perception and memory update. The perception system processes RGB-D input to infill depth, segment object instances, project them into a top-down semantic map, ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4. (A) Object Instance Memory. We cluster object detections, along with image views in which they were observed, into instances using their location in ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mobile base와 one/two-arm manipulation environment.
- **Input boundary:** egocentric RGB-D, language/task goal, base-arm proprioception.
- **Output/decision under evaluation:** base motion plus arm/gripper action.
- **Primary target:** long-horizon task success, reachability, collision과 recovery.
- **Detected evaluation headings:** V. RESULTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| V. RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | GOAT w/o memory achieves 61% success rate with an SPL of only 0.19 compared to the 0.64 of GOAT. | p. 5 (V. RESULTS) |
| V. RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | GOAT achieves 83% average success rate (94% for object categories, 86% for image goals, and 68% for language goals). | p. 5 (V. RESULTS) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 6. Navigation performance based on sequential goal count. GOAT performance improves with experience in the environment: from a 60% success rate (0.2 SPL) ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 3. Perception and memory update. The perception system processes RGB-D input to infill depth, segment object instances, project them into a top-down semantic ... | p. 4 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / V. RESULTS - extractive body cue:** We evaluate the ability of the GOAT agent to tackle the GOAT task, i.e., reach a sequence of unseen multimodal object instances in unseen environments.
- **p. 5 / V. RESULTS - extractive body cue:** To generate an episode within a home, we sampled a random sequence of 5-10 goals split equally among language, image, and category goals among all ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. GOAT (GO to Any Thing) task. The GOAT task requires lifelong learning, meaning taking advantage of past experience in the same environment, for ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. GOAT system overview. The perception system detects and localizes object instances, the global policy outputs high-level navigation commands depending on whether the robot ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3. Perception and memory update. The perception system processes RGB-D input to infill depth, segment object instances, project them into a top-down semantic map, ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4. (A) Object Instance Memory. We cluster object detections, along with image views in which they were observed, into instances using their location in ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5. "In-the-wild" evaluation. We deploy the GOAT navigation policy in 9 visually diverse homes and evaluate in on reaching 200+ different object instances as ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6. Navigation performance based on sequential goal count. GOAT performance improves with experience in the environment: from a 60% success rate (0.2 SPL) at ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 7. Online evaluation qualitative trajectories. We compare methods on the same sequence of 5 goals (top) in the same environment. GOAT localizes all goals ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate the ability of the GOAT agent to tackle the GOAT task, i.e., reach a sequence of unseen multimodal object instances in unseen ... | embodiment, simulator version and control stack | p. 5 (V. RESULTS), p. 5 (V. RESULTS) |
| Task/environment | To generate an episode within a home, we sampled a random sequence of 5-10 goals split equally among language, image, and category goals among ... | reset, timeout, object/scene variation | p. 5 (V. RESULTS) |
| Observation/sensor | egocentric RGB-D, language/task goal, base-arm proprioception | calibration, preprocessing, privileged input | p. 3 (IV. GOAT METHOD), p. 3 (IV. GOAT METHOD) |
| Output/decision | base motion plus arm/gripper action | action frame, controller and termination | p. 4 (IV. GOAT METHOD), p. 4 (IV. GOAT METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| GOAT w/o memory achieves 61% success rate with an SPL of only 0.19 compared to the 0.64 of GOAT. | definition/direction/unit from same section | p. 5 (V. RESULTS) |
| It has to re-explore the environment with every goal, explaining the low SPL and low success rate due to many time-outs. | definition/direction/unit from same section | p. 5 (V. RESULTS) |
| Fig. 6. Navigation performance based on sequential goal count. GOAT performance improves with experience in the environment: from a 60% success rate (0.2 SPL) ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Fig. 7. Online evaluation qualitative trajectories. We compare methods on the same sequence of 5 goals (top) in the same environment. GOAT localizes all ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Fig. 3. Perception and memory update. The perception system processes RGB-D input to infill depth, segment object instances, project them into a top-down semantic ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Fig. 4. (A) Object Instance Memory. We cluster object detections, along with image views in which they were observed, into instances using their location ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| GOAT w/o memory achieves 61% success rate with an SPL of only 0.19 compared to the 0.64 of GOAT. | comparison identity and matched condition | p. 5 (V. RESULTS) |
| We report evaluation metrics per goal within an episode with two standard deviation error bars. b) Baselines: We compare GOAT to three baselines: 1. | comparison identity and matched condition | p. 5 (V. RESULTS) |
| Fig. 6. Navigation performance based on sequential goal count. GOAT performance improves with experience in the environment: from a 60% success rate (0.2 SPL) ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Fig. 7. Online evaluation qualitative trajectories. We compare methods on the same sequence of 5 goals (top) in the same environment. GOAT localizes all ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Conversely, GOAT without memory shows no improvement from experience, while COW benefits but plateaus at much lower performance. | component/input/data sensitivity | p. 5 (V. RESULTS) |
| GOAT w/o Memory, an ablation that resets the semantic map and Object Instance Memory after every goal, allowing us to quantify the benefits of ... | component/input/data sensitivity | p. 5 (V. RESULTS) |
| Fig. 7. Online evaluation qualitative trajectories. We compare methods on the same sequence of 5 goals (top) in the same environment. GOAT localizes all ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| This enables GOAT to distinguish between different instances of the same category to enable navigation to targets specified by images and fine-grained language descriptions. | GOAT w/o memory achieves 61% success rate with an SPL of only 0.19 compared to the 0.64 of GOAT. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (V. RESULTS), p. 5 (V. RESULTS), p. 8 (Figure/Table caption), p. 4 (Figure/Table caption) |
| Primary metric/result | GOAT achieves 83% average success rate (94% for object categories, 86% for image goals, and 68% for language goals). | numeric claim only at cited anchor | p. 5 (V. RESULTS) |

- Numeric sentences retained from the body:
- **p. 5 / V. RESULTS - extractive body cue:** A demo video qualitatively illustrating our results can be found in the supplementary. a) Experimental Setting: We evaluate the GOAT agent as well as three ...
- **p. 5 / V. RESULTS - extractive body cue:** GOAT w/o Memory, an ablation that resets the semantic map and Object Instance Memory after every goal, allowing us to quantify the benefits of GOAT's ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | environment is fully explored, failures are almost exclusively due to failures in matching the correct goal. | p. 10 (VII. DISCUSSION) |
| body limitation/failure cue | The most common failure is a language goal being matched against the an object of the correct class, but the wrong instance (i.e. | p. 10 (VII. DISCUSSION) |
| body limitation/failure cue | a) Modularity allows GOAT to Achieve Robust GeneralPurpose Navigation in the Real World: The GOAT system as a whole is a robust navigation platform, ... | p. 8 (VII. DISCUSSION) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| A local policy finally computes actions towards the long-term goal. b) Perception: Figure 3 shows the perception system. | p. 3 (IV. GOAT METHOD) |
| We project the first-person semantic segmentation into a point cloud, bin the point cloud into a 3D semantic voxel map, and finally sum over ... | p. 3 (IV. GOAT METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / VII. DISCUSSION - extractive body cue:** environment is fully explored, failures are almost exclusively due to failures in matching the correct goal.
- **p. 10 / VII. DISCUSSION - extractive body cue:** The most common failure is a language goal being matched against the an object of the correct class, but the wrong instance (i.e.
- **p. 8 / VII. DISCUSSION - extractive body cue:** a) Modularity allows GOAT to Achieve Robust GeneralPurpose Navigation in the Real World: The GOAT system as a whole is a robust navigation platform, achieving ...

- **Evidence anchors reviewed:** datasets p. 5 (V. RESULTS), p. 5 (V. RESULTS), metrics p. 5 (V. RESULTS), p. 5 (V. RESULTS), p. 8 (Figure/Table caption), p. 9 (Figure/Table caption), p. 4 (Figure/Table caption), p. 6 (Figure/Table caption), baselines p. 5 (V. RESULTS), p. 5 (V. RESULTS), p. 8 (Figure/Table caption), p. 9 (Figure/Table caption), results p. 5 (V. RESULTS), p. 5 (V. RESULTS), p. 8 (Figure/Table caption), p. 4 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** GOAT w/o memory achieves 61% success rate with an SPL of only 0.19 compared to the 0.64 of GOAT. (p. 5, V. RESULTS).
- **Metric evidence:** GOAT w/o memory achieves 61% success rate with an SPL of only 0.19 compared to the 0.64 of GOAT. (p. 5, V. RESULTS).
- **Baseline/ablation evidence:** GOAT w/o memory achieves 61% success rate with an SPL of only 0.19 compared to the 0.64 of GOAT. (p. 5, V. RESULTS).
- **Failure/negative evidence:** 68.2). d) Real-World Open-Vocabulary Detection: Limitations and Opportunities: An interesting and noteworthy observation is that despite the rapid advances in open (or large) vocabulary vision-and-language models (VLMs) [37, 43], we ... (p. 10, VII. DISCUSSION).
