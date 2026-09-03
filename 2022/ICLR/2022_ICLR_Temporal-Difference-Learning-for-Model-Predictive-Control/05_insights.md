# Insights — Temporal Difference Learning for Model Predictive Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2203.04955; PDF retrieval source: https://arxiv.org/pdf/2203.04955. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1. Introduction - extractive body cue:** (Top) We present a framework for MPC using a task-oriented latent dynamics model and value function learned jointly by temporal difference learning.
- **p. 1 / 1. Introduction - extractive body cue:** (Bottom) Episode return of our method, SAC, and MPC with a ground-truth simulator on challenging, highdimensional Humanoid and Dog tasks (Tassa et al., 2018).
- **p. 2 / 1. Introduction - extractive body cue:** Lastly, we propose a modality-agnostic prediction loss in latent space that enforces temporal consistency in the learned representation without explicit state or image prediction.
- **p. 2 / 1. Introduction - extractive body cue:** In particular, our method solves Humanoid and Dog locomotion tasks with up to 38-dimensional continuous action spaces in as little as 1M environment steps (see ...
- **p. 3 / 3. TD-Learning for Model Predictive Control - extractive body cue:** We summarize our framework in Figure 1 and Algorithm 1.
- **p. 4 / 4. Task-Oriented Latent Dynamics Model - extractive body cue:** Our proposed TOLD consists of five learned components hθ, dθ, Rθ, Qθ, πθ that predict the following quantities: Representation: zt = hθ(st) Latent dynamics: zt+1 ...
- **p. 5 / 4. Task-Oriented Latent Dynamics Model - extractive body cue:** Instead, we propose to regularize TOLD with a latent state consistency loss (shown in Equation 10) that forces a future latent state prediction zt+1 = ...
- **Contribution anchor:** p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. TD-Learning for Model Predictive Control), p. 4 (4. Task-Oriented Latent Dynamics Model)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** To overcome these challenges, we make three key changes to model learning.
- **p. 2 / 1. Introduction - extractive body cue:** While prior work learns a model through state or video prediction, we argue that it is remarkably inefficient to model everything in the environment, including ...
- **p. 1 / 1. Introduction - extractive body cue:** Concretely, prior work on model-based methods can largely be subdivided into two directions, each exploiting key ad
- **p. 1 / 1. Introduction - extractive body cue:** Planning is a powerful approach to such sequential decision making problems, and has achieved tremendous success in application areas such as game-playing (Kaiser et al., ...
- **p. 7 / 5. Experiments - extractive body cue:** Due to dimensionality explosion under discretization, MuZero and EfficientZero cannot feasibly solve tasks with higher-dimensional action spaces, e.g., Walker Walk and Cheetah Run (A ∈R6), ...
- **p. 8 / 5. Experiments - extractive body cue:** Mean of 5 runs. have access to the egocentric camera fails.
- **p. 8 / 5. Experiments - extractive body cue:** Performance of LOOP is similar to SAC, and MPC with a simulator (MPC:sim) performs well on locomotion tasks but fails in tasks with sparse rewards.
- **Boundary to test:** Due to dimensionality explosion under discretization, MuZero and EfficientZero cannot feasibly solve tasks with higher-dimensional action spaces, e.g., Walker Walk and Cheetah Run (A ∈R6), while our method can.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | (Top) We present a framework for MPC using a task-oriented latent dynamics model and value function learned jointly by temporal difference learning. | p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Reported outcome | Figure 14. Individual Meta-World tasks. Success rate of our method (TD-MPC) and SAC on diverse manipulation tasks from Meta- World (Yu et al., 2019). We use the goal-conditioned version of Meta-World, which ... | p. 19 (Figure/Table caption), p. 17 (Figure/Table caption) |
| Failure/limitation | Due to dimensionality explosion under discretization, MuZero and EfficientZero cannot feasibly solve tasks with higher-dimensional action spaces, e.g., Walker Walk and Cheetah Run (A ∈R6), while our method can. | p. 7 (5. Experiments), p. 8 (5. Experiments) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `observation, uncertainty/risk estimate와 task command → safe set, recovery state 또는 constraint margin → shielded, recovery 또는 safe action`.
- 이 논문의 재사용 가능한 지점은 (2015)) control for planning (denoted Πθ), learned models dθ, Rθ of the (latent) dynamics and reward signal, respectively, a terminal state-action value function Qθ, and a parameterized policy πθ that helps guide ...를 H from N(µj-1, (σj-1)2I) 4: Sample Nπ traj. of length H using πθ, dθ // Estimate trajectory returns φΓ using dθ, Rθ, Qθ, starting from zt and initially letting φΓ = 0: ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 safe set, recovery state 또는 constraint margin가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Due to dimensionality explosion under discretization, MuZero and EfficientZero cannot feasibly solve tasks with higher-dimensional action spaces, e.g., Walker Walk and Cheetah Run (A ∈R6), while our method can.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: (Top) We present a framework for MPC using a task-oriented latent dynamics model and value function learned jointly by temporal difference learning.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `World models, safety, uncertainty, and recovery`; tags: `Robotics, world model, model predictive control, Reinforcement Learning`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Due to dimensionality explosion under discretization, MuZero and EfficientZero cannot feasibly solve tasks with higher-dimensional action spaces, e.g., Walker Walk and Cheetah Run (A ∈R6), while our method can.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: TD-Learning for MPC 0 250 500 750 1000 Episode return Average 0 100 200 300 400 Acrobot Swingup 0 250 500 750 1000 Cartpole Swingup 0 250 500 750 1000 Cartpole Swingup ....
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 4. Learning from pixels. Return of our method (TD-MPC) and state-of-the-art algorithms on 12 challenging image-based DMControl tasks. We follow prior work (Hafner et al., 2020b;a; Yarats et al., 2021) and ....
4. Report the body metric and its denominator/aggregation: In contrast, a blind agent that does not 0.0 0.2 0.4 0.6 0.8 1.0 0.00 0.25 0.50 0.75 1.00 Success rate Meta-World (Goal-Conditioned) 0 1 2 3 0.00 0.25 0.50 0.75 1.00 ....
5. Re-run the body-reported ablation/failure condition: We consider: (i) our method implemented using a state predictor (hθ being the identity function), (ii) our method implemented without the latent consistency loss from Equation 10, and lastly: the consistency loss ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (4. Task-Oriented Latent Dynamics Model), p. 5 (4. Task-Oriented Latent Dynamics Model), p. 4 (4. Task-Oriented Latent Dynamics Model); the primary result is directionally consistent at p. 19 (Figure/Table caption), p. 17 (Figure/Table caption), p. 8 (5. Experiments); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Top, present, framework mechanism이 Figure 4. Learning from pixels. Return of our method (TD-MPC) and state-of-the-art algorithms on 12 challenging ... 대비 In contrast, a blind agent that does not 0.0 0.2 0.4 0.6 0.8 1.0 0.00 0.25 0.50 0.75 ...을 개선하고, Due to dimensionality explosion under discretization, MuZero and EfficientZero cannot feasibly solve tasks with higher-dimensional action ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
