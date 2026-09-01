# Evaluation - MimicPlay: Long-Horizon Imitation Learning by Watching Human Play

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2302.12422; PDF retrieval source: https://arxiv.org/pdf/2302.12422. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5 Results), p. 7 (5 Results), p. 1 (Figure/Table caption), p. 15 (C Supplementary Experiment Results), p. 17 (C Supplementary Experiment Results), p. 15 (Figure/Table caption)): 2, although Ours (w/o KL) baseline outperforms most baselines in trained tasks, its success rate is 17% lower than Ours.

## Evaluation Body Digest

- **p. 15 / C Supplementary Experiment Results - extractive PDF cue:** To extensively evaluate the methods with more testing trials and training seeds, we conduct an experiment in simulation LIBERO [60], which is a multitask robot ...
- **p. 15 / C Supplementary Experiment Results - extractive PDF cue:** However, in simulation, there is no way to get such dataset, which will always end up being robot teleoperation.
- **p. 17 / C Supplementary Experiment Results - extractive PDF cue:** Each sequence of robot demonstration has a pre-defined task goal.
- **p. 16 / C Supplementary Experiment Results - extractive PDF cue:** For instance, in the training data, the robot only learns to open the box after turning off the lamp, meanwhile in the Easy setting of ...
- **p. 17 / C Supplementary Experiment Results - extractive PDF cue:** (b) Robot demonstration data collection.
- **p. 7 / 5 Results - extractive PDF cue:** We hypothesize this is due to the reason that the length of the demonstration for the whiteboard task is shorter than the other tasks, which ...
- **p. 7 / 5 Results - extractive PDF cue:** Although being trained with full human play data, Task-2 Task-3 Medium ALL 0.0 0.2 0.4 0.6 0.8 Success rate (%) Ours (human prompt) Ours (robot ...
- **p. 16 / C Supplementary Experiment Results - extractive PDF cue:** (a) Distribution overlap of Ours (w/o KL) (b) Distribution overlap of Ours Figure 7: t-SNE visualization of the generated feature embeddings by taking human data ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** demonstration으로 정의된 robot task distribution.
- **Input boundary:** observation history와 expert trajectory/action.
- **Output/decision under evaluation:** predicted action 또는 action chunk.
- **Primary target:** imitation error, task success, robustness와 compounding error.
- **Detected evaluation headings:** 5 Results (p. 7); A Implementation details (p. 14); B Experiment setups (p. 14); C Supplementary Experiment Results (p. 15).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5 Results | EMPIRICAL / SIMULATION | 2, although Ours (w/o KL) baseline outperforms most baselines in trained tasks, its success rate is 17% lower than Ours. | p. 7 (5 Results) |
| 5 Results | EMPIRICAL / SIMULATION | A 10-minute of cheap and unlabelled human play data brings large improvements in the task success rate and sample efficiency. | p. 7 (5 Results) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Figure 1: Human is able to complete a long-horizon task much faster than a teleoperated robot. This observation inspires us to develop MIMICPLAY, a ... | p. 1 (Figure/Table caption) |
| C Supplementary Experiment Results | EMPIRICAL / SIMULATION | For each method, we train with 5 random seeds and report the average success rate over 100 testing trials. | p. 15 (C Supplementary Experiment Results) |
| C Supplementary Experiment Results | EMPIRICAL / SIMULATION | 2 (Ours (w/o KL) is inferior to Ours in task success rate). | p. 17 (C Supplementary Experiment Results) |

## Dataset / Benchmark Role

- **p. 15 / C Supplementary Experiment Results - extractive PDF cue:** To extensively evaluate the methods with more testing trials and training seeds, we conduct an experiment in simulation LIBERO [60], which is a multitask robot ...
- **p. 15 / C Supplementary Experiment Results - extractive PDF cue:** However, in simulation, there is no way to get such dataset, which will always end up being robot teleoperation.
- **p. 17 / C Supplementary Experiment Results - extractive PDF cue:** Each sequence of robot demonstration has a pre-defined task goal.
- **p. 16 / C Supplementary Experiment Results - extractive PDF cue:** For instance, in the training data, the robot only learns to open the box after turning off the lamp, meanwhile in the Easy setting of ...
- **p. 17 / C Supplementary Experiment Results - extractive PDF cue:** (b) Robot demonstration data collection.
- **p. 7 / 5 Results - extractive PDF cue:** We hypothesize this is due to the reason that the length of the demonstration for the whiteboard task is shorter than the other tasks, which ...
- **p. 7 / 5 Results - extractive PDF cue:** Although being trained with full human play data, Task-2 Task-3 Medium ALL 0.0 0.2 0.4 0.6 0.8 Success rate (%) Ours (human prompt) Ours (robot ...
- **p. 16 / C Supplementary Experiment Results - extractive PDF cue:** (a) Distribution overlap of Ours (w/o KL) (b) Distribution overlap of Ours Figure 7: t-SNE visualization of the generated feature embeddings by taking human data ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: Human is able to complete a long-horizon task much faster than a teleoperated robot. This observation inspires us to develop MIMICPLAY, a hierarchical ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Overview of MIMICPLAY. (a) Training Stage 1: using cheap human play data to train a goal-conditioned trajectory generation model to build a latent ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: Evaluation Tasks. We design six environments with long-horizon tasks for a Franka Emika robot arm, with initial (left) and goal (right) states shown ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1: Quantitative evaluation results in the Kitchen environment. to the decreased dimensionality. In the following, we introduce how to generate the latent plan pt ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2: Ablation evaluation results in the Study Desk environment (20 demos). Spatial generalization Extreme long horizon Deformable Flower Whiteboard Sandwich
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3: Quantitative evaluation results of multi-task learning. Baselines. We evaluate five methods: 1) GC-BC (BC-RNN) and 2) GC-BC (BC-trans), goal-conditioned BC variants of [20] ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4: Evaluation of multi-task policy prompted with robot/human videos in the Study Desk environment. Ours (w/o GMM) even fails to match the performance of ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5: Qualitative visualization of the latent plans before the disturbance and re-planning. Column 1: third- person view. Column 2: visualization of the latent plan ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To extensively evaluate the methods with more testing trials and training seeds, we conduct an experiment in simulation LIBERO [60], which is a multitask ... | embodiment, simulator version and control stack | p. 15 (C Supplementary Experiment Results), p. 15 (C Supplementary Experiment Results) |
| Task/environment | However, in simulation, there is no way to get such dataset, which will always end up being robot teleoperation. | reset, timeout, object/scene variation | p. 15 (C Supplementary Experiment Results), p. 17 (C Supplementary Experiment Results) |
| Observation/sensor | observation history와 expert trajectory/action | calibration, preprocessing, privileged input | p. 14 (A Implementation details), p. 2 (1 Introduction) |
| Output/decision | predicted action 또는 action chunk | action frame, controller and termination | p. 14 (A Implementation details), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| However, we do observe an uneven performance drop with our method (the success rate of the whiteboard task drops from 0.5 to 0.2). | definition/direction/unit from same section | p. 7 (5 Results) |
| 2, although Ours (w/o KL) baseline outperforms most baselines in trained tasks, its success rate is 17% lower than Ours. | definition/direction/unit from same section | p. 7 (5 Results) |
| For each method, we train with 5 random seeds and report the average success rate over 100 testing trials. | definition/direction/unit from same section | p. 15 (C Supplementary Experiment Results) |
| 2 (Ours (w/o KL) is inferior to Ours in task success rate). | definition/direction/unit from same section | p. 17 (C Supplementary Experiment Results) |
| Table 4: Quantitative evaluation results in simulation (success rates % averaged over 5 seeds) compositional generalization ability of the models to novel task goal ... | definition/direction/unit from same section | p. 15 (Figure/Table caption) |
| Since our whole system (including the vision-based latent planner, low-level guided policy, and robot control) is running at a speed of 17Hz, our model ... | definition/direction/unit from same section | p. 8 (5 Results) |
| Figure 1: Human is able to complete a long-horizon task much faster than a teleoperated robot. This observation inspires us to develop MIMICPLAY, a ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| KL) fails to match the performance of Ours (50% human). | definition/direction/unit from same section | p. 8 (5 Results) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 2, although Ours (w/o KL) baseline outperforms most baselines in trained tasks, its success rate is 17% lower than Ours. | comparison identity and matched condition | p. 7 (5 Results) |
| For a fair comparison with our method, the baseline approaches trained without human play data have five more demonstrations during training the latent planner ... | comparison identity and matched condition | p. 14 (A Implementation details) |
| 2, our full with GMM model largely outperforms Ours (w/o GMM). | comparison identity and matched condition | p. 7 (5 Results) |
| 2 unseen tasks, Ours surpasses all baselines by more than 35%. | comparison identity and matched condition | p. 8 (5 Results) |
| With this hierarchical design, MIMICPLAY outperforms prior arts by over 50% in 14 challenging long-horizon manipulation tasks. | comparison identity and matched condition | p. 8 (5 Results) |
| The results showcase the advantage of MIMICPLAY's hierarchical policy learning framework over the baselines, which is consistent with the real-world results (Tab. | comparison identity and matched condition | p. 15 (C Supplementary Experiment Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 8: System setups for the data collection. (a) Human play data collection. A human operator directly interacts with the scene with one of ... | component/input/data sensitivity | p. 17 (Figure/Table caption) |
| (a) Feature visualization results of our method without using KL divergence loss. | component/input/data sensitivity | p. 16 (C Supplementary Experiment Results) |
| Ours (0% human) variant still outputs a latent plan to open the box, which causes the task to fail since the box is already ... | component/input/data sensitivity | p. 16 (C Supplementary Experiment Results) |
| 7, we use t-SNE to process and visualize the learned feature embeddings generated by Ours and the model variant Ours (w/o KL) on the ... | component/input/data sensitivity | p. 17 (C Supplementary Experiment Results) |
| Table 2: Ablation evaluation results in the Study Desk environment (20 demos). Spatial generalization Extreme long horizon Deformable Flower Whiteboard Sandwich | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| We visualize the trajectories generated by all of the model variants in the Appendix, where we found Ours (w/o GMM) has the worst quality ... | component/input/data sensitivity | p. 7 (5 Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To summarize, the main contributions of our work are as follows: • A novel paradigm for learning 3D-aware latent plans from cheap human play ... | 2, although Ours (w/o KL) baseline outperforms most baselines in trained tasks, its success rate is 17% lower than Ours. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5 Results), p. 7 (5 Results), p. 1 (Figure/Table caption), p. 15 (C Supplementary Experiment Results), p. 17 (C Supplementary Experiment Results), p. 15 (Figure/Table caption) |
| Primary metric/result | A 10-minute of cheap and unlabelled human play data brings large improvements in the task success rate and sample efficiency. | numeric claim only at cited anchor | p. 7 (5 Results) |

