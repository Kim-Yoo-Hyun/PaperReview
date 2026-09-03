# Evaluation - SaPaVe: Towards Active Perception and Manipulation in Vision-Language Action Models for Robotics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_SaPaVe_Towards_Active_Perception_and_Manipulation_in_Vision-Language_Action_Models_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_SaPaVe_Towards_Active_Perception_and_Manipulation_in_Vision-Language_Action_Models_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 1 (Figure/Table caption), p. 7 (4.2. Semantic Active Perception Evaluation), p. 8 (4.4. Comparison with existing VLA models), p. 8 (4.6. Ablation Studies), p. 6 (Figure/Table caption)): Table 3. Performance on active manipulation in real-world set- tings. We report the success rate (%) compared to the existing VLA models. Our approach achieves the best performance.

## Evaluation Body Digest

- **p. 7 / 4.1. Experimental Setup - extractive body cue:** Pick-and-Place Pick-and-Place Arti-Manip Arti-Manip π0 [6] 55 45 45 35 45.00 GR00T-N1 [5] 60 55 50 50 53.75 Ours 90 85 85 80 85.00 robot ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** We design a series of experiments leveraging different components of our dataset and benchmarks: (1) For the first experiment to evaluate semantic active perception (Sec.
- **p. 8 / 4.4. Comparison with existing VLA models - extractive body cue:** Our model demonstrates robust generalization when performing active manipulation across unseen objects, varying lighting conditions, and diverse scenes.
- **p. 8 / 4.6. Ablation Studies - extractive body cue:** We conduct a series of ablation experiments on 4 real-world tasks to evaluate the effectiveness of different components in our method.
- **p. 7 / 4.1. Experimental Setup - extractive body cue:** Performance on active manipulation in real-world settings.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** 3.4), which comprises 6 task types: Unoccluded/Occluded/Out-of-View Pick-andPlace, as well as Unoccluded/Occluded/Out-of-View Articulated Manipulation.
- **p. 7 / 4.1. Experimental Setup - extractive body cue:** For all experiments, we report the success rate.
- **p. 7 / 4.3. Fixed and Dynamic Cameras Evaluation - extractive body cue:** 2, under a fixed viewpoint, the success rates of unoccluded, occluded, and out-of-view tasks all decrease substantially-especially for the Out-of-View task, which drops by more ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Experimental Setup (p. 6); 4.2. Semantic Active Perception Evaluation (p. 7); 4.3. Fixed and Dynamic Cameras Evaluation (p. 7); 4.5. Generalization Ability Evaluation (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 3. Performance on active manipulation in real-world set- tings. We report the success rate (%) compared to the existing VLA models. Our approach ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 1. We propose SaPaVe, an end-to-end active manipulation framework that jointly integrates semantic active perception and active- view execution; the former selectively shifting ... | p. 1 (Figure/Table caption) |
| 4.2. Semantic Active Perception Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 1, our model significantly outperforms powerful VLMs across all test splits, especially on test2, where semantic understanding is paramount. | p. 7 (4.2. Semantic Active Perception Evaluation) |
| 4.4. Comparison with existing VLA models | EMPIRICAL / REAL-ROBOT OR HARDWARE | 3, our bottom-up approach significantly outperforms direct VLA fine-tuning, demonstrating that first establishing robust semantic active perception priors and then learning active manipulation tasks ... | p. 8 (4.4. Comparison with existing VLA models) |
| 4.6. Ablation Studies | EMPIRICAL / REAL-ROBOT OR HARDWARE | 5 indicates that both training stages substantially improve the model's performance. | p. 8 (4.6. Ablation Studies) |

## Dataset / Benchmark Role

- **p. 7 / 4.1. Experimental Setup - extractive body cue:** Pick-and-Place Pick-and-Place Arti-Manip Arti-Manip π0 [6] 55 45 45 35 45.00 GR00T-N1 [5] 60 55 50 50 53.75 Ours 90 85 85 80 85.00 robot ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** We design a series of experiments leveraging different components of our dataset and benchmarks: (1) For the first experiment to evaluate semantic active perception (Sec.
- **p. 8 / 4.4. Comparison with existing VLA models - extractive body cue:** Our model demonstrates robust generalization when performing active manipulation across unseen objects, varying lighting conditions, and diverse scenes.
- **p. 8 / 4.6. Ablation Studies - extractive body cue:** We conduct a series of ablation experiments on 4 real-world tasks to evaluate the effectiveness of different components in our method.
- **p. 7 / 4.1. Experimental Setup - extractive body cue:** Performance on active manipulation in real-world settings.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** 3.4), which comprises 6 task types: Unoccluded/Occluded/Out-of-View Pick-andPlace, as well as Unoccluded/Occluded/Out-of-View Articulated Manipulation.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. We propose SaPaVe, an end-to-end active manipulation framework that jointly integrates semantic active perception and active- view execution; the former selectively shifting viewpoints ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Overview of SaPaVe. SaPaVe can process RGB images and task instructions and output camera movement and manipulation actions in a decoupled action space. ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Overview of ActiveViewPose-200K. It is a high-quality dataset comprising 200k image-language and camera movement pairs, enriched with highly detailed semantic annotations to enable ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. Overview of ActiveManip-Bench: It is the first simulation benchmark to evaluate active manipulation beyond traditional fixed- view settings. ActiveManip-Bench features 12 richly annotated ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. The performance of semantic active perception evalua- tion. We report the success rate (%) compared to current general VLMs and specialized spatial VLMs.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Evaluation results for fixed and dynamic cameras in simulation of ActiveManip-Bench. We report the success rate (%) compare to different camera configurations with ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Performance on active manipulation in real-world set- tings. We report the success rate (%) compared to the existing VLA models. Our approach achieves ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Performance on generalization ability evaluation. We report the success rate (%). Our model demonstrates robust gener- alization when performing active manipulation across unseen ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Pick-and-Place Pick-and-Place Arti-Manip Arti-Manip π0 [6] 55 45 45 35 45.00 GR00T-N1 [5] 60 55 50 50 53.75 Ours 90 85 85 80 85.00 ... | embodiment, simulator version and control stack | p. 7 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Task/environment | We design a series of experiments leveraging different components of our dataset and benchmarks: (1) For the first experiment to evaluate semantic active perception ... | reset, timeout, object/scene variation | p. 6 (4.1. Experimental Setup), p. 8 (4.4. Comparison with existing VLA models) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (3.1. Problem Formulation), p. 4 (Model) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 3 (3.1. Problem Formulation), p. 4 (3.2. Architecture) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For all experiments, we report the success rate. | definition/direction/unit from same section | p. 7 (4.1. Experimental Setup) |
| 2, under a fixed viewpoint, the success rates of unoccluded, occluded, and out-of-view tasks all decrease substantially-especially for the Out-of-View task, which drops by ... | definition/direction/unit from same section | p. 7 (4.3. Fixed and Dynamic Cameras Evaluation) |
| Meanwhile, omitting Stage 2 reduces the model's overall success rate, underscoring the necessity of active manipulation finetuning. | definition/direction/unit from same section | p. 8 (4.6. Ablation Studies) |
| In particular, for out-of-view tasks, omitting Stage 1 drastically reduces the success rate-by half in artifact manipulation-showing that first equipping the model with semantic ... | definition/direction/unit from same section | p. 8 (4.6. Ablation Studies) |
| Figure 1. We propose SaPaVe, an end-to-end active manipulation framework that jointly integrates semantic active perception and active- view execution; the former selectively shifting ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| 4.3), we assess performance on ActiveManip-Bench (see Sec. | definition/direction/unit from same section | p. 6 (4.1. Experimental Setup) |
| (5) What role do each of the system components play in enhancing its overall performance (Sec. | definition/direction/unit from same section | p. 6 (4. Experiments) |
| Figure 2. Overview of SaPaVe. SaPaVe can process RGB images and task instructions and output camera movement and manipulation actions in a decoupled action ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 1. We propose SaPaVe, an end-to-end active manipulation framework that jointly integrates semantic active perception and active- view execution; the former selectively shifting ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| We compare our method against several strong baselines: (1) In the first experiment, we compare our model with current powerful VLM, including the general ... | comparison identity and matched condition | p. 7 (4.1. Experimental Setup) |
| (3) Compared to existing VLA models, how does our model architecture enhance active manipulation capabilities (Sec. | comparison identity and matched condition | p. 6 (4. Experiments) |
| We report the success rate (%) compared to the existing VLA models. | comparison identity and matched condition | p. 7 (4.1. Experimental Setup) |
| 75 75 65 60 68.75 a unified single action decoder for simultaneously learning camera movement and other actions, compared to using a decoupled approach, ... | comparison identity and matched condition | p. 8 (4.6. Ablation Studies) |
| 3, our bottom-up approach significantly outperforms direct VLA fine-tuning, demonstrating that first establishing robust semantic active perception priors and then learning active manipulation tasks ... | comparison identity and matched condition | p. 8 (4.4. Comparison with existing VLA models) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We conduct a series of ablation experiments on 4 real-world tasks to evaluate the effectiveness of different components in our method. | component/input/data sensitivity | p. 8 (4.6. Ablation Studies) |
| Ablation Study on the effect about training strategy of Stage 1 and Stage2, decoupled action head (D.A.H.), camera adapter (C.A.), and universal spatial knowledge ... | component/input/data sensitivity | p. 8 (4.6. Ablation Studies) |
| (2) For the second experiment to evaluate the effect of fixed or dynamic cameras across different types (Sec. | component/input/data sensitivity | p. 6 (4.1. Experimental Setup) |
| (5) What role do each of the system components play in enhancing its overall performance (Sec. | component/input/data sensitivity | p. 6 (4. Experiments) |
| Both are fine-tuned for active manipulation tasks. | component/input/data sensitivity | p. 7 (4.4. Comparison with existing VLA models) |
| Directly fine-tuning existing VLA models is insufficient to fully address active manipulation tasks In Tab. | component/input/data sensitivity | p. 7 (4.4. Comparison with existing VLA models) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are threefold: • We propose SaPaVe, a novel end-to-end framework that first achieves active manipulation with a bottom-up learning strategy ... | Table 3. Performance on active manipulation in real-world set- tings. We report the success rate (%) compared to the existing VLA models. Our approach ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 1 (Figure/Table caption), p. 7 (4.2. Semantic Active Perception Evaluation), p. 8 (4.4. Comparison with existing VLA models), p. 8 (4.6. Ablation Studies), p. 6 (Figure/Table caption) |
| Primary metric/result | Figure 1. We propose SaPaVe, an end-to-end active manipulation framework that jointly integrates semantic active perception and active- view execution; the former selectively shifting ... | numeric claim only at cited anchor | p. 1 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** 3.4), which comprises 6 task types: Unoccluded/Occluded/Out-of-View Pick-andPlace, as well as Unoccluded/Occluded/Out-of-View Articulated Manipulation.
- **p. 7 / 4.1. Experimental Setup - extractive body cue:** Pick-and-Place Pick-and-Place Arti-Manip Arti-Manip π0 [6] 55 45 45 35 45.00 GR00T-N1 [5] 60 55 50 50 53.75 Ours 90 85 85 80 85.00 robot ...
- **p. 8 / 4.4. Comparison with existing VLA models - extractive body cue:** Task Name Object 1 Object 2 Light 1 Light 2 Scene 1 Scene 2 Original Occluded 85 90 90 95 90 85 90 Pick-and-Place Out-of-View ...
- **p. 6 / 3.4. ActiveViewPose-200K and ActiveManip-Bench - extractive body cue:** (b) This simulation includes a total of 12 tasks and we demonstrates some tasks and scenarios.
- **p. 6 / 3.4. ActiveViewPose-200K and ActiveManip-Bench - extractive body cue:** ActiveManip-Bench features 12 richly annotated tasks across 100 objects and 20 diverse scenes.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Two main factors account for this shortfall: (1) Direct VLA fine-tuning does not provide sufficient active perception priors. | p. 7 (4.4. Comparison with existing VLA models) |
| body limitation/failure cue | This result indicates that a fixed camera greatly limits the model's ability to explore the accessible space, leading to failures for active manipulation. | p. 7 (4.3. Fixed and Dynamic Cameras Evaluation) |
| body limitation/failure cue | Figure 1. We propose SaPaVe, an end-to-end active manipulation framework that jointly integrates semantic active perception and active- view execution; the former selectively shifting ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | 4, our model demonstrates strong generalization to previously unseen objects, indicating robust high-level semantic understanding that enables it to interpret out-of-distribution objects and correctly ... | p. 8 (4.5. Generalization Ability Evaluation) |
| body limitation/failure cue | (4) How well does our model generalize to out-of-distribution (OOD) scenarios (Sec. | p. 6 (4. Experiments) |
| body limitation/failure cue | Universal Spatial Knowledge Injection greatly enhances the model's robustness for basic operations under active views. | p. 8 (4.6. Ablation Studies) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We thus use this dataset to train Camera Adapter and Camera Action Decoder by supervising camera movement (see Fig. | p. 5 (3.3. Two-Stage Training Strategy) |
| 75 75 65 60 68.75 a unified single action decoder for simultaneously learning camera movement and other actions, compared to using a decoupled approach, ... | p. 8 (4.6. Ablation Studies) |
| Forcing the use of a unified action decoder couples the two training stages in the action space, not only disrupting the semantic active perception ... | p. 8 (4.6. Ablation Studies) |
| 2, we design two decoders to decouple camera movement from other actions. | p. 4 (Model) |
| 2, we adopt a Universal Spatial Encoder inherited from a powerful feedforward 3D geometry model [17]. | p. 4 (Model) |
| First, place it on the desk to the right of the computer; then, place it to the right side of the computer. | p. 6 (3.4. ActiveViewPose-200K and ActiveManip-Bench) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4.4. Comparison with existing VLA models - extractive body cue:** Two main factors account for this shortfall: (1) Direct VLA fine-tuning does not provide sufficient active perception priors.
- **p. 7 / 4.3. Fixed and Dynamic Cameras Evaluation - extractive body cue:** This result indicates that a fixed camera greatly limits the model's ability to explore the accessible space, leading to failures for active manipulation.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. We propose SaPaVe, an end-to-end active manipulation framework that jointly integrates semantic active perception and active- view execution; the former selectively shifting viewpoints ...
- **p. 8 / 4.5. Generalization Ability Evaluation - extractive body cue:** 4, our model demonstrates strong generalization to previously unseen objects, indicating robust high-level semantic understanding that enables it to interpret out-of-distribution objects and correctly follow ...
- **p. 6 / 4. Experiments - extractive body cue:** (4) How well does our model generalize to out-of-distribution (OOD) scenarios (Sec.
- **p. 8 / 4.6. Ablation Studies - extractive body cue:** Universal Spatial Knowledge Injection greatly enhances the model's robustness for basic operations under active views.

- **Evidence anchors reviewed:** datasets p. 7 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 8 (4.4. Comparison with existing VLA models), p. 8 (4.6. Ablation Studies), p. 7 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), metrics p. 7 (4.1. Experimental Setup), p. 7 (4.3. Fixed and Dynamic Cameras Evaluation), p. 8 (4.6. Ablation Studies), p. 8 (4.6. Ablation Studies), p. 1 (Figure/Table caption), p. 6 (4.1. Experimental Setup), baselines p. 1 (Figure/Table caption), p. 7 (4.1. Experimental Setup), p. 6 (4. Experiments), p. 7 (4.1. Experimental Setup), p. 8 (4.6. Ablation Studies), p. 8 (4.4. Comparison with existing VLA models), results p. 7 (Figure/Table caption), p. 1 (Figure/Table caption), p. 7 (4.2. Semantic Active Perception Evaluation), p. 8 (4.4. Comparison with existing VLA models), p. 8 (4.6. Ablation Studies), p. 6 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
