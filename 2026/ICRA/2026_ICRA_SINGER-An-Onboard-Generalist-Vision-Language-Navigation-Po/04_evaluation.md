# Evaluation - SINGER: An Onboard Generalist Vision-Language Navigation Policy for Drones

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_3.html; PDF retrieval source: https://arxiv.org/pdf/2509.18610. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 5 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS)): The overall success rate of the policy insimulation is also comparable to the results in hardware.

## Evaluation Body Digest

- **p. 6 / VI. EXPERIMENTS - extractive body cue:** Baseline and SINGER On Hardware We evaluate the real-world performance of SINGER against a baseline in six hardware experiments with five trials each, corresponding to ...
- **p. 5 / VI. EXPERIMENTS - extractive body cue:** We evaluate the performance of the SINGER in drone experiments to evaluate its generalization and robustness capabilities in simulation within a 3DGS environment and in ...
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** When deployed in hardware in the hardest evaluation scenario (three unseen semantic queries in an unseen deployment environment) SINGER performs the best overall, keeping all ...
- **p. 7 / VI. EXPERIMENTS - extractive body cue:** The overall success rate of the policy insimulation is also comparable to the results in hardware.
- **p. 7 / VI. EXPERIMENTS - extractive body cue:** The most challenging semantic query tested in hardware was the clock, which SINGER performed the worst on in simulation.
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** We additionally compare against SINGER with no reliance on motion capture in the same environment to demonstrate fully onboard implementation, although this experiment is subject ...
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** The policy is evaluated on successful flight towards the queried object without collisions.
- **p. 7 / VI. EXPERIMENTS - extractive body cue:** Crosshatching direction on unsuccessful trials denotes the reason for failure, where collisions are counted while the policy has the query in-view, while query-not-in-view describes cases ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** VI. EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| VI. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The overall success rate of the policy insimulation is also comparable to the results in hardware. | p. 7 (VI. EXPERIMENTS) |
| VI. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | We include SINGER's results under the same conditions as a testament to its ability to outperform the baseline. | p. 7 (VI. EXPERIMENTS) |
| VI. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | We evaluate the performance of the SINGER in drone experiments to evaluate its generalization and robustness capabilities in simulation within a 3DGS environment and ... | p. 5 (VI. EXPERIMENTS) |
| VI. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The policy is evaluated on successful flight towards the queried object without collisions. | p. 6 (VI. EXPERIMENTS) |
| VI. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Finally, the hardest scenario is designed to evaluate policy performance in a unseen environment and on unseen semantic queries. | p. 6 (VI. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 6 / VI. EXPERIMENTS - extractive body cue:** Baseline and SINGER On Hardware We evaluate the real-world performance of SINGER against a baseline in six hardware experiments with five trials each, corresponding to ...
- **p. 5 / VI. EXPERIMENTS - extractive body cue:** We evaluate the performance of the SINGER in drone experiments to evaluate its generalization and robustness capabilities in simulation within a 3DGS environment and in ...
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** When deployed in hardware in the hardest evaluation scenario (three unseen semantic queries in an unseen deployment environment) SINGER performs the best overall, keeping all ...
- **p. 7 / VI. EXPERIMENTS - extractive body cue:** The overall success rate of the policy insimulation is also comparable to the results in hardware.
- **p. 7 / VI. EXPERIMENTS - extractive body cue:** The most challenging semantic query tested in hardware was the clock, which SINGER performed the worst on in simulation.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. SINGER: pipeline for training and deploying open-vocabulary language conditioned guidance policies in the open world with inference entirely onboard drone hardware. Scene-spanning trajectories ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2. The SINGER data synthesis pipeline. (A.) Time-inverted RRT* based trajectory generation process leveraging semantic Gaussian Splatting. (B.) Natural language conditioning process applied to ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3. Training architecture. SINGER is trained on images consisting of the output logits from CLIPSeg, a pixel-dense semantic segmentation network built on CLIP. At ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4. SINGER evaluated in simulation across three different 3DGS environments. The darkest of each colored bar denotes reaching the goal, while the middle hue ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5. Experimental results comparing SINGER to a yaw-rate PD controlled baseline, and to SINGER with fully onboard sensors. Our policy performs the best given ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Baseline and SINGER On Hardware We evaluate the real-world performance of SINGER against a baseline in six hardware experiments with five trials each, corresponding ... | embodiment, simulator version and control stack | p. 6 (VI. EXPERIMENTS), p. 5 (VI. EXPERIMENTS) |
| Task/environment | We evaluate the performance of the SINGER in drone experiments to evaluate its generalization and robustness capabilities in simulation within a 3DGS environment and ... | reset, timeout, object/scene variation | p. 5 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The overall success rate of the policy insimulation is also comparable to the results in hardware. | definition/direction/unit from same section | p. 7 (VI. EXPERIMENTS) |
| We additionally compare against SINGER with no reliance on motion capture in the same environment to demonstrate fully onboard implementation, although this experiment is ... | definition/direction/unit from same section | p. 6 (VI. EXPERIMENTS) |
| We evaluate the performance of the SINGER in drone experiments to evaluate its generalization and robustness capabilities in simulation within a 3DGS environment and ... | definition/direction/unit from same section | p. 5 (VI. EXPERIMENTS) |
| The policy is evaluated on successful flight towards the queried object without collisions. | definition/direction/unit from same section | p. 6 (VI. EXPERIMENTS) |
| Crosshatching direction on unsuccessful trials denotes the reason for failure, where collisions are counted while the policy has the query in-view, while query-not-in-view describes ... | definition/direction/unit from same section | p. 7 (VI. EXPERIMENTS) |
| Fig. 1. SINGER: pipeline for training and deploying open-vocabulary language conditioned guidance policies in the open world with inference entirely onboard drone hardware. Scene-spanning ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Fig. 3. Training architecture. SINGER is trained on images consisting of the output logits from CLIPSeg, a pixel-dense semantic segmentation network built on CLIP. ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The baseline fails to track the correct semantic query 16.67% of the time (5/30), demonstrating the limited semantic scene understanding of the baseline compared ... | comparison identity and matched condition | p. 6 (VI. EXPERIMENTS) |
| We include SINGER's results under the same conditions as a testament to its ability to outperform the baseline. | comparison identity and matched condition | p. 7 (VI. EXPERIMENTS) |
| The baseline was completely unable to perform without an externally provided true north heading, as the velocity set point requires a reliable heading in ... | comparison identity and matched condition | p. 7 (VI. EXPERIMENTS) |
| The baseline is most similar to [27] in implementation and [28] in deployment. | comparison identity and matched condition | p. 6 (VI. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The policy is evaluated on successful flight towards the queried object without collisions. | component/input/data sensitivity | p. 6 (VI. EXPERIMENTS) |
| When the external true-north is removed from SINGER and it must rely on its internal sensors, SINGER still performs comparably or better than the ... | component/input/data sensitivity | p. 6 (VI. EXPERIMENTS) |
| Without a reliable true-north, the onboard magnetometer is susceptible to varying external magnetic fields induced by heavy machinery nearby. | component/input/data sensitivity | p. 7 (VI. EXPERIMENTS) |
| The baseline was completely unable to perform without an externally provided true north heading, as the velocity set point requires a reliable heading in ... | component/input/data sensitivity | p. 7 (VI. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We summarize our contributions as follows: • We introduce a high-fidelity drone simulator for efficient imitation learning in language-specified drone navigation problems built on ... | The overall success rate of the policy insimulation is also comparable to the results in hardware. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 5 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS) |
| Primary metric/result | We include SINGER's results under the same conditions as a testament to its ability to outperform the baseline. | numeric claim only at cited anchor | p. 7 (VI. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** The CLIPSeg ViT-B/16 patch size is 16×16, corresponding to 42×24 patches of input for the camera image stream.
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** The image processing pipeline runs at 12 -13Hz, the majority of which is the forward pass through CLIPSeg.
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** Results SINGER was tested in simulation in 90 experiments with 10 trials each across six different environments and nine semantic queries.
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** When deployed in hardware in the hardest evaluation scenario (three unseen semantic queries in an unseen deployment environment) SINGER performs the best overall, keeping all ...
- **p. 5 / V. SINGER POLICY ARCHITECTURE AND TRAINING - extractive body cue:** This full network is trained with a loss on the expert demonstrator's motor commands over the 2s trajectory chunks.
- **p. 5 / V. SINGER POLICY ARCHITECTURE AND TRAINING - extractive body cue:** SINGER produces motor commands at 20Hz, but CLIPSeg uses CLIP based on the ViT-B/16 vision transformer model with 86M parameters.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | SINGER performs the best at this experiment difficulty, reaching the goal region 73% of the time, and reaching sub-meter proximity 92.7% of the time ... | p. 6 (VI. EXPERIMENTS) |
| body limitation/failure cue | This results in one more failure case (6/30) vs. the baseline at (5/30) due to tracking the incorrect semantic query, as the drone cannot ... | p. 7 (VI. EXPERIMENTS) |
| body limitation/failure cue | Crosshatching direction on unsuccessful trials denotes the reason for failure, where collisions are counted while the policy has the query in-view, while query-not-in-view describes ... | p. 7 (VI. EXPERIMENTS) |
| body limitation/failure cue | The policy is evaluated on successful flight towards the queried object without collisions. | p. 6 (VI. EXPERIMENTS) |
| body limitation/failure cue | We evaluate the performance of the SINGER in drone experiments to evaluate its generalization and robustness capabilities in simulation within a 3DGS environment and ... | p. 5 (VI. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Baseline and SINGER On Hardware We evaluate the real-world performance of SINGER against a baseline in six hardware experiments with five trials each, corresponding ... | p. 6 (VI. EXPERIMENTS) |
| When deployed in hardware in the hardest evaluation scenario (three unseen semantic queries in an unseen deployment environment) SINGER performs the best overall, keeping ... | p. 6 (VI. EXPERIMENTS) |
| This imposes a significant bottleneck on the inference time of the policy (3Hz on NVIDIA Jetson Orin Nano 8Gb), and is the primary reason ... | p. 5 (V. SINGER POLICY ARCHITECTURE AND TRAINING) |
| At runtime, a semantic query is passed into CLIPSeg along with monocular RGB images. | p. 5 (V. SINGER POLICY ARCHITECTURE AND TRAINING) |
| All trials are depicted, with successful trials above unsuccessful ones. | p. 7 (VI. EXPERIMENTS) |
| The overall success rate of the policy insimulation is also comparable to the results in hardware. | p. 7 (VI. EXPERIMENTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / VI. EXPERIMENTS - extractive body cue:** SINGER performs the best at this experiment difficulty, reaching the goal region 73% of the time, and reaching sub-meter proximity 92.7% of the time with ...
- **p. 7 / VI. EXPERIMENTS - extractive body cue:** This results in one more failure case (6/30) vs. the baseline at (5/30) due to tracking the incorrect semantic query, as the drone cannot maintain ...
- **p. 7 / VI. EXPERIMENTS - extractive body cue:** Crosshatching direction on unsuccessful trials denotes the reason for failure, where collisions are counted while the policy has the query in-view, while query-not-in-view describes cases ...
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** The policy is evaluated on successful flight towards the queried object without collisions.
- **p. 5 / VI. EXPERIMENTS - extractive body cue:** We evaluate the performance of the SINGER in drone experiments to evaluate its generalization and robustness capabilities in simulation within a 3DGS environment and in ...

- **Evidence anchors reviewed:** datasets p. 6 (VI. EXPERIMENTS), p. 5 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), metrics p. 7 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 5 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 1 (Figure/Table caption), baselines p. 6 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), results p. 7 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 5 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
