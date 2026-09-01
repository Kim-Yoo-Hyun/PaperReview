# Evaluation - Dream to Control: Learning Behaviors by Latent Imagination

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1912.01603; PDF retrieval source: https://arxiv.org/pdf/1912.01603. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 8 (Figure/Table caption), p. 6 (Figure/Table caption), p. 16 (Figure/Table caption)): Baseline methods The highest reported performance on the continuous tasks is achieved by D4PG (Barth-Maron et al., 2018), an improved variant of DDPG (Lillicrap et al., 2015) that uses distributed ...

## Evaluation Body Digest

- **p. 8 / 6 EXPERIMENTS - extractive body cue:** These tasks pose a variety of challenges, including sparse rewards, contact dynamics, and 3D scenes.
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** Agent observations are images of shape 64 × 64 × 3, actions range from 1 to 12 dimensions, rewards range from 0 to 1, episodes ...
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** With an average score of 823 across tasks after 5 × 106 environment steps, Dreamer exceeds the performance of the strong model-free D4PG agent that ...
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** This suggests that future improvements in representation learning are likely to translate to higher task performance with Dreamer.
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 11: Comparison of representation learning methods for Dreamer. The lines show mean scores and the shaded areas show the standard deviation across 5 seeds. ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Using the same hyper parameters for all tasks, Dreamer exceeds previous model-based and model-free agents in terms of data-efficiency, computation time, and final ...
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 10: Comparison of action selection schemes on the continuous control tasks of the DeepMind Control Suite from pixel inputs. The lines show mean scores ...
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** We include the scores for D4PG with pixel inputs and A3C (Mnih et al., 2016) with state inputs from Tassa et al.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** 6 EXPERIMENTS (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 6 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Baseline methods The highest reported performance on the continuous tasks is achieved by D4PG (Barth-Maron et al., 2018), an improved variant of DDPG (Lillicrap ... | p. 8 (6 EXPERIMENTS) |
| 6 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | With an average score of 823 across tasks after 5 × 106 environment steps, Dreamer exceeds the performance of the strong model-free D4PG agent ... | p. 9 (6 EXPERIMENTS) |
| 6 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | This suggests that future improvements in representation learning are likely to translate to higher task performance with Dreamer. | p. 9 (6 EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 8: Comparison of representation learning objectives to be used with Dreamer. Pixel recon- struction performs best for the majority of tasks. The contrastive ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 6: Performance comparison to existing methods. Dreamer inherits the data-efficiency of PlaNet while exceeding the asymptotic performance of the best model-free agents. After ... | p. 6 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 8 / 6 EXPERIMENTS - extractive body cue:** These tasks pose a variety of challenges, including sparse rewards, contact dynamics, and 3D scenes.
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** Agent observations are images of shape 64 × 64 × 3, actions range from 1 to 12 dimensions, rewards range from 0 to 1, episodes ...
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** With an average score of 823 across tasks after 5 × 106 environment steps, Dreamer exceeds the performance of the strong model-free D4PG agent that ...
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** This suggests that future improvements in representation learning are likely to translate to higher task performance with Dreamer.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Dreamer learns a world model from past experience and efficiently learns farsighted behaviors in its latent
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: Image observations for 5 of the 20 visual control tasks used in our experiments. The tasks pose a variety of challenges including contact ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Using the same hyper parameters for all tasks, Dreamer exceeds previous model-based and model-free agents in terms of data-efficiency, computation time, and final ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3: Components of Dreamer. (a) From the dataset of past experience, the agent learns to encode observations and actions into compact latent states ( ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4: Imagination horizons. We compare the final performance of Dreamer, learning an action model without value prediction, and online planning using PlaNet. Learning a ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5: Reconstructions of long-term predictions. We apply the representation model to the first 5 images of two hold-out trajectories and predict forward for 45 ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 6: Performance comparison to existing methods. Dreamer inherits the data-efficiency of PlaNet while exceeding the asymptotic performance of the best model-free agents. After 5 ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 7: Dreamer succeeds at visual control tasks that require long-horizon credit assignment, such as the acrobot and hopper tasks. Optimizing only imagined rewards within ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | These tasks pose a variety of challenges, including sparse rewards, contact dynamics, and 3D scenes. | embodiment, simulator version and control stack | p. 8 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS) |
| Task/environment | Agent observations are images of shape 64 × 64 × 3, actions range from 1 to 12 dimensions, rewards range from 0 to 1, ... | reset, timeout, object/scene variation | p. 8 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 3 (1 INTRODUCTION), p. 6 (B Sequence length) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 11: Comparison of representation learning methods for Dreamer. The lines show mean scores and the shaded areas show the standard deviation across 5 ... | definition/direction/unit from same section | p. 18 (Figure/Table caption) |
| Figure 2. Using the same hyper parameters for all tasks, Dreamer exceeds previous model-based and model-free agents in terms of data-efficiency, computation time, and ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| With an average score of 823 across tasks after 5 × 106 environment steps, Dreamer exceeds the performance of the strong model-free D4PG agent ... | definition/direction/unit from same section | p. 9 (6 EXPERIMENTS) |
| Figure 10: Comparison of action selection schemes on the continuous control tasks of the DeepMind Control Suite from pixel inputs. The lines show mean ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |
| These tasks pose a variety of challenges, including sparse rewards, contact dynamics, and 3D scenes. | definition/direction/unit from same section | p. 8 (6 EXPERIMENTS) |
| We include the scores for D4PG with pixel inputs and A3C (Mnih et al., 2016) with state inputs from Tassa et al. | definition/direction/unit from same section | p. 8 (6 EXPERIMENTS) |
| Reward prediction alone was not sufficient in our experiments. | definition/direction/unit from same section | p. 9 (6 EXPERIMENTS) |
| Figure 4: Imagination horizons. We compare the final performance of Dreamer, learning an action model without value prediction, and online planning using PlaNet. Learning ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The training time for our Dreamer implementation is about 3 hours per 106 environment steps on the control suite, compared to 11 hours for ... | comparison identity and matched condition | p. 8 (6 EXPERIMENTS) |
| Baseline methods The highest reported performance on the continuous tasks is achieved by D4PG (Barth-Maron et al., 2018), an improved variant of DDPG (Lillicrap ... | comparison identity and matched condition | p. 8 (6 EXPERIMENTS) |
| Performance curves for all 19 tasks with horizon of 20 are shown in Appendix D, where Dreamer outperforms the alternatives on 16 of 20 ... | comparison identity and matched condition | p. 9 (6 EXPERIMENTS) |
| The empirical success of Dreamer shows that learning behaviors by latent imagination with world models can outperform top methods based on experience replay. | comparison identity and matched condition | p. 9 (6 EXPERIMENTS) |
| Figure 6: Performance comparison to existing methods. Dreamer inherits the data-efficiency of PlaNet while exceeding the asymptotic performance of the best model-free agents. After ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Figure 10: Comparison of action selection schemes on the continuous control tasks of the DeepMind Control Suite from pixel inputs. The lines show mean ... | comparison identity and matched condition | p. 17 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| PlaNet (Hafner et al., 2018) learns the same world model as Dreamer and selects actions via online planning without an action model and drastically ... | component/input/data sensitivity | p. 8 (6 EXPERIMENTS) |
| Baseline methods The highest reported performance on the continuous tasks is achieved by D4PG (Barth-Maron et al., 2018), an improved variant of DDPG (Lillicrap ... | component/input/data sensitivity | p. 8 (6 EXPERIMENTS) |
| Further ablations are included in the appendix of the paper. | component/input/data sensitivity | p. 9 (6 EXPERIMENTS) |
| For this, we learn an action model to maximize imagined rewards without a value model and compare to online planning using PlaNet. | component/input/data sensitivity | p. 9 (6 EXPERIMENTS) |
| Figure 3: Components of Dreamer. (a) From the dataset of past experience, the agent learns to encode observations and actions into compact latent states ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |
| Figure 6: Performance comparison to existing methods. Dreamer inherits the data-efficiency of PlaNet while exceeding the asymptotic performance of the best model-free agents. After ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We present Dreamer, an agent that learns long-horizon behaviors from images purely by latent imagination. | Baseline methods The highest reported performance on the continuous tasks is achieved by D4PG (Barth-Maron et al., 2018), an improved variant of DDPG (Lillicrap ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 8 (Figure/Table caption), p. 6 (Figure/Table caption), p. 16 (Figure/Table caption) |
| Primary metric/result | With an average score of 823 across tasks after 5 × 106 environment steps, Dreamer exceeds the performance of the strong model-free D4PG agent ... | numeric claim only at cited anchor | p. 9 (6 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** Agent observations are images of shape 64 × 64 × 3, actions range from 1 to 12 dimensions, rewards range from 0 to 1, episodes ...
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** The training time for our Dreamer implementation is about 3 hours per 106 environment steps on the control suite, compared to 11 hours for online ...
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** Performance curves for all 19 tasks with horizon of 20 are shown in Appendix D, where Dreamer outperforms the alternatives on 16 of 20 tasks, ...
- **p. 4 / B Sequence length - extractive body cue:** Published as a conference paper at ICLR 2020 10 20 30 40 Imagination Horizon 0 200 400 600 800 1000 Episode Return Cartpole Swingup 10 ...
- **p. 4 / B Sequence length - extractive body cue:** State values can be estimated in multiple ways that trade off bias and variance (Sutton and Barto, 2018), VR(sτ) .= Eqθ,qφ  t+H X n=τ ...
- **p. 5 / B Sequence length - extractive body cue:** We apply the representation model to the first 5 images of two hold-out trajectories and predict forward for 45 steps using the latent dynamics, given ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 2: Image observations for 5 of the 20 visual control tasks used in our experiments. The tasks pose a variety of challenges including ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | Figure 9: Performance of Dreamer in environments with discrete actions and early termination. Dreamer learns successful behaviors on this subset of Atari games and ... | p. 16 (Figure/Table caption) |
| body limitation/failure cue | Figure 4: Imagination horizons. We compare the final performance of Dreamer, learning an action model without value prediction, and online planning using PlaNet. Learning ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | Figure 12: Robustness of Dreamer to different control frequencies. Reinforcement learning methods can be sensitive to this hyper parameter, which could be amplified when ... | p. 19 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The training time for our Dreamer implementation is about 3 hours per 106 environment steps on the control suite, compared to 11 hours for ... | p. 8 (6 EXPERIMENTS) |
| We use a single Nvidia V100 GPU and 10 CPU cores for each training run. | p. 8 (6 EXPERIMENTS) |
| With an average score of 823 across tasks after 5 × 106 environment steps, Dreamer exceeds the performance of the strong model-free D4PG agent ... | p. 9 (6 EXPERIMENTS) |
| (c) The agent encodes the history of the episode to compute the current model state and predict the next action to execute in the ... | p. 3 (1 INTRODUCTION) |
| Since all steps are implemented as neural networks, we analytically compute ∇φEqθ,qφ   Pt+H τ=t Vλ(sτ)  by stochastic backpropagation (Kingma and Welling, 2013; ... | p. 5 (B Sequence length) |
| Published as a conference paper at ICLR 2020 0.0 0.5 1.0 1.5 2.0 0 100 200 300 400 Episode Return Acrobot Swingup 0.0 0.5 ... | p. 7 (B Sequence length) |
| L Imagination horizon H Learning rate α 3 | p. 3 (B Sequence length) |
| The representation model encodes observations and actions to create continuous vector-valued model states st with Markovian transitions (Watter et al., 2015; Zhang et al., ... | p. 2 (1 INTRODUCTION) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: Image observations for 5 of the 20 visual control tasks used in our experiments. The tasks pose a variety of challenges including contact ...
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 9: Performance of Dreamer in environments with discrete actions and early termination. Dreamer learns successful behaviors on this subset of Atari games and the ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4: Imagination horizons. We compare the final performance of Dreamer, learning an action model without value prediction, and online planning using PlaNet. Learning a ...
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 12: Robustness of Dreamer to different control frequencies. Reinforcement learning methods can be sensitive to this hyper parameter, which could be amplified when learning ...

- **PDF anchors reviewed:** datasets p. 8 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), metrics p. 18 (Figure/Table caption), p. 2 (Figure/Table caption), p. 9 (6 EXPERIMENTS), p. 17 (Figure/Table caption), p. 8 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS), baselines p. 8 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 6 (Figure/Table caption), p. 17 (Figure/Table caption), results p. 8 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 8 (Figure/Table caption), p. 6 (Figure/Table caption), p. 16 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
