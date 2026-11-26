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

- **Paper-specific interface:** We define a discrete time step t, hidden states st, image observations ot, continuous action vectors at, and scalar rewards rt, that follow the stochastic dynamics Transition function: st ∼p(st ... (p. 2, 2. Latent Space Planning).
- **Paper-specific mechanism:** Key contributions of this work are summarized as follows: • Planning in latent spaces We solve a variety of tasks from the DeepMind control suite, shown in Figure 1, by ... (p. 1, 1. Introduction).
- **Evidence boundary:** the reported outcome is Figure 12: Planning performance on the cheetah running task with the true simulator using different planner settings. Performance ranges from 132 (blue) to 837 (yellow). Evaluating more action sequences, optimizing ... (p. 20, Figure/Table caption); the relevant task/metric cue is Iterative search for action sequences using CEM improves performance on all tasks. (p. 6, 5. Experiments). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Key difficulties include model inaccuracies, accumulating errors of multi-step predictions, failure to capture multiple possible futures, and overconfident predictions outside of the training distribution. (p. 1, 1. Introduction).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `World models, safety, uncertainty, and recovery`; tags: `Robotics, world model, Planning, latent dynamics`.
- **Reading predecessor in the generated track queue:** DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Dream to Control: Learning Behaviors by Latent Imagination (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Directions for future work include learning temporal abstraction instead of using a fixed action repeat, possibly through hierarchical models.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: We define a discrete time step t, hidden states st, image observations ot, continuous action vectors at, and scalar rewards rt, that follow the stochastic dynamics Transition function: st ∼p(st ... (p. 2, 2. Latent Space Planning); preserve the objective/update rule: Estimating the outer expectations using a single reparameterized sample yields an efficient objective for inference and learning in non-linear latent variable models that can be optimized using gradient ascent (Kingma ... (p. 4, 3. Recurrent State Space Model).
2. Use the paper-reported task/data/environment cue: After 500 episodes, it achieves performance similar to D4PG, trained from images for 100,000 episodes, except for the finger task. (p. 6, 5. Experiments).
3. Compare against the reported or matched baseline: The stochastic component is even more important - the agent does not learn without it. (p. 6, 5. Experiments).
4. Report the body metric with its denominator and aggregation: Iterative search for action sequences using CEM improves performance on all tasks. (p. 6, 5. Experiments).
5. Re-run the reported ablation or stress/failure condition: The stochastic component is even more important - the agent does not learn without it. (p. 6, 5. Experiments); if none is reported, design one around: Key difficulties include model inaccuracies, accumulating errors of multi-step predictions, failure to capture multiple possible futures, and overconfident predictions outside of the training distribution. (p. 1, 1. Introduction).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (1. Introduction), p. 1 (1. Introduction), match the reported outcome at p. 20 (Figure/Table caption), p. 6 (5. Experiments), p. 6 (5. Experiments), and measure the boundary at p. 1 (1. Introduction), p. 6 (5. Experiments).

## Falsifiable research question

Under the paper's stated interface (We define a discrete time step t, hidden states st, image observations ot, continuous action vectors at, and scalar rewards rt, that ...), does the paper-specific mechanism (Key contributions of this work are summarized as follows: • Planning in latent spaces We solve a variety of tasks from the ...) retain the reported evaluation outcome (Iterative search for action sequences using CEM improves performance on all tasks.) when tested against the paper's strongest explicit boundary (Key difficulties include model inaccuracies, accumulating errors of multi-step predictions, failure to capture multiple possible futures, and overconfident ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Iterative search for action sequences using CEM improves performance on all tasks.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (20 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Key contributions of this work are summarized as follows: • Planning in latent spaces We solve a variety of tasks from the DeepMind control suite, shown in Figure 1, by ... (p. 1, 1. Introduction).
- **Paper-supported outcome:** Figure 12: Planning performance on the cheetah running task with the true simulator using different planner settings. Performance ranges from 132 (blue) to 837 (yellow). Evaluating more action sequences, optimizing ... (p. 20, Figure/Table caption).
- **Strongest explicit boundary:** Key difficulties include model inaccuracies, accumulating errors of multi-step predictions, failure to capture multiple possible futures, and overconfident predictions outside of the training distribution. (p. 1, 1. Introduction).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