- Numeric sentences retained from the body:
- **p. 7 / 5 Results - extractive PDF cue:** Although being trained with full human play data, Task-2 Task-3 Medium ALL 0.0 0.2 0.4 0.6 0.8 Success rate (%) Ours (human prompt) Ours (robot ...
- **p. 8 / 5 Results - extractive PDF cue:** Since our whole system (including the vision-based latent planner, low-level guided policy, and robot control) is running at a speed of 17Hz, our model is ...
- **p. 14 / A Implementation details - extractive PDF cue:** The entire trajectory τ is recorded at the speed of 60 frames per second and is used without cutting or labeling.
- **p. 14 / A Implementation details - extractive PDF cue:** We train 100k iterations for the latent planner which takes a single GPU machine for 12 hours.
- **p. 14 / A Implementation details - extractive PDF cue:** The control frequency of the robot arm is 17-20Hz and the gripper is controlled at 2Hz.
- **p. 14 / A Implementation details - extractive PDF cue:** We train 100k iterations for the policy with a single GPU machine in 12 hours.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Ours (w/o GMM) even fails to match the performance of Ours (0% human) in the generalization task settings. | p. 7 (5 Results) |
| body limitation/failure cue | 6 Conclusion and Limitations Existing limitations of the MIMICPLAY include: 1) The current high-level latent plan is learned from scene-specific human play data. | p. 8 (5 Results) |
| body limitation/failure cue | 2, we compared the model variants with 50% human play data (Ours (50% human)) and found it fails to match the performance of Ours, ... | p. 8 (5 Results) |
| body limitation/failure cue | This result showcases that learning a latent plan space does not need to rely fully on teleoperated robot demonstration data. | p. 7 (5 Results) |
| body limitation/failure cue | Figure 1: Human is able to complete a long-horizon task much faster than a teleoperated robot. This observation inspires us to develop MIMICPLAY, a ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Ours (0% human) variant still outputs a latent plan to open the box, which causes the task to fail since the box is already ... | p. 16 (C Supplementary Experiment Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For each method, we train with 5 random seeds and report the average success rate over 100 testing trials. | p. 15 (C Supplementary Experiment Results) |
| To extensively evaluate the methods with more testing trials and training seeds, we conduct an experiment in simulation LIBERO [60], which is a multitask ... | p. 15 (C Supplementary Experiment Results) |
| We train 100k iterations for the policy with a single GPU machine in 12 hours. | p. 14 (A Implementation details) |
| 2(b)), we specify the goal image gr t (gr t ∈Vr) as the frame H steps after the input observation or t in the ... | p. 14 (A Implementation details) |
| (a) Visualization of the trajectory prediction results decoded from the latent plans learned by different methods. | p. 16 (C Supplementary Experiment Results) |
| 3.2, to minimize the visual gap between human play data and robot demonstration data, we use a KL divergence loss over the feature embeddings ... | p. 17 (C Supplementary Experiment Results) |
| We also list the hyperparameters for the baseline GC-BC (BC-trans) in Tab. | p. 19 (C Supplementary Experiment Results) |
| F Training hyperparameters We list the hyperparameters for training the models in Tab. | p. 19 (C Supplementary Experiment Results) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 5 Results - extractive PDF cue:** Ours (w/o GMM) even fails to match the performance of Ours (0% human) in the generalization task settings.
- **p. 8 / 5 Results - extractive PDF cue:** 6 Conclusion and Limitations Existing limitations of the MIMICPLAY include: 1) The current high-level latent plan is learned from scene-specific human play data.
- **p. 8 / 5 Results - extractive PDF cue:** 2, we compared the model variants with 50% human play data (Ours (50% human)) and found it fails to match the performance of Ours, which ...
- **p. 7 / 5 Results - extractive PDF cue:** This result showcases that learning a latent plan space does not need to rely fully on teleoperated robot demonstration data.
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: Human is able to complete a long-horizon task much faster than a teleoperated robot. This observation inspires us to develop MIMICPLAY, a hierarchical ...
- **p. 16 / C Supplementary Experiment Results - extractive PDF cue:** Ours (0% human) variant still outputs a latent plan to open the box, which causes the task to fail since the box is already open.

- **PDF anchors reviewed:** datasets p. 15 (C Supplementary Experiment Results), p. 15 (C Supplementary Experiment Results), p. 17 (C Supplementary Experiment Results), p. 16 (C Supplementary Experiment Results), p. 17 (C Supplementary Experiment Results), p. 7 (5 Results), metrics p. 7 (5 Results), p. 7 (5 Results), p. 15 (C Supplementary Experiment Results), p. 17 (C Supplementary Experiment Results), p. 15 (Figure/Table caption), p. 8 (5 Results), baselines p. 7 (5 Results), p. 14 (A Implementation details), p. 7 (5 Results), p. 8 (5 Results), p. 8 (5 Results), p. 15 (C Supplementary Experiment Results), results p. 7 (5 Results), p. 7 (5 Results), p. 1 (Figure/Table caption), p. 15 (C Supplementary Experiment Results), p. 17 (C Supplementary Experiment Results), p. 15 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
