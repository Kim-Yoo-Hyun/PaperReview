# Evaluation - Trust Region Policy Optimization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v37/schulman15.html; PDF retrieval source: https://arxiv.org/pdf/1502.05477. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (3. Approximately solve this constrained optimization), p. 5 (3. Approximately solve this constrained optimization), p. 5 (3. Approximately solve this constrained optimization), p. 6 (1. What are the performance characteristics of the single), p. 7 (3. Can TRPO be used to solve challenging large-scale), p. 7 (3. Can TRPO be used to solve challenging large-scale)): Though this difference might seem subtle, our experiments demonstrate that it significantly improves the algorithm's performance on larger problems.

## Evaluation Body Digest

- **p. 6 / 3. Can TRPO be used to solve challenging large-scale - extractive body cue:** 8.1 Simulated Robotic Locomotion We conducted the robotic locomotion experiments using the MuJoCo simulator (Todorov et al., 2012).
- **p. 6 / 1. What are the performance characteristics of the single - extractive body cue:** 2D robot models used for locomotion experiments.
- **p. 7 / 3. Can TRPO be used to solve challenging large-scale - extractive body cue:** We ended the episodes when the hopper fell over, which was defined by thresholds on the torso height and angle.
- **p. 5 / 2 Preliminaries - extractive body cue:** By averaging over samples, construct the estimated objective and constraint in Equation (14).
- **p. 5 / 2 Preliminaries - extractive body cue:** In large or continuous state spaces, we can construct an estimator of the surrogate objective using importance sampling.
- **p. 7 / 3. Can TRPO be used to solve challenging large-scale - extractive body cue:** Trust Region Policy Optimization tasks very challenging.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1. Performance comparison for vision-based RL algorithms on the Atari domain. Our algorithms (bottom rows) were run once on each task, with the same ...
- **p. 5 / 3. Approximately solve this constrained optimization - extractive body cue:** Kakade & Langford (2002) consider this error in their derivation, and the same arguments would hold in the setting of this paper, but we omit ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** robot/environment의 sequential decision process.
- **Input boundary:** state 또는 observation, action, reward와 transition history.
- **Output/decision under evaluation:** action policy와 induced trajectory.
- **Primary target:** expected return, task success, stability와 sample efficiency.
- **Detected evaluation headings:** 8 Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 3. Approximately solve this constrained optimization | EMPIRICAL / SIMULATION | Though this difference might seem subtle, our experiments demonstrate that it significantly improves the algorithm's performance on larger problems. | p. 6 (3. Approximately solve this constrained optimization) |
| 3. Approximately solve this constrained optimization | EMPIRICAL / SIMULATION | The rate of improvement in the policy is similar to the empirical FIM, as shown in the experiments. | p. 5 (3. Approximately solve this constrained optimization) |
| 3. Approximately solve this constrained optimization | EMPIRICAL / SIMULATION | 7 Connections with Prior Work As mentioned in Section 4, our derivation results in a policy update that is related to several prior methods, ... | p. 5 (3. Approximately solve this constrained optimization) |
| 1. What are the performance characteristics of the single | EMPIRICAL / SIMULATION | How does this affect the performance of the algorithm? | p. 6 (1. What are the performance characteristics of the single) |
| 3. Can TRPO be used to solve challenging large-scale | EMPIRICAL / SIMULATION | For the natural gradient method, we swept through the possible values of the stepsize in factors of three, and took the best value according ... | p. 7 (3. Can TRPO be used to solve challenging large-scale) |

## Dataset / Benchmark Role

