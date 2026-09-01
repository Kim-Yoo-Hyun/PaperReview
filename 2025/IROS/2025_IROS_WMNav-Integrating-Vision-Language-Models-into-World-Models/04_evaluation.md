# Evaluation - WMNav: Integrating Vision-Language Models into World Models for Object Goal Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2503.02247; PDF retrieval source: https://arxiv.org/pdf/2503.02247. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 3 (Figure/Table caption), p. 4 (Figure/Table caption), p. 5 (Figure/Table caption)): Metrics We adopt Success Rate (SR) and Success Rate Weighted by Inverse Path Length (SPL) as the evaluation metrics.

## Evaluation Body Digest

- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Datasets and Evaluation Metrics Datasets The HM3D v0.1 [38] is used in the Habitat 2022 ObjectNav challenge, providing 2000 validation episodes on 20 validation environments ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** MP3D [19] contains 11 high-fidelity scenes and 2195 episodes for validation, with 21 categories of object goals.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Metrics We adopt Success Rate (SR) and Success Rate Weighted by Inverse Path Length (SPL) as the evaluation metrics.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** SPL quantifies the agent's navigation efficiency by calculating the inverse ratio of the actual path length traversed to the optimal path length weighted by success ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: The WMNav framework. After acquiring the RGB-D panoramic image and pose information at step t, the PredictVLM first predicts the state of the ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Predict the Likelihood. (a) The world model predicts the Curiosity Value for each direction in the panoramic image based on the likelihood of ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: Plan the Route. Text prompt is configured by the previous step's subtask, the explanation for selecting the highest-scoring image, and the goal. Using ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: World Model Navigation with VLM. In object navigation, our model first estimates the goal's presence likelihood in each scene of the panoramic image ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Metrics We adopt Success Rate (SR) and Success Rate Weighted by Inverse Path Length (SPL) as the evaluation metrics. | p. 6 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | SPL quantifies the agent's navigation efficiency by calculating the inverse ratio of the actual path length traversed to the optimal path length weighted by ... | p. 6 (IV. EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 2: The WMNav framework. After acquiring the RGB-D panoramic image and pose information at step t, the PredictVLM first predicts the state of ... | p. 3 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 3: Predict the Likelihood. (a) The world model predicts the Curiosity Value for each direction in the panoramic image based on the likelihood ... | p. 4 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 4: Plan the Route. Text prompt is configured by the previous step's subtask, the explanation for selecting the highest-scoring image, and the goal. ... | p. 5 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Datasets and Evaluation Metrics Datasets The HM3D v0.1 [38] is used in the Habitat 2022 ObjectNav challenge, providing 2000 validation episodes on 20 validation environments ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** MP3D [19] contains 11 high-fidelity scenes and 2195 episodes for validation, with 21 categories of object goals.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: World Model Navigation with VLM. In object navigation, our model first estimates the goal's presence likelihood in each scene of the panoramic image ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: The WMNav framework. After acquiring the RGB-D panoramic image and pose information at step t, the PredictVLM first predicts the state of the ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Predict the Likelihood. (a) The world model predicts the Curiosity Value for each direction in the panoramic image based on the likelihood of ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: Plan the Route. Text prompt is configured by the previous step's subtask, the explanation for selecting the highest-scoring image, and the goal. Using ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 5: Reason the Action. In the exploration stage, the agent uses the action proposer to filter sampled actions. ActionVLM(obtained by configuring ReasonVLM) selects the ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Datasets and Evaluation Metrics Datasets The HM3D v0.1 [38] is used in the Habitat 2022 ObjectNav challenge, providing 2000 validation episodes on 20 validation ... | embodiment, simulator version and control stack | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Task/environment | MP3D [19] contains 11 high-fidelity scenes and 2195 episodes for validation, with 21 categories of object goals. | reset, timeout, object/scene variation | p. 6 (IV. EXPERIMENTS) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 2 (I. INTRODUCTION), p. 5 (III. WMNAV APPROACH) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 3 (III. WMNAV APPROACH), p. 4 (III. WMNAV APPROACH) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Metrics We adopt Success Rate (SR) and Success Rate Weighted by Inverse Path Length (SPL) as the evaluation metrics. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| SPL quantifies the agent's navigation efficiency by calculating the inverse ratio of the actual path length traversed to the optimal path length weighted by ... | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| Fig. 2: The WMNav framework. After acquiring the RGB-D panoramic image and pose information at step t, the PredictVLM first predicts the state of ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Fig. 3: Predict the Likelihood. (a) The world model predicts the Curiosity Value for each direction in the panoramic image based on the likelihood ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Fig. 4: Plan the Route. Text prompt is configured by the previous step's subtask, the explanation for selecting the highest-scoring image, and the goal. ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Fig. 1: World Model Navigation with VLM. In object navigation, our model first estimates the goal's presence likelihood in each scene of the panoramic ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Memory SD TAP SR(%)↑SPL(%)↑ a No ✗ ✗ 65.8 25.8 b No ✓ ✗ 67.4 33.1 c Text-Image ✓ ✗ 62.0 29.6 d CVM(Ours) ... | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| Compared to all methods, including supervised methods, our approach also achieves the optimal SR on MP3D and the best SPL on HM3D, demonstrating the ... | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| As shown in TABLE II: Ablation study of different modules and memory strategies on HM3D v0.2 [38]. | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |
| So, the agent only needs a VLM base to complete all the processes without any policy modules to train. | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions can be summarized as follows: • We introduce a new direction for object goal navigation in a complex, unknown environment using a ... | Metrics We adopt Success Rate (SR) and Success Rate Weighted by Inverse Path Length (SPL) as the evaluation metrics. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 3 (Figure/Table caption), p. 4 (Figure/Table caption), p. 5 (Figure/Table caption) |
| Primary metric/result | SPL quantifies the agent's navigation efficiency by calculating the inverse ratio of the actual path length traversed to the optimal path length weighted by ... | numeric claim only at cited anchor | p. 6 (IV. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** MP3D [19] contains 11 high-fidelity scenes and 2195 episodes for validation, with 21 categories of object goals.
- **p. 5 / III. WMNAV APPROACH - extractive body cue:** Choose your action from the image prompt.' Image Prompt Exploration Stage Action VLM Update Navigable Area Candidate Actions Initial Actions Exploration State Map Filter 2 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | If there is no sofa, then return failure message. | p. 5 (III. WMNAV APPROACH) |
| body limitation/failure cue | 2) Goal-approaching Stage: Due to the limitations of the existing VLMs' capability, we do not rely on the VLM to estimate the stopping condition ... | p. 5 (III. WMNAV APPROACH) |
| body limitation/failure cue | But textual information cannot accurately describe the spatial relationships in the scene, and it is difficult for LLM to make good spatial decisions. | p. 6 (IV. EXPERIMENTS) |
| body limitation/failure cue | However, since VLM is trained on egocentric image data, it does not take advantage of VLM's powerful egocentric reasoning ability. | p. 6 (IV. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Implementation Details We set 40 as the agent's maximal navigation steps. | p. 6 (IV. EXPERIMENTS) |
| Similar to the frontier map, our simple and online maintained Curiosity Value Map, without prior information from other detectors, makes full use of the ... | p. 6 (IV. EXPERIMENTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / III. WMNAV APPROACH - extractive body cue:** If there is no sofa, then return failure message.
- **p. 5 / III. WMNAV APPROACH - extractive body cue:** 2) Goal-approaching Stage: Due to the limitations of the existing VLMs' capability, we do not rely on the VLM to estimate the stopping condition directly ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** But textual information cannot accurately describe the spatial relationships in the scene, and it is difficult for LLM to make good spatial decisions.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** However, since VLM is trained on egocentric image data, it does not take advantage of VLM's powerful egocentric reasoning ability.

- **PDF anchors reviewed:** datasets p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), metrics p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 3 (Figure/Table caption), p. 4 (Figure/Table caption), p. 5 (Figure/Table caption), p. 1 (Figure/Table caption), baselines p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), results p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 3 (Figure/Table caption), p. 4 (Figure/Table caption), p. 5 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
