# Evaluation - Contact-GraspNet: Efficient 6-DoF Grasp Generation in Cluttered Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2103.14127; PDF retrieval source: https://arxiv.org/pdf/2103.14127. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION), p. 5 (Figure/Table caption), p. 5 (Figure/Table caption)): We observe a significantly higher grasp success rate of our method compared to [11] and [12] which themselves outperform other learning-based methods and analytic/heuristic baselines.

## Evaluation Body Digest

- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** We evaluate our method in a grasping study with a Franka robot where we pick unknown objects in cluttered scenes.
- **p. 6 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** We closely replicate the 9 cluttered scenes defined in [12] with a total of 51 unseen objects.
- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** In the end we execute the most confident grasp that is kinematically reachable and where the robot does not collide with the scene [38].
- **p. 6 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** Training on a small grasp datasets with 110 objects from 5 categories [11] is not sufficient for out-of-category generalization irrespective of the method.
- **p. 6 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** The average distance loss ladd-s improves the success rate of high confidence contacts which is important because most grasps that we execute lie in the ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 5. Loss Ablations: Without weighted binning in the grasp width loss lwidth both, success rate and coverage decrease. The ladd-s loss leads to increased ...
- **p. 6 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** Here, we evaluate the success rate and coverage of the generated grasps following [11].
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 6. Data Ablations: Training with Gaussian noise has similar perfor- mance in simulation but helps generalization to noisy sensor data. Predicting grasps directly on ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** rigid/articulated object와 robot manipulator contact scene.
- **Input boundary:** RGB-D/point cloud, object state와 contact/task observation.
- **Output/decision under evaluation:** grasp, pose, force 또는 end-effector trajectory.
- **Primary target:** task completion, contact success, pose/force error와 generalization.
- **Detected evaluation headings:** IV. EXPERIMENTAL EVALUATION (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTAL EVALUATION | EMPIRICAL / SIMULATION | We observe a significantly higher grasp success rate of our method compared to [11] and [12] which themselves outperform other learning-based methods and analytic/heuristic ... | p. 6 (IV. EXPERIMENTAL EVALUATION) |
| IV. EXPERIMENTAL EVALUATION | EMPIRICAL / SIMULATION | The average distance loss ladd-s improves the success rate of high confidence contacts which is important because most grasps that we execute lie in ... | p. 6 (IV. EXPERIMENTAL EVALUATION) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Fig. 6. Data Ablations: Training with Gaussian noise has similar perfor- mance in simulation but helps generalization to noisy sensor data. Predicting grasps directly ... | p. 5 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Fig. 5. Loss Ablations: Without weighted binning in the grasp width loss lwidth both, success rate and coverage decrease. The ladd-s loss leads to ... | p. 5 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** We evaluate our method in a grasping study with a Franka robot where we pick unknown objects in cluttered scenes.
- **p. 6 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** We closely replicate the 9 cluttered scenes defined in [12] with a total of 51 unseen objects.
- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** In the end we execute the most confident grasp that is kinematically reachable and where the robot does not collide with the scene [38].
- **p. 6 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** Training on a small grasp datasets with 110 objects from 5 categories [11] is not sufficient for out-of-category generalization irrespective of the method.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Contact-GraspNet efficiently predicts diverse and stable grasps in cluttered scenes while avoiding collisions. space of possible grasps to planar grasping, where grasps are ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. Training Data Pipeline. We place object meshes with dense grasp annotations from the ACRONYM dataset [32] at random stable poses in scenes. Grasp ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 3. Our grasp representation: c depicts an observed contact point. a and b constitute the 3-DoF rotation, w is the predicted grasp width, d ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4. Full Inference Pipeline: We segment unknown objects from an RGB-D image using [15]. Our Contact-GraspNet processes the full scene point cloud or a ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 5. Loss Ablations: Without weighted binning in the grasp width loss lwidth both, success rate and coverage decrease. The ladd-s loss leads to increased ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 6. Data Ablations: Training with Gaussian noise has similar perfor- mance in simulation but helps generalization to noisy sensor data. Predicting grasps directly on ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 7. One advantage of our method is that it does not rely on an accurate segmentation of unknown objects. Here, successful grasp contacts are ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate our method in a grasping study with a Franka robot where we pick unknown objects in cluttered scenes. | embodiment, simulator version and control stack | p. 5 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION) |
| Task/environment | We closely replicate the 9 cluttered scenes defined in [12] with a total of 51 unseen objects. | reset, timeout, object/scene variation | p. 6 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION) |
| Observation/sensor | RGB-D/point cloud, object state와 contact/task observation | calibration, preprocessing, privileged input | p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Output/decision | grasp, pose, force 또는 end-effector trajectory | action frame, controller and termination | p. 3 (III. METHOD), p. 1 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The average distance loss ladd-s improves the success rate of high confidence contacts which is important because most grasps that we execute lie in ... | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTAL EVALUATION) |
| Fig. 5. Loss Ablations: Without weighted binning in the grasp width loss lwidth both, success rate and coverage decrease. The ladd-s loss leads to ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Here, we evaluate the success rate and coverage of the generated grasps following [11]. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTAL EVALUATION) |
| Fig. 6. Data Ablations: Training with Gaussian noise has similar perfor- mance in simulation but helps generalization to noisy sensor data. Predicting grasps directly ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Fig. 3. Our grasp representation: c depicts an observed contact point. a and b constitute the 3-DoF rotation, w is the predicted grasp width, ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Fig. 1. Contact-GraspNet efficiently predicts diverse and stable grasps in cluttered scenes while avoiding collisions. space of possible grasps to planar grasping, where grasps ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Fig. 2. Training Data Pipeline. We place object meshes with dense grasp annotations from the ACRONYM dataset [32] at random stable poses in scenes. ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We observe a significantly higher grasp success rate of our method compared to [11] and [12] which themselves outperform other learning-based methods and analytic/heuristic ... | comparison identity and matched condition | p. 6 (IV. EXPERIMENTAL EVALUATION) |
| Compared to other 6-DoF grasp generation methods this is quite fast and enables applications requiring reactive closed loop grasping. | comparison identity and matched condition | p. 5 (IV. EXPERIMENTAL EVALUATION) |
| Fig. 3. Our grasp representation: c depicts an observed contact point. a and b constitute the 3-DoF rotation, w is the predicted grasp width, ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |
| Ablations Optimization Targets: In Fig. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTAL EVALUATION) |
| Fig. 5. Loss Ablations: Without weighted binning in the grasp width loss lwidth both, success rate and coverage decrease. The ladd-s loss leads to ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 5. Loss Ablations: Without weighted binning in the grasp width loss lwidth both, success rate and coverage decrease. The ladd-s loss leads to ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| Fig. 6. Data Ablations: Training with Gaussian noise has similar perfor- mance in simulation but helps generalization to noisy sensor data. Predicting grasps directly ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| 5 we first investigate the effect of our loss targets. | component/input/data sensitivity | p. 6 (IV. EXPERIMENTAL EVALUATION) |
| Ablations Optimization Targets: In Fig. | component/input/data sensitivity | p. 6 (IV. EXPERIMENTAL EVALUATION) |
| Fig. 2. Training Data Pipeline. We place object meshes with dense grasp annotations from the ACRONYM dataset [32] at random stable poses in scenes. ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our method is closely related to the work of Murali et al. | We observe a significantly higher grasp success rate of our method compared to [11] and [12] which themselves outperform other learning-based methods and analytic/heuristic ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION), p. 5 (Figure/Table caption), p. 5 (Figure/Table caption) |
| Primary metric/result | The average distance loss ladd-s improves the success rate of high confidence contacts which is important because most grasps that we execute lie in ... | numeric claim only at cited anchor | p. 6 (IV. EXPERIMENTAL EVALUATION) |

