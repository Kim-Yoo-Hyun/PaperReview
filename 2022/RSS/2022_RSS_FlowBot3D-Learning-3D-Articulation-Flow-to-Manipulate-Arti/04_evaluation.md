# Evaluation - FlowBot3D: Learning 3D Articulation Flow to Manipulate Articulated Objects

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2205.04382; PDF retrieval source: https://arxiv.org/pdf/2205.04382. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (IV. RESULTS), p. 7 (IV. RESULTS), p. 6 (IV. RESULTS), p. 5 (IV. RESULTS), p. 5 (IV. RESULTS), p. 6 (IV. RESULTS)): Notice that even with occlusions, such as in the intermediate mini-fridge observation, the network is able to predict reasonable 3D articulation flow vectors for downstream policy. steps, terminating earlier if ...

## Evaluation Body Digest

- **p. 7 / IV. RESULTS - extractive body cue:** Real-World Experiments To evaluate the performance of FlowBot3D when executed in a real robotic environment, we design a set of of realworld experiments in which ...
- **p. 2 / 4) Simulated experiments to test the performance of our - extractive body cue:** 5) Real-world experiments deployed on a Sawyer robot to test the generalizablity and feasibility of our system in real-world scenarios.
- **p. 5 / IV. RESULTS - extractive body cue:** The PartNet-Mobility dataset contains 46 categories of articulated objects; following UMPNet [39], we consider a subset of PartNet-Mobility containing 21 classes, split into 11 training ...
- **p. 2 / 4) Simulated experiments to test the performance of our - extractive body cue:** system in articulating a wide range of PartNet-Mobility dataset objects.
- **p. 5 / IV. RESULTS - extractive body cue:** Simulation Results To evaluate our method in simulation, we implement a suction gripper in the ManiSkill environment [27], which serves as a simulation interface for ...
- **p. 7 / IV. RESULTS - extractive body cue:** For each trial, the object is placed in the scene at a random position such that the articulations are visible and the robot can reach ...
- **p. 8 / IV. RESULTS - extractive body cue:** As in our simulated experiments, we use a single model trained in simulation across multiple object categories without any further finetuning. # Objects 2 1 ...
- **p. 8 / IV. RESULTS - extractive body cue:** See Figure 5 and Table III for a summary of the dataset, and the supplementary materials for specifics for each object.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4) Simulated experiments to test the performance of our (p. 2); IV. RESULTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| IV. RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Notice that even with occlusions, such as in the intermediate mini-fridge observation, the network is able to predict reasonable 3D articulation flow vectors for ... | p. 8 (IV. RESULTS) |
| IV. RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | First, our formulation of FlowBot3D has a very high success rate across all categories, including test categories, which are completely novel types of objects ... | p. 7 (IV. RESULTS) |
| IV. RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | At test time, we select the contact point based on ground-truth 3DAF, and after contact 4We could not yet compare directly to UMPNet, as ... | p. 6 (IV. RESULTS) |
| IV. RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Results are shown in Tables VI and VII3. | p. 5 (IV. RESULTS) |
| IV. RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Simulation Results To evaluate our method in simulation, we implement a suction gripper in the ManiSkill environment [27], which serves as a simulation interface ... | p. 5 (IV. RESULTS) |

## Dataset / Benchmark Role

