# Evaluation - Unleashing Large-Scale Video Generative Pre-training for Visual Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2024/hash/2c37c5bcef24b9541550261dcd63261b-Abstract-Conference.html; PDF retrieval source: https://proceedings.iclr.cc/paper_files/paper/2024/hash/2c37c5bcef24b9541550261dcd63261b-Abstract-Conference.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4 EXPERIMENT), p. 7 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 9 (Figure/Table caption), p. 15 (A.3 REAL ROBOT EXPERIMENTS), p. 8 (4 EXPERIMENT)): GR-1 significantly outperforms all the comparing baseline methods, achieving a success rate of 77.8% and an average length of 2.00.

## Evaluation Body Digest

- **p. 5 / 4 EXPERIMENT - extractive body cue:** 3) Can GR-1 handle challenging settings including small dataset, generalization to unseen scenes, generalization to unseen objects, and generalization to unseen languages?
- **p. 5 / 4 EXPERIMENT - extractive body cue:** We perform experiments on the challenging CALVIN benchmark (Mees et al., 2022c) and a real robot.
- **p. 6 / 4 EXPERIMENT - extractive body cue:** 4.1 CALVIN BENCHMARK EXPERIMENT CALVIN is a challenging benchmark focusing on learning language-conditioned policy for longhorizon robot manipulation (Fig.
- **p. 8 / 4 EXPERIMENT - extractive body cue:** That is, the categories of the transported objects are unseen in the robot data.
- **p. 8 / 4 EXPERIMENT - extractive body cue:** Besides evaluating in a scene that only contains these three objects as in the training data, we also evaluate in two more unseen scenes with ...
- **p. 7 / 4 EXPERIMENT - extractive body cue:** To study the data efficiency, we train on 10% data of the full training dataset from ABCD→D split.
- **p. 6 / 4 EXPERIMENT - extractive body cue:** The environment contains a Franka Emika Panda robot with a parallel-jaw gripper and a desk with a sliding door, a drawer that can be opened ...
- **p. 7 / 4 EXPERIMENT - extractive body cue:** We also perform experiments on the ABC→D split to evaluate the capability of zero-shot unseen scene generalization.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4 EXPERIMENT (p. 5); A.2 CALVIN BENCHMARK EXPERIMENTS (p. 14); A.3 REAL ROBOT EXPERIMENTS (p. 14); A.6 MORE RESULTS (p. 16).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | GR-1 significantly outperforms all the comparing baseline methods, achieving a success rate of 77.8% and an average length of 2.00. | p. 7 (4 EXPERIMENT) |
| 4 EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | GR-1 substantially improves the performance in terms of success rate and average length. | p. 7 (4 EXPERIMENT) |
| 4 EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | GR-1 achieves a high success rate in the setting of seen objects. | p. 8 (4 EXPERIMENT) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 6: Video Prediction Results. The images in green boxes are ground-truth images; the images in blue boxes are predicted images. results are shown ... | p. 9 (Figure/Table caption) |
| A.3 REAL ROBOT EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | (b) We show the success rates of picking and transporting in real robot experiments. setting of Unseen Instances and the tomato and yellow peach ... | p. 15 (A.3 REAL ROBOT EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 5 / 4 EXPERIMENT - extractive body cue:** 3) Can GR-1 handle challenging settings including small dataset, generalization to unseen scenes, generalization to unseen objects, and generalization to unseen languages?
- **p. 5 / 4 EXPERIMENT - extractive body cue:** We perform experiments on the challenging CALVIN benchmark (Mees et al., 2022c) and a real robot.
- **p. 6 / 4 EXPERIMENT - extractive body cue:** 4.1 CALVIN BENCHMARK EXPERIMENT CALVIN is a challenging benchmark focusing on learning language-conditioned policy for longhorizon robot manipulation (Fig.
- **p. 8 / 4 EXPERIMENT - extractive body cue:** That is, the categories of the transported objects are unseen in the robot data.
- **p. 8 / 4 EXPERIMENT - extractive body cue:** Besides evaluating in a scene that only contains these three objects as in the training data, we also evaluate in two more unseen scenes with ...
- **p. 7 / 4 EXPERIMENT - extractive body cue:** To study the data efficiency, we train on 10% data of the full training dataset from ABCD→D split.
- **p. 6 / 4 EXPERIMENT - extractive body cue:** The environment contains a Franka Emika Panda robot with a parallel-jaw gripper and a desk with a sliding door, a drawer that can be opened ...
- **p. 7 / 4 EXPERIMENT - extractive body cue:** We also perform experiments on the ABC→D split to evaluate the capability of zero-shot unseen scene generalization.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Overview of GR-1. GR-1 is first pre-trained on the task of video prediction with a large- scale video dataset. It is then finetuned ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Encoders and Decoders. (a) Language encoder. (b) Robot state encoder. (c) Image encoder. (d) Image decoder. (e) Action decoder. 4
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: CALVIN Benchmark Results. We show examples of multi-task learning trained on ABCD→D split. 4.1 CALVIN BENCHMARK EXPERIMENT CALVIN is a challenging benchmark focusing ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: The positions of the sliding door, LED, bulb, light switch, and but- ton are different across the four environments. Multi-Task Learning. We first ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Real Robot Experiments. We perform real robot experiments of object transportation and articulated object manipulation.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Real Robot Experiment Results.
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 6: Video Prediction Results. The images in green boxes are ground-truth images; the images in blue boxes are predicted images. results are shown in ...
- **p. 14 / Figure/Table caption - extractive body cue:** Table 3: Training Hyperparameters Hyperparameters Pre-training Finetuning batch size 1024 512 learning rate

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 3) Can GR-1 handle challenging settings including small dataset, generalization to unseen scenes, generalization to unseen objects, and generalization to unseen languages? | embodiment, simulator version and control stack | p. 5 (4 EXPERIMENT), p. 5 (4 EXPERIMENT) |
| Task/environment | We perform experiments on the challenging CALVIN benchmark (Mees et al., 2022c) and a real robot. | reset, timeout, object/scene variation | p. 5 (4 EXPERIMENT), p. 6 (4 EXPERIMENT) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 2 (1 INTRODUCTION), p. 4 (3 METHOD) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 4 (3 METHOD), p. 1 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| GR-1 substantially improves the performance in terms of success rate and average length. | definition/direction/unit from same section | p. 7 (4 EXPERIMENT) |
| HULC, achieves a success rate of 66.8% and an average length of 1.11. | definition/direction/unit from same section | p. 7 (4 EXPERIMENT) |
| GR-1 achieves a high success rate in the setting of seen objects. | definition/direction/unit from same section | p. 8 (4 EXPERIMENT) |
| (b) We show the success rates of picking and transporting in real robot experiments. setting of Unseen Instances and the tomato and yellow peach ... | definition/direction/unit from same section | p. 15 (A.3 REAL ROBOT EXPERIMENTS) |
| Table 7: Task Success Rates. Task GR-1 GR-1 w/o Video GR-1 trained on 10% data Prediction & Pre-training from ABCD→D split rotate blue block ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |
| Note that the CALVIN dataset contains 24 hours of teleoperated undirected play data. | definition/direction/unit from same section | p. 6 (4 EXPERIMENT) |
| RT-1 (Brohan et al., 2022) is a state-of-the-art method that uses convolution layers and transformers to generate actions in an end-to-end manner. | definition/direction/unit from same section | p. 6 (4 EXPERIMENT) |
| Another failure mode of RT-1 is collision with the plate or the desk. | definition/direction/unit from same section | p. 8 (4 EXPERIMENT) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| GR-1 outperforms all the comparing baseline methods. | comparison identity and matched condition | p. 7 (4 EXPERIMENT) |
| RT-1 (Brohan et al., 2022) is a state-of-the-art method that uses convolution layers and transformers to generate actions in an end-to-end manner. | comparison identity and matched condition | p. 6 (4 EXPERIMENT) |
| We compare with four baseline methods: MCIL (Lynch & Sermanet, 2020), RT-1 (Brohan et al., 2022), HULC (Mees et al., 2022b), and a multi-task ... | comparison identity and matched condition | p. 6 (4 EXPERIMENT) |
| Robot data is expensive and sparse compared to vision-language data. | comparison identity and matched condition | p. 7 (4 EXPERIMENT) |
| Ablation studies and more results can be found in the appendix. | comparison identity and matched condition | p. 5 (4 EXPERIMENT) |
| We also perform ablation studies to understand how different modules of GR-1 help visual robot manipulation learning. | comparison identity and matched condition | p. 5 (4 EXPERIMENT) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation studies and more results can be found in the appendix. | component/input/data sensitivity | p. 5 (4 EXPERIMENT) |
| We also perform ablation studies to understand how different modules of GR-1 help visual robot manipulation learning. | component/input/data sensitivity | p. 5 (4 EXPERIMENT) |
| MCIL and HULC are trained on the full CALVIN dataset containing data with and without language annotations. | component/input/data sensitivity | p. 7 (4 EXPERIMENT) |
| And this is very important as it allows GR-1 to quickly learn skills without collecting a large amount of data. | component/input/data sensitivity | p. 7 (4 EXPERIMENT) |
| Figure 1: Overview of GR-1. GR-1 is first pre-trained on the task of video prediction with a large- scale video dataset. It is then ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| Table 4: Ablation Studies. Pre-Training Video Prediction Data Tasks completed in a row 1 2 3 | component/input/data sensitivity | p. 15 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Key contributions of the paper includes: • We show that large-scale video generative pre-training is able to effectively benefit visual robot manipulation learning. • ... | GR-1 significantly outperforms all the comparing baseline methods, achieving a success rate of 77.8% and an average length of 2.00. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4 EXPERIMENT), p. 7 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 9 (Figure/Table caption), p. 15 (A.3 REAL ROBOT EXPERIMENTS), p. 8 (4 EXPERIMENT) |
| Primary metric/result | GR-1 substantially improves the performance in terms of success rate and average length. | numeric claim only at cited anchor | p. 7 (4 EXPERIMENT) |

