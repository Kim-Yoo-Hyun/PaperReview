# Evaluation - Learning Robust Perceptive Locomotion for Quadrupedal Robots in the Wild

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2201.08117; PDF retrieval source: https://arxiv.org/pdf/2201.08117. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (2. RESULTS), p. 5 (2. RESULTS), p. 3 (2. RESULTS), p. 8 (2. RESULTS), p. 3 (2. RESULTS), p. 8 (2. RESULTS)): First, we compared the success rate of overcoming fixed-height steps as shown in Figure 4A.

## Evaluation Body Digest

- **p. 5 / 2. RESULTS - extractive body cue:** The robot perceives the environment in the form of height samples from an elevation map constructed from point cloud input, as seen in Figure 3A.
- **p. 3 / 2. RESULTS - extractive body cue:** The robot was robust in these conditions, even when occlusion and surface properties such as high reflectance impeded exteroception.
- **p. 3 / 2. RESULTS - extractive body cue:** Because of the exteroceptive perception, the robot could anticipate the terrain and adapt its motion to achieve fast and smooth walking.
- **p. 5 / 2. RESULTS - extractive body cue:** A trial was considered successful if the robot overcomes the step within 5 seconds.
- **p. 8 / 2. RESULTS - extractive body cue:** The robot was commanded to walk up and down two steps of stairs.
- **p. 8 / 2. RESULTS - extractive body cue:** We placed each obstacle ahead of the robot and commanded the robot to walk forward at a constant velocity.
- **p. 6 / 2. RESULTS - extractive body cue:** Our locomotion controller perceives the environment through height samples (red dots) from an elevation map (A).
- **p. 6 / 2. RESULTS - extractive body cue:** Research Article ETH Zurich and Intel 6 B Reflective ground D Overhanging objects E Non rigid obstacles F Pose estimation drift C Deep snow G ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** legged robot, terrain과 contact dynamics.
- **Input boundary:** proprioception, terrain/perception observation과 velocity command.
- **Output/decision under evaluation:** joint target, torque, footstep 또는 locomotion action.
- **Primary target:** velocity/progress, stability, energy와 terrain generalization.
- **Detected evaluation headings:** 2. RESULTS (p. 3).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 2. RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | First, we compared the success rate of overcoming fixed-height steps as shown in Figure 4A. | p. 5 (2. RESULTS) |
| 2. RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | The success rate of the proprioceptive baseline dropped at 20 cm step height when the front legs started frequently getting stuck at the step ... | p. 5 (2. RESULTS) |
| 2. RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Because of the exteroceptive perception, the robot could anticipate the terrain and adapt its motion to achieve fast and smooth walking. | p. 3 (2. RESULTS) |
| 2. RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | The sensors perceived the foam block as solid and the robot consequently prepared to step on it but could not achieve a stable foothold ... | p. 8 (2. RESULTS) |
| 2. RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | ANYmal successfully traversed challenging natural environments with steep inclination, slippery surfaces, grass, and snow (Figure 1 A-J). | p. 3 (2. RESULTS) |

## Dataset / Benchmark Role

