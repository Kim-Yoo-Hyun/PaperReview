# Problem - Learning Neural Network Policies with Guided Policy Search under Unknown Dynamics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (40 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://jmlr.org/papers/v17/15-522.html; PDF retrieval source: https://jmlr.org/papers/volume17/15-522/15-522.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 7 (3.2 Approach Summary), p. 3 (1. Introduction)): However, designing the perception and control software for autonomous operation remains a major challenge, even for basic tasks.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Policy search methods can allow robots to learn control policies for a wide range of tasks, but practical applications of policy search often require hand-engineered ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we aim to answer the following question: does training the perception and control systems jointly end-toend provide better performance than training each ...
- **p. 1 / Abstract - extractive body cue:** To this end, we develop a method that can be used to learn policies that map raw image observations directly to torques at the robot's ...
- **p. 1 / Abstract - extractive body cue:** The policies are represented by deep convolutional neural networks (CNNs) with 92,000 parameters, and are trained using a guided policy search method, which transforms policy ...
- **p. 1 / Abstract - extractive body cue:** We evaluate our method on a range of real-world manipulation tasks that require close coordination between vision and control, such as screwing a cap onto ...
- **p. 1 / 1. Introduction - extractive body cue:** However, designing the perception and control software for autonomous operation remains a major challenge, even for basic tasks.
- **p. 2 / 1. Introduction - extractive body cue:** However, using deep neural networks for real-world sensorimotor policies, such as robotic controllers that map image pixels and joint angles to motor torques, presents a ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, designing the perception and control software for autonomous operation remains a major challenge, even for basic tasks. | robot/environment의 sequential decision process | body wording is the source claim |
| Observation / input | The policy is trained to predict the actions along each trajectory from the observations ot, rather than the full state xt. | state 또는 observation, action, reward와 transition history | exact sensor/frame/preprocessing from PDF body |
| State / latent | policy, trained, predict, actions, along, trajectory, observations, rather, full, state | policy/value state와 action-selection variable | notation and tensor shape require body check |
| Output / action | Since, training, complex, neural, networks, requires, substantial, number | action policy와 induced trajectory | exact unit/frame/decoder require body check |
| Target outcome | task return, success and safe execution | expected return, task success, stability와 sample efficiency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | s_t/o_t; body terms: policy, trained, predict, actions, along, trajectory, observations, rather, full, state | p. 8 (4. Guided Policy Search with BADMM), p. 12 (4.3 Supervised Policy Optimization), p. 12 (4.3 Supervised Policy Optimization) |
| Decision / output variable | a_t sampled or selected by πθ; body terms: methods, consists, main, components, illustrated, Figure, full, state | p. 5 (3.2 Approach Summary), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Objective / loss / cost | expected return / constrained return; cue terms: goal, task, given, cost, function, objective, policy, search | p. 12 (4.3 Supervised Policy Optimization), p. 12 (4.3 Supervised Policy Optimization), p. 11 (4.2 Trajectory Optimization under Unknown Dynamics), p. 5 (3.1 Definitions and Problem Formulation), p. 8 (4.1 Algorithm Derivation), p. 9 (4.1 Algorithm Derivation) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 8 (4.1 Algorithm Derivation), p. 8 (4.1 Algorithm Derivation), p. 11 (4.2 Trajectory Optimization under Unknown Dynamics) |
| Success / guarantee | task return, success and safe execution | p. 21 (6.3 Spatial Softmax CNN Architecture Evaluation), p. 21 (6.2 Learning Linear-Gaussian Controllers on a PR2 Robot), p. 23 (6.4 Deep Visuomotor Policy Evaluation) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** However, using deep neural networks for real-world sensorimotor policies, such as robotic controllers that map image pixels and joint angles to motor torques, presents a ...
- **p. 2 / 1. Introduction - extractive body cue:** We address these challenges by developing a guided policy search algorithm for sensorimotor deep learning, as well as a novel CNN architecture designed for robotic ...
- **p. 7 / 3.2 Approach Summary - extractive body cue:** Our network has 7 layers and around 92,000 parameters, which presents a major challenge for standard policy search methods (Deisenroth et al., 2013). initial controllers ...
- **p. 3 / 1. Introduction - extractive body cue:** End-to-End Training of Deep Visuomotor Policies number of prior methods when training high-dimensional neural network policies.

## What the Paper Changes

PDF body contribution framing (p. 5 (3.2 Approach Summary), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3. Background and Overview), p. 9 (4.1 Algorithm Derivation)): Our methods consists of two main components, which are illustrated in Figure 3.

- **p. 2 / 1. Introduction - extractive body cue:** In our method, the full state of the system is observable at training time, but not at test time.
- **p. 2 / 1. Introduction - extractive body cue:** Levine, Finn, Darrell, and Abbeel hanger cube hammer bottle Figure 1: Our method learns visuomotor policies that directly use camera image observations (left) to set ...
- **p. 5 / 3. Background and Overview - extractive body cue:** We also discuss a policy architecture suitable for end-to-end learning of vision and control, and a training setup that allows our method to be applied ...
- **p. 9 / 4.1 Algorithm Derivation - extractive body cue:** Minimization of the Lagrangian with respect to p(τ) and θ is done in alternating fashion: minimizing with respect to θ corresponds to supervised learning (making ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 27 | In many cases, this limitation is minor, and the only "instrumentation" required at training is to position the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 27 | A promising direction for addressing this limitation is to combine our method with unsupervised state-space learning, as proposed ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 23 | This suggests that the failure of this baseline is not atypical, and that our visuomotor policies are learning ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 26 | Although we demonstrate moderate generalization over variations in the scene, our current method does not generalize to dramatically ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

rl writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 8 (4. Guided Policy Search with BADMM), p. 12 (4.3 Supervised Policy Optimization), p. 12 (4.3 Supervised Policy Optimization), p. 5 (3.1 Definitions and Problem Formulation). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 7 (3.2 Approach Summary), p. 3 (1. Introduction), interface p. 8 (4. Guided Policy Search with BADMM), p. 12 (4.3 Supervised Policy Optimization), p. 12 (4.3 Supervised Policy Optimization), p. 5 (3.1 Definitions and Problem Formulation), objective p. 12 (4.3 Supervised Policy Optimization), p. 12 (4.3 Supervised Policy Optimization), p. 11 (4.2 Trajectory Optimization under Unknown Dynamics), p. 5 (3.1 Definitions and Problem Formulation), p. 8 (4.1 Algorithm Derivation), p. 9 (4.1 Algorithm Derivation).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (40 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, designing the perception and control software for autonomous operation remains a major challenge, even for basic tasks. (p. 1, 1. Introduction).
- **Formulation-changing contribution:** In our method, the full state of the system is observable at training time, but not at test time. (p. 2, 1. Introduction).
- **Assumption/failure evidence:** The graph shows the average distance travelled on rollouts that did not fall, and shows that only our method was able to learn walking policies that succeeded consistently. (p. 19, 6.1 Simulated Comparisons to Prior Policy Search Methods).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
