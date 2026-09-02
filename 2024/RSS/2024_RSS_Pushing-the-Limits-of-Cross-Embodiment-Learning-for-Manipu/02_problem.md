# Problem - Pushing the Limits of Cross-Embodiment Learning for Manipulation and Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p093.html; PDF retrieval source: https://arxiv.org/pdf/2402.19432.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. PRELIMINARIES)): However, these prior works typically restrict their investigations to sets of similar embodiments - e.g., arms with parallel jaw grippers.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Recent years in robotics and imitation learning have shown remarkable progress in training large-scale foundation models by leveraging data across a multitude of embodiments.
- **p. 1 / Abstract - extractive body cue:** The success of such policies might lead us to wonder: just how diverse can the robots in the training set be while still facilitating positive ...
- **p. 1 / Abstract - extractive body cue:** In this work, we study this question in the context of heterogeneous embodiments, examining how even seemingly very different domains, such as robotic navigation and ...
- **p. 1 / Abstract - extractive body cue:** We train a single goalconditioned policy that is capable of controlling robotic arms, quadcopters, quadrupeds, and mobile bases.
- **p. 1 / Abstract - extractive body cue:** We then investigate the extent to which transfer can occur across navigation and manipulation on these embodiments by framing them as a single goal-reaching task.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, these prior works typically restrict their investigations to sets of similar embodiments - e.g., arms with parallel jaw grippers.
- **p. 1 / I. INTRODUCTION - extractive body cue:** The advent of large-scale foundation models in machine learning has enabled harnessing diverse datasets to enhance sample efficiency, improve generalization, and facilitate transfer to novel ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, these prior works typically restrict their investigations to sets of similar embodiments - e.g., arms with parallel jaw grippers. | mobile base와 one/two-arm manipulation environment | body wording is the source claim |
| Observation / input | The objective of goal-conditioned imitation learning is to train a policy π(a/o, og) to output actions that control a particular embodiment given ... | egocentric RGB-D, language/task goal, base-arm proprioception | exact sensor/frame/preprocessing from PDF body |
| State / latent | objective, goal-conditioned, imitation, learning, train, policy, output, actions, control, particular | map/object/contact state와 base-arm coordination decision | notation and tensor shape require body check |
| Output / action | action, output, head, chose, diffusion, policy, account, noise | base motion plus arm/gripper action | exact unit/frame/decoder require body check |
| Target outcome | task completion and recovery | long-horizon task success, reachability, collision과 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | base-arm-object state and language/task goal; body terms: objective, goal-conditioned, imitation, learning, train, policy, output, actions, control, particular | p. 3 (III. PRELIMINARIES), p. 3 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 5 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING) |
| Decision / output variable | base plus arm/gripper action; body terms: While, particular, training, methodology, model, architecture, prior, techniques | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. PRELIMINARIES) |
| Objective / loss / cost | long-horizon task utility under reachability/contact constraints; cue terms: overall, objective, weighted, combination, losses, Ldiffusion, Ldistance, Note | p. 5 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 3 (III. PRELIMINARIES), p. 3 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 4 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 4 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 5 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 4 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 5 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING) |
| Success / guarantee | task completion and recovery | p. 8 (Figure/Table caption), p. 7 (VI. ANALYSIS), p. 7 (VI. ANALYSIS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** The advent of large-scale foundation models in machine learning has enabled harnessing diverse datasets to enhance sample efficiency, improve generalization, and facilitate transfer to novel ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We finally show that our policy can generalize to two new robots: a mobile manipulator and a quadrotor, without any data specific to these embodiments.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Similarly, in visual navigation, the robot examines the spatial relationship between its current location and goal, as inferred from image observations, and determines how to ...
- **p. 3 / III. PRELIMINARIES - extractive body cue:** In addition, the agent predicts a distance function d(·/ot-k:t, og) to determine the distance between its current observation and its goal.

## What the Paper Changes

PDF body contribution framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. PRELIMINARIES), p. 3 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 1 (I. INTRODUCTION)): While the particular training methodology and model architecture are based on prior techniques, the empirical findings are a novel contribution of our work, demonstrating for the first time that navigation ...

- **p. 2 / I. INTRODUCTION - extractive body cue:** We present, to our knowledge, the first results demonstrating a large-scale policy trained jointly on navigation and manipulation data from many different robots, showing that ...
- **p. 3 / III. PRELIMINARIES - extractive body cue:** Each trajectory τ ∈Dem consists of a sequence of observations (images) and actions.
- **p. 3 / IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING - extractive body cue:** While we could simply train a single policy across all of the navigation and manipulation datasets to output action labels that match each specific dataset ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** The advent of large-scale foundation models in machine learning has enabled harnessing diverse datasets to enhance sample efficiency, improve generalization, and facilitate transfer to novel ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Gauging object distance is analogous to testing the robustness to a change in table height in tabletop manipulation, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | This requires the robot to avoid colliding with the shelf as well as gauge its distance to the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | While we qualitatively observed that these policies had better estimates for the closest node and had less collision ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | However, small changes in the mobile base can elicit large changes in position of the robot arm with ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

mobile_manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (III. PRELIMINARIES), p. 3 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 5 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 7 (VI. ANALYSIS). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. PRELIMINARIES), interface p. 3 (III. PRELIMINARIES), p. 3 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 5 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 7 (VI. ANALYSIS), objective p. 5 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 3 (III. PRELIMINARIES), p. 3 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 4 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 4 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 5 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