- Numeric sentences retained from the body:
- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** Run time: The Contact-GraspNet has a run time of 0.28s for a full scene or ∼0.19s for a local region around a target object.
- **p. 6 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** Training on a small grasp datasets with 110 objects from 5 categories [11] is not sufficient for out-of-category generalization irrespective of the method.
- **p. 4 / III. METHOD - extractive body cue:** The network takes n=20000 random points p ∈R20000×3 as input and predicts grasps for only m=2048 farthest points of the input to make sure the ...
- **p. 4 / III. METHOD - extractive body cue:** We train with a batch size of 3 for 144.000 iterations which takes ∼40 hours on a single Nvidia V100 GPU.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Gripper collisions are effectively avoided by considering them during training and by predicting grasps directly in scenes. | p. 6 (V. CONCLUSIONS) |
| body limitation/failure cue | Failure Cases: We observe some failure cases for thick objects that only allow grasps almost at maximum grasp width. | p. 6 (IV. EXPERIMENTAL EVALUATION) |
| body limitation/failure cue | Fig. 1. Contact-GraspNet efficiently predicts diverse and stable grasps in cluttered scenes while avoiding collisions. space of possible grasps to planar grasping, where grasps ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Fig. 2. Training Data Pipeline. We place object meshes with dense grasp annotations from the ACRONYM dataset [32] at random stable poses in scenes. ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | However, grasping in only one or two trials is crucial in cluttered scenes (e.g. in households) with large, densely packed objects where collisions should ... | p. 5 (IV. EXPERIMENTAL EVALUATION) |
| body limitation/failure cue | In the end we execute the most confident grasp that is kinematically reachable and where the robot does not collide with the scene [38]. | p. 5 (IV. EXPERIMENTAL EVALUATION) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We train with a batch size of 3 for 144.000 iterations which takes ∼40 hours on a single Nvidia V100 GPU. | p. 4 (III. METHOD) |
| Implementation Details We use the Adam optimizer with an initial learning rate of 0.001 and a step-wise decay to 0.0001. | p. 4 (III. METHOD) |
| Evaluation Metrics In our robotic experiments we report the number of successful grasps and the number of trials. | p. 5 (IV. EXPERIMENTAL EVALUATION) |
| Run time: The Contact-GraspNet has a run time of 0.28s for a full scene or ∼0.19s for a local region around a target object. | p. 5 (IV. EXPERIMENTAL EVALUATION) |
| Furthermore, our method strongly improves the grasp success at first trial and thereby reduces the number of re-grasps. | p. 6 (IV. EXPERIMENTAL EVALUATION) |
| Here, successful grasp contacts are still found on the driller despite severe under-segmentation. limit ourselves to a maximum of two grasp trials per object ... | p. 6 (IV. EXPERIMENTAL EVALUATION) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / V. CONCLUSIONS - extractive body cue:** Gripper collisions are effectively avoided by considering them during training and by predicting grasps directly in scenes.
- **p. 6 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** Failure Cases: We observe some failure cases for thick objects that only allow grasps almost at maximum grasp width.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Contact-GraspNet efficiently predicts diverse and stable grasps in cluttered scenes while avoiding collisions. space of possible grasps to planar grasping, where grasps are ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. Training Data Pipeline. We place object meshes with dense grasp annotations from the ACRONYM dataset [32] at random stable poses in scenes. Grasp ...
- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** However, grasping in only one or two trials is crucial in cluttered scenes (e.g. in households) with large, densely packed objects where collisions should be ...
- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** In the end we execute the most confident grasp that is kinematically reachable and where the robot does not collide with the scene [38].

