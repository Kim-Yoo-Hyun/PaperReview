# Evaluation - VoxAct-B: Voxel-Based Acting and Stabilizing Policy for Bimanual Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v270/liu25i.html; PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v270/main/assets/liu25i/liu25i.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 16 (C Additional Implementation Details for the Baselines), p. 6 (5 Experiments), p. 7 (6 Results), p. 17 (Figure/Table caption), p. 7 (6 Results), p. 16 (C Additional Implementation Details for the Baselines)): We found the Time-series Diffusion Transformer to outperform the CNN-based Diffusion Policy on Open Drawer and Open Jar, while both of them achieved comparable success rates on Put Item in ...

## Evaluation Body Digest

- **p. 6 / 5 Experiments - extractive body cue:** For simulation experiments, we build on top of RLBench [14], a popular robot manipulation benchmark widely used in prior work, including VoxPoser and PerAct.
- **p. 6 / 5 Experiments - extractive body cue:** 5.2 Experiment Protocol and Evaluation To generate demonstrations in simulation, we follow the convention from RLBench and define a sequence of waypoints to complete the ...
- **p. 7 / 5 Experiments - extractive body cue:** We generate 25 episodes of validation and test data using different random seeds.
- **p. 14 / A.1 Additional Implementation Details - extractive body cue:** If it is closer to the left robot arm, ℓas is selected because it provides the right arm with a better angle for grasping the ...
- **p. 7 / 6 Results - extractive body cue:** We use five training seeds for all methods, and evaluate on the same 25 episodes of unseen test data using the best checkpoints from validation ...
- **p. 14 / A.1 Additional Implementation Details - extractive body cue:** In Open Jar, we use the jar's pose to determine which robot arm it is closer to.
- **p. 8 / 6 Results - extractive body cue:** 6.2 Physical Results Figure 4 shows real-world examples of VoxAct-B.
- **p. 8 / 6 Results - extractive body cue:** It succeeds in 5 out of 10 trials, demonstrating its ability to learn from multi-modal, real-world data.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 5 Experiments (p. 6); 6 Results (p. 7); A Simulation Benchmark for Bimanual Manipulation (p. 14); A.1 Additional Implementation Details (p. 14); A.3 Multi-Task Experiment (p. 15); B Real-World Experimental Details (p. 16); C Additional Implementation Details for the Baselines (p. 16).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| C Additional Implementation Details for the Baselines | EMPIRICAL / REAL-ROBOT OR HARDWARE | We found the Time-series Diffusion Transformer to outperform the CNN-based Diffusion Policy on Open Drawer and Open Jar, while both of them achieved comparable ... | p. 16 (C Additional Implementation Details for the Baselines) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | We adapt the Mobile ALOHA repository for ACT and a CNN-based Diffusion Policy, and we tune their parameters (e.g., chunk size and action horizon) ... | p. 6 (5 Experiments) |
| 6 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Through ablations of ACT and Diffusion Policy, we found that removing environment variations greatly improved their performance. | p. 7 (6 Results) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 5: Ablation results of ACT and Diffusion Policy trained on 100 demonstrations and evaluated across five training seeds. "FAS" refers to the demonstrations ... | p. 17 (Figure/Table caption) |
| 6 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | When we train all methods using more demonstrations (100), VoxAct-B still outperforms all baselines. | p. 7 (6 Results) |

## Dataset / Benchmark Role

