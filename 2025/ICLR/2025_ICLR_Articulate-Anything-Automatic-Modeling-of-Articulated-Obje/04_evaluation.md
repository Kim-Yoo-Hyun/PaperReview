# Evaluation - Articulate-Anything: Automatic Modeling of Articulated Objects via a Vision-Language Foundation Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=s3FTX4Ay55; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/114017. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (Figure/Table caption), p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS)): Figure 10: In-context learning. ARTICULATE-ANYTHING improves with the number of prompting examples, demonstrating in-context learning. The zero-shot performance (0 example) is included. We conduct this ablation study on the Faucet ...

## Evaluation Body Digest

- **p. 10 / 5 EXPERIMENTS - extractive body cue:** Articulate real-world videos 1 RL training in simulation 2 Transfer to real 3 Figure 13: Robotic Application: ARTICULATE-ANYTHING can automatically generate assets given in-the-wild input ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** We hope that our work contributes to bridging the gap between the digital and physical worlds, enabling 3D creators to focus on artistic vision rather ...
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** Both methods were trained or fine-tuned on five object categories in the PartNet-Mobility dataset.
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** Datasets: We use the Partnet-Mobility dataset (Mo et al., 2018) which includes human annotations for ∼2.3K objects, ∼1.9K revolute joints, and ∼7.6K prismatic joints.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** As before, we select both OOD and ID objects.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** Performance on articulation tasks improves with more grounded modalities.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Casual inputs: Our video-based approach excels with casually captured inputs in cluttered environments while baselines require extensive manual curation (more details in Appendix A.4 Fig.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** We conduct this ablation study on the Faucet object category for link placement and StorageFurniture for joint prediction.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 5 EXPERIMENTS (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 10: In-context learning. ARTICULATE-ANYTHING improves with the number of prompting examples, demonstrating in-context learning. The zero-shot performance (0 example) is included. We conduct ... | p. 9 (Figure/Table caption) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | 1 2 3 Iteration 70 80 90 100 Success Rate (%) 80.2 85.5 86.0 84.0 89.4 90.1 Link Placement Ground Truth Critic 1 2 ... | p. 9 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Both policies trained via ARTICULATE-ANYTHING's and human-annotated assets achieve 100% success rate in the real world. | p. 10 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Evaluation Metrics: We assess performance using success rates for each task. | p. 6 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our approach significantly outperforms all baselines in the joint prediction task. | p. 7 (5 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 10 / 5 EXPERIMENTS - extractive body cue:** Articulate real-world videos 1 RL training in simulation 2 Transfer to real 3 Figure 13: Robotic Application: ARTICULATE-ANYTHING can automatically generate assets given in-the-wild input ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** We hope that our work contributes to bridging the gap between the digital and physical worlds, enabling 3D creators to focus on artistic vision rather ...
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** Both methods were trained or fine-tuned on five object categories in the PartNet-Mobility dataset.
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** Datasets: We use the Partnet-Mobility dataset (Mo et al., 2018) which includes human annotations for ∼2.3K objects, ∼1.9K revolute joints, and ∼7.6K prismatic joints.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** As before, we select both OOD and ID objects.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** Performance on articulation tasks improves with more grounded modalities.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Casual inputs: Our video-based approach excels with casually captured inputs in cluttered environments while baselines require extensive manual curation (more details in Appendix A.4 Fig.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** We conduct this ablation study on the Faucet object category for link placement and StorageFurniture for joint prediction.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Given text, images, or videos showing an object's motion, ARTICULATE-ANYTHING auto- matically generates its 3D interactable digital twin, handling a wide variety of ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Method Overview. Given a text, image or video input, ARTICULATE-ANYTHING operates in three stages: (1) Mesh Retrieval (Sec. 4.1) retrieves a mesh for ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Mesh retrieval. The top and bottom diagrams provide overviews for reconstructing visual (i.e., image or video) and text inputs, respectively. For visual input, ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Both link placement and joint prediction systems consist of an actor and a critic. The actor produces Python code, which is automatically compiled ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Comparison against the baselines. Our approach significantly outperforms all base- lines in the joint prediction task. We use few-shot prompting and make no ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6: Input modality ablation. Perfor- mance on articulation tasks improves with more grounded modalities. Videos are only used for joint prediction. Input videos provided ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7: In-the-wild Reconstruction. We demonstrate ARTICULATE-ANYTHING's performance input modalities compared to prior works URDFormer and Real2Code. Green and red borders denote correct and incorrect ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 8: Breakdown of failure percentages in all classes. In ARTICULATE-ANYTHING, incorrect link placement leads to all predicted joints being marked incorrect. For baselines, 59.1% ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Articulate real-world videos 1 RL training in simulation 2 Transfer to real 3 Figure 13: Robotic Application: ARTICULATE-ANYTHING can automatically generate assets given in-the-wild ... | embodiment, simulator version and control stack | p. 10 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS) |
| Task/environment | We hope that our work contributes to bridging the gap between the digital and physical worlds, enabling 3D creators to focus on artistic vision ... | reset, timeout, object/scene variation | p. 10 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 16 (A.3 ROBOTIC TRAINING DETAILS), p. 16 (A.3 ROBOTIC TRAINING DETAILS) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In Appendix A.6, table 1 reveals the raw joint prediction errors behind the success rate of Fig. | definition/direction/unit from same section | p. 7 (5 EXPERIMENTS) |
| Evaluation Metrics: We assess performance using success rates for each task. | definition/direction/unit from same section | p. 6 (5 EXPERIMENTS) |
| The breakdowns of success rate of our method by object categories are provided in Fig. | definition/direction/unit from same section | p. 7 (5 EXPERIMENTS) |
| 6 demonstrate that richer input modalities consistently improve success rates, underscoring the importance of visual information in articulation tasks. | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| The critic success rate is computed as the percentage of predictions that are deemed successful by our VLM critic while the ground-truth success rate ... | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| Our method is robust to the choice of VLMs, maintaining high success rates throughout. | definition/direction/unit from same section | p. 10 (5 EXPERIMENTS) |
| GPT-4o Gemini Flash-1.5 Claude-3.5 Sonnet 0 20 40 60 80 100 Success Rate (%) 70.4 77.7 85.7 Figure 11: Base VLMs. | definition/direction/unit from same section | p. 10 (5 EXPERIMENTS) |
| Figure 21: ARTICULATE-ANYTHING's link placement success rate by object categories. 21 | definition/direction/unit from same section | p. 21 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 7: In-the-wild Reconstruction. We demonstrate ARTICULATE-ANYTHING's performance input modalities compared to prior works URDFormer and Real2Code. Green and red borders denote correct and ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Baselines: We compare against two prior state-of-the-art methods: URDFormer (Chen et al., 2024) and Real2Code (Mandi et al., 2024). | comparison identity and matched condition | p. 6 (5 EXPERIMENTS) |
| Our approach significantly outperforms all baselines in the joint prediction task. | comparison identity and matched condition | p. 7 (5 EXPERIMENTS) |
| We also provide an ablation where our method is given the same impoverished input modality as the baselines in Appendix A.5. | comparison identity and matched condition | p. 7 (5 EXPERIMENTS) |
| Table 2: Mesh reconstruction quality. Chamfer distance is included (lower is better) for different models for in-the-wild results. Best results are bolded, second best ... | comparison identity and matched condition | p. 23 (Figure/Table caption) |
| Baseline limitations: URDFormer consistently predicts drawer-like structures and is sensitive to minor misalignments (e.g., slightly tilted drawers). | comparison identity and matched condition | p. 8 (5 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 10: In-context learning. ARTICULATE-ANYTHING improves with the number of prompting examples, demonstrating in-context learning. The zero-shot performance (0 example) is included. We conduct ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| Joint prediction without videos is similarly difficult (e.g., see Fig. | component/input/data sensitivity | p. 7 (5 EXPERIMENTS) |
| We also provide an ablation where our method is given the same impoverished input modality as the baselines in Appendix A.5. | component/input/data sensitivity | p. 7 (5 EXPERIMENTS) |
| 6 AN APPLICATION IN ROBOTICS A 3D model without articulation can only afford trivial interaction such as pick and place. | component/input/data sensitivity | p. 10 (5 EXPERIMENTS) |
| Figure 17: Real2code manually curated inputs and intermediate outputs. We used about 3 to 7 input images per object from different views to obtain ... | component/input/data sensitivity | p. 18 (Figure/Table caption) |
| Figure 19: Comparable Inputs. We compare ARTICULATE-ANYTHING with two baselines, Real2Code and UDRFormer using the same input modalities. The ablation is done on the ... | component/input/data sensitivity | p. 20 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To address this challenge, we present ARTICULATE-ANYTHING, a novel approach in automatic articulation that harnesses the power of leading foundation vision-language models (VLMs) to ... | Figure 10: In-context learning. ARTICULATE-ANYTHING improves with the number of prompting examples, demonstrating in-context learning. The zero-shot performance (0 example) is included. We conduct ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (Figure/Table caption), p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Primary metric/result | 1 2 3 Iteration 70 80 90 100 Success Rate (%) 80.2 85.5 86.0 84.0 89.4 90.1 Link Placement Ground Truth Critic 1 2 ... | numeric claim only at cited anchor | p. 9 (5 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** The position threshold is set to 50mm and the angular threshold to 0.25 radian (∼14.3 degree).
- **p. 23 / A.7 MESH RECONSTRUCTION - extractive body cue:** Method Chamfer distance Articulate-Anything (retrieval) 0.1007 ± 0.062 Real2Code (Oracle) 0.229 ± 0.166 URDFormer (Oracle) 0.429 ± 0.267 URDFormer (DINO) 0.437 ± 0.217 Table 2 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 8 breaks down the failure reasons for each method. | p. 7 (5 EXPERIMENTS) |
| body limitation/failure cue | Figure 8: Breakdown of failure percentages in all classes. In ARTICULATE-ANYTHING, incorrect link placement leads to all predicted joints being marked incorrect. For baselines, ... | p. 9 (Figure/Table caption) |
| body limitation/failure cue | Figure 14: Joint prediction failure visualization. We visualize different types of joint failures, ranging from the most egregious, joint type, to the least, joint ... | p. 14 (Figure/Table caption) |
| body limitation/failure cue | Link placement: Success is determined by the pose difference between predicted and ground-truth links falling below a small threshold. | p. 6 (5 EXPERIMENTS) |
| body limitation/failure cue | Prior works are also limited to simplified inputs as they cannot handle videos. | p. 7 (5 EXPERIMENTS) |
| body limitation/failure cue | Baseline limitations: URDFormer consistently predicts drawer-like structures and is sensitive to minor misalignments (e.g., slightly tilted drawers). | p. 8 (5 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We train policies over 3 random seeds per task for 2 million environment steps using PPO in Stable-Baselines3 library Raffin et al. | p. 16 (A.3 ROBOTIC TRAINING DETAILS) |
| Implementation details are provided in Appendix A.4. | p. 6 (5 EXPERIMENTS) |
| Baselines: We compare against two prior state-of-the-art methods: URDFormer (Chen et al., 2024) and Real2Code (Mandi et al., 2024). | p. 6 (5 EXPERIMENTS) |
| In contrast, URDFormer directly predicts part position (discretized) coordinates, and Real2code operates on oriented bounding box coordinate inputs. | p. 7 (5 EXPERIMENTS) |
| For the text modality, we provide only the semantic part names for link placement; during joint prediction, the model receives the Python code for ... | p. 7 (5 EXPERIMENTS) |
| We demonstrate ARTICULATE-ANYTHING's performance input modalities compared to prior works URDFormer and Real2Code. | p. 8 (5 EXPERIMENTS) |
| Real2Code, which uses multi-view images for mesh reconstruction and text-oriented bounding boxes (OBBs) for joint prediction, achieves good global alignment from DUSt3R but produces ... | p. 8 (5 EXPERIMENTS) |
| We run an actor-only system for one iteration without the critic to isolate the effect of input modalities. | p. 9 (5 EXPERIMENTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 5 EXPERIMENTS - extractive body cue:** 8 breaks down the failure reasons for each method.
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 8: Breakdown of failure percentages in all classes. In ARTICULATE-ANYTHING, incorrect link placement leads to all predicted joints being marked incorrect. For baselines, 59.1% ...
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 14: Joint prediction failure visualization. We visualize different types of joint failures, ranging from the most egregious, joint type, to the least, joint limit. ...
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** Link placement: Success is determined by the pose difference between predicted and ground-truth links falling below a small threshold.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** Prior works are also limited to simplified inputs as they cannot handle videos.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Baseline limitations: URDFormer consistently predicts drawer-like structures and is sensitive to minor misalignments (e.g., slightly tilted drawers).

- **Evidence anchors reviewed:** datasets p. 10 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), metrics p. 7 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), baselines p. 8 (Figure/Table caption), p. 6 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 23 (Figure/Table caption), p. 8 (5 EXPERIMENTS), results p. 9 (Figure/Table caption), p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
