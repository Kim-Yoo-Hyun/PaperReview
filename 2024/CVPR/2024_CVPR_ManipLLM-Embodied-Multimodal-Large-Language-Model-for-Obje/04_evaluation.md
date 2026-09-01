# Evaluation - ManipLLM: Embodied Multimodal Large Language Model for Object-Centric Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Li_ManipLLM_Embodied_Multimodal_Large_Language_Model_for_Object-Centric_Robotic_Manipulation_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Li_ManipLLM_Embodied_Multimodal_Large_Language_Model_for_Object-Centric_Robotic_Manipulation_CVPR_2024_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.3. Ablation and Analysis), p. 6 (4.1. Training Details), p. 6 (4.1. Training Details), p. 7 (4.2. Quantitative Comparison), p. 8 (4.4. Real-world Evaluation), p. 8 (4.4. Real-world Evaluation)): It thus significantly improves the manipulation success rate by +7%.

## Evaluation Body Digest

- **p. 8 / 4.4. Real-world Evaluation - extractive PDF cue:** 5, the devised TTA strategy addresses discrepancies arising from real-world hardware configurations.
- **p. 6 / 4.1. Training Details - extractive PDF cue:** We adopt SAPIEN [31] and the PartNetMobility dataset to set up an interactive environment for our task, with VulkanRenderer of high-efficiency rasterizationbased renderer.
- **p. 8 / 4.4. Real-world Evaluation - extractive PDF cue:** We conduct experiments that involve interacting with various real-world household objects.
- **p. 6 / 4.1. Training Details - extractive PDF cue:** We use a Franka Panda Robot with flying suction gripper as the robot actuator.
- **p. 7 / 4.3. Ablation and Analysis - extractive PDF cue:** Object Category Identification(OCI.): Subsequently, in the second row of Table 2, we introduce the task of object category identiTrain Test AVG FT.
- **p. 7 / 4.3. Ablation and Analysis - extractive PDF cue:** Effectiveness of tasks in the training paradigm.
- **p. 6 / 4.1. Training Details - extractive PDF cue:** We adopt the manipulation success rate to reflect the outcome of the manipulation which is the ratio of the number of successfully manipulated samples divided ...
- **p. 7 / 4.2. Quantitative Comparison - extractive PDF cue:** The success rate of VoxPoser is 14.0% while ours is 69.0%.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Experiment Results (p. 6); 4.4. Real-world Evaluation (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Ablation and Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | It thus significantly improves the manipulation success rate by +7%. | p. 7 (4.3. Ablation and Analysis) |
| 4.1. Training Details | EMPIRICAL / REAL-ROBOT OR HARDWARE | If successful manipulation is achieved, we record it as a successful sample. | p. 6 (4.1. Training Details) |
| 4.1. Training Details | EMPIRICAL / REAL-ROBOT OR HARDWARE | We adopt the manipulation success rate to reflect the outcome of the manipulation which is the ratio of the number of successfully manipulated samples ... | p. 6 (4.1. Training Details) |
| 4.2. Quantitative Comparison | EMPIRICAL / REAL-ROBOT OR HARDWARE | The success rate of VoxPoser is 14.0% while ours is 69.0%. | p. 7 (4.2. Quantitative Comparison) |
| 4.4. Real-world Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results of real-world experiments are shown in Table 3. | p. 8 (4.4. Real-world Evaluation) |

## Dataset / Benchmark Role

- **p. 8 / 4.4. Real-world Evaluation - extractive PDF cue:** 5, the devised TTA strategy addresses discrepancies arising from real-world hardware configurations.
- **p. 6 / 4.1. Training Details - extractive PDF cue:** We adopt SAPIEN [31] and the PartNetMobility dataset to set up an interactive environment for our task, with VulkanRenderer of high-efficiency rasterizationbased renderer.
- **p. 8 / 4.4. Real-world Evaluation - extractive PDF cue:** We conduct experiments that involve interacting with various real-world household objects.
- **p. 6 / 4.1. Training Details - extractive PDF cue:** We use a Franka Panda Robot with flying suction gripper as the robot actuator.
- **p. 7 / 4.3. Ablation and Analysis - extractive PDF cue:** Object Category Identification(OCI.): Subsequently, in the second row of Table 2, we introduce the task of object category identiTrain Test AVG FT.
- **p. 7 / 4.3. Ablation and Analysis - extractive PDF cue:** Effectiveness of tasks in the training paradigm.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. The prediction of ManipLLM. Given the text prompt, RGB image, and depth map inputs, we obtain 3D contact point (x, y, z). Here, ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Training details of ManipLLM. This paradigm contains four training tasks, enabling the model to recognize the current object (category-level), understand which regions can ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Affordance map for movable parts on objects. It indi- cates the probability of actionability on the pixel level. visualize affordance maps in Fig. ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. The chain-of-thought inference process of ManipLLM. trast with leveraging a model to predict each following pose, such a heuristic policy is much more ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. Comparisons of our method against baseline methods. used to determine end-effector pose. Our current experimental settings involve training on a wider range of ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Ablation analysis of each training task in the training paradigm and strategies in inference. fication, the first prompt in Fig. 2. It enables ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5. Visualizations of TTA process in real-world scenarios. The center of pink dot represents the predicted contact position. aims to enable the model to ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 5, the devised TTA strategy addresses discrepancies arising from real-world hardware configurations. | embodiment, simulator version and control stack | p. 8 (4.4. Real-world Evaluation), p. 6 (4.1. Training Details) |
| Task/environment | We adopt SAPIEN [31] and the PartNetMobility dataset to set up an interactive environment for our task, with VulkanRenderer of high-efficiency rasterizationbased renderer. | reset, timeout, object/scene variation | p. 6 (4.1. Training Details), p. 8 (4.4. Real-world Evaluation) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 5 (3.2. Active Impedance Adaptation Policy), p. 5 (3.2. Active Impedance Adaptation Policy) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 1 (1. Introduction), p. 4 (3.1. Fine-tuning Strategy) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We adopt the manipulation success rate to reflect the outcome of the manipulation which is the ratio of the number of successfully manipulated samples ... | definition/direction/unit from same section | p. 6 (4.1. Training Details) |
| The success rate of VoxPoser is 14.0% while ours is 69.0%. | definition/direction/unit from same section | p. 7 (4.2. Quantitative Comparison) |
| It thus significantly improves the manipulation success rate by +7%. | definition/direction/unit from same section | p. 7 (4.3. Ablation and Analysis) |
| It further predicts 100 end-effector orientations and selects the orientation with the highest score to formulate the contact pose. | definition/direction/unit from same section | p. 6 (4.2. Quantitative Comparison) |
| Figure 1. The prediction of ManipLLM. Given the text prompt, RGB image, and depth map inputs, we obtain 3D contact point (x, y, z). ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Object Category Success/Total 4/5 5/5 4/5 3/5 4/5 4/5 4/5 Distance(m) 0.17 0.28 0.10 0.08 0.14 0.15 0.18 Table 3. | definition/direction/unit from same section | p. 8 (4.4. Real-world Evaluation) |
| In the last row of Table 2 w/o AIA., we employ a straightforward control policy, which operates by moving directly to the desired position ... | definition/direction/unit from same section | p. 8 (4.3. Ablation and Analysis) |
| Figure 2. Training details of ManipLLM. This paradigm contains four training tasks, enabling the model to recognize the current object (category-level), understand which regions ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 1. Comparisons of our method against baseline methods. used to determine end-effector pose. Our current experimental settings involve training on a wider range ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Figure 5. Visualizations of TTA process in real-world scenarios. The center of pink dot represents the predicted contact position. aims to enable the model ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| We compare ManipLLM against four representative baselines, including Where2Act [23], UMPNet [33], Flowbot3D [6], and Implicit3D [39]. | comparison identity and matched condition | p. 6 (4.2. Quantitative Comparison) |
| For fair comparison, we alter the used parallel gripper to suction gripper. | comparison identity and matched condition | p. 6 (4.2. Quantitative Comparison) |
| Ablation analysis of each training task in the training paradigm and strategies in inference. fication, the first prompt in Fig. | comparison identity and matched condition | p. 7 (4.3. Ablation and Analysis) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To elucidate the contribution and effectiveness of individual modules within our approach, we conduct extensive ablation studies. | component/input/data sensitivity | p. 7 (4.3. Ablation and Analysis) |
| In the last row of Table 2 w/o AIA., we employ a straightforward control policy, which operates by moving directly to the desired position ... | component/input/data sensitivity | p. 8 (4.3. Ablation and Analysis) |
| Ablation analysis of each training task in the training paradigm and strategies in inference. fication, the first prompt in Fig. | component/input/data sensitivity | p. 7 (4.3. Ablation and Analysis) |
| For comparison, we ask the model to generate the final pose prediction directly without the thinking process in Fig. | component/input/data sensitivity | p. 8 (4.3. Ablation and Analysis) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Meanwhile, in real-world experiments, our method shows strong generalization ability, with or without TTA strategy. | It thus significantly improves the manipulation success rate by +7%. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.3. Ablation and Analysis), p. 6 (4.1. Training Details), p. 6 (4.1. Training Details), p. 7 (4.2. Quantitative Comparison), p. 8 (4.4. Real-world Evaluation), p. 8 (4.4. Real-world Evaluation) |
| Primary metric/result | If successful manipulation is achieved, we record it as a successful sample. | numeric claim only at cited anchor | p. 6 (4.1. Training Details) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Training Details - extractive PDF cue:** We finetuned LLaMA-Adapter [38] on a 40G A100 GPU for 10 epochs, with an epoch costs around an hour.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Additionally, its head is relatively short, which presents a collision risk when interacting with the protruding handle. | p. 8 (4.4. Real-world Evaluation) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We finetuned LLaMA-Adapter [38] on a 40G A100 GPU for 10 epochs, with an epoch costs around an hour. | p. 6 (4.1. Training Details) |
| It includes pre-trained CLIP [25] as the visual encoder, 7B LLaMA [26] model as the decoder, and multi-modal projection module of 32 transformer layers. | p. 6 (4.1. Training Details) |
| 5, the devised TTA strategy addresses discrepancies arising from real-world hardware configurations. | p. 8 (4.4. Real-world Evaluation) |
| In our specific hardware configuration, the suction gripper is unable to grasp the handle due to the nonsmooth surface. | p. 8 (4.4. Real-world Evaluation) |
| Given an RGB image I ∈RH×W ×3, we adopt the visual encoder of CLIP [25] to extract its visual feature. | p. 3 (3.1. Fine-tuning Strategy) |
| While text prompts T are encoded into a text feature using the tokenizer of the pre-trained LLaMa [26]. | p. 3 (3.1. Fine-tuning Strategy) |
| Since we only have a language decoder (LLaMa) instead of a visual decoder, the model is not able to generate an affordance map directly. | p. 4 (3.1. Fine-tuning Strategy) |
| 4, the reasoning process follows the three steps that are consistent with the training tasks. | p. 5 (3.1. Fine-tuning Strategy) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 4.4. Real-world Evaluation - extractive PDF cue:** Additionally, its head is relatively short, which presents a collision risk when interacting with the protruding handle.

- **PDF anchors reviewed:** datasets p. 8 (4.4. Real-world Evaluation), p. 6 (4.1. Training Details), p. 8 (4.4. Real-world Evaluation), p. 6 (4.1. Training Details), p. 7 (4.3. Ablation and Analysis), p. 7 (4.3. Ablation and Analysis), metrics p. 6 (4.1. Training Details), p. 7 (4.2. Quantitative Comparison), p. 7 (4.3. Ablation and Analysis), p. 6 (4.2. Quantitative Comparison), p. 1 (Figure/Table caption), p. 8 (4.4. Real-world Evaluation), baselines p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (4.2. Quantitative Comparison), p. 6 (4.2. Quantitative Comparison), p. 7 (4.3. Ablation and Analysis), results p. 7 (4.3. Ablation and Analysis), p. 6 (4.1. Training Details), p. 6 (4.1. Training Details), p. 7 (4.2. Quantitative Comparison), p. 8 (4.4. Real-world Evaluation), p. 8 (4.4. Real-world Evaluation).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
