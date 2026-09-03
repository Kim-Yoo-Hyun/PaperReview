# Evaluation - Gaussian Splatting Visual MPC for Granular Media Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.proceedings.com/content/081/081087webtoc.pdf; PDF retrieval source: https://arxiv.org/pdf/2410.09740v3. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS)): Manipulation Results TABLE I MANIPULATION SUCCESS RATE IN SIMULATION (MAX = 1.0) Collection Splitting Redistributing NeRF-dy [38] 0.67 0.43 0.31 Dyn-Res [16] 0.79 0.72 0.67 NFD [29] 0.89 0.74 0.46 ...

## Evaluation Body Digest

- **p. 4 / V. EXPERIMENTAL RESULTS - extractive body cue:** (b) The granular materials used in real-world experiments include coffee beans, peanuts, pistachios, and almonds. transfer our model trained in the simulation environment to our ...
- **p. 5 / V. EXPERIMENTAL RESULTS - extractive body cue:** Collection Splitting Pistachios 0.85 0.80 Almonds 0.85 0.75 Peanuts 0.85 0.85 Coffee Beans 0.65 0.60 In real-world experiments, as shown in Table III, we observe ...
- **p. 5 / V. EXPERIMENTAL RESULTS - extractive body cue:** In simulation, we perform 100 trials, while for real-world experiments, we conduct 20 trials.
- **p. 4 / V. EXPERIMENTAL RESULTS - extractive body cue:** 3 shows the granular materials tested and the robot setup.
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** Qualitative results from real-world experiments.
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** (a) Evaluation of our method on a collection task with different objects than what it was trained on.
- **p. 5 / V. EXPERIMENTAL RESULTS - extractive body cue:** We use two metrics to evaluate the frameworks. • Success rate: success is defined as moving all materials to the target region. • State error: ...
- **p. 5 / V. EXPERIMENTAL RESULTS - extractive body cue:** Manipulation Results TABLE I MANIPULATION SUCCESS RATE IN SIMULATION (MAX = 1.0) Collection Splitting Redistributing NeRF-dy [38] 0.67 0.43 0.31 Dyn-Res [16] 0.79 0.72 0.67 ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** V. EXPERIMENTAL RESULTS (p. 4).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| V. EXPERIMENTAL RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Manipulation Results TABLE I MANIPULATION SUCCESS RATE IN SIMULATION (MAX = 1.0) Collection Splitting Redistributing NeRF-dy [38] 0.67 0.43 0.31 Dyn-Res [16] 0.79 0.72 ... | p. 5 (V. EXPERIMENTAL RESULTS) |
| V. EXPERIMENTAL RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our approach achieves higher performance than NeRF-dy while requiring fewer views. | p. 5 (V. EXPERIMENTAL RESULTS) |
| V. EXPERIMENTAL RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Qualitative results from real-world experiments. | p. 6 (V. EXPERIMENTAL RESULTS) |
| V. EXPERIMENTAL RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Manipulation performance with different numbers of viewpoints as input. | p. 6 (V. EXPERIMENTAL RESULTS) |

## Dataset / Benchmark Role

