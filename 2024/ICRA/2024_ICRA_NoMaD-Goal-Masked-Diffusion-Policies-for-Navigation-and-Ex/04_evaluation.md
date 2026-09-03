# Evaluation - NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2310.07896; PDF retrieval source: https://arxiv.org/pdf/2310.07896. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (V. EVALUATION), p. 5 (V. EVALUATION), p. 6 (V. EVALUATION), p. 6 (V. EVALUATION), p. 4 (V. EVALUATION), p. 4 (V. EVALUATION)): NoMaD consistently outperforms all baselines and results in smooth, reactive policies.

## Evaluation Body Digest

- **p. 4 / V. EVALUATION - extractive body cue:** Benchmarking Performance Towards understanding Q1, we compare NoMaD to six performant baselines for exploration and navigation in 6 challenging real-world environments.
- **p. 4 / V. EVALUATION - extractive body cue:** How does NoMaD compare to prior work for visual exploration and goal-reaching in real-world environments?
- **p. 5 / V. EVALUATION - extractive body cue:** Success Masked ViNTm 15M 50% 1.0 30% VIB [17] 6M 30% 4.0 15% Autoregressivem 19M 90% 2.0 60% Random Subgoals [3] 30M 70% 2.7 90% ...
- **p. 5 / V. EVALUATION - extractive body cue:** The Autoregressive baseline uses a more expressive policy class and outperforms these baselines, but struggles in complex environments.
- **p. 6 / V. EVALUATION - extractive body cue:** This suggests that training for these two behaviors involves learning shared representations and affordances, and a single policy can indeed excel at both task-agnostic and ...
- **p. 4 / V. EVALUATION - extractive body cue:** We report the mean success rate for each baseline, as well as the mean number of collisions per experiment.
- **p. 6 / V. EVALUATION - extractive body cue:** Visual Encoder Success # Collisions Late Fusion CNN 52% 3.2 Early Fusion CNN 68% 1.5 ViT 32% 2.5 NoMaD 98% 0.2 TABLE III: The performance ...
- **p. 6 / V. EVALUATION - extractive body cue:** NoMaD outperforms both the ViT- and CNN-based architectures, successfully reaching the goal while avoiding collisions.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** V. EVALUATION (p. 4).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| V. EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | NoMaD consistently outperforms all baselines and results in smooth, reactive policies. | p. 5 (V. EVALUATION) |
| V. EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | Success Masked ViNTm 15M 50% 1.0 30% VIB [17] 6M 30% 4.0 15% Autoregressivem 19M 90% 2.0 60% Random Subgoals [3] 30M 70% 2.7 ... | p. 5 (V. EVALUATION) |
| V. EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | NoMaD outperforms both the ViT- and CNN-based architectures, successfully reaching the goal while avoiding collisions. | p. 6 (V. EVALUATION) |
| V. EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | The ViNT encoder with attention-based goal masking outperforms all alternatives. find that despite having comparable model capacities, the unified policy trained with goal masking ... | p. 6 (V. EVALUATION) |
| V. EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | We report the mean success rate for each baseline, as well as the mean number of collisions per experiment. | p. 4 (V. EVALUATION) |

## Dataset / Benchmark Role

