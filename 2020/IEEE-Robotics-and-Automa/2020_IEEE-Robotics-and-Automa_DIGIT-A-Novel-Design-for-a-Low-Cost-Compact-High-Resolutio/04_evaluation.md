# Evaluation - DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/LRA.2020.2977257; PDF retrieval source: https://doi.org/10.1109/LRA.2020.2977257. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS)): This result is in agreement with previous results in [17], where learned models outperform simple handtuned controllers.

## Evaluation Body Digest

- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** To validate our modeling choices, we measure the prediction error on a standard benchmark for video prediction, the BAIR robot pushing dataset [36], in addition ...
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** In both datasets, we use 64 × 64 images and compare prediction performance with CDNA [35] used for tactile servoing in [17] in terms of ...
- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** A fixed P matrix can only be optimal in some of the operating regions but not all of them, especially at the boundary of the ...
- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** LAMBETA et al.: DIGIT: A NOVEL DESIGN FOR A LOW-COST COMPACT HIGH-RESOLUTION TACTILE SENSOR 7 0 2 4 6 8 10 0 10 20 30 ...
- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** It can be seen how the MPC controller can move the marble to reach the goal quite accurately. from the learned model successfully rolling the ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3: Object under test and corresponding raw measurements taken using DIGIT. The measurements taken from DIGIT clearly capture sub-millimeters structures. relatively bulky form factors, ...
- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** This result is in agreement with previous results in [17], where learned models outperform simple handtuned controllers.
- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** We hypothesize that improving the low level controller and collecting more data for improving the learned model will help in decreasing the number of marbles ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** contact-rich manipulation scene.
- **Input boundary:** tactile image/force, vision과 proprioceptive history.
- **Output/decision under evaluation:** grasp/contact action, force command 또는 object motion.
- **Primary target:** slip/contact success, force/pose error와 robustness.
- **Detected evaluation headings:** V. EXPERIMENTAL RESULTS (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| V. EXPERIMENTAL RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | This result is in agreement with previous results in [17], where learned models outperform simple handtuned controllers. | p. 7 (V. EXPERIMENTAL RESULTS) |
| V. EXPERIMENTAL RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | We hypothesize that improving the low level controller and collecting more data for improving the learned model will help in decreasing the number of ... | p. 7 (V. EXPERIMENTAL RESULTS) |
| V. EXPERIMENTAL RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | These results are shown in Table III. | p. 6 (V. EXPERIMENTAL RESULTS) |
| V. EXPERIMENTAL RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | In both datasets, we use 64 × 64 images and compare prediction performance with CDNA [35] used for tactile servoing in [17] in terms ... | p. 6 (V. EXPERIMENTAL RESULTS) |

## Dataset / Benchmark Role

- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** To validate our modeling choices, we measure the prediction error on a standard benchmark for video prediction, the BAIR robot pushing dataset [36], in addition ...
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** In both datasets, we use 64 × 64 images and compare prediction performance with CDNA [35] used for tactile servoing in [17] in terms of ...
- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** A fixed P matrix can only be optimal in some of the operating regions but not all of them, especially at the boundary of the ...
- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** LAMBETA et al.: DIGIT: A NOVEL DESIGN FOR A LOW-COST COMPACT HIGH-RESOLUTION TACTILE SENSOR 7 0 2 4 6 8 10 0 10 20 30 ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: DIGITs mounted on an Allegro multi-finger hand. To validate our sensor design, we learn to manipulate glass marbles between two fingers. [12], [13], ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: Exploded view of a single DIGIT sensor. A) elas- tomer, B) acrylic window, C) snap-fit holder, D) lighting PCB, E) plastic housing, F) ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3: Object under test and corresponding raw measurements taken using DIGIT. The measurements taken from DIGIT clearly capture sub-millimeters structures. relatively bulky form factors, ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 4: DIGIT supports different types of elastomers which can be rapidly replaced thanks to its mechanical design. Here we show readings when touching an ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 5: Surface of the different gels after 5 abrasion passes. In both the gel from [11] and the one from GelSight Inc. the coating ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 6: System diagram of the self-supervised marble detector (top) and model predictive control using the learned dynamics for marble manipulation (bottom). We first used ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 7: Sequences of trajectory predictions produced by our video-predictive model. The first and the third rows are ground truth images. The second and the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 8: Results from real-world marble manipulation. (Top) Euclidean distance (median and 68th percentile) to the desired goal during trajectory rollouts of MPC. The curve ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To validate our modeling choices, we measure the prediction error on a standard benchmark for video prediction, the BAIR robot pushing dataset [36], in ... | embodiment, simulator version and control stack | p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS) |
| Task/environment | In both datasets, we use 64 × 64 images and compare prediction performance with CDNA [35] used for tactile servoing in [17] in terms ... | reset, timeout, object/scene variation | p. 6 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS) |
| Observation/sensor | tactile image/force, vision과 proprioceptive history | calibration, preprocessing, privileged input | p. 1 (I. INTRODUCTION), p. 1 (Abstract) |
| Output/decision | grasp/contact action, force command 또는 object motion | action frame, controller and termination | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In both datasets, we use 64 × 64 images and compare prediction performance with CDNA [35] used for tactile servoing in [17] in terms ... | definition/direction/unit from same section | p. 6 (V. EXPERIMENTAL RESULTS) |
| LAMBETA et al.: DIGIT: A NOVEL DESIGN FOR A LOW-COST COMPACT HIGH-RESOLUTION TACTILE SENSOR 7 0 2 4 6 8 10 0 10 20 ... | definition/direction/unit from same section | p. 7 (V. EXPERIMENTAL RESULTS) |
| To validate our modeling choices, we measure the prediction error on a standard benchmark for video prediction, the BAIR robot pushing dataset [36], in ... | definition/direction/unit from same section | p. 6 (V. EXPERIMENTAL RESULTS) |
| It can be seen how the MPC controller can move the marble to reach the goal quite accurately. from the learned model successfully rolling ... | definition/direction/unit from same section | p. 7 (V. EXPERIMENTAL RESULTS) |
| Figure 3: Object under test and corresponding raw measurements taken using DIGIT. The measurements taken from DIGIT clearly capture sub-millimeters structures. relatively bulky form ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| However, compared to our MPC approach which is virtually parameters-free, this proved significantly more challenging. | comparison identity and matched condition | p. 7 (V. EXPERIMENTAL RESULTS) |
| To test this hyphothesis, we compared our approach against a simple linear proportional controller in keypoints space. | comparison identity and matched condition | p. 7 (V. EXPERIMENTAL RESULTS) |
| Figure 3: Object under test and corresponding raw measurements taken using DIGIT. The measurements taken from DIGIT clearly capture sub-millimeters structures. relatively bulky form ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |
| In comparison, CDNA would take 69 seconds for a single step, making it impractical to use for control. | comparison identity and matched condition | p. 6 (V. EXPERIMENTAL RESULTS) |
| Figure 2: Exploded view of a single DIGIT sensor. A) elas- tomer, B) acrylic window, C) snap-fit holder, D) lighting PCB, E) plastic housing, ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 4: DIGIT supports different types of elastomers which can be rapidly replaced thanks to its mechanical design. Here we show readings when touching ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To better fulfill these requirements, in this paper, we present the design of a novel tactile sensor. | This result is in agreement with previous results in [17], where learned models outperform simple handtuned controllers. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS) |
| Primary metric/result | We hypothesize that improving the low level controller and collecting more data for improving the learned model will help in decreasing the number of ... | numeric claim only at cited anchor | p. 7 (V. EXPERIMENTAL RESULTS) |

