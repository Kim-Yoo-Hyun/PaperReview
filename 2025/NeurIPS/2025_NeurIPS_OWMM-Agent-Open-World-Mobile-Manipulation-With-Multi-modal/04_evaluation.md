# Evaluation - OWMM-Agent: Open World Mobile Manipulation With Multi-modal Agentic Data Synthesis

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (30 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=vSLzoUoJt6; PDF retrieval source: https://openreview.net/pdf/b83bcc6b13bf3bed81ebb73be9bae7cc2be710e7.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (5 Experiments), p. 8 (5 Experiments), p. 8 (Figure/Table caption), p. 24 (Figure/Table caption), p. 27 (C.2 Camera Pose Selection), p. 9 (5 Experiments)): OWMM-VLM-38B model achieved the best performance, and OWMM-VLM-8B model also outperformed the baseline.

## Evaluation Body Digest

- **p. 22 / C.2 Camera Pose Selection - extractive PDF cue:** D Details of Datasets sectionDetails of Datasets D.1 Extra Dataset Construction Details Our evaluation pipeline is constructed using the HomeRobot [40] framework, which serves as ...
- **p. 8 / 4 Dataset - extractive PDF cue:** In each scene, objects were randomly placed for the robot to pick and relocate to another receptacle, with 400 episodes sampled per scene.
- **p. 7 / 4 Dataset - extractive PDF cue:** Stage 2: Trajectory Execution and Data Collection We direct the robot to execute task sequences within the simulator, recording key information at each step: robot ...
- **p. 8 / 4 Dataset - extractive PDF cue:** In our datasets, we also apply a re-labeling process for objects and receptacles, unlike HomeRobot's fixed criteria[40].
- **p. 9 / 5 Experiments - extractive PDF cue:** 5.3 Real world Evaluation In our real-robot experiments, we adopted the mobile manipulation system described in Robi Butler[35] within a real-world home environment.
- **p. 22 / C.2 Camera Pose Selection - extractive PDF cue:** Specifically, we use the simulation part of HomeRobot project, built on Habitat platform [26], with 200 scenes, 150 categories, and 7,892 object instances.
- **p. 7 / 4 Dataset - extractive PDF cue:** Finally, we collect scene graph frames for each episode by sampling robot head-view images at taskrelevant locations (initial and goal receptacles) and additional random positions ...
- **p. 23 / C.2 Camera Pose Selection - extractive PDF cue:** We examine dataset diversity using three 45k-sample sets: 100% scenes and objects, 100% scenes with 30% objects, and 30% scenes with 100% objects.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mobile base와 one/two-arm manipulation environment.
- **Input boundary:** egocentric RGB-D, language/task goal, base-arm proprioception.
- **Output/decision under evaluation:** base motion plus arm/gripper action.
- **Primary target:** long-horizon task success, reachability, collision과 recovery.
- **Detected evaluation headings:** 4 Dataset (p. 6); 5 Experiments (p. 8); 7. Experiment statistical significance (p. 16); 8. Experiments compute resources (p. 17); C Implementation Details (p. 21).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | OWMM-VLM-38B model achieved the best performance, and OWMM-VLM-8B model also outperformed the baseline. | p. 10 (5 Experiments) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | The OWMM-VLM-38B model achieves the best performance across all metrics, demonstrating its superior ability to integrate scene understanding, decision-making, and action generation. *: Since ... | p. 8 (5 Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 3: Agent success rate in OWMM Task. OWMM-VLM-38B model consistently outperforms others across all metrics. | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 5: OVMM-VLM-8B Sub-task Performance with the Increase of Training Data Size. The task scores consistently improve as the training data size increases. in-context ... | p. 24 (Figure/Table caption) |
| C.2 Camera Pose Selection | EMPIRICAL / REAL-ROBOT OR HARDWARE | Bottleneck in object picking/placing actions: While our model achieves strong performance in early stages (88.56% on object image retrieval, 84.64% on robot navigation to ... | p. 27 (C.2 Camera Pose Selection) |

## Dataset / Benchmark Role

- **p. 22 / C.2 Camera Pose Selection - extractive PDF cue:** D Details of Datasets sectionDetails of Datasets D.1 Extra Dataset Construction Details Our evaluation pipeline is constructed using the HomeRobot [40] framework, which serves as ...
- **p. 8 / 4 Dataset - extractive PDF cue:** In each scene, objects were randomly placed for the robot to pick and relocate to another receptacle, with 400 episodes sampled per scene.
- **p. 7 / 4 Dataset - extractive PDF cue:** Stage 2: Trajectory Execution and Data Collection We direct the robot to execute task sequences within the simulator, recording key information at each step: robot ...
- **p. 8 / 4 Dataset - extractive PDF cue:** In our datasets, we also apply a re-labeling process for objects and receptacles, unlike HomeRobot's fixed criteria[40].
- **p. 9 / 5 Experiments - extractive PDF cue:** 5.3 Real world Evaluation In our real-robot experiments, we adopted the mobile manipulation system described in Robi Butler[35] within a real-world home environment.
- **p. 22 / C.2 Camera Pose Selection - extractive PDF cue:** Specifically, we use the simulation part of HomeRobot project, built on Habitat platform [26], with 200 scenes, 150 categories, and 7,892 object instances.
- **p. 7 / 4 Dataset - extractive PDF cue:** Finally, we collect scene graph frames for each episode by sampling robot head-view images at taskrelevant locations (initial and goal receptacles) and additional random positions ...
- **p. 23 / C.2 Camera Pose Selection - extractive PDF cue:** We examine dataset diversity using three 45k-sample sets: 100% scenes and objects, 100% scenes with 30% objects, and 30% scenes with 100% objects.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: OWMM-Agent Operates Fetch Robot for Tidying Task. OWMM-Agent receives natural language instructions and leverages both long-term environment memory (scene images) and transient robot ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: The Overview of OWMM Agent Framework. The left panel represents the world space, including a graph of posed frames generated during the pre-mapping ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: Overview of OWMM-VLM. Our model is fine-tuned on InternVL-2.5[5], comprising a ViT, a 2-layer projection MLP, and a LLM. During training, ViT parameters ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1: Dataset Overview for Instruction Fine-tuning. Our dataset consists of four subsets, each correspond- ing to one of the four primary task actions: Pick, ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: Single-step evaluation of VLM models on OWMM core multi-modal capabilities. The OWMM-VLM-38B model achieves the best performance across all metrics, demonstrating its superior ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3: Agent success rate in OWMM Task. OWMM-VLM-38B model consistently outperforms others across all metrics.
- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 4: Real world single evaluation. OWMM-VLM-38B model achieved the best performance, and OWMM-VLM-8B model also outperformed the baseline. While the baseline model demonstrated relatively ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 5: Demonstration of single step evaluation in real world. These demos showcase OWMM-VLM-38B's outputs, illustrating that even though its training data are drawn entirely ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | D Details of Datasets sectionDetails of Datasets D.1 Extra Dataset Construction Details Our evaluation pipeline is constructed using the HomeRobot [40] framework, which serves ... | embodiment, simulator version and control stack | p. 22 (C.2 Camera Pose Selection), p. 8 (4 Dataset) |
| Task/environment | In each scene, objects were randomly placed for the robot to pick and relocate to another receptacle, with 400 episodes sampled per scene. | reset, timeout, object/scene variation | p. 8 (4 Dataset), p. 7 (4 Dataset) |
| Observation/sensor | egocentric RGB-D, language/task goal, base-arm proprioception | calibration, preprocessing, privileged input | p. 4 (3 Methodology), p. 6 (3 Methodology) |
| Output/decision | base motion plus arm/gripper action | action frame, controller and termination | p. 5 (3 Methodology), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Model/ Task Score Ego-centric Decisionmaking↑ Image Retrieval↑ Affordance Grounding (object)↑ Affordance Grounding (receptacle)↑ Affordance Grounding (navigation)↑ Time Consumption(s)↓ OWMM-VLM-38B(ours) 97.85% 87.54% 0.97(±0.14) 0.94(± ... | definition/direction/unit from same section | p. 8 (5 Experiments) |
| 3) Robot close to: The success rate of robot staying within 1.5m or 2.0m of the object or goal receptacle before picking or placing. | definition/direction/unit from same section | p. 9 (5 Experiments) |
| Additionally, we introduce three metrics to assess subgoals: 1) Image retrieval: Success rate in locating object and goal receptacles from multiple posed images. | definition/direction/unit from same section | p. 9 (5 Experiments) |
| As performance gains plateau, egocentric decision making approaches a success rate of 1.0, whereas image retrieval lingers at approximately 0.8. | definition/direction/unit from same section | p. 24 (C.2 Camera Pose Selection) |
| Table 3: Agent success rate in OWMM Task. OWMM-VLM-38B model consistently outperforms others across all metrics. | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Table 6: Results with different data diversity data scales. The best performance across training sets with different scales is indicated with bold font. Besides, ... | definition/direction/unit from same section | p. 24 (Figure/Table caption) |
| This cascading effect accounts for the performance gap between single-step and episodic evaluations, as errors in object retrieval or navigation prevent the robot from ... | definition/direction/unit from same section | p. 27 (C.2 Camera Pose Selection) |
| While the baseline model demonstrated relatively strong affordance grounding capabilities for objects, its poor performance in action decisionmaking led to incorrect navigation. | definition/direction/unit from same section | p. 10 (5 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| OWMM-VLM-38B model achieved the best performance, and OWMM-VLM-8B model also outperformed the baseline. | comparison identity and matched condition | p. 10 (5 Experiments) |
| J Qualitative Evaluation We provide the qualitative evaluation of our OWMM-VLM model compared to other baseline models. | comparison identity and matched condition | p. 28 (C.2 Camera Pose Selection) |
| OWMM-VLM-38B model consistently outperforms others across all metrics. | comparison identity and matched condition | p. 8 (5 Experiments) |
| Our model excels in decision-making, achieving state-of-the-art results in image retrieval and affordance grounding. | comparison identity and matched condition | p. 9 (5 Experiments) |
| This advantage directly translates into higher overall accuracy compared to methods that employ GPT-4o as the agent. | comparison identity and matched condition | p. 9 (5 Experiments) |
| While the baseline model demonstrated relatively strong affordance grounding capabilities for objects, its poor performance in action decisionmaking led to incorrect navigation. | comparison identity and matched condition | p. 10 (5 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Hence, its effect is briefly shown only in the ablation study. | component/input/data sensitivity | p. 26 (C.2 Camera Pose Selection) |
| For the ablation study on model design, such as the choice of generating bounding boxes rather than points, please see Appendix G. | component/input/data sensitivity | p. 8 (5 Experiments) |
| G Ablation Study on OWMM-VLM The ablation study evaluates the contributions of the components of the OWMM-VLM model. | component/input/data sensitivity | p. 26 (C.2 Camera Pose Selection) |
| Figure 1: OWMM-Agent Operates Fetch Robot for Tidying Task. OWMM-Agent receives natural language instructions and leverages both long-term environment memory (scene images) and transient ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| This increases robustness to natural language variation without compromising annotation precision. | component/input/data sensitivity | p. 7 (4 Dataset) |
| Regarding the model's architecture, we have trained two variants consisting of 8 billion and 38 billion parameters, based on the pre-trained model from InternVL-2.5[5]. | component/input/data sensitivity | p. 21 (C Implementation Details) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are as follows: • We propose OWMM-Agent, a unified VLM-based agent architecture for open-world mobile manipulation, capable of global scene ... | OWMM-VLM-38B model achieved the best performance, and OWMM-VLM-8B model also outperformed the baseline. | PDF body cue; verify exact table/figure and matched conditions | p. 10 (5 Experiments), p. 8 (5 Experiments), p. 8 (Figure/Table caption), p. 24 (Figure/Table caption), p. 27 (C.2 Camera Pose Selection), p. 9 (5 Experiments) |
| Primary metric/result | The OWMM-VLM-38B model achieves the best performance across all metrics, demonstrating its superior ability to integrate scene understanding, decision-making, and action generation. *: Since ... | numeric claim only at cited anchor | p. 8 (5 Experiments) |

- Numeric sentences retained from the body:
- **p. 8 / 4 Dataset - extractive PDF cue:** 4.2 Dataset Analysis We used 143 scenes from The Habitat Synthetic Scenes Dataset (HSSD) [13] and combined objects from YCB Objects [3] and Google Scanned ...
- **p. 8 / 4 Dataset - extractive PDF cue:** In each scene, objects were randomly placed for the robot to pick and relocate to another receptacle, with 400 episodes sampled per scene.
- **p. 21 / C Implementation Details - extractive PDF cue:** As for the training time, OWMM-VLM-8B is trained on 8X NVIDIA A100 GPUs for about 7 hours, and OWMM-VLM-38B is trained on 24X NVIDIA A100 ...
- **p. 21 / C Implementation Details - extractive PDF cue:** Both our models were trained for 1 epoch.
- **p. 22 / C.2 Camera Pose Selection - extractive PDF cue:** Specifically, we use the simulation part of HomeRobot project, built on Habitat platform [26], with 200 scenes, 150 categories, and 7,892 object instances.
- **p. 22 / C.2 Camera Pose Selection - extractive PDF cue:** Besides, we allocated 157 objects between the training and validation sets with a ratio of 137:20, ensuring that the testing set contained entirely unseen objects.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | H Failure Mode Analysis To better understand the limitations and bottlenecks of our system, we conducted a comprehensive failure analysis on 100 randomly selected ... | p. 27 (C.2 Camera Pose Selection) |
| body limitation/failure cue | Episodic evaluations in simulated environments further confirmed the OWMM-Agent's superior success rates and robustness against common failure modes like dead loops, while real-world tests ... | p. 10 (6 Conclusion) |
| body limitation/failure cue | Future work will focus on addressing limitations like pre-mapping reliance and enhancing cross-embodiment adaptability for more complex manipulation tasks. | p. 10 (6 Conclusion) |
| body limitation/failure cue | Since the current evaluation pipeline does not support automatic failure case analysis, we manually reviewed the action sequences and categorized failures into four distinct ... | p. 27 (C.2 Camera Pose Selection) |
| body limitation/failure cue | Additional analysis including failure mode categorization (Appendix H) and computational efficiency with varying frame counts (Appendix I) are also available in the appendix. | p. 8 (5 Experiments) |
| body limitation/failure cue | We provide a comprehensive failure mode analysis categorizing 100 failed episodes in Appendix H. | p. 9 (5 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| I Computational Efficiency Analysis To address concerns about real-world deployment efficiency and scalability to large scenes, we conducted experiments evaluating GPU memory consumption and ... | p. 27 (C.2 Camera Pose Selection) |
| As for the training time, OWMM-VLM-8B is trained on 8X NVIDIA A100 GPUs for about 7 hours, and OWMM-VLM-38B is trained on 24X NVIDIA ... | p. 21 (C Implementation Details) |
| For the 8B model, doubling frames from 8+1 to 16+1 increases inference time by only 46% (4.84s to 7.09s). | p. 28 (C.2 Camera Pose Selection) |
| Input Frames Prompt Tokens Time (s) Memory (GB) 8+1 (default) 2810.37 4.39 98.22 16+1 4922.37 5.04 99.13 32+1 9146.37 7.34 100.65 64+1 17594.37 15.33 ... | p. 28 (C.2 Camera Pose Selection) |
| We then select 10 test samples from the sequence of the robot's head view during its run. | p. 9 (5 Experiments) |
| 3) Affordance Grounding: Instead of predicting points directly like in [42, 25], OWMM-VLM outputs a bounding box, from which we compute the center as ... | p. 9 (5 Experiments) |
| This section provides comprehensive implementation details for the pre-mapping stage and camera pose selection, which are essential for reproducing our approach. | p. 21 (C.1 Pre-mapping) |
| More specifically, RobiButler uses Gmapping [9] algorithm to compute the 2D occupancy map from lidar data. | p. 22 (C.1 Pre-mapping) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 27 / C.2 Camera Pose Selection - extractive PDF cue:** H Failure Mode Analysis To better understand the limitations and bottlenecks of our system, we conducted a comprehensive failure analysis on 100 randomly selected failed ...
- **p. 10 / 6 Conclusion - extractive PDF cue:** Episodic evaluations in simulated environments further confirmed the OWMM-Agent's superior success rates and robustness against common failure modes like dead loops, while real-world tests on ...
- **p. 10 / 6 Conclusion - extractive PDF cue:** Future work will focus on addressing limitations like pre-mapping reliance and enhancing cross-embodiment adaptability for more complex manipulation tasks.
- **p. 27 / C.2 Camera Pose Selection - extractive PDF cue:** Since the current evaluation pipeline does not support automatic failure case analysis, we manually reviewed the action sequences and categorized failures into four distinct types: ...
- **p. 8 / 5 Experiments - extractive PDF cue:** Additional analysis including failure mode categorization (Appendix H) and computational efficiency with varying frame counts (Appendix I) are also available in the appendix.
- **p. 9 / 5 Experiments - extractive PDF cue:** We provide a comprehensive failure mode analysis categorizing 100 failed episodes in Appendix H.

- **PDF anchors reviewed:** datasets p. 22 (C.2 Camera Pose Selection), p. 8 (4 Dataset), p. 7 (4 Dataset), p. 8 (4 Dataset), p. 9 (5 Experiments), p. 22 (C.2 Camera Pose Selection), metrics p. 8 (5 Experiments), p. 9 (5 Experiments), p. 9 (5 Experiments), p. 24 (C.2 Camera Pose Selection), p. 8 (Figure/Table caption), p. 24 (Figure/Table caption), baselines p. 10 (5 Experiments), p. 28 (C.2 Camera Pose Selection), p. 8 (5 Experiments), p. 9 (5 Experiments), p. 9 (5 Experiments), p. 10 (5 Experiments), results p. 10 (5 Experiments), p. 8 (5 Experiments), p. 8 (Figure/Table caption), p. 24 (Figure/Table caption), p. 27 (C.2 Camera Pose Selection), p. 9 (5 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