- **Evidence anchors reviewed:** datasets p. 5 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION), metrics p. 6 (IV. EXPERIMENTAL EVALUATION), p. 5 (Figure/Table caption), p. 6 (IV. EXPERIMENTAL EVALUATION), p. 5 (Figure/Table caption), p. 3 (Figure/Table caption), p. 1 (Figure/Table caption), baselines p. 6 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION), p. 3 (Figure/Table caption), p. 6 (IV. EXPERIMENTAL EVALUATION), p. 5 (Figure/Table caption), results p. 6 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION), p. 5 (Figure/Table caption), p. 5 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (7 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** We observe a significantly higher grasp success rate of our method compared to [11] and [12] which themselves outperform other learning-based methods and analytic/heuristic baselines. (p. 6, IV. EXPERIMENTAL EVALUATION).
- **Metric evidence:** The average distance loss ladd-s improves the success rate of high confidence contacts which is important because most grasps that we execute lie in the first decimal of coverage. (p. 6, IV. EXPERIMENTAL EVALUATION).
- **Baseline/ablation evidence:** We observe a significantly higher grasp success rate of our method compared to [11] and [12] which themselves outperform other learning-based methods and analytic/heuristic baselines. (p. 6, IV. EXPERIMENTAL EVALUATION).
- **Failure/negative evidence:** Failure Cases: We observe some failure cases for thick objects that only allow grasps almost at maximum grasp width. (p. 6, IV. EXPERIMENTAL EVALUATION).
