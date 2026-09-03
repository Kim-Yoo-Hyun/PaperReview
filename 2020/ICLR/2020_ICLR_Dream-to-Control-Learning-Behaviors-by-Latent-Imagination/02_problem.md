# Problem - Dream to Control: Learning Behaviors by Latent Imagination

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1912.01603; PDF retrieval source: https://arxiv.org/pdf/1912.01603. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 3 (1 INTRODUCTION)): We approach this limitation by predicting both actions and state values.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Learned world models summarize an agent's experience to facilitate learning complex behaviors.
- **p. 1 / Abstract - extractive body cue:** While learning world models from high-dimensional sensory inputs is becoming feasible through deep learning, there are many potential ways for deriving behaviors from them.
- **p. 1 / Abstract - extractive body cue:** We present Dreamer, a reinforcement learning agent that solves long-horizon tasks from images purely by latent imagination.
- **p. 1 / Abstract - extractive body cue:** We efficiently learn behaviors by propagating analytic gradients of learned state values back through trajectories imagined in the compact state space of a learned world ...
- **p. 1 / Abstract - extractive body cue:** On 20 challenging visual control tasks, Dreamer exceeds existing approaches in data-efficiency, computation time, and final performance.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We approach this limitation by predicting both actions and state values.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The tasks pose a variety of challenges including contact dynamics, sparse rewards, many degrees of freedom, and 3D environments.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | We approach this limitation by predicting both actions and state values. | uncertain robot state와 safe/unsafe operating region | body wording is the source claim |
| Observation / input | When the sensory inputs are high-dimensional images, latent dynamics models can abstract observations to predict forward in compact state spaces (Watter et ... | observation, uncertainty/risk estimate와 task command | exact sensor/frame/preprocessing from PDF body |
| State / latent | When, sensory, inputs, high-dimensional, images, latent, dynamics, models, abstract, observations | safe set, recovery state 또는 constraint margin | notation and tensor shape require body check |
| Output / action | dataset, past, experience, agent, learns, encode, observations, actions | shielded, recovery 또는 safe action | exact unit/frame/decoder require body check |
| Target outcome | low violation/failure probability with useful intervention | task return과 violation/failure probability | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | state/history and risk h(s); body terms: When, sensory, inputs, high-dimensional, images, latent, dynamics, models, abstract, observations | p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| Decision / output variable | filtered/recovery action u_safe; body terms: present, Dreamer, agent, learns, long-horizon, behaviors, images, purely | p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Objective / loss / cost | task utility subject to safety constraint; cue terms: values, optimize, Bellman, consistency, imagined, rewards, policy, maximizes | p. 5 (B Sequence length), p. 2 (1 INTRODUCTION), p. 5 (B Sequence length), p. 1 (1 INTRODUCTION), p. 1 (Abstract), p. 2 (1 INTRODUCTION) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Success / guarantee | low violation/failure probability with useful intervention | p. 18 (Figure/Table caption), p. 2 (Figure/Table caption), p. 9 (6 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 INTRODUCTION - extractive body cue:** The tasks pose a variety of challenges including contact dynamics, sparse rewards, many degrees of freedom, and 3D environments.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** This ability requires building representations of the world from past experience that enable generalization to novel situations.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Moreover, prior work commonly resorts to derivative-free optimization for robustness to model errors (Ebert et al., 2017; Chua et al., 2018; Parmas et al., 2019), ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** (c) The agent encodes the history of the episode to compute the current model state and predict the next action to execute in the environment.

## What the Paper Changes

PDF body contribution framing (p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION)): We present Dreamer, an agent that learns long-horizon behaviors from images purely by latent imagination.

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Latent dynamics Dreamer uses a latent dynamics model that consists of three components.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Compared to predictions in image space, latent states have a small memory footprint that enables imagining thousands of trajectories in parallel.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The key contributions of this paper are summarized as follows: • Learning long-horizon behaviors by latent imagination Model-based agents can be shortsighted if they use ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** This section describes the main contribution of our paper.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 2 | Figure 2: Image observations for 5 of the 20 visual control tasks used in our experiments. The tasks ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 16 | Figure 9: Performance of Dreamer in environments with discrete actions and early termination. Dreamer learns successful behaviors on ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Figure 4: Imagination horizons. We compare the final performance of Dreamer, learning an action model without value prediction, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 19 | Figure 12: Robustness of Dreamer to different control frequencies. Reinforcement learning methods can be sensitive to this hyper ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

safety writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 6 (B Sequence length). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), interface p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 6 (B Sequence length), objective p. 5 (B Sequence length), p. 2 (1 INTRODUCTION), p. 5 (B Sequence length), p. 1 (1 INTRODUCTION), p. 1 (Abstract), p. 2 (1 INTRODUCTION).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (20 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** We approach this limitation by predicting both actions and state values. (p. 2, 1 INTRODUCTION).
- **Formulation-changing contribution:** The key contributions of this paper are summarized as follows: • Learning long-horizon behaviors by latent imagination Model-based agents can be shortsighted if they use a finite imagination horizon. (p. 2, 1 INTRODUCTION).
- **Assumption/failure evidence:** We approach this limitation by predicting both actions and state values. (p. 2, 1 INTRODUCTION).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
