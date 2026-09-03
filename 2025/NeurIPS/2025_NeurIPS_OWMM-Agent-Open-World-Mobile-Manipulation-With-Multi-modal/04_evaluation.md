# Evaluation - OWMM-Agent: Open World Mobile Manipulation With Multi-modal Agentic Data Synthesis

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=vSLzoUoJt6; PDF retrieval source: https://arxiv.org/pdf/2506.04217. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 15 (Figure/Table caption), p. 9 (5 Experiments), p. 7 (5 Experiments), p. 7 (Figure/Table caption), p. 8 (5 Experiments), p. 8 (5 Experiments)): Figure 5: OVMM-VLM-8B Sub-task Performance with the Increase of Training Data Size. The task scores consistently improve as the training data size increases. marginal gains decrease beyond a threshold. As ...

## Evaluation Body Digest

- **p. 7 / 4 Dataset - extractive body cue:** In each scene, objects were randomly placed for the robot to pick and relocate to another receptacle, resulting in 400 episodes per scene for our ...
- **p. 13 / C Implementation Details - extractive body cue:** D Details of Datasets D.1 Extra Dataset Construction Details Our evaluation pipeline is constructed using the HomeRobot[37] framework, which serves as a software structure designed ...
- **p. 7 / 4 Dataset - extractive body cue:** In our datasets, we also apply a re-labeling process for objects and receptacles, unlike HomeRobot's fixed criteria[37].
- **p. 8 / 5 Experiments - extractive body cue:** 5.3 Real world Evaluation In our real-robot experiments, we adopted the mobile manipulation system described in Robi Butler[33] within a real-world home environment.
- **p. 13 / C Implementation Details - extractive body cue:** Specifically, we use the simulation part of HomeRobot project, built on Habitat platform[25], with 200 scenes, 150 categories, and 7892 object instances.
- **p. 14 / C Implementation Details - extractive body cue:** (a) Object Categories (b) Receptacle Categories Figure 4: Word Cloud Distribution of Objects and Receptacles in our dataset D.2 Analysis on the training data This ...
- **p. 14 / C Implementation Details - extractive body cue:** We examine dataset diversity using three 45k-sample sets: 100% scenes and objects, 100% scenes with 30% objects, and 30% scenes with 100% objects.
- **p. 6 / 4 Dataset - extractive body cue:** We then directed the robot to execute task sequences within the simulator, recording key information at each step.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mobile base와 one/two-arm manipulation environment.
- **Input boundary:** egocentric RGB-D, language/task goal, base-arm proprioception.
- **Output/decision under evaluation:** base motion plus arm/gripper action.
- **Primary target:** long-horizon task success, reachability, collision과 recovery.
- **Detected evaluation headings:** 4 Dataset (p. 6); 5 Experiments (p. 7); C Implementation Details (p. 13).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 5: OVMM-VLM-8B Sub-task Performance with the Increase of Training Data Size. The task scores consistently improve as the training data size increases. marginal ... | p. 15 (Figure/Table caption) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | OWMM-VLM-38B model achieved the best performance, and OWMM-VLM-8B model also outperformed the baseline. | p. 9 (5 Experiments) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | The OWMM-VLM-38B model achieves the best performance across all metrics, demonstrating its superior ability to integrate scene understanding, decision-making, and action generation. *: Since ... | p. 7 (5 Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 3: Agent success rate in OWMM Task. OWMM-VLM-38B model consistently outperforms others across all metrics. | p. 7 (Figure/Table caption) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | 3) Robot close to: The success rate of robot staying within 1.5m or 2.0m of the object or goal receptacle before picking or placing. | p. 8 (5 Experiments) |

## Dataset / Benchmark Role