- **p. 7 / IV. RESULTS - extractive body cue:** Real-World Experiments To evaluate the performance of FlowBot3D when executed in a real robotic environment, we design a set of of realworld experiments in which ...
- **p. 2 / 4) Simulated experiments to test the performance of our - extractive body cue:** 5) Real-world experiments deployed on a Sawyer robot to test the generalizablity and feasibility of our system in real-world scenarios.
- **p. 5 / IV. RESULTS - extractive body cue:** The PartNet-Mobility dataset contains 46 categories of articulated objects; following UMPNet [39], we consider a subset of PartNet-Mobility containing 21 classes, split into 11 training ...
- **p. 2 / 4) Simulated experiments to test the performance of our - extractive body cue:** system in articulating a wide range of PartNet-Mobility dataset objects.
- **p. 5 / IV. RESULTS - extractive body cue:** Simulation Results To evaluate our method in simulation, we implement a suction gripper in the ManiSkill environment [27], which serves as a simulation interface for ...
- **p. 7 / IV. RESULTS - extractive body cue:** For each trial, the object is placed in the scene at a random position such that the articulations are visible and the robot can reach ...
- **p. 8 / IV. RESULTS - extractive body cue:** As in our simulated experiments, we use a single model trained in simulation across multiple object categories without any further finetuning. # Objects 2 1 ...
- **p. 8 / IV. RESULTS - extractive body cue:** See Figure 5 and Table III for a summary of the dataset, and the supplementary materials for specifics for each object.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: FlowBot3D in action. The system first observes the initial con- figuration of the object of interest, estimates the per-point articulation flow of the ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: Illustrations of prismatic and revolute joints. We now consider an idealized policy to actuate an articu- lated object. Suppose we are able to ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: FlowBot3D System Overview. Our system in deployment has two phases: the Grasp-Selection phase and the Articulation-Execution Phase. The dark red dots represent the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4: Workspace setup for physical experiments. The sensory signal comes from an Azure Kinect depth camera, and the agent is a Sawyer BLACK robot. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Fourteen test objects for our real-world experiments. Please refer to Supplementary Material for the exact category of each object. on trajectories provided by ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6: Real world examples of FlowBot3D executing an articulation policy based on predicting 3D Articulated Flow. Notice that even with occlusions, such as in ...
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 7: Simulated rollout examples Novel Instances in Train Categories Test Categories AVG. AVG. Baselines UMPNet 0.18 0.18 0.17 0.32
- **p. 16 / Figure/Table caption - extractive body cue:** Fig. 8: Objects in the dataset for real world experiments

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Real-World Experiments To evaluate the performance of FlowBot3D when executed in a real robotic environment, we design a set of of realworld experiments in ... | embodiment, simulator version and control stack | p. 7 (IV. RESULTS), p. 2 (4) Simulated experiments to test the performance of our) |
| Task/environment | 5) Real-world experiments deployed on a Sawyer robot to test the generalizablity and feasibility of our system in real-world scenarios. | reset, timeout, object/scene variation | p. 2 (4) Simulated experiments to test the performance of our), p. 5 (IV. RESULTS) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (III. METHOD - FROM THEORY TO PRACTICE), p. 4 (III. METHOD - FROM THEORY TO PRACTICE) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (III. METHOD - FROM THEORY TO PRACTICE), p. 3 (III. METHOD - FROM THEORY TO PRACTICE) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| First, our formulation of FlowBot3D has a very high success rate across all categories, including test categories, which are completely novel types of objects ... | definition/direction/unit from same section | p. 7 (IV. RESULTS) |
| Additionally, our method's accuracy increases when the object is at least partially open, because there is less ambiguity about object structure than when an ... | definition/direction/unit from same section | p. 7 (IV. RESULTS) |
| The higher the better. • Success: We also define a binary success metric, which is computed by thresholding the final resulting normalized distance at ... | definition/direction/unit from same section | p. 6 (IV. RESULTS) |
| Metrics: During our trials, we compute the following metrics for each policy: • Overall Success: Was the object articulated more than 90% of its ... | definition/direction/unit from same section | p. 8 (IV. RESULTS) |
| During our experiments, we calculate two metrics: • Normalized distance: Following Xu et al. | definition/direction/unit from same section | p. 5 (IV. RESULTS) |
| [39], we compute the normalized distance travelled by a specific child link through its range of motion. | definition/direction/unit from same section | p. 5 (IV. RESULTS) |
| We set δ = 0.1, meaning that we define a success as articulating a part for more than 90%. | definition/direction/unit from same section | p. 6 (IV. RESULTS) |
| Notice that even with occlusions, such as in the intermediate mini-fridge observation, the network is able to predict reasonable 3D articulation flow vectors for ... | definition/direction/unit from same section | p. 8 (IV. RESULTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The best BC baseline, DAgger Oracle + F, is only able to fully articulate objects 33% of the time. | comparison identity and matched condition | p. 7 (IV. RESULTS) |
| Please refer to Supplementary Material for the exact category of each object. on trajectories provided by an oracle version of GT 3DAF. • BC ... | comparison identity and matched condition | p. 7 (IV. RESULTS) |
| Baseline Comparisons: We compare our proposed method with several baseline methods: • UMP-DI: We implement a variant4 of UMPNet's Direction Inference network (DistNet) [39], ... | comparison identity and matched condition | p. 6 (IV. RESULTS) |
| We train our models (ArtFlowNet and baselines) exclusively on the training instances of the training object categories, and evaluate by rolling out the corresponding ... | comparison identity and matched condition | p. 5 (IV. RESULTS) |
| In addition, since the camera position in reality is different from that in the ManiSkill environments, we apply a viewpoint augmentation (VPA) at training ... | comparison identity and matched condition | p. 8 (IV. RESULTS) |
| Fig. 7: Simulated rollout examples Novel Instances in Train Categories Test Categories AVG. AVG. Baselines UMPNet 0.18 0.18 0.17 0.32 | comparison identity and matched condition | p. 14 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Baseline Comparisons: We compare our proposed method with several baseline methods: • UMP-DI: We implement a variant4 of UMPNet's Direction Inference network (DistNet) [39], ... | component/input/data sensitivity | p. 6 (IV. RESULTS) |
| Second, none of the Behavior Cloning and DAgger policies, nor their flow-based variants, perform well. | component/input/data sensitivity | p. 7 (IV. RESULTS) |
| In experiments, we use an ArtFlowNet trained without a part mask in the observation space. | component/input/data sensitivity | p. 8 (IV. RESULTS) |
| As in our simulated experiments, we use a single model trained in simulation across multiple object categories without any further finetuning. # Objects 2 ... | component/input/data sensitivity | p. 8 (IV. RESULTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we present FlowBot3D, a deep 3D visionbased robotic system that predicts dense per-point motion of an articulated object in 3D space, ... | Notice that even with occlusions, such as in the intermediate mini-fridge observation, the network is able to predict reasonable 3D articulation flow vectors for ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (IV. RESULTS), p. 7 (IV. RESULTS), p. 6 (IV. RESULTS), p. 5 (IV. RESULTS), p. 5 (IV. RESULTS), p. 6 (IV. RESULTS) |
| Primary metric/result | First, our formulation of FlowBot3D has a very high success rate across all categories, including test categories, which are completely novel types of objects ... | numeric claim only at cited anchor | p. 7 (IV. RESULTS) |

- Numeric sentences retained from the body:
- **p. 7 / IV. RESULTS - extractive body cue:** Our experiment protocol is thus: for each object in the dataset, we conducted 5 trials of each method.
- **p. 8 / IV. RESULTS - extractive body cue:** We conducted one round of evaluation (70 trials in total) for each of the following methods: • FlowBot3D: The version of our generalized articulation policy ...
- **p. 2 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** An Idealized Policy Based On Dynamics and Kinematics The articulated objects we consider in this work are generally objects that 1) consist of one or ...
- **p. 3 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** A hierarchy-free representation of the kinematic properties of the object could assign each point on the object its own set of parameters; however, this would ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Notice that even with occlusions, such as in the intermediate mini-fridge observation, the network is able to predict reasonable 3D articulation flow vectors for ... | p. 8 (IV. RESULTS) |
| body limitation/failure cue | UMPNet Pybullet Environment: The simulation environment used in the original UMPNet evaluations [39] is a PyBullet-based environment with different physical and collision parameters. | p. 7 (IV. RESULTS) |
| body limitation/failure cue | Each object falls into one of either the training or test classes we selected from the PartNet-Mobility. | p. 8 (IV. RESULTS) |
| body limitation/failure cue | Normal Direction estimation suffers from occlusion issues and the normal is not always the correct direction to actuate the object (for example, for the ... | p. 7 (IV. RESULTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| However, the source code to run the UMPNet environment was not available for us to run until after this paper was submitted for review; ... | p. 7 (IV. RESULTS) |
| Details about how our trials are conducted and measurements computed can be found in the supplementary materials. | p. 8 (IV. RESULTS) |
| Metrics: During our trials, we compute the following metrics for each policy: • Overall Success: Was the object articulated more than 90% of its ... | p. 8 (IV. RESULTS) |
| This process repeats in a closed loop fashion until the object has been fully-articulated, a max number of steps has been exceeded, or the ... | p. 4 (III. METHOD - FROM THEORY TO PRACTICE) |
| While contact selection for suction-based grasping is a well-studied problem [3, 23, 24], we find that a simple heuristic performs acceptably; we choose the ... | p. 4 (III. METHOD - FROM THEORY TO PRACTICE) |
| See the supplementary materials for other implementation details. | p. 5 (III. METHOD - FROM THEORY TO PRACTICE) |
| [39], we compute the normalized distance travelled by a specific child link through its range of motion. | p. 5 (IV. RESULTS) |
| The higher the better. • Success: We also define a binary success metric, which is computed by thresholding the final resulting normalized distance at ... | p. 6 (IV. RESULTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / IV. RESULTS - extractive body cue:** Notice that even with occlusions, such as in the intermediate mini-fridge observation, the network is able to predict reasonable 3D articulation flow vectors for downstream ...
- **p. 7 / IV. RESULTS - extractive body cue:** UMPNet Pybullet Environment: The simulation environment used in the original UMPNet evaluations [39] is a PyBullet-based environment with different physical and collision parameters.
- **p. 8 / IV. RESULTS - extractive body cue:** Each object falls into one of either the training or test classes we selected from the PartNet-Mobility.
- **p. 7 / IV. RESULTS - extractive body cue:** Normal Direction estimation suffers from occlusion issues and the normal is not always the correct direction to actuate the object (for example, for the spherical-shaped ...

- **Evidence anchors reviewed:** datasets p. 7 (IV. RESULTS), p. 2 (4) Simulated experiments to test the performance of our), p. 5 (IV. RESULTS), p. 2 (4) Simulated experiments to test the performance of our), p. 5 (IV. RESULTS), p. 7 (IV. RESULTS), metrics p. 7 (IV. RESULTS), p. 7 (IV. RESULTS), p. 6 (IV. RESULTS), p. 8 (IV. RESULTS), p. 5 (IV. RESULTS), p. 5 (IV. RESULTS), baselines p. 7 (IV. RESULTS), p. 7 (IV. RESULTS), p. 6 (IV. RESULTS), p. 5 (IV. RESULTS), p. 8 (IV. RESULTS), p. 14 (Figure/Table caption), results p. 8 (IV. RESULTS), p. 7 (IV. RESULTS), p. 6 (IV. RESULTS), p. 5 (IV. RESULTS), p. 5 (IV. RESULTS), p. 6 (IV. RESULTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Real-World Experiments To evaluate the performance of FlowBot3D when executed in a real robotic environment, we design a set of of realworld experiments in which we attempt to articulate a ... (p. 7, IV. RESULTS).
- **Metric evidence:** Metrics: During our trials, we compute the following metrics for each policy: • Overall Success: Was the object articulated more than 90% of its range of motion (defined per-object)? • ... (p. 8, IV. RESULTS).
- **Baseline/ablation evidence:** Baseline Comparisons: We compare our proposed method with several baseline methods: • UMP-DI: We implement a variant4 of UMPNet's Direction Inference network (DistNet) [39], where instead of bootstrapping an action ... (p. 6, IV. RESULTS).
- **Failure/negative evidence:** However, the remaining failure modes raise questions we would like to explore in future work. (p. 9, V. CONCLUSION).
