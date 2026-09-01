# Evaluation - Masked Visual Pre-training for Motor Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2203.06173; PDF retrieval source: https://arxiv.org/abs/2203.06173. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (Figure/Table caption), p. 7 (Figure/Table caption), p. 6 (5.1. Sample Complexity), p. 8 (5.3. Ablations), p. 8 (5.4. Additional Comparisons), p. 6 (4. Experimental Setup)): Figure 5. Sample complexity. We plot the success rate as a function of environment steps on the 8 PixMC tasks. Each task uses either the Franka arm with a parallel ...

## Evaluation Body Digest

- **p. 4 / 3.4. Observations and Actions - extractive PDF cue:** The benchmark provides proprioceptive information for the robots, as well as hand-engineered states typically including 3D poses or relevant objects, goals, and their relations.
- **p. 4 / 3.1. Motivation - extractive PDF cue:** In particular, there is no benchmark suite for learning motor control algorithms that has high-resolution images, realistic robots, fast physics simulation, efficient training, and appropriate ...
- **p. 6 / 5.1. Sample Complexity - extractive PDF cue:** We consider the oracle state model (i.e., position, orientation, and velocity of the object, goal and robot in world-coordinate system, which is difficult to estimate ...
- **p. 6 / 5.2. Generalization - extractive PDF cue:** We import various objects from the YCB dataset (Calli et al., 2015)-box, can, mug, and banana-for the pick task and re-train the model for each ...
- **p. 5 / 4. Experimental Setup - extractive PDF cue:** We consider two kinds of pretraining data: ImageNet (Deng et al., 2009) and a joint Human-Object Interaction (HOI) dataset.
- **p. 5 / 4. Experimental Setup - extractive PDF cue:** We train the MAE models for 1600 epochs on 16 GPUs for both HOI and ImageNet datasets.
- **p. 8 / 5.4. Additional Comparisons - extractive PDF cue:** We believe it would be interesting to perform a controlled study on in-the-wild images with text annotations, like from the recently released Ego4D dataset (Grauman ...
- **p. 7 / 5.3. Ablations - extractive PDF cue:** We conjecture that it may be due to (a) the RL signal being unstable and hard to tune; (b) noisy gradients from the RL objective ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** demonstration으로 정의된 robot task distribution.
- **Input boundary:** observation history와 expert trajectory/action.
- **Output/decision under evaluation:** predicted action 또는 action chunk.
- **Primary target:** imitation error, task success, robustness와 compounding error.
- **Detected evaluation headings:** 3. PixMC Benchmark (p. 4); 4. Experimental Setup (p. 5); 5. Experimental Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 5. Sample complexity. We plot the success rate as a function of environment steps on the 8 PixMC tasks. Each task uses either ... | p. 5 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 10. Learning rate and seed stability. For each model, we train 15 instances of the model with 3 learning rates and 5 seeds. ... | p. 7 (Figure/Table caption) |
| 5.1. Sample Complexity | EMPIRICAL / REAL-ROBOT OR HARDWARE | The supervised baseline is flat at zero success rate on the pick and move tasks with both robots; MVP rivals the oracle on the ... | p. 6 (5.1. Sample Complexity) |
| 5.3. Ablations | EMPIRICAL / REAL-ROBOT OR HARDWARE | We observe that the larger encoder does not improve performance. | p. 8 (5.3. Ablations) |
| 5.4. Additional Comparisons | EMPIRICAL / REAL-ROBOT OR HARDWARE | We see that MoCo-v3 can achieve non-trivial performance, showing the generality of our approach. | p. 8 (5.4. Additional Comparisons) |

## Dataset / Benchmark Role

- **p. 4 / 3.4. Observations and Actions - extractive PDF cue:** The benchmark provides proprioceptive information for the robots, as well as hand-engineered states typically including 3D poses or relevant objects, goals, and their relations.
- **p. 4 / 3.1. Motivation - extractive PDF cue:** In particular, there is no benchmark suite for learning motor control algorithms that has high-resolution images, realistic robots, fast physics simulation, efficient training, and appropriate ...
- **p. 6 / 5.1. Sample Complexity - extractive PDF cue:** We consider the oracle state model (i.e., position, orientation, and velocity of the object, goal and robot in world-coordinate system, which is difficult to estimate ...
- **p. 6 / 5.2. Generalization - extractive PDF cue:** We import various objects from the YCB dataset (Calli et al., 2015)-box, can, mug, and banana-for the pick task and re-train the model for each ...
- **p. 5 / 4. Experimental Setup - extractive PDF cue:** We consider two kinds of pretraining data: ImageNet (Deng et al., 2009) and a joint Human-Object Interaction (HOI) dataset.
- **p. 5 / 4. Experimental Setup - extractive PDF cue:** We train the MAE models for 1600 epochs on 16 GPUs for both HOI and ImageNet datasets.
- **p. 8 / 5.4. Additional Comparisons - extractive PDF cue:** We believe it would be interesting to perform a controlled study on in-the-wild images with text annotations, like from the recently released Ego4D dataset (Grauman ...
- **p. 7 / 5.3. Ablations - extractive PDF cue:** We conjecture that it may be due to (a) the RL signal being unstable and hard to tune; (b) noisy gradients from the RL objective ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. We explore learning complex motor control from pixels. We show that we are able to solve a range of motor control tasks with ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. Masked visual pre-training for motor control. Left: We first pre-train visual representations using self-supervision through masked image modeling (He et al., 2021) from ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 3. Example reconstructions. For each triplet from left to right: the masked image, the reconstructed image, the ground-truth target. We observe that the autoencoder ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Table 1. Existing benchmarks. Compared to existing bench- marks, ours features a unique combination of hand-designed tasks, dense rewards, and complex robots (e.g., multi-finger hands). ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 4. Example tasks. We show example trajectories for the Franka and Kuka tasks. See the project page for video examples.
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 5. Sample complexity. We plot the success rate as a function of environment steps on the 8 PixMC tasks. Each task uses either the ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 6. Robustness to distractors. The robots are trained to pick up a blue box of 4.5cm side length. At test time, we add a ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 7. Generalization to objects of various geometries. We import three additional objects (i.e., can, mug, and banana) from the YCB dataset and re-train the ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The benchmark provides proprioceptive information for the robots, as well as hand-engineered states typically including 3D poses or relevant objects, goals, and their relations. | embodiment, simulator version and control stack | p. 4 (3.4. Observations and Actions), p. 4 (3.1. Motivation) |
| Task/environment | In particular, there is no benchmark suite for learning motor control algorithms that has high-resolution images, realistic robots, fast physics simulation, efficient training, and ... | reset, timeout, object/scene variation | p. 4 (3.1. Motivation), p. 6 (5.1. Sample Complexity) |
| Observation/sensor | observation history와 expert trajectory/action | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 3 (2.2. Learning Motor Control from Pixels) |
| Output/decision | predicted action 또는 action chunk | action frame, controller and termination | p. 2 (1. Introduction), p. 4 (3.4. Observations and Actions) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We plot the success rate as a function of environment steps on the 8 PixMC tasks. | definition/direction/unit from same section | p. 5 (3.6. Distributed Training) |
| MVP maintains high success rates for color and shape. | definition/direction/unit from same section | p. 6 (4. Experimental Setup) |
| The Kuka robot with the Allegro hand can pick up all of the objects with at least a 50% success rate. | definition/direction/unit from same section | p. 6 (5.2. Generalization) |
| The random model fails on 6 out of 8 PixMC tasks (0 success rate). | definition/direction/unit from same section | p. 7 (5.3. Ablations) |
| Still, both models yielded flat zero success rate on the task at all seeds. | definition/direction/unit from same section | p. 7 (5.3. Ablations) |
| We define reward-independent success metrics that typically quantify the distance from the agent or an object to a specified goal location over sufficient time ... | definition/direction/unit from same section | p. 4 (3.4. Observations and Actions) |
| We hand-design task-specific dense reward functions for training RL policies. | definition/direction/unit from same section | p. 4 (3.4. Observations and Actions) |
| We always report the performance yielded by the best learning rate aggregated over seeds unless otherwise specified. | definition/direction/unit from same section | p. 5 (4. Experimental Setup) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The MVP approach significantly outperforms the supervised baseline on 7 tasks and closely matches the oracle state model (considered the upper bound of RL) ... | comparison identity and matched condition | p. 5 (3.6. Distributed Training) |
| The supervised baseline is flat at zero success rate on the pick and move tasks with both robots; MVP rivals the oracle on the ... | comparison identity and matched condition | p. 6 (5.1. Sample Complexity) |
| We observe that, for a fixed number of steps, MVP outperforms both baselines while being less computationally expensive (1 vs. | comparison identity and matched condition | p. 8 (5.4. Additional Comparisons) |
| MVP trained on HOI data outperforms the counterpart trained on ImageNet data on 7 out of 8 tasks. | comparison identity and matched condition | p. 6 (5.3. Ablations) |
| Steps (M) KukaReach Oracle MVP Supervised Figure 10. | comparison identity and matched condition | p. 7 (5.3. Ablations) |
| We compare our learnt representations to a random features baseline. | comparison identity and matched condition | p. 7 (5.3. Ablations) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We pre-train supervised and self-supervised variants of the ViT model. | component/input/data sensitivity | p. 5 (4. Experimental Setup) |
| We freeze the visual encoder throughout the entire training horizon. | component/input/data sensitivity | p. 5 (4. Experimental Setup) |
| We use the same visual encoder, initialize it randomly, and freeze. | component/input/data sensitivity | p. 7 (5.3. Ablations) |
| Figure 2. Masked visual pre-training for motor control. Left: We first pre-train visual representations using self-supervision through masked image modeling (He et al., 2021) ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We also compare our method to visual encoders trained by supervised learning on ImageNet (Deng et al., 2009), the choice of encoder in most ... | Figure 5. Sample complexity. We plot the success rate as a function of environment steps on the 8 PixMC tasks. Each task uses either ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (Figure/Table caption), p. 7 (Figure/Table caption), p. 6 (5.1. Sample Complexity), p. 8 (5.3. Ablations), p. 8 (5.4. Additional Comparisons), p. 6 (4. Experimental Setup) |
| Primary metric/result | Figure 10. Learning rate and seed stability. For each model, we train 15 instances of the model with 3 learning rates and 5 seeds. ... | numeric claim only at cited anchor | p. 7 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 4 / 3.2. Simulator - extractive PDF cue:** For example, we are able to train our oracle state-based models in ∼12 minutes and our image models in ∼5 hours (∼8 million environment steps) ...
- **p. 4 / 3.4. Observations and Actions - extractive PDF cue:** All of our default settings use position control in joint angle space with a control frequency of 60Hz.
- **p. 4 / 3.6. Distributed Training - extractive PDF cue:** For our typical setup with 224×224 images, we can fit at most 256 environments on a single 2080 Ti GPU.
- **p. 5 / 3.6. Distributed Training - extractive PDF cue:** The MVP approach significantly outperforms the supervised baseline on 7 tasks and closely matches the oracle state model (considered the upper bound of RL) on ...
- **p. 5 / 4. Experimental Setup - extractive PDF cue:** To build HOI, we sample frames from Epic-Kitchens and SomethingSomething at 1fps and 0.3fps, respectively.
- **p. 5 / 4. Experimental Setup - extractive PDF cue:** We use the ViT-Small model with a 16×16 patch size, 384 hidden size, 6 attention heads, an MLP multiplier of 4, and 12 blocks.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | While there exist a number of excellent benchmarks for motor control, e.g., DMC (Tassa et al., 2018), RLBench (James et al., 2020), Robosuite (Zhu ... | p. 4 (3.1. Motivation) |
| body limitation/failure cue | The random model fails on 6 out of 8 PixMC tasks (0 success rate). | p. 7 (5.3. Ablations) |
| body limitation/failure cue | We observed unstable training (the loss goes to NaN), and we decreased the learning rate until training successfully completed. | p. 7 (5.3. Ablations) |
| body limitation/failure cue | We observe that the larger encoder does not improve performance. | p. 8 (5.3. Ablations) |
| body limitation/failure cue | We do not observe clear gains from preliminary model scaling and believe that scaling data and model size is an exciting area for future ... | p. 8 (5.3. Ablations) |
| body limitation/failure cue | Other hyperparams use defaults: Adam optimizer with β1 = 0.9 and β2 = 0.999, gradient norm of 1, initial noise standard deviation of 1.0. | p. 5 (4. Experimental Setup) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We always report the performance yielded by the best learning rate aggregated over seeds unless otherwise specified. | p. 5 (4. Experimental Setup) |
| To reduce randomness in the RL experiments (Agarwal et al., 2021), for each task and model we search for the best learning rate in ... | p. 5 (4. Experimental Setup) |
| For each model, we train 15 instances of the model with 3 learning rates and 5 seeds. | p. 7 (5.3. Ablations) |
| We characterize how sensitive different models are to changes in learning rate and random seed. | p. 7 (5.3. Ablations) |
| Second, it leads to considerable memory and run time savings since there is no need to back-propagate through the encoder. | p. 3 (2.2. Learning Motor Control from Pixels) |
| We implement PPO with distributed training to support large batch sizes. | p. 4 (3.6. Distributed Training) |
| This proprioceptive information is readily available on real robot hardware. | p. 3 (2.2. Learning Motor Control from Pixels) |
| The scarcity of GPU memory is a bottleneck for learning motor control from pixels. | p. 4 (3.6. Distributed Training) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 4 / 3.1. Motivation - extractive PDF cue:** While there exist a number of excellent benchmarks for motor control, e.g., DMC (Tassa et al., 2018), RLBench (James et al., 2020), Robosuite (Zhu et ...
- **p. 7 / 5.3. Ablations - extractive PDF cue:** The random model fails on 6 out of 8 PixMC tasks (0 success rate).
- **p. 7 / 5.3. Ablations - extractive PDF cue:** We observed unstable training (the loss goes to NaN), and we decreased the learning rate until training successfully completed.
- **p. 8 / 5.3. Ablations - extractive PDF cue:** We observe that the larger encoder does not improve performance.
- **p. 8 / 5.3. Ablations - extractive PDF cue:** We do not observe clear gains from preliminary model scaling and believe that scaling data and model size is an exciting area for future work.
- **p. 5 / 4. Experimental Setup - extractive PDF cue:** Other hyperparams use defaults: Adam optimizer with β1 = 0.9 and β2 = 0.999, gradient norm of 1, initial noise standard deviation of 1.0.

- **PDF anchors reviewed:** datasets p. 4 (3.4. Observations and Actions), p. 4 (3.1. Motivation), p. 6 (5.1. Sample Complexity), p. 6 (5.2. Generalization), p. 5 (4. Experimental Setup), p. 5 (4. Experimental Setup), metrics p. 5 (3.6. Distributed Training), p. 6 (4. Experimental Setup), p. 6 (5.2. Generalization), p. 7 (5.3. Ablations), p. 7 (5.3. Ablations), p. 4 (3.4. Observations and Actions), baselines p. 5 (3.6. Distributed Training), p. 6 (5.1. Sample Complexity), p. 8 (5.4. Additional Comparisons), p. 6 (5.3. Ablations), p. 7 (5.3. Ablations), p. 7 (5.3. Ablations), results p. 5 (Figure/Table caption), p. 7 (Figure/Table caption), p. 6 (5.1. Sample Complexity), p. 8 (5.3. Ablations), p. 8 (5.4. Additional Comparisons), p. 6 (4. Experimental Setup).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
