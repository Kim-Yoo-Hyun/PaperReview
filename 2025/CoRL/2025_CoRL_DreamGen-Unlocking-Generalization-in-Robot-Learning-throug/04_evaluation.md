# Evaluation - DreamGen: Unlocking Generalization in Robot Learning through Video World Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://research.nvidia.com/labs/lpr/publication/jang2025neural/; PDF retrieval source: https://research.nvidia.com/labs/lpr/publication/jang2025neural/. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (3 Experiments), p. 6 (3 Experiments), p. 7 (3 Experiments), p. 7 (3 Experiments), p. 5 (Figure/Table caption), p. 8 (3 Experiments)): Lastly, we show that solely training on neural trajectories with IDM actions enables us to reach a non-trivial performance (20.6% average success rate across 24 tasks), further highlighting the quality ...

## Evaluation Body Digest

- **p. 7 / 3 Experiments - extractive body cue:** 4 DreamGen Bench: A Video Generation Benchmark for Robotics Motivated by recent work benchmarking the capabilities of video generative models as world models [25, 26, ...
- **p. 5 / 3 Experiments - extractive body cue:** For real-world experiments, we evaluate on 9 real-world tasks across three embodiments: the GR1 humanoid robot, the Franka arm robot, and the low-cost SO-100 robot ...
- **p. 8 / 3 Experiments - extractive body cue:** Using these two metrics, we benchmark 4 different video world models, Hunyuan [10], CogVideoX [8], WAN 2.1 [9], and Cosmos [7], on 2 different training ...
- **p. 8 / 3 Experiments - extractive body cue:** In practice, we find the model has not been trained on multiview videos (RoboCasa) and diverse robot environments, so we use a general VLM: Qwen-VL-2.5 ...
- **p. 6 / 3 Experiments - extractive body cue:** As shown in Figure 5, neural trajectories consistently improve performance for different visuomotor policies (Diffusion Policy, π0, and GR00T N1) across all robot embodiments for ...
- **p. 5 / 3 Experiments - extractive body cue:** 6Enabling zero-shot generalization to novel behaviors and novel environments with robot embodiments with zero ground-truth data still remains an open research question.
- **p. 6 / 3 Experiments - extractive body cue:** Real-world Experiments For real-world experiments, we collect 100 trajectories per task for the four GR1 and three Franka tasks.
- **p. 7 / 3 Experiments - extractive body cue:** Leveraging this capability, we generate 50 neural trajectories for each of the 14 novel behavior tasks and train our downstream visuomotor robot policy only on ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** 3 Experiments (p. 5); B Environment for Teleoperation and Evaluation (p. 15).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 3 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Lastly, we show that solely training on neural trajectories with IDM actions enables us to reach a non-trivial performance (20.6% average success rate across ... | p. 5 (3 Experiments) |
| 3 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Figure 5, neural trajectories consistently improve performance for different visuomotor policies (Diffusion Policy, π0, and GR00T N1) across all robot embodiments ... | p. 6 (3 Experiments) |
| 3 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Lastly, the baseline model trained only on pick-and-place in a single environment shows 0% Success Rate, since it does not have the ability to ... | p. 7 (3 Experiments) |
| 3 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | We follow the same proposed pipeline and train visuomotor robot policies solely on neural trajectories, and observe that we can get non-trivial success rates ... | p. 7 (3 Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4: Scaling # of Neural Trajectories in RoboCasa. We vary the sizes of neural trajectories (x-axis) and ground-truth trajectories (low, mid, high) and ... | p. 5 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 3 Experiments - extractive body cue:** 4 DreamGen Bench: A Video Generation Benchmark for Robotics Motivated by recent work benchmarking the capabilities of video generative models as world models [25, 26, ...
- **p. 5 / 3 Experiments - extractive body cue:** For real-world experiments, we evaluate on 9 real-world tasks across three embodiments: the GR1 humanoid robot, the Franka arm robot, and the low-cost SO-100 robot ...
- **p. 8 / 3 Experiments - extractive body cue:** Using these two metrics, we benchmark 4 different video world models, Hunyuan [10], CogVideoX [8], WAN 2.1 [9], and Cosmos [7], on 2 different training ...
- **p. 8 / 3 Experiments - extractive body cue:** In practice, we find the model has not been trained on multiview videos (RoboCasa) and diverse robot environments, so we use a general VLM: Qwen-VL-2.5 ...
- **p. 6 / 3 Experiments - extractive body cue:** As shown in Figure 5, neural trajectories consistently improve performance for different visuomotor policies (Diffusion Policy, π0, and GR00T N1) across all robot embodiments for ...
- **p. 5 / 3 Experiments - extractive body cue:** 6Enabling zero-shot generalization to novel behaviors and novel environments with robot embodiments with zero ground-truth data still remains an open research question.
- **p. 6 / 3 Experiments - extractive body cue:** Real-world Experiments For real-world experiments, we collect 100 trajectories per task for the four GR1 and three Franka tasks.
- **p. 7 / 3 Experiments - extractive body cue:** Leveraging this capability, we generate 50 neural trajectories for each of the 14 novel behavior tasks and train our downstream visuomotor robot policy only on ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Generalization through DREAMGEN. We enable 2D visuomotor robot policies to generalize to new environments with new behaviors, while only collecting teleoperation data for ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: DREAMGEN Overview. We begin by fine-tuning a video world model on teleoperated robot trajectories. Given an initial frame and a language instruction, the ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: Extracting Pseudo Actions. (a) shows the architecture of our IDM model and (b) shows the architecture of our latent action model. IDM Actions. ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 3. One benefit of latent actions is that it does not require actually having ground-truth actions for the target robot embodiment when training latent ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4: Scaling # of Neural Trajectories in RoboCasa. We vary the sizes of neural trajectories (x-axis) and ground-truth trajectories (low, mid, high) and report ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: Real-world Robot Evaluation Results. The red rectangular box shows the range of object randomization during training and evaluation. Low Data denotes training 10% ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Success Rate (%) Across New Behaviors (14 tasks) and Environments (13 tasks). Seen Environments, Novel Behaviors
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: DreamGen Bench Statistics and Results. IF represents Instruction Following, and PA represents Physics Alignment. GPT represents the evaluation from GPT4o, Qwen represents the ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 4 DreamGen Bench: A Video Generation Benchmark for Robotics Motivated by recent work benchmarking the capabilities of video generative models as world models [25, ... | embodiment, simulator version and control stack | p. 7 (3 Experiments), p. 5 (3 Experiments) |
| Task/environment | For real-world experiments, we evaluate on 9 real-world tasks across three embodiments: the GR1 humanoid robot, the Franka arm robot, and the low-cost SO-100 ... | reset, timeout, object/scene variation | p. 5 (3 Experiments), p. 8 (3 Experiments) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 4 (1 Introduction), p. 4 (1 Introduction) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 2 (1 Introduction), p. 2 (Abstract) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Lastly, we show that solely training on neural trajectories with IDM actions enables us to reach a non-trivial performance (20.6% average success rate across ... | definition/direction/unit from same section | p. 5 (3 Experiments) |
| Lastly, the baseline model trained only on pick-and-place in a single environment shows 0% Success Rate, since it does not have the ability to ... | definition/direction/unit from same section | p. 7 (3 Experiments) |
| We follow the same proposed pipeline and train visuomotor robot policies solely on neural trajectories, and observe that we can get non-trivial success rates ... | definition/direction/unit from same section | p. 7 (3 Experiments) |
| Figure 4: Scaling # of Neural Trajectories in RoboCasa. We vary the sizes of neural trajectories (x-axis) and ground-truth trajectories (low, mid, high) and ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Table 5: Success Rate (%) of Real-world Data Augmentation Experiments.. | definition/direction/unit from same section | p. 18 (Figure/Table caption) |
| For this purpose, we first employ the VideoCon-Physics [26], a VLM specifically trained to give scores for physics adherence of generated videos. | definition/direction/unit from same section | p. 8 (3 Experiments) |
| 0 10 20 30 40 50 60 70 DreamGenBench Score 0 5 10 15 20 RoboCasa Score WAN CogVideoX Hunyuan Cosmos Figure 6: Performance ... | definition/direction/unit from same section | p. 8 (3 Experiments) |
| Empricially, we observe a higher performance gain for GR00T N1 compared to DP and π0; we hypothesize that having separate action and decoder parameters ... | definition/direction/unit from same section | p. 6 (3 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| This hints towards a potential for a new paradigm in robot learning, as synthetic data generation through neural trajectories is significantly more scalable compared ... | comparison identity and matched condition | p. 5 (3 Experiments) |
| Empricially, we observe a higher performance gain for GR00T N1 compared to DP and π0; we hypothesize that having separate action and decoder parameters ... | comparison identity and matched condition | p. 6 (3 Experiments) |
| Lastly, the baseline model trained only on pick-and-place in a single environment shows 0% Success Rate, since it does not have the ability to ... | comparison identity and matched condition | p. 7 (3 Experiments) |
| Figure 1: Generalization through DREAMGEN. We enable 2D visuomotor robot policies to generalize to new environments with new behaviors, while only collecting teleoperation data ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Figure 4: Scaling # of Neural Trajectories in RoboCasa. We vary the sizes of neural trajectories (x-axis) and ground-truth trajectories (low, mid, high) and ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| Behavior Generalization We investigate whether our pipeline enables robots to learn entirely new behaviors solely from neural trajectories without involving any human teleoperation. | comparison identity and matched condition | p. 7 (3 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| GPT represents the evaluation from GPT4o, Qwen represents the evaluation from Qwen2.5VL, and Hu represents the human evaluation. -zero represents zero-shot inference and -sft ... | component/input/data sensitivity | p. 8 (3 Experiments) |
| Behavior Generalization We investigate whether our pipeline enables robots to learn entirely new behaviors solely from neural trajectories without involving any human teleoperation. | component/input/data sensitivity | p. 7 (3 Experiments) |
| We follow the same proposed pipeline and train visuomotor robot policies solely on neural trajectories, and observe that we can get non-trivial success rates ... | component/input/data sensitivity | p. 7 (3 Experiments) |
| We also quantify the zero-shot capability of the models, evaluated without adapting to the specific embodiment. | component/input/data sensitivity | p. 8 (3 Experiments) |
| Table 6: Pearson correlation coefficients between automatic IF (GPT-4o) and human IF-human scores across different datasets and model variants. | component/input/data sensitivity | p. 19 (Figure/Table caption) |
| Figure 2: DREAMGEN Overview. We begin by fine-tuning a video world model on teleoperated robot trajectories. Given an initial frame and a language instruction, ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Lastly, we introduce DreamGen Bench (Section 4), a new video generation benchmark designed to evaluate how well different video world models adapt to novel ... | Lastly, we show that solely training on neural trajectories with IDM actions enables us to reach a non-trivial performance (20.6% average success rate across ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (3 Experiments), p. 6 (3 Experiments), p. 7 (3 Experiments), p. 7 (3 Experiments), p. 5 (Figure/Table caption), p. 8 (3 Experiments) |
| Primary metric/result | As shown in Figure 5, neural trajectories consistently improve performance for different visuomotor policies (Diffusion Policy, π0, and GR00T N1) across all robot embodiments ... | numeric claim only at cited anchor | p. 6 (3 Experiments) |

- Numeric sentences retained from the body:
- **p. 5 / 3 Experiments - extractive body cue:** For real-world experiments, we evaluate on 9 real-world tasks across three embodiments: the GR1 humanoid robot, the Franka arm robot, and the low-cost SO-100 robot ...
- **p. 5 / 3 Experiments - extractive body cue:** Lastly, we show that solely training on neural trajectories with IDM actions enables us to reach a non-trivial performance (20.6% average success rate across 24 ...
- **p. 6 / 3 Experiments - extractive body cue:** Low Data denotes training 10% of available training data (only 10 trajectories per task except for GR1-folding, where we used 25 trajectories), and Low Data ...
- **p. 6 / 3 Experiments - extractive body cue:** Real-world Experiments For real-world experiments, we collect 100 trajectories per task for the four GR1 and three Franka tasks.
- **p. 6 / 3 Experiments - extractive body cue:** For the two SO-100 tasks, we collect 40 and 50 trajectories for the strawberry pick-and-place and tic-tac-toe tasks, respectively.
- **p. 6 / 3 Experiments - extractive body cue:** Details of the data collection and evaluation criteria for each of the 9 tasks are provided in the Appendix I, and details of the video ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 7 Limitation Our approach is complementary to existing methods that learn from videos, although we do not directly benchmark against them. | p. 9 (6 Conclusion) |
| body limitation/failure cue | Supporting more complex, dexterous behaviors that require richer control remains an important direction for future work. | p. 9 (6 Conclusion) |
| body limitation/failure cue | Table 3. One benefit of latent actions is that it does not require actually having ground-truth actions for the target robot embodiment when training ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | Lastly, the baseline model trained only on pick-and-place in a single environment shows 0% Success Rate, since it does not have the ability to ... | p. 7 (3 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 2We provide the hyperparameters (learning rate, number of epochs, etc.) used for all of the experimental setups in Appendix D. | p. 3 (1 Introduction) |
| Empricially, we observe a higher performance gain for GR00T N1 compared to DP and π0; we hypothesize that having separate action and decoder parameters ... | p. 6 (3 Experiments) |
| 2 DREAMGEN In the next subsections, we describe in detail the 4 different steps (shown in Figure 2) of DREAMGEN, creating and utilizing neural ... | p. 3 (1 Introduction) |
| For GR00T N1, we treat the two types of trajectories as separate embodiments by using separate action encoder and decoder. | p. 4 (1 Introduction) |
| For the inverse dynamics model (IDM) architecture, we use diffusion transformers with SigLIP-2 vision encoder and train with a flow matching objective. | p. 4 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 6 Conclusion - extractive body cue:** 7 Limitation Our approach is complementary to existing methods that learn from videos, although we do not directly benchmark against them.
- **p. 9 / 6 Conclusion - extractive body cue:** Supporting more complex, dexterous behaviors that require richer control remains an important direction for future work.
- **p. 4 / Figure/Table caption - extractive body cue:** Table 3. One benefit of latent actions is that it does not require actually having ground-truth actions for the target robot embodiment when training latent ...
- **p. 7 / 3 Experiments - extractive body cue:** Lastly, the baseline model trained only on pick-and-place in a single environment shows 0% Success Rate, since it does not have the ability to generalize ...

- **PDF anchors reviewed:** datasets p. 7 (3 Experiments), p. 5 (3 Experiments), p. 8 (3 Experiments), p. 8 (3 Experiments), p. 6 (3 Experiments), p. 5 (3 Experiments), metrics p. 5 (3 Experiments), p. 7 (3 Experiments), p. 7 (3 Experiments), p. 5 (Figure/Table caption), p. 18 (Figure/Table caption), p. 8 (3 Experiments), baselines p. 5 (3 Experiments), p. 6 (3 Experiments), p. 7 (3 Experiments), p. 1 (Figure/Table caption), p. 5 (Figure/Table caption), p. 7 (3 Experiments), results p. 5 (3 Experiments), p. 6 (3 Experiments), p. 7 (3 Experiments), p. 7 (3 Experiments), p. 5 (Figure/Table caption), p. 8 (3 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
