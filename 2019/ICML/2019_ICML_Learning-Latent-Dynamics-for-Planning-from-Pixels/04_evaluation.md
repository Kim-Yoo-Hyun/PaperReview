# Evaluation - Learning Latent Dynamics for Planning from Pixels

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1811.04551; PDF retrieval source: https://arxiv.org/pdf/1811.04551. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (5. Experiments), p. 6 (5. Experiments), p. 20 (Figure/Table caption), p. 7 (Figure/Table caption), p. 14 (Figure/Table caption), p. 15 (Figure/Table caption)): Within less than one hundredth the episodes, PlaNet outperforms A3C (Mnih et al., 2016) and achieves similar performance to the top model-free algorithm D4PG (Barth-Maron et al., 2018).

## Evaluation Body Digest

- **p. 6 / 5. Experiments - extractive body cue:** The cartpole swingup task requires a long planning horizon and to memorize the cart when it is out of view, reacher has a sparse reward ...
- **p. 6 / 5. Experiments - extractive body cue:** After 500 episodes, it achieves performance similar to D4PG, trained from images for 100,000 episodes, except for the finger task.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Comparison of PlaNet to model-free algorithms and other model designs. Plots show test performance over the number of collected episodes. We compare PlaNet ...
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 11: Open-loop state diagnostics. We freeze the dynamics model of a PlaNet agent and learn small neural networks to predict the true positions, velocities, ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Image-based control domains used in our experiments. The images show agent observations before downscaling to 64 × 64 × 3 pixels. (a) The ...
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 6: We compare a single PlaNet agent trained on all tasks to individual PlaNet agents. The plot shows test performance over the number of ...
- **p. 6 / 5. Experiments - extractive body cue:** Iterative search for action sequences using CEM improves performance on all tasks.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Unrolling schemes. The labels si/j are short for the state at time i conditioned on observations up to time j. Arrows pointing at ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** 5. Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5. Experiments | EMPIRICAL / SIMULATION | Within less than one hundredth the episodes, PlaNet outperforms A3C (Mnih et al., 2016) and achieves similar performance to the top model-free algorithm D4PG ... | p. 6 (5. Experiments) |
| 5. Experiments | EMPIRICAL / SIMULATION | Iterative search for action sequences using CEM improves performance on all tasks. | p. 6 (5. Experiments) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Figure 12: Planning performance on the cheetah running task with the true simulator using different planner settings. Performance ranges from 132 (blue) to 837 ... | p. 20 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Table 1: Comparison of PlaNet to the model-free algorithms A3C and D4PG reported by Tassa et al. (2018). The training curves for these are ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Figure 8: We compare the standard variational objective with latent overshooting on our proposed RSSM and another model called DRNN that uses two RNNs ... | p. 14 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 5. Experiments - extractive body cue:** The cartpole swingup task requires a long planning horizon and to memorize the cart when it is out of view, reacher has a sparse reward ...
- **p. 6 / 5. Experiments - extractive body cue:** After 500 episodes, it achieves performance similar to D4PG, trained from images for 100,000 episodes, except for the finger task.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Image-based control domains used in our experiments. The images show agent observations before downscaling to 64 × 64 × 3 pixels. (a) The ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Latent dynamics model designs. In this example, the model observes the first two time steps and predicts the third. Circles represent stochastic variables ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Unrolling schemes. The labels si/j are short for the state at time i conditioned on observations up to time j. Arrows pointing at ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Comparison of PlaNet to model-free algorithms and other model designs. Plots show test performance over the number of collected episodes. We compare PlaNet ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Comparison of PlaNet to the model-free algorithms A3C and D4PG reported by Tassa et al. (2018). The training curves for these are shown ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Comparison of agent designs. Plots show test performance over the number of collected episodes. We compare PlaNet, a version that collects data under ...
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 6: We compare a single PlaNet agent trained on all tasks to individual PlaNet agents. The plot shows test performance over the number of ...
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 7: Per-task performance of a single PlaNet agent trained on the six tasks. Plots show test performance over the number of episodes collected per ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The cartpole swingup task requires a long planning horizon and to memorize the cart when it is out of view, reacher has a sparse ... | embodiment, simulator version and control stack | p. 6 (5. Experiments), p. 6 (5. Experiments) |
| Task/environment | After 500 episodes, it achieves performance similar to D4PG, trained from images for 100,000 episodes, except for the finger task. | reset, timeout, object/scene variation | p. 6 (5. Experiments) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 2 (2. Latent Space Planning), p. 3 (3. Recurrent State Space Model) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 2 (2. Latent Space Planning), p. 3 (2 Initialize model parameters θ randomly) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The cartpole swingup task requires a long planning horizon and to memorize the cart when it is out of view, reacher has a sparse ... | definition/direction/unit from same section | p. 6 (5. Experiments) |
| Figure 4: Comparison of PlaNet to model-free algorithms and other model designs. Plots show test performance over the number of collected episodes. We compare ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 11: Open-loop state diagnostics. We freeze the dynamics model of a PlaNet agent and learn small neural networks to predict the true positions, ... | definition/direction/unit from same section | p. 19 (Figure/Table caption) |
| Figure 1: Image-based control domains used in our experiments. The images show agent observations before downscaling to 64 × 64 × 3 pixels. (a) ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Figure 6: We compare a single PlaNet agent trained on all tasks to individual PlaNet agents. The plot shows test performance over the number ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |
| Iterative search for action sequences using CEM improves performance on all tasks. | definition/direction/unit from same section | p. 6 (5. Experiments) |
| Figure 3: Unrolling schemes. The labels si/j are short for the state at time i conditioned on observations up to time j. Arrows pointing ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Figure 7: Per-task performance of a single PlaNet agent trained on the six tasks. Plots show test performance over the number of episodes collected ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The agent solves all tasks while learning slower compared to individually trained agents. | comparison identity and matched condition | p. 6 (5. Experiments) |
| Within 100 episodes, PlaNet outperforms the policy-gradient method A3C trained from proprioceptive states for 100,000 episodes, on all tasks. | comparison identity and matched condition | p. 6 (5. Experiments) |
| Figure 1: Image-based control domains used in our experiments. The images show agent observations before downscaling to 64 × 64 × 3 pixels. (a) ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| Figure 6: We compare a single PlaNet agent trained on all tasks to individual PlaNet agents. The plot shows test performance over the number ... | comparison identity and matched condition | p. 13 (Figure/Table caption) |
| Figure 5: Comparison of agent designs. Plots show test performance over the number of collected episodes. We compare PlaNet, a version that collects data ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Figure 4: Comparison of PlaNet to model-free algorithms and other model designs. Plots show test performance over the number of collected episodes. We compare ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The stochastic component is even more important - the agent does not learn without it. | component/input/data sensitivity | p. 6 (5. Experiments) |
| Figure 5: Comparison of agent designs. Plots show test performance over the number of collected episodes. We compare PlaNet, a version that collects data ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Figure 11: Open-loop state diagnostics. We freeze the dynamics model of a PlaNet agent and learn small neural networks to predict the true positions, ... | component/input/data sensitivity | p. 19 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we propose the Deep Planning Network (PlaNet), a model-based agent that learns the environment dynamics from pixels and chooses actions through ... | Within less than one hundredth the episodes, PlaNet outperforms A3C (Mnih et al., 2016) and achieves similar performance to the top model-free algorithm D4PG ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (5. Experiments), p. 6 (5. Experiments), p. 20 (Figure/Table caption), p. 7 (Figure/Table caption), p. 14 (Figure/Table caption), p. 15 (Figure/Table caption) |
| Primary metric/result | Iterative search for action sequences using CEM improves performance on all tasks. | numeric claim only at cited anchor | p. 6 (5. Experiments) |

