# Problem - Recovery RL: Safe Reinforcement Learning with Learned Recovery Zones

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2010.15920; PDF retrieval source: https://arxiv.org/pdf/2010.15920. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. PROBLEM STATEMENT)): However, when deploying RL agents in the real world, unconstrained exploration can result in highly suboptimal behaviors which can damage the robot, break surroundings objects, or bottleneck the learning process.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Safety remains a central obstacle preventing widespread use of RL in the real world: learning new tasks in uncertain environments requires extensive exploration, but safety ...
- **p. 1 / Abstract - extractive body cue:** We propose Recovery RL, an algorithm which navigates this tradeoff by (1) leveraging offline data to learn about constraint violating zones before policy learning and ...
- **p. 1 / Abstract - extractive body cue:** We evaluate Recovery RL on 6 simulation domains, including two contact-rich manipulation tasks and an imagebased navigation task, and an image-based obstacle avoidance task on ...
- **p. 1 / Abstract - extractive body cue:** We compare Recovery RL to 5 prior safe RL methods which jointly optimize for task performance and safety via constrained optimization or reward shaping and ...
- **p. 1 / Abstract - extractive body cue:** Results suggest that Recovery RL trades off constraint violations and task successes 2 - 20 times more efficiently in simulation domains and 3 times more ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, when deploying RL agents in the real world, unconstrained exploration can result in highly suboptimal behaviors which can damage the robot, break surroundings objects, ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** While these approaches are appealing for their generality and simplicity, there are two key aspects which make them difficult to use in practice.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, when deploying RL agents in the real world, unconstrained exploration can result in highly suboptimal behaviors which can damage the robot, ... | uncertain robot state와 safe/unsafe operating region | body wording is the source claim |
| Observation / input | We present an algorithm to optimize equation (III.1) by utilizing a pair of policies, a task policy πtask, which is trained to ... | observation, uncertainty/risk estimate와 task command | exact sensor/frame/preprocessing from PDF body |
| State / latent | present, algorithm, optimize, equation, III, utilizing, pair, policies, task, policy | safe set, recovery state 또는 constraint margin | notation and tensor shape require body check |
| Output / action | Safe, exploration, poses, tradeoff, learning, skills, through, environmental | shielded, recovery 또는 safe action | exact unit/frame/decoder require body check |
| Target outcome | low violation/failure probability with useful intervention | task return과 violation/failure probability | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | state/history and risk h(s); body terms: present, algorithm, optimize, equation, III, utilizing, pair, policies, task, policy | p. 3 (III. PROBLEM STATEMENT), p. 4 (IV. RECOVERY RL), p. 1 (I. INTRODUCTION) |
| Decision / output variable | filtered/recovery action u_safe; body terms: Thus, endowing, agents, ability, satisfy, constraints, during, learning | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (Abstract) |
| Objective / loss / cost | task utility subject to safety constraint; cue terms: train, risk, minimizing, following, MSE, loss, respect, target | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. PROBLEM STATEMENT), p. 4 (IV. RECOVERY RL) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (I. INTRODUCTION), p. 1 (Abstract), p. 2 (I. INTRODUCTION) |
| Success / guarantee | low violation/failure probability with useful intervention | p. 5 (V. EXPERIMENTS), p. 12 (Figure/Table caption), p. 12 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive body cue:** While these approaches are appealing for their generality and simplicity, there are two key aspects which make them difficult to use in practice.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Most prior work in safe RL integrates constraint satisfaction into the task objective to ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We evaluate Recovery RL on an imagebased obstacle avoidance task on a physical robot and find that it trades off constraint violations and task successes ...
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** Setting εrisk = 0 as well results in a robust optimal control problem.

## What the Paper Changes

PDF body contribution framing (p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (Abstract), p. 3 (III. PROBLEM STATEMENT), p. 2 (I. INTRODUCTION)): Thus, endowing RL agents with the ability to satisfy constraints during learning not only enables robots to interact safely, but also allows them to more efficiently learn in the real ...

- **p. 2 / I. INTRODUCTION - extractive body cue:** We present Recovery RL, a new algorithm for safe robotic RL.
- **p. 1 / Abstract - extractive body cue:** We propose Recovery RL, an algorithm which navigates this tradeoff by (1) leveraging offline data to learn about constraint violating zones before policy learning and ...
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** We present an algorithm to optimize equation (III.1) by utilizing a pair of policies, a task policy πtask, which is trained to maximize Rπ over ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Separating the task and recovery policies makes it easier to balance task performance and safety, and allows using off-the-shelf RL algorithms for both.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | In all navigation tasks, we find that Recovery RL significantly outperforms prior methods with both model-free and model-based ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | We hypothesize that the model-based recovery mechanism is better able to compensate for approximation errors in ˆQπ φ,risk, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Figure 7. Results suggest that Recovery RL performs much more poorly when πrec and ˆQπ φ,risk are not ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 14 | Figure 12: Physical Experiment Reward Learning Curve: We show the total reward attained in each episode smoothed over ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

safety writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (III. PROBLEM STATEMENT), p. 4 (IV. RECOVERY RL), p. 1 (I. INTRODUCTION), p. 1 (Abstract). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. PROBLEM STATEMENT), interface p. 3 (III. PROBLEM STATEMENT), p. 4 (IV. RECOVERY RL), p. 1 (I. INTRODUCTION), p. 1 (Abstract), objective p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. PROBLEM STATEMENT), p. 4 (IV. RECOVERY RL).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, when deploying RL agents in the real world, unconstrained exploration can result in highly suboptimal behaviors which can damage the robot, break surroundings objects, or bottleneck the learning process. (p. 1, I. INTRODUCTION).
- **Formulation-changing contribution:** Thus, endowing RL agents with the ability to satisfy constraints during learning not only enables robots to interact safely, but also allows them to more efficiently learn in the real ... (p. 1, I. INTRODUCTION).
- **Assumption/failure evidence:** We then study the sensitivity of Recovery RL to the number of offline transitions used to pretrain πrec and ˆQπ φ,risk (right) and find that Recovery RL performs well even ... (p. 7, V. EXPERIMENTS).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