- **p. 6 / 3. Can TRPO be used to solve challenging large-scale - extractive body cue:** 8.1 Simulated Robotic Locomotion We conducted the robotic locomotion experiments using the MuJoCo simulator (Todorov et al., 2012).
- **p. 6 / 1. What are the performance characteristics of the single - extractive body cue:** 2D robot models used for locomotion experiments.
- **p. 7 / 3. Can TRPO be used to solve challenging large-scale - extractive body cue:** We ended the episodes when the hopper fell over, which was defined by thresholds on the torso height and angle.
- **p. 5 / 2 Preliminaries - extractive body cue:** By averaging over samples, construct the estimated objective and constraint in Equation (14).
- **p. 5 / 2 Preliminaries - extractive body cue:** In large or continuous state spaces, we can construct an estimator of the surrogate objective using importance sampling.
- **p. 7 / 3. Can TRPO be used to solve challenging large-scale - extractive body cue:** Trust Region Policy Optimization tasks very challenging.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 1. Left: illustration of single path procedure. Here, we generate a set of trajectories via simulation of the policy and in- corporate all state-action ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 2. 2D robot models used for locomotion experiments. From left to right: swimmer, hopper, walker. The hopper and walker present a particular challenge, due ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. Neural networks used for the locomotion task (top) and for playing Atari games (bottom).
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Learning curves for locomotion tasks, averaged across five runs of each algorithm with random initializations. Note that for the hopper and walker, a ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1. Performance comparison for vision-based RL algorithms on the Atari domain. Our algorithms (bottom rows) were run once on each task, with the same ...
- **p. 15 / Figure/Table caption - extractive body cue:** Table 2. Parameters for continuous control tasks, vine and single path (SP) algorithms.
- **p. 16 / Figure/Table caption - extractive body cue:** Table 3. Parameters used for Atari domain. F Learning Curves for the Atari Domain 0 100 200 300 400
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 5. Learning curves for the Atari domain. For historical reasons, the plots show cost = negative reward.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 8.1 Simulated Robotic Locomotion We conducted the robotic locomotion experiments using the MuJoCo simulator (Todorov et al., 2012). | embodiment, simulator version and control stack | p. 6 (3. Can TRPO be used to solve challenging large-scale), p. 6 (1. What are the performance characteristics of the single) |
| Task/environment | 2D robot models used for locomotion experiments. | reset, timeout, object/scene variation | p. 6 (1. What are the performance characteristics of the single), p. 7 (3. Can TRPO be used to solve challenging large-scale) |
| Observation/sensor | state 또는 observation, action, reward와 transition history | calibration, preprocessing, privileged input | p. 2 (2 Preliminaries), p. 4 (2 Preliminaries) |
| Output/decision | action policy와 induced trajectory | action frame, controller and termination | p. 5 (2 Preliminaries), p. 6 (3. Approximately solve this constrained optimization) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 1. Performance comparison for vision-based RL algorithms on the Atari domain. Our algorithms (bottom rows) were run once on each task, with the ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Kakade & Langford (2002) consider this error in their derivation, and the same arguments would hold in the setting of this paper, but we ... | definition/direction/unit from same section | p. 5 (3. Approximately solve this constrained optimization) |
| Empirically, it is hard to robustly choose the penalty coefficient, so we use a hard constraint instead of a penalty, with parameter δ (the ... | definition/direction/unit from same section | p. 5 (3. Approximately solve this constrained optimization) |
| Learning curves showing the total reward averaged across five runs of each algorithm are shown in Figure 4. | definition/direction/unit from same section | p. 7 (3. Can TRPO be used to solve challenging large-scale) |
| 12-dimensional state space, same reward as the swimmer, with a bonus of +1 for being in a nonterminal state. | definition/direction/unit from same section | p. 7 (3. Can TRPO be used to solve challenging large-scale) |
| Figure 5. Learning curves for the Atari domain. For historical reasons, the plots show cost = negative reward. | definition/direction/unit from same section | p. 16 (Figure/Table caption) |
| Figure 1. Left: illustration of single path procedure. Here, we generate a set of trajectories via simulation of the policy and in- corporate all ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Though this difference might seem subtle, our experiments demonstrate that it significantly improves the algorithm's performance on larger problems. | definition/direction/unit from same section | p. 6 (3. Approximately solve this constrained optimization) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| This self-normalized estimator removes the need to use a baseline for the Q-values (note that the gradient is unchanged by adding a constant to ... | comparison identity and matched condition | p. 5 (2 Preliminaries) |
| To establish a standard baseline, we also included the classic cart-pole balancing problem, based on the formulation from Barto et al. | comparison identity and matched condition | p. 7 (3. Can TRPO be used to solve challenging large-scale) |
| These results provide empirical evidence that constraining the KL divergence is a more robust way to choose step sizes and make fast, consistent progress, ... | comparison identity and matched condition | p. 7 (3. Can TRPO be used to solve challenging large-scale) |
| 7 Connections with Prior Work As mentioned in Section 4, our derivation results in a policy update that is related to several prior methods, ... | comparison identity and matched condition | p. 5 (3. Approximately solve this constrained optimization) |
| Table 1. Performance comparison for vision-based RL algorithms on the Atari domain. Our algorithms (bottom rows) were run once on each task, with the ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| This self-normalized estimator removes the need to use a baseline for the Q-values (note that the gradient is unchanged by adding a constant to ... | component/input/data sensitivity | p. 5 (2 Preliminaries) |
| As described in Appendix C, this analytic estimator has computational benefits in the large-scale setting, since it removes the need to store a dense ... | component/input/data sensitivity | p. 5 (3. Approximately solve this constrained optimization) |
| To answer (1) and (2), we compare the performance of the single path and vine variants of TRPO, several ablated variants, and a number ... | component/input/data sensitivity | p. 6 (3. Can TRPO be used to solve challenging large-scale) |
| Note that for the hopper and walker, a score of -1 is achievable without any forward velocity, indicating a policy that simply learned balanced ... | component/input/data sensitivity | p. 7 (3. Can TRPO be used to solve challenging large-scale) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Instead, we introduce the following local approximation to η: Lπ(˜π) = η(π) + X s ρπ(s) X a ˜π(a/s)Aπ(s, a). | Though this difference might seem subtle, our experiments demonstrate that it significantly improves the algorithm's performance on larger problems. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (3. Approximately solve this constrained optimization), p. 5 (3. Approximately solve this constrained optimization), p. 5 (3. Approximately solve this constrained optimization), p. 6 (1. What are the performance characteristics of the single), p. 7 (3. Can TRPO be used to solve challenging large-scale), p. 7 (3. Can TRPO be used to solve challenging large-scale) |
| Primary metric/result | The rate of improvement in the policy is similar to the empirical FIM, as shown in the experiments. | numeric claim only at cited anchor | p. 5 (3. Approximately solve this constrained optimization) |

- Numeric sentences retained from the body:
- **p. 5 / 3. Approximately solve this constrained optimization - extractive body cue:** That is, we estimate Aij as 1 N PN n=1 ∂2 ∂θi∂θj DKL(πθold(·/sn) ∥πθ(·/sn)), rather than 1 N PN n=1 ∂ ∂θi log πθ(an/sn) ∂ ...
- **p. 6 / 1. What are the performance characteristics of the single - extractive body cue:** Joint angles and kinematics Control Standard deviations Fully connected layer 30 units Input layer Mean parameters Sampling Screen input 4×4 4×4 4×4 4×4 4×4 4×4 ...
- **p. 5 / 3. Approximately solve this constrained optimization - extractive body cue:** That is, we estimate Aij as 1 N PN n=1 ∂2 ∂θi∂θj DKL(πθold(·/sn) ∥πθ(·/sn)), rather than 1 N PN n=1 ∂ ∂θi log πθ(an/sn) ∂ ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The analytic estimator integrates over the action at each state sn, and does not depend on the action an that was sampled. | p. 5 (3. Approximately solve this constrained optimization) |
| body limitation/failure cue | Unlike REPS, our approach does not require a costly nonlinear optimization in the inner loop. | p. 6 (3. Approximately solve this constrained optimization) |
| body limitation/failure cue | We can greatly reduce the variance of the Q-value differences between rollouts by using the same random number sequence for the noise in each ... | p. 5 (2 Preliminaries) |
| body limitation/failure cue | These results provide empirical evidence that constraining the KL divergence is a more robust way to choose step sizes and make fast, consistent progress, ... | p. 7 (3. Can TRPO be used to solve challenging large-scale) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The algorithms repeatedly perform the following steps: 1. | p. 5 (2 Preliminaries) |
| However, the large penalty coefficient C leads to prohibitively small steps, so we would like to decrease this coefficient. | p. 5 (3. Approximately solve this constrained optimization) |
| θ=θold, where the stepsize 1 λ is typically treated as an algorithm parameter. | p. 6 (3. Approximately solve this constrained optimization) |
| For the natural gradient method, we swept through the possible values of the stepsize in factors of three, and took the best value according ... | p. 7 (3. Can TRPO be used to solve challenging large-scale) |
| This is in contrast with most prior methods for learning locomotion, which typically rely on hand-architected policy classes that explicitly encode notions of balance ... | p. 7 (3. Can TRPO be used to solve challenging large-scale) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / 3. Approximately solve this constrained optimization - extractive body cue:** The analytic estimator integrates over the action at each state sn, and does not depend on the action an that was sampled.
- **p. 6 / 3. Approximately solve this constrained optimization - extractive body cue:** Unlike REPS, our approach does not require a costly nonlinear optimization in the inner loop.
- **p. 5 / 2 Preliminaries - extractive body cue:** We can greatly reduce the variance of the Q-value differences between rollouts by using the same random number sequence for the noise in each of ...
- **p. 7 / 3. Can TRPO be used to solve challenging large-scale - extractive body cue:** These results provide empirical evidence that constraining the KL divergence is a more robust way to choose step sizes and make fast, consistent progress, compared ...

- **Evidence anchors reviewed:** datasets p. 6 (3. Can TRPO be used to solve challenging large-scale), p. 6 (1. What are the performance characteristics of the single), p. 7 (3. Can TRPO be used to solve challenging large-scale), p. 5 (2 Preliminaries), p. 5 (2 Preliminaries), p. 7 (3. Can TRPO be used to solve challenging large-scale), metrics p. 8 (Figure/Table caption), p. 5 (3. Approximately solve this constrained optimization), p. 5 (3. Approximately solve this constrained optimization), p. 7 (3. Can TRPO be used to solve challenging large-scale), p. 7 (3. Can TRPO be used to solve challenging large-scale), p. 16 (Figure/Table caption), baselines p. 5 (2 Preliminaries), p. 7 (3. Can TRPO be used to solve challenging large-scale), p. 7 (3. Can TRPO be used to solve challenging large-scale), p. 5 (3. Approximately solve this constrained optimization), p. 8 (Figure/Table caption), results p. 6 (3. Approximately solve this constrained optimization), p. 5 (3. Approximately solve this constrained optimization), p. 5 (3. Approximately solve this constrained optimization), p. 6 (1. What are the performance characteristics of the single), p. 7 (3. Can TRPO be used to solve challenging large-scale), p. 7 (3. Can TRPO be used to solve challenging large-scale).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Table 1. Performance comparison for vision-based RL algorithms on the Atari domain. Our algorithms (bottom rows) were run once on each task, with the same architecture and parameters. Performance varies ... (p. 8, Figure/Table caption).
- **Metric evidence:** Table 1. Performance comparison for vision-based RL algorithms on the Atari domain. Our algorithms (bottom rows) were run once on each task, with the same architecture and parameters. Performance varies ... (p. 8, Figure/Table caption).
- **Baseline/ablation evidence:** This self-normalized estimator removes the need to use a baseline for the Q-values (note that the gradient is unchanged by adding a constant to the Q-values). (p. 5, 2 Preliminaries).
- **Failure/negative evidence:** Our analysis also provides a perspective that unifies policy gradient and policy iteration methods, and shows them to be special limiting cases of an algorithm that optimizes a certain objective ... (p. 8, 9 Discussion).
