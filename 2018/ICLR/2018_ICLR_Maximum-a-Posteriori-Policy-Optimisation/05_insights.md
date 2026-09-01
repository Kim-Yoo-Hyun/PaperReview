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

- **Closed-loop position:** `state 또는 observation, action, reward와 transition history → policy/value state와 action-selection variable → action policy와 induced trajectory`.
- 이 논문의 재사용 가능한 지점은 And subsequently it updates the policy such that better actions in that state will have better probabilities to be chosen.를 We develop two off-policy algorithms and demonstrate that they are competitive with the state-of-the-art in deep reinforcement learning.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 policy/value state와 action-selection variable가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4 training_steps 1e7 0 200 400 600 800 1000 mean_return task_name=run, domain_name=humanoid agent=DDPG agent=EPG + retrace + entropy (optimized) agent=MPO agent=MPO (parametric) agent=PPO 0 1 ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this paper we propose a novel off-policy algorithm that benefits from the best properties of both classes.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Reinforcement Learning, policy optimization, Off-Policy Learning`.
- **Reading predecessor in the generated track queue:** Where are we in the search for an Artificial Visual Cortex for Embodied Intelligence? (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** MT-Opt: Continuous Multi-Task Robotic Reinforcement Learning at Scale (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** 0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4 training_steps 1e7 0 200 400 600 800 1000 mean_return task_name=run, domain_name=humanoid agent=DDPG agent=EPG + retrace + entropy (optimized) agent=MPO agent=MPO (parametric) agent=PPO 0 1 ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: For example, the classical cart-pole and acrobot dynamical systems, 2D and Humanoid walking as well as simple low-dimensional planar reaching and manipulation tasks..
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 2: Ablation study of the MPO algorithm and comparison to common baselines from the liter- ature on three domains from the control suite. We plot the median performance over 10 experiments ....
4. Report the body metric and its denominator/aggregation: The reward in the Acrobot task is the distance of the robots end-effector to an upright position of the underactuated system..
5. Re-run the body-reported ablation/failure condition: Finally using only a single sample to estimate the integral (and hence the likelihood ratio gradient) results in an actor-critic variant with Retrace that is the least performant off-policy algorithm in our ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 1 (ABSTRACT), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION); the primary result is directionally consistent at p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 novel, off-policy, algorithm mechanism이 Figure 2: Ablation study of the MPO algorithm and comparison to common baselines from the liter- ... 대비 The reward in the Acrobot task is the distance of the robots end-effector to an upright position of ...을 개선하고, 0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4 training_steps 1e7 0 200 400 600 800 1000 ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