- **p. 5 / 2. RESULTS - extractive body cue:** The robot perceives the environment in the form of height samples from an elevation map constructed from point cloud input, as seen in Figure 3A.
- **p. 3 / 2. RESULTS - extractive body cue:** The robot was robust in these conditions, even when occlusion and surface properties such as high reflectance impeded exteroception.
- **p. 3 / 2. RESULTS - extractive body cue:** Because of the exteroceptive perception, the robot could anticipate the terrain and adapt its motion to achieve fast and smooth walking.
- **p. 5 / 2. RESULTS - extractive body cue:** A trial was considered successful if the robot overcomes the step within 5 seconds.
- **p. 8 / 2. RESULTS - extractive body cue:** The robot was commanded to walk up and down two steps of stairs.
- **p. 8 / 2. RESULTS - extractive body cue:** We placed each obstacle ahead of the robot and commanded the robot to walk forward at a constant velocity.
- **p. 6 / 2. RESULTS - extractive body cue:** Our locomotion controller perceives the environment through height samples (red dots) from an elevation map (A).
- **p. 6 / 2. RESULTS - extractive body cue:** Research Article ETH Zurich and Intel 6 B Reflective ground D Overhanging objects E Non rigid obstacles F Pose estimation drift C Deep snow G ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1. Robust locomotion in the wild. The presented locomotion controller was extensively tested in a variety of complex environments over multiple seasons. The controller ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2. A hike on the Etzel mountain in Switzerland, completed by ANYmal with our locomotion controller. The 2.2km route - with 120m of elevation ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3. Our locomotion controller perceives the environment through height samples (red dots) from an elevation map (A). The controller is ro- bust to many ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 4. Internal belief state inspection during perceptive failure using a learned belief decoder. Red dots indicate height samples given as input to the policy. ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 5. Overview of the training methods and deployment. We first train a teacher policy with access to privileged simulation data using re- inforcement learning ...
- **p. 13 / Figure/Table caption - extractive body cue:** Fig. 6. Details of robust terrain perception components. (A) During student training, random noise is added to the height samples. The noise is sampled from ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The robot perceives the environment in the form of height samples from an elevation map constructed from point cloud input, as seen in Figure ... | embodiment, simulator version and control stack | p. 5 (2. RESULTS), p. 3 (2. RESULTS) |
| Task/environment | The robot was robust in these conditions, even when occlusion and surface properties such as high reflectance impeded exteroception. | reset, timeout, object/scene variation | p. 3 (2. RESULTS), p. 3 (2. RESULTS) |
| Observation/sensor | proprioception, terrain/perception observation과 velocity command | calibration, preprocessing, privileged input | p. 3 (1. INTRODUCTION), p. 3 (1. INTRODUCTION) |
| Output/decision | joint target, torque, footstep 또는 locomotion action | action frame, controller and termination | p. 10 (1. Teacher policy training), p. 8 (4. MATERIALS AND METHODS) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| First, we compared the success rate of overcoming fixed-height steps as shown in Figure 4A. | definition/direction/unit from same section | p. 5 (2. RESULTS) |
| The success rate of the proprioceptive baseline dropped at 20 cm step height when the front legs started frequently getting stuck at the step ... | definition/direction/unit from same section | p. 5 (2. RESULTS) |
| Evaluating robustness with belief state visualization To examine how our controller integrates proprioception and exteroception, we conducted a number of controlled experiments. | definition/direction/unit from same section | p. 8 (2. RESULTS) |
| ANYmal successfully traversed challenging natural environments with steep inclination, slippery surfaces, grass, and snow (Figure 1 A-J). | definition/direction/unit from same section | p. 3 (2. RESULTS) |
| Our locomotion controller perceives the environment through height samples (red dots) from an elevation map (A). | definition/direction/unit from same section | p. 6 (2. RESULTS) |
| The controller is robust to many perception challenges commonly encountered in the field: missing map information due to sensing failure (B, C, G) and ... | definition/direction/unit from same section | p. 6 (2. RESULTS) |
| Further quantitative performance evaluation is provided in the supplementary section S2. | definition/direction/unit from same section | p. 8 (2. RESULTS) |
| Fig. 4. Internal belief state inspection during perceptive failure using a learned belief decoder. Red dots indicate height samples given as input to the ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We compared our controller to a proprioceptive baseline [4] that does not use exteroception. | comparison identity and matched condition | p. 5 (2. RESULTS) |
| The baseline, on the other hand, failed to track the path without human assistance. | comparison identity and matched condition | p. 5 (2. RESULTS) |
| For traversing stairs, the state-of-the-art quadrupedal robot Spot from Boston Dynamics requires that a dedicated mode is engaged, and the robot must be properly ... | comparison identity and matched condition | p. 3 (2. RESULTS) |
| Baseline Time to complete 75 sec. with help 29 sec. | comparison identity and matched condition | p. 7 (2. RESULTS) |
| D B 20 cm step command command 20 cm step command command H command command ours baseline 27cm 22cm E F ours baseline | comparison identity and matched condition | p. 7 (2. RESULTS) |
| Research Article ETH Zurich and Intel 8 the baseline policy and ours. | comparison identity and matched condition | p. 8 (2. RESULTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The baseline, on the other hand, failed to track the path without human assistance. | component/input/data sensitivity | p. 5 (2. RESULTS) |
| Our controller followed the given path smoothly without any assistance, as shown in Figure 4C. | component/input/data sensitivity | p. 5 (2. RESULTS) |
| With an unobstructed sensor, the controller traversed the stairs gracefully, without any unintended contact with the stair risers, adjusting its footholds and body posture ... | component/input/data sensitivity | p. 8 (2. RESULTS) |
| Fig. 6. Details of robust terrain perception components. (A) During student training, random noise is added to the height samples. The noise is sampled ... | component/input/data sensitivity | p. 13 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our method consists of three stages, illustrated in Figure 6. | First, we compared the success rate of overcoming fixed-height steps as shown in Figure 4A. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (2. RESULTS), p. 5 (2. RESULTS), p. 3 (2. RESULTS), p. 8 (2. RESULTS), p. 3 (2. RESULTS), p. 8 (2. RESULTS) |
| Primary metric/result | The success rate of the proprioceptive baseline dropped at 20 cm step height when the front legs started frequently getting stuck at the step ... | numeric claim only at cited anchor | p. 5 (2. RESULTS) |

- Numeric sentences retained from the body:
- **p. 5 / 2. RESULTS - extractive body cue:** Wooden steps of various height (from 12 cm to 36.5 cm) were placed ahead of the robot, which performed 10 trials to overcome each step ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 4. Internal belief state inspection during perceptive failure using a learned belief decoder. Red dots indicate height samples given as input to the ... | p. 9 (Figure/Table caption) |
| body limitation/failure cue | Fig. 1. Robust locomotion in the wild. The presented locomotion controller was extensively tested in a variety of complex environments over multiple seasons. The ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | Fig. 6. Details of robust terrain perception components. (A) During student training, random noise is added to the height samples. The noise is sampled ... | p. 13 (Figure/Table caption) |
| body limitation/failure cue | Until this height, the dominating failure reason was the robot evading the step sideways instead of falling. | p. 5 (2. RESULTS) |
| body limitation/failure cue | As shown in Figure 3 B-G, the estimated elevation map can unreliable due to sensing failures, limitations of the 2.5D height map representation, or ... | p. 5 (2. RESULTS) |
| body limitation/failure cue | The controller is robust to many perception challenges commonly encountered in the field: missing map information due to sensing failure (B, C, G) and ... | p. 6 (2. RESULTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Wooden steps of various height (from 12 cm to 36.5 cm) were placed ahead of the robot, which performed 10 trials to overcome each ... | p. 5 (2. RESULTS) |
| In contrast, our controller reliably traversed steps of up to 30.5 cm in height. | p. 5 (2. RESULTS) |
| The robot was commanded to walk up and down two steps of stairs. | p. 8 (2. RESULTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 4. Internal belief state inspection during perceptive failure using a learned belief decoder. Red dots indicate height samples given as input to the policy. ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1. Robust locomotion in the wild. The presented locomotion controller was extensively tested in a variety of complex environments over multiple seasons. The controller ...
- **p. 13 / Figure/Table caption - extractive body cue:** Fig. 6. Details of robust terrain perception components. (A) During student training, random noise is added to the height samples. The noise is sampled from ...
- **p. 5 / 2. RESULTS - extractive body cue:** Until this height, the dominating failure reason was the robot evading the step sideways instead of falling.
- **p. 5 / 2. RESULTS - extractive body cue:** As shown in Figure 3 B-G, the estimated elevation map can unreliable due to sensing failures, limitations of the 2.5D height map representation, or viewpoint ...
- **p. 6 / 2. RESULTS - extractive body cue:** The controller is robust to many perception challenges commonly encountered in the field: missing map information due to sensing failure (B, C, G) and misleading ...

- **PDF anchors reviewed:** datasets p. 5 (2. RESULTS), p. 3 (2. RESULTS), p. 3 (2. RESULTS), p. 5 (2. RESULTS), p. 8 (2. RESULTS), p. 8 (2. RESULTS), metrics p. 5 (2. RESULTS), p. 5 (2. RESULTS), p. 8 (2. RESULTS), p. 3 (2. RESULTS), p. 6 (2. RESULTS), p. 6 (2. RESULTS), baselines p. 5 (2. RESULTS), p. 5 (2. RESULTS), p. 3 (2. RESULTS), p. 7 (2. RESULTS), p. 7 (2. RESULTS), p. 8 (2. RESULTS), results p. 5 (2. RESULTS), p. 5 (2. RESULTS), p. 3 (2. RESULTS), p. 8 (2. RESULTS), p. 3 (2. RESULTS), p. 8 (2. RESULTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
