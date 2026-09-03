# Problem - Relay Policy Learning: Solving Long-Horizon Tasks via Imitation and Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v100/gupta20a.html; PDF retrieval source: https://arxiv.org/pdf/1910.11956. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 5 (3 Preliminaries), p. 6 (3 Preliminaries), p. 6 (3 Preliminaries), p. 7 (3 Preliminaries)): However, HRL methods have traditionally struggled due to various practical challenges such as exploration [5], skill segmentation [6] and reward definition [7].

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We present relay policy learning, a method for imitation and reinforcement learning that can solve multi-stage, long-horizon robotic tasks.
- **p. 1 / Abstract - extractive body cue:** This general and universally-applicable, two-phase approach consists of an imitation learning stage that produces goal-conditioned hierarchical policies, and a reinforcement learning phase that finetunes these ...
- **p. 1 / Abstract - extractive body cue:** Our method, while not necessarily perfect at imitation learning, is very amenable to further improvement via environment interaction, allowing it to scale to challenging longhorizon ...
- **p. 1 / Abstract - extractive body cue:** We simplify the long-horizon policy learning problem by using a novel data-relabeling algorithm for learning goal-conditioned hierarchical policies, where the low-level only acts for a ...
- **p. 1 / Abstract - extractive body cue:** While we rely on demonstration data to bootstrap policy learning, we do not assume access to demonstrations of every specific tasks that is being solved, ...
- **p. 1 / 1 Introduction - extractive body cue:** However, HRL methods have traditionally struggled due to various practical challenges such as exploration [5], skill segmentation [6] and reward definition [7].
- **p. 5 / 3 Preliminaries - extractive body cue:** Reinforcement learning provides a solution to this challenge, by enabling continuous improvement of the learned policy directly from experience.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, HRL methods have traditionally struggled due to various practical challenges such as exploration [5], skill segmentation [6] and reward definition [7]. | demonstration으로 정의된 robot task distribution | body wording is the source claim |
| Observation / input | 7: end while 8: Distill fine-tuned policies into a single multi-goal policy Algorithm 2 Relay data relabeling for RIL low level Require: ... | observation history와 expert trajectory/action | exact sensor/frame/preprocessing from PDF body |
| State / latent | while, Distill, fine-tuned, policies, single, multi-goal, policy, Algorithm, Relay, data | behavior policy와 temporal action context | notation and tensor shape require body check |
| Output / action | However, actions, high, level, subgoal, states, provided, low-level | predicted action 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | closed-loop task success and robustness | imitation error, task success, robustness와 compounding error | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | observation history o_{t−H:t}; body terms: while, Distill, fine-tuned, policies, single, multi-goal, policy, Algorithm, Relay, data | p. 4 (3 Preliminaries), p. 3 (3 Preliminaries), p. 5 (3 Preliminaries) |
| Decision / output variable | expert-like action/chunk a_{t:t+H}; body terms: Lastly, most, importantly, since, ensures, every, low-level, trajectory | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (3 Preliminaries) |
| Objective / loss / cost | imitation or action-distribution loss; cue terms: high-level, policy, given, goal-reaching, reward, function, optimize, running | p. 4 (3 Preliminaries), p. 5 (3 Preliminaries), p. 3 (3 Preliminaries), p. 5 (3 Preliminaries), p. 6 (3 Preliminaries), p. 6 (3 Preliminaries) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3 Preliminaries), p. 4 (3 Preliminaries), p. 1 (1 Introduction) |
| Success / guarantee | closed-loop task success and robustness | p. 7 (3 Preliminaries), p. 7 (3 Preliminaries), p. 8 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 5 / 3 Preliminaries - extractive body cue:** Reinforcement learning provides a solution to this challenge, by enabling continuous improvement of the learned policy directly from experience.
- **p. 6 / 3 Preliminaries - extractive body cue:** This allows us to learn a single policy capable of achieving multiple high level goals, without dealing with the challenges of multi-task optimization.
- **p. 6 / 3 Preliminaries - extractive body cue:** [33], it is often difficult to learn multiple tasks together with on-policy policy gradient methods, because of high variance and conflicting gradients.
- **p. 7 / 3 Preliminaries - extractive body cue:** The last baseline is representative of a class of HIL algorithms [23, 24, 26], which are difficult to fine-tune because it is not clear how ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (3 Preliminaries), p. 1 (Abstract), p. 1 (Abstract)): Lastly, and most importantly, since our method ensures that every low-level trajectory is goal-conditioned (allowing for a simple reward specification) and of the same, limited length, it is very amenable ...

- **p. 2 / 1 Introduction - extractive body cue:** Second, our method does not require any explicit form of skill segmentation or subgoal definition, which otherwise would need to be learned or explicitly provided.
- **p. 3 / 3 Preliminaries - extractive body cue:** Our approach consists of two phases: relay imitation learning (RIL), followed by relay reinforcement fine-tuning (RRF) described in Sec.
- **p. 1 / Abstract - extractive body cue:** We present relay policy learning, a method for imitation and reinforcement learning that can solve multi-stage, long-horizon robotic tasks.
- **p. 1 / Abstract - extractive body cue:** We demonstrate the effectiveness of our method on a number of multi-stage, long-horizon manipulation tasks in a challenging kitchen simulation environment.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 13 | Figure 9: Visualization of successful learned behavior for moving kettle, turning top knob, sliding the slider and opening ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | While these trajectories did not necessarily reach the goals that were originally commanded, and therefore cannot be considered ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 13 | Figure 10: Visualization of failing learned behavior for moving kettle, turning the bottom knob, moving the slider and ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

il writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (3 Preliminaries), p. 3 (3 Preliminaries), p. 5 (3 Preliminaries), p. 5 (3 Preliminaries). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 Introduction), p. 5 (3 Preliminaries), p. 6 (3 Preliminaries), p. 6 (3 Preliminaries), p. 7 (3 Preliminaries), interface p. 4 (3 Preliminaries), p. 3 (3 Preliminaries), p. 5 (3 Preliminaries), p. 5 (3 Preliminaries), objective p. 4 (3 Preliminaries), p. 5 (3 Preliminaries), p. 3 (3 Preliminaries), p. 5 (3 Preliminaries), p. 6 (3 Preliminaries), p. 6 (3 Preliminaries).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, HRL methods have traditionally struggled due to various practical challenges such as exploration [5], skill segmentation [6] and reward definition [7]. (p. 1, 1 Introduction).
- **Formulation-changing contribution:** Second, our method does not require any explicit form of skill segmentation or subgoal definition, which otherwise would need to be learned or explicitly provided. (p. 2, 1 Introduction).
- **Assumption/failure evidence:** While these trajectories did not necessarily reach the goals that were originally commanded, and therefore cannot be considered optimal for those goals, they do end up reaching the actual states ... (p. 6, 3 Preliminaries).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
