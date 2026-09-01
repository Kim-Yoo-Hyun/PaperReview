# Problem - RT-Trajectory: Robotic Task Generalization via Hindsight Trajectory Sketches

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2311.01977; PDF retrieval source: https://arxiv.org/pdf/2311.01977. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): Recently, language conditioning significantly improves generalization to new language commands (Brohan et al., 2023b), but it suffers from the lack of specificity, which makes it difficult to generalize to a ...

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive PDF cue:** Generalization remains one of the most important desiderata for robust robot learning systems.
- **p. 1 / ABSTRACT - extractive PDF cue:** While recently proposed approaches show promise in generalization to novel objects, semantic concepts, or visual distribution shifts, generalization to new tasks remains challenging.
- **p. 1 / ABSTRACT - extractive PDF cue:** For example, a language-conditioned policy trained on pick-andplace tasks will not be able to generalize to a folding task, even if the arm trajectory of ...
- **p. 1 / ABSTRACT - extractive PDF cue:** Our key insight is that this kind of generalization becomes feasible if we represent the task through rough trajectory sketches.
- **p. 1 / ABSTRACT - extractive PDF cue:** We propose a policy conditioning method using such rough trajectory sketches, which we call RTTrajectory, that is practical, easy to specify, and allows the policy ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Recently, language conditioning significantly improves generalization to new language commands (Brohan et al., 2023b), but it suffers from the lack of specificity, which makes it ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Our experiments show that RT-Trajectory outperforms existing policy conditioning techniques, particularly in terms of generalization to novel motions, an open challenge in robotics.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Recently, language conditioning significantly improves generalization to new language commands (Brohan et al., 2023b), but it suffers from the lack of specificity, ... | multi-robot demonstration/dataset ecosystem | body wording is the source claim |
| Observation / input | Human Demonstration Videos with Hand-object Interaction First-person human demonstration videos are an alternative input. | multi-view observation, language/task label과 action trajectory | exact sensor/frame/preprocessing from PDF |
| State / latent | Human, Demonstration, Videos, Hand-object, Interaction, First-person, alternative, input, Behavior, Cloning | shared representation, embodiment/task identity와 data distribution | notation and tensor shape require body check |
| Output / action | episode, contains, sequence, pairs, observations, actions, OVERVIEW, goal | dataset sample 또는 learned policy action | exact unit/frame/decoder require body check |
| Target outcome | cross-domain transfer and task performance | coverage, cross-embodiment transfer, data efficiency와 task success | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | trajectory D with task/embodiment metadata; body terms: Human, Demonstration, Videos, Hand-object, Interaction, First-person, alternative, input, Behavior, Cloning | p. 5 (3 METHOD), p. 5 (3 METHOD), p. 4 (3 METHOD) |
| Decision / output variable | normalized sample or downstream action; body terms: main, contribution, novel, policy, conditioning, framework, RT-Trajectory, fosters | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (3 METHOD) |
| Objective / loss / cost | coverage/data efficiency/transfer objective; cue terms: Behavior, Cloning, Pomerleau, following, RT-1, framework, Brohan, minimizing | p. 5 (3 METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3 METHOD), p. 5 (3 METHOD), p. 4 (3 METHOD) |
| Success / guarantee | cross-domain transfer and task performance | p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 14 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Our experiments show that RT-Trajectory outperforms existing policy conditioning techniques, particularly in terms of generalization to novel motions, an open challenge in robotics.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** The pursuit of generalist robot policies has been a perennial challenge in robotics.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** The main contribution of this paper is a novel policy conditioning framework RT-Trajectory that fosters task generalization.

## What the Paper Changes

PDF contribution framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (3 METHOD), p. 4 (3 METHOD), p. 4 (3 METHOD)): The main contribution of this paper is a novel policy conditioning framework RT-Trajectory that fosters task generalization.

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** To this end, we propose to use a coarse trajectory as a middle-ground solution between expressiveness and ease of use.
- **p. 3 / 3 METHOD - extractive PDF cue:** We introduce three basic elements for constructing the trajectory representation format: 2D Trajectories, Color Grading, and Interaction Markers.
- **p. 4 / 3 METHOD - extractive PDF cue:** Trajectory Representations In this work, we propose two forms of trajectory representation from different combinations of the basic elements.
- **p. 4 / 3 METHOD - extractive PDF cue:** In the second representation, we introduce a more detailed trajectory representation RT-Trajectory (2.5D), which includes the height information in the 2D trajectory (Fig.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 22 | Figure 19: Case studies in prompt engineering. Each row shows the trajectory sketch overlaid on the first frame ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | We find that changing trajectory sketches induces RT-Trajectory to change behavior modes in a reproducible manner, which suggests ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Though we demonstrate that our proposed approach achieves encouraging generalization capabilities for novel manipulation tasks, there are a ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | 5 CONCLUSION AND LIMITATIONS In this work, we propose a novel policy-conditioning method for training robot manipulation policies ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

robot_data writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 5 (3 METHOD), p. 5 (3 METHOD), p. 4 (3 METHOD), p. 3 (3 METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), interface p. 5 (3 METHOD), p. 5 (3 METHOD), p. 4 (3 METHOD), p. 3 (3 METHOD), objective p. 5 (3 METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
