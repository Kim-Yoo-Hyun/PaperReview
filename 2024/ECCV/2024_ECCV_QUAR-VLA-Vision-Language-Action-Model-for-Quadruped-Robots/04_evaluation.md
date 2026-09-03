# Evaluation - QUAR-VLA: Vision-Language-Action Model for Quadruped Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/808_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00808.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 11 (4 Experiments), p. 12 (1. Comparison within VLM baselines. The experiment results reveal), p. 10 (4 Experiments), p. 11 (1. Comparison within VLM baselines. The experiment results reveal), p. 12 (1. Comparison within VLM baselines. The experiment results reveal), p. 13 (1. Comparison within VLM baselines. The experiment results reveal)): QUART has achieved success rates far exceeding those of the baselines in tasks of all difficulty levels, especially in the most challenging crawl and unload tasks, where the baselines have ...

## Evaluation Body Digest

- **p. 14 / 1. Comparison within VLM baselines. The experiment results reveal - extractive body cue:** To tackle these two questions, we present the QUART models tailored for quadruped robots and the QUARD dataset, which includes diverse tasks such as navigation ...
- **p. 14 / 1. Comparison within VLM baselines. The experiment results reveal - extractive body cue:** The left part shows 4 instances of seen tasks in both simulation environment and real-world.
- **p. 10 / 4 Experiments - extractive body cue:** Both models are trained with the next token prediction objective, which corresponds to the behavior cloning loss in robot learning.
- **p. 10 / 4 Experiments - extractive body cue:** It's important to note that this evaluation introduces variations in the placement of objects and other setup factors (such as robot position).
- **p. 12 / 1. Comparison within VLM baselines. The experiment results reveal - extractive body cue:** For the unfamiliar objects, we cast our gaze upon an array of circumstances: objects belonging to an identical category but exhibiting divergent textures and colors; ...
- **p. 13 / 1. Comparison within VLM baselines. The experiment results reveal - extractive body cue:** The ability to utilize language for precise control of quadruped robots facilitated by scene perception, as showcased in Fig.
- **p. 13 / 1. Comparison within VLM baselines. The experiment results reveal - extractive body cue:** It was further noted that even in the absence of explicit directional information within the dataset, the model reliably interpreted linguistic directives which, in turn, ...
- **p. 11 / 4 Experiments - extractive body cue:** Seen Unseen Easy Medium Hard Distinguish Go to Go avoid Go through Crawl Unload Object Verbal CLIP [27] 0.44 0.43 0.45 0.19 0 0 0.11 ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** legged robot, terrain과 contact dynamics.
- **Input boundary:** proprioception, terrain/perception observation과 velocity command.
- **Output/decision under evaluation:** joint target, torque, footstep 또는 locomotion action.
- **Primary target:** velocity/progress, stability, energy와 terrain generalization.
- **Detected evaluation headings:** 4 Experiments (p. 9); 1. Comparison within VLM baselines. The experiment results reveal (p. 11).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | QUART has achieved success rates far exceeding those of the baselines in tasks of all difficulty levels, especially in the most challenging crawl and ... | p. 11 (4 Experiments) |
| 1. Comparison within VLM baselines. The experiment results reveal | EMPIRICAL / REAL-ROBOT OR HARDWARE | Consequently, while the performance gains may be marginal in simple tasks, there is a noticeable enhancement in tasks that involve complex mechanical movements. significantly ... | p. 12 (1. Comparison within VLM baselines. The experiment results reveal) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | We follow the standard robot evaluation metrics [7, 9], success rate (SR), to evaluate the overall performance. | p. 10 (4 Experiments) |
| 1. Comparison within VLM baselines. The experiment results reveal | EMPIRICAL / REAL-ROBOT OR HARDWARE | As is shown in Table 2, Our model has achieved optimal performance on nearly all the baseline models. | p. 11 (1. Comparison within VLM baselines. The experiment results reveal) |
| 1. Comparison within VLM baselines. The experiment results reveal | EMPIRICAL / REAL-ROBOT OR HARDWARE | Conversely, QUART, leveraging the language prowess inherited from large language models, adeptly achieves generalization under novel instructions, thereby effectuating the harmonization of vision, language, ... | p. 12 (1. Comparison within VLM baselines. The experiment results reveal) |

## Dataset / Benchmark Role

