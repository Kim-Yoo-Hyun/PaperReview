# Problem - DiffSkill: Skill Abstraction from Differentiable Physics for Deformable Object Manipulations with Tools

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2203.17275; PDF retrieval source: https://arxiv.org/pdf/2203.17275. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION)): These differentiable simulators have facilitated gradient-based trajectory optimizers to find a motion trajectory with much fewer samples, compared with black box optimizers such as CEM or reinforcement learning algorithms (Huang ...

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** We consider the problem of sequential robotic manipulation of deformable objects using tools.
- **p. 1 / ABSTRACT - extractive body cue:** Previous works have shown that differentiable physics simulators provide gradients to the environment state and help trajectory optimization to converge orders of magnitude faster than ...
- **p. 1 / ABSTRACT - extractive body cue:** However, such gradient-based trajectory optimization typically requires access to the full simulator states and can only solve short-horizon, single-skill tasks due to local optima.
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we propose a novel framework, named DiffSkill, that uses a differentiable physics simulator for skill abstraction to solve long-horizon deformable object manipulation ...
- **p. 1 / ABSTRACT - extractive body cue:** In particular, we first obtain short-horizon skills using individual tools from a gradient-based optimizer, using the full state information in a differentiable simulator; we then ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** These differentiable simulators have facilitated gradient-based trajectory optimizers to find a motion trajectory with much fewer samples, compared with black box optimizers such as CEM ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** This work aims to narrow the gap and develop a method named DiffSkill that learns to use tools like a rolling pin, spatula, knife, etc., ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | These differentiable simulators have facilitated gradient-based trajectory optimizers to find a motion trajectory with much fewer samples, compared with black box optimizers ... | rigid/articulated object와 robot manipulator contact scene | body wording is the source claim |
| Observation / input | Our neural skill abstraction consists of a goal-conditioned policy that takes a sensory observation (RGB-D images in our case) as input, a ... | RGB-D/point cloud, object state와 contact/task observation | exact sensor/frame/preprocessing from PDF body |
| State / latent | neural, skill, abstraction, consists, goal-conditioned, policy, takes, sensory, observation, RGB-D | object geometry, affordance, contact mode 또는 end-effector state | notation and tensor shape require body check |
| Output / action | goal, learn, policy, perform, sequential, deformable, object, manipulation | grasp, pose, force 또는 end-effector trajectory | exact unit/frame/decoder require body check |
| Target outcome | completion, contact success and robustness | task completion, contact success, pose/force error와 generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | object geometry/contact state; body terms: neural, skill, abstraction, consists, goal-conditioned, policy, takes, sensory, observation, RGB-D | p. 4 (2 METHOD), p. 2 (1 INTRODUCTION), p. 2 (2 METHOD) |
| Decision / output variable | grasp/pose/force/trajectory; body terms: consists, three, components, trajectory, optimizer, acts, expert, applies | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (2 METHOD) |
| Objective / loss / cost | task/contact/pose objective; cue terms: Model, parameter, Value, dimension, latent, space, MLP, hidden | p. 5 (2 METHOD), p. 5 (2 METHOD), p. 14 (A IMPLEMENTATION DETAILS), p. 3 (2 METHOD), p. 3 (2 METHOD), p. 4 (2 METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (2 METHOD), p. 4 (2 METHOD), p. 3 (2 METHOD) |
| Success / guarantee | completion, contact success and robustness | p. 6 (3 EXPERIMENTS), p. 7 (Figure/Table caption), p. 6 (3 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 INTRODUCTION - extractive body cue:** This work aims to narrow the gap and develop a method named DiffSkill that learns to use tools like a rolling pin, spatula, knife, etc., ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** For example, while standard skills such as grasping an object or moving the robot arm from one pose to another may be manually specified (Toussaint ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** The recent development of differentiable physics simulators for deformable objects has shown promising results for solving soft-body control problems (Hu et al., 2019b; Murthy et ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (2 METHOD), p. 4 (2 METHOD), p. 1 (1 INTRODUCTION)): Our method consists of three components, (1) a trajectory optimizer that acts as an expert that applies gradient-based optimization on the differentiable simulator to obtain demonstration trajectories, which requires the ...

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To extend the use of differentiable physics models to these long-horizon tasks and enable the agent to directly consume visual observations, we propose DiffSkill: a ...
- **p. 4 / 2 METHOD - extractive body cue:** As such, we propose to learn a neural skill abstractor that learns skills from the demonstration videos of a trajectory optimizer; we will then leverage ...
- **p. 4 / 2 METHOD - extractive body cue:** Our neural skill abstraction consists of a goal-conditioned policy that takes a sensory observation (RGB-D images in our case) as input, a feasibility and reward ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** The recent development of differentiable physics simulators for deformable objects has shown promising results for solving soft-body control problems (Hu et al., 2019b; Murthy et ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | In Table 3, we can see that the learned skills (labeled as Behavior Cloning) approach the normalized performance ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | 3.4 RESULT ANALYSIS We show that DiffSkill is able to solve the challenging long-horizon, tool-use tasks from the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | On the other hand, if we do not optimize for the intermediate goals, we also cannot determine which ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | In this way, a normalized performance of 0 representing a policy that does nothing and a normalized performance ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (2 METHOD), p. 2 (1 INTRODUCTION), p. 2 (2 METHOD), p. 4 (2 METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), interface p. 4 (2 METHOD), p. 2 (1 INTRODUCTION), p. 2 (2 METHOD), p. 4 (2 METHOD), objective p. 5 (2 METHOD), p. 5 (2 METHOD), p. 14 (A IMPLEMENTATION DETAILS), p. 3 (2 METHOD), p. 3 (2 METHOD), p. 4 (2 METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** The recent development of differentiable physics simulators for deformable objects has shown promising results for solving soft-body control problems (Hu et al., 2019b; Murthy et al., 2020; Heiden et al., ... (p. 1, 1 INTRODUCTION).
- **Formulation-changing contribution:** To extend the use of differentiable physics models to these long-horizon tasks and enable the agent to directly consume visual observations, we propose DiffSkill: a novel framework where the agent ... (p. 2, 1 INTRODUCTION).
- **Assumption/failure evidence:** This threshold is manually picked by observing the performance gap between successful and failed trajectories. (p. 6, 3 EXPERIMENTS).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