- Numeric sentences retained from the body:
- **p. 6 / 5. Experiments - extractive body cue:** The training time of 10 to 20 hours (depending on the task) on a single Nvidia V100 GPU compares favorably to that of A3C and ...
- **p. 6 / 5. Experiments - extractive body cue:** Within 100 episodes, PlaNet outperforms the policy-gradient method A3C trained from proprioceptive states for 100,000 episodes, on all tasks.
- **p. 6 / 5. Experiments - extractive body cue:** After 500 episodes, it achieves performance similar to D4PG, trained from images for 100,000 episodes, except for the finger task.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Directions for future work include learning temporal abstraction instead of using a fixed action repeat, possibly through hierarchical models. | p. 8 (7. Discussion) |
| body limitation/failure cue | The cartpole swingup task requires a long planning horizon and to memorize the cart when it is out of view, reacher has a sparse ... | p. 6 (5. Experiments) |
| body limitation/failure cue | The noise might also add a safety margin to the planning objective that results in more robust action sequences. | p. 6 (5. Experiments) |
| body limitation/failure cue | Figure 4: Comparison of PlaNet to model-free algorithms and other model designs. Plots show test performance over the number of collected episodes. We compare ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | Figure 2: Latent dynamics model designs. In this example, the model observes the first two time steps and predicts the third. Circles represent stochastic ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | Figure 9: Comparison of hard ReLU (Nair & Hinton, 2010) and smooth ELU (Clevert et al., 2015) activation functions. We find that smooth activations ... | p. 15 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We define a discrete time step t, hidden states st, image observations ot, continuous action vectors at, and scalar rewards rt, that follow the ... | p. 2 (2. Latent Space Planning) |
| The training time of 10 to 20 hours (depending on the task) on a single Nvidia V100 GPU compares favorably to that of A3C ... | p. 6 (5. Experiments) |
| Our implementation uses TensorFlow Probability (Dillon et al., 2017). | p. 6 (5. Experiments) |
| Variational encoder Since the model is non-linear, we cannot directly compute the state posteriors that are needed for parameter learning. | p. 3 (3. Recurrent State Space Model) |
| Starting from a small amount of S seed episodes collected under random actions, we train the model and add one additional episode to the ... | p. 3 (2 Initialize model parameters θ randomly) |
| 6 Compute loss L(θ) from Equation 3. | p. 2 (2 Initialize model parameters θ randomly) |
| This makes it difficult to remember information over multiple time steps. | p. 4 (3. Recurrent State Space Model) |
| In this example, the model observes the first two time steps and predicts the third. | p. 4 (3. Recurrent State Space Model) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 7. Discussion - extractive body cue:** Directions for future work include learning temporal abstraction instead of using a fixed action repeat, possibly through hierarchical models.
- **p. 6 / 5. Experiments - extractive body cue:** The cartpole swingup task requires a long planning horizon and to memorize the cart when it is out of view, reacher has a sparse reward ...
- **p. 6 / 5. Experiments - extractive body cue:** The noise might also add a safety margin to the planning objective that results in more robust action sequences.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Comparison of PlaNet to model-free algorithms and other model designs. Plots show test performance over the number of collected episodes. We compare PlaNet ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Latent dynamics model designs. In this example, the model observes the first two time steps and predicts the third. Circles represent stochastic variables ...
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 9: Comparison of hard ReLU (Nair & Hinton, 2010) and smooth ELU (Clevert et al., 2015) activation functions. We find that smooth activations help ...

