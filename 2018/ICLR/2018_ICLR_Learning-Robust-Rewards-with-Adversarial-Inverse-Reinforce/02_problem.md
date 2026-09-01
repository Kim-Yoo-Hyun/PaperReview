# Problem - Learning Robust Rewards with Adversarial Inverse Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1710.11248; PDF retrieval source: https://arxiv.org/pdf/1710.11248. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 4 (3 BACKGROUND), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): Our algorithm provides for simultaneous learning of the reward function and value function, which enables us to both make use of the efficient adversarial formulation and recover a generalizable and ...

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive PDF cue:** Reinforcement learning provides a powerful and general framework for decision making and control, but its application in practice is often hindered by the need for ...
- **p. 1 / ABSTRACT - extractive PDF cue:** Deep reinforcement learning methods can remove the need for explicit engineering of policy or value features, but still require a manually specified reward function.
- **p. 1 / ABSTRACT - extractive PDF cue:** Inverse reinforcement learning holds the promise of automatic reward acquisition, but has proven exceptionally difficult to apply to large, high-dimensional problems with unknown dynamics.
- **p. 1 / ABSTRACT - extractive PDF cue:** In this work, we propose AIRL, a practical and scalable inverse reinforcement learning algorithm based on an adversarial reward learning formulation.
- **p. 1 / ABSTRACT - extractive PDF cue:** We demonstrate that AIRL is able to recover reward functions that are robust to changes in dynamics, enabling us to learn policies even under significant ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Our algorithm provides for simultaneous learning of the reward function and value function, which enables us to both make use of the efficient adversarial formulation ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** However, adversarial IRL methods (Finn et al., 2016b;a) hold promise for tackling difficult tasks due to the ability to adapt training samples to improve learning ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Our algorithm provides for simultaneous learning of the reward function and value function, which enables us to both make use of the ... | demonstration으로 정의된 robot task distribution | body wording is the source claim |
| Observation / input | The goal of (forward) reinforcement learning is to find the optimal policy π∗that maximizes the expected entropy-regularized discounted reward, under π, T ... | observation history와 expert trajectory/action | exact sensor/frame/preprocessing from PDF |
| State / latent | goal, forward, reinforcement, learning, find, optimal, policy, maximizes, expected, entropy-regularized | behavior policy와 temporal action context | notation and tensor shape require body check |
| Output / action | Suppose, IRL, recovers, state-only, reward, produces, optimal, policy | predicted action 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | closed-loop task success and robustness | imitation error, task success, robustness와 compounding error | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | observation history o_{t−H:t}; body terms: goal, forward, reinforcement, learning, find, optimal, policy, maximizes, expected, entropy-regularized | p. 3 (3 BACKGROUND), p. 3 (3 BACKGROUND), p. 5 (3 BACKGROUND) |
| Decision / output variable | expert-like action/chunk a_{t:t+H}; body terms: adversarial, inverse, reinforcement, learning, AIRL, algorithm, When, compared | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 5 (3 BACKGROUND) |
| Objective / loss / cost | imitation or action-distribution loss; cue terms: goal, forward, reinforcement, learning, find, optimal, policy, maximizes | p. 3 (3 BACKGROUND), p. 5 (3 BACKGROUND), p. 5 (3 BACKGROUND) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3 BACKGROUND), p. 1 (1 INTRODUCTION), p. 3 (3 BACKGROUND) |
| Success / guarantee | closed-loop task success and robustness | p. 8 (Figure/Table caption), p. 6 (7 EXPERIMENTS), p. 6 (7 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** However, adversarial IRL methods (Finn et al., 2016b;a) hold promise for tackling difficult tasks due to the ability to adapt training samples to improve learning ...
- **p. 4 / 3 BACKGROUND - extractive PDF cue:** Because IRL methods only infer rewards from demonstrations given from an optimal agent, they cannot in general disambiguate between reward functions within this class of ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Part of the challenge is that IRL is an ill-defined problem, since there are many optimal policies that can explain a set of demonstrations, and ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** (2008) handles the former ambiguity, but the latter ambiguity means that IRL algorithms have difficulty distinguishing the true reward functions from those shaped by the ...

## What the Paper Changes

PDF contribution framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 5 (3 BACKGROUND), p. 1 (1 INTRODUCTION), p. 5 (3 BACKGROUND)): In this paper, we propose adversarial inverse reinforcement learning (AIRL), an inverse reinforcement learning algorithm based on adversarial learning.

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** When compared to GAIL (Ho & Ermon, 2016), which does not attempt to directly recover rewards, our method achieves comparable results on tasks that do ...
- **p. 5 / 3 BACKGROUND - extractive PDF cue:** In order to decouple the reward function from the advantage, we propose to modify the discriminator of Sec.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** There are many scenarios where IRL may be preferred over direct imitation learning, such as re-optimizing a reward in novel environments (Finn et al., 2017) ...
- **p. 5 / 3 BACKGROUND - extractive PDF cue:** If the ground truth reward is also only a function of state, this allows us to recover the true reward up to a constant.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | 6 LEARNING DISENTANGLED REWARDS WITH AIRL In the method presented in Section 4, we cannot learn a state-only ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | At test time, the agent cannot simply mimic the actions learned during training, and instead must successfully infer ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | (2016a) does not implement or evaluate GAN-GCL and, to our knowledge, we present the first empirical evaluation of ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | We subtract a constant offset from all reward functions so that they share the same mean for visualization ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

il writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (3 BACKGROUND), p. 3 (3 BACKGROUND), p. 5 (3 BACKGROUND), p. 4 (3 BACKGROUND). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 4 (3 BACKGROUND), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), interface p. 3 (3 BACKGROUND), p. 3 (3 BACKGROUND), p. 5 (3 BACKGROUND), p. 4 (3 BACKGROUND), objective p. 3 (3 BACKGROUND), p. 5 (3 BACKGROUND), p. 5 (3 BACKGROUND).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
