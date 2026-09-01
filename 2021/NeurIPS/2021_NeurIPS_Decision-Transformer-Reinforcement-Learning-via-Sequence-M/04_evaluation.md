# Evaluation - Decision Transformer: Reinforcement Learning via Sequence Modeling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2106.01345; PDF retrieval source: https://arxiv.org/pdf/2106.01345. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 21 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 11 (Dataset), p. 10 (Dataset)): Table 3: Comparison between Decision Transformer (DT) and Percentile Behavior Cloning (%BC). In contrast, when we study low data regimes - such as Atari, where we use 1% of a ...

## Evaluation Body Digest

- **p. 10 / Dataset - extractive body cue:** To evaluate this, we consider a delayed return version of the D4RL benchmarks where the agent does not receive any rewards along the trajectory, and ...
- **p. 10 / Dataset - extractive body cue:** Delayed (Sparse) Agnostic Original (Dense) Dataset Environment DT (Ours) CQL BC %BC DT (Ours) CQL Medium-Expert Hopper 107.3 ± 3.5 9.0 59.9 102.6 107.6 111.0 ...
- **p. 11 / Dataset - extractive body cue:** Offline RL and the ability to model behaviors has the potential to enable sample-efficient online RL for downstream tasks.
- **p. 11 / Dataset - extractive body cue:** Since Decision Transformer does not require explicit optimization using learned functions as objectives, it avoids the need for regularization or conservatism.
- **p. 10 / Figure/Table caption - extractive body cue:** Table 6: Success rate for Key-to-Door environment. Methods using hindsight (Decision Transformer, %BC) can learn successful policies, while TD learning struggles to perform credit assignment. ...
- **p. 10 / Dataset - extractive body cue:** DT (Ours) CQL BC %BC Random 1K Random Trajectories 71.8% 13.1% 1.4% 69.9% 3.1% 10K Random Trajectories 94.6% 13.3% 1.6% 95.1% 3.1% Table 6: Success ...
- **p. 21 / Figure/Table caption - extractive body cue:** Table 12: Raw scores for the 1% DQN-replay Atari dataset. We report the mean and variance across 3 seeds. Best mean scores are highlighted in ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4: %BC scores for Atari. We report the mean and variance across 3 seeds. Decision Transformer (DT) outperforms all versions of %BC in most ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** robot/environment의 sequential decision process.
- **Input boundary:** state 또는 observation, action, reward와 transition history.
- **Output/decision under evaluation:** action policy와 induced trajectory.
- **Primary target:** expected return, task success, stability와 sample efficiency.
- **Detected evaluation headings:** Dataset (p. 10); A Experimental Details (p. 18); 90 Breakout (≈1× max in dataset) (p. 18); 20 Pong (≈1× max in dataset) (p. 18).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 3: Comparison between Decision Transformer (DT) and Percentile Behavior Cloning (%BC). In contrast, when we study low data regimes - such as Atari, ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 12: Raw scores for the 1% DQN-replay Atari dataset. We report the mean and variance across 3 seeds. Best mean scores are highlighted ... | p. 21 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 2: Results for D4RL datasets3. We report the mean and variance for three seeds. Decision Transformer (DT) outperforms conventional RL algorithms on almost ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 4: %BC scores for Atari. We report the mean and variance across 3 seeds. Decision Transformer (DT) outperforms all versions of %BC in ... | p. 8 (Figure/Table caption) |
| Dataset | SYSTEM / EVALUATION SCOPE UNRESOLVED | One key difference between Decision Transformer and prior offline RL algorithms is that we do not require policy regularization or conservatism to achieve good ... | p. 11 (Dataset) |

## Dataset / Benchmark Role

