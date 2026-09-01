# Insights — Dream to Control: Learning Behaviors by Latent Imagination

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1912.01603; PDF retrieval source: https://arxiv.org/pdf/1912.01603. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1 INTRODUCTION - extractive body cue:** We present Dreamer, an agent that learns long-horizon behaviors from images purely by latent imagination.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Latent dynamics Dreamer uses a latent dynamics model that consists of three components.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Compared to predictions in image space, latent states have a small memory footprint that enables imagining thousands of trajectories in parallel.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The key contributions of this paper are summarized as follows: • Learning long-horizon behaviors by latent imagination Model-based agents can be shortsighted if they use ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** This section describes the main contribution of our paper.
- **p. 5 / B Sequence length - extractive body cue:** We apply the representation model to the first 5 images of two hold-out trajectories and predict forward for 45 steps using the latent dynamics, given ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** As outlined in Figure 3 and detailed in Algorithm 1, Dreamer performs the following operations throughout the agent's life time, either interleaved or in parallel: ...
- **Contribution anchor:** p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 5 (B Sequence length)

### Strongest assumption and failure boundary

- **p. 2 / 1 INTRODUCTION - extractive body cue:** We approach this limitation by predicting both actions and state values.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The tasks pose a variety of challenges including contact dynamics, sparse rewards, many degrees of freedom, and 3D environments.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** This ability requires building representations of the world from past experience that enable generalization to novel situations.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Moreover, prior work commonly resorts to derivative-free optimization for robustness to model errors (Ebert et al., 2017; Chua et al., 2018; Parmas et al., 2019), ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** (c) The agent encodes the history of the episode to compute the current model state and predict the next action to execute in the environment.
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 9: Performance of Dreamer in environments with discrete actions and early termination. Dreamer learns successful behaviors on this subset of Atari games and the ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4: Imagination horizons. We compare the final performance of Dreamer, learning an action model without value prediction, and online planning using PlaNet. Learning a ...
- **Boundary to test:** Figure 2: Image observations for 5 of the 20 visual control tasks used in our experiments. The tasks pose a variety of challenges including contact dynamics, sparse rewards, many degrees of freedom, ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We present Dreamer, an agent that learns long-horizon behaviors from images purely by latent imagination. | p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Reported outcome | Baseline methods The highest reported performance on the continuous tasks is achieved by D4PG (Barth-Maron et al., 2018), an improved variant of DDPG (Lillicrap et al., 2015) that uses distributed collection, distributional ... | p. 8 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS) |
| Failure/limitation | Figure 2: Image observations for 5 of the 20 visual control tasks used in our experiments. The tasks pose a variety of challenges including contact dynamics, sparse rewards, many degrees of freedom, ... | p. 2 (Figure/Table caption), p. 16 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `observation, uncertainty/risk estimate와 task command → safe set, recovery state 또는 constraint margin → shielded, recovery 또는 safe action`.
- 이 논문의 재사용 가능한 지점은 When the sensory inputs are high-dimensional images, latent dynamics models can abstract observations to predict forward in compact state spaces (Watter et al., 2015; Oh et al., 2017; Gregor et al., 2019).를 The representation model encodes observations and actions to create continuous vector-valued model states st with Markovian transitions (Watter et al., 2015; Zhang et al., 2019; Hafner et al., 2018).로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 safe set, recovery state 또는 constraint margin가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 2: Image observations for 5 of the 20 visual control tasks used in our experiments. The tasks pose a variety of challenges including contact dynamics, sparse rewards, many degrees of freedom, ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We present Dreamer, an agent that learns long-horizon behaviors from images purely by latent imagination.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `World models, safety, uncertainty, and recovery`; tags: `Robotics, world model, latent imagination, model-based reinforcement learning`.
- **Reading predecessor in the generated track queue:** Learning Latent Dynamics for Planning from Pixels (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Mastering Diverse Domains through World Models (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 2: Image observations for 5 of the 20 visual control tasks used in our experiments. The tasks pose a variety of challenges including contact dynamics, sparse rewards, many degrees of freedom, ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: These tasks pose a variety of challenges, including sparse rewards, contact dynamics, and 3D scenes..
3. Compare against the body-reported baseline or a matched simpler baseline: The training time for our Dreamer implementation is about 3 hours per 106 environment steps on the control suite, compared to 11 hours for online planning using PlaNet, and the 24 hours ....
4. Report the body metric and its denominator/aggregation: Figure 11: Comparison of representation learning methods for Dreamer. The lines show mean scores and the shaded areas show the standard deviation across 5 seeds. We compare generating both images and rewards, ....
5. Re-run the body-reported ablation/failure condition: PlaNet (Hafner et al., 2018) learns the same world model as Dreamer and selects actions via online planning without an action model and drastically improves over D4PG and A3C in data efficiency..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (B Sequence length), p. 2 (1 INTRODUCTION), p. 5 (B Sequence length); the primary result is directionally consistent at p. 8 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 present, Dreamer, agent mechanism이 The training time for our Dreamer implementation is about 3 hours per 106 environment steps on ... 대비 Figure 11: Comparison of representation learning methods for Dreamer. The lines show mean scores and the shaded areas ...을 개선하고, Figure 2: Image observations for 5 of the 20 visual control tasks used in our experiments. ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