- **p. 4 / V. EXPERIMENTAL RESULTS - extractive body cue:** (b) The granular materials used in real-world experiments include coffee beans, peanuts, pistachios, and almonds. transfer our model trained in the simulation environment to our ...
- **p. 5 / V. EXPERIMENTAL RESULTS - extractive body cue:** Collection Splitting Pistachios 0.85 0.80 Almonds 0.85 0.75 Peanuts 0.85 0.85 Coffee Beans 0.65 0.60 In real-world experiments, as shown in Table III, we observe ...
- **p. 5 / V. EXPERIMENTAL RESULTS - extractive body cue:** In simulation, we perform 100 trials, while for real-world experiments, we conduct 20 trials.
- **p. 4 / V. EXPERIMENTAL RESULTS - extractive body cue:** 3 shows the granular materials tested and the robot setup.
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** Qualitative results from real-world experiments.
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** (a) Evaluation of our method on a collection task with different objects than what it was trained on.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Our method takes a few multi-view images of a scene and their corresponding camera poses as input, and (a) converts them into their ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. Our framework. (a) Given demonstration trajectories with multi-view observations, we leverage Gaussian splatting representations to reconstruct the observed images at each timestep. (b) ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3. Real-world experiment setup. (a) The robotic manipulator, with a pusher attached to the end-effector, moves granular materials within the workspace. Four calibrated RGBD ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4. Dynamics model rollouts. We show the rollout predictions of the dynamics model in both simulation (left) and real-world data (right). Both of the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5. Qualitative results from real-world experiments. (a) Evaluation of our method on a collection task with different objects than what it was trained on. ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 6. Manipulation performance with different numbers of viewpoints as input. Performance increases with more views, providing more accurate granular material reconstruction. dynamics. In contrast, ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 7. Manipulation performance with different numbers of particles in the workspace. Our approach demonstrates superior generalization compared to other baselines. Message Passing in Dynamics. ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 8. Manipulation performance with different numbers of message- passing steps. More steps lead to better performance. rice. This limitation stems from the difficulty in ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | (b) The granular materials used in real-world experiments include coffee beans, peanuts, pistachios, and almonds. transfer our model trained in the simulation environment to ... | embodiment, simulator version and control stack | p. 4 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS) |
| Task/environment | Collection Splitting Pistachios 0.85 0.80 Almonds 0.85 0.75 Peanuts 0.85 0.85 Coffee Beans 0.65 0.60 In real-world experiments, as shown in Table III, we ... | reset, timeout, object/scene variation | p. 5 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (III. PRELIMINARIES), p. 3 (IV. OUR APPROACH) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We use two metrics to evaluate the frameworks. • Success rate: success is defined as moving all materials to the target region. • State ... | definition/direction/unit from same section | p. 5 (V. EXPERIMENTAL RESULTS) |
| Manipulation Results TABLE I MANIPULATION SUCCESS RATE IN SIMULATION (MAX = 1.0) Collection Splitting Redistributing NeRF-dy [38] 0.67 0.43 0.31 Dyn-Res [16] 0.79 0.72 ... | definition/direction/unit from same section | p. 5 (V. EXPERIMENTAL RESULTS) |
| We directly Algorithm 1: Our Visual MPC Planning Algorithm Data: Current observation Ot, target Otarget, planning horizon T, the dynamics model f, Number of ... | definition/direction/unit from same section | p. 4 (V. EXPERIMENTAL RESULTS) |
| Performance increases with more views, providing more accurate granular material reconstruction. dynamics. | definition/direction/unit from same section | p. 6 (V. EXPERIMENTAL RESULTS) |
| Fig. 8. Manipulation performance with different numbers of message- passing steps. More steps lead to better performance. rice. This limitation stems from the difficulty ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Four calibrated RGBD cameras are mounted around the workspace to provide multi-view observations. | definition/direction/unit from same section | p. 4 (V. EXPERIMENTAL RESULTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Manipulation Results TABLE I MANIPULATION SUCCESS RATE IN SIMULATION (MAX = 1.0) Collection Splitting Redistributing NeRF-dy [38] 0.67 0.43 0.31 Dyn-Res [16] 0.79 0.72 ... | comparison identity and matched condition | p. 5 (V. EXPERIMENTAL RESULTS) |
| Our approach demonstrates superior generalization compared to other baselines. | comparison identity and matched condition | p. 6 (V. EXPERIMENTAL RESULTS) |
| We compare our approach against several baselines, providing a brief description of each below: • Dyn-Res[16] constructs dynamic-resolution particle representations for granular materials and ... | comparison identity and matched condition | p. 4 (V. EXPERIMENTAL RESULTS) |
| Generalization Studies In this section, we conduct ablation studies to evaluate the effectiveness of each component. | comparison identity and matched condition | p. 5 (V. EXPERIMENTAL RESULTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Generalization Studies In this section, we conduct ablation studies to evaluate the effectiveness of each component. | component/input/data sensitivity | p. 5 (V. EXPERIMENTAL RESULTS) |
| This approach leverages the spatial locality of inter-object interactions and translation equivariance through convolutional operations. • NeRF-dy [38] leverages NeRF to learn viewpointinvariant and ... | component/input/data sensitivity | p. 5 (V. EXPERIMENTAL RESULTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We form the node features of the GNN as (ci t,σi t ,Ri t,gi t,si t) for node vi t. f consists of node ... | Manipulation Results TABLE I MANIPULATION SUCCESS RATE IN SIMULATION (MAX = 1.0) Collection Splitting Redistributing NeRF-dy [38] 0.67 0.43 0.31 Dyn-Res [16] 0.79 0.72 ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS) |
| Primary metric/result | Our approach achieves higher performance than NeRF-dy while requiring fewer views. | numeric claim only at cited anchor | p. 5 (V. EXPERIMENTAL RESULTS) |

- Numeric sentences retained from the body:
- **p. 4 / V. EXPERIMENTAL RESULTS - extractive body cue:** We directly Algorithm 1: Our Visual MPC Planning Algorithm Data: Current observation Ot, target Otarget, planning horizon T, the dynamics model f, Number of sampled ...
- **p. 5 / V. EXPERIMENTAL RESULTS - extractive body cue:** In simulation, we perform 100 trials, while for real-world experiments, we conduct 20 trials.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | This limitation stems from the difficulty in accurately reconstructing such tiny particles using Gaussian splatting, which struggles to maintain precision at smaller scales. | p. 6 (VI. LIMITATIONS) |
| body limitation/failure cue | Future work could extend this framework to other non-rigid materials, further enhancing the capabilities of robotic systems in dynamic tasks. | p. 6 (VII. CONCLUSION) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Implementation Details We implement the entire framework using PyTorch [33] and PyTorch-Geometric [34]. | p. 4 (V. EXPERIMENTAL RESULTS) |
| We directly Algorithm 1: Our Visual MPC Planning Algorithm Data: Current observation Ot, target Otarget, planning horizon T, the dynamics model f, Number of ... | p. 4 (V. EXPERIMENTAL RESULTS) |
| In simulation, we perform 100 trials, while for real-world experiments, we conduct 20 trials. | p. 5 (V. EXPERIMENTAL RESULTS) |
| Both of the rollout results show that the dynamics model prediction is accurate for a few steps. • NFD[29] uses a fully convolutional neural ... | p. 5 (V. EXPERIMENTAL RESULTS) |
| Tasks requiring accurate future state predictions benefit from additional message-passing steps for precise manipulation. | p. 6 (V. EXPERIMENTAL RESULTS) |
| The objects vary in scale and physical properties (e.g., almonds and pistachios remain quasi-static during MPC steps, while peanuts and coffee beans may roll ... | p. 6 (V. EXPERIMENTAL RESULTS) |
| Finally, we have the decoder fdec that transforms node features after Γ message passing steps to dynamic information ∆ri t ,∆gi t = fdec(qi,Γ ... | p. 3 (IV. OUR APPROACH) |
| We form the node features of the GNN as (ci t,σi t ,Ri t,gi t,si t) for node vi t. f consists of node ... | p. 3 (IV. OUR APPROACH) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / VI. LIMITATIONS - extractive body cue:** This limitation stems from the difficulty in accurately reconstructing such tiny particles using Gaussian splatting, which struggles to maintain precision at smaller scales.
- **p. 6 / VII. CONCLUSION - extractive body cue:** Future work could extend this framework to other non-rigid materials, further enhancing the capabilities of robotic systems in dynamic tasks.

- **Evidence anchors reviewed:** datasets p. 4 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS), p. 4 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), metrics p. 5 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS), p. 4 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (Figure/Table caption), p. 4 (V. EXPERIMENTAL RESULTS), baselines p. 5 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 4 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS), results p. 5 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (7 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Manipulation Results TABLE I MANIPULATION SUCCESS RATE IN SIMULATION (MAX = 1.0) Collection Splitting Redistributing NeRF-dy [38] 0.67 0.43 0.31 Dyn-Res [16] 0.79 0.72 0.67 NFD [29] 0.89 0.74 0.46 ... (p. 5, V. EXPERIMENTAL RESULTS).
- **Metric evidence:** We use two metrics to evaluate the frameworks. • Success rate: success is defined as moving all materials to the target region. • State error: in simulation experiments, we also ... (p. 5, V. EXPERIMENTAL RESULTS).
- **Baseline/ablation evidence:** Our approach demonstrates superior generalization compared to other baselines. (p. 6, V. EXPERIMENTAL RESULTS).
- **Failure/negative evidence:** This limitation stems from the difficulty in accurately reconstructing such tiny particles using Gaussian splatting, which struggles to maintain precision at smaller scales. (p. 6, VI. LIMITATIONS).
