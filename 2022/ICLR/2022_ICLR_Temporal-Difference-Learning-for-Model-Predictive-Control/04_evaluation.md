# Evaluation - Temporal Difference Learning for Model Predictive Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2203.04955; PDF retrieval source: https://arxiv.org/pdf/2203.04955. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 19 (Figure/Table caption), p. 17 (Figure/Table caption), p. 8 (5. Experiments), p. 8 (5. Experiments), p. 6 (5. Experiments), p. 7 (5. Experiments)): Figure 14. Individual Meta-World tasks. Success rate of our method (TD-MPC) and SAC on diverse manipulation tasks from Meta- World (Yu et al., 2019). We use the goal-conditioned version of ...

## Evaluation Body Digest

- **p. 6 / 5. Experiments - extractive body cue:** TD-Learning for MPC 0 250 500 750 1000 Episode return Average 0 100 200 300 400 Acrobot Swingup 0 250 500 750 1000 Cartpole Swingup ...
- **p. 7 / 5. Experiments - extractive body cue:** Results are shown in Table 1. -12 image-based tasks from the DMControl Dreamer benchmark (3M environment steps).
- **p. 7 / 5. Experiments - extractive body cue:** Throughout, we benchmark performance on relatively few environment steps, e.g., 3M steps for Humanoid tasks whereas prior work typically runs for 30M steps (10×).
- **p. 5 / 5. Experiments - extractive body cue:** We choose these two benchmarks for their great task diversity and availability of baseline implementations and results.
- **p. 6 / 5. Experiments - extractive body cue:** We observe especially large performance gains on tasks with complex dynamics, e.g., the Quadruped and Acrobot tasks. the top-64 trajectories each iteration.
- **p. 8 / 5. Experiments - extractive body cue:** In contrast, a blind agent that does not 0.0 0.2 0.4 0.6 0.8 1.0 0.00 0.25 0.50 0.75 1.00 Success rate Meta-World (Goal-Conditioned) 0 1 ...
- **p. 9 / 5. Experiments - extractive body cue:** Methods are benchmarked on a single RTX3090 GPU.
- **p. 5 / 5. Experiments - extractive body cue:** We seek to answer the following questions: -How does planning with TD-MPC compare to state-ofthe-art model-based and model-free approaches? -Are TOLD models capable of multi-task ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** 5. Experiments (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 14. Individual Meta-World tasks. Success rate of our method (TD-MPC) and SAC on diverse manipulation tasks from Meta- World (Yu et al., 2019). ... | p. 19 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 8. Meta-World MT10. As our performance metric reported in Figure 5 differs from that of the Meta-World v2 benchmark proposal (Yu et al., ... | p. 17 (Figure/Table caption) |
| 5. Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Success rate on 50 goal-conditioned Meta-World tasks using individual policies, and a multi-task policy trained on 10 tasks simultaneously (Meta-World MT10). | p. 8 (5. Experiments) |
| 5. Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | In contrast, a blind agent that does not 0.0 0.2 0.4 0.6 0.8 1.0 0.00 0.25 0.50 0.75 1.00 Success rate Meta-World (Goal-Conditioned) 0 ... | p. 8 (5. Experiments) |
| 5. Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | LOOP has been shown to outperform a number of model-based methods, e.g., MBPO (Janner et al., 2019) and POLO (Lowrey et al., 2019)) on ... | p. 6 (5. Experiments) |

## Dataset / Benchmark Role

- **p. 6 / 5. Experiments - extractive body cue:** TD-Learning for MPC 0 250 500 750 1000 Episode return Average 0 100 200 300 400 Acrobot Swingup 0 250 500 750 1000 Cartpole Swingup ...
- **p. 7 / 5. Experiments - extractive body cue:** Results are shown in Table 1. -12 image-based tasks from the DMControl Dreamer benchmark (3M environment steps).
- **p. 7 / 5. Experiments - extractive body cue:** Throughout, we benchmark performance on relatively few environment steps, e.g., 3M steps for Humanoid tasks whereas prior work typically runs for 30M steps (10×).
- **p. 5 / 5. Experiments - extractive body cue:** We choose these two benchmarks for their great task diversity and availability of baseline implementations and results.
- **p. 6 / 5. Experiments - extractive body cue:** We observe especially large performance gains on tasks with complex dynamics, e.g., the Quadruped and Acrobot tasks. the top-64 trajectories each iteration.
- **p. 8 / 5. Experiments - extractive body cue:** In contrast, a blind agent that does not 0.0 0.2 0.4 0.6 0.8 1.0 0.00 0.25 0.50 0.75 1.00 Success rate Meta-World (Goal-Conditioned) 0 1 ...
- **p. 9 / 5. Experiments - extractive body cue:** Methods are benchmarked on a single RTX3090 GPU.
- **p. 5 / 5. Experiments - extractive body cue:** We seek to answer the following questions: -How does planning with TD-MPC compare to state-ofthe-art model-based and model-free approaches? -Are TOLD models capable of multi-task ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Overview. (Top) We present a framework for MPC using a task-oriented latent dynamics model and value function learned jointly by temporal difference learning. ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Training our TOLD model. A trajectory Γ0:H of length H is sampled from a replay buffer, and the first observation s0 is encoded ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. DMControl tasks. Return of our method (TD-MPC) and baselines on 15 state-based continuous control tasks from DMControl (Tassa et al., 2018). Mean of ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Learning from pixels. Return of our method (TD-MPC) and state-of-the-art algorithms on the image-based DMControl 100k benchmark used in Srinivas et al. (2020); ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Learning from pixels. Return of our method (TD-MPC) and state-of-the-art algorithms on 12 challenging image-based DMControl tasks. We follow prior work (Hafner et ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. (top) Meta-World. Success rate on 50 goal-conditioned Meta-World tasks using individual policies, and a multi-task policy trained on 10 tasks simultaneously (Meta-World MT10). ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. Variable computational budget. Return of TD-MPC on Quadruped Walk under a variable budget. We evaluate perfor- mance of fully trained agents when varying ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2. Wall-time. (top) time to solve, and (bottom) time per 500k environment steps (in hours) for the Walker Walk and Hu- manoid Stand tasks ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | TD-Learning for MPC 0 250 500 750 1000 Episode return Average 0 100 200 300 400 Acrobot Swingup 0 250 500 750 1000 Cartpole ... | embodiment, simulator version and control stack | p. 6 (5. Experiments), p. 7 (5. Experiments) |
| Task/environment | Results are shown in Table 1. -12 image-based tasks from the DMControl Dreamer benchmark (3M environment steps). | reset, timeout, object/scene variation | p. 7 (5. Experiments), p. 7 (5. Experiments) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 3 (3. TD-Learning for Model Predictive Control), p. 3 (3. TD-Learning for Model Predictive Control) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 5 (4. Task-Oriented Latent Dynamics Model), p. 2 (2. Preliminaries) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In contrast, a blind agent that does not 0.0 0.2 0.4 0.6 0.8 1.0 0.00 0.25 0.50 0.75 1.00 Success rate Meta-World (Goal-Conditioned) 0 ... | definition/direction/unit from same section | p. 8 (5. Experiments) |
| Figure 5. (top) Meta-World. Success rate on 50 goal-conditioned Meta-World tasks using individual policies, and a multi-task policy trained on 10 tasks simultaneously (Meta-World ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 14. Individual Meta-World tasks. Success rate of our method (TD-MPC) and SAC on diverse manipulation tasks from Meta- World (Yu et al., 2019). ... | definition/direction/unit from same section | p. 19 (Figure/Table caption) |
| Table 8. Meta-World MT10. As our performance metric reported in Figure 5 differs from that of the Meta-World v2 benchmark proposal (Yu et al., ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |
| Figure 10. Latent dynamics objective. Return of our method (TD-MPC) using different latent dynamics objectives in addition to reward and value prediction. 15 state-based ... | definition/direction/unit from same section | p. 15 (Figure/Table caption) |
| We seek to answer the following questions: -How does planning with TD-MPC compare to state-ofthe-art model-based and model-free approaches? -Are TOLD models capable of ... | definition/direction/unit from same section | p. 5 (5. Experiments) |
| 10: zt = hθ(st) ◁Encode first observation 11: J = 0 ◁Initialize J for loss accumulation 12: for i = t...t + H do ... | definition/direction/unit from same section | p. 5 (5. Experiments) |
| All three methods learn a model using a reconstruction loss, and select actions using either MPC or a learned policy. -MuZero (Schrittwieser et al., ... | definition/direction/unit from same section | p. 6 (5. Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 4. Learning from pixels. Return of our method (TD-MPC) and state-of-the-art algorithms on 12 challenging image-based DMControl tasks. We follow prior work (Hafner ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| We find our method to outperform or match baselines in most tasks considered, generally with larger gains on complex tasks such as Humanoid, Dog ... | comparison identity and matched condition | p. 8 (5. Experiments) |
| Table 1. Learning from pixels. Return of our method (TD-MPC) and state-of-the-art algorithms on the image-based DMControl 100k benchmark used in Srinivas et al. ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| However, we also observe that we can reduce the planning cost during inference by 50% (compared to during training) without a drop in performance ... | comparison identity and matched condition | p. 8 (5. Experiments) |
| We choose these two benchmarks for their great task diversity and availability of baseline implementations and results. | comparison identity and matched condition | p. 5 (5. Experiments) |
| See Appendix G for further discussion on baselines. | comparison identity and matched condition | p. 6 (5. Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We consider: (i) our method implemented using a state predictor (hθ being the identity function), (ii) our method implemented without the latent consistency loss ... | component/input/data sensitivity | p. 6 (5. Experiments) |
| All three methods learn a model using a reconstruction loss, and select actions using either MPC or a learned policy. -MuZero (Schrittwieser et al., ... | component/input/data sensitivity | p. 6 (5. Experiments) |
| However, we also observe that we can reduce the planning cost during inference by 50% (compared to during training) without a drop in performance ... | component/input/data sensitivity | p. 8 (5. Experiments) |
| Figure 7. Model generalization. Return of our method under three different settings: (Rand. init) TD-MPC trained from scratch on the two Run tasks; (Finetune) ... | component/input/data sensitivity | p. 12 (Figure/Table caption) |
| Figure 10. Latent dynamics objective. Return of our method (TD-MPC) using different latent dynamics objectives in addition to reward and value prediction. 15 state-based ... | component/input/data sensitivity | p. 15 (Figure/Table caption) |
| All components are deterministic and implemented using MLPs. | component/input/data sensitivity | p. 5 (5. Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| (Top) We present a framework for MPC using a task-oriented latent dynamics model and value function learned jointly by temporal difference learning. | Figure 14. Individual Meta-World tasks. Success rate of our method (TD-MPC) and SAC on diverse manipulation tasks from Meta- World (Yu et al., 2019). ... | PDF body cue; verify exact table/figure and matched conditions | p. 19 (Figure/Table caption), p. 17 (Figure/Table caption), p. 8 (5. Experiments), p. 8 (5. Experiments), p. 6 (5. Experiments), p. 7 (5. Experiments) |
| Primary metric/result | Table 8. Meta-World MT10. As our performance metric reported in Figure 5 differs from that of the Meta-World v2 benchmark proposal (Yu et al., ... | numeric claim only at cited anchor | p. 17 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / 5. Experiments - extractive body cue:** During planning, we plan for 6 iterations (8 for Dog; 12 for Humanoid), sampling N = 512 trajectories (+5% sampled from πθ), and we compute ...
- **p. 6 / 5. Experiments - extractive body cue:** TD-Learning for MPC 0 250 500 750 1000 Episode return Average 0 100 200 300 400 Acrobot Swingup 0 250 500 750 1000 Cartpole Swingup ...
- **p. 6 / 5. Experiments - extractive body cue:** In the top left, we visualize results averaged across all 15 tasks.
- **p. 6 / 5. Experiments - extractive body cue:** We observe especially large performance gains on tasks with complex dynamics, e.g., the Quadruped and Acrobot tasks. the top-64 trajectories each iteration.
- **p. 6 / 5. Experiments - extractive body cue:** For image-based tasks, observations are 3 stacked 84×84-dimensional RGB frames and we use ±4 pixel shift augmentation (Kostrikov et al., 2020).
- **p. 7 / 5. Experiments - extractive body cue:** We consider the following 92 tasks: -6 challenging Humanoid (A ∈R21) and Dog (A ∈R38) locomotion tasks with high-dimensional state and action spaces.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Due to dimensionality explosion under discretization, MuZero and EfficientZero cannot feasibly solve tasks with higher-dimensional action spaces, e.g., Walker Walk and Cheetah Run (A ... | p. 7 (5. Experiments) |
| body limitation/failure cue | Mean of 5 runs. have access to the egocentric camera fails. | p. 8 (5. Experiments) |
| body limitation/failure cue | Performance of LOOP is similar to SAC, and MPC with a simulator (MPC:sim) performs well on locomotion tasks but fails in tasks with sparse ... | p. 8 (5. Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| During planning, we plan for 6 iterations (8 for Dog; 12 for Humanoid), sampling N = 512 trajectories (+5% sampled from πθ), and we ... | p. 5 (5. Experiments) |
| TD-Learning for MPC 0 250 500 750 1000 Episode return Average 0 100 200 300 400 Acrobot Swingup 0 250 500 750 1000 Cartpole ... | p. 6 (5. Experiments) |
| TD-MPC solves Walker Walk 16× faster than LOOP while using 3.3× less compute per 500k steps. | p. 9 (5. Experiments) |
| (2018)) and Algorithm 2 TOLD (training) Require: θ, θ-: randomly initialized network parameters η, τ, λ, B: learning rate, coefficients, buffer 1: while not ... | p. 5 (5. Experiments) |
| We provide additional experiments on inference times in Appendix H. | p. 9 (5. Experiments) |
| In particular, we adopt the implementation of Yarats & Kostrikov (2020). -LOOP (Sikchi et al., 2022), a hybrid algorithm that extends SAC with planning ... | p. 6 (5. Experiments) |
| While baselines use task-dependent hyperparameters, TD-MPC uses the same hyperparameters for all tasks. | p. 7 (5. Experiments) |
| Results are shown in Table 1. -12 image-based tasks from the DMControl Dreamer benchmark (3M environment steps). | p. 7 (5. Experiments) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 5. Experiments - extractive body cue:** Due to dimensionality explosion under discretization, MuZero and EfficientZero cannot feasibly solve tasks with higher-dimensional action spaces, e.g., Walker Walk and Cheetah Run (A ∈R6), ...
- **p. 8 / 5. Experiments - extractive body cue:** Mean of 5 runs. have access to the egocentric camera fails.
- **p. 8 / 5. Experiments - extractive body cue:** Performance of LOOP is similar to SAC, and MPC with a simulator (MPC:sim) performs well on locomotion tasks but fails in tasks with sparse rewards.

- **Evidence anchors reviewed:** datasets p. 6 (5. Experiments), p. 7 (5. Experiments), p. 7 (5. Experiments), p. 5 (5. Experiments), p. 6 (5. Experiments), p. 8 (5. Experiments), metrics p. 8 (5. Experiments), p. 8 (Figure/Table caption), p. 19 (Figure/Table caption), p. 17 (Figure/Table caption), p. 15 (Figure/Table caption), p. 5 (5. Experiments), baselines p. 7 (Figure/Table caption), p. 8 (5. Experiments), p. 7 (Figure/Table caption), p. 8 (5. Experiments), p. 5 (5. Experiments), p. 6 (5. Experiments), results p. 19 (Figure/Table caption), p. 17 (Figure/Table caption), p. 8 (5. Experiments), p. 8 (5. Experiments), p. 6 (5. Experiments), p. 7 (5. Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
