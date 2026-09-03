# Evaluation - TactAlign: Human-to-Robot Policy Transfer via Tactile Alignment

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://roboticsconference.org/program/papers/6/; PDF retrieval source: https://roboticsconference.org/program/papers/6/. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 5 (IV. EXPERIMENTS AND RESULTS)): Fig. 8: Lid Closing Task. With randomized grasps, the policy uses touch to perform search, alignment, and closing between the lid and the bottle. We show human data improves generalization ...

## Evaluation Body Digest

- **p. 5 / IV. EXPERIMENTS AND RESULTS - extractive body cue:** The dataset includes 1,472 robot force samples (24:1 train:test split) and 1,527 human force samples used only for evaluation.
- **p. 5 / IV. EXPERIMENTS AND RESULTS - extractive body cue:** For each task, we collect 140-160 human demonstrations, where 100 demonstrations (≈30 minutes) are from the same object seen by the robot ("seen-by-both" object), and ...
- **p. 4 / IV. EXPERIMENTS AND RESULTS - extractive body cue:** Robot demonstrations are collected using Xela sensors Action Sequence Transformer Decoder Attentive Pooling ... ...
- **p. 4 / IV. EXPERIMENTS AND RESULTS - extractive body cue:** Hardware In our experiments, humans wear the OSMO glove [45], which provides three-axis magnetic tactile signals at the fingertips.
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 10: ℓ1 force prediction error (mean ± std) along each axis, averaged over five evaluations. G →R evaluates force prediction on the robot using ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We propose TactAlign, a cross-sensor tactile alignment method for cross-embodiment human-to-robot policy transfer. Given unpaired human (tactile glove) and robot demonstrations, TactAlign uses ...
- **p. 5 / IV. EXPERIMENTS AND RESULTS - extractive body cue:** Successful execution therefore depends on detecting contact onset and reasoning about contact throughout the task as in Fig.
- **p. 5 / IV. EXPERIMENTS AND RESULTS - extractive body cue:** Second & Third: Colors denote normalized raw tactile magnitude (0: no contact, 1: highest force/shear), computed separately for glove and robot data.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** contact-rich manipulation scene.
- **Input boundary:** tactile image/force, vision과 proprioceptive history.
- **Output/decision under evaluation:** grasp/contact action, force command 또는 object motion.
- **Primary target:** slip/contact success, force/pose error와 robustness.
- **Detected evaluation headings:** IV. EXPERIMENTS AND RESULTS (p. 4).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 8: Lid Closing Task. With randomized grasps, the policy uses touch to perform search, alignment, and closing between the lid and the bottle. ... | p. 7 (Figure/Table caption) |
| IV. EXPERIMENTS AND RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Successful execution therefore depends on detecting contact onset and reasoning about contact throughout the task as in Fig. | p. 5 (IV. EXPERIMENTS AND RESULTS) |

## Dataset / Benchmark Role

