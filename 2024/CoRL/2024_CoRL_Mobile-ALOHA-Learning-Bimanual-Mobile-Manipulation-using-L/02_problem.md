# Problem - Mobile ALOHA: Learning Bimanual Mobile Manipulation using Low-Cost Whole-Body Teleoperation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2401.02117; PDF retrieval source: https://arxiv.org/pdf/2401.02117. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction)): (1) We lack accessible, plug-and-play hardware for whole-body teleoperation.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Imitation learning from human demonstrations has shown impressive performance in robotics.
- **p. 1 / Abstract - extractive body cue:** However, most results focus on table-top manipulation, lacking the mobility and dexterity necessary for generally useful tasks.
- **p. 1 / Abstract - extractive body cue:** In this work, we develop a system for imitating mobile manipulation tasks that are bimanual and require whole-body control.
- **p. 1 / Abstract - extractive body cue:** We first present Mobile ALOHA, a low-cost and whole-body teleoperation system for data collection.
- **p. 1 / Abstract - extractive body cue:** It augments the ALOHA system [104] with a mobile base, and a whole-body teleoperation interface.
- **p. 2 / 1. Introduction - extractive body cue:** (1) We lack accessible, plug-and-play hardware for whole-body teleoperation.
- **p. 2 / 1. Introduction - extractive body cue:** We seek to tackle the challenges of applying imitation learning to bimanual mobile manipulation in this paper.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | (1) We lack accessible, plug-and-play hardware for whole-body teleoperation. | mobile base와 one/two-arm manipulation environment | body wording is the source claim |
| Observation / input | This observation is also consistent across different class of state-of-the-art imitation learning methods, including ACT [104] and Diffusion Policy [18]. | egocentric RGB-D, language/task goal, base-arm proprioception | exact sensor/frame/preprocessing from PDF |
| State / latent | observation, consistent, across, different, class, state-of-the-art, imitation, learning, methods, including | map/object/contact state와 base-arm coordination decision | notation and tensor shape require body check |
| Output / action | While, many, recent, works, demonstrate, highly, expressive, policy | base motion plus arm/gripper action | exact unit/frame/decoder require body check |
| Target outcome | task completion and recovery | long-horizon task success, reachability, collision과 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | base-arm-object state and language/task goal; body terms: observation, consistent, across, different, class, state-of-the-art, imitation, learning, methods, including | p. 2 (1. Introduction), p. 4 (3. Mobile ALOHA Hardware), p. 2 (1. Introduction) |
| Decision / output variable | base plus arm/gripper action; body terms: hardware, front, present, Mobile, ALOHA, low-cost, whole-body, teleoperation | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Objective / loss / cost | long-horizon task utility under reachability/contact constraints; cue terms: training, objective, mobile, manipulation, policy, task, aiarms, base | p. 5 (3. Mobile ALOHA Hardware), p. 6 (5. Tasks) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (1. Introduction), p. 3 (3. Mobile ALOHA Hardware), p. 3 (3. Mobile ALOHA Hardware) |
| Success / guarantee | task completion and recovery | p. 7 (Figure/Table caption), p. 8 (6.1. Co-training Improves Performance), p. 8 (6.1. Co-training Improves Performance) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** We seek to tackle the challenges of applying imitation learning to bimanual mobile manipulation in this paper.

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 4 (3. Mobile ALOHA Hardware), p. 1 (Abstract)): On the hardware front, we present Mobile ALOHA, a low-cost and whole-body teleoperation system for collecting bimanual mobile manipulation data.

- **p. 2 / 1. Introduction - extractive body cue:** The main contribution of this paper is a system for learning complex mobile bimanual manipulation tasks.
- **p. 1 / 1. Introduction - extractive body cue:** Imitation learning from human-provided demonstrations is a promising tool for developing generalist robots, as it allows people to teach arbitrary skills to robots.
- **p. 4 / 3. Mobile ALOHA Hardware - extractive body cue:** Connecting the operator to the mobile manipulator directly also enables coarse haptic feedback when the robot collides with objects.
- **p. 1 / Abstract - extractive body cue:** In this work, we develop a system for imitating mobile manipulation tasks that are bimanual and require whole-body control.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | Despite Mobile ALOHA's simplicity and performance, there are still limitations that we hope to address in future works. | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | Figure 2: Hardware Details. Left: Mobile ALOHA has two wrist cameras and one top camera, with onboard power ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | In all of these cases, compounding errors appear to be the main source of failure, either from the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | The main failure modes are imprecise grasping on Lift Glass and Wipe as well as jerky motion when ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

mobile_manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1. Introduction), p. 4 (3. Mobile ALOHA Hardware), p. 2 (1. Introduction), p. 4 (3. Mobile ALOHA Hardware). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 2 (1. Introduction), p. 4 (3. Mobile ALOHA Hardware), p. 2 (1. Introduction), p. 4 (3. Mobile ALOHA Hardware), objective p. 5 (3. Mobile ALOHA Hardware), p. 6 (5. Tasks).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