- **p. 7 / 4 Dataset - extractive body cue:** In each scene, objects were randomly placed for the robot to pick and relocate to another receptacle, resulting in 400 episodes per scene for our ...
- **p. 13 / C Implementation Details - extractive body cue:** D Details of Datasets D.1 Extra Dataset Construction Details Our evaluation pipeline is constructed using the HomeRobot[37] framework, which serves as a software structure designed ...
- **p. 7 / 4 Dataset - extractive body cue:** In our datasets, we also apply a re-labeling process for objects and receptacles, unlike HomeRobot's fixed criteria[37].
- **p. 8 / 5 Experiments - extractive body cue:** 5.3 Real world Evaluation In our real-robot experiments, we adopted the mobile manipulation system described in Robi Butler[33] within a real-world home environment.
- **p. 13 / C Implementation Details - extractive body cue:** Specifically, we use the simulation part of HomeRobot project, built on Habitat platform[25], with 200 scenes, 150 categories, and 7892 object instances.
- **p. 14 / C Implementation Details - extractive body cue:** (a) Object Categories (b) Receptacle Categories Figure 4: Word Cloud Distribution of Objects and Receptacles in our dataset D.2 Analysis on the training data This ...
- **p. 14 / C Implementation Details - extractive body cue:** We examine dataset diversity using three 45k-sample sets: 100% scenes and objects, 100% scenes with 30% objects, and 30% scenes with 100% objects.
- **p. 6 / 4 Dataset - extractive body cue:** We then directed the robot to execute task sequences within the simulator, recording key information at each step.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: OWMM-Agent Operates Fetch Robot for Tidying Task. OWMM-Agent receives natural language instructions and leverages both long-term environment memory (scene images) and transient robot ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: The Overview of OWMM Agent Framework. The left panel represents the world space, including a graph of posed frames generated during the pre-mapping ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Overview of OWMM-VLM. Our model is fine-tuned on InternVL-2.5[5], comprising a ViT, a 2-layer projection MLP, and a LLM. During training, ViT parameters ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Dataset Overview for Instruction Fine-tuning. Our dataset consists of four subsets, each correspond- ing to one of the four primary task actions: Pick, ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Single-step evaluation of VLM models on OWMM core multi-modal capabilities. The OWMM-VLM-38B model achieves the best performance across all metrics, demonstrating its superior ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3: Agent success rate in OWMM Task. OWMM-VLM-38B model consistently outperforms others across all metrics.
- **p. 9 / Figure/Table caption - extractive body cue:** Table 4: Real world single evaluation. OWMM-VLM-38B model achieved the best performance, and OWMM-VLM-8B model also outperformed the baseline. While the baseline model demonstrated relatively ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 5: Demonstration of single step evaluation in real world. These demos showcase OWMM-VLM-38B's outputs, illustrating that even though its training data are drawn entirely ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In each scene, objects were randomly placed for the robot to pick and relocate to another receptacle, resulting in 400 episodes per scene for ... | embodiment, simulator version and control stack | p. 7 (4 Dataset), p. 13 (C Implementation Details) |
| Task/environment | D Details of Datasets D.1 Extra Dataset Construction Details Our evaluation pipeline is constructed using the HomeRobot[37] framework, which serves as a software structure ... | reset, timeout, object/scene variation | p. 13 (C Implementation Details), p. 7 (4 Dataset) |
| Observation/sensor | egocentric RGB-D, language/task goal, base-arm proprioception | calibration, preprocessing, privileged input | p. 4 (3 Methodology), p. 5 (3 Methodology) |
| Output/decision | base motion plus arm/gripper action | action frame, controller and termination | p. 2 (1 Introduction), p. 3 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Model/ Task Score Ego-centric Decisionmaking↑ Image Retrieval↑ Affordance Grounding (object)↑ Affordance Grounding (receptacle)↑ Affordance Grounding (navigation)↑ Time Consumption(s)↓ OWMM-VLM-38B(ours) 97.85% 87.54% 0.97(±0.14) 0.94(± ... | definition/direction/unit from same section | p. 7 (5 Experiments) |
| Figure 5: OVMM-VLM-8B Sub-task Performance with the Increase of Training Data Size. The task scores consistently improve as the training data size increases. marginal ... | definition/direction/unit from same section | p. 15 (Figure/Table caption) |
| 3) Robot close to: The success rate of robot staying within 1.5m or 2.0m of the object or goal receptacle before picking or placing. | definition/direction/unit from same section | p. 8 (5 Experiments) |
| Additionally, we introduce three metrics to assess subgoals: 1) Image retrieval: Success rate in locating object and goal receptacles from multiple posed images. | definition/direction/unit from same section | p. 8 (5 Experiments) |
| Table 3: Agent success rate in OWMM Task. OWMM-VLM-38B model consistently outperforms others across all metrics. | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 6: Results with different data diversity data scales. The best performance across training sets with different scales is indicated with bold font. Besides, ... | definition/direction/unit from same section | p. 15 (Figure/Table caption) |
| While the baseline model demonstrated relatively strong affordance grounding capabilities for objects, its poor performance in action decisionmaking led to incorrect navigation. | definition/direction/unit from same section | p. 9 (5 Experiments) |
| OWMM-VLM-38B model achieved the best performance, and OWMM-VLM-8B model also outperformed the baseline. | definition/direction/unit from same section | p. 9 (5 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| OWMM-VLM-38B model achieved the best performance, and OWMM-VLM-8B model also outperformed the baseline. | comparison identity and matched condition | p. 9 (5 Experiments) |
| Model Ablation Ego-centric Decisionmaking↑ Image Retrieval↑ Affordance Grounding (object)↑ Affordance Grounding (receptacle)↑ Affordance Grounding (navigation)↑ OWMM-VLM-8B 96.72% 79.04% 0.93(±0.14) 0.91(±0.20) 0.83(±0.21) + beam search ... | comparison identity and matched condition | p. 17 (C Implementation Details) |
| OWMM-VLM-38B model consistently outperforms others across all metrics. | comparison identity and matched condition | p. 7 (5 Experiments) |
| Our model excels in decision-making, achieving state-of-the-art results in image retrieval and affordance grounding. | comparison identity and matched condition | p. 8 (5 Experiments) |
| This advantage directly translates into higher overall accuracy compared to methods that employ GPT-4o as the agent. | comparison identity and matched condition | p. 8 (5 Experiments) |
| While the baseline model demonstrated relatively strong affordance grounding capabilities for objects, its poor performance in action decisionmaking led to incorrect navigation. | comparison identity and matched condition | p. 9 (5 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Hence, its effect is briefly shown only in the ablation study. | component/input/data sensitivity | p. 17 (C Implementation Details) |
| For the ablation study on model design, such as the choice of generating bounding boxes rather than points, please see Appendix G. | component/input/data sensitivity | p. 7 (5 Experiments) |
| G Ablation Study on OWMM-VLM The ablation study evaluates the contributions of the components of the OWMM-VLM model. | component/input/data sensitivity | p. 17 (C Implementation Details) |
| Figure 1: OWMM-Agent Operates Fetch Robot for Tidying Task. OWMM-Agent receives natural language instructions and leverages both long-term environment memory (scene images) and transient ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| Regarding the model's architecture, we have trained two variants consisting of 8 billion and 38 billion parameters, based on the pre-trained model from InternVL-2.5[5]. | component/input/data sensitivity | p. 13 (C Implementation Details) |
| In other words, using the data from our data synthesis pipeline to conduct a supervised fine-tuning yields a significant enhancement in robotic decision-making performance. | component/input/data sensitivity | p. 8 (5 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are as follows: • We propose OWMM-Agent, a unified VLM-based agent architecture for open-world mobile manipulation, capable of global scene ... | Figure 5: OVMM-VLM-8B Sub-task Performance with the Increase of Training Data Size. The task scores consistently improve as the training data size increases. marginal ... | PDF body cue; verify exact table/figure and matched conditions | p. 15 (Figure/Table caption), p. 9 (5 Experiments), p. 7 (5 Experiments), p. 7 (Figure/Table caption), p. 8 (5 Experiments), p. 8 (5 Experiments) |
| Primary metric/result | OWMM-VLM-38B model achieved the best performance, and OWMM-VLM-8B model also outperformed the baseline. | numeric claim only at cited anchor | p. 9 (5 Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 4 Dataset - extractive body cue:** 4.2 Dataset Analysis We used 143 scenes from The Habitat Synthetic Scenes Dataset (HSSD)[13] and combined objects from YCB Objects[4] and Google Scanned Objects[6] to ...
- **p. 7 / 4 Dataset - extractive body cue:** In each scene, objects were randomly placed for the robot to pick and relocate to another receptacle, resulting in 400 episodes per scene for our ...
- **p. 13 / C Implementation Details - extractive body cue:** As for the training time, OWMM-VLM-8B is trained on 8X NVIDIA A100 GPUs for about 7 hours, and OWMM-VLM-38B is trained on 24X NVIDIA A100 ...
- **p. 13 / C Implementation Details - extractive body cue:** Both our models were trained for 1 epoch.
- **p. 13 / C Implementation Details - extractive body cue:** Specifically, we use the simulation part of HomeRobot project, built on Habitat platform[25], with 200 scenes, 150 categories, and 7892 object instances.
- **p. 14 / C Implementation Details - extractive body cue:** Besides, we allocated 157 objects between the training and validation sets with a ratio of 137:20, ensuring that the testing set contained entirely unseen objects.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Episodic evaluations in simulated environments further confirmed the OWMM-Agent's superior success rates and robustness against common failure modes like dead loops, while real-world tests ... | p. 9 (6 Conclusion) |
| body limitation/failure cue | Future work will focus on addressing limitations like pre-mapping reliance and enhancing cross-embodiment adaptability for more complex manipulation tasks. | p. 9 (6 Conclusion) |
| body limitation/failure cue | For safety reasons, we cannot allow the agent to fully operate the fetch robot in the real world. | p. 8 (5 Experiments) |
| body limitation/failure cue | This division resulted in a total of 152k training data entries and 4k testing data entries, establishing a robust dataset for training and testing ... | p. 14 (C Implementation Details) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| As for the training time, OWMM-VLM-8B is trained on 8X NVIDIA A100 GPUs for about 7 hours, and OWMM-VLM-38B is trained on 24X NVIDIA ... | p. 13 (C Implementation Details) |
| We then select 10 test samples from the sequence of the robot's head view during its run. | p. 8 (5 Experiments) |
| 3) Affordance Grounding: Instead of predicting points directly like in [39, 24], OWMM-VLM outputs a bounding box, from which we compute the center as ... | p. 8 (5 Experiments) |
| Within these steps, we sample the waypoint step data at specified intervals. | p. 14 (C Implementation Details) |
| In particular, at this stage, we did not collect the robot's head-view images to enhance the data collection efficiency.We recollected the robot's head-view images ... | p. 14 (C Implementation Details) |
| The robot state and observations updates can be expressed mathematically as: xt+1 = fk(xt, at, ∆t) Ic t+1, Dc t+1 = fobs(xt+1) where xt ... | p. 16 (C Implementation Details) |
| To establish appropriate thresholds, we first calculated the 3D bounding box diagonal distances of all goal receptacles in the test set, filtering out those ... | p. 16 (C Implementation Details) |
| The model's output represents a high-level action At spanning several simulation steps, while planners resolve trajectories and low-level actions at for each step. | p. 5 (3 Methodology) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 6 Conclusion - extractive body cue:** Episodic evaluations in simulated environments further confirmed the OWMM-Agent's superior success rates and robustness against common failure modes like dead loops, while real-world tests on ...
- **p. 9 / 6 Conclusion - extractive body cue:** Future work will focus on addressing limitations like pre-mapping reliance and enhancing cross-embodiment adaptability for more complex manipulation tasks.
- **p. 8 / 5 Experiments - extractive body cue:** For safety reasons, we cannot allow the agent to fully operate the fetch robot in the real world.
- **p. 14 / C Implementation Details - extractive body cue:** This division resulted in a total of 152k training data entries and 4k testing data entries, establishing a robust dataset for training and testing in ...

- **Evidence anchors reviewed:** datasets p. 7 (4 Dataset), p. 13 (C Implementation Details), p. 7 (4 Dataset), p. 8 (5 Experiments), p. 13 (C Implementation Details), p. 14 (C Implementation Details), metrics p. 7 (5 Experiments), p. 15 (Figure/Table caption), p. 8 (5 Experiments), p. 8 (5 Experiments), p. 7 (Figure/Table caption), p. 15 (Figure/Table caption), baselines p. 9 (5 Experiments), p. 17 (C Implementation Details), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 8 (5 Experiments), p. 9 (5 Experiments), results p. 15 (Figure/Table caption), p. 9 (5 Experiments), p. 7 (5 Experiments), p. 7 (Figure/Table caption), p. 8 (5 Experiments), p. 8 (5 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
