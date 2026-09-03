# Evaluation - Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2309.10150; PDF retrieval source: https://arxiv.org/pdf/2309.10150. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5 Experiments), p. 8 (Figure/Table caption), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 18 (Figure/Table caption), p. 6 (5 Experiments)): Q-Transformer has the highest success rate and outperforms both the behavior cloning baseline (RT-1) and offline RL baselines (Decision Transformer, IQL), exceeding the average performance of the best-performing prior method ...

## Evaluation Body Digest

- **p. 6 / 5 Experiments - extractive body cue:** To evaluate how well Q-Transformer can perform when learning from real-world offline datasets while effectively incorporating autonomously collected failed episodes, we evaluate Q-Transformer on 72 ...
- **p. 8 / 5 Experiments - extractive body cue:** This experiment includes all of the data collected with 13 robots and comprises of the demonstrations used by RT-1 [1] and successful autonomous episodes, corresponding ...
- **p. 6 / 5 Experiments - extractive body cue:** 5.1 Real-world language-conditioned manipulation evaluation Training dataset.
- **p. 7 / 5 Experiments - extractive body cue:** 5.2 Benchmarking in simulation Training steps Success rate QT-Opt CQL AW-Opt IQL Q-Transformer (ours) Decision Transformer RT-1 BC Figure 5: Performance comparison on a simulated ...
- **p. 7 / 5 Experiments - extractive body cue:** As we see in Figure 6 (left), performance with softmax conservatism drops to around the fraction of demonstration episodes (∼8%).
- **p. 8 / 5 Experiments - extractive body cue:** Bottom Right: Success rates on real world task categories with a larger dataset.
- **p. 7 / 5 Experiments - extractive body cue:** Q-Transformer has the highest success rate and outperforms both the behavior cloning baseline (RT-1) and offline RL baselines (Decision Transformer, IQL), exceeding the average performance ...
- **p. 8 / 5 Experiments - extractive body cue:** Training steps Success rate Q-Transformer with softmax Q-Transformer without conservatism Q-Transformer (ours) Q-Transformer without Monte-Carlo n-step ablation n-step 1-step 1-step # of gradient steps 137480 ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** offline robot transition/trajectory dataset과 deployment MDP.
- **Input boundary:** dataset state/observation, action, reward와 return-to-go.
- **Output/decision under evaluation:** dataset-supported action sequence.
- **Primary target:** offline policy value, OOD safety와 closed-loop success.
- **Detected evaluation headings:** 5 Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Q-Transformer has the highest success rate and outperforms both the behavior cloning baseline (RT-1) and offline RL baselines (Decision Transformer, IQL), exceeding the average ... | p. 7 (5 Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 6: Left: Ablations: changing to softmax conservatism decreases performance. Removing MC returns or conservatism completely collapse performance. Top Right: The n-step return ver- ... | p. 8 (Figure/Table caption) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | 5.2 Benchmarking in simulation Training steps Success rate QT-Opt CQL AW-Opt IQL Q-Transformer (ours) Decision Transformer RT-1 BC Figure 5: Performance comparison on a ... | p. 7 (5 Experiments) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Training steps Success rate Q-Transformer with softmax Q-Transformer without conservatism Q-Transformer (ours) Q-Transformer without Monte-Carlo n-step ablation n-step 1-step 1-step # of gradient steps ... | p. 8 (5 Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 7: Mean and variance of Q-Transformer and RT-1 performance in simulation when running the training for 5 different random seeds. In addition to ... | p. 18 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 5 Experiments - extractive body cue:** To evaluate how well Q-Transformer can perform when learning from real-world offline datasets while effectively incorporating autonomously collected failed episodes, we evaluate Q-Transformer on 72 ...
- **p. 8 / 5 Experiments - extractive body cue:** This experiment includes all of the data collected with 13 robots and comprises of the demonstrations used by RT-1 [1] and successful autonomous episodes, corresponding ...
- **p. 6 / 5 Experiments - extractive body cue:** 5.1 Real-world language-conditioned manipulation evaluation Training dataset.
- **p. 7 / 5 Experiments - extractive body cue:** 5.2 Benchmarking in simulation Training steps Success rate QT-Opt CQL AW-Opt IQL Q-Transformer (ours) Decision Transformer RT-1 BC Figure 5: Performance comparison on a simulated ...
- **p. 7 / 5 Experiments - extractive body cue:** As we see in Figure 6 (left), performance with softmax conservatism drops to around the fraction of demonstration episodes (∼8%).
- **p. 8 / 5 Experiments - extractive body cue:** Bottom Right: Success rates on real world task categories with a larger dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Q-Transformer enables training high- capacity sequential architectures on mixed qual- ity data. Our policies are able to improve upon human demonstrations and execute ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Q-values update for each action dimension at timestep t. Given a history of states, we update the Q-values of all bins in all ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: Q-Transformer network architecture, as applied to our multi-task language-conditioned robotic control setting. The encoding of the observations is concatenated with embeddings of the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Left: Real world manipulation tasks. Right: Real world performance comparison. RT-1 [1] is imitation learning on demonstrations. Q-Transformer (Q-T), Decision Transformer (DT) [32], ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Performance comparison on a simulated picking task. In this section, we evaluate Q-Transformer on a challenging simulated offline RL task that re- quire ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: Left: Ablations: changing to softmax conservatism decreases performance. Removing MC returns or conservatism completely collapse performance. Top Right: The n-step return ver- sion ...
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 7: Mean and variance of Q-Transformer and RT-1 performance in simulation when running the training for 5 different random seeds. In addition to performing ...
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 8: Qualitative comparisons of Q-values from QT-Opt (sim-to-real) and Q-Transformer. Q- Transformer outputs sharper Q-values for objects close to the robot, which can be ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To evaluate how well Q-Transformer can perform when learning from real-world offline datasets while effectively incorporating autonomously collected failed episodes, we evaluate Q-Transformer on ... | embodiment, simulator version and control stack | p. 6 (5 Experiments), p. 8 (5 Experiments) |
| Task/environment | This experiment includes all of the data collected with 13 robots and comprises of the demonstrations used by RT-1 [1] and successful autonomous episodes, ... | reset, timeout, object/scene variation | p. 8 (5 Experiments), p. 6 (5 Experiments) |
| Observation/sensor | dataset state/observation, action, reward와 return-to-go | calibration, preprocessing, privileged input | p. 4 (3 Background), p. 4 (3 Background) |
| Output/decision | dataset-supported action sequence | action frame, controller and termination | p. 6 (3 Background), p. 3 (3 Background) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 5.2 Benchmarking in simulation Training steps Success rate QT-Opt CQL AW-Opt IQL Q-Transformer (ours) Decision Transformer RT-1 BC Figure 5: Performance comparison on a ... | definition/direction/unit from same section | p. 7 (5 Experiments) |
| Q-Transformer has the highest success rate and outperforms both the behavior cloning baseline (RT-1) and offline RL baselines (Decision Transformer, IQL), exceeding the average ... | definition/direction/unit from same section | p. 7 (5 Experiments) |
| Training steps Success rate Q-Transformer with softmax Q-Transformer without conservatism Q-Transformer (ours) Q-Transformer without Monte-Carlo n-step ablation n-step 1-step 1-step # of gradient steps ... | definition/direction/unit from same section | p. 8 (5 Experiments) |
| Figure 6: Left: Ablations: changing to softmax conservatism decreases performance. Removing MC returns or conservatism completely collapse performance. Top Right: The n-step return ver- ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| As such, the average success rate in Table 4 is the average over 72 tasks. | definition/direction/unit from same section | p. 6 (5 Experiments) |
| Table 1: Affordance estimation comparison: precision, recall and F1 score when using Q-values to determine if a task is feasible. Q-Transformer (Q-T) with multi- ... | definition/direction/unit from same section | p. 19 (Figure/Table caption) |
| Figure 2: Q-values update for each action dimension at timestep t. Given a history of states, we update the Q-values of all bins in ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| All of these demonstrations succeed on their respective tasks and receive a reward of 1.0. | definition/direction/unit from same section | p. 6 (5 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Q-Transformer has the highest success rate and outperforms both the behavior cloning baseline (RT-1) and offline RL baselines (Decision Transformer, IQL), exceeding the average ... | comparison identity and matched condition | p. 7 (5 Experiments) |
| To ensure a fair comparison between Q-Transformer and imitation learning methods, we discard all successful episodes in the autonomously collected data when we train ... | comparison identity and matched condition | p. 6 (5 Experiments) |
| Q-Transformer outperforms prior methods for planning and executing long-horizon tasks. | comparison identity and matched condition | p. 7 (5 Experiments) |
| This experiment demonstrates that Q-Transformer can continue to scale to extremely large dataset sizes, and continues to outperform both imitation learning with RT-1 and ... | comparison identity and matched condition | p. 8 (5 Experiments) |
| Top Right: The n-step return version of our method reaches similar performance to the standard version with 4 times fewer steps, indicating that the ... | comparison identity and matched condition | p. 8 (5 Experiments) |
| Table 2: Performance on SayCan style long-horizon tasks: SayCan queries Q(s, a) in planning to pick a language instruction, then runs a policy to ... | comparison identity and matched condition | p. 19 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Training steps Success rate Q-Transformer with softmax Q-Transformer without conservatism Q-Transformer (ours) Q-Transformer without Monte-Carlo n-step ablation n-step 1-step 1-step # of gradient steps ... | component/input/data sensitivity | p. 8 (5 Experiments) |
| 5.3 Ablations We perform a series of ablations of our method design choices in simulation, with results presented in Figure 6 (left). | component/input/data sensitivity | p. 7 (5 Experiments) |
| Figure 6: Left: Ablations: changing to softmax conservatism decreases performance. Removing MC returns or conservatism completely collapse performance. Top Right: The n-step return ver- ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| When removing conservatism entirely, we observe that performance collapses. | component/input/data sensitivity | p. 7 (5 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We propose a specific regularizer that minimizes values of every action that was not taken in the dataset and show that our method can ... | Q-Transformer has the highest success rate and outperforms both the behavior cloning baseline (RT-1) and offline RL baselines (Decision Transformer, IQL), exceeding the average ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5 Experiments), p. 8 (Figure/Table caption), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 18 (Figure/Table caption), p. 6 (5 Experiments) |
| Primary metric/result | Figure 6: Left: Ablations: changing to softmax conservatism decreases performance. Removing MC returns or conservatism completely collapse performance. Top Right: The n-step return ver- ... | numeric claim only at cited anchor | p. 8 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / 5 Experiments - extractive body cue:** The offline data used in our experiments was collected with a fleet of 13 robots, and consists of a subset of the demonstration data described ...
- **p. 6 / 5 Experiments - extractive body cue:** This leaves us with about 20,000 additional autonomously collected failed episodes, each with a reward of 0.0, for a dataset size of about 58,000 episodes.
- **p. 6 / 5 Experiments - extractive body cue:** As such, the average success rate in Table 4 is the average over 72 tasks.
- **p. 8 / 5 Experiments - extractive body cue:** This experiment includes all of the data collected with 13 robots and comprises of the demonstrations used by RT-1 [1] and successful autonomous episodes, corresponding ...
- **p. 2 / 1 Introduction - extractive body cue:** Our real-world experiments utilize a dataset with 38,000 successful demonstrations and 20,000 failed autonomously collected episodes on more than 700 tasks, gathered with a fleet ...
- **p. 4 / 3 Background - extractive body cue:** FiLM EfficientNet + Transformer Positional encoding Universal Sentence Encoder Self-Attention Layers (8x) Camera images Language instruction Pick sponge… Q-values for each action bin One-hot action ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | First, we focus on sparse binary reward tasks corresponding to success or failure for each trial. | p. 8 (5 Experiments) |
| body limitation/failure cue | Our framework does have several limitations. | p. 8 (5 Experiments) |
| body limitation/failure cue | Although this does not change convergence, including this maximization speeds up learning (see Section 5.3). | p. 6 (3 Background) |
| body limitation/failure cue | To ensure a fair comparison between Q-Transformer and imitation learning methods, we discard all successful episodes in the autonomously collected data when we train ... | p. 6 (5 Experiments) |
| body limitation/failure cue | Decision Transformer is trained on both demonstrations and sub-optimal data, but is not able to leverage the noisy data for policy improvement and does ... | p. 7 (5 Experiments) |
| body limitation/failure cue | The demonstrations are replayed with noise to generate more trajectories (∼92% of the data). | p. 7 (5 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Second, the per-dimension action discretization scheme that we employ may become more cumbersome in higher dimensions (e.g., controlling a humanoid robot), as the sequence ... | p. 8 (5 Experiments) |
| The episodes are on average 35 time steps in length. | p. 6 (5 Experiments) |
| To ensure a fair comparison between Q-Transformer and imitation learning methods, we discard all successful episodes in the autonomously collected data when we train ... | p. 6 (5 Experiments) |
| We also analyze the statistical significance of the results by training with multiple random seeds in Appendix F. | p. 7 (5 Experiments) |
| 5.2 Benchmarking in simulation Training steps Success rate QT-Opt CQL AW-Opt IQL Q-Transformer (ours) Decision Transformer RT-1 BC Figure 5: Performance comparison on a ... | p. 7 (5 Experiments) |
| First, we focus on sparse binary reward tasks corresponding to success or failure for each trial. | p. 8 (5 Experiments) |
| First, we would like robotic systems that are more proficient than human teleoperators, exploiting the full potential of the hardware to perform tasks quickly, ... | p. 1 (1 Introduction) |
| The language instruction is encoded with Universal Sentence Encoder [68] and then fed to FiLM EfficientNet [69, 70] network together with the robot camera ... | p. 4 (3 Background) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5 Experiments - extractive body cue:** First, we focus on sparse binary reward tasks corresponding to success or failure for each trial.
- **p. 8 / 5 Experiments - extractive body cue:** Our framework does have several limitations.
- **p. 6 / 3 Background - extractive body cue:** Although this does not change convergence, including this maximization speeds up learning (see Section 5.3).
- **p. 6 / 5 Experiments - extractive body cue:** To ensure a fair comparison between Q-Transformer and imitation learning methods, we discard all successful episodes in the autonomously collected data when we train our ...
- **p. 7 / 5 Experiments - extractive body cue:** Decision Transformer is trained on both demonstrations and sub-optimal data, but is not able to leverage the noisy data for policy improvement and does not ...
- **p. 7 / 5 Experiments - extractive body cue:** The demonstrations are replayed with noise to generate more trajectories (∼92% of the data).

- **Evidence anchors reviewed:** datasets p. 6 (5 Experiments), p. 8 (5 Experiments), p. 6 (5 Experiments), p. 7 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments), metrics p. 7 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 8 (Figure/Table caption), p. 6 (5 Experiments), p. 19 (Figure/Table caption), baselines p. 7 (5 Experiments), p. 6 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 8 (5 Experiments), p. 19 (Figure/Table caption), results p. 7 (5 Experiments), p. 8 (Figure/Table caption), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 18 (Figure/Table caption), p. 6 (5 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (20 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Training steps Success rate Q-Transformer with softmax Q-Transformer without conservatism Q-Transformer (ours) Q-Transformer without Monte-Carlo n-step ablation n-step 1-step 1-step # of gradient steps 137480 582960 136920 Training dura ... (p. 8, 5 Experiments).
- **Metric evidence:** Q-Transformer has the highest success rate and outperforms both the behavior cloning baseline (RT-1) and offline RL baselines (Decision Transformer, IQL), exceeding the average performance of the best-performing prior method ... (p. 7, 5 Experiments).
- **Baseline/ablation evidence:** To ensure a fair comparison between Q-Transformer and imitation learning methods, we discard all successful episodes in the autonomously collected data when we train our method, to ensure that by ... (p. 6, 5 Experiments).
- **Failure/negative evidence:** This leaves us with about 20,000 additional autonomously collected failed episodes, each with a reward of 0.0, for a dataset size of about 58,000 episodes. (p. 6, 5 Experiments).
