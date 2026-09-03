# Evaluation - Offline Reinforcement Learning with Implicit Q-Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=68n2s9ZJWF8; PDF retrieval source: https://arxiv.org/pdf/2110.06169. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (Figure/Table caption), p. 9 (3 PRELIMINARIES), p. 8 (Figure/Table caption), p. 5 (3 PRELIMINARIES), p. 6 (3 PRELIMINARIES), p. 7 (3 PRELIMINARIES)): Table 2: Online finetuning results showing the initial perfor- mance after offline RL, and performance after 1M steps of on- line RL. In all tasks, IQL is able to finetune ...

## Evaluation Body Digest

- **p. 7 / 3 PRELIMINARIES - extractive body cue:** We will then compare IQL with state-of-theart single-step and multi-step algorithms on the D4RL (Fu et al., 2020) benchmark tasks, studying the degree to which ...
- **p. 7 / 3 PRELIMINARIES - extractive body cue:** The MuJoCo tasks in D4RL consist of the Gym locomotion tasks, the Ant Maze tasks, and the Adroit and Kitchen robotic manipulation environments.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** (4) Our algorithm, implicit Q-Learning (IQL), aims to estimate this objective while evaluating the Qfunction only on the state-action pairs in the dataset.
- **p. 5 / 3 PRELIMINARIES - extractive body cue:** (6) Note that these losses do not use any explicit policy, and only utilize actions from the dataset for both objectives, similarly to SARSA-style policy ...
- **p. 8 / 3 PRELIMINARIES - extractive body cue:** However, these tasks include a significant fraction of near-optimal trajectories in the dataset.
- **p. 9 / 3 PRELIMINARIES - extractive body cue:** We obtained results for "-v2" datasets using an author-suggested implementation.4 On the Gym locomotion tasks (halfcheetah, hopper, walker2d), we find that IQL performs comparably to ...
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** This avoids any issues with out-ofdistribution actions, since the TD loss only uses dataset actions.
- **p. 6 / 3 PRELIMINARIES - extractive body cue:** 4.4 ANALYSIS In this section, we will show that IQL can recover the optimal value function under the dataset support constraints.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** offline robot transition/trajectory dataset과 deployment MDP.
- **Input boundary:** dataset state/observation, action, reward와 return-to-go.
- **Output/decision under evaluation:** dataset-supported action sequence.
- **Primary target:** offline policy value, OOD safety와 closed-loop success.
- **Detected evaluation headings:** B EXPERIMENTAL DETAILS (p. 12); C FINETUNING EXPERIMENTAL DETAILS (p. 13).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 2: Online finetuning results showing the initial perfor- mance after offline RL, and performance after 1M steps of on- line RL. In all ... | p. 9 (Figure/Table caption) |
| 3 PRELIMINARIES | SYSTEM / EVALUATION SCOPE UNRESOLVED | On the Ant Maze domains, IQL significantly outperforms both prior methods after online finetuning. | p. 9 (3 PRELIMINARIES) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 1: Averaged normalized scores on MuJoCo locomotion and Ant Maze tasks. Our method outperforms prior methods on the challenging Ant Maze tasks, which ... | p. 8 (Figure/Table caption) |
| 3 PRELIMINARIES | SYSTEM / EVALUATION SCOPE UNRESOLVED | Therefore, a large target value might not necessarily reflect the existence of a single action that achieves that value, but rather a "lucky" sample ... | p. 5 (3 PRELIMINARIES) |
| 3 PRELIMINARIES | SYSTEM / EVALUATION SCOPE UNRESOLVED | The proof follows the policy improvement proof (Sutton & Barto, 2018). | p. 6 (3 PRELIMINARIES) |

## Dataset / Benchmark Role

