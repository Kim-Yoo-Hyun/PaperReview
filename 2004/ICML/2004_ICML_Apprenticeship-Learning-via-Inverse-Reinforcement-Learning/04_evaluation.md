# Evaluation - Apprenticeship Learning via Inverse Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ai.stanford.edu/~pabbeel/irl/; PDF retrieval source: https://ai.stanford.edu/~ang/papers/icml04-apprentice.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (5.1. Gridworld), p. 4 (4. Theoretical results), p. 4 (4. Theoretical results), p. 5 (5.1. Gridworld), p. 5 (5.1. Gridworld), p. 6 (5.2. Car driving simulation)): Screenshot of driving simulator. learning a compact representation of the reward function, our algorithm significantly outperforms the other methods.

## Evaluation Body Digest

- **p. 6 / 5.2. Car driving simulation - extractive body cue:** The simulation runs at 10Hz, and in the experiments that follow, the expert's features were estimated from a single trajectory of 1200 samples (corresponding to ...
- **p. 6 / 5.2. Car driving simulation - extractive body cue:** For our second experiment, we implemented a cardriving simulation, and applied apprenticeship learning to try to learn different "driving styles." A screenshot of our simulator ...
- **p. 5 / 5.1. Gridworld - extractive body cue:** In particular, we do not rely on the expert's demonstrations to learn the state transition probabilities.
- **p. 5 / 5.1. Gridworld - extractive body cue:** (Note log scale on x-axis.)9 Thus, by mainly in the question of how many times an expert must demonstrate a task before we learn to ...
- **p. 4 / 4. Theoretical results - extractive body cue:** In the case where the true reward function R∗does not lie exactly in the span of the basis functions φ, the algorithm still enjoys a ...
- **p. 5 / 4. Theoretical results - extractive body cue:** some residual (error) term ε(s), then our algorithm will have performance that is worse than the expert's by no more than O(∥ε∥∞).
- **p. 5 / 5.1. Gridworld - extractive body cue:** The weights w∗ are generated randomly so as to give sparse rewards, which leads to fairly interesting/rich optimal policies.7 In the basic version, the algorithm ...
- **p. 6 / 5.2. Car driving simulation - extractive body cue:** For instance, in the first driving style, we see negative rewards for collisions and for driving offroad, and larger positive rewards for driving in the ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** demonstration으로 정의된 robot task distribution.
- **Input boundary:** observation history와 expert trajectory/action.
- **Output/decision under evaluation:** predicted action 또는 action chunk.
- **Primary target:** imitation error, task success, robustness와 compounding error.
- **Detected evaluation headings:** 4. Theoretical results (p. 4); 5. Experiments (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.1. Gridworld | EMPIRICAL / SIMULATION | Screenshot of driving simulator. learning a compact representation of the reward function, our algorithm significantly outperforms the other methods. | p. 6 (5.1. Gridworld) |
| 4. Theoretical results | EMPIRICAL / SIMULATION | Most of the results in the previous section were predicated on the assumption that the algorithm terminates with t ≤ϵ. | p. 4 (4. Theoretical results) |
| 4. Theoretical results | EMPIRICAL / SIMULATION | In the case where the true reward function R∗does not lie exactly in the span of the basis functions φ, the algorithm still enjoys ... | p. 4 (4. Theoretical results) |
| 5.1. Gridworld | EMPIRICAL / SIMULATION | Plot of performance vs. number of sampled trajectories from the expert. | p. 5 (5.1. Gridworld) |
| 5.1. Gridworld | EMPIRICAL / SIMULATION | The performance measure is the value of the best policy in the set output by the algorithm. | p. 5 (5.1. Gridworld) |

## Dataset / Benchmark Role

- **p. 6 / 5.2. Car driving simulation - extractive body cue:** The simulation runs at 10Hz, and in the experiments that follow, the expert's features were estimated from a single trajectory of 1200 samples (corresponding to ...
- **p. 6 / 5.2. Car driving simulation - extractive body cue:** For our second experiment, we implemented a cardriving simulation, and applied apprenticeship learning to try to learn different "driving styles." A screenshot of our simulator ...
- **p. 5 / 5.1. Gridworld - extractive body cue:** In particular, we do not rely on the expert's demonstrations to learn the state transition probabilities.
- **p. 5 / 5.1. Gridworld - extractive body cue:** (Note log scale on x-axis.)9 Thus, by mainly in the question of how many times an expert must demonstrate a task before we learn to ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1. Three iterations for max-margin algorithm. the reward function being optimized by the expert. The maximization in that step is equivalently written maxt,w t ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Three iterations for projection algorithm. algorithm. An example showing three iterations of the projection method is shown in Figure 2.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. A comparison of the convergence speeds of the max-margin and projection versions of the algorithm on a 128x128 grid. Euclidean distance to the ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Plot of performance vs. number of sampled tra- jectories from the expert. (Shown in color, where avail- able.) Averages over 20 instances are ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. Screenshot of driving simulator. learning a compact representation of the reward func- tion, our algorithm significantly outperforms the other methods. We also observe ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Feature expectations of teacher ˆµE and of selected/learned policy µ(˜π) (as estimated by Monte Carlo). and weights w corresponding to the reward function ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. Progress in one iteration step. ¯µ(i))·µ(π), and let ˜µ(i+1) = (ˆµE-¯µ(i))·(µ(i+1)-¯µ(i)) ∥µ(i+1)-¯µ(i)∥2 2 (µ(i+1) - ¯µ(i)) + ¯µ(i), i.e. the projection of ˆµE ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The simulation runs at 10Hz, and in the experiments that follow, the expert's features were estimated from a single trajectory of 1200 samples (corresponding ... | embodiment, simulator version and control stack | p. 6 (5.2. Car driving simulation), p. 6 (5.2. Car driving simulation) |
| Task/environment | For our second experiment, we implemented a cardriving simulation, and applied apprenticeship learning to try to learn different "driving styles." A screenshot of our ... | reset, timeout, object/scene variation | p. 6 (5.2. Car driving simulation), p. 5 (5.1. Gridworld) |
| Observation/sensor | observation history와 expert trajectory/action | calibration, preprocessing, privileged input | p. 2 (2. Preliminaries), p. 2 (2. Preliminaries) |
| Output/decision | predicted action 또는 action chunk | action frame, controller and termination | p. 1 (1. Introduction), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In the case where the true reward function R∗does not lie exactly in the span of the basis functions φ, the algorithm still enjoys ... | definition/direction/unit from same section | p. 4 (4. Theoretical results) |
| some residual (error) term ε(s), then our algorithm will have performance that is worse than the expert's by no more than O(∥ε∥∞). | definition/direction/unit from same section | p. 5 (4. Theoretical results) |
| The weights w∗ are generated randomly so as to give sparse rewards, which leads to fairly interesting/rich optimal policies.7 In the basic version, the ... | definition/direction/unit from same section | p. 5 (5.1. Gridworld) |
| For instance, in the first driving style, we see negative rewards for collisions and for driving offroad, and larger positive rewards for driving in ... | definition/direction/unit from same section | p. 6 (5.2. Car driving simulation) |
| Table 1. Feature expectations of teacher ˆµE and of selected/learned policy µ(˜π) (as estimated by Monte Carlo). and weights w corresponding to the reward ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| (14), and outputs a policy ˜π so that for any true reward R∗(s) = w∗T φ(s) (∥w∗∥1 ≤1) we have E[P∞ t=0 γtR∗(st)/˜π] ≥E[P∞ ... | definition/direction/unit from same section | p. 4 (4. Theoretical results) |
| Since no "true" reward was ever specified or used in the experiments, we cannot report on the results of the algorithm according to R∗. | definition/direction/unit from same section | p. 6 (5.2. Car driving simulation) |
| Figure 1. Three iterations for max-margin algorithm. the reward function being optimized by the expert. The maximization in that step is equivalently written maxt,w ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Screenshot of driving simulator. learning a compact representation of the reward function, our algorithm significantly outperforms the other methods. | comparison identity and matched condition | p. 6 (5.1. Gridworld) |
| A comparison of the convergence speeds of the max-margin and projection versions of the algorithm on a 128x128 grid. | comparison identity and matched condition | p. 5 (5.1. Gridworld) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| no ablation sentence selected | not reported; proposed stress test only | verify ablation section |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we assume that the expert is trying (without necessarily succeeding) to optimize an unknown reward function that can be expressed as ... | Screenshot of driving simulator. learning a compact representation of the reward function, our algorithm significantly outperforms the other methods. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (5.1. Gridworld), p. 4 (4. Theoretical results), p. 4 (4. Theoretical results), p. 5 (5.1. Gridworld), p. 5 (5.1. Gridworld), p. 6 (5.2. Car driving simulation) |
| Primary metric/result | Most of the results in the previous section were predicated on the assumption that the algorithm terminates with t ≤ϵ. | numeric claim only at cited anchor | p. 4 (4. Theoretical results) |

- Numeric sentences retained from the body:
- **p. 5 / 5.1. Gridworld - extractive body cue:** The plot shows averages over 40 runs, with 1 s.e. errorbars.
- **p. 5 / 5.1. Gridworld - extractive body cue:** (Shown in color, where available.) Averages over 20 instances are plotted, with 1 s.e. errorbars.
- **p. 6 / 5.2. Car driving simulation - extractive body cue:** The simulation runs at 10Hz, and in the experiments that follow, the expert's features were estimated from a single trajectory of 1200 samples (corresponding to ...
- **p. 4 / 3.1. A simpler algorithm - extractive body cue:** The full justification for this method is deferred to the full paper (Abbeel and Ng, 2004), but in Sections 4 and 5 we will also ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The agent has four actions to try to move in each of the four compass directions, but with 30% chance an action fails and ... | p. 5 (5.1. Gridworld) |
| body limitation/failure cue | Nice: The highest priority is to avoid collisions than the "mimic the expert" algorithm initially. | p. 6 (5.2. Car driving simulation) |
| body limitation/failure cue | Since no "true" reward was ever specified or used in the experiments, we cannot report on the results of the algorithm according to R∗. | p. 6 (5.2. Car driving simulation) |
| body limitation/failure cue | Table 1. Feature expectations of teacher ˆµE and of selected/learned policy µ(˜π) (as estimated by Monte Carlo). and weights w corresponding to the reward ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | In the case where the true reward function R∗does not lie exactly in the span of the basis functions φ, the algorithm still enjoys ... | p. 4 (4. Theoretical results) |
| body limitation/failure cue | If the algorithm sometimes does not terminate, or if it sometimes takes a very (perhaps exponentially) large number of iterations to terminate, then it ... | p. 4 (4. Theoretical results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The weights w∗ are generated randomly so as to give sparse rewards, which leads to fairly interesting/rich optimal policies.7 In the basic version, the ... | p. 5 (5.1. Gridworld) |
| In all of our experiments, the algorithm was run for 30 iterations, and a policy was selected by inspection (per the discussion in Section ... | p. 6 (5.2. Car driving simulation) |
| Using the RL algorithm, compute the optimal policy π(i) for the MDP using rewards R = (w(i))T φ. | p. 3 (3. Algorithm) |
| Randomly pick some policy π(0), compute (or approximate via Monte Carlo) µ(0) = µ(π(0)), and set i = 1. | p. 3 (3. Algorithm) |
| Suppose the apprenticeship learning algorithm (either max-margin or projection version) is run using an estimate ˆµE for µE obtained by m Monte Carlo samples. | p. 4 (4. Theoretical results) |
| Briefly, the projection method replaces step 2 of the algorithm with the following: - Set ¯µ(i-1) = ¯µ(i-2)+ (µ(i-1)-¯µ(i-2))T (µE-¯µ(i-2)) (µ(i-1)-¯µ(i-2))T (µ(i-1)-¯µ(i-2))(µ(i-1)-¯µ(i-2)) (This computes ... | p. 4 (3.1. A simpler algorithm) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / 5.1. Gridworld - extractive body cue:** The agent has four actions to try to move in each of the four compass directions, but with 30% chance an action fails and results ...
- **p. 6 / 5.2. Car driving simulation - extractive body cue:** Nice: The highest priority is to avoid collisions than the "mimic the expert" algorithm initially.
- **p. 6 / 5.2. Car driving simulation - extractive body cue:** Since no "true" reward was ever specified or used in the experiments, we cannot report on the results of the algorithm according to R∗.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Feature expectations of teacher ˆµE and of selected/learned policy µ(˜π) (as estimated by Monte Carlo). and weights w corresponding to the reward function ...
- **p. 4 / 4. Theoretical results - extractive body cue:** In the case where the true reward function R∗does not lie exactly in the span of the basis functions φ, the algorithm still enjoys a ...
- **p. 4 / 4. Theoretical results - extractive body cue:** If the algorithm sometimes does not terminate, or if it sometimes takes a very (perhaps exponentially) large number of iterations to terminate, then it would ...

- **Evidence anchors reviewed:** datasets p. 6 (5.2. Car driving simulation), p. 6 (5.2. Car driving simulation), p. 5 (5.1. Gridworld), p. 5 (5.1. Gridworld), metrics p. 4 (4. Theoretical results), p. 5 (4. Theoretical results), p. 5 (5.1. Gridworld), p. 6 (5.2. Car driving simulation), p. 7 (Figure/Table caption), p. 4 (4. Theoretical results), baselines p. 6 (5.1. Gridworld), p. 5 (5.1. Gridworld), results p. 6 (5.1. Gridworld), p. 4 (4. Theoretical results), p. 4 (4. Theoretical results), p. 5 (5.1. Gridworld), p. 5 (5.1. Gridworld), p. 6 (5.2. Car driving simulation).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
