# Problem - FACTR: Force-Attending Curriculum Training for Contact-Rich Policy Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p079.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p079.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 5 (A. Problem Statement and Base Model)): 4: FACTR allows our policy to beter integrate force information without overfittng to visual information, resulting in better generalization

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Many contact-rich tasks humans perform, such as, box pickup or rolling dough, rely on force feedback for reliable execution.
- **p. 1 / Abstract - extractive body cue:** However, this force information, which is readily avail able in most robot arms, is not commonly used in teleoperation and policy learning.
- **p. 1 / Abstract - extractive body cue:** Consequently, robot behavior is often limited to quasi-static kinematic tasks that do not require intr
- **p. 1 / Abstract - extractive body cue:** In this paper, we first present a low-cost, intuitive, bilateral teleoperation setup that relays external forces of the follower arm back to the teacher arm, ...
- **p. 1 / Abstract - extractive body cue:** We then introduce FACTR, a policy learning method that employs a curriculum which corrupts the visual input with decreasing intensity throughout training. ‘The curriculum prevents ...
- **p. 5 / A. Problem Statement and Base Model - extractive body cue:** 4: FACTR allows our policy to beter integrate force information without overfittng to visual information, resulting in better generalization
- **p. 5 / A. Problem Statement and Base Model - extractive body cue:** For the decoder, we introduce & action tokens, A ¢ R**¢.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | 4: FACTR allows our policy to beter integrate force information without overfittng to visual information, resulting in better generalization | contact-rich manipulation scene | body wording is the source claim |
| Observation / input | We consider a policy o(- / -) that produces a chunk of future actions of length k d..++1 (joint positions) given visual ... | tactile image/force, vision과 proprioceptive history | exact sensor/frame/preprocessing from PDF body |
| State / latent | consider, policy, produces, chunk, future, actions, length, joint, positions, given | contact geometry, force state 또는 latent dynamics | notation and tensor shape require body check |
| Output / action | Visual, observations, force, readings, converted, tokens, encoder, then | grasp/contact action, force command 또는 object motion | exact unit/frame/decoder require body check |
| Target outcome | slip/contact success and safe interaction | slip/contact success, force/pose error와 robustness | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | visual/tactile/proprioceptive contact history; body terms: consider, policy, produces, chunk, future, actions, length, joint, positions, given | p. 4 (A. Problem Statement and Base Model), p. 5 (A. Problem Statement and Base Model), p. 5 (A. Problem Statement and Base Model) |
| Decision / output variable | contact-aware action/force; body terms: decoder, introduce, action, tokens, FACTR, allows, policy, beter | p. 5 (A. Problem Statement and Base Model), p. 5 (A. Problem Statement and Base Model) |
| Objective / loss / cost | contact prediction/control error; cue terms: not stated or recoverable in the selected PDF body | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | 본문 anchor 없음 |
| Success / guarantee | slip/contact success and safe interaction | p. 7 (C. Policy Evaluation), p. 8 (C. Policy Evaluation), p. 8 (C. Policy Evaluation) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 5 / A. Problem Statement and Base Model - extractive body cue:** 4: FACTR allows our policy to beter integrate force information without overfittng to visual information, resulting in better generalization

## What the Paper Changes

PDF body contribution framing (p. 5 (A. Problem Statement and Base Model), p. 5 (A. Problem Statement and Base Model)): For the decoder, we introduce & action tokens, A ¢ R**¢.

- **p. 5 / A. Problem Statement and Base Model - extractive body cue:** 4: FACTR allows our policy to beter integrate force information without overfittng to visual information, resulting in better generalization

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | Developing. adaptive or self-tuning curriculum strategies could help mitigate this issue by dynamically adjusting hyperparameters based on task-specific ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | While without the curriculum, the policy does not pay enough attention 10 force, and either fails to lift ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | This limitation can particularly affect tasks that involve subtle force adjustments during finegrained manipulation since the torque readings ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | 6, All the policies perform similarly on the train objects for most tasks, except for the rolling dough ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

tactile writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (A. Problem Statement and Base Model), p. 5 (A. Problem Statement and Base Model), p. 5 (A. Problem Statement and Base Model), p. 4 (A. Problem Statement and Base Model). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 5 (A. Problem Statement and Base Model), interface p. 4 (A. Problem Statement and Base Model), p. 5 (A. Problem Statement and Base Model), p. 5 (A. Problem Statement and Base Model), p. 4 (A. Problem Statement and Base Model), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** 4: FACTR allows our policy to beter integrate force information without overfittng to visual information, resulting in better generalization (p. 5, A. Problem Statement and Base Model).
- **Formulation-changing contribution:** For the decoder, we introduce & action tokens, A ¢ R**¢. (p. 5, A. Problem Statement and Base Model).
- **Assumption/failure evidence:** While without the curriculum, the policy does not pay enough attention 10 force, and either fails to lift or balance the novel boxes. (p. 8, C. Policy Evaluation).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
