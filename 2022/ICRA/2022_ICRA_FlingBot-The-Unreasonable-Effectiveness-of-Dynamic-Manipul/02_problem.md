# Problem - FlingBot: The Unreasonable Effectiveness of Dynamic Manipulation for Cloth Unfolding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2105.03655; PDF retrieval source: https://arxiv.org/pdf/2105.03655. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction)): Additionally, since the robot arm cannot manipulate the cloth at locations it can't reach, the maximum cloth size is greatly limited by the robot arm's reach range.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** High-velocity dynamic actions (e.g., fling or throw) play a crucial role in our everyday interaction with deformable objects by improving our efficiency and effectively expanding ...
- **p. 1 / Abstract - extractive PDF cue:** Yet, most prior works have tackled cloth manipulation using exclusively single-arm quasi-static actions, which requires a large number of interactions for challenging initial cloth configurations ...
- **p. 1 / Abstract - extractive PDF cue:** In this work, we demonstrate the effectiveness of dynamic flinging actions for cloth unfolding with our proposed self-supervised learning framework, FlingBot.
- **p. 1 / Abstract - extractive PDF cue:** Our approach learns how to unfold a piece of fabric from arbitrary initial configurations using a pick, stretch, and fling primitive for a dual-arm setup ...
- **p. 1 / Abstract - extractive PDF cue:** The final system achieves over 80% coverage within 3 actions on novel cloths, can unfold cloths larger than the system's reach range, and generalizes to ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Additionally, since the robot arm cannot manipulate the cloth at locations it can't reach, the maximum cloth size is greatly limited by the robot arm's ...
- **p. 1 / 1 Introduction - extractive PDF cue:** From goal-conditioned folding [2] to fabric smoothing [3, 4], prior works have achieved success using exclusively single-arm quasistatic interactions (e.g., pick & place) for cloth ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Additionally, since the robot arm cannot manipulate the cloth at locations it can't reach, the maximum cloth size is greatly limited by ... | rigid/articulated object와 robot manipulator contact scene | body wording is the source claim |
| Observation / input | From a top-down RGB image a), our policy evaluates a batch of different action rotations and scales by transforming the observation b) ... | RGB-D/point cloud, object state와 contact/task observation | exact sensor/frame/preprocessing from PDF |
| State / latent | top-down, RGB, image, policy, evaluates, batch, different, action, rotations, scales | object geometry, affordance, contact mode 또는 end-effector state | notation and tensor shape require body check |
| Output / action | top-down, RGB, image, workspace, cloth, policy, decides, next | grasp, pose, force 또는 end-effector trajectory | exact unit/frame/decoder require body check |
| Target outcome | completion, contact success and robustness | task completion, contact success, pose/force error와 generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | object geometry/contact state; body terms: top-down, RGB, image, policy, evaluates, batch, different, action, rotations, scales | p. 5 (3 Method), p. 2 (1 Introduction), p. 3 (3 Method) |
| Decision / output variable | grasp/pose/force/trajectory; body terms: summary, main, contribution, demonstrating, effectiveness, dynamic, manipulation, cloth | p. 2 (1 Introduction), p. 4 (3 Method), p. 2 (1 Introduction) |
| Objective / loss / cost | task/contact/pose objective; cue terms: However, minimize, collisions, between, arms, wish, impose, constraint | p. 3 (3 Method), p. 4 (3 Method), p. 4 (3 Method), p. 5 (3 Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method) |
| Success / guarantee | completion, contact success and robustness | p. 9 (4.4 Results), p. 7 (4 Evaluation), p. 9 (4.4 Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive PDF cue:** From goal-conditioned folding [2] to fabric smoothing [3, 4], prior works have achieved success using exclusively single-arm quasistatic interactions (e.g., pick & place) for cloth ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Our approach is flexible to large cloths whose dimensions exceed the robot arm's reach ranges and generalizes to T-shirts despite being trained on rectangular cloths.

## What the Paper Changes

PDF contribution framing (p. 2 (1 Introduction), p. 4 (3 Method), p. 2 (1 Introduction), p. 5 (3 Method), p. 6 (3 Method)): In summary: • Our main contribution is in demonstrating the effectiveness of dynamic manipulation for cloth unfolding through our self-supervised learning framework, FlingBot. • We propose a parameterization for the ...

- **p. 4 / 3 Method - extractive PDF cue:** To make these constraints linear and independent, we propose an alternative 4-scalar parameterization, which consists of pixel position of the point C ∈R2 at the ...
- **p. 2 / 1 Introduction - extractive PDF cue:** To achieve this goal, we present FlingBot, a self-supervised algorithm that learns how to unfold cloths from arbitrary initial configurations using a pick, stretch, and ...
- **p. 5 / 3 Method - extractive PDF cue:** To this end, we propose to use spatial action maps [5, 6, 7].
- **p. 6 / 3 Method - extractive PDF cue:** Our real-world experiment setup consists of two UR5s, where one is equipped with a Schunk WSG50 and the other with an OnRobot RG2, facing each ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 13 | Figure 8: Failure Cases in Simulation Experiments. 6.3 Real world fling parameter robustness In designing our motion primitive, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | We discuss more of real world grasp failures in Sec. | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | The performance is reported averaged over 10 test episodes, where real-world grasp errors are filtered out (see "Real ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | Figure 6: Qualitative Results in Simulation Experiments. 6.2 Failure cases 1.0 1.2 1.4 1.6 Fling speed | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 5 (3 Method), p. 2 (1 Introduction), p. 3 (3 Method), p. 5 (3 Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), interface p. 5 (3 Method), p. 2 (1 Introduction), p. 3 (3 Method), p. 5 (3 Method), objective p. 3 (3 Method), p. 4 (3 Method), p. 4 (3 Method), p. 5 (3 Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