- Numeric sentences retained from the body:
- **p. 6 / 4 EXPERIMENT - extractive body cue:** It contains 34 tasks and features unconstrained language instructions.
- **p. 6 / 4 EXPERIMENT - extractive body cue:** Note that the CALVIN dataset contains 24 hours of teleoperated undirected play data.
- **p. 7 / 4 EXPERIMENT - extractive body cue:** GR-1 outperforms all the baseline methods on sequentially completing 1, 2, 3, 4, and 5 tasks in a row.
- **p. 7 / 4 EXPERIMENT - extractive body cue:** Specifically, we sample 66 trajectories for each of the 34 tasks, i.e.
- **p. 7 / 4 EXPERIMENT - extractive body cue:** 2244 trajectories, from the total 22,966 training trajectories.
- **p. 7 / 4 EXPERIMENT - extractive body cue:** To investigate whether GR-1 can generalize to unseen language instructions, we use GPT-4 (OpenAI, 2023) to generate 50 synonymous instructions for each of the 34 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Another failure mode of RT-1 is collision with the plate or the desk. | p. 8 (4 EXPERIMENT) |
| body limitation/failure cue | In the most challenging setting of unseen categories, a typical failure mode of GR-1 is that it sometimes mixes up the bell pepper with ... | p. 8 (4 EXPERIMENT) |
| body limitation/failure cue | Typical failure modes of GR-1 include 1) failing to completely close the drawer in the closing task and 2) failing to engage with the ... | p. 9 (4 EXPERIMENT) |
| body limitation/failure cue | If a task is not completed within 360 timesteps, it is considered a failure. | p. 14 (A.2 CALVIN BENCHMARK EXPERIMENTS) |
| body limitation/failure cue | Table 6: Examples of Unseen Language Instructions Generated by GPT-4 (OpenAI, 2023) for the Zero-Shot Unseen Language Generalization Experiment in CALVIN. Original Generated "use ... | p. 16 (Figure/Table caption) |
| body limitation/failure cue | Original Generated "use the switch to turn off the light bulb" "use the switch to stop the light source" "slide the block that it ... | p. 16 (A.6 MORE RESULTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In both experiments, we use the same training setting as in the CALVIN experiments except that the batch size and training epochs are changed ... | p. 15 (A.3 REAL ROBOT EXPERIMENTS) |
| We apply dropout and use AdamW (Loshchilov & Hutter, 2017) with cosine learning rate decay (Loshchilov & Hutter, 2016) to optimize the network. | p. 14 (A.1 NETWORK AND TRAINING DETAILS) |
| We freeze the R3M image encoder during training as in Nair et al. | p. 7 (4 EXPERIMENT) |
| We use R3M to encode the observation images and leverages a GPT-style transformer to output actions. | p. 7 (4 EXPERIMENT) |
| We compare on different future steps in Sec. | p. 14 (A.1 NETWORK AND TRAINING DETAILS) |
| We use linear layers to encode them (Fig. | p. 4 (3 METHOD) |
| The language l is encoded via a text encoder (Fig. | p. 4 (3 METHOD) |
| The decoder operates on the outputs corresponding the [OBS] tokens and mask tokens (Fig. | p. 5 (3 METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 4 EXPERIMENT - extractive body cue:** Another failure mode of RT-1 is collision with the plate or the desk.
- **p. 8 / 4 EXPERIMENT - extractive body cue:** In the most challenging setting of unseen categories, a typical failure mode of GR-1 is that it sometimes mixes up the bell pepper with the ...
- **p. 9 / 4 EXPERIMENT - extractive body cue:** Typical failure modes of GR-1 include 1) failing to completely close the drawer in the closing task and 2) failing to engage with the drawer ...
- **p. 14 / A.2 CALVIN BENCHMARK EXPERIMENTS - extractive body cue:** If a task is not completed within 360 timesteps, it is considered a failure.
- **p. 16 / Figure/Table caption - extractive body cue:** Table 6: Examples of Unseen Language Instructions Generated by GPT-4 (OpenAI, 2023) for the Zero-Shot Unseen Language Generalization Experiment in CALVIN. Original Generated "use the ...
- **p. 16 / A.6 MORE RESULTS - extractive body cue:** Original Generated "use the switch to turn off the light bulb" "use the switch to stop the light source" "slide the block that it falls ...

- **Evidence anchors reviewed:** datasets p. 5 (4 EXPERIMENT), p. 5 (4 EXPERIMENT), p. 6 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 7 (4 EXPERIMENT), metrics p. 7 (4 EXPERIMENT), p. 7 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 15 (A.3 REAL ROBOT EXPERIMENTS), p. 17 (Figure/Table caption), p. 6 (4 EXPERIMENT), baselines p. 7 (4 EXPERIMENT), p. 6 (4 EXPERIMENT), p. 6 (4 EXPERIMENT), p. 7 (4 EXPERIMENT), p. 5 (4 EXPERIMENT), p. 5 (4 EXPERIMENT), results p. 7 (4 EXPERIMENT), p. 7 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 9 (Figure/Table caption), p. 15 (A.3 REAL ROBOT EXPERIMENTS), p. 8 (4 EXPERIMENT).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (22 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Figure 6: Video Prediction Results. The images in green boxes are ground-truth images; the images in blue boxes are predicted images. results are shown in Fig. 9. GR-1 outperforms the ... (p. 9, Figure/Table caption).
- **Metric evidence:** HULC, achieves a success rate of 66.8% and an average length of 1.11. (p. 7, 4 EXPERIMENT).
- **Baseline/ablation evidence:** GR-1 outperforms all the comparing baseline methods. (p. 7, 4 EXPERIMENT).
- **Failure/negative evidence:** Another failure mode of RT-1 is collision with the plate or the desk. (p. 8, 4 EXPERIMENT).
