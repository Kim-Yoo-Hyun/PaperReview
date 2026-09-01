# Insights — Learning Latent Dynamics for Planning from Pixels

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1811.04551; PDF retrieval source: https://arxiv.org/pdf/1811.04551. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we propose the Deep Planning Network (PlaNet), a model-based agent that learns the environment dynamics from pixels and chooses actions through online ...
- **p. 1 / 1. Introduction - extractive body cue:** Key contributions of this work are summarized as follows: • Planning in latent spaces We solve a variety of tasks from the DeepMind control suite, ...
- **p. 2 / 2. Latent Space Planning - extractive body cue:** In this section, we introduce notation for the environment and describe the general implementation of our model-based agent.
- **p. 3 / 2 Initialize model parameters θ randomly - extractive body cue:** Because the reward is modeled as a function of the latent state, the planner can operate purely in latent space without generating images, which allows ...
- **p. 2 / 2. Latent Space Planning - extractive body cue:** We define a discrete time step t, hidden states st, image observations ot, continuous action vectors at, and scalar rewards rt, that follow the stochastic ...
- **p. 3 / 3. Recurrent State Space Model - extractive body cue:** Instead, we use an encoder q(s1:T / o1:T , a1:T ) = QT t=1 q(st / st-1, at-1, ot) to infer approximate state posteriors from ...
- **p. 4 / 3. Recurrent State Space Model - extractive body cue:** We use such a model, shown in Figure 2c, that we name recurrent state-space model (RSSM), Deterministic state model: ht = f(ht-1, st-1, at-1) Stochastic ...
- **Contribution anchor:** p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (2. Latent Space Planning), p. 3 (2 Initialize model parameters θ randomly), p. 2 (2. Latent Space Planning), p. 3 (3. Recurrent State Space Model)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** Key difficulties include model inaccuracies, accumulating errors of multi-step predictions, failure to capture multiple possible futures, and overconfident predictions outside of the training distribution.
- **p. 1 / 1. Introduction - extractive body cue:** PlaNet solves continuous control tasks from pixels that are more difficult than those previously solved by planning with learned models.
- **p. 2 / 1. Introduction - extractive body cue:** (f) The walker task requires balance and predicting difficult interactions with the ground when the robot is lying down. its latent space.
- **p. 2 / 1. Introduction - extractive body cue:** Our experiments indicate having both components to be crucial for high planning performance. • Latent overshooting We generalize the standard variational bound to include multi-step ...
- **p. 8 / 7. Discussion - extractive body cue:** Directions for future work include learning temporal abstraction instead of using a fixed action repeat, possibly through hierarchical models.
- **p. 6 / 5. Experiments - extractive body cue:** The cartpole swingup task requires a long planning horizon and to memorize the cart when it is out of view, reacher has a sparse reward ...
- **p. 6 / 5. Experiments - extractive body cue:** The noise might also add a safety margin to the planning objective that results in more robust action sequences.
- **Boundary to test:** Directions for future work include learning temporal abstraction instead of using a fixed action repeat, possibly through hierarchical models.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this paper, we propose the Deep Planning Network (PlaNet), a model-based agent that learns the environment dynamics from pixels and chooses actions through online planning in a compact latent space. | p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Reported outcome | Within less than one hundredth the episodes, PlaNet outperforms A3C (Mnih et al., 2016) and achieves similar performance to the top model-free algorithm D4PG (Barth-Maron et al., 2018). | p. 6 (5. Experiments), p. 6 (5. Experiments) |
| Failure/limitation | Directions for future work include learning temporal abstraction instead of using a fixed action repeat, possibly through hierarchical models. | p. 8 (7. Discussion), p. 6 (5. Experiments) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `observation, uncertainty/risk estimate와 task command → safe set, recovery state 또는 constraint margin → shielded, recovery 또는 safe action`.
- 이 논문의 재사용 가능한 지점은 We define a discrete time step t, hidden states st, image observations ot, continuous action vectors at, and scalar rewards rt, that follow the stochastic dynamics Transition function: st ∼p(st / st-1, ...를 Instead, we use an encoder q(s1:T / o1:T , a1:T ) = QT t=1 q(st / st-1, at-1, ot) to infer approximate state posteriors from past observations and actions, where q(st / ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 safe set, recovery state 또는 constraint margin가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Directions for future work include learning temporal abstraction instead of using a fixed action repeat, possibly through hierarchical models.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this paper, we propose the Deep Planning Network (PlaNet), a model-based agent that learns the environment dynamics from pixels and chooses actions through online planning in a compact latent space.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `World models, safety, uncertainty, and recovery`; tags: `Robotics, world model, Planning, latent dynamics`.
- **Reading predecessor in the generated track queue:** DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Dream to Control: Learning Behaviors by Latent Imagination (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Directions for future work include learning temporal abstraction instead of using a fixed action repeat, possibly through hierarchical models.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The cartpole swingup task requires a long planning horizon and to memorize the cart when it is out of view, reacher has a sparse reward given when the hand and goal area ....
3. Compare against the body-reported baseline or a matched simpler baseline: The agent solves all tasks while learning slower compared to individually trained agents..
4. Report the body metric and its denominator/aggregation: The cartpole swingup task requires a long planning horizon and to memorize the cart when it is out of view, reacher has a sparse reward given when the hand and goal area ....
5. Re-run the body-reported ablation/failure condition: The stochastic component is even more important - the agent does not learn without it..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (2. Latent Space Planning), p. 3 (3. Recurrent State Space Model), p. 4 (3. Recurrent State Space Model); the primary result is directionally consistent at p. 6 (5. Experiments), p. 6 (5. Experiments), p. 20 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Deep, Planning, Network mechanism이 The agent solves all tasks while learning slower compared to individually trained agents. 대비 The cartpole swingup task requires a long planning horizon and to memorize the cart when it is out ...을 개선하고, Directions for future work include learning temporal abstraction instead of using a fixed action repeat, possibly ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
