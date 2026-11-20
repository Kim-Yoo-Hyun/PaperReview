# Problem - RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (60 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2306.11706; PDF retrieval source: https://arxiv.org/pdf/2306.11706. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 8 (1 Introduction), p. 9 (1 Introduction), p. 11 (4.3 Evaluation), p. 2 (1 Introduction), p. 5 (1 Introduction)): In the real world, the shafts are metallic and the base is not fixed to the basket, which significantly increases the difficulty of the task.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** The ability to leverage heterogeneous robotic experience from different robots and tasks to quickly master novel skills and embodiments has the potential to transform robot ...
- **p. 1 / Abstract - extractive body cue:** Inspired by recent advances in foundation models for vision and language, we propose a multi-embodiment, multi-task generalist agent for robotic manipulation.
- **p. 1 / Abstract - extractive body cue:** This agent, named RoboCat, is a visual goal-conditioned decision transformer capable of consuming actionlabelled visual experience.
- **p. 1 / Abstract - extractive body cue:** This data spans a large repertoire of motor control skills from simulated and real robotic arms with varying sets of observations and actions.
- **p. 1 / Abstract - extractive body cue:** With RoboCat, we demonstrate the ability to generalise to new tasks and robots, both zero-shot as well as through adaptation using only 100-1000 examples for ...
- **p. 8 / 1 Introduction - extractive body cue:** In the real world, the shafts are metallic and the base is not fixed to the basket, which significantly increases the difficulty of the task.
- **p. 9 / 1 Introduction - extractive body cue:** They differ in difficulty, but in all cases require dexterous and precise movements to ensure that the structure remains stable after completion.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | In the real world, the shafts are metallic and the base is not fixed to the basket, which significantly increases the difficulty ... | multi-robot demonstration/dataset ecosystem | body wording is the source claim |
| Observation / input | Our agent handles these variations natively without requiring common action or observation representations, by leveraging the transformer's ability to input and output ... | multi-view observation, language/task label과 action trajectory | exact sensor/frame/preprocessing from PDF body |
| State / latent | agent, handles, variations, natively, without, requiring, common, action, observation, representations | shared representation, embodiment/task identity와 data distribution | notation and tensor shape require body check |
| Output / action | Concretely, tokenised, trajectory, represented, where, denote, number, tokens | dataset sample 또는 learned policy action | exact unit/frame/decoder require body check |
| Target outcome | cross-domain transfer and task performance | coverage, cross-embodiment transfer, data efficiency와 task success | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | trajectory D with task/embodiment metadata; body terms: agent, handles, variations, natively, without, requiring, common, action, observation, representations | p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction) |
| Decision / output variable | normalized sample or downstream action; body terms: main, contributions, outlined, below, demonstrate, first, time, large | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Objective / loss / cost | coverage/data efficiency/transfer objective; cue terms: Combining, action, observation, prediction, losses, token, level, obtain | p. 5 (1 Introduction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (1 Introduction), p. 5 (1 Introduction), p. 6 (1 Introduction) |
| Success / guarantee | cross-domain transfer and task performance | p. 12 (5 Experiments), p. 13 (5 Experiments), p. 55 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 9 / 1 Introduction - extractive body cue:** They differ in difficulty, but in all cases require dexterous and precise movements to ensure that the structure remains stable after completion.
- **p. 11 / 4.3 Evaluation - extractive body cue:** 4.4 Baselines In order to contextualise the difficulty of the tasks, we compare RoboCat to high capacity, pretrained vision foundation models (VFMs).
- **p. 2 / 1 Introduction - extractive body cue:** Specifically in robotics, recent works (Brohan et al., 2022; Driess et al., 2023) have focused on bridging the gap between large pretrained language models and ...
- **p. 5 / 1 Introduction - extractive body cue:** This capability is especially crucial in a real robotics context-unlike in simulation, data is bottlenecked by real-time operation per robot, and high-quality supervision is scarce.

## What the Paper Changes

PDF body contribution framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction)): Our main contributions in this work are outlined below: (1) we demonstrate, for the first time, that a large transformer sequence model can solve a large set of dexterous tasks ...

- **p. 2 / 1 Introduction - extractive body cue:** We introduce the embodiments, tasks, and object sets that we have used in this work in Section 3.
- **p. 3 / 1 Introduction - extractive body cue:** We describe our experimental setup for both training and evaluation in Section 4, before we present our extensive experiments to support our claims in Section ...
- **p. 3 / 1 Introduction - extractive body cue:** 2 RoboCat We introduce RoboCat, a self-improving generalist agent for robotic manipulation that can perform multiple tasks and control multiple embodiments in simulation and the ...
- **p. 4 / 1 Introduction - extractive body cue:** Specifically, the encoder is trained on a dataset that consists of images from ImageNet (Deng et al., 2009), images from the control tasks in Reed ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 20 | While visual goal specification already allows the agent to learn from failures and sub-optimal data, incorporating RL would ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 38 | Table 8: Quantities of human demonstrations and self-generated data. Embodiment Task Family Object Set Variant Human teleop demos ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 60 | Table 20: Skill transfer analysis. Average accumulated error over all three NIST-i gear sizes. Moving from the 364M ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 56 | Figure 27: The different types of NIST-i based environments we ablate performance against. Note, in the main paper ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

robot_data writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 6 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 8 (1 Introduction), p. 9 (1 Introduction), p. 11 (4.3 Evaluation), p. 2 (1 Introduction), p. 5 (1 Introduction), interface p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 6 (1 Introduction), objective p. 5 (1 Introduction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
