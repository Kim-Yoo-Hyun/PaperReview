# Problem - WoCoCo: Learning Whole-Body Humanoid Control with Sequential Contacts

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=Czs2xH9114; PDF retrieval source: https://arxiv.org/pdf/2406.06005. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 8 (1 Introduction), p. 5 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction), p. 2 (1 Introduction)): 6 Limitation and Future Works One limitation of our work is the lacking knowledge of when the controller will fail.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Humanoid activities involving sequential contacts are crucial for complex robotic interactions and operations in the real world and are traditionally solved by model-based motion planning, ...
- **p. 1 / Abstract - extractive body cue:** Although model-free reinforcement learning (RL) has become a powerful tool for versatile and robust whole-body humanoid control, it still requires tedious task-specific tuning and state ...
- **p. 1 / Abstract - extractive body cue:** In this work, we propose WoCoCo (Whole-Body Control with Sequential Contacts), a unified framework to learn whole-body humanoid control with sequential contacts by naturally decomposing ...
- **p. 1 / Abstract - extractive body cue:** Such decomposition facilitates simple and general policy learning pipelines through task-agnostic reward and sim-to-real designs, requiring only one or two task-related terms to be specified ...
- **p. 1 / Abstract - extractive body cue:** We demonstrated that endto-end RL-based controllers trained with WoCoCo enable four challenging wholebody humanoid tasks involving diverse contact sequences in the real world without any ...
- **p. 8 / 1 Introduction - extractive body cue:** 6 Limitation and Future Works One limitation of our work is the lacking knowledge of when the controller will fail.
- **p. 5 / 1 Introduction - extractive body cue:** However, model mismatch and perturbations such as uneven terrains pose significant challenges to these controllers, for which RL can be a promising solution [13, 22].

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | 6 Limitation and Future Works One limitation of our work is the lacking knowledge of when the controller will fail. | high-DoF humanoid whole-body dynamics와 contacts | body wording is the source claim |
| Observation / input | [28, 40], we stack 3 control steps of previous joint states and actions, and append them to the policy observations to enhance ... | proprioception, reference pose/motion, visual or language command | exact sensor/frame/preprocessing from PDF |
| State / latent | stack, control, steps, previous, joint, states, actions, append, them, policy | whole-body pose, balance/contact state와 skill/mode | notation and tensor shape require body check |
| Output / action | policy, observations, include, proprioception, exteroception, optional, goal-related, detailed | joint/whole-body action, motion target 또는 task trajectory | exact unit/frame/decoder require body check |
| Target outcome | motion/task success and recovery | tracking, balance, skill/task success와 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | whole-body pose/contact/reference state; body terms: stack, control, steps, previous, joint, states, actions, append, them, policy | p. 5 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction) |
| Decision / output variable | joint/whole-body action; body terms: Section, framework, WoCoCo, applied, variety, challenging, dynamic, tasks | p. 3 (1 Introduction), p. 5 (1 Introduction), p. 3 (1 Introduction) |
| Objective / loss / cost | tracking/balance/task objective; cue terms: objective, maximize, expected, return, finding, optimal, policy, st/gcon | p. 3 (1 Introduction), p. 5 (1 Introduction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 7 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Success / guarantee | motion/task success and recovery | p. 7 (Figure/Table caption), p. 2 (Figure/Table caption), p. 6 (1 Introduction) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 5 / 1 Introduction - extractive body cue:** However, model mismatch and perturbations such as uneven terrains pose significant challenges to these controllers, for which RL can be a promising solution [13, 22].
- **p. 2 / 1 Introduction - extractive body cue:** This drives the robot to explore further stages to maximize cumulative rewards, thus mitigating the shortsightedness caused by the RL policy strategically staying in the ...
- **p. 4 / 1 Introduction - extractive body cue:** Exploring new contact stages can come with failures and penalties, while staying at the current one may bring positive rewards.
- **p. 2 / 1 Introduction - extractive body cue:** This then transforms each challenge to a question: Q1: How to reach desired contact states within each stage?

## What the Paper Changes

PDF contribution framing (p. 3 (1 Introduction), p. 5 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction)): In Section 4, we show how our framework, WoCoCo, can be applied to a variety of challenging dynamic tasks with flexible definitions and representations of contact and task goals.

- **p. 5 / 1 Introduction - extractive body cue:** 4 Case Studies In this section, we show how our framework, WoCoCo, can be applied to various challenging tasks with different contact sequences.
- **p. 3 / 1 Introduction - extractive body cue:** In this paper, we study tasks where contact stages are predefined (e.g., heuristically designed), and our method can seamlessly be integrated with high-level contact planners ...
- **p. 2 / 1 Introduction - extractive body cue:** To better facilitate exploration, we propose a task-agnostic curiosity reward term.
- **p. 4 / 1 Introduction - extractive body cue:** Instead, we propose to use count-based curiosity rewards via random neural network (NN) based hash, inspired by Tang et al.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | 6 Limitation and Future Works One limitation of our work is the lacking knowledge of when the controller ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Therefore, we may explore failure predictors [56] and other safety assessment methods in the future [57]. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | The contact goal requires foot contact with the ground in their corresponding bounding boxes (predefined in the world ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | [44] use RL to learn double-foot jumping in the 3D space, yet their method does not support continuous ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

humanoid writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 5 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 8 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 8 (1 Introduction), p. 5 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction), p. 2 (1 Introduction), interface p. 5 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 8 (1 Introduction), objective p. 3 (1 Introduction), p. 5 (1 Introduction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
