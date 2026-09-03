# Evaluation - Graph2Nav: 3D Object-Relation Graph Generation to Robot Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.proceedings.com/content/081/081087webtoc.pdf; PDF retrieval source: https://arxiv.org/pdf/2504.16782v1. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS)): Combining observations from different 2D images shall improve the robustness and accuracy in depicting the actual relationships among 3D objects in the real world.

## Evaluation Body Digest

- **p. 6 / V. EXPERIMENTS - extractive body cue:** Therefore, once the robot starts the task, it will first look around to build the initial scene graph of the perceived environment using Graph2Nav.
- **p. 4 / V. EXPERIMENTS - extractive body cue:** Datasets from these environments are ranged roughly from a half kilometer to a kilometer in total trajectory length, except the second indoor environment (around 250 ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** The robot then will set up and execute a search plan for finding the target object based on LLM's knowledge of the perceived environment.
- **p. 4 / V. EXPERIMENTS - extractive body cue:** It includes typical objects inside urban scenes, such as cars and poles.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** The user can therefore assign a navigation task (such as finding a backpack) to the robot via voice commands.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** We also manually label the object relations, based on the definition in [20], among the representative objects inside the collected datasets.
- **p. 4 / V. EXPERIMENTS - extractive body cue:** First, we validate the accuracy of our generated 3D scene graphs for both indoor and outdoor scenes in the real world.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Combining observations from different 2D images shall improve the robustness and accuracy in depicting the actual relationships among 3D objects in the real world.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** V. EXPERIMENTS (p. 4).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| V. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Combining observations from different 2D images shall improve the robustness and accuracy in depicting the actual relationships among 3D objects in the real world. | p. 5 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Clearly, Graph2Nav greatly improves the capability in detecting correct relationships among the objects, compared to 2D-based method. | p. 5 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | First, we validate the accuracy of our generated 3D scene graphs for both indoor and outdoor scenes in the real world. | p. 4 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Note the accuracy of our mapped 3D point cloud and the estimated platform pose relies on the underlying SLAM system (LIO-SAM [23] in our ... | p. 4 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | From the results, we found that the LLM is able to utilize the object-relations to design more efficient plans to search objects. | p. 6 (V. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 6 / V. EXPERIMENTS - extractive body cue:** Therefore, once the robot starts the task, it will first look around to build the initial scene graph of the perceived environment using Graph2Nav.
- **p. 4 / V. EXPERIMENTS - extractive body cue:** Datasets from these environments are ranged roughly from a half kilometer to a kilometer in total trajectory length, except the second indoor environment (around 250 ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** The robot then will set up and execute a search plan for finding the target object based on LLM's knowledge of the perceived environment.
- **p. 4 / V. EXPERIMENTS - extractive body cue:** It includes typical objects inside urban scenes, such as cars and poles.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** The user can therefore assign a navigation task (such as finding a backpack) to the robot via voice commands.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** We also manually label the object relations, based on the definition in [20], among the representative objects inside the collected datasets.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: 3D scene graphs constructed using Graph2Nav for outdoor (left) and indoor (right) scenes. The graph includes a hierarchy (from top to bottom): a ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: The process flow diagram for Graph2Nav. A pose graph-based SLAM system is utilized to provide real-time pose estimations for received image and point ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Same as [1]-[6], we manually define the layers in the 3D scene graph. Our definition aims to find a general and consistent hierarchy ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: Two examples of object-relations ("beside" and "on" top of) from portions of our generated 3D scene graphs (top) with their correspondent 2D images ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: An example of the impact from object-relations to the search plan (yellow trajectory in bottom-left picture and bottom- right picture) executed by our ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Therefore, once the robot starts the task, it will first look around to build the initial scene graph of the perceived environment using Graph2Nav. | embodiment, simulator version and control stack | p. 6 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS) |
| Task/environment | Datasets from these environments are ranged roughly from a half kilometer to a kilometer in total trajectory length, except the second indoor environment (around ... | reset, timeout, object/scene variation | p. 4 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 3 (III. GRAPH2NAV), p. 3 (III. GRAPH2NAV) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 1 (I. INTRODUCTION), p. 1 (Abstract) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| First, we validate the accuracy of our generated 3D scene graphs for both indoor and outdoor scenes in the real world. | definition/direction/unit from same section | p. 4 (V. EXPERIMENTS) |
| Combining observations from different 2D images shall improve the robustness and accuracy in depicting the actual relationships among 3D objects in the real world. | definition/direction/unit from same section | p. 5 (V. EXPERIMENTS) |
| Note the accuracy of our mapped 3D point cloud and the estimated platform pose relies on the underlying SLAM system (LIO-SAM [23] in our ... | definition/direction/unit from same section | p. 4 (V. EXPERIMENTS) |
| The third row describes errors from our proposed graph generation framework. | definition/direction/unit from same section | p. 5 (V. EXPERIMENTS) |
| Without object-relations, the LLM generates the initial search plan based on (1) the distances to different large objects inside the environment, and (2) the ... | definition/direction/unit from same section | p. 6 (V. EXPERIMENTS) |
| For each scenario, we also evaluate the impact of the object-relations, which do not exist in [16], from the 3D scene graphs generated from ... | definition/direction/unit from same section | p. 6 (V. EXPERIMENTS) |
| Fig. 1: 3D scene graphs constructed using Graph2Nav for outdoor (left) and indoor (right) scenes. The graph includes a hierarchy (from top to bottom): ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Fig. 2: The process flow diagram for Graph2Nav. A pose graph-based SLAM system is utilized to provide real-time pose estimations for received image and ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We measure 3D coordinates of a set of representative 3D objects using state-of-the-art survey techniques inside these three environments. | comparison identity and matched condition | p. 4 (V. EXPERIMENTS) |
| Clearly, Graph2Nav greatly improves the capability in detecting correct relationships among the objects, compared to 2D-based method. | comparison identity and matched condition | p. 5 (V. EXPERIMENTS) |
| It means the robot does two trials (one uses the graph without relations, and the other uses the entire graph with object relations from ... | comparison identity and matched condition | p. 6 (V. EXPERIMENTS) |
| Without object-relations, the LLM generates the initial search plan based on (1) the distances to different large objects inside the environment, and (2) the ... | comparison identity and matched condition | p. 6 (V. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| It means the robot does two trials (one uses the graph without relations, and the other uses the entire graph with object relations from ... | component/input/data sensitivity | p. 6 (V. EXPERIMENTS) |
| Without object-relations, the LLM generates the initial search plan based on (1) the distances to different large objects inside the environment, and (2) the ... | component/input/data sensitivity | p. 6 (V. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contributions are summarized as follows: • We propose Graph2Nav, a new real-time 3D objectrelation graph generation framework that combines strengths of 2D ... | Combining observations from different 2D images shall improve the robustness and accuracy in depicting the actual relationships among 3D objects in the real world. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Primary metric/result | Clearly, Graph2Nav greatly improves the capability in detecting correct relationships among the objects, compared to 2D-based method. | numeric claim only at cited anchor | p. 5 (V. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 4 / V. EXPERIMENTS - extractive body cue:** The 3D LiDAR has a detection range of 40 meters and a field-of-view (FOV) of 360-by-59 degrees.
- **p. 4 / V. EXPERIMENTS - extractive body cue:** The Realsense camera has one RGB and two infrared imaging sensors, which have a FOV of 90-by-65 degrees.
- **p. 4 / V. EXPERIMENTS - extractive body cue:** Our system can recognize 133 object classes and 56 object relationships across both indoor and outdoor scenes.
- **p. 4 / V. EXPERIMENTS - extractive body cue:** Datasets from these environments are ranged roughly from a half kilometer to a kilometer in total trajectory length, except the second indoor environment (around 250 ...
- **p. 4 / V. EXPERIMENTS - extractive body cue:** There are total 67 measured objects: 32 objects in cafeteria, 38 objects in lab, 22 objects in courtyard, and 13 objects in parking lot.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** With a battery, the robot can operate continuously for up to 2 hours.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | To fulfull this goal, we propose Graph2Nav, a novel real-time 3D object-relation graph generation framework that addresses current limitations to robot navigation. | p. 6 (VI. CONCLUSIONS AND DISCUSSION) |
| body limitation/failure cue | The plan can also be dynamically changed, updated, or replanned during execution, if any failure happens or any new information is received. | p. 6 (V. EXPERIMENTS) |
| body limitation/failure cue | Combining observations from different 2D images shall improve the robustness and accuracy in depicting the actual relationships among 3D objects in the real world. | p. 5 (V. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The second environment is our laboratory space, including typical office objects such as desks, monitors, books, and computers. | p. 4 (V. EXPERIMENTS) |
| We use Nvidia AGX Orin as our onboard computer for Graph2Nav processing and SayNav inference. | p. 5 (V. EXPERIMENTS) |
| It means the robot does two trials (one uses the graph without relations, and the other uses the entire graph with object relations from ... | p. 6 (V. EXPERIMENTS) |
| It separately models the objects and relations in the form of queries from two Transformer decoders, followed by a prompting-like relation-object matching mechanism. | p. 3 (III. GRAPH2NAV) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / VI. CONCLUSIONS AND DISCUSSION - extractive body cue:** To fulfull this goal, we propose Graph2Nav, a novel real-time 3D object-relation graph generation framework that addresses current limitations to robot navigation.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** The plan can also be dynamically changed, updated, or replanned during execution, if any failure happens or any new information is received.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Combining observations from different 2D images shall improve the robustness and accuracy in depicting the actual relationships among 3D objects in the real world.

- **Evidence anchors reviewed:** datasets p. 6 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), metrics p. 4 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), baselines p. 4 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), results p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