- **p. 5 / IV. EXPERIMENTS AND RESULTS - extractive body cue:** The dataset includes 1,472 robot force samples (24:1 train:test split) and 1,527 human force samples used only for evaluation.
- **p. 5 / IV. EXPERIMENTS AND RESULTS - extractive body cue:** For each task, we collect 140-160 human demonstrations, where 100 demonstrations (≈30 minutes) are from the same object seen by the robot ("seen-by-both" object), and ...
- **p. 4 / IV. EXPERIMENTS AND RESULTS - extractive body cue:** Robot demonstrations are collected using Xela sensors Action Sequence Transformer Decoder Attentive Pooling ... ...
- **p. 4 / IV. EXPERIMENTS AND RESULTS - extractive body cue:** Hardware In our experiments, humans wear the OSMO glove [45], which provides three-axis magnetic tactile signals at the fingertips.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We propose TactAlign, a cross-sensor tactile alignment method for cross-embodiment human-to-robot policy transfer. Given unpaired human (tactile glove) and robot demonstrations, TactAlign uses ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: Tactile Alignment Overview. Our method consists of two stages: self-supervised representation learning and cross-embodiment alignment via pseudo-pairs. We use a learnable length-1 query ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Red and blue indicate two subsets of the source distribution. The left side of each of the three panels shows the provided training ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4: H2R Action Policy. Given either human or robot inputs, the shared policy follows a color-coded structure, representing robot, human, and shared modules. Human ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 5: Tactile Features UMAP Projections. First: Rectified flow maps the glove latent distribution to overlap with the robot distribution. Second & Third: Colors denote ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 6: Pivoting Task. The task begins in a non-contact state and transitions to pivoting upon contact detection via tactile feedback, with the goal of ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7: Insertion Task. With randomized grasps, the policy leverages tactile feedback to perform search, alignment, and insertion of the adapter into the outlet. We ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 8: Lid Closing Task. With randomized grasps, the policy uses touch to perform search, alignment, and closing between the lid and the bottle. We ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The dataset includes 1,472 robot force samples (24:1 train:test split) and 1,527 human force samples used only for evaluation. | embodiment, simulator version and control stack | p. 5 (IV. EXPERIMENTS AND RESULTS), p. 5 (IV. EXPERIMENTS AND RESULTS) |
| Task/environment | For each task, we collect 140-160 human demonstrations, where 100 demonstrations (≈30 minutes) are from the same object seen by the robot ("seen-by-both" object), ... | reset, timeout, object/scene variation | p. 5 (IV. EXPERIMENTS AND RESULTS), p. 4 (IV. EXPERIMENTS AND RESULTS) |
| Observation/sensor | tactile image/force, vision과 proprioceptive history | calibration, preprocessing, privileged input | p. 1 (I. INTRODUCTION), p. 2 (III. METHODOLOGY) |
| Output/decision | grasp/contact action, force command 또는 object motion | action frame, controller and termination | p. 2 (I. INTRODUCTION), p. 4 (III. METHODOLOGY) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 10: ℓ1 force prediction error (mean ± std) along each axis, averaged over five evaluations. G →R evaluates force prediction on the robot ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Fig. 1: We propose TactAlign, a cross-sensor tactile alignment method for cross-embodiment human-to-robot policy transfer. Given unpaired human (tactile glove) and robot demonstrations, TactAlign ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Successful execution therefore depends on detecting contact onset and reasoning about contact throughout the task as in Fig. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS AND RESULTS) |
| Second & Third: Colors denote normalized raw tactile magnitude (0: no contact, 1: highest force/shear), computed separately for glove and robot data. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS AND RESULTS) |
| Fig. 3: Red and blue indicate two subsets of the source distribution. The left side of each of the three panels shows the provided ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Fig. 15: Norm of raw sensor signal observations from the human glove [45] and the robot Xela sensor. The red dotted vertical line indicates ... | definition/direction/unit from same section | p. 15 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 10: ℓ1 force prediction error (mean ± std) along each axis, averaged over five evaluations. G →R evaluates force prediction on the robot ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Fig. 8: Lid Closing Task. With randomized grasps, the policy uses touch to perform search, alignment, and closing between the lid and the bottle. ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Fig. 6: Pivoting Task. The task begins in a non-contact state and transitions to pivoting upon contact detection via tactile feedback, with the goal ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 6: Pivoting Task. The task begins in a non-contact state and transitions to pivoting upon contact detection via tactile feedback, with the goal ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| Fig. 10: ℓ1 force prediction error (mean ± std) along each axis, averaged over five evaluations. G →R evaluates force prediction on the robot ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our method consists of two stages: self-supervised representation learning and cross-embodiment alignment via pseudo-pairs. | Fig. 8: Lid Closing Task. With randomized grasps, the policy uses touch to perform search, alignment, and closing between the lid and the bottle. ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 5 (IV. EXPERIMENTS AND RESULTS) |
| Primary metric/result | Successful execution therefore depends on detecting contact onset and reasoning about contact throughout the task as in Fig. | numeric claim only at cited anchor | p. 5 (IV. EXPERIMENTS AND RESULTS) |