- **Evidence anchors reviewed:** datasets p. 6 (5. Experiments), p. 6 (5. Experiments), metrics p. 6 (5. Experiments), p. 7 (Figure/Table caption), p. 19 (Figure/Table caption), p. 2 (Figure/Table caption), p. 13 (Figure/Table caption), p. 6 (5. Experiments), baselines p. 6 (5. Experiments), p. 6 (5. Experiments), p. 2 (Figure/Table caption), p. 13 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), results p. 6 (5. Experiments), p. 6 (5. Experiments), p. 20 (Figure/Table caption), p. 7 (Figure/Table caption), p. 14 (Figure/Table caption), p. 15 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (20 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Figure 12: Planning performance on the cheetah running task with the true simulator using different planner settings. Performance ranges from 132 (blue) to 837 (yellow). Evaluating more action sequences, optimizing ... (p. 20, Figure/Table caption).
- **Metric evidence:** Iterative search for action sequences using CEM improves performance on all tasks. (p. 6, 5. Experiments).
- **Baseline/ablation evidence:** The stochastic component is even more important - the agent does not learn without it. (p. 6, 5. Experiments).
- **Failure/negative evidence:** Key difficulties include model inaccuracies, accumulating errors of multi-step predictions, failure to capture multiple possible futures, and overconfident predictions outside of the training distribution. (p. 1, 1. Introduction).
