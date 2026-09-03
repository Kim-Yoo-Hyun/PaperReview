# Problem - Bring My Cup! Personalizing Vision-Language-Action Models with Visual Attentive Prompting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (48 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=fm6Z3wfTae; PDF retrieval source: https://openreview.net/pdf/68e389cf48e82eb16b32f886139baddd9122f43d.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction), p. 4 (3.1. Problem Formulation), p. 1 (1. Introduction)): To bridge this semantic gap, we formulate the challenge of manipulating personal objects.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** While Vision-Language-Action (VLA) models generalize well to generic instructions, they struggle with personalized commands such as "bring my cup," where the robot must act on ...
- **p. 1 / Abstract - extractive body cue:** We study this setting of manipulating personal objects, in which a VLA must identify and control a user-specific object unseen during training using only a ...
- **p. 1 / Abstract - extractive body cue:** To address this challenge, we propose Visual Attentive Prompting (VAP), a simple-yet-effective training-free perceptual adapter that equips frozen VLAs with topdown selective attention.
- **p. 1 / Abstract - extractive body cue:** VAP treats the reference images as a non-parametric visual memory, grounds the personal object in the scene through open-vocabulary detection and embedding-based matching, and then ...
- **p. 1 / Abstract - extractive body cue:** We construct two simulation benchmarks, Personalized-SIMPLER and Personalized-VLABench, and a real-world tabletop benchmark to evaluate personalized manipu1GSAI, POSTECH 2IME, POSTECH.
- **p. 2 / 1. Introduction - extractive body cue:** To bridge this semantic gap, we formulate the challenge of manipulating personal objects.
- **p. 2 / 1. Introduction - extractive body cue:** In each benchmark, one object is replaced by a user-specific instance, same-category distractors are added, and the policy must ground the correct instance from a ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | To bridge this semantic gap, we formulate the challenge of manipulating personal objects. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | We consider a pre-trained VLA policy πVLA(a / x, ℓ) mapping observation x = (I, s) and instruction ℓto action a, where ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | consider, pre-trained, VLA, policy, mapping, observation, instruction, action, where, denotes | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | explicitly, overlaying, grounded, mask, canonical, visual, attributes, solid | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: consider, pre-trained, VLA, policy, mapping, observation, instruction, action, where, denotes | p. 4 (3.1. Problem Formulation), p. 3 (1. Introduction), p. 4 (3.1. Problem Formulation) |
| Decision / output variable | action, pose, option or chunk a; body terms: main, contributions, follows, Personal, Object, Manipulation, introduce, personalization | p. 3 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.1. Problem Formulation) |
| Objective / loss / cost | policy/action modeling objective; cue terms: While, exact, gradientbased, optimization, would, computationally, prohibitive, VAP | p. 4 (3.1. Problem Formulation), p. 4 (3.1. Problem Formulation) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3.1. Problem Formulation), p. 4 (3.1. Problem Formulation) |
| Success / guarantee | instruction-conditioned task success | p. 45 (Figure/Table caption), p. 7 (5.1. Experimental Setup), p. 7 (5.1. Experimental Setup) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** In each benchmark, one object is replaced by a user-specific instance, same-category distractors are added, and the policy must ground the correct instance from a ...
- **p. 3 / 1. Introduction - extractive body cue:** Ablations confirm that neither component alone reliably closes the gap between semantic commands and instance-level control.
- **p. 4 / 3.1. Problem Formulation - extractive body cue:** Reference images are the primary signal in this regime: detailed verbal descriptions cannot reliably distinguish two same-category instances, while a few photographs carry the discriminative ...
- **p. 1 / 1. Introduction - extractive body cue:** By training on large-scale robot datasets (Open XEmbodiment Collaboration et al., 2023), these models achieve strong generalization to generic instructions (e.g., "pick up the cup").

## What the Paper Changes

PDF body contribution framing (p. 3 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.1. Problem Formulation), p. 4 (3.1. Problem Formulation)): Our main contributions are as follows: • Personal Object Manipulation: We introduce a personalization task for VLAs where the policy must manipulate user-specific objects among visually similar distractors using only ...

- **p. 2 / 1. Introduction - extractive body cue:** We propose Visual Attentive Prompting (VAP), a training-free framework that injects instance-awareness into frozen VLAs by intervening only on their inputs.
- **p. 4 / 3.1. Problem Formulation - extractive body cue:** While exact gradientbased optimization would be computationally prohibitive, we propose VAP as a zero-shot approximation.
- **p. 4 / 3.1. Problem Formulation - extractive body cue:** The category is known, but the specific instance is novel and unseen during training, and at test time the robot encounters o amidst visually similar ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 42 | Figure 23. Case 3 (correct prompt): correct instance highlighted but manipulation fails. The mask prompt consistently highlights the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 25 | Figure 9. Soft Prompt: relatively consistent localization yet failed execution. Across the rollout, the token-patch similarity heatmaps remain ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 1 | Figure 1. Manipulating personal objects with VLA. Existing vision-language-action (VLA) models cannot handle per- sonal objects such as ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | First, the sequential factorization of grounding and manipulation does not itself bound performance: reliable spatio-temporal tracking maintains target ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (3.1. Problem Formulation), p. 3 (1. Introduction), p. 4 (3.1. Problem Formulation), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction), p. 4 (3.1. Problem Formulation), p. 1 (1. Introduction), interface p. 4 (3.1. Problem Formulation), p. 3 (1. Introduction), p. 4 (3.1. Problem Formulation), p. 2 (1. Introduction), objective p. 4 (3.1. Problem Formulation), p. 4 (3.1. Problem Formulation).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