- **p. 6 / 5 Experiments - extractive body cue:** For simulation experiments, we build on top of RLBench [14], a popular robot manipulation benchmark widely used in prior work, including VoxPoser and PerAct.
- **p. 6 / 5 Experiments - extractive body cue:** 5.2 Experiment Protocol and Evaluation To generate demonstrations in simulation, we follow the convention from RLBench and define a sequence of waypoints to complete the ...
- **p. 7 / 5 Experiments - extractive body cue:** We generate 25 episodes of validation and test data using different random seeds.
- **p. 14 / A.1 Additional Implementation Details - extractive body cue:** If it is closer to the left robot arm, ℓas is selected because it provides the right arm with a better angle for grasping the ...
- **p. 7 / 6 Results - extractive body cue:** We use five training seeds for all methods, and evaluate on the same 25 episodes of unseen test data using the best checkpoints from validation ...
- **p. 14 / A.1 Additional Implementation Details - extractive body cue:** In Open Jar, we use the jar's pose to determine which robot arm it is closer to.
- **p. 8 / 6 Results - extractive body cue:** 6.2 Physical Results Figure 4 shows real-world examples of VoxAct-B.
- **p. 8 / 6 Results - extractive body cue:** It succeeds in 5 out of 10 trials, demonstrating its ability to learn from multi-modal, real-world data.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: VoxAct-B uses voxel representations and language to perform bimanual manipulation with 6-DoF manipulation from both arms. We test four language-conditioned bimanual tasks in ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Overview of VoxAct-B. Given RGB-D images and a language goal, we input an RGB image from the front camera and a text query ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Top: VLMs usage as part of VoxAct-B, visualizing the Open Jar task in simulation, showing the role of OWL-ViT and Segment Anything. The ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Performance of different methods on bimanual manipulation tasks in simulation, based on 10 or 100 (task-specific) training demonstrations. We use five training seeds ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Ablation experiment results in simulation. Qualitatively, baseline methods, especially Vox- Poser, typically struggle with precisely grasping objects such as drawer handles and jars. ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Example successful rollouts (one per row) of VoxAct-B on a real-world bimanual setup with UR5s. Ablation experiments. Table 2 reports results on Open ...
- **p. 15 / Figure/Table caption - extractive body cue:** Table 3: Multi-task results of ACT and VoxAct-B trained on 10 demonstrations of each task and evalu- ated across three training seeds. We train a ...
- **p. 17 / Figure/Table caption - extractive body cue:** Table 4: Combined hyperparameters of ACT and Diffusion Policy. A dash ("-") indicates the absence of a hyperparameter for a given method. Open Open Put ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For simulation experiments, we build on top of RLBench [14], a popular robot manipulation benchmark widely used in prior work, including VoxPoser and PerAct. | embodiment, simulator version and control stack | p. 6 (5 Experiments), p. 6 (5 Experiments) |
| Task/environment | 5.2 Experiment Protocol and Evaluation To generate demonstrations in simulation, we follow the convention from RLBench and define a sequence of waypoints to complete ... | reset, timeout, object/scene variation | p. 6 (5 Experiments), p. 7 (5 Experiments) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 4 (4 Method), p. 1 (1 Introduction) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 2 (1 Introduction), p. 4 (4 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Then, we use the bestperforming acting and stabilizing checkpoints to obtain the test success rate. | definition/direction/unit from same section | p. 14 (A.1 Additional Implementation Details) |
| We found the Time-series Diffusion Transformer to outperform the CNN-based Diffusion Policy on Open Drawer and Open Jar, while both of them achieved comparable ... | definition/direction/unit from same section | p. 16 (C Additional Implementation Details for the Baselines) |
| In contrast, we observe fewer of these errors with VoxAct-B. | definition/direction/unit from same section | p. 7 (6 Results) |
| In addition to common errors described in Section 6.1, for Put Item in Drawer, VoxAct-B tends to struggle more with executing acting actions (e.g., ... | definition/direction/unit from same section | p. 8 (6 Results) |
| VoxAct-B succeeds in 6 out of 10 trials; the failures include robot joints hitting their limits, imprecision in grasping the handle, and collisions with ... | definition/direction/unit from same section | p. 8 (6 Results) |
| Otherwise, it is the same as VoxAct-B. • VoxAct-B w/o arm ID: disables the arm ID loss function. | definition/direction/unit from same section | p. 6 (5 Experiments) |
| We adapt the Mobile ALOHA repository for ACT and a CNN-based Diffusion Policy, and we tune their parameters (e.g., chunk size and action horizon) ... | definition/direction/unit from same section | p. 6 (5 Experiments) |
| We generate 10 and 100 demonstrations of training data. | definition/direction/unit from same section | p. 7 (5 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| When we train all methods using more demonstrations (100), VoxAct-B still outperforms all baselines. | comparison identity and matched condition | p. 7 (6 Results) |
| 5.1 Baselines and Ablations In simulation, we compare against several strong baseline methods: Action Chunking with Transformers (ACT) [3], Diffusion Policy [15], and VoxPoser ... | comparison identity and matched condition | p. 6 (5 Experiments) |
| Table 5: Ablation results of ACT and Diffusion Policy trained on 100 demonstrations and evaluated across five training seeds. "FAS" refers to the demonstrations ... | comparison identity and matched condition | p. 17 (Figure/Table caption) |
| ACT is a state-of-the-art method for bimanual manipulation. | comparison identity and matched condition | p. 6 (5 Experiments) |
| The baselines also struggle with correctly assigning the roles of each arm. | comparison identity and matched condition | p. 7 (6 Results) |
| Moreover, VoxAct-B w/o acting and stabilizing and VoxAct-B w/o arm ID perform worse than VoxAct-B, and they struggle with the same issues as the ... | comparison identity and matched condition | p. 8 (6 Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 5: Ablation results of ACT and Diffusion Policy trained on 100 demonstrations and evaluated across five training seeds. "FAS" refers to the demonstrations ... | component/input/data sensitivity | p. 17 (Figure/Table caption) |
| Figure 4: Example successful rollouts (one per row) of VoxAct-B on a real-world bimanual setup with UR5s. Ablation experiments. Table 2 reports results on ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Note that the real-world jar and drawer cannot be opened without the use of a second arm. | component/input/data sensitivity | p. 6 (5 Experiments) |
| We also test the following ablations of VoxAct-B: • VoxAct-B w/o VLMs: does not use the VLMs to detect the object of interest and ... | component/input/data sensitivity | p. 6 (5 Experiments) |
| Through ablations of ACT and Diffusion Policy, we found that removing environment variations greatly improved their performance. | component/input/data sensitivity | p. 7 (6 Results) |
| Open Method Drawer VoxAct-B w/o VLMs 19.2 VoxAct-B w/o Segment Anything 67.2 VoxAct-B w/o acting and stabilizing 64.8 VoxAct-B w/o arm ID 68.0 VoxAct-B ... | component/input/data sensitivity | p. 7 (6 Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To this end, we propose VoxAct-B, a novel voxel-based, language-conditioned method for bimanual manipulation. | We found the Time-series Diffusion Transformer to outperform the CNN-based Diffusion Policy on Open Drawer and Open Jar, while both of them achieved comparable ... | PDF body cue; verify exact table/figure and matched conditions | p. 16 (C Additional Implementation Details for the Baselines), p. 6 (5 Experiments), p. 7 (6 Results), p. 17 (Figure/Table caption), p. 7 (6 Results), p. 16 (C Additional Implementation Details for the Baselines) |
| Primary metric/result | We adapt the Mobile ALOHA repository for ACT and a CNN-based Diffusion Policy, and we tune their parameters (e.g., chunk size and action horizon) ... | numeric claim only at cited anchor | p. 6 (5 Experiments) |

- Numeric sentences retained from the body:
- **p. 6 / 5 Experiments - extractive body cue:** We design the following four bimanual tasks: • Open Jar: a jar with a screw-on lid is randomly spawned and scaled from 90% to 100% ...
- **p. 6 / 5 Experiments - extractive body cue:** The robot must grasp the jar with one hand and use the other to unscrew the lid in an anti-clockwise direction until it is removed. ...
- **p. 6 / 5 Experiments - extractive body cue:** The robot needs to stabilize the top of the drawer with one hand and then open the bottom drawer with the other. • Put Item ...
- **p. 6 / 5 Experiments - extractive body cue:** The robot needs to open the top drawer with one hand, grasp the item placed on top of the drawer with the other hand, and ...
- **p. 6 / 5 Experiments - extractive body cue:** In the real world, we test Open Jar and Open Drawer using a coffee jar with dimensions 3.35×2.85×4.8 inches and a drawer of dimensions 12×12×12 ...
- **p. 7 / 5 Experiments - extractive body cue:** We generate 25 episodes of validation and test data using different random seeds.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 6.3 Limitations and Failure Cases VoxAct-B implicitly assumes the object of interest does not encompass most of the workspace. | p. 8 (6 Results) |
| body limitation/failure cue | VoxAct-B succeeds in 6 out of 10 trials; the failures include robot joints hitting their limits, imprecision in grasping the handle, and collisions with ... | p. 8 (6 Results) |
| body limitation/failure cue | Figure 2: Overview of VoxAct-B. Given RGB-D images and a language goal, we input an RGB image from the front camera and a text ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | Figure 3: Top: VLMs usage as part of VoxAct-B, visualizing the Open Jar task in simulation, showing the role of OWL-ViT and Segment Anything. ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | Note that the real-world jar and drawer cannot be opened without the use of a second arm. | p. 6 (5 Experiments) |
| body limitation/failure cue | We also test the following ablations of VoxAct-B: • VoxAct-B w/o VLMs: does not use the VLMs to detect the object of interest and ... | p. 6 (5 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Hyperparameter ACT Value Diffusion Policy Value learning rate 3e-5 1e-4 weight decay (for transformer only) - 1e-3 # encoder layers 4 - # decoder ... | p. 17 (C Additional Implementation Details for the Baselines) |
| Note that the batch size is not optimized based on GPU memory capacity. | p. 14 (A.1 Additional Implementation Details) |
| The policy is trained with a batch size of 1 on an Nvidia 3080 GPU for two days. | p. 14 (A.1 Additional Implementation Details) |
| We use a batch size of 32 for both methods, and the observation resolution is 128×128 16 | p. 16 (C Additional Implementation Details for the Baselines) |
| It uses the same number of voxels as our method and the default workspace dimensions. • VoxAct-B w/o Segment Anything: uses the bounding box ... | p. 6 (5 Experiments) |
| See Appendix A.1 for details on how checkpoint selection is done in VoxAct-B. | p. 7 (5 Experiments) |
| We generate 25 episodes of validation and test data using different random seeds. | p. 7 (5 Experiments) |
| We carefully tune the baselines and include the hyperparameters used in Table 4. | p. 16 (C Additional Implementation Details for the Baselines) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 6 Results - extractive body cue:** 6.3 Limitations and Failure Cases VoxAct-B implicitly assumes the object of interest does not encompass most of the workspace.
- **p. 8 / 6 Results - extractive body cue:** VoxAct-B succeeds in 6 out of 10 trials; the failures include robot joints hitting their limits, imprecision in grasping the handle, and collisions with the ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Overview of VoxAct-B. Given RGB-D images and a language goal, we input an RGB image from the front camera and a text query ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Top: VLMs usage as part of VoxAct-B, visualizing the Open Jar task in simulation, showing the role of OWL-ViT and Segment Anything. The ...
- **p. 6 / 5 Experiments - extractive body cue:** Note that the real-world jar and drawer cannot be opened without the use of a second arm.
- **p. 6 / 5 Experiments - extractive body cue:** We also test the following ablations of VoxAct-B: • VoxAct-B w/o VLMs: does not use the VLMs to detect the object of interest and crop ...

- **PDF anchors reviewed:** datasets p. 6 (5 Experiments), p. 6 (5 Experiments), p. 7 (5 Experiments), p. 14 (A.1 Additional Implementation Details), p. 7 (6 Results), p. 14 (A.1 Additional Implementation Details), metrics p. 14 (A.1 Additional Implementation Details), p. 16 (C Additional Implementation Details for the Baselines), p. 7 (6 Results), p. 8 (6 Results), p. 8 (6 Results), p. 6 (5 Experiments), baselines p. 7 (6 Results), p. 6 (5 Experiments), p. 17 (Figure/Table caption), p. 6 (5 Experiments), p. 7 (6 Results), p. 8 (6 Results), results p. 16 (C Additional Implementation Details for the Baselines), p. 6 (5 Experiments), p. 7 (6 Results), p. 17 (Figure/Table caption), p. 7 (6 Results), p. 16 (C Additional Implementation Details for the Baselines).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
