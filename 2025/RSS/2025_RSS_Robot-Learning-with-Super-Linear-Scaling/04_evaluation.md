# Evaluation - Robot Learning with Super-Linear Scaling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p025.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p025.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (A. Zero-Shot Scaling Laws Analysis), p. 6 (A. Zero-Shot Scaling Laws Analysis)): To verify the robustness of the learned policies, we ran evaluation on eight additional kitchens, ‘The results highlight an improvement of 16% to 60% rate as the number of training ...

## Evaluation Body Digest

- **p. 6 / A. Zero-Shot Scaling Laws Analysis - extractive PDF cue:** The first experiment involves a thorough real-world evaluation of these policies across two institutions, using three different kitchens and six different objects, with six rollouts ...
- **p. 12 / IX. IMPLEMENTATION DETAILS - extractive PDF cue:** We train an MLP network of size 256,256, that takes the embedding of the point cloud observation, which has 128 ‘dimensions, together With the state ...
- **p. 6 / A. Zero-Shot Scaling Laws Analysis - extractive PDF cue:** For fair comparison, we train these policies using human demonstrations in each environment.
- **p. 12 / IX. IMPLEMENTATION DETAILS - extractive PDF cue:** 1) State-based policy: As described in Section III-B, we trained a series of state-based policies with privileged information in simulation.
- **p. 6 / A. Zero-Shot Scaling Laws Analysis - extractive PDF cue:** As shown in Figure 3 a, we confirm the real-to-sim-to-real pipeline scaling law: as the number of trained environments increases, the zeroshot success rate also ...
- **p. 6 / A. Zero-Shot Scaling Laws Analysis - extractive PDF cue:** To verify the robustness of the learned policies, we ran evaluation on eight additional kitchens, ‘The results highlight an improvement of 16% to 60% rate ...
- **p. 12 / IX. IMPLEMENTATION DETAILS - extractive PDF cue:** To implement PPO with the BC loss algorithm, we built upon the Stable Baselines 3 repository [33].
- **p. 12 / IX. IMPLEMENTATION DETAILS - extractive PDF cue:** To encode the point cloud observation, we use the volumetric 3D point cloud encoder proposed in Convolutional Occupancy Networks [31], which consists ofa local point ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** demonstration으로 정의된 robot task distribution.
- **Input boundary:** observation history와 expert trajectory/action.
- **Output/decision under evaluation:** predicted action 또는 action chunk.
- **Primary target:** imitation error, task success, robustness와 compounding error.
- **Detected evaluation headings:** IX. IMPLEMENTATION DETAILS (p. 12); XI. DETAILED EVALUATION RESULTS (p. 12); A. Evaluation on Multi-Object Scenes (p. 12); B. Evaluation on Scenes Involving Disturbance and Distrac (p. 12).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| A. Zero-Shot Scaling Laws Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | To verify the robustness of the learned policies, we ran evaluation on eight additional kitchens, ‘The results highlight an improvement of 16% to 60% ... | p. 6 (A. Zero-Shot Scaling Laws Analysis) |
| A. Zero-Shot Scaling Laws Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | Furthermore, Figure 3b shows a linear correlation between simulation and real world performance, indicating that our real-to-sim-to-real scaling approach in simulation proportionally corresponds to ... | p. 6 (A. Zero-Shot Scaling Laws Analysis) |

## Dataset / Benchmark Role