- Numeric sentences retained from the body:
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** In both datasets, we use 64 × 64 images and compare prediction performance with CDNA [35] used for tactile servoing in [17] in terms of ...
- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** One challenge of comparing against the proportional controller is that the gains P consists of a 3×8 matrix, which is multiplied against the 3-dimensional displacement ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | This is a very challenging task because it requires controlling the slipping and rolling dynamics of the marble over the small and deformable DIGIT ... | p. 7 (V. EXPERIMENTAL RESULTS) |
| body limitation/failure cue | 3) and the robustness of the gel (Section III-D), we now evaluate the DIGIT in the complex in-hand tactile manipulation task described in Section ... | p. 6 (V. EXPERIMENTAL RESULTS) |
| body limitation/failure cue | (Bottom) Due to control noise, potential planning inaccuracies and the challenging nature of this task, the hand tends to drop marbles over time. | p. 7 (V. EXPERIMENTAL RESULTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In both datasets, we use 64 × 64 images and compare prediction performance with CDNA [35] used for tactile servoing in [17] in terms ... | p. 6 (V. EXPERIMENTAL RESULTS) |
| We repeat each experiments 50 times to compute statistical performance. | p. 7 (V. EXPERIMENTAL RESULTS) |
| In our experiments, we manually tuned the gains based on human expertise and iterative trials. | p. 7 (V. EXPERIMENTAL RESULTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** This is a very challenging task because it requires controlling the slipping and rolling dynamics of the marble over the small and deformable DIGIT surfaces ...
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** 3) and the robustness of the gel (Section III-D), we now evaluate the DIGIT in the complex in-hand tactile manipulation task described in Section IV.
- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** (Bottom) Due to control noise, potential planning inaccuracies and the challenging nature of this task, the hand tends to drop marbles over time.

- **Evidence anchors reviewed:** datasets p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), metrics p. 6 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), p. 3 (Figure/Table caption), baselines p. 7 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), p. 3 (Figure/Table caption), p. 6 (V. EXPERIMENTAL RESULTS), p. 2 (Figure/Table caption), results p. 7 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** LAMBETA et al.: DIGIT: A NOVEL DESIGN FOR A LOW-COST COMPACT HIGH-RESOLUTION TACTILE SENSOR 7 0 2 4 6 8 10 0 10 20 30 Number of actions Euclidean distance ... (p. 7, V. EXPERIMENTAL RESULTS).
- **Metric evidence:** LAMBETA et al.: DIGIT: A NOVEL DESIGN FOR A LOW-COST COMPACT HIGH-RESOLUTION TACTILE SENSOR 7 0 2 4 6 8 10 0 10 20 30 Number of actions Euclidean distance ... (p. 7, V. EXPERIMENTAL RESULTS).
- **Baseline/ablation evidence:** In comparison, CDNA would take 69 seconds for a single step, making it impractical to use for control. (p. 6, V. EXPERIMENTAL RESULTS).
- **Failure/negative evidence:** (Bottom) Due to control noise, potential planning inaccuracies and the challenging nature of this task, the hand tends to drop marbles over time. (p. 7, V. EXPERIMENTAL RESULTS).
