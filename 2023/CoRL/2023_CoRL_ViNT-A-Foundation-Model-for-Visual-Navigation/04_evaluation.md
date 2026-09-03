# Evaluation - ViNT: A Foundation Model for Visual Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2306.14846; PDF retrieval source: https://arxiv.org/pdf/2306.14846. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (Figure/Table caption), p. 9 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 4 (Figure/Table caption)): Figure 4: Adapting ViNT to different goals using a new tunable goal token. Full model fine-tuning: While ViNT demonstrates strong zero-shot generalization to new environments and robots, we can further ...

## Evaluation Body Digest

- **p. 20 / B.4 Fine-tuning ViNT - extractive body cue:** [22], we further augment this dataset by allowing the rule-based agent to correct its position and re-center to the lane after a perturbation.
- **p. 21 / B.4 Fine-tuning ViNT - extractive body cue:** We assume training data is not labelled with the discrete command, so we label dataset trajectories with the corresponding commands retroactively by sampling a future ...
- **p. 20 / B.4 Fine-tuning ViNT - extractive body cue:** We collect 181 training trajectories (roughly 4 hours) in CARLA's Town 01 environment, and a further 52 trajectories (1 hour) in the held-out Town 02 ...
- **p. 18 / B.2 Subgoal Diffusion - extractive body cue:** [49], we use the unweighted training objective, called Lsimple in Ho et al.
- **p. 21 / B.4 Fine-tuning ViNT - extractive body cue:** Once we have a future goal coordinate for self-supervision, we convert to local coordinates and pass into our architecture, finetuning with the same objective as ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7: Satellite-guided physical search with ViNT. We visualize a 765m rollout of ViNT with a satellite image-based heuristic from start (orange) to goal (green). ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: Long-horizon navigation in unseen environments with ViNT. We use physical search with a topological graph-based planner to explore the environment. An image-to-image diffusion ...
- **p. 11 / Figure/Table caption - extractive body cue:** Figure 11: Robustness to dynamic pedestrians. ViNT can successfully navigate around a crowd of dynamic pedestrians and reach the goal behind them, despite its simple ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** B Implementation Details (p. 18); C Training Dataset (p. 21); Dataset (p. 22).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 4: Adapting ViNT to different goals using a new tunable goal token. Full model fine-tuning: While ViNT demonstrates strong zero-shot generalization to new ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 3: Left: ViNT can be fine-tuned end-to-end (Images) or adapted to downstream tasks (Positions and Routing), and outperforms training from scratch and other ... | p. 9 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 7: Satellite-guided physical search with ViNT. We visualize a 765m rollout of ViNT with a satellite image-based heuristic from start (orange) to goal ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 5: ViNT accomplishes long-horizon navigation with a variety of objectives in indoor and outdoor environments; example trajectories between start (orange) and goal (green) ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 1: ViNT paired with our physical search algorithm consistently outperforms baselines for the task of undirected goal-reaching in indoor and outdoor environments (left). ... | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 20 / B.4 Fine-tuning ViNT - extractive body cue:** [22], we further augment this dataset by allowing the rule-based agent to correct its position and re-center to the lane after a perturbation.
- **p. 21 / B.4 Fine-tuning ViNT - extractive body cue:** We assume training data is not labelled with the discrete command, so we label dataset trajectories with the corresponding commands retroactively by sampling a future ...
- **p. 20 / B.4 Fine-tuning ViNT - extractive body cue:** We collect 181 training trajectories (roughly 4 hours) in CARLA's Town 01 environment, and a further 52 trajectories (1 hour) in the held-out Town 02 ...
- **p. 18 / B.2 Subgoal Diffusion - extractive body cue:** [49], we use the unweighted training objective, called Lsimple in Ho et al.
- **p. 21 / B.4 Fine-tuning ViNT - extractive body cue:** Once we have a future goal coordinate for self-supervision, we convert to local coordinates and pass into our architecture, finetuning with the same objective as ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Overview of the ViNT foundation model. ViNT generalizes zero-shot across environments and robot embodiments, and can be directly applied to tasks including exploration ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: ViNT Model Architecture. ViNT uses two EfficientNet encoders ψ, ϕ to generate input tokens to a Transformer decoder. The resulting sequence is concatenated ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: Long-horizon navigation in unseen environments with ViNT. We use physical search with a topological graph-based planner to explore the environment. An image-to-image diffusion ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: ViNT accomplishes long-horizon navigation with a variety of objectives in indoor and outdoor environments; example trajectories between start (orange) and goal (green) visualized ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Adapting ViNT to different goals using a new tunable goal token. Full model fine-tuning: While ViNT demonstrates strong zero-shot generalization to new environments ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: ViNT paired with our physical search algorithm consistently outperforms baselines for the task of undirected goal-reaching in indoor and outdoor environments (left). By ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6: Visualizing ViNT exploration rollouts in challenging indoor environments using the Vizbot (top) and LoCoBot (bottom) robotic platforms. Future action samples ˆa obtained by ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: ViNT can effectively utilize goal-directed heuristics, such as 2D goal positions and satellite images, to explore novel kilometer-scale environments successfully and without interventions. ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | [22], we further augment this dataset by allowing the rule-based agent to correct its position and re-center to the lane after a perturbation. | embodiment, simulator version and control stack | p. 20 (B.4 Fine-tuning ViNT), p. 21 (B.4 Fine-tuning ViNT) |
| Task/environment | We assume training data is not labelled with the discrete command, so we label dataset trajectories with the corresponding commands retroactively by sampling a ... | reset, timeout, object/scene variation | p. 21 (B.4 Fine-tuning ViNT), p. 20 (B.4 Fine-tuning ViNT) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 18 (B.2 Subgoal Diffusion), p. 20 (B.3 Long-Horizon Physical Search via Topological Graphs) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 18 (B.2 Subgoal Diffusion), p. 19 (B.3 Long-Horizon Physical Search via Topological Graphs) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 7: Satellite-guided physical search with ViNT. We visualize a 765m rollout of ViNT with a satellite image-based heuristic from start (orange) to goal ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 3: Long-horizon navigation in unseen environments with ViNT. We use physical search with a topological graph-based planner to explore the environment. An image-to-image ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 11: Robustness to dynamic pedestrians. ViNT can successfully navigate around a crowd of dynamic pedestrians and reach the goal behind them, despite its ... | definition/direction/unit from same section | p. 11 (Figure/Table caption) |
| Figure 2: ViNT Model Architecture. ViNT uses two EfficientNet encoders ψ, ϕ to generate input tokens to a Transformer decoder. The resulting sequence is ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Figure 4: Adapting ViNT to different goals using a new tunable goal token. Full model fine-tuning: While ViNT demonstrates strong zero-shot generalization to new ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Table 4: Architectural Details of ViNT The inputs to the model are RGB images ot:t-P ∈[0, 1]P ×3×85×64 and os ∈[0, 1]3×85×64, representing the ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |
| For our experiments, we considered three heuristics to demonstrate the flexibility of our approach: • Coverage exploration: We have no long-horizon guidance for coverage ... | definition/direction/unit from same section | p. 19 (B.3 Long-Horizon Physical Search via Topological Graphs) |
| Table 2: ViNT can effectively utilize goal-directed heuristics, such as 2D goal positions and satellite images, to explore novel kilometer-scale environments successfully and without ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 1: ViNT paired with our physical search algorithm consistently outperforms baselines for the task of undirected goal-reaching in indoor and outdoor environments (left). ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Table 8: Evaluation of ViNT fine-tuning with and with- out a frozen encoder, as compared to a general-purpose visual encoder. Even when frozen, ViNT's ... | comparison identity and matched condition | p. 25 (Figure/Table caption) |
| Table 3: Left: ViNT can be fine-tuned end-to-end (Images) or adapted to downstream tasks (Positions and Routing), and outperforms training from scratch and other ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| Figure 7: Satellite-guided physical search with ViNT. We visualize a 765m rollout of ViNT with a satellite image-based heuristic from start (orange) to goal ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Figure 11: Robustness to dynamic pedestrians. ViNT can successfully navigate around a crowd of dynamic pedestrians and reach the goal behind them, despite its ... | comparison identity and matched condition | p. 11 (Figure/Table caption) |
| In all CARLA fine-tuning experiments, on-task data was collected using a rule-based oracle agent, with start and end locations sampled randomly up to 900 ... | comparison identity and matched condition | p. 20 (B.4 Fine-tuning ViNT) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 2: ViNT can effectively utilize goal-directed heuristics, such as 2D goal positions and satellite images, to explore novel kilometer-scale environments successfully and without ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Table 3: Left: ViNT can be fine-tuned end-to-end (Images) or adapted to downstream tasks (Positions and Routing), and outperforms training from scratch and other ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| Table 3: In coverage tasks, ViNT drives dif- ferent robots for 100s of meters (reported maxi- mum displacement without intervention), beating lower-capacity models (GNM) ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| We use the Flax U-Net implementation from the diffusers library [48] with textual cross-attention removed since we do not condition on text inputs. | component/input/data sensitivity | p. 18 (B.2 Subgoal Diffusion) |
| Figure 1: Overview of the ViNT foundation model. ViNT generalizes zero-shot across environments and robot embodiments, and can be directly applied to tasks including ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| Figure 4: Adapting ViNT to different goals using a new tunable goal token. Full model fine-tuning: While ViNT demonstrates strong zero-shot generalization to new ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We propose a novel exploration algorithm for the visual navigation paradigm using a diffusion model to propose short-horizon goals, and demonstrate that it enables ... | Figure 4: Adapting ViNT to different goals using a new tunable goal token. Full model fine-tuning: While ViNT demonstrates strong zero-shot generalization to new ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (Figure/Table caption), p. 9 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 4 (Figure/Table caption) |
| Primary metric/result | Table 3: Left: ViNT can be fine-tuned end-to-end (Images) or adapted to downstream tasks (Positions and Routing), and outperforms training from scratch and other ... | numeric claim only at cited anchor | p. 9 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 18 / B.2 Subgoal Diffusion - extractive body cue:** We 2We used a variety of workstations equipped with different GPU configurations over the course of this research, including 2×4090, 3×Titan Xp, 4×P100, 8×1080Ti, 8×V100, ...
- **p. 19 / B.2 Subgoal Diffusion - extractive body cue:** 2048 # Attention Layers nL 4 # Attention Heads nH 4 Temporal Context P 5 Prediction Horizon H 5 MLP layers (256, 128, 64, 32) ...
- **p. 19 / B.2 Subgoal Diffusion - extractive body cue:** Resolutions 32, 16, 8 Layers per Block 2 Attn.
- **p. 19 / B.2 Subgoal Diffusion - extractive body cue:** Gamma 1.0 EMA Power 0.75 EMA Max Decay 0.9999 CFG Mask Proportion 0.2 Train Steps 250,000 Training Time 30 hours Compute Resources v4-8 TPU board ...
- **p. 20 / B.4 Fine-tuning ViNT - extractive body cue:** In all CARLA fine-tuning experiments, on-task data was collected using a rule-based oracle agent, with start and end locations sampled randomly up to 900 meters ...
- **p. 20 / B.4 Fine-tuning ViNT - extractive body cue:** We collect 181 training trajectories (roughly 4 hours) in CARLA's Town 01 environment, and a further 52 trajectories (1 hour) in the held-out Town 02 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Limitations and Future Work As with many large-scale models, ViNT carries a heavier computational burden at inference time, which can present a challenge for ... | p. 11 (7 Discussion) |
| body limitation/failure cue | For example, it cannot control the altitude of a quadcopter or handle other changes in the action representation, nor accommodate new sensors such as ... | p. 11 (7 Discussion) |
| body limitation/failure cue | To produce training pairs for the diffusion model, we first select ot uniformly at random from the training data and then select osi to ... | p. 18 (B.2 Subgoal Diffusion) |
| body limitation/failure cue | Table 5: Comparing merits (✓) and demerits (✗) of different goal-conditioning architectures. While "Early Fusion" works the best for the core navigation task, it ... | p. 18 (Figure/Table caption) |
| body limitation/failure cue | Figure 9: Samples from the diffusion model may be invalid subgoals, but ViNT is robust to such proposals. Implicit navigation affor- dances: Ideally, we ... | p. 10 (Figure/Table caption) |
| body limitation/failure cue | Head Dim 8 Channels (128, 128, 256, 512, 640) Diffusion Type continuous time Noise Schedule linear Hyperparameter Value Diffusion Training Dropout 0.1 Batch Size ... | p. 19 (B.2 Subgoal Diffusion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 2048 # Attention Layers nL 4 # Attention Heads nH 4 Temporal Context P 5 Prediction Horizon H 5 MLP layers (256, 128, 64, ... | p. 19 (B.2 Subgoal Diffusion) |
| Head Dim 8 Channels (128, 128, 256, 512, 640) Diffusion Type continuous time Noise Schedule linear Hyperparameter Value Diffusion Training Dropout 0.1 Batch Size ... | p. 19 (B.2 Subgoal Diffusion) |
| With the model architecture fixed, the batch size and training time varies significantly across these devices, and the entry in Table 6 is representative ... | p. 18 (B.2 Subgoal Diffusion) |
| We again use a cosine scheduler with a learning rate warmup to 0.0001 for 4 epochs. | p. 21 (B.4 Fine-tuning ViNT) |
| See Table 6 for a detailed list of hyperparameters for training the ViNT foundation model.2 | p. 18 (B.1 Training ViNT) |
| Right: command-adaptation architecture, using latent zi selected by command label index i. • Architecture: To adapt to GPS-style goals, we cut off the goal ... | p. 21 (B.4 Fine-tuning ViNT) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 11 / 7 Discussion - extractive body cue:** Limitations and Future Work As with many large-scale models, ViNT carries a heavier computational burden at inference time, which can present a challenge for power-constrained ...
- **p. 11 / 7 Discussion - extractive body cue:** For example, it cannot control the altitude of a quadcopter or handle other changes in the action representation, nor accommodate new sensors such as LIDAR.
- **p. 18 / B.2 Subgoal Diffusion - extractive body cue:** To produce training pairs for the diffusion model, we first select ot uniformly at random from the training data and then select osi to fall ...
- **p. 18 / Figure/Table caption - extractive body cue:** Table 5: Comparing merits (✓) and demerits (✗) of different goal-conditioning architectures. While "Early Fusion" works the best for the core navigation task, it does ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 9: Samples from the diffusion model may be invalid subgoals, but ViNT is robust to such proposals. Implicit navigation affor- dances: Ideally, we would ...
- **p. 19 / B.2 Subgoal Diffusion - extractive body cue:** Head Dim 8 Channels (128, 128, 256, 512, 640) Diffusion Type continuous time Noise Schedule linear Hyperparameter Value Diffusion Training Dropout 0.1 Batch Size 128 ...

- **Evidence anchors reviewed:** datasets p. 20 (B.4 Fine-tuning ViNT), p. 21 (B.4 Fine-tuning ViNT), p. 20 (B.4 Fine-tuning ViNT), p. 18 (B.2 Subgoal Diffusion), p. 21 (B.4 Fine-tuning ViNT), metrics p. 8 (Figure/Table caption), p. 4 (Figure/Table caption), p. 11 (Figure/Table caption), p. 3 (Figure/Table caption), p. 6 (Figure/Table caption), p. 17 (Figure/Table caption), baselines p. 7 (Figure/Table caption), p. 25 (Figure/Table caption), p. 9 (Figure/Table caption), p. 8 (Figure/Table caption), p. 11 (Figure/Table caption), p. 20 (B.4 Fine-tuning ViNT), results p. 6 (Figure/Table caption), p. 9 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 4 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (25 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Figure 7: Satellite-guided physical search with ViNT. We visualize a 765m rollout of ViNT with a satellite image-based heuristic from start (orange) to goal (green). The future action samples ˆa ... (p. 8, Figure/Table caption).
- **Metric evidence:** Figure 3: Long-horizon navigation in unseen environments with ViNT. We use physical search with a topological graph-based planner to explore the environment. An image-to-image diffusion model proposes diverse exploration targets ... (p. 4, Figure/Table caption).
- **Baseline/ablation evidence:** Table 1: ViNT paired with our physical search algorithm consistently outperforms baselines for the task of undirected goal-reaching in indoor and outdoor environments (left). By effectively planning over diffusion subgoal ... (p. 7, Figure/Table caption).
- **Failure/negative evidence:** Limitations and Future Work As with many large-scale models, ViNT carries a heavier computational burden at inference time, which can present a challenge for power-constrained platforms such as quadcopters. (p. 11, 7 Discussion).