- **p. 6 / A. Zero-Shot Scaling Laws Analysis - extractive PDF cue:** The first experiment involves a thorough real-world evaluation of these policies across two institutions, using three different kitchens and six different objects, with six rollouts ...
- **p. 12 / IX. IMPLEMENTATION DETAILS - extractive PDF cue:** We train an MLP network of size 256,256, that takes the embedding of the point cloud observation, which has 128 ‘dimensions, together With the state ...
- **p. 6 / A. Zero-Shot Scaling Laws Analysis - extractive PDF cue:** For fair comparison, we train these policies using human demonstrations in each environment.
- **p. 12 / IX. IMPLEMENTATION DETAILS - extractive PDF cue:** 1) State-based policy: As described in Section III-B, we trained a series of state-based policies with privileged information in simulation.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 5. resus on the task of pik and place mugbowLeups in the sink
- **p. 11 / Figure/Table caption - extractive PDF cue:** Fig. 8. Overview of «sclcted number of scenes and objects used forthe real-world evaluation ofthe tsk of placing bowlsmugscups in the snk.
- **p. 14 / Figure/Table caption - extractive PDF cue:** Fig. 10. Overview of the experiment setup for evaluating the robustness
- **p. 15 / Figure/Table caption - extractive PDF cue:** Fig. 12. Poster used for calling crowdsourcing contribution.

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The first experiment involves a thorough real-world evaluation of these policies across two institutions, using three different kitchens and six different objects, with six ... | embodiment, simulator version and control stack | p. 6 (A. Zero-Shot Scaling Laws Analysis), p. 12 (IX. IMPLEMENTATION DETAILS) |
| Task/environment | We train an MLP network of size 256,256, that takes the embedding of the point cloud observation, which has 128 ‘dimensions, together With the ... | reset, timeout, object/scene variation | p. 12 (IX. IMPLEMENTATION DETAILS), p. 6 (A. Zero-Shot Scaling Laws Analysis) |
| Observation/sensor | observation history와 expert trajectory/action | calibration, preprocessing, privileged input | p. 12 (IX. IMPLEMENTATION DETAILS), p. 12 (IX. IMPLEMENTATION DETAILS) |
| Output/decision | predicted action 또는 action chunk | action frame, controller and termination | p. 4 (4 Sample set of A' digital twins from crowdsourced), p. 4 (4 Sample set of A' digital twins from crowdsourced) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| As shown in Figure 3 a, we confirm the real-to-sim-to-real pipeline scaling law: as the number of trained environments increases, the zeroshot success rate ... | definition/direction/unit from same section | p. 6 (A. Zero-Shot Scaling Laws Analysis) |
| To verify the robustness of the learned policies, we ran evaluation on eight additional kitchens, ‘The results highlight an improvement of 16% to 60% ... | definition/direction/unit from same section | p. 6 (A. Zero-Shot Scaling Laws Analysis) |
| To implement PPO with the BC loss algorithm, we built upon the Stable Baselines 3 repository [33]. | definition/direction/unit from same section | p. 12 (IX. IMPLEMENTATION DETAILS) |
| To encode the point cloud observation, we use the volumetric 3D point cloud encoder proposed in Convolutional Occupancy Networks [31], which consists ofa local ... | definition/direction/unit from same section | p. 12 (IX. IMPLEMENTATION DETAILS) |
| Fig. 10. Overview of the experiment setup for evaluating the robustness | definition/direction/unit from same section | p. 14 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In Section IV-B, ‘we compare this baseline to the autonomous data collection system presented in Section III-B. | comparison identity and matched condition | p. 6 (A. Zero-Shot Scaling Laws Analysis) |
| To implement PPO with the BC loss algorithm, we built upon the Stable Baselines 3 repository [33]. | comparison identity and matched condition | p. 12 (IX. IMPLEMENTATION DETAILS) |
| For fair comparison, we train these policies using human demonstrations in each environment. | comparison identity and matched condition | p. 6 (A. Zero-Shot Scaling Laws Analysis) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| lef: results fr few-sot fine-tuning on the ask of pick and place « box om a shelf middle: results opening a cabinet right: muli-object ... | component/input/data sensitivity | p. 6 (A. Zero-Shot Scaling Laws Analysis) |
| 2) Point cloud policy: As mentioned in Section II-C, when distilling the state-based teacher policy t0 a fine-tuned visuomotor policy, we will train a ... | component/input/data sensitivity | p. 12 (IX. IMPLEMENTATION DETAILS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We show that CASHER enables fine-tuning of prestrained to a target scenario using a video sean without any additional hbuman effort. | To verify the robustness of the learned policies, we ran evaluation on eight additional kitchens, ‘The results highlight an improvement of 16% to 60% ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (A. Zero-Shot Scaling Laws Analysis), p. 6 (A. Zero-Shot Scaling Laws Analysis) |
| Primary metric/result | Furthermore, Figure 3b shows a linear correlation between simulation and real world performance, indicating that our real-to-sim-to-real scaling approach in simulation proportionally corresponds to ... | numeric claim only at cited anchor | p. 6 (A. Zero-Shot Scaling Laws Analysis) |

- Numeric sentences retained from the body:
- **p. 6 / A. Zero-Shot Scaling Laws Analysis - extractive PDF cue:** The first experiment involves a thorough real-world evaluation of these policies across two institutions, using three different kitchens and six different objects, with six rollouts ...
- **p. 6 / A. Zero-Shot Scaling Laws Analysis - extractive PDF cue:** On the same lines we evaluate the policy on multiple objects in the scene and observe that even though it was only trained to pick ...
- **p. 12 / IX. IMPLEMENTATION DETAILS - extractive PDF cue:** We train an MLP network of size 256,256, that takes the embedding of the point cloud observation, which has 128 ‘dimensions, together With the state ...
- **p. 12 / IX. IMPLEMENTATION DETAILS - extractive PDF cue:** We train an MLP network of size 256,256, that takes the embedding of the point cloud observation, which has 128 ‘dimensions, together With the state ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | For these environments F, we fall back to querying the human demonstrator for high-quality demonstrations and learn a second state-based policy *+a(a,/s) using demonstration-bootstrapped ... | p. 4 (4 Sample set of A' digital twins from crowdsourced) |
| body limitation/failure cue | This reduces the amount of human effort required for data collection as training progresses, Importantly, the generalization across environments does not need to achieve ... | p. 5 (4 Sample set of A' digital twins from crowdsourced) |
| body limitation/failure cue | T can be used to obtain a single robust, statecovering optimal multi-environment policy xs3(as/s¢) for all Ex :1,-++»€2x Via demonstration-bootstrapped reinforcement learning. | p. 4 (4 Sample set of A' digital twins from crowdsourced) |
| body limitation/failure cue | This model-generated data can then be used to train a robust, high-coverage statebased policy 4(a/s+) using demonstration-bootstrapped re | p. 5 (C. Fine-uning of Generalist Policies on Deployment) |
| body limitation/failure cue | To verify the robustness of the learned policies, we ran evaluation on eight additional kitchens, ‘The results highlight an improvement of 16% to 60% ... | p. 6 (A. Zero-Shot Scaling Laws Analysis) |
| body limitation/failure cue | Fig. 10. Overview of the experiment setup for evaluating the robustness | p. 14 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| To encode the point cloud observation, we use the volumetric 3D point cloud encoder proposed in Convolutional Occupancy Networks [31], which consists ofa local ... | p. 12 (IX. IMPLEMENTATION DETAILS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 4 / 4 Sample set of A' digital twins from crowdsourced - extractive PDF cue:** For these environments F, we fall back to querying the human demonstrator for high-quality demonstrations and learn a second state-based policy *+a(a,/s) using demonstration-bootstrapped reinforcement ...
- **p. 5 / 4 Sample set of A' digital twins from crowdsourced - extractive PDF cue:** This reduces the amount of human effort required for data collection as training progresses, Importantly, the generalization across environments does not need to achieve perfect ...
- **p. 4 / 4 Sample set of A' digital twins from crowdsourced - extractive PDF cue:** T can be used to obtain a single robust, statecovering optimal multi-environment policy xs3(as/s¢) for all Ex :1,-++»€2x Via demonstration-bootstrapped reinforcement learning.
- **p. 5 / C. Fine-uning of Generalist Policies on Deployment - extractive PDF cue:** This model-generated data can then be used to train a robust, high-coverage statebased policy 4(a/s+) using demonstration-bootstrapped re
- **p. 6 / A. Zero-Shot Scaling Laws Analysis - extractive PDF cue:** To verify the robustness of the learned policies, we ran evaluation on eight additional kitchens, ‘The results highlight an improvement of 16% to 60% rate ...
- **p. 14 / Figure/Table caption - extractive PDF cue:** Fig. 10. Overview of the experiment setup for evaluating the robustness

- **PDF anchors reviewed:** datasets p. 6 (A. Zero-Shot Scaling Laws Analysis), p. 12 (IX. IMPLEMENTATION DETAILS), p. 6 (A. Zero-Shot Scaling Laws Analysis), p. 12 (IX. IMPLEMENTATION DETAILS), metrics p. 6 (A. Zero-Shot Scaling Laws Analysis), p. 6 (A. Zero-Shot Scaling Laws Analysis), p. 12 (IX. IMPLEMENTATION DETAILS), p. 12 (IX. IMPLEMENTATION DETAILS), p. 14 (Figure/Table caption), baselines p. 6 (A. Zero-Shot Scaling Laws Analysis), p. 12 (IX. IMPLEMENTATION DETAILS), p. 6 (A. Zero-Shot Scaling Laws Analysis), results p. 6 (A. Zero-Shot Scaling Laws Analysis), p. 6 (A. Zero-Shot Scaling Laws Analysis).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
