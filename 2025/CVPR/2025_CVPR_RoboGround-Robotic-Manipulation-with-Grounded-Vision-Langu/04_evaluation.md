# Evaluation - RoboGround: Robotic Manipulation with Grounded Vision-Language Priors

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Huang_RoboGround_Robotic_Manipulation_with_Grounded_Vision-Language_Priors_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Huang_RoboGround_Robotic_Manipulation_with_Grounded_Vision-Language_Priors_CVPR_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5.3. Zero-shot Evaluation), p. 8 (5.4. Ablation Study), p. 7 (5.2. Main Results), p. 8 (5.4. Ablation Study), p. 6 (5.2. Main Results), p. 6 (5.2. Main Results)): Notably, in more challenging scenarios, mask guidance achieves approximately 100% relative improvement over non-mask baselines, highlighting its crucial role in handling complex, unseen situations.

## Evaluation Body Digest

- **p. 8 / 5.4. Ablation Study - extractive PDF cue:** Specifically, we create an instruction-following dataset based on simulated data using the following prompt format: "Given a robotic manipulation instruction: <Instruction>, identify the target object ...
- **p. 7 / 5.2. Main Results - extractive PDF cue:** The original GR-1 model was pre-trained on a large video dataset and predicts both robot actions and future images.
- **p. 6 / 5.1. Simulation Setting - extractive PDF cue:** In these tasks, target masks (e.g., for a drawer handle) are also generated to guide the robot's policy in precise manipulation.
- **p. 6 / 5.2. Main Results - extractive PDF cue:** Each method is trained on the same dataset, which includes RoboCasa's 66K demonstrations for foundational skills, alongside our proposed dataset containing 24K demonstrations and 112K ...
- **p. 7 / 5.2. Main Results - extractive PDF cue:** We attribute this to the diverse range of objects in the dataset, which makes learning accurate grasping poses more difficult.
- **p. 8 / 5.4. Ablation Study - extractive PDF cue:** Fine-tuning on simulation data alone significantly improves results but risks losing the knowledge embedded in the original VLM dataset.
- **p. 6 / 5.2. Main Results - extractive PDF cue:** Metrics for pick-and-place tasks are reported as "a / b", where a is the contact rate (%) and b is the success rate (%).
- **p. 6 / 5.2. Main Results - extractive PDF cue:** The contact rate refers to the percentage of attempts where the gripper makes contact with the target object, while the success rate indicates the percentage ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 5. Experiments (p. 6); 5.2. Main Results (p. 6); 5.3. Zero-shot Evaluation (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5.3. Zero-shot Evaluation | EMPIRICAL / SIMULATION | Notably, in more challenging scenarios, mask guidance achieves approximately 100% relative improvement over non-mask baselines, highlighting its crucial role in handling complex, unseen situations. | p. 7 (5.3. Zero-shot Evaluation) |
| 5.4. Ablation Study | EMPIRICAL / SIMULATION | Fine-tuning on simulation data alone significantly improves results but risks losing the knowledge embedded in the original VLM dataset. | p. 8 (5.4. Ablation Study) |
| 5.2. Main Results | EMPIRICAL / SIMULATION | Interestingly, we observe a consistent gap between the success rate and the contact rate, with the latter being significantly higher. | p. 7 (5.2. Main Results) |
| 5.4. Ablation Study | EMPIRICAL / SIMULATION | While simple mask concatenation allows the model to utilize mask information, the grounded perceiver enables a more comprehensive exploitation of mask features, resulting in ... | p. 8 (5.4. Ablation Study) |
| 5.2. Main Results | EMPIRICAL / SIMULATION | Metrics for pick-and-place tasks are reported as "a / b", where a is the contact rate (%) and b is the success rate (%). | p. 6 (5.2. Main Results) |

## Dataset / Benchmark Role

- **p. 8 / 5.4. Ablation Study - extractive PDF cue:** Specifically, we create an instruction-following dataset based on simulated data using the following prompt format: "Given a robotic manipulation instruction: <Instruction>, identify the target object ...
- **p. 7 / 5.2. Main Results - extractive PDF cue:** The original GR-1 model was pre-trained on a large video dataset and predicts both robot actions and future images.
- **p. 6 / 5.1. Simulation Setting - extractive PDF cue:** In these tasks, target masks (e.g., for a drawer handle) are also generated to guide the robot's policy in precise manipulation.
- **p. 6 / 5.2. Main Results - extractive PDF cue:** Each method is trained on the same dataset, which includes RoboCasa's 66K demonstrations for foundational skills, alongside our proposed dataset containing 24K demonstrations and 112K ...
- **p. 7 / 5.2. Main Results - extractive PDF cue:** We attribute this to the diverse range of objects in the dataset, which makes learning accurate grasping poses more difficult.
- **p. 8 / 5.4. Ablation Study - extractive PDF cue:** Fine-tuning on simulation data alone significantly improves results but risks losing the knowledge embedded in the original VLM dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Examples of generated data and mask guidance for robot policy. The generated data includes more object distractors in the scene, leading to higher ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Data Generation Pipeline. The pipeline is composed of three key stages: (a) First, we extract informative object attributes in both keyword and descriptive ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Overall Architecture of ROBOGROUND. To enhance policy generalization, we leverage grounding masks as intermediate representations for spatial guidance. Specifically, (a) The grounded vision-language ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. Performance Comparison on Simulated Tasks. Metrics for pick-and-place tasks are reported as "a / b", where a is the contact rate (%) and ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Evaluation Results of Unseen Settings. Unseen instance denotes evaluation on new objects belonging to classes present in the training data. In contrast, unseen ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3. Ablation Study on Training Data and Grounded Masks. "Ori. Data" refers to original data in RoboCasa, while "New Data" denotes our proposed data ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4. Ablation Study on Modules for Incorporating Grounding Masks. "Channel Concat." denotes whether to do the channel concatenation for the image and mask. "Grounded ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 5. Ablation Study on Grounding Representations. "Point" and "Bbox" denote the center pixel point and the 2D bounding box extracted from predicted masks, respectively. ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Specifically, we create an instruction-following dataset based on simulated data using the following prompt format: "Given a robotic manipulation instruction: <Instruction>, identify the target ... | embodiment, simulator version and control stack | p. 8 (5.4. Ablation Study), p. 7 (5.2. Main Results) |
| Task/environment | The original GR-1 model was pre-trained on a large video dataset and predicts both robot actions and future images. | reset, timeout, object/scene variation | p. 7 (5.2. Main Results), p. 6 (5.1. Simulation Setting) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 5 (4.3. Grounded Policy Network), p. 5 (4.2. Grounded Vision-Language Model) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 6 (4.4. Training and Inference), p. 4 (4.1. Overview) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Metrics for pick-and-place tasks are reported as "a / b", where a is the contact rate (%) and b is the success rate (%). | definition/direction/unit from same section | p. 6 (5.2. Main Results) |
| The contact rate refers to the percentage of attempts where the gripper makes contact with the target object, while the success rate indicates the ... | definition/direction/unit from same section | p. 6 (5.2. Main Results) |
| Interestingly, we observe a consistent gap between the success rate and the contact rate, with the latter being significantly higher. | definition/direction/unit from same section | p. 7 (5.2. Main Results) |
| We also report the success rates for other fundamental skills, including door opening/closing, button pressing, lever turning and knob twisting. | definition/direction/unit from same section | p. 7 (5.2. Main Results) |
| As shown in Table 4, both approaches effectively incorporate grounding knowledge. | definition/direction/unit from same section | p. 8 (5.4. Ablation Study) |
| We evaluate different grounding representations and their impact on model performance. | definition/direction/unit from same section | p. 8 (5.4. Ablation Study) |
| Figure 1. Examples of generated data and mask guidance for robot policy. The generated data includes more object distractors in the scene, leading to ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 2. Data Generation Pipeline. The pipeline is composed of three key stages: (a) First, we extract informative object attributes in both keyword and ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared to baseline models, our method consistently outperforms across all tasks. | comparison identity and matched condition | p. 7 (5.2. Main Results) |
| Baselines. • ACT [50]: A transformer-based policy network introduced by ALOHA [50]. | comparison identity and matched condition | p. 6 (5.2. Main Results) |
| To evaluate our approach, we compare it with three wellestablished, easy-to-implement methods as baselines. | comparison identity and matched condition | p. 6 (5.2. Main Results) |
| Notably, in more challenging scenarios, mask guidance achieves approximately 100% relative improvement over non-mask baselines, highlighting its crucial role in handling complex, unseen situations. | comparison identity and matched condition | p. 7 (5.3. Zero-shot Evaluation) |
| Ablation Study on Training Data and Grounded Masks. "Ori. | comparison identity and matched condition | p. 8 (5.4. Ablation Study) |
| For evaluation, we compute the mean Intersection over Union (mIoU) of the predicted simulation results, with a performance comparison shown in Table 6. | comparison identity and matched condition | p. 8 (5.4. Ablation Study) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation Study on Grounded VLM. "Zero-shot" refers to the zero-shot evaluation of the grounded VLM. "Sim. data" and "VLM data" denotes the use of ... | component/input/data sensitivity | p. 8 (5.4. Ablation Study) |
| Figure 1. Examples of generated data and mask guidance for robot policy. The generated data includes more object distractors in the scene, leading to ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| We perform ablation studies by training models with different datasets and mask configurations. | component/input/data sensitivity | p. 7 (5.4. Ablation Study) |
| Since the pre-trained model is unavailable, we reproduce it here without large-scale pre-training or image prediction. | component/input/data sensitivity | p. 7 (5.2. Main Results) |
| Ablation Study on Training Data and Grounded Masks. "Ori. | component/input/data sensitivity | p. 8 (5.4. Ablation Study) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this work, we introduce grounding masks as a promising intermediate representation that balances two key aspects: (1) Effective spatial guidance, which not only ... | Notably, in more challenging scenarios, mask guidance achieves approximately 100% relative improvement over non-mask baselines, highlighting its crucial role in handling complex, unseen situations. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5.3. Zero-shot Evaluation), p. 8 (5.4. Ablation Study), p. 7 (5.2. Main Results), p. 8 (5.4. Ablation Study), p. 6 (5.2. Main Results), p. 6 (5.2. Main Results) |
| Primary metric/result | Fine-tuning on simulation data alone significantly improves results but risks losing the knowledge embedded in the original VLM dataset. | numeric claim only at cited anchor | p. 8 (5.4. Ablation Study) |

- Numeric sentences retained from the body:
- **p. 7 / 5.3. Zero-shot Evaluation - extractive PDF cue:** We exclude 30 classes, comprising 597 objects, as unseen and filter out 1/4 of the objects from each of the remaining classes, resulting in a ...
- **p. 7 / 5.4. Ablation Study - extractive PDF cue:** To accelerate our ablation study, we use a subset of the dataset, as full training and evaluation would require several days on 8 NVIDIA 4090 ...
- **p. 8 / 5.4. Ablation Study - extractive PDF cue:** Point, Low-dim 72 / 28 44 / 12 56 / 18 42 / 14 Point, Image 76 / 32 60 / 26 68 / 32 ...
- **p. 5 / 4.2. Grounded Vision-Language Model - extractive PDF cue:** (1) The model perceives the image through a prompt formatted as: "The <IMAGE> provides an overview of the picture," where the <IMAGE> token is replaced ...
- **p. 5 / 4.3. Grounded Policy Network - extractive PDF cue:** The encoded feature Zv consists of a global representation ZCLS v ∈R1×Dv, obtained from the CLS token, and a set of local patch representations ZP ...
- **p. 5 / 4.3. Grounded Policy Network - extractive PDF cue:** The perceiver takes as input the 14×14 patch features, denoted as ZP v , extracted from the vision encoder, along 22544

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 2. Data Generation Pipeline. The pipeline is composed of three key stages: (a) First, we extract informative object attributes in both keyword and ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | This limitation likely arises from design shortcomings, as these models encode language input as a single, global text feature, which is inadequate for the ... | p. 7 (5.2. Main Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| To optimize inference time, segmentation masks are extracted from the grounded VLM only once, at the beginning of the episode. | p. 6 (4.4. Training and Inference) |
| We use the publicly available BC-Transformer implementation from 22545 | p. 6 (5.2. Main Results) |
| This limitation likely arises from design shortcomings, as these models encode language input as a single, global text feature, which is inadequate for the ... | p. 7 (5.2. Main Results) |
| For evaluation, we compute the mean Intersection over Union (mIoU) of the predicted simulation results, with a performance comparison shown in Table 6. | p. 8 (5.4. Ablation Study) |
| The encoded visual feature Zv ∈R197×Dv is computed as follows: Zv = ViTMAE(Linear(Concat(xv, Mo, Mp))), (3) where Dv denotes the hidden dimension of the ... | p. 5 (4.3. Grounded Policy Network) |
| The result is then fed into a pre-trained ViTMAE encoder [16]. | p. 5 (4.3. Grounded Policy Network) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Data Generation Pipeline. The pipeline is composed of three key stages: (a) First, we extract informative object attributes in both keyword and descriptive ...
- **p. 7 / 5.2. Main Results - extractive PDF cue:** This limitation likely arises from design shortcomings, as these models encode language input as a single, global text feature, which is inadequate for the nuanced ...

- **PDF anchors reviewed:** datasets p. 8 (5.4. Ablation Study), p. 7 (5.2. Main Results), p. 6 (5.1. Simulation Setting), p. 6 (5.2. Main Results), p. 7 (5.2. Main Results), p. 8 (5.4. Ablation Study), metrics p. 6 (5.2. Main Results), p. 6 (5.2. Main Results), p. 7 (5.2. Main Results), p. 7 (5.2. Main Results), p. 8 (5.4. Ablation Study), p. 8 (5.4. Ablation Study), baselines p. 7 (5.2. Main Results), p. 6 (5.2. Main Results), p. 6 (5.2. Main Results), p. 7 (5.3. Zero-shot Evaluation), p. 8 (5.4. Ablation Study), p. 8 (5.4. Ablation Study), results p. 7 (5.3. Zero-shot Evaluation), p. 8 (5.4. Ablation Study), p. 7 (5.2. Main Results), p. 8 (5.4. Ablation Study), p. 6 (5.2. Main Results), p. 6 (5.2. Main Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
