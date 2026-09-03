# Problem - ArticuBot: Learning Universal Articulated Object Manipulation Policy via Large Scale Simulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p156.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p156.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION)): However, few have demonstrated generalization to manipulating many different articulated objects in the real world without simplifying assumptions (e.g, using a suction gripper (10).

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** This paper presents ArticuBot, in which a learned policy enables a robotics system to open diverse cate egories of unseen articulated objects in the real ...
- **p. 1 / Abstract - extractive body cue:** This task has long been challenging for robotics due to the large variations in the geometry, size, and articulation types of such objects.
- **p. 1 / Abstract - extractive body cue:** Our system, ArticuBot, consists of three parts: generating, a large number of demonstrations in physics-based simulation, distilling all generated demonstrations into a point cloud-based neural ...
- **p. 1 / Abstract - extractive body cue:** demonstrations over 322 training articulated objects.
- **p. 1 / Abstract - extractive body cue:** For policy learning, we propose a novel hierarchical policy representation,
- **p. 2 / 1. INTRODUCTION - extractive body cue:** However, few have demonstrated generalization to manipulating many different articulated objects in the real world without simplifying assumptions (e.g, using a suction gripper (10).
- **p. 2 / 1. INTRODUCTION - extractive body cue:** Many prior works have studied the problem of articulated object' manipulation [58 31, 10, 19, 21, 53, 15, 32].

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, few have demonstrated generalization to manipulating many different articulated objects in the real world without simplifying assumptions (e.g, using a suction ... | mobile base와 one/two-arm manipulation environment | body wording is the source claim |
| Observation / input | takes 3D point cloud as input and outputs delta endeffector transformations as the actions. + DP3 Transformer, which replaces the simplified PointNet ... | egocentric RGB-D, language/task goal, base-arm proprioception | exact sensor/frame/preprocessing from PDF body |
| State / latent | takes, point, cloud, input, outputs, delta, endeffector, transformations, actions, DP3 | map/object/contact state와 base-arm coordination decision | notation and tensor shape require body check |
| Output / action | Bottom, goal-conditioned, diffusion, policy, low-level, first, applies, attention | base motion plus arm/gripper action | exact unit/frame/decoder require body check |
| Target outcome | task completion and recovery | long-horizon task success, reachability, collision과 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | base-arm-object state and language/task goal; body terms: takes, point, cloud, input, outputs, delta, endeffector, transformations, actions, DP3 | p. 8 (B. Is a Hierarchical Policy Needed?), p. 7 (B. Policy Learning with a Hierarchical Policy Representation), p. 4 (2. Hierarchical Policy Learning -- Low-level Policy Architecture) |
| Decision / output variable | base plus arm/gripper action; body terms: Instead, hilrarchical, policy, representation, consists, high-level, low-level, present | p. 5 (B. Policy Learning with a Hierarchical Policy Representation), p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION) |
| Objective / loss / cost | long-horizon task utility under reachability/contact constraints; cue terms: Formally, high-level, policy, learned, minimizing, following, loss, goal | p. 5 (B. Policy Learning with a Hierarchical Policy Representation), p. 5 (B. Policy Learning with a Hierarchical Policy Representation), p. 6 (B. Policy Learning with a Hierarchical Policy Representation), p. 7 (B. Policy Learning with a Hierarchical Policy Representation) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (2. Hierarchical Policy Learning -- Low-level Policy Architecture), p. 6 (B. Policy Learning with a Hierarchical Policy Representation), p. 7 (B. Policy Learning with a Hierarchical Policy Representation) |
| Success / guarantee | task completion and recovery | p. 12 (C. Mobile X-Arm Results), p. 12 (B. Table-Top Franka Arm Results), p. 13 (C. Mobile X-Arm Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. INTRODUCTION - extractive body cue:** Many prior works have studied the problem of articulated object' manipulation [58 31, 10, 19, 21, 53, 15, 32].

## What the Paper Changes

PDF body contribution framing (p. 5 (B. Policy Learning with a Hierarchical Policy Representation), p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 3 (B. Sim2real Policy Learning), p. 4 (2. Hierarchical Policy Learning -- Low-level Policy Architecture)): Instead, we propose to use a hilrarchical policy representation, which consists of 4 high-level policy and a low-level policy.

- **p. 2 / 1. INTRODUCTION - extractive body cue:** ‘+ We present a weighted displacement policy representation that scales up well with the number of demonstrations, outperforming alternative policy representations.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** 1 for a visualization of some of the different real-world articulated objects that our policy is able to open, In summary, our contributions are:
- **p. 3 / B. Sim2real Policy Learning - extractive body cue:** In contrast, we train a single model that ean be applied to opening various categories of articulated objects Besides, their system requires a specialized gripper, ...
- **p. 4 / 2. Hierarchical Policy Learning -- Low-level Policy Architecture - extractive body cue:** Middle: We propose a weighted displacement model for the high-level policy, which predicts the sub-goal end-effector pose.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 13 | See Appendix L for visualizations of some of the failure cases of ArticuBot, and some basic failure recovery ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 13 | We leave addressing these limitations as important future work. | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | Common failure ceases for table-top experiments include: 1, The robot arm runs to joint limits while opening the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | The major failure case for FlowBot3D is that the predicted flow is in the wrong direction, e.g., it ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

mobile_manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 8 (B. Is a Hierarchical Policy Needed?), p. 7 (B. Policy Learning with a Hierarchical Policy Representation), p. 4 (2. Hierarchical Policy Learning -- Low-level Policy Architecture), p. 5 (B. Policy Learning with a Hierarchical Policy Representation). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), interface p. 8 (B. Is a Hierarchical Policy Needed?), p. 7 (B. Policy Learning with a Hierarchical Policy Representation), p. 4 (2. Hierarchical Policy Learning -- Low-level Policy Architecture), p. 5 (B. Policy Learning with a Hierarchical Policy Representation), objective p. 5 (B. Policy Learning with a Hierarchical Policy Representation), p. 5 (B. Policy Learning with a Hierarchical Policy Representation), p. 6 (B. Policy Learning with a Hierarchical Policy Representation), p. 7 (B. Policy Learning with a Hierarchical Policy Representation).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
