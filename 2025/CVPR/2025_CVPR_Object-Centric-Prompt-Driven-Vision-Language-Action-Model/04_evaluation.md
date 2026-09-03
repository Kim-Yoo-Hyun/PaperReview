# Evaluation - Object-Centric Prompt-Driven Vision-Language-Action Model for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Li_Object-Centric_Prompt-Driven_Vision-Language-Action_Model_for_Robotic_Manipulation_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_Object-Centric_Prompt-Driven_Vision-Language-Action_Model_for_Robotic_Manipulation_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.3. Ablation Study), p. 8 (4.3.2. Tolerance Analysis of Prompt Noise), p. 6 (4.2. Comparisons with Baselines), p. 7 (Figure/Table caption), p. 8 (4.3. Ablation Study), p. 7 (4.3. Ablation Study)): Beginning with Ex1, where only a 2D position prompt is provided, the model achieves impressive performance with scores of 0.42/0.37.

## Evaluation Body Digest

- **p. 6 / 4.2. Comparisons with Baselines - extractive body cue:** Simulator visualizations are shown in the left of Figure 4, illustrating the prompt input, the robot's contact state with the object, and the final state ...
- **p. 6 / 4.1. Setup Details - extractive body cue:** Following previous work [31, 40], we utilize SAPIEN [53] along with the PartNet-Mobility dataset to construct an environment, interacting with about 1500 object shapes under ...
- **p. 8 / 4.4. Real-world Experiment - extractive body cue:** We conduct experiments involving interaction with various real-world objects without additional sim-to-real finetuning.
- **p. 8 / 4.4. Real-world Experiment - extractive body cue:** During fine-tuning, the image input includes only the object, while the language input excludes all 2D prompts but incorporates the current robot state to ensure ...
- **p. 7 / 4.3. Ablation Study - extractive body cue:** Visualization results in SAPIEN simulator and real world. 푎푝 0 푎푧 0 푎푦 0 푎푚 0 Seen Unseen Ex1 ✓ - - - 0.42 0.37 ...
- **p. 7 / 4.3. Ablation Study - extractive body cue:** Consequently, it becomes challenging to make accurate object-centric manipulation predictions when relying solely on language prompts.
- **p. 6 / 4.1. Setup Details - extractive body cue:** We utilize the manipulation success rate to assess the effectiveness of the manipulation, calculated as the ratio of successfully manipulated samples to the total number ...
- **p. 8 / 4.3. Ablation Study - extractive body cue:** Real-world success rate. * contains multiple steps.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Experiment (p. 6); 4.4. Real-world Experiment (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | Beginning with Ex1, where only a 2D position prompt is provided, the model achieves impressive performance with scores of 0.42/0.37. | p. 6 (4.3. Ablation Study) |
| 4.3.2. Tolerance Analysis of Prompt Noise | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results, shown in Figure 5, indicate that with 10% and 20% noise, our method achieves performance levels comparable to those of the noise-free ... | p. 8 (4.3.2. Tolerance Analysis of Prompt Noise) |
| 4.2. Comparisons with Baselines | EMPIRICAL / REAL-ROBOT OR HARDWARE | For automatically generated prompts, the results are 0.64/0.62 on seen and unseen tasks, still outperforming the baselines. | p. 6 (4.2. Comparisons with Baselines) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 2. Ablation Study. dict rotation given the same pixel coordinate, which results in lower scores of 0.35/0.31. This shows even without direc- tional ... | p. 7 (Figure/Table caption) |
| 4.3. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | Real-world success rate. * contains multiple steps. | p. 8 (4.3. Ablation Study) |

## Dataset / Benchmark Role

- **p. 6 / 4.2. Comparisons with Baselines - extractive body cue:** Simulator visualizations are shown in the left of Figure 4, illustrating the prompt input, the robot's contact state with the object, and the final state ...
- **p. 6 / 4.1. Setup Details - extractive body cue:** Following previous work [31, 40], we utilize SAPIEN [53] along with the PartNet-Mobility dataset to construct an environment, interacting with about 1500 object shapes under ...
- **p. 8 / 4.4. Real-world Experiment - extractive body cue:** We conduct experiments involving interaction with various real-world objects without additional sim-to-real finetuning.
- **p. 8 / 4.4. Real-world Experiment - extractive body cue:** During fine-tuning, the image input includes only the object, while the language input excludes all 2D prompts but incorporates the current robot state to ensure ...
- **p. 7 / 4.3. Ablation Study - extractive body cue:** Visualization results in SAPIEN simulator and real world. 푎푝 0 푎푧 0 푎푦 0 푎푚 0 Seen Unseen Ex1 ✓ - - - 0.42 0.37 ...
- **p. 7 / 4.3. Ablation Study - extractive body cue:** Consequently, it becomes challenging to make accurate object-centric manipulation predictions when relying solely on language prompts.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. (a) shows our expression of different color prompts. (b) shows that we utilize a sequence of images with crayon visual prompts to express ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. We design training pairs that convey varying levels of information to enable the model to comprehend each type of prompt and introduce loss ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Illustration of model inference with input generated in different ways. GPT-4 [1] is then prompted to select lines from all candidates to represent ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Comparison of our method against baseline methods. (s) and (f) denote suction gripper and finger gripper, respectively. Bold text indicates the highest score ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Visualization results in SAPIEN simulator and real world. 푎푝 0 푎푧 0 푎푦 0 푎푚
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Ablation Study. dict rotation given the same pixel coordinate, which results in lower scores of 0.35/0.31. This shows even without direc- tional prompts, ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. Robustness analysis on the noise in prompts. Open the trashcan Open microwave* Lift lid Wipe
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Real-world success rate. * contains multiple steps.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Simulator visualizations are shown in the left of Figure 4, illustrating the prompt input, the robot's contact state with the object, and the final ... | embodiment, simulator version and control stack | p. 6 (4.2. Comparisons with Baselines), p. 6 (4.1. Setup Details) |
| Task/environment | Following previous work [31, 40], we utilize SAPIEN [53] along with the PartNet-Mobility dataset to construct an environment, interacting with about 1500 object shapes ... | reset, timeout, object/scene variation | p. 6 (4.1. Setup Details), p. 8 (4.4. Real-world Experiment) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 5 (3.4.1. Model Inference), p. 4 (3.3.2. Policy Learning) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 2 (1. Introduction), p. 4 (3.3.2. Policy Learning) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We utilize the manipulation success rate to assess the effectiveness of the manipulation, calculated as the ratio of successfully manipulated samples to the total ... | definition/direction/unit from same section | p. 6 (4.1. Setup Details) |
| Real-world success rate. * contains multiple steps. | definition/direction/unit from same section | p. 8 (4.3. Ablation Study) |
| The fine-tuned model is then evaluated on these tasks, achieving success rates of 5/10 and 6/10, respectively. | definition/direction/unit from same section | p. 8 (4.4. Real-world Experiment) |
| Given that the performance of the generative video-based execution policy is highly dependent on the quality of the generated videos, we believe this score ... | definition/direction/unit from same section | p. 6 (4.2. Comparisons with Baselines) |
| Bold text indicates the highest score within each end-effector type. | definition/direction/unit from same section | p. 7 (4.3. Ablation Study) |
| Ablation Study. dict rotation given the same pixel coordinate, which results in lower scores of 0.35/0.31. | definition/direction/unit from same section | p. 7 (4.3. Ablation Study) |
| Figure 2. We design training pairs that convey varying levels of information to enable the model to comprehend each type of prompt and introduce ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 3. Illustration of model inference with input generated in different ways. GPT-4 [1] is then prompted to select lines from all candidates to ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| For automatically generated prompts, the results are 0.64/0.62 on seen and unseen tasks, still outperforming the baselines. | comparison identity and matched condition | p. 6 (4.2. Comparisons with Baselines) |
| Comparison of our method against baseline methods. | comparison identity and matched condition | p. 7 (4.3. Ablation Study) |
| The above three methods use suction gripper as the endeffector, which is compared with ours(s) in Table. | comparison identity and matched condition | p. 6 (4.2. Comparisons with Baselines) |
| This configuration results in a performance drop compared to inputting prompts from both modalities. | comparison identity and matched condition | p. 7 (4.3. Ablation Study) |
| We conduct experiments involving interaction with various real-world objects without additional sim-to-real finetuning. | comparison identity and matched condition | p. 8 (4.4. Real-world Experiment) |
| Ablation experiments regarding the effectiveness of each loss and failure case analysis are shown in Appendix.5 and Appendix.6. | comparison identity and matched condition | p. 8 (4.3.2. Tolerance Analysis of Prompt Noise) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In our experiments, we mainly focus on exploring the following questions: • Section 4.3.1: What is the effect of different types of prompts on ... | component/input/data sensitivity | p. 6 (4. Experiment) |
| Additionally, to investigate the differential effects of visual and language prompts, in the last row of Table 2, we enable the model to learn ... | component/input/data sensitivity | p. 7 (4.3. Ablation Study) |
| Ablation experiments regarding the effectiveness of each loss and failure case analysis are shown in Appendix.5 and Appendix.6. | component/input/data sensitivity | p. 8 (4.3.2. Tolerance Analysis of Prompt Noise) |
| Table 2. Ablation Study. dict rotation given the same pixel coordinate, which results in lower scores of 0.35/0.31. This shows even without direc- tional ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| 3, we further explore whether it is possible to fine-tune the model using prompts provided during the first set of executions for a specific ... | component/input/data sensitivity | p. 8 (4.4. Real-world Experiment) |
| Analysis on The Effect of Different Types of Prompt In Table 2 Ex1-Ex3, since our model is able to handle various input patterns thanks ... | component/input/data sensitivity | p. 6 (4.3. Ablation Study) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are as follows: • 1) We propose employing a sequence of key-frames presented with prompts to explicitly convey the task ... | Beginning with Ex1, where only a 2D position prompt is provided, the model achieves impressive performance with scores of 0.42/0.37. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.3. Ablation Study), p. 8 (4.3.2. Tolerance Analysis of Prompt Noise), p. 6 (4.2. Comparisons with Baselines), p. 7 (Figure/Table caption), p. 8 (4.3. Ablation Study), p. 7 (4.3. Ablation Study) |
| Primary metric/result | The results, shown in Figure 5, indicate that with 10% and 20% noise, our method achieves performance levels comparable to those of the noise-free ... | numeric claim only at cited anchor | p. 8 (4.3.2. Tolerance Analysis of Prompt Noise) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Setup Details - extractive body cue:** Following previous work [31, 40], we utilize SAPIEN [53] along with the PartNet-Mobility dataset to construct an environment, interacting with about 1500 object shapes under ...
- **p. 6 / 4.1. Setup Details - extractive body cue:** We follow the procedure in Section 3.2 to collect prompts within the simulator, which takes about 6-8 hours to collect about 10,000 training samples.
- **p. 8 / 4.4. Real-world Experiment - extractive body cue:** The model is finetuned for 20 epochs using key frames and the corresponding predicted 3D poses from successful trials in the previous experiment as ground ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Limitation: As for the limitation, though our method can not directly avoid obstacles, we can incorporate collision-free motion planner library like curobo [48] to ... | p. 8 (5. Conclusion) |
| body limitation/failure cue | Ablation experiments regarding the effectiveness of each loss and failure case analysis are shown in Appendix.5 and Appendix.6. | p. 8 (4.3.2. Tolerance Analysis of Prompt Noise) |
| body limitation/failure cue | However, our results demonstrate the robustness of CrayonRobo in handling such input inaccuracies. | p. 6 (4.2. Comparisons with Baselines) |
| body limitation/failure cue | This is because the model is trained to manipulate objects, it can, to some extent, correct the noise in the prompts. | p. 6 (4.2. Comparisons with Baselines) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 1 Visual prompt conditioned model RT-trajectory [20]: Since the RT-Trajectory code is not publicly available at the time of this paper's submission, we replicate ... | p. 6 (4.2. Comparisons with Baselines) |
| The model is finetuned for 20 epochs using key frames and the corresponding predicted 3D poses from successful trials in the previous experiment as ... | p. 8 (4.4. Real-world Experiment) |
| We further conduct experiments involving tasks with multiple steps, such as pulling a door and subsequently pushing it. | p. 6 (4.2. Comparisons with Baselines) |
| Real-world success rate. * contains multiple steps. | p. 8 (4.3. Ablation Study) |
| This approach aims to preserve the inherent existing pre-trained knowledge, particularly in simto-real transfer, while enhancing the model's ability to comprehend visual prompts and ... | p. 3 (3.3.1. Model Architecture) |
| Simultaneously, text prompts 푃are encoded into text features using LLaMa's pre-trained tokenizer [51]. | p. 3 (3.3.1. Model Architecture) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive body cue:** Limitation: As for the limitation, though our method can not directly avoid obstacles, we can incorporate collision-free motion planner library like curobo [48] to realize ...
- **p. 8 / 4.3.2. Tolerance Analysis of Prompt Noise - extractive body cue:** Ablation experiments regarding the effectiveness of each loss and failure case analysis are shown in Appendix.5 and Appendix.6.
- **p. 6 / 4.2. Comparisons with Baselines - extractive body cue:** However, our results demonstrate the robustness of CrayonRobo in handling such input inaccuracies.
- **p. 6 / 4.2. Comparisons with Baselines - extractive body cue:** This is because the model is trained to manipulate objects, it can, to some extent, correct the noise in the prompts.

- **Evidence anchors reviewed:** datasets p. 6 (4.2. Comparisons with Baselines), p. 6 (4.1. Setup Details), p. 8 (4.4. Real-world Experiment), p. 8 (4.4. Real-world Experiment), p. 7 (4.3. Ablation Study), p. 7 (4.3. Ablation Study), metrics p. 6 (4.1. Setup Details), p. 8 (4.3. Ablation Study), p. 8 (4.4. Real-world Experiment), p. 6 (4.2. Comparisons with Baselines), p. 7 (4.3. Ablation Study), p. 7 (4.3. Ablation Study), baselines p. 6 (4.2. Comparisons with Baselines), p. 7 (4.3. Ablation Study), p. 6 (4.2. Comparisons with Baselines), p. 7 (4.3. Ablation Study), p. 8 (4.4. Real-world Experiment), p. 8 (4.3.2. Tolerance Analysis of Prompt Noise), results p. 6 (4.3. Ablation Study), p. 8 (4.3.2. Tolerance Analysis of Prompt Noise), p. 6 (4.2. Comparisons with Baselines), p. 7 (Figure/Table caption), p. 8 (4.3. Ablation Study), p. 7 (4.3. Ablation Study).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