- **p. 14 / 1. Comparison within VLM baselines. The experiment results reveal - extractive body cue:** To tackle these two questions, we present the QUART models tailored for quadruped robots and the QUARD dataset, which includes diverse tasks such as navigation ...
- **p. 14 / 1. Comparison within VLM baselines. The experiment results reveal - extractive body cue:** The left part shows 4 instances of seen tasks in both simulation environment and real-world.
- **p. 10 / 4 Experiments - extractive body cue:** Both models are trained with the next token prediction objective, which corresponds to the behavior cloning loss in robot learning.
- **p. 10 / 4 Experiments - extractive body cue:** It's important to note that this evaluation introduces variations in the placement of objects and other setup factors (such as robot position).
- **p. 12 / 1. Comparison within VLM baselines. The experiment results reveal - extractive body cue:** For the unfamiliar objects, we cast our gaze upon an array of circumstances: objects belonging to an identical category but exhibiting divergent textures and colors; ...
- **p. 13 / 1. Comparison within VLM baselines. The experiment results reveal - extractive body cue:** The ability to utilize language for precise control of quadruped robots facilitated by scene perception, as showcased in Fig.
- **p. 13 / 1. Comparison within VLM baselines. The experiment results reveal - extractive body cue:** It was further noted that even in the absence of explicit directional information within the dataset, the model reliably interpreted linguistic directives which, in turn, ...
- **p. 11 / 4 Experiments - extractive body cue:** Seen Unseen Easy Medium Hard Distinguish Go to Go avoid Go through Crawl Unload Object Verbal CLIP [27] 0.44 0.43 0.45 0.19 0 0 0.11 ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: Comparison of QUAR-VA, QUAR-LA, and QUAR-VLA. QUAR-VA solely utilizes coarse-grained vision information, lacking explicit instructions for han- dling diverse tasks. In contrast, QUAR-LA ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: Overview of QUAR-VLA. Our tasks encompass a diverse range of percep- tion, navigation, and other advanced capability. The Vision-Language-Action (VLA) model first undergoes ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Tasks Definition. The "Type" means different capabilities of robots. The "Level" devides the difficulty into 3 levels. The "Skill" means different skill/task cat- ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 3: The left figure illustrates the trajectory lengths corresponding to different tasks and the right figure illustrates the relationships between tasks. As the difficulty ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 4: Statistic analysis of QUARD. 1) Simulation data accounts for a larger pro- portion compared to real data. 2) Trotting occupied most of the ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 5: Architecture of QUART. It is designed to leverage the scene comprehension capability of a pretrained MLLM. It receives visual information as observation, and ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 6: Tasks Successful Rate. R3M lacks alignment with text, which means that al- though it has some recognition capabilities, it struggles to understand actions ...
- **p. 11 / Figure/Table caption - extractive body cue:** Table 2: Overall performance. QUART has achieved success rates far exceeding those of the baselines in tasks of all difficulty levels, especially in the most ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To tackle these two questions, we present the QUART models tailored for quadruped robots and the QUARD dataset, which includes diverse tasks such as ... | embodiment, simulator version and control stack | p. 14 (1. Comparison within VLM baselines. The experiment results reveal), p. 14 (1. Comparison within VLM baselines. The experiment results reveal) |
| Task/environment | The left part shows 4 instances of seen tasks in both simulation environment and real-world. | reset, timeout, object/scene variation | p. 14 (1. Comparison within VLM baselines. The experiment results reveal), p. 10 (4 Experiments) |
| Observation/sensor | proprioception, terrain/perception observation과 velocity command | calibration, preprocessing, privileged input | p. 8 (3 Method), p. 9 (3 Method) |
| Output/decision | joint target, torque, footstep 또는 locomotion action | action frame, controller and termination | p. 9 (3 Method), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We follow the standard robot evaluation metrics [7, 9], success rate (SR), to evaluate the overall performance. | definition/direction/unit from same section | p. 10 (4 Experiments) |
| QUART has achieved success rates far exceeding those of the baselines in tasks of all difficulty levels, especially in the most challenging crawl and ... | definition/direction/unit from same section | p. 11 (4 Experiments) |
| It was further noted that even in the absence of explicit directional information within the dataset, the model reliably interpreted linguistic directives which, in ... | definition/direction/unit from same section | p. 13 (1. Comparison within VLM baselines. The experiment results reveal) |
| In contrast, CLIP and VC-1 demonstrate satisfactory performance on fundamental perceptual tasks, such as navigation (e.g., "go to" commands). | definition/direction/unit from same section | p. 11 (1. Comparison within VLM baselines. The experiment results reveal) |
| This figure demonstrates the excellent performance of QUART for seen tasks in both simulated and real-world environments. | definition/direction/unit from same section | p. 14 (1. Comparison within VLM baselines. The experiment results reveal) |
| We concentrate our experiments on the multi-task ability and generalization. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| 4.2 Overall Performance Multi-task Performance. | definition/direction/unit from same section | p. 10 (4 Experiments) |
| To examine the adaptability in unanticipated scenarios, we orchestrated two primary examinations: one concentrated on unfamiliar objects, and the other on unprecedented linguistic directives. | definition/direction/unit from same section | p. 12 (1. Comparison within VLM baselines. The experiment results reveal) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Ding et al. action architecture for multi-task quadruped task compared to previous VLM baselines? | comparison identity and matched condition | p. 10 (4 Experiments) |
| Considering the absence of VLA models work on quadruped robots at present, we have taken the following baselines into account for a fair comparison: ... | comparison identity and matched condition | p. 10 (4 Experiments) |
| As is shown in Table 2, Our model has achieved optimal performance on nearly all the baseline models. | comparison identity and matched condition | p. 11 (1. Comparison within VLM baselines. The experiment results reveal) |
| QUART has achieved success rates far exceeding those of the baselines in tasks of all difficulty levels, especially in the most challenging crawl and ... | comparison identity and matched condition | p. 11 (4 Experiments) |
| When confronted with unseen instructions, the alighment between the existing language and the integration of vision and action cues within the baselines is compromised, ... | comparison identity and matched condition | p. 12 (1. Comparison within VLM baselines. The experiment results reveal) |
| 7 is that QUART surpasses other baseline methods, an innate advantage of large-scale multimodal models. | comparison identity and matched condition | p. 13 (1. Comparison within VLM baselines. The experiment results reveal) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In total, over 1500 episodes are tested in this evaluation, comprising 425 episodes for going to objects, 500 for going to objects without colliding ... | component/input/data sensitivity | p. 10 (4 Experiments) |
| And we use learning rate 2e-5 and batch size 256 to fine-tune the model for 100K gradient steps. | component/input/data sensitivity | p. 10 (4 Experiments) |
| Fig. 5: Architecture of QUART. It is designed to leverage the scene comprehension capability of a pretrained MLLM. It receives visual information as observation, ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our extensive evaluation shows that our approach leads to performant robotic policies and enables QUART to obtain a range of generalization capabilities. | QUART has achieved success rates far exceeding those of the baselines in tasks of all difficulty levels, especially in the most challenging crawl and ... | PDF body cue; verify exact table/figure and matched conditions | p. 11 (4 Experiments), p. 12 (1. Comparison within VLM baselines. The experiment results reveal), p. 10 (4 Experiments), p. 11 (1. Comparison within VLM baselines. The experiment results reveal), p. 12 (1. Comparison within VLM baselines. The experiment results reveal), p. 13 (1. Comparison within VLM baselines. The experiment results reveal) |
| Primary metric/result | Consequently, while the performance gains may be marginal in simple tasks, there is a noticeable enhancement in tasks that involve complex mechanical movements. significantly ... | numeric claim only at cited anchor | p. 12 (1. Comparison within VLM baselines. The experiment results reveal) |

