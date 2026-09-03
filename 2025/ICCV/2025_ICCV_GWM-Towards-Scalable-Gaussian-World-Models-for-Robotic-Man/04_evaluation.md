# Evaluation - GWM: Towards Scalable Gaussian World Models for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Lu_GWM_Towards_Scalable_Gaussian_World_Models_for_Robotic_Manipulation_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Lu_GWM_Towards_Scalable_Gaussian_World_Models_for_Robotic_Manipulation_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.5. Ablation Analysis), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (4.5. Ablation Analysis), p. 5 (4. Experiments), p. 6 (Figure/Table caption)): Choice of Gaussian Splatting As shown in Table 4, compared to directly building image-based world model with diffusion transformer on par with [1], introducing Gaussian Splatting significantly improves the success ...

## Evaluation Body Digest

- **p. 8 / 4.5. Ablation Analysis - extractive body cue:** This validates our hypothesis that explicit 3D representation enhances spatial understanding for robot learning compared to pure 2D approaches.
- **p. 8 / 4.5. Ablation Analysis - extractive body cue:** The results confirm that our 3D Gaussian VAE efficiently captures the latent structure of the scene, enabling more compact scene representation while maintaining spatial understanding.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Multi-Task Imitation Learning Results in Robocasa. Average success rates (%) of multi-task agents trained with 50 human demonstrations or 3000 generated demonstrations per ...
- **p. 8 / 4.5. Ablation Analysis - extractive body cue:** The success rate further improves from 18% to 24%.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Quantitative results for future state prediction on Meta-World and FRANKA PNP. LPIPS and SSIM scores are scaled by 100. Best results are highlighted ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Model-based RL Results of GWM and ivideogpt [82] on METAWORLD. The shadow area represents 95% confidence interval (CI) across three random seeds. Each ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. Real-World Experiment Setup. Left: using a Franka Emika Panda robotic arm equipped with an RGB camera, we eval- uate the performance of the ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. The overall pipeline of GWM, which primarily consists of a 3D variational encoder and a latent diffusion transformer. The 3D variational encoder embeds ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Experiments (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.5. Ablation Analysis | EMPIRICAL / SOURCE-REPORTED EVALUATION | Choice of Gaussian Splatting As shown in Table 4, compared to directly building image-based world model with diffusion transformer on par with [1], introducing ... | p. 8 (4.5. Ablation Analysis) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 2. Multi-Task Imitation Learning Results in Robocasa. Average success rates (%) of multi-task agents trained with 50 human demonstrations or 3000 generated demonstrations ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 5. Model-based RL Results of GWM and ivideogpt [82] on METAWORLD. The shadow area represents 95% confidence interval (CI) across three random seeds. ... | p. 7 (Figure/Table caption) |
| 4.5. Ablation Analysis | EMPIRICAL / SOURCE-REPORTED EVALUATION | Choice of 3D Gaussian VAE Further incorporating the 3D VAE component yields consistent improvements across all metrics, including PSNR. | p. 8 (4.5. Ablation Analysis) |
| 4. Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | How is the quality of the action-conditioned video prediction results across different domains? | p. 5 (4. Experiments) |

## Dataset / Benchmark Role

- **p. 8 / 4.5. Ablation Analysis - extractive body cue:** This validates our hypothesis that explicit 3D representation enhances spatial understanding for robot learning compared to pure 2D approaches.
- **p. 8 / 4.5. Ablation Analysis - extractive body cue:** The results confirm that our 3D Gaussian VAE efficiently captures the latent structure of the scene, enabling more compact scene representation while maintaining spatial understanding.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Gaussian World Model (GWM) is a novel branch of world model that predicts dynamic future states and enables robotic manipulation based on the ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. The overall pipeline of GWM, which primarily consists of a 3D variational encoder and a latent diffusion transformer. The 3D variational encoder embeds ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Quantitative results for future state prediction on Meta-World and FRANKA PNP. LPIPS and SSIM scores are scaled by 100. Best results are highlighted ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. Qualitative comparison between models on META- WORLD. GWM successfully predicts better details on the gripper movement (highlighted in blue). the future prediction quality ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. Qualitative visualization on future state prediction of GWM on FRANKA-PNP and ROBOCASA. All predictions are rolled out by applying the unseen action trajectory ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Multi-Task Imitation Learning Results in Robocasa. Average success rates (%) of multi-task agents trained with 50 human demonstrations or 3000 generated demonstrations per ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Model-based RL Results of GWM and ivideogpt [82] on METAWORLD. The shadow area represents 95% confidence interval (CI) across three random seeds. Each ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. Real-World Experiment Setup. Left: using a Franka Emika Panda robotic arm equipped with an RGB camera, we eval- uate the performance of the ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | This validates our hypothesis that explicit 3D representation enhances spatial understanding for robot learning compared to pure 2D approaches. | embodiment, simulator version and control stack | p. 8 (4.5. Ablation Analysis), p. 8 (4.5. Ablation Analysis) |
| Task/environment | The results confirm that our 3D Gaussian VAE efficiently captures the latent structure of the scene, enabling more compact scene representation while maintaining spatial ... | reset, timeout, object/scene variation | p. 8 (4.5. Ablation Analysis) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (3.1. World State Encoding), p. 3 (3.1. World State Encoding) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 6 (4.2. GWM-based Imitation Learning), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 2. Multi-Task Imitation Learning Results in Robocasa. Average success rates (%) of multi-task agents trained with 50 human demonstrations or 3000 generated demonstrations ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| The success rate further improves from 18% to 24%. | definition/direction/unit from same section | p. 8 (4.5. Ablation Analysis) |
| Table 1. Quantitative results for future state prediction on Meta-World and FRANKA PNP. LPIPS and SSIM scores are scaled by 100. Best results are ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Figure 5. Model-based RL Results of GWM and ivideogpt [82] on METAWORLD. The shadow area represents 95% confidence interval (CI) across three random seeds. ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 6. Real-World Experiment Setup. Left: using a Franka Emika Panda robotic arm equipped with an RGB camera, we eval- uate the performance of ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 2. The overall pipeline of GWM, which primarily consists of a 3D variational encoder and a latent diffusion transformer. The 3D variational encoder ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 4. Qualitative visualization on future state prediction of GWM on FRANKA-PNP and ROBOCASA. All predictions are rolled out by applying the unseen action ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 5. Model-based RL Results of GWM and ivideogpt [82] on METAWORLD. The shadow area represents 95% confidence interval (CI) across three random seeds. ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Figure 4. Qualitative visualization on future state prediction of GWM on FRANKA-PNP and ROBOCASA. All predictions are rolled out by applying the unseen action ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| This validates our hypothesis that explicit 3D representation enhances spatial understanding for robot learning compared to pure 2D approaches. | comparison identity and matched condition | p. 8 (4.5. Ablation Analysis) |
| Choice of Gaussian Splatting As shown in Table 4, compared to directly building image-based world model with diffusion transformer on par with [1], introducing ... | comparison identity and matched condition | p. 8 (4.5. Ablation Analysis) |
| Figure 3. Qualitative comparison between models on META- WORLD. GWM successfully predicts better details on the gripper movement (highlighted in blue). the future prediction ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 4. Ablation Study on PnP CabToCounter in ROBO- CASA task suite. We report the reconstruction metrics and the suc- cess rates (SR) of ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Figure 6. Real-World Experiment Setup. Left: using a Franka Emika Panda robotic arm equipped with an RGB camera, we eval- uate the performance of ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our main contributions are threefold. • We introduce GWM, a novel 3D world model that is instantiated with a Gaussian diffusion transformer ... | Choice of Gaussian Splatting As shown in Table 4, compared to directly building image-based world model with diffusion transformer on par with [1], introducing ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.5. Ablation Analysis), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (4.5. Ablation Analysis), p. 5 (4. Experiments), p. 6 (Figure/Table caption) |
| Primary metric/result | Table 2. Multi-Task Imitation Learning Results in Robocasa. Average success rates (%) of multi-task agents trained with 50 human demonstrations or 3000 generated demonstrations ... | numeric claim only at cited anchor | p. 7 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 7 / 4.3. GWM-based Reinforcement Learning - extractive body cue:** Results are evaluated over 50 episodes with different floor plans and styles.
- **p. 7 / 4.3. GWM-based Reinforcement Learning - extractive body cue:** Each data point is evaluated over 20 episodes. trained initialization of both methods.
- **p. 7 / 4.3. GWM-based Reinforcement Learning - extractive body cue:** For fair comparisons, all compared methods use the same context length, horizon, and are trained to a maximum of 1 × 105 steps.
- **p. 8 / 4.3. GWM-based Reinforcement Learning - extractive body cue:** We report the number of successful trials out of all 20 trials in FRANKA PNP.
- **p. 8 / 4.4. Real-world Deployment - extractive body cue:** 35% success rate) on 20 trials with different initial start positions and object locations (i.e. distractors).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In this paper, we introduce a novel Gaussian World Model (GWM) for robotic manipulation that addresses limitations of image-based world models by incorporating robust ... | p. 8 (5. Conclusion) |
| body limitation/failure cue | Figure 1. Gaussian World Model (GWM) is a novel branch of world model that predicts dynamic future states and enables robotic manipulation based on ... | p. 1 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Specifically, we encode the realworld vision inputs into latent 3D Gaussian representations (Sec. | p. 3 (3. Gaussian World Model) |
| To obtain the color of each pixel from a given viewpoint, 3D-GS projects the 3D Gaussians onto the image plane and computes the pixel ... | p. 3 (3.1. World State Encoding) |
| The overall pipeline of GWM, which primarily consists of a 3D variational encoder and a latent diffusion transformer. | p. 4 (3.1. World State Encoding) |
| With the encoded world state embeddings xt at time t and its future state xt+1, we aim to learn the world dynamics p(xt+1/x≤t, a≤t), ... | p. 4 (3.2. Diffusion-based Dynamics Modeling) |
| Implementation Technically, we implement the network Fθ with a DiT [60]. | p. 5 (3.2. Diffusion-based Dynamics Modeling) |
| We provide the pseudo-code for the model-based RL policy learning in Algorithm 1. | p. 5 (3.3. GWM for Policy Learning) |
| The shadow area represents 95% confidence interval (CI) across three random seeds. | p. 7 (4.3. GWM-based Reinforcement Learning) |
| For fair comparisons, all compared methods use the same context length, horizon, and are trained to a maximum of 1 × 105 steps. | p. 7 (4.3. GWM-based Reinforcement Learning) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive body cue:** In this paper, we introduce a novel Gaussian World Model (GWM) for robotic manipulation that addresses limitations of image-based world models by incorporating robust geometric ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Gaussian World Model (GWM) is a novel branch of world model that predicts dynamic future states and enables robotic manipulation based on the ...

- **Evidence anchors reviewed:** datasets p. 8 (4.5. Ablation Analysis), p. 8 (4.5. Ablation Analysis), metrics p. 7 (Figure/Table caption), p. 8 (4.5. Ablation Analysis), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 4 (Figure/Table caption), baselines p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 8 (4.5. Ablation Analysis), p. 8 (4.5. Ablation Analysis), p. 6 (Figure/Table caption), results p. 8 (4.5. Ablation Analysis), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (4.5. Ablation Analysis), p. 5 (4. Experiments), p. 6 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