- Numeric sentences retained from the body:
- **p. 5 / IV. EXPERIMENTS AND RESULTS - extractive body cue:** 2) Tactile alignment via rectified flow: We use a total of 100 robot demonstrations via kinesthetic teaching and 200 human demonstrations collected from two contact-rich ...
- **p. 5 / IV. EXPERIMENTS AND RESULTS - extractive body cue:** The dataset includes 1,472 robot force samples (24:1 train:test split) and 1,527 human force samples used only for evaluation.
- **p. 4 / III. METHODOLOGY - extractive body cue:** During execution, the policy runs at 10-30 Hz (Appendix E).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Moreover, tactile alignment alone does not address visual discrepancies between human and robot embodiments. | p. 8 (V. LIMITATION) |
| body limitation/failure cue | Incorporating vision and other modalities into a unified multi-modal policy is also an important direction for future work. | p. 8 (V. LIMITATION) |
| body limitation/failure cue | Fig. 3: Red and blue indicate two subsets of the source distribution. The left side of each of the three panels shows the provided ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | We use Manus glove [25] with OSMO tactile sensors [45] for robust hand pose estimation under visual occlusions from the lamp shade and light ... | p. 5 (IV. EXPERIMENTS AND RESULTS) |
| body limitation/failure cue | We record fingertip poses only, as the Manus glove does not provide wrist pose information. | p. 5 (IV. EXPERIMENTS AND RESULTS) |
| body limitation/failure cue | Fig. 8: Lid Closing Task. With randomized grasps, the policy uses touch to perform search, alignment, and closing between the lid and the bottle. ... | p. 7 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Index Action Token Action Token Ring Ring or MLP Proprio Encoder ODE Solver Fig. | p. 4 (IV. EXPERIMENTS AND RESULTS) |
| The proprioceptive encoder takes fingertip locations in yellow dots and wrist orientation. | p. 4 (IV. EXPERIMENTS AND RESULTS) |
| Second & Third: Colors denote normalized raw tactile magnitude (0: no contact, 1: highest force/shear), computed separately for glove and robot data. | p. 5 (IV. EXPERIMENTS AND RESULTS) |
| 1) Tactile self-supervised learning: Both human and robot tactile encoders are trained using a combination of play data (≈10 minutes) and an in-domain tactile ... | p. 5 (IV. EXPERIMENTS AND RESULTS) |
| 2 left) is based on JEPA [2] with the decoder adapted from the online probe module in [13, 34]. | p. 3 (III. METHODOLOGY) |
| We use a learnable length-1 query between the encoder and decoder to produce a fixed-dimensional latent representation via cross-attention pooling. | p. 3 (III. METHODOLOGY) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / V. LIMITATION - extractive body cue:** Moreover, tactile alignment alone does not address visual discrepancies between human and robot embodiments.
- **p. 8 / V. LIMITATION - extractive body cue:** Incorporating vision and other modalities into a unified multi-modal policy is also an important direction for future work.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Red and blue indicate two subsets of the source distribution. The left side of each of the three panels shows the provided training ...
- **p. 5 / IV. EXPERIMENTS AND RESULTS - extractive body cue:** We use Manus glove [25] with OSMO tactile sensors [45] for robust hand pose estimation under visual occlusions from the lamp shade and light bulb.
- **p. 5 / IV. EXPERIMENTS AND RESULTS - extractive body cue:** We record fingertip poses only, as the Manus glove does not provide wrist pose information.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 8: Lid Closing Task. With randomized grasps, the policy uses touch to perform search, alignment, and closing between the lid and the bottle. We ...

- **Evidence anchors reviewed:** datasets p. 5 (IV. EXPERIMENTS AND RESULTS), p. 5 (IV. EXPERIMENTS AND RESULTS), p. 4 (IV. EXPERIMENTS AND RESULTS), p. 4 (IV. EXPERIMENTS AND RESULTS), metrics p. 8 (Figure/Table caption), p. 1 (Figure/Table caption), p. 5 (IV. EXPERIMENTS AND RESULTS), p. 5 (IV. EXPERIMENTS AND RESULTS), p. 4 (Figure/Table caption), p. 15 (Figure/Table caption), baselines p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), results p. 7 (Figure/Table caption), p. 5 (IV. EXPERIMENTS AND RESULTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** The dataset includes 1,472 robot force samples (24:1 train:test split) and 1,527 human force samples used only for evaluation. (p. 5, IV. EXPERIMENTS AND RESULTS).
- **Metric evidence:** Successful execution therefore depends on detecting contact onset and reasoning about contact throughout the task as in Fig. (p. 5, IV. EXPERIMENTS AND RESULTS).
- **Baseline/ablation evidence:** Successful execution therefore depends on detecting contact onset and reasoning about contact throughout the task as in Fig. (p. 5, IV. EXPERIMENTS AND RESULTS).
- **Failure/negative evidence:** Without alignment, the success rate is also 0%, with failures primarily arising from jamming, from which the policy cannot recover, often leading to complete unscrewing of the light bulb. (p. 7, 8. The pivoting and insertion).