- **p. 4 / V. EVALUATION - extractive body cue:** Benchmarking Performance Towards understanding Q1, we compare NoMaD to six performant baselines for exploration and navigation in 6 challenging real-world environments.
- **p. 4 / V. EVALUATION - extractive body cue:** How does NoMaD compare to prior work for visual exploration and goal-reaching in real-world environments?
- **p. 5 / V. EVALUATION - extractive body cue:** Success Masked ViNTm 15M 50% 1.0 30% VIB [17] 6M 30% 4.0 15% Autoregressivem 19M 90% 2.0 60% Random Subgoals [3] 30M 70% 2.7 90% ...
- **p. 5 / V. EVALUATION - extractive body cue:** The Autoregressive baseline uses a more expressive policy class and outperforms these baselines, but struggles in complex environments.
- **p. 6 / V. EVALUATION - extractive body cue:** This suggests that training for these two behaviors involves learning shared representations and affordances, and a single policy can indeed excel at both task-agnostic and ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: NoMaD is the first flexibly conditioned diffusion model of robot actions that can perform both goal-conditioned navigation and undirected exploration in previously unseen ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: Model Architecture. NoMaD uses two EfficientNet encoders ψ, ϕ to generate input tokens to a Transformer decoder. We use goal masking to jointly ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Visualizing the task-agnostic (yellow) and goal-directed pathways for two goal images (green, blue) learned by NoMaD. NoMaD predicts a bimodal distribution of collision-free ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: Visualizing rollouts of NoMaD deployed in challenging indoor (top) and outdoor (bottom) environments on the LoCoBot platform, showcasing successful exploration trajectories. Future action ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Examples of action predictions from NoMaD and baselines in undirected mode (yellow) and goal-directed mode with two different goal images (blue towards left, ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Benchmarking Performance Towards understanding Q1, we compare NoMaD to six performant baselines for exploration and navigation in 6 challenging real-world environments. | embodiment, simulator version and control stack | p. 4 (V. EVALUATION), p. 4 (V. EVALUATION) |
| Task/environment | How does NoMaD compare to prior work for visual exploration and goal-reaching in real-world environments? | reset, timeout, object/scene variation | p. 4 (V. EVALUATION), p. 5 (V. EVALUATION) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 2 (III. PRELIMINARIES), p. 1 (I. INTRODUCTION) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 2 (III. PRELIMINARIES), p. 3 (IV. METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We report the mean success rate for each baseline, as well as the mean number of collisions per experiment. | definition/direction/unit from same section | p. 4 (V. EVALUATION) |
| Visual Encoder Success # Collisions Late Fusion CNN 52% 3.2 Early Fusion CNN 68% 1.5 ViT 32% 2.5 NoMaD 98% 0.2 TABLE III: The ... | definition/direction/unit from same section | p. 6 (V. EVALUATION) |
| NoMaD outperforms both the ViT- and CNN-based architectures, successfully reaching the goal while avoiding collisions. | definition/direction/unit from same section | p. 6 (V. EVALUATION) |
| Masked ViNT: We integrate our goal masking with the ViNT policy [3] to flexibly condition on the observation context ct. | definition/direction/unit from same section | p. 4 (V. EVALUATION) |
| Exploration Navigation Method Params Success Coll. | definition/direction/unit from same section | p. 5 (V. EVALUATION) |
| NoMaD consistently captures the multimodal distribution, and also makes accurate predictions when conditioned on a goal image. | definition/direction/unit from same section | p. 5 (V. EVALUATION) |
| Fig. 1: NoMaD is the first flexibly conditioned diffusion model of robot actions that can perform both goal-conditioned navigation and undirected exploration in previously ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Fig. 2: Model Architecture. NoMaD uses two EfficientNet encoders ψ, ϕ to generate input tokens to a Transformer decoder. We use goal masking to ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Most notably, NoMaD outperforms the state-of-the-art (Subgoal Diffusion) by 25%, while also avoiding collisions and requiring 15× fewer parameters. mThese baselines that use goal ... | comparison identity and matched condition | p. 5 (V. EVALUATION) |
| This is the best exploration baseline, outperforming both VIB and IBC. | comparison identity and matched condition | p. 5 (V. EVALUATION) |
| CNN with early fusion outperforms late fusion, confirming similar analysis in prior work [3, 38], but struggles to effectively condition on goal information. | comparison identity and matched condition | p. 6 (V. EVALUATION) |
| We report the mean success rate for each baseline, as well as the mean number of collisions per experiment. | comparison identity and matched condition | p. 4 (V. EVALUATION) |
| This baseline predicts point estimates of future actions conditioned on ct, rather than modeling the distribution. | comparison identity and matched condition | p. 4 (V. EVALUATION) |
| NoMaD outperforms both the ViT- and CNN-based architectures, successfully reaching the goal while avoiding collisions. | comparison identity and matched condition | p. 6 (V. EVALUATION) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Random Subgoals: A variation of the above ViNT system which replaces subgoal diffusion with randomly sampling the training data for a candidate subgoal, which ... | component/input/data sensitivity | p. 5 (V. EVALUATION) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we present a design for such a policy by combining a Transformer backbone for encoding the highdimensional stream of visual observations ... | NoMaD consistently outperforms all baselines and results in smooth, reactive policies. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (V. EVALUATION), p. 5 (V. EVALUATION), p. 6 (V. EVALUATION), p. 6 (V. EVALUATION), p. 4 (V. EVALUATION), p. 4 (V. EVALUATION) |
| Primary metric/result | Success Masked ViNTm 15M 50% 1.0 30% VIB [17] 6M 30% 4.0 15% Autoregressivem 19M 90% 2.0 60% Random Subgoals [3] 30M 70% 2.7 ... | numeric claim only at cited anchor | p. 5 (V. EVALUATION) |

- Numeric sentences retained from the body:
- **p. 4 / V. EVALUATION - extractive body cue:** All baselines are trained on a combination of GNM and SACSoN datasets for 20 epochs, and we perform minimal hyperparameter tuning to ensure stable training ...
- **p. 4 / IV. METHOD - extractive body cue:** We train NoMaD on a combination of GNM and SACSoN datasets, large heterogeneous datasets collected across a diverse set of environments and robotic platforms, including ...
- **p. 4 / IV. METHOD - extractive body cue:** We use the AdamW optimizer [43] with a learning rate of 10-4 and train NoMaD for 30 epochs with a batch size of 256.
- **p. 4 / IV. METHOD - extractive body cue:** For the ViNT observation encoder, we use EfficientNet-B0 [39] to tokenize observations and goals into 256-dimensional embeddings, followed by a Transformer decoder with 4 layers ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | While our experiments provide a proof of concept that unified policies can provide more effective navigation in new environments, our system has a number ... | p. 6 (VI. DISCUSSION) |
| body limitation/failure cue | Exploration with topological maps: While goalconditioned policies can exhibit useful affordances and collision-avoidance behavior, they may be insufficient for navigation in large environments that ... | p. 3 (8 Future) |
| body limitation/failure cue | We report the mean success rate for each baseline, as well as the mean number of collisions per experiment. | p. 4 (V. EVALUATION) |
| body limitation/failure cue | Fig. 3: Visualizing the task-agnostic (yellow) and goal-directed pathways for two goal images (green, blue) learned by NoMaD. NoMaD predicts a bimodal distribution of ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | VIB and Masked ViNT struggle in all the environments we tested and frequently end in collisions, likely due to challenges with effectively modeling multimodal ... | p. 5 (V. EVALUATION) |
| body limitation/failure cue | For exploratory goal discovery, NoMaD outperforms the best published baseline (Subgoal Diffusion) by over 25% in terms of both efficiency and collision avoidance, and ... | p. 5 (V. EVALUATION) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We use the AdamW optimizer [43] with a learning rate of 10-4 and train NoMaD for 30 epochs with a batch size of 256. | p. 4 (IV. METHOD) |
| Our implementation uses a categorical representation of the action distribution, goal masking, and the same visual encoder design. | p. 4 (V. EVALUATION) |
| Diffusion Policy: We train a diffusion policy [31] with the same visual encoder as NoMaD and m = 0. | p. 5 (V. EVALUATION) |
| ViNT Policy: We use the authors' published checkpoint of the ViNT navigation policy [3], which predicts point estimates of future actions conditioned on observations ... | p. 5 (V. EVALUATION) |
| We find the choice of visual encoder to be crucial for training diffusion policies, as summarized in Table III. | p. 6 (V. EVALUATION) |
| We use a straight-through estimator [44] for propagating gradients to the observation and goal encoders during training. | p. 6 (V. EVALUATION) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / VI. DISCUSSION - extractive body cue:** While our experiments provide a proof of concept that unified policies can provide more effective navigation in new environments, our system has a number of ...
- **p. 3 / 8 Future - extractive body cue:** Exploration with topological maps: While goalconditioned policies can exhibit useful affordances and collision-avoidance behavior, they may be insufficient for navigation in large environments that require ...
- **p. 4 / V. EVALUATION - extractive body cue:** We report the mean success rate for each baseline, as well as the mean number of collisions per experiment.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Visualizing the task-agnostic (yellow) and goal-directed pathways for two goal images (green, blue) learned by NoMaD. NoMaD predicts a bimodal distribution of collision-free ...
- **p. 5 / V. EVALUATION - extractive body cue:** VIB and Masked ViNT struggle in all the environments we tested and frequently end in collisions, likely due to challenges with effectively modeling multimodal action ...
- **p. 5 / V. EVALUATION - extractive body cue:** For exploratory goal discovery, NoMaD outperforms the best published baseline (Subgoal Diffusion) by over 25% in terms of both efficiency and collision avoidance, and succeeds ...

- **Evidence anchors reviewed:** datasets p. 4 (V. EVALUATION), p. 4 (V. EVALUATION), p. 5 (V. EVALUATION), p. 5 (V. EVALUATION), p. 6 (V. EVALUATION), metrics p. 4 (V. EVALUATION), p. 6 (V. EVALUATION), p. 6 (V. EVALUATION), p. 4 (V. EVALUATION), p. 5 (V. EVALUATION), p. 5 (V. EVALUATION), baselines p. 5 (V. EVALUATION), p. 5 (V. EVALUATION), p. 6 (V. EVALUATION), p. 4 (V. EVALUATION), p. 4 (V. EVALUATION), p. 6 (V. EVALUATION), results p. 5 (V. EVALUATION), p. 5 (V. EVALUATION), p. 6 (V. EVALUATION), p. 6 (V. EVALUATION), p. 4 (V. EVALUATION), p. 4 (V. EVALUATION).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Benchmarking Performance Towards understanding Q1, we compare NoMaD to six performant baselines for exploration and navigation in 6 challenging real-world environments. (p. 4, V. EVALUATION).
- **Metric evidence:** Success Masked ViNTm 15M 50% 1.0 30% VIB [17] 6M 30% 4.0 15% Autoregressivem 19M 90% 2.0 60% Random Subgoals [3] 30M 70% 2.7 90% Subgoal Diffusion [3] 335M 77% ... (p. 5, V. EVALUATION).
- **Baseline/ablation evidence:** Most notably, NoMaD outperforms the state-of-the-art (Subgoal Diffusion) by 25%, while also avoiding collisions and requiring 15× fewer parameters. mThese baselines that use goal masking. images, which are used by ... (p. 5, V. EVALUATION).
- **Failure/negative evidence:** VIB and Masked ViNT struggle in all the environments we tested and frequently end in collisions, likely due to challenges with effectively modeling multimodal action distributions. (p. 5, V. EVALUATION).
