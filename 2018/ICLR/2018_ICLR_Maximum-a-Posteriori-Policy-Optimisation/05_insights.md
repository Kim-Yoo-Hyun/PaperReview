# Insights — Maximum a Posteriori Policy Optimisation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=S1ANxQW0b; PDF retrieval source: https://openreview.net/forum?id=S1ANxQW0b. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1 INTRODUCTION - extractive body cue:** In this paper we propose a novel off-policy algorithm that benefits from the best properties of both classes.
- **p. 1 / ABSTRACT - extractive body cue:** We introduce a new algorithm for reinforcement learning called Maximum aposteriori Policy Optimisation (MPO) based on coordinate ascent on a relativeentropy objective.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We show below that several algorithms, including TRPO, can be directly related to this perspective.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** And subsequently it updates the policy such that better actions in that state will have better probabilities to be chosen.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We leverage the fast convergence properties of EM-style coordinate ascent by alternating a nonparametric data-based E-step which re-weights state-action samples, with a supervised, parametric M-step ...
- **Contribution anchor:** p. 1 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)

### Strongest assumption and failure boundary

- **p. 1 / 1 INTRODUCTION - extractive body cue:** While also popular, these algorithms can be difficult to tune, especially for high-dimensional domains like general robot manipulation tasks.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Two types of algorithms currently dominate scalable learning for continuous control problems: First, Trust-Region Policy Optimisation (TRPO; Schulman et al.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We evaluate our algorithm on a broad spectrum of continuous control problems including a 56 DoF humanoid body.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** 0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4 training_steps 1e7 0 200 400 600 800 1000 mean_return task_name=run, domain_name=humanoid agent=DDPG agent=EPG + retrace + entropy ...
- **Boundary to test:** 0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4 training_steps 1e7 0 200 400 600 800 1000 mean_return task_name=run, domain_name=humanoid agent=DDPG agent=EPG + retrace + entropy (optimized) agent=MPO agent=MPO (parametric) agent=PPO 0 1 ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this paper we propose a novel off-policy algorithm that benefits from the best properties of both classes. | p. 1 (1 INTRODUCTION), p. 1 (ABSTRACT) |
| Reported outcome | This difference is so extreme that in several instances the PPO baseline converges an order of magnitude slower than the off-policy algorithms and we thus indicate the asymptotic performance of each algorithm ... | p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Failure/limitation | 0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4 training_steps 1e7 0 200 400 600 800 1000 mean_return task_name=run, domain_name=humanoid agent=DDPG agent=EPG + retrace + entropy (optimized) agent=MPO agent=MPO (parametric) agent=PPO 0 1 ... | p. 9 (5 EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** In this paper we propose a novel off-policy algorithm that benefits from the best properties of both classes. (p. 1, 1 INTRODUCTION).
- **Paper-specific mechanism:** In this paper we propose a novel off-policy algorithm that benefits from the best properties of both classes. (p. 1, 1 INTRODUCTION).
- **Evidence boundary:** the reported outcome is Figure 2: Ablation study of the MPO algorithm and comparison to common baselines from the liter- ature on three domains from the control suite. We plot the median performance over ... (p. 8, Figure/Table caption); the relevant task/metric cue is The reward in the Acrobot task is the distance of the robots end-effector to an upright position of the underactuated system. (p. 8, 5 EXPERIMENTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** The case for the Walker-2D parkour domain (where we compare against a PPO baseline) is even more striking: where standard PPO requires approximately 1M trajectories to find a good policy ... (p. 9, 5 EXPERIMENTS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Reinforcement Learning, policy optimization, Off-Policy Learning`.
- **Reading predecessor in the generated track queue:** Where are we in the search for an Artificial Visual Cortex for Embodied Intelligence? (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** MT-Opt: Continuous Multi-Task Robotic Reinforcement Learning at Scale (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** 0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4 training_steps 1e7 0 200 400 600 800 1000 mean_return task_name=run, domain_name=humanoid agent=DDPG agent=EPG + retrace + entropy (optimized) agent=MPO agent=MPO (parametric) agent=PPO 0 1 ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: In this paper we propose a novel off-policy algorithm that benefits from the best properties of both classes. (p. 1, 1 INTRODUCTION); preserve the objective/update rule: In contrast to typical off-policy value-gradient algorithms, the new algorithm does not require gradient of the Q-function to update the policy. (p. 2, 1 INTRODUCTION).
2. Use the paper-reported task/data/environment cue: For example, the classical cart-pole and acrobot dynamical systems, 2D and Humanoid walking as well as simple low-dimensional planar reaching and manipulation tasks. (p. 7, 5 EXPERIMENTS).
3. Compare against the reported or matched baseline: We note that in order to ensure a fair comparison all algorithms ran with exactly the same network configuration, used a single learner (no distributed computation), used the same optimizer ... (p. 8, 5 EXPERIMENTS).
4. Report the body metric with its denominator and aggregation: The reward in the Acrobot task is the distance of the robots end-effector to an upright position of the underactuated system. (p. 8, 5 EXPERIMENTS).
5. Re-run the reported ablation or stress/failure condition: Finally using only a single sample to estimate the integral (and hence the likelihood ratio gradient) results in an actor-critic variant with Retrace that is the least performant off-policy algorithm ... (p. 8, 5 EXPERIMENTS); if none is reported, design one around: The case for the Walker-2D parkour domain (where we compare against a PPO baseline) is even more striking: where standard PPO requires approximately 1M trajectories to find a good policy ... (p. 9, 5 EXPERIMENTS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), match the reported outcome at p. 8 (Figure/Table caption), p. 9 (5 EXPERIMENTS), p. 11 (Figure/Table caption), and measure the boundary at p. 9 (5 EXPERIMENTS), p. 18 (A.2 REGULARIZED JOINT POLICY GRADIENT).

## Falsifiable research question

Under the paper's stated interface (In this paper we propose a novel off-policy algorithm that benefits from the best properties of both classes.), does the paper-specific mechanism (In this paper we propose a novel off-policy algorithm that benefits from the best properties of both classes.) retain the reported evaluation outcome (The reward in the Acrobot task is the distance of the robots end-effector to an upright position of ...) when tested against the paper's strongest explicit boundary (The case for the Walker-2D parkour domain (where we compare against a PPO baseline) is even more striking: ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (The reward in the Acrobot task is the distance of the robots end-effector to an upright position of ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (23 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** In this paper we propose a novel off-policy algorithm that benefits from the best properties of both classes. (p. 1, 1 INTRODUCTION).
- **Paper-supported outcome:** Figure 2: Ablation study of the MPO algorithm and comparison to common baselines from the liter- ature on three domains from the control suite. We plot the median performance over ... (p. 8, Figure/Table caption).
- **Strongest explicit boundary:** The case for the Walker-2D parkour domain (where we compare against a PPO baseline) is even more striking: where standard PPO requires approximately 1M trajectories to find a good policy ... (p. 9, 5 EXPERIMENTS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