- **p. 10 / Dataset - extractive body cue:** To evaluate this, we consider a delayed return version of the D4RL benchmarks where the agent does not receive any rewards along the trajectory, and ...
- **p. 10 / Dataset - extractive body cue:** Delayed (Sparse) Agnostic Original (Dense) Dataset Environment DT (Ours) CQL BC %BC DT (Ours) CQL Medium-Expert Hopper 107.3 ± 3.5 9.0 59.9 102.6 107.6 111.0 ...
- **p. 11 / Dataset - extractive body cue:** Offline RL and the ability to model behaviors has the potential to enable sample-efficient online RL for downstream tasks.
- **p. 11 / Dataset - extractive body cue:** Since Decision Transformer does not require explicit optimization using learned functions as objectives, it avoids the need for regularization or conservatism.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Decision Transformer architecture1. States, actions, and returns are fed into modality- specific linear embeddings and a positional episodic timestep encoding is added. Tokens ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Illustrative example of finding shortest path for a fixed graph (left) posed as reinforcement learning. Training dataset consists of random walk trajectories and ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Results comparing Decision Transformer (ours) to TD learning (CQL) and behavior cloning across Atari, OpenAI Gym, and Minigrid. On a diverse set of ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Gamer-normalized scores for the 1% DQN-replay Atari dataset. We report the mean and variance across 3 seeds. Best mean scores are highlighted in ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Results for D4RL datasets3. We report the mean and variance for three seeds. Decision Transformer (DT) outperforms conventional RL algorithms on almost all ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Comparison between Decision Transformer (DT) and Percentile Behavior Cloning (%BC). In contrast, when we study low data regimes - such as Atari, where ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4: %BC scores for Atari. We report the mean and variance across 3 seeds. Decision Transformer (DT) outperforms all versions of %BC in most ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4: Sampled (evaluation) returns accumulated by Decision Transformer when conditioned on the specified target (desired) returns. Top: Atari. Bottom: D4RL medium-replay datasets. 5.3 What ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To evaluate this, we consider a delayed return version of the D4RL benchmarks where the agent does not receive any rewards along the trajectory, ... | embodiment, simulator version and control stack | p. 10 (Dataset), p. 10 (Dataset) |
| Task/environment | Delayed (Sparse) Agnostic Original (Dense) Dataset Environment DT (Ours) CQL BC %BC DT (Ours) CQL Medium-Expert Hopper 107.3 ± 3.5 9.0 59.9 102.6 107.6 ... | reset, timeout, object/scene variation | p. 10 (Dataset), p. 11 (Dataset) |
| Observation/sensor | state 또는 observation, action, reward와 transition history | calibration, preprocessing, privileged input | p. 3 (1 Introduction), p. 4 (2 Preliminaries) |
| Output/decision | action policy와 induced trajectory | action frame, controller and termination | p. 4 (2 Preliminaries), p. 5 (3 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 6: Success rate for Key-to-Door environment. Methods using hindsight (Decision Transformer, %BC) can learn successful policies, while TD learning struggles to perform credit ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| DT (Ours) CQL BC %BC Random 1K Random Trajectories 71.8% 13.1% 1.4% 69.9% 3.1% 10K Random Trajectories 94.6% 13.3% 1.6% 95.1% 3.1% Table 6: ... | definition/direction/unit from same section | p. 10 (Dataset) |
| Table 12: Raw scores for the 1% DQN-replay Atari dataset. We report the mean and variance across 3 seeds. Best mean scores are highlighted ... | definition/direction/unit from same section | p. 21 (Figure/Table caption) |
| Table 4: %BC scores for Atari. We report the mean and variance across 3 seeds. Decision Transformer (DT) outperforms all versions of %BC in ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Table 11: Atari baseline scores used for normalization. 20 | definition/direction/unit from same section | p. 20 (Figure/Table caption) |
| Figure 3: Results comparing Decision Transformer (ours) to TD learning (CQL) and behavior cloning across Atari, OpenAI Gym, and Minigrid. On a diverse set ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Figure 4: Sampled (evaluation) returns accumulated by Decision Transformer when conditioned on the specified target (desired) returns. Top: Atari. Bottom: D4RL medium-replay datasets. 5.3 ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Figure 6: Histogram of steps to reach the goal node for random walks on the graph, shortest possible paths to the goal, and attempted ... | definition/direction/unit from same section | p. 20 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 2: Results for D4RL datasets3. We report the mean and variance for three seeds. Decision Transformer (DT) outperforms conventional RL algorithms on almost ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Table 1: Gamer-normalized scores for the 1% DQN-replay Atari dataset. We report the mean and variance across 3 seeds. Best mean scores are highlighted ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Table 3: Comparison between Decision Transformer (DT) and Percentile Behavior Cloning (%BC). In contrast, when we study low data regimes - such as Atari, ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Figure 6: Histogram of steps to reach the goal node for random walks on the graph, shortest possible paths to the goal, and attempted ... | comparison identity and matched condition | p. 20 (Figure/Table caption) |
| Table 4: %BC scores for Atari. We report the mean and variance across 3 seeds. Decision Transformer (DT) outperforms all versions of %BC in ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Table 11: Atari baseline scores used for normalization. 20 | comparison identity and matched condition | p. 20 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 5: Ablation on context length. Decision Transformer (DT) performs better when using a longer context length (K = 50 for Pong, K = ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| Table 3: Comparison between Decision Transformer (DT) and Percentile Behavior Cloning (%BC). In contrast, when we study low data regimes - such as Atari, ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Training dataset consists of random walk trajectories and their per-node returns-to-go (middle). | Table 3: Comparison between Decision Transformer (DT) and Percentile Behavior Cloning (%BC). In contrast, when we study low data regimes - such as Atari, ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 21 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 11 (Dataset), p. 10 (Dataset) |
| Primary metric/result | Table 12: Raw scores for the 1% DQN-replay Atari dataset. We report the mean and variance across 3 seeds. Best mean scores are highlighted ... | numeric claim only at cited anchor | p. 21 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 10 / Dataset - extractive body cue:** Delayed (Sparse) Agnostic Original (Dense) Dataset Environment DT (Ours) CQL BC %BC DT (Ours) CQL Medium-Expert Hopper 107.3 ± 3.5 9.0 59.9 102.6 107.6 111.0 ...
- **p. 6 / 3 Method - extractive body cue:** [13], representing 500 thousand of the 50 million transitions observed by an online DQN agent [20] during training; we report the mean and standard deviation ...
- **p. 7 / 3 Method - extractive body cue:** Game DT (Ours) CQL QR-DQN REM BC Breakout 267.5 ± 97.5 211.1 17.1 8.9 138.9 ± 61.7 Qbert 15.4 ± 11.4 104.2 0.0 0.0 17.3 ...
- **p. 7 / 3 Method - extractive body cue:** We report the mean and variance across 3 seeds.
- **p. 7 / 3 Method - extractive body cue:** Dataset Environment DT (Ours) CQL BEAR BRAC-v AWR BC Medium-Expert HalfCheetah 86.8 ± 1.3 62.4 53.4 41.9 52.7 59.9 Medium-Expert Hopper 107.6 ± 1.8 111.0 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | TD learning (CQL) cannot effectively propagate Q-values over the long horizons involved and gets poor performance. | p. 9 (5 Discussion) |
| body limitation/failure cue | This act of optimizing a learned function can exacerbate and exploit any inaccuracies in the value function approximation, causing failures in policy improvement. | p. 11 (Dataset) |
| body limitation/failure cue | Transformer models can also be used to model the state evolution of trajectory, potentially serving as an alternative to model-based RL, and we hope ... | p. 12 (7 Conclusion) |
| body limitation/failure cue | Decision Transformer (DT) and imitation learning are minimally affected by the removal of dense rewards, while CQL fails. | p. 10 (Dataset) |
| body limitation/failure cue | To evaluate this, we consider a delayed return version of the D4RL benchmarks where the agent does not receive any rewards along the trajectory, ... | p. 10 (Dataset) |
| body limitation/failure cue | Since Decision Transformer does not require explicit optimization using learned functions as objectives, it avoids the need for regularization or conservatism. | p. 11 (Dataset) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For environments with visual inputs, the state is fed into a convolutional encoder instead of a linear layer. | p. 5 (3 Method) |
| We feed the last K timesteps into Decision Transformer, for a total of 3K tokens (one for each modality: return-to-go, state, or action). | p. 5 (3 Method) |
| [13], representing 500 thousand of the 50 million transitions observed by an online DQN agent [20] during training; we report the mean and standard ... | p. 6 (3 Method) |
| We also report the performance of behavior cloning (BC), which utilizes the same network architecture and hyperparameters as Decision Transformer but does not have ... | p. 6 (3 Method) |
| We report the mean and variance across 3 seeds. | p. 7 (3 Method) |
| 3Given that CQL is generally the strongest TD learning method, for Reacher we only run the CQL baseline. | p. 7 (3 Method) |
| Right: Transformer attention weights from all timesteps superimposed for a particular successful episode. | p. 10 (Dataset) |
| The model attends to steps near pivotal events in the episode, such as picking up the key and reaching the door. | p. 10 (Dataset) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 5 Discussion - extractive body cue:** TD learning (CQL) cannot effectively propagate Q-values over the long horizons involved and gets poor performance.
- **p. 11 / Dataset - extractive body cue:** This act of optimizing a learned function can exacerbate and exploit any inaccuracies in the value function approximation, causing failures in policy improvement.
- **p. 12 / 7 Conclusion - extractive body cue:** Transformer models can also be used to model the state evolution of trajectory, potentially serving as an alternative to model-based RL, and we hope to ...
- **p. 10 / Dataset - extractive body cue:** Decision Transformer (DT) and imitation learning are minimally affected by the removal of dense rewards, while CQL fails.
- **p. 10 / Dataset - extractive body cue:** To evaluate this, we consider a delayed return version of the D4RL benchmarks where the agent does not receive any rewards along the trajectory, and ...
- **p. 11 / Dataset - extractive body cue:** Since Decision Transformer does not require explicit optimization using learned functions as objectives, it avoids the need for regularization or conservatism.

- **PDF anchors reviewed:** datasets p. 10 (Dataset), p. 10 (Dataset), p. 11 (Dataset), p. 11 (Dataset), metrics p. 10 (Figure/Table caption), p. 10 (Dataset), p. 21 (Figure/Table caption), p. 8 (Figure/Table caption), p. 20 (Figure/Table caption), p. 6 (Figure/Table caption), baselines p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 20 (Figure/Table caption), p. 8 (Figure/Table caption), p. 20 (Figure/Table caption), results p. 8 (Figure/Table caption), p. 21 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 11 (Dataset), p. 10 (Dataset).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