- **p. 7 / 3 PRELIMINARIES - extractive body cue:** We will then compare IQL with state-of-theart single-step and multi-step algorithms on the D4RL (Fu et al., 2020) benchmark tasks, studying the degree to which ...
- **p. 7 / 3 PRELIMINARIES - extractive body cue:** The MuJoCo tasks in D4RL consist of the Gym locomotion tasks, the Ant Maze tasks, and the Adroit and Kitchen robotic manipulation environments.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** (4) Our algorithm, implicit Q-Learning (IQL), aims to estimate this objective while evaluating the Qfunction only on the state-action pairs in the dataset.
- **p. 5 / 3 PRELIMINARIES - extractive body cue:** (6) Note that these losses do not use any explicit policy, and only utilize actions from the dataset for both objectives, similarly to SARSA-style policy ...
- **p. 8 / 3 PRELIMINARIES - extractive body cue:** However, these tasks include a significant fraction of near-optimal trajectories in the dataset.
- **p. 9 / 3 PRELIMINARIES - extractive body cue:** We obtained results for "-v2" datasets using an author-suggested implementation.4 On the Gym locomotion tasks (halfcheetah, hopper, walker2d), we find that IQL performs comparably to ...
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** This avoids any issues with out-ofdistribution actions, since the TD loss only uses dataset actions.
- **p. 6 / 3 PRELIMINARIES - extractive body cue:** 4.4 ANALYSIS In this section, we will show that IQL can recover the optimal value function under the dataset support constraints.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 5 / Figure/Table caption - extractive body cue:** Figure 1: Left: The asymmetric squared loss used for expectile regression. τ = 0.5 corresponds to the standard mean squared error loss, while τ = ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 2: Evaluation of our algorithm on a toy umaze environment (a). When the static dataset is heavily corrupted by suboptimal actions, one-step policy evaluation ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Averaged normalized scores on MuJoCo locomotion and Ant Maze tasks. Our method outperforms prior methods on the challenging Ant Maze tasks, which require ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 3: Estimating a larger expectile τ is crucial for antmaze tasks that require dynamical program- ming ('stitching'). Comparisons and baselines. We compare to methods ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Online finetuning results showing the initial perfor- mance after offline RL, and performance after 1M steps of on- line RL. In all tasks, ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 3: Evaluation on Franca Kitchen and Adroit tasks from D4RL

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We will then compare IQL with state-of-theart single-step and multi-step algorithms on the D4RL (Fu et al., 2020) benchmark tasks, studying the degree to ... | embodiment, simulator version and control stack | p. 7 (3 PRELIMINARIES), p. 7 (3 PRELIMINARIES) |
| Task/environment | The MuJoCo tasks in D4RL consist of the Gym locomotion tasks, the Ant Maze tasks, and the Adroit and Kitchen robotic manipulation environments. | reset, timeout, object/scene variation | p. 7 (3 PRELIMINARIES), p. 4 (3 PRELIMINARIES) |
| Observation/sensor | dataset state/observation, action, reward와 return-to-go | calibration, preprocessing, privileged input | p. 3 (3 PRELIMINARIES), p. 7 (3 PRELIMINARIES) |
| Output/decision | dataset-supported action sequence | action frame, controller and termination | p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 1.0 0.5 0.0 0.5 1.0 u 0.0 0.2 0.4 0.6 0.8 1.0 / (u < 0)/u2 = 0.01 = 0.1 = 0.5 = 0.9 ... | definition/direction/unit from same section | p. 5 (3 PRELIMINARIES) |
| The agent receives a reward of 10 for entering the goal state and zero reward for all other transitions. | definition/direction/unit from same section | p. 7 (3 PRELIMINARIES) |
| When the static dataset is heavily corrupted by suboptimal actions, one-step policy evaluation results in a value function that degrades to zero far from ... | definition/direction/unit from same section | p. 7 (3 PRELIMINARIES) |
| Table 1: Averaged normalized scores on MuJoCo locomotion and Ant Maze tasks. Our method outperforms prior methods on the challenging Ant Maze tasks, which ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Because of this fix, our reported CQL scores are higher than all other prior methods. | definition/direction/unit from same section | p. 9 (3 PRELIMINARIES) |
| CQL attains the second best score, while AWAC performs comparatively worse due to much weaker offline initialization. | definition/direction/unit from same section | p. 9 (3 PRELIMINARIES) |
| We resolve this by introducing a separate value function that approximates an expectile only with respect to the action distribution, leading to the following ... | definition/direction/unit from same section | p. 5 (3 PRELIMINARIES) |
| The quantile regression loss is defined as an asymmetric ℓ1 loss. | definition/direction/unit from same section | p. 4 (3 PRELIMINARIES) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 3: Estimating a larger expectile τ is crucial for antmaze tasks that require dynamical program- ming ('stitching'). Comparisons and baselines. We compare to ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Our method outperforms prior methods on the challenging Ant Maze tasks, which require dynamic programming, and is competitive with the best prior methods on ... | comparison identity and matched condition | p. 8 (3 PRELIMINARIES) |
| Our approach is also computationally faster than the baselines (see Table 1). | comparison identity and matched condition | p. 9 (3 PRELIMINARIES) |
| On the Ant Maze domains, IQL significantly outperforms both prior methods after online finetuning. | comparison identity and matched condition | p. 9 (3 PRELIMINARIES) |
| Prior work (Brandfonbrener et al., 2021; Peng et al., 2019) has proposed directly using this objective to learn Qπβ, and then train the policy ... | comparison identity and matched condition | p. 4 (3 PRELIMINARIES) |
| 2Our method could also be derived with quantiles, but since we are not interested in learning all of the expectiles/quantiles, unlike prior work (Dabney ... | comparison identity and matched condition | p. 4 (3 PRELIMINARIES) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Crucially, we will show that it is possible to do this without ever querying the learned Q-function on out-of-sample actions by utilizing expectile regression. | component/input/data sensitivity | p. 4 (3 PRELIMINARIES) |
| IQL is well-suited for online fine-tuning for two reasons. | component/input/data sensitivity | p. 9 (3 PRELIMINARIES) |
| 5.3 ONLINE FINE-TUNING AFTER OFFLINE RL Dataset AWAC CQL IQL (Ours) antmaze-umaze-v0 56.7 →59.0 70.1 →99.4 86.7 →96.0 antmaze-umaze-diverse-v0 49.3 →49.0 31.1 →99.4 75.0 ... | component/input/data sensitivity | p. 9 (3 PRELIMINARIES) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We propose a new offline RL method that never needs to evaluate actions outside of the dataset, but still enables the learned policy to ... | Table 2: Online finetuning results showing the initial perfor- mance after offline RL, and performance after 1M steps of on- line RL. In all ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (Figure/Table caption), p. 9 (3 PRELIMINARIES), p. 8 (Figure/Table caption), p. 5 (3 PRELIMINARIES), p. 6 (3 PRELIMINARIES), p. 7 (3 PRELIMINARIES) |
| Primary metric/result | On the Ant Maze domains, IQL significantly outperforms both prior methods after online finetuning. | numeric claim only at cited anchor | p. 9 (3 PRELIMINARIES) |

- Numeric sentences retained from the body:
- **p. 5 / 3 PRELIMINARIES - extractive body cue:** 1.0 0.5 0.0 0.5 1.0 u 0.0 0.2 0.4 0.6 0.8 1.0 / (u < 0)/u2 = 0.01 = 0.1 = 0.5 = 0.9 = ...
- **p. 7 / 3 PRELIMINARIES - extractive body cue:** The dataset consists of 1 optimal trajectory and 99 trajectories with uniform random actions.
- **p. 8 / 3 PRELIMINARIES - extractive body cue:** 0.00 0.25 0.50 0.75 1.00 Gradient Steps (×106) 0 50 100 Episode Return antmaze-medium-play-v0 0.00 0.25 0.50 0.75 1.00 Gradient Steps (×106) 0 50 100 ...
- **p. 9 / 3 PRELIMINARIES - extractive body cue:** For example, the original implementation of CQL takes more than 4 hours to perform 1M updates, while ours takes only 80 minutes.
- **p. 9 / 3 PRELIMINARIES - extractive body cue:** Even so, IQL still requires about 4x less time than our reimplementation of CQL on average, and is comparable to the fastest prior one-step methods.
- **p. 5 / 3 PRELIMINARIES - extractive body cue:** 1.0 0.5 0.0 0.5 1.0 u 0.0 0.2 0.4 0.6 0.8 1.0 / (u < 0)/u2 = 0.01 = 0.1 = 0.5 = 0.9 = ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | TD learning (IQL): for each gradient step do ψ ←ψ -λV ∇ψLV (ψ) θ ←θ -λQ∇θLQ(θ) ˆθ ←(1 -α)ˆθ + αθ end for Policy ... | p. 5 (3 PRELIMINARIES) |
| body limitation/failure cue | Note that the policy does not influence the value function in any way, and therefore extraction could be performed either concurrently or after TD ... | p. 6 (3 PRELIMINARIES) |
| body limitation/failure cue | Since IQL (d) performs iterative dynamic programming, it correctly propagates the signal, and the values are no longer dominated by noise. | p. 7 (3 PRELIMINARIES) |
| body limitation/failure cue | When the static dataset is heavily corrupted by suboptimal actions, one-step policy evaluation results in a value function that degrades to zero far from ... | p. 7 (3 PRELIMINARIES) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We report results for the original hyperparameters and runtime for a comparable set of hyperparameters. those proposing one-step methods, focus entirely on the Gym ... | p. 8 (3 PRELIMINARIES) |
| We did not reimplement Decision Transformers due to their complexity and report runtime of the original implementation. | p. 9 (3 PRELIMINARIES) |
| To evaluate the finetuning capability of various RL algorithms, we first run offline RL on each dataset, then run 1M steps of online RL, ... | p. 9 (3 PRELIMINARIES) |
| We alternate between fitting this value function with expectile regression, and then using it to compute Bellman backups for training the Q-function. | p. 2 (1 INTRODUCTION) |
| For smaller hyperparameter values, the objective behaves similarly to behavioral cloning, while for larger values, it attempts to recover the maximum of the Q-function. | p. 5 (3 PRELIMINARIES) |
| For both steps, we use a version of clipped double Q-learning (Fujimoto et al., 2018), taking a minimum of two Q-functions for V -function ... | p. 6 (3 PRELIMINARIES) |
| Thus, we treat τ as a hyperparameter. | p. 7 (3 PRELIMINARIES) |
| (2021) reports results for a set of hyperparameters, such as batch and network size, that is significantly different from other methods. | p. 8 (3 PRELIMINARIES) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / 3 PRELIMINARIES - extractive body cue:** TD learning (IQL): for each gradient step do ψ ←ψ -λV ∇ψLV (ψ) θ ←θ -λQ∇θLQ(θ) ˆθ ←(1 -α)ˆθ + αθ end for Policy extraction ...
- **p. 6 / 3 PRELIMINARIES - extractive body cue:** Note that the policy does not influence the value function in any way, and therefore extraction could be performed either concurrently or after TD learning.
- **p. 7 / 3 PRELIMINARIES - extractive body cue:** Since IQL (d) performs iterative dynamic programming, it correctly propagates the signal, and the values are no longer dominated by noise.
- **p. 7 / 3 PRELIMINARIES - extractive body cue:** When the static dataset is heavily corrupted by suboptimal actions, one-step policy evaluation results in a value function that degrades to zero far from the ...

- **Evidence anchors reviewed:** datasets p. 7 (3 PRELIMINARIES), p. 7 (3 PRELIMINARIES), p. 4 (3 PRELIMINARIES), p. 5 (3 PRELIMINARIES), p. 8 (3 PRELIMINARIES), p. 9 (3 PRELIMINARIES), metrics p. 5 (3 PRELIMINARIES), p. 7 (3 PRELIMINARIES), p. 7 (3 PRELIMINARIES), p. 8 (Figure/Table caption), p. 9 (3 PRELIMINARIES), p. 9 (3 PRELIMINARIES), baselines p. 8 (Figure/Table caption), p. 8 (3 PRELIMINARIES), p. 9 (3 PRELIMINARIES), p. 9 (3 PRELIMINARIES), p. 4 (3 PRELIMINARIES), p. 4 (3 PRELIMINARIES), results p. 9 (Figure/Table caption), p. 9 (3 PRELIMINARIES), p. 8 (Figure/Table caption), p. 5 (3 PRELIMINARIES), p. 6 (3 PRELIMINARIES), p. 7 (3 PRELIMINARIES).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Figure 2: Evaluation of our algorithm on a toy umaze environment (a). When the static dataset is heavily corrupted by suboptimal actions, one-step policy evaluation results in a value function ... (p. 7, Figure/Table caption).
- **Metric evidence:** The agent receives a reward of 10 for entering the goal state and zero reward for all other transitions. (p. 7, 3 PRELIMINARIES).
- **Baseline/ablation evidence:** Figure 3: Estimating a larger expectile τ is crucial for antmaze tasks that require dynamical program- ming ('stitching'). Comparisons and baselines. We compare to methods that are representative of both ... (p. 8, Figure/Table caption).
- **Failure/negative evidence:** Our reproduced results offline are worse than the reported results, particularly on medium and large antmaze environments. (p. 13, C FINETUNING EXPERIMENTAL DETAILS).