- Numeric sentences retained from the body:
- **p. 10 / 4 Experiments - extractive body cue:** In total, over 1500 episodes are tested in this evaluation, comprising 425 episodes for going to objects, 500 for going to objects without colliding with ...
- **p. 7 / 3 Method - extractive body cue:** In obstacle scenarios, obstacles are placed 1.5 meters from the target's x-coordinate, with the same y-coordinate.
- **p. 9 / 3 Method - extractive body cue:** Observation I Instruction W VLA De-Tokenize Deploy ··· Action ad Velocity Gait B-Pose Terminate vx vy wz θ1 θ2 θ3 f hz sy hz f ...
- **p. 9 / 3 Method - extractive body cue:** QUART can generate a complete action sequence at a processing rate of 2Hz in actual scenarios, and hand it over to the underlying low-level strategy ...
- **p. 9 / 3 Method - extractive body cue:** For QUART, the inference time could get 2Hz.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | This failure manifests in behaviors such as repetitive motion, misdirection, wrong terminate commands. | p. 12 (1. Comparison within VLM baselines. The experiment results reveal) |
| body limitation/failure cue | When confronted with unseen instructions, the alighment between the existing language and the integration of vision and action cues within the baselines is compromised, ... | p. 12 (1. Comparison within VLM baselines. The experiment results reveal) |
| body limitation/failure cue | This observation suggests that while visual language models (VLMs) can grasp abstract principles of the world, directly applying VLMs does not readily translate to ... | p. 11 (1. Comparison within VLM baselines. The experiment results reveal) |
| body limitation/failure cue | 5 Conclusion & Future Work This paper emphasizes the significance of deploying Vision-Language-Action models on quadruped robots. | p. 14 (1. Comparison within VLM baselines. The experiment results reveal) |
| body limitation/failure cue | Future works will explore hardware acceleration techniques and model compression techniques to enable faster and more efficient execution of the models. | p. 14 (1. Comparison within VLM baselines. The experiment results reveal) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| And we use learning rate 2e-5 and batch size 256 to fine-tune the model for 100K gradient steps. | p. 10 (4 Experiments) |
| 4.1 Implementation Details Training Details. | p. 10 (4 Experiments) |
| In our study, we have achieved a decoder-only VLA framework. | p. 11 (1. Comparison within VLM baselines. The experiment results reveal) |
| Future works will explore hardware acceleration techniques and model compression techniques to enable faster and more efficient execution of the models. | p. 14 (1. Comparison within VLM baselines. The experiment results reveal) |
| For QUART, the inference time could get 2Hz. | p. 9 (3 Method) |
| The complexity of tasks is reflected in the average trajectory length, with more challenging tasks requiring a greater number of steps and consequently taking ... | p. 6 (3 Method) |
| Notably, QUART model takes a single image s and a natural language instruction w as input, which are first converted into corresponding tokens t ... | p. 8 (3 Method) |
| In contrast to many applications of large models, such as natural language or image generation, one of the unique requirements for a model that ... | p. 9 (3 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 12 / 1. Comparison within VLM baselines. The experiment results reveal - extractive body cue:** This failure manifests in behaviors such as repetitive motion, misdirection, wrong terminate commands.
- **p. 12 / 1. Comparison within VLM baselines. The experiment results reveal - extractive body cue:** When confronted with unseen instructions, the alighment between the existing language and the integration of vision and action cues within the baselines is compromised, resulting ...
- **p. 11 / 1. Comparison within VLM baselines. The experiment results reveal - extractive body cue:** This observation suggests that while visual language models (VLMs) can grasp abstract principles of the world, directly applying VLMs does not readily translate to the ...
- **p. 14 / 1. Comparison within VLM baselines. The experiment results reveal - extractive body cue:** 5 Conclusion & Future Work This paper emphasizes the significance of deploying Vision-Language-Action models on quadruped robots.
- **p. 14 / 1. Comparison within VLM baselines. The experiment results reveal - extractive body cue:** Future works will explore hardware acceleration techniques and model compression techniques to enable faster and more efficient execution of the models.

- **Evidence anchors reviewed:** datasets p. 14 (1. Comparison within VLM baselines. The experiment results reveal), p. 14 (1. Comparison within VLM baselines. The experiment results reveal), p. 10 (4 Experiments), p. 10 (4 Experiments), p. 12 (1. Comparison within VLM baselines. The experiment results reveal), p. 13 (1. Comparison within VLM baselines. The experiment results reveal), metrics p. 10 (4 Experiments), p. 11 (4 Experiments), p. 13 (1. Comparison within VLM baselines. The experiment results reveal), p. 11 (1. Comparison within VLM baselines. The experiment results reveal), p. 14 (1. Comparison within VLM baselines. The experiment results reveal), p. 9 (4 Experiments), baselines p. 10 (4 Experiments), p. 10 (4 Experiments), p. 11 (1. Comparison within VLM baselines. The experiment results reveal), p. 11 (4 Experiments), p. 12 (1. Comparison within VLM baselines. The experiment results reveal), p. 13 (1. Comparison within VLM baselines. The experiment results reveal), results p. 11 (4 Experiments), p. 12 (1. Comparison within VLM baselines. The experiment results reveal), p. 10 (4 Experiments), p. 11 (1. Comparison within VLM baselines. The experiment results reveal), p. 12 (1. Comparison within VLM baselines. The experiment results reveal), p. 13 (1. Comparison within VLM baselines. The experiment results reveal).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
