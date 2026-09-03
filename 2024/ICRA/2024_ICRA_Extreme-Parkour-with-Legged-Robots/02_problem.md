# Problem - Extreme Parkour with Legged Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2309.14341; PDF retrieval source: https://arxiv.org/pdf/2309.14341. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 3 (1 Introduction), p. 3 (1 Introduction)): However, low cost poses a new challenge for parkour which is not as prominent in prior walking works.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Humans can perform parkour by traversing obstacles in a highly dynamic fashion requiring precise eye-muscle coordination and movement.
- **p. 1 / Abstract - extractive body cue:** Getting robots to do the same task requires overcoming similar challenges.
- **p. 1 / Abstract - extractive body cue:** Classically, this is done by independently engineering perception, actuation, and control systems to very low tolerances.
- **p. 1 / Abstract - extractive body cue:** This restricts them to tightly controlled settings such as a predetermined obstacle course in labs.
- **p. 1 / Abstract - extractive body cue:** In contrast, humans are able to learn parkour through practice without significantly changing their underlying biology.
- **p. 3 / 1 Introduction - extractive body cue:** However, low cost poses a new challenge for parkour which is not as prominent in prior walking works.
- **p. 3 / 1 Introduction - extractive body cue:** All these challenges are not feasible with such an approach.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, low cost poses a new challenge for parkour which is not as prominent in prior walking works. | legged robot, terrain과 contact dynamics | body wording is the source claim |
| Observation / input | As a result at deployment, the policy not only outputs agile motor commands but also rapidly adjusts heading directions all from input ... | proprioception, terrain/perception observation과 velocity command | exact sensor/frame/preprocessing from PDF body |
| State / latent | result, deployment, policy, only, outputs, agile, motor, commands, rapidly, adjusts | body/contact state, foothold 또는 behavior mode | notation and tensor shape require body check |
| Output / action | exteroception, similar, RMA, architecture, replace, scandots, input, base | joint target, torque, footstep 또는 locomotion action | exact unit/frame/decoder require body check |
| Target outcome | progress, balance and terrain robustness | velocity/progress, stability, energy와 terrain generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | body/proprioceptive/terrain state; body terms: result, deployment, policy, only, outputs, agile, motor, commands, rapidly, adjusts | p. 3 (1 Introduction), p. 6 (3 Method), p. 6 (3 Method) |
| Decision / output variable | joint action/torque/footstep; body terms: allow, robot, adjust, itself, obstacle, type, deployment, novel | p. 3 (1 Introduction), p. 3 (1 Introduction), p. 5 (3 Method) |
| Objective / loss / cost | return, tracking or stability objective; cue terms: While, above, reward, sufficient, diverse, parkour, behavior, challenging | p. 5 (3 Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (3 Method), p. 6 (3 Method), p. 4 (3 Method) |
| Success / guarantee | progress, balance and terrain robustness | p. 9 (4 Results), p. 9 (4 Results), p. 8 (4 Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 3 / 1 Introduction - extractive body cue:** All these challenges are not feasible with such an approach.

## What the Paper Changes

PDF body contribution framing (p. 3 (1 Introduction), p. 3 (1 Introduction), p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method)): To allow the robot to adjust itself as per the obstacle type at deployment, we propose a novel dual distillation method.

- **p. 3 / 1 Introduction - extractive body cue:** Below, we summarize the main contributions: • A novel dual distillation method for distilling both agile motor commands and rapidly fluctuating heading directions from depth ...
- **p. 5 / 3 Method - extractive body cue:** We present a simple, unified reward formulation from which diverse behaviors emerge automatically and are perfectly adapted to the terrain geometry.
- **p. 6 / 3 Method - extractive body cue:** To overcome this issue, we propose to use a mixture of teacher and student (MTS).
- **p. 6 / 3 Method - extractive body cue:** To explore this diversity, we introduce a term to track a desired forward vector using the same inner product design principle, which can be controlled ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | Figure 7: For each terrain, we run 5 trials and record the number of successes. We find that ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Noisy is able to get some performance but has very large variance since it can rely on collisions ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | These sudden adjustments are out-ofdistribution for the policy and it cannot adapt fast enough, causing it to fail. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | NoClear achieves slightly higher performance but it places feet close to the obstacle edges which is unstable in ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

locomotion writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (1 Introduction), p. 6 (3 Method), p. 6 (3 Method), p. 5 (3 Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 3 (1 Introduction), p. 3 (1 Introduction), interface p. 3 (1 Introduction), p. 6 (3 Method), p. 6 (3 Method), p. 5 (3 Method), objective p. 5 (3 Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, low cost poses a new challenge for parkour which is not as prominent in prior walking works. (p. 3, 1 Introduction).
- **Formulation-changing contribution:** Below, we summarize the main contributions: • A novel dual distillation method for distilling both agile motor commands and rapidly fluctuating heading directions from depth images. • A simple yet ... (p. 3, 1 Introduction).
- **Assumption/failure evidence:** It sometimes succeeds on hurdles and gaps but fails when the human has to provide sudden direction changes which are out-of-distribution. (p. 9, 4 Results).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
