# Problem - Diffusion Meets DAgger: Supercharging Eye-in-hand Imitation Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p048.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p048.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): 1: Eye-in-hand Imitation learning with DMD: A common failure mode in an imitation learning setting is the problem of poor generalization due to compounding execution errors at test time as ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** A common failure mode for policies trained with imitation is compounding execution errors at test time.
- **p. 1 / Abstract - extractive body cue:** When the learned policy encounters states that are not present in the expert demonstrations, the policy fails, leading to degenerate behavior.
- **p. 1 / Abstract - extractive body cue:** The Dataset Aggregation, or DAgger approach to this problem simply collects more data to cover these failure states.
- **p. 1 / Abstract - extractive body cue:** However, in practice, this is often prohibitively expensive.
- **p. 1 / Abstract - extractive body cue:** In this work, we propose Diffusion Meets DAgger (DMD), a method that reaps the benefits of DAgger but without the cost, for eye-in-hand imitation learning ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, DAgger [56] is challenging to put into practice: it requires an expert operator to supervise the robot during execution and guide it to recover ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Computing action labels for these samples present yet another challenge (Figure 5).

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | 1: Eye-in-hand Imitation learning with DMD: A common failure mode in an imitation learning setting is the problem of poor generalization due ... | demonstration으로 정의된 robot task distribution | body wording is the source claim |
| Observation / input | Purple-outlined images are diffusion-generated augmenting samples. c) The original task data and augmenting dataset are combined for policy learning. views from a ... | observation history와 expert trajectory/action | exact sensor/frame/preprocessing from PDF body |
| State / latent | Purple-outlined, images, diffusion-generated, augmenting, samples, original, task, data, dataset, combined | behavior policy와 temporal action context | notation and tensor shape require body check |
| Output / action | Policy, trained, supervised, learning, regress, action, images, target | predicted action 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | closed-loop task success and robustness | imitation error, task success, robustness와 compounding error | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | observation history o_{t−H:t}; body terms: Purple-outlined, images, diffusion-generated, augmenting, samples, original, task, data, dataset, combined | p. 3 (III. APPROACH), p. 1 (I. INTRODUCTION), p. 2 (III. APPROACH) |
| Decision / output variable | expert-like action/chunk a_{t:t+H}; body terms: present, experiments, evaluate, aforementioned, design, choices, developing, data | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. APPROACH) |
| Objective / loss / cost | imitation or action-distribution loss; cue terms: gives, final, training, objective, aTb, where, causes, conflicting | p. 3 (III. APPROACH) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (III. APPROACH), p. 4 (III. APPROACH) |
| Success / guarantee | closed-loop task success and robustness | p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 8 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** However, DAgger [56] is challenging to put into practice: it requires an expert operator to supervise the robot during execution and guide it to recover ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Computing action labels for these samples present yet another challenge (Figure 5).

## What the Paper Changes

PDF body contribution framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. APPROACH), p. 3 (III. APPROACH), p. 4 (III. APPROACH)): We present experiments that evaluate the aforementioned design choices in developing a data creation framework to supercharge eye-in-hand imitation learning.

- **p. 2 / I. INTRODUCTION - extractive body cue:** Across all tasks, we see a sizeable improvement over vanilla behavior cloning, demonstrating the effectiveness of our framework Diffusion Meets DAgger (DMD).
- **p. 3 / III. APPROACH - extractive body cue:** To address this issue, as shown in Figure 2, our approach generates an augmented dataset ˜D and trains the policy jointly on ˜D ∪D.
- **p. 3 / III. APPROACH - extractive body cue:** 2: DMD System Overview: Our system operates in three stages. a) A diffusion model is trained, using task and play data, to synthesize novel views ...
- **p. 4 / III. APPROACH - extractive body cue:** Finetuning with around 50 trajectories leads to realistic novel view synthesis for our tasks as shown in Figure 7.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | A common failure case for BC is that as the robot rotates the cup with coffee beans, it ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 1 | Fig. 1: Eye-in-hand Imitation learning with DMD: A common failure mode in an imitation learning setting is the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | See videos on project website for failure modes. | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | [86] seek to imitate, it fails when the gripper manipulates the scene, as in our tasks. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

il writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (III. APPROACH), p. 1 (I. INTRODUCTION), p. 2 (III. APPROACH), p. 1 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 3 (III. APPROACH), p. 1 (I. INTRODUCTION), p. 2 (III. APPROACH), p. 1 (I. INTRODUCTION), objective p. 3 (III. APPROACH).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, DAgger [56] is challenging to put into practice: it requires an expert operator to supervise the robot during execution and guide it to recover from failures. (p. 1, I. INTRODUCTION).
- **Formulation-changing contribution:** We present experiments that evaluate the aforementioned design choices in developing a data creation framework to supercharge eye-in-hand imitation learning. (p. 2, I. INTRODUCTION).
- **Assumption/failure evidence:** A common failure case for BC is that as the robot rotates the cup with coffee beans, it does not move the cup closer to the receiving cup; the blue ... (p. 9, 24 Demo).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
