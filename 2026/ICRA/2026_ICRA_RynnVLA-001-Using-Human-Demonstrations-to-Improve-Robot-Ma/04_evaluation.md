# Evaluation - RynnVLA-001: Using Human Demonstrations to Improve Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_3.html; PDF retrieval source: https://arxiv.org/pdf/2509.15212v1. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (5 EXPERIMENTS), p. 12 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 12 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS)): In contrast, RynnVLA-001-Video achieves a significant performance improvement, indicating that priors learned from ego-centric videos are effective for VLA adaptation.

## Evaluation Body Digest

- **p. 7 / 5 Experiments - extractive body cue:** To train and evaluate our proposed RynnVLA-001 model, we collect a new real-world manipulation dataset using a LeRobot SO100 robotic arm (Cadene et al., 2024).
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** To evaluate generalization, each task is evaluated on multiple robotic arms, each operating in a unique physical environment.
- **p. 7 / 5 Experiments - extractive body cue:** The dataset comprises expert demonstrations collected through human teleoperation.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** To enhance the richness and complexity of the data, the scenes of manipulation are set to vary from containing only target objects to more complex ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** 2Given the low performance of the RynnVLA-001-Scratch model, its evaluation is limited to 5 trials per task and setting, and conducted on a single robot ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** To assess the impact of head complexity, we perform an ablation study comparing this design with a deeper five-layer MLP head on the Calvin Task ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** 1 2 3 4 5 256 x 256 Task ABC -> D 92.7 83.7 73.5 62.1 53.2 3.652 Raw Actions Prediction Task ABC -> D ...
- **p. 12 / 5 EXPERIMENTS - extractive body cue:** Under normal conditions (Figure 5(a)), the robot successfully completes the task.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 5 EXPERIMENTS (p. 7); 5 Experiments (p. 7); 5 EXPERIMENTS (p. 8); 5 EXPERIMENTS (p. 9); 5 EXPERIMENTS (p. 10); 5 EXPERIMENTS (p. 11); 5 EXPERIMENTS (p. 12).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | In contrast, RynnVLA-001-Video achieves a significant performance improvement, indicating that priors learned from ego-centric videos are effective for VLA adaptation. | p. 9 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | In contrast, our full RynnVLA-001 model, trained on our comprehensive dataset including distractors, achieves a 90% success rate (9/10) on this task. | p. 12 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | For Pi0, when distractor objects appear on the desk, the success rates drop significantly, indicating its limited instruction-following capability. | p. 9 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Quantitative results confirm this: for targets on the right, the success rate drops slightly from 100% (5/5) to 80% (4/5) after masking. | p. 12 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our model, RynnVLA-001, demonstrates substantially higher overall performance, outperforming both GR00T N1.5 and Pi0 across all three tasks. | p. 8 (5 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 7 / 5 Experiments - extractive body cue:** To train and evaluate our proposed RynnVLA-001 model, we collect a new real-world manipulation dataset using a LeRobot SO100 robotic arm (Cadene et al., 2024).
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** To evaluate generalization, each task is evaluated on multiple robotic arms, each operating in a unique physical environment.
- **p. 7 / 5 Experiments - extractive body cue:** The dataset comprises expert demonstrations collected through human teleoperation.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** To enhance the richness and complexity of the data, the scenes of manipulation are set to vary from containing only target objects to more complex ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** 2Given the low performance of the RynnVLA-001-Scratch model, its evaluation is limited to 5 trials per task and setting, and conducted on a single robot ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** To assess the impact of head complexity, we perform an ablation study comparing this design with a deeper five-layer MLP head on the Calvin Task ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** 1 2 3 4 5 256 x 256 Task ABC -> D 92.7 83.7 73.5 62.1 53.2 3.652 Raw Actions Prediction Task ABC -> D ...
- **p. 12 / 5 EXPERIMENTS - extractive body cue:** Under normal conditions (Figure 5(a)), the robot successfully completes the task.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: 1) Ego-Centric Video Generative Pretraining: An ego-centric Image-to-Video (I2V) model is trained on ego-centric human manipulation videos. This stage enables the model to ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To train and evaluate our proposed RynnVLA-001 model, we collect a new real-world manipulation dataset using a LeRobot SO100 robotic arm (Cadene et al., ... | embodiment, simulator version and control stack | p. 7 (5 Experiments), p. 8 (5 EXPERIMENTS) |
| Task/environment | To evaluate generalization, each task is evaluated on multiple robotic arms, each operating in a unique physical environment. | reset, timeout, object/scene variation | p. 8 (5 EXPERIMENTS), p. 7 (5 Experiments) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 4 (3 Methodology), p. 4 (3 Methodology) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 2 (1 INTRODUCTION), p. 6 (3 METHODOLOGY) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| However, it exhibits a limited localization capability, capping its performance at a success rate of 50.0%. | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| 5.2 Comparison with SoTA methods Table 1 presents a detailed comparison of task-specific and average success rates. | definition/direction/unit from same section | p. 8 (5 EXPERIMENTS) |
| We report the success rates in three different evaluation settings. | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| Method Task Task Success Rate (%) Avg. | definition/direction/unit from same section | p. 10 (5 EXPERIMENTS) |
| For the targets on the left, the success rate decreases from 80% (4/5) to 0%. | definition/direction/unit from same section | p. 12 (5 EXPERIMENTS) |
| Quantitative results confirm this: for targets on the right, the success rate drops slightly from 100% (5/5) to 80% (4/5) after masking. | definition/direction/unit from same section | p. 12 (5 EXPERIMENTS) |
| 5, increasing the depth of action head is surprisingly detrimental to performance, causing the evaluation score to decrease substantially from 4.019 to 3.323. | definition/direction/unit from same section | p. 10 (5 EXPERIMENTS) |
| Our model, RynnVLA-001, demonstrates substantially higher overall performance, outperforming both GR00T N1.5 and Pi0 across all three tasks. | definition/direction/unit from same section | p. 8 (5 EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We compare our model with two strong open-source baselines, namely GR00T N1.5 (Bjorck et al., 2025a) and Pi0 (Black et al., 2024). | comparison identity and matched condition | p. 8 (5 EXPERIMENTS) |
| Our model, RynnVLA-001, demonstrates substantially higher overall performance, outperforming both GR00T N1.5 and Pi0 across all three tasks. | comparison identity and matched condition | p. 8 (5 EXPERIMENTS) |
| We compare three initialization strategies for the final VLA model: 1) RynnVLA-001-Scratch: A baseline initialized from random weights, skipping all pretraining. | comparison identity and matched condition | p. 9 (5 EXPERIMENTS) |
| 2) RynnVLA-001-Chameleon: A stronger baseline initialized directly from the pretrained weights of the Chameleon Text-to-Image (T2I) model (Team, 2024), bypassing our video pretraining stage. | comparison identity and matched condition | p. 9 (5 EXPERIMENTS) |
| 5, predicting actions in the VAE's latent space outperforms the direct prediction of raw actions. | comparison identity and matched condition | p. 10 (5 EXPERIMENTS) |
| Furthermore, our choice of 384 × 384 strikes a balance: 1) it maintains high reconstruction fidelity by using the resolution closer to the VQGAN's ... | comparison identity and matched condition | p. 10 (5 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To investigate the effectiveness of our proposed two-stage pretraining pipeline, we conduct a comprehensive ablation study, with results presented in Table 3 and Table ... | component/input/data sensitivity | p. 9 (5 EXPERIMENTS) |
| To evaluate the effectiveness of the component, we conduct an ablation study on the Calvin ABC->D benchmark, comparing the performance of predicting VAE embeddings ... | component/input/data sensitivity | p. 10 (5 EXPERIMENTS) |
| A variant of RynnVLA-001 is trained solely on data without distractor objects. | component/input/data sensitivity | p. 12 (5 EXPERIMENTS) |
| By incorporating this second pretraining stage where the model learns to predict human trajectories, our full model, RynnVLA-001, achieves the best performance among all ... | component/input/data sensitivity | p. 9 (5 EXPERIMENTS) |
| For experimental efficiency, our full model and the ablated variants are trained from the pretraining weights of RynnVLA-001-Video but for a reduced number of ... | component/input/data sensitivity | p. 10 (5 EXPERIMENTS) |
| 5.4 Ablation Study on Model Designs | component/input/data sensitivity | p. 11 (5 EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this work, we propose RynnVLA-001, a VLA model enhanced by video generation pretraining. | In contrast, RynnVLA-001-Video achieves a significant performance improvement, indicating that priors learned from ego-centric videos are effective for VLA adaptation. | PDF body cue; verify exact table/figure and matched conditions | p. 9 (5 EXPERIMENTS), p. 12 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 12 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS) |
| Primary metric/result | In contrast, our full RynnVLA-001 model, trained on our comprehensive dataset including distractors, achieves a 90% success rate (9/10) on this task. | numeric claim only at cited anchor | p. 12 (5 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** 2Given the low performance of the RynnVLA-001-Scratch model, its evaluation is limited to 5 trials per task and setting, and conducted on a single robot ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** In contrast, all other models are evaluated with 60 trials per task.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** These trials are distributed evenly across two robotic arms, with each arm conducting 10 trials for each of the three scenarios (totaling 30 trials per ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** 1 2 3 4 5 256 x 256 Task ABC -> D 92.7 83.7 73.5 62.1 53.2 3.652 Raw Actions Prediction Task ABC -> D ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** 5, a substantial performance drop is observed when the resolution decreases from our proposed 384×384 to 256×256.
- **p. 11 / 5 EXPERIMENTS - extractive body cue:** Given an input image and a text prompt, an I2V model is trained to predict the next 7 frames.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | At a lower resolution of 256 × 256, the VQGAN's reconstruction quality degrades, the VQGAN fails to generate high-fidelity reconstructions, resulting in imprecise visual ... | p. 10 (5 EXPERIMENTS) |
| body limitation/failure cue | A trial is marked as a failure under any of the following conditions: 1) The time limit is exceeded. | p. 8 (5 EXPERIMENTS) |
| body limitation/failure cue | A total of 5 failure cases of the 10 trials consistently select a distractor object. | p. 12 (5 EXPERIMENTS) |
| body limitation/failure cue | However, when we elevate the front camera, altering the scene's projective geometry, the model fails to insert 12 | p. 12 (5 EXPERIMENTS) |
| body limitation/failure cue | 2) The model makes more than five consecutive failed attempts to grasp a target object. | p. 8 (5 EXPERIMENTS) |
| body limitation/failure cue | This degradation is attributed to the resolution mismatch with the VQGAN component, which is pretrained exclusively on 512 × 512 images. | p. 10 (5 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The pipeline consists of the following steps: Keypoint Detection. | p. 7 (5 EXPERIMENTS) |
| The predicted action embedding is then immediately passed to the decoder of the ActionVAE. | p. 7 (5 EXPERIMENTS) |
| A trial is marked as a failure under any of the following conditions: 1) The time limit is exceeded. | p. 8 (5 EXPERIMENTS) |
| We use the official code of GR00T N1.5 and Pi0 and strictly follow the instructions to finetune the model. | p. 8 (5 EXPERIMENTS) |
| In contrast, all other models are evaluated with 60 trials per task. | p. 9 (5 EXPERIMENTS) |
| Benefiting from the pretrained T2I checkpoint, the RynnVLA-001-Chameleon model achieves reasonable results on simple grasping. | p. 9 (5 EXPERIMENTS) |
| All models are trained with reduced epochs for efficiency; scores are for relative comparison. | p. 10 (5 EXPERIMENTS) |
| In this work, we propose to use a Variational Autoencoder (VAE) to compress action chunks into compact latent embeddings. | p. 10 (5 EXPERIMENTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 5 EXPERIMENTS - extractive body cue:** At a lower resolution of 256 × 256, the VQGAN's reconstruction quality degrades, the VQGAN fails to generate high-fidelity reconstructions, resulting in imprecise visual tokens ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** A trial is marked as a failure under any of the following conditions: 1) The time limit is exceeded.
- **p. 12 / 5 EXPERIMENTS - extractive body cue:** A total of 5 failure cases of the 10 trials consistently select a distractor object.
- **p. 12 / 5 EXPERIMENTS - extractive body cue:** However, when we elevate the front camera, altering the scene's projective geometry, the model fails to insert 12
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** 2) The model makes more than five consecutive failed attempts to grasp a target object.
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** This degradation is attributed to the resolution mismatch with the VQGAN component, which is pretrained exclusively on 512 × 512 images.

- **Evidence anchors reviewed:** datasets p. 7 (5 Experiments), p. 8 (5 EXPERIMENTS), p. 7 (5 Experiments), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), metrics p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 12 (5 EXPERIMENTS), p. 12 (5 EXPERIMENTS), baselines p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), results p. 9 (5 EXPERIMENTS), p. 12 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 12 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
