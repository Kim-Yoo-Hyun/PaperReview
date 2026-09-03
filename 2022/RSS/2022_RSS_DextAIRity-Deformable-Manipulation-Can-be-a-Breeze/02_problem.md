# Problem - DextAIRity: Deformable Manipulation Can be a Breeze

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2203.01197; PDF retrieval source: https://arxiv.org/pdf/2203.01197. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): However, despite the potential advantages of air-based manipulation, it is an open and challenging problem.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** This paper introduces DextAIRity, an approach to manipulate deformable objects using active airflow.
- **p. 1 / Abstract - extractive body cue:** In contrast to conventional contact-based quasi-static manipulations, DextAIRity allows the system to apply dense forces on out-ofcontact surfaces, expands the system's reach range, and provides ...
- **p. 1 / Abstract - extractive body cue:** These properties are particularly advantageous when manipulating under-actuated deformable objects with large surface areas or volumes.
- **p. 1 / Abstract - extractive body cue:** We demonstrate the effectiveness of DextAIRity through two challenging deformable object manipulation tasks: cloth unfolding and bag opening.
- **p. 1 / Abstract - extractive body cue:** We present a self-supervised learning framework that learns to effectively perform a target task through a sequence of grasping or air-based blowing actions.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, despite the potential advantages of air-based manipulation, it is an open and challenging problem.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Both challenges motivate a self-supervised closed-loop solution for DextAIRity that could learn and improve from data.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, despite the potential advantages of air-based manipulation, it is an open and challenging problem. | rigid/articulated object와 robot manipulator contact scene | body wording is the source claim |
| Observation / input | Observation Blowing Scores Blowing Network max Execution Cloth unfolding Grasp (a) Grasping Policy (Cloth Unfolding) Stretch Place Initial State Bag opening ×8 ... | RGB-D/point cloud, object state와 contact/task observation | exact sensor/frame/preprocessing from PDF body |
| State / latent | Observation, Blowing, Scores, Network, Execution, Cloth, unfolding, Grasp, Grasping, Policy | object geometry, affordance, contact mode 또는 end-effector state | notation and tensor shape require body check |
| Output / action | blowing, step, network, takes, top-down, observation, input, infers | grasp, pose, force 또는 end-effector trajectory | exact unit/frame/decoder require body check |
| Target outcome | completion, contact success and robustness | task completion, contact success, pose/force error와 generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | object geometry/contact state; body terms: Observation, Blowing, Scores, Network, Execution, Cloth, unfolding, Grasp, Grasping, Policy | p. 4 (IV. METHOD), p. 5 (IV. METHOD), p. 4 (IV. METHOD) |
| Decision / output variable | grasp/pose/force/trajectory; body terms: system, setup, consists, three, UR5, robot, arms, equipped | p. 2 (I. INTRODUCTION), p. 4 (IV. METHOD), p. 1 (I. INTRODUCTION) |
| Objective / loss / cost | task/contact/pose objective; cue terms: total, collected, training, validation, interactions, over, course, hours | p. 4 (IV. METHOD), p. 4 (IV. METHOD), p. 5 (IV. METHOD), p. 5 (IV. METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (IV. METHOD), p. 4 (IV. METHOD), p. 5 (IV. METHOD) |
| Success / guarantee | completion, contact success and robustness | p. 7 (V. EVALUATION), p. 8 (V. EVALUATION), p. 8 (V. EVALUATION) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** Both challenges motivate a self-supervised closed-loop solution for DextAIRity that could learn and improve from data.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We also discuss the potential limitations and necessary considerations of deploying DextAIRity in real-world applications.

## What the Paper Changes

PDF body contribution framing (p. 2 (I. INTRODUCTION), p. 4 (IV. METHOD), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): Our system setup consists of (a) three UR5 robot arms, two of which are equipped with parallel-jaw grippers and one with a commodity centrifugal air pump.

- **p. 4 / IV. METHOD - extractive body cue:** The blowing network consists of an image encoder (7-layer convolution network) and an action encoder (3-layer MLP), followed by a 3-layer MLP to produce the ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** This property particularly is useful when the target object has a large volume or surface area - spreading a large piece of cloth for instance ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** The primary contribution of this work is to suggest a new approach for deformable object manipulation utilizing directed airstreams, DextAIRity.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Instead of applying force through sparse contact positions, DextAIRity allows the system to simultaneously apply dense forces to a 3D space.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | While in this paper we demonstrate the effectiveness of directed air to manipulate deformable objects, we discuss a ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | The failure of [FlingBot] is due to its limited move speed, which needs to Large Rect X-Large Rect ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Fig. 10: Failure Cases. (a) A corner is inadvertently rolled up due to Eddy effects. (b) Multiple layers ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Overall, we find that quasi-static pick-and-place actions are generally inefficient for cloth unfolding and, while dynamic actions such ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (IV. METHOD), p. 5 (IV. METHOD), p. 4 (IV. METHOD), p. 2 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 4 (IV. METHOD), p. 5 (IV. METHOD), p. 4 (IV. METHOD), p. 2 (I. INTRODUCTION), objective p. 4 (IV. METHOD), p. 4 (IV. METHOD), p. 5 (IV. METHOD), p. 5 (IV. METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
