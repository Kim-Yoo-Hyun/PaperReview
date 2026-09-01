# Evaluation - TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2409.12514; PDF retrieval source: https://arxiv.org/pdf/2409.12514. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 3 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 3 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS)): In our experiments, we aim to study the following questions: • Does TinyVLA achieve a higher success rate in multitasking robotic manipulation compared to the baselines? • Can TinyVLA interpret ...

## Evaluation Body Digest

- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** More Real-World Experiments: Bimanual Robot We further conducted experiments on the Bimanual UR5 Robot, applying it to three distinct tasks: PlaceBread, StackCube, and PlaceTennisBag.
- **p. 3 / IV. EXPERIMENTS - extractive PDF cue:** In our experiments, we aim to study the following questions: • Does TinyVLA achieve a higher success rate in multitasking robotic manipulation compared to the ...
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** We suspect this is because OpenVLA is pre-trained on the OpenX dataset, which consists entirely of single-arm robot data, making it ineffective when applied to ...
- **p. 4 / IV. EXPERIMENTS - extractive PDF cue:** Generalization to Unseen Instructions In this work, we investigate the generalization capabilities of TinyVLA-H, which demonstrates the best performance in both real-world scenarios and simulations.
- **p. 3 / IV. EXPERIMENTS - extractive PDF cue:** 1) Simulation Benchmark: We evaluate our approach on MetaWorld.
- **p. 4 / IV. EXPERIMENTS - extractive PDF cue:** In the bimanual robot experiment, we set up three tasks that involved cooperation between two arms: 1) transferring bread to a plate (TransferBread), 2) unzipping ...
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** 6 IEEE ROBOTICS AND AUTOMATION LETTERS.
- **p. 4 / IV. EXPERIMENTS - extractive PDF cue:** We report the mean and standard deviation of success rates across 3 checkpoints.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 3).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | In our experiments, we aim to study the following questions: • Does TinyVLA achieve a higher success rate in multitasking robotic manipulation compared to ... | p. 3 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table III, while the Diffusion Policy excels in the PlaceTennisBag task, our TinyVLA-H model achieved an average success rate of 44.5%, ... | p. 5 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | It is evaluated with 3 seeds, and for each seed, the success rate was averaged over five different iterations. | p. 3 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | We report the average success rate over 10 trials. | p. 4 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | We report the mean and standard deviation of success rates across 3 checkpoints. | p. 4 (IV. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** More Real-World Experiments: Bimanual Robot We further conducted experiments on the Bimanual UR5 Robot, applying it to three distinct tasks: PlaceBread, StackCube, and PlaceTennisBag.
- **p. 3 / IV. EXPERIMENTS - extractive PDF cue:** In our experiments, we aim to study the following questions: • Does TinyVLA achieve a higher success rate in multitasking robotic manipulation compared to the ...
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** We suspect this is because OpenVLA is pre-trained on the OpenX dataset, which consists entirely of single-arm robot data, making it ineffective when applied to ...
- **p. 4 / IV. EXPERIMENTS - extractive PDF cue:** Generalization to Unseen Instructions In this work, we investigate the generalization capabilities of TinyVLA-H, which demonstrates the best performance in both real-world scenarios and simulations.
- **p. 3 / IV. EXPERIMENTS - extractive PDF cue:** 1) Simulation Benchmark: We evaluate our approach on MetaWorld.
- **p. 4 / IV. EXPERIMENTS - extractive PDF cue:** In the bimanual robot experiment, we set up three tasks that involved cooperation between two arms: 1) transferring bread to a plate (TransferBread), 2) unzipping ...
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** 6 IEEE ROBOTICS AND AUTOMATION LETTERS.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2: Model architecture. The left image illustrates the VLM pretraining pipeline, whereas the right image demon- strates the process of training TinyVLA using robotic ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 3: Real robot settings. The real robot setup for the single- arm Franka and bimanual UR5. TABLE I: Comparing TinyVLA with Diffusion Policy in ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 3. The single-arm scene is perceived via two external ZED 2 stereo cameras fixed on both sides of the robot. The bimanual robot's scene ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 4: Instruction Generalization. We conducted three dif- ferent types of instruction generalization experiments with progressively increasing difficulty. cess rate exceeds that of Diffusion Policy ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 5: View Generalization. We evaluated the view generalization capability of our model in a new environment, which we designed to be as consistent with ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. We test with three objects, a mug, a toy car, and a pink cube. The first level challenges TinyVLA to differentiate between an ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 6: Background Generalization. We utilized six different backgrounds, testing three of them on Task a and the remaining three on Task b. For each ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 7: Distractor & Illumination Generalization. For dis- tractor settings, Level L1 involves the addition of objects such as books and cups, which are unrelated ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | More Real-World Experiments: Bimanual Robot We further conducted experiments on the Bimanual UR5 Robot, applying it to three distinct tasks: PlaceBread, StackCube, and PlaceTennisBag. | embodiment, simulator version and control stack | p. 5 (IV. EXPERIMENTS), p. 3 (IV. EXPERIMENTS) |
| Task/environment | In our experiments, we aim to study the following questions: • Does TinyVLA achieve a higher success rate in multitasking robotic manipulation compared to ... | reset, timeout, object/scene variation | p. 3 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 2 (III. METHOD), p. 3 (III. METHOD) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 3 (III. METHOD), p. 2 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We report the mean and standard deviation of success rates across 3 checkpoints. | definition/direction/unit from same section | p. 4 (IV. EXPERIMENTS) |
| In our experiments, we aim to study the following questions: • Does TinyVLA achieve a higher success rate in multitasking robotic manipulation compared to ... | definition/direction/unit from same section | p. 3 (IV. EXPERIMENTS) |
| We report the average success rate. | definition/direction/unit from same section | p. 3 (IV. EXPERIMENTS) |
| Notably, TinyVLA-H attained a 98.3% success rate in flipping a mug, stacking cubes, and a 90% success rate in place tennis, leading a large ... | definition/direction/unit from same section | p. 4 (IV. EXPERIMENTS) |
| In contrast, TinyVLA demonstrates a certain degree of robustness in handling view generalization. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| We use a cross mark to denote the failure of the model and a checkmark to indicate successful task completion. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In our experiments, we aim to study the following questions: • Does TinyVLA achieve a higher success rate in multitasking robotic manipulation compared to ... | comparison identity and matched condition | p. 3 (IV. EXPERIMENTS) |
| Notably, TinyVLA-H attained a 98.3% success rate in flipping a mug, stacking cubes, and a 90% success rate in place tennis, leading a large ... | comparison identity and matched condition | p. 4 (IV. EXPERIMENTS) |
| Although it occasionally fails, TinyVLA still shows a significantly stronger view generalization compared to Diffusion Policy and OpenVLA, underscoring the benefits of using diffusion-based ... | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| We did a few modifications to ensure the comparison is fair. | comparison identity and matched condition | p. 4 (IV. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| For all the tasks we do not add additional distractors except in the remove the lid of the box task, in order to better ... | component/input/data sensitivity | p. 4 (IV. EXPERIMENTS) |
| Since TinyVLA uses a pre-trained multimodal model as its backbone, we observe similar embodied capabilities driven by the rich world knowledge implicitly stored in ... | component/input/data sensitivity | p. 4 (IV. EXPERIMENTS) |
| Fig. 2: Model architecture. The left image illustrates the VLM pretraining pipeline, whereas the right image demon- strates the process of training TinyVLA using ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |
| Fig. 8: Object & Appearance generalization. For object generalization, we replace the objects with previously unseen ones that have different shapes or colors. For ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contribution are the three folds: • We introduce a novel VLA architecture that combines lightweight vision-language models with a diffusion model, enabling fast ... | In our experiments, we aim to study the following questions: • Does TinyVLA achieve a higher success rate in multitasking robotic manipulation compared to ... | PDF body cue; verify exact table/figure and matched conditions | p. 3 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 3 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Primary metric/result | As shown in Table III, while the Diffusion Policy excels in the PlaceTennisBag task, our TinyVLA-H model achieved an average success rate of 44.5%, ... | numeric claim only at cited anchor | p. 5 (IV. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 3 / IV. EXPERIMENTS - extractive PDF cue:** The 50 tasks in MetaWorld [36] can be categorized into multiple levels [37], i.e., easy, medium, hard, and very hard.
- **p. 3 / IV. EXPERIMENTS - extractive PDF cue:** It is evaluated with 3 seeds, and for each seed, the success rate was averaged over five different iterations.
- **p. 4 / IV. EXPERIMENTS - extractive PDF cue:** Pre-trained Total Trainable RealWorld(5 tasks) Model \ Tasks Trajectory Params Params PlaceTennis FlipMug StackCubes CloseDrawer OpenBox Avg.
- **p. 4 / IV. EXPERIMENTS - extractive PDF cue:** Diffusion Policy [3] N/A 111M 111M 16.7±0.6 30±0.2 3.3±0.1 73.3±0.1 53.3±0.1 35.3 Multimodal Diffusion [38] N/A 230M 230M 23.3±0.3 13.3±1.3 6.7±0.3 36.7±0.3 10.0±0 18.0 OpenVLA ...
- **p. 4 / IV. EXPERIMENTS - extractive PDF cue:** In total, we collected 100 trajectories for each task to balance data distribution across all 5 tasks.
- **p. 4 / IV. EXPERIMENTS - extractive PDF cue:** We report the average success rate over 10 trials.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Our approach overcomes the limitations of previous methods by | p. 7 (VI. CONCLUSION) |
| body limitation/failure cue | We use a cross mark to denote the failure of the model and a checkmark to indicate successful task completion. | p. 5 (IV. EXPERIMENTS) |
| body limitation/failure cue | Fig. 10: Types of failure for TinyVLA with different sizes of pre-trained vision-language models. | p. 7 (Figure/Table caption) |
| body limitation/failure cue | Notably, the OpenVLA fails in every trial. | p. 5 (IV. EXPERIMENTS) |
| body limitation/failure cue | Secondly, the vanilla DP does not incorporate language instructions. | p. 4 (IV. EXPERIMENTS) |
| body limitation/failure cue | In our experiments, we aim to study the following questions: • Does TinyVLA achieve a higher success rate in multitasking robotic manipulation compared to ... | p. 3 (IV. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| It is evaluated with 3 seeds, and for each seed, the success rate was averaged over five different iterations. | p. 3 (IV. EXPERIMENTS) |
| We report the average success rate over 10 trials. | p. 4 (IV. EXPERIMENTS) |
| We evaluate each model 20 trials per task in single arm setting. | p. 4 (IV. EXPERIMENTS) |
| Notably, the OpenVLA fails in every trial. | p. 5 (IV. EXPERIMENTS) |
| For all experiments on generalization, we conduct one trial for each setting. | p. 5 (IV. EXPERIMENTS) |
| TinyVLA encompasses several crucial designs: 1) We adopt a pre-trained VLM as the initialization of a policy network; 2) During training the robot data, ... | p. 2 (III. METHOD) |
| And the pipeline can be splited into 3 steps. | p. 3 (III. METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / VI. CONCLUSION - extractive PDF cue:** Our approach overcomes the limitations of previous methods by
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** We use a cross mark to denote the failure of the model and a checkmark to indicate successful task completion.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 10: Types of failure for TinyVLA with different sizes of pre-trained vision-language models.
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** Notably, the OpenVLA fails in every trial.
- **p. 4 / IV. EXPERIMENTS - extractive PDF cue:** Secondly, the vanilla DP does not incorporate language instructions.
- **p. 3 / IV. EXPERIMENTS - extractive PDF cue:** In our experiments, we aim to study the following questions: • Does TinyVLA achieve a higher success rate in multitasking robotic manipulation compared to the ...

- **PDF anchors reviewed:** datasets p. 5 (IV. EXPERIMENTS), p. 3 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 3 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), metrics p. 4 (IV. EXPERIMENTS), p. 3 (IV. EXPERIMENTS), p. 3 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), baselines p. 3 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), results p. 3 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 3 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
