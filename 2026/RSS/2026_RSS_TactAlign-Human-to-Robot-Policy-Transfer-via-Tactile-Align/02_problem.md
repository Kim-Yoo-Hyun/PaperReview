# Problem - TactAlign: Human-to-Robot Policy Transfer via Tactile Alignment

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://roboticsconference.org/program/papers/6/; PDF retrieval source: https://roboticsconference.org/program/papers/6/. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): This strict pairing can be prohibitively difficult to maintain during contact-rich interactions involving sliding contact or dynamic object motion necessary for general manipulation.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Human demonstrations collected by wearable devices (e.g., tactile gloves) provide fast and dexterous supervision for policy learning, and are guided by rich, natural tactile feedback.
- **p. 1 / Abstract - extractive body cue:** However, a key challenge is how to transfer humancollected tactile signals to robots despite the differences in sensing modalities and embodiment.
- **p. 1 / Abstract - extractive body cue:** Existing human-to-robot (H2R) approaches that incorporate touch often assume identical tactile sensors, require paired data, and involve little to no embodiment gap between human demonstrator ...
- **p. 1 / Abstract - extractive body cue:** We propose TactAlign, a crossembodiment tactile alignment method that transfers humancollected tactile signals to a robot with different embodiment.
- **p. 1 / Abstract - extractive body cue:** TactAlign transforms human and robot tactile observations into a shared latent representation using a rectified flow, without paired datasets, manual labels, or privileged information.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This strict pairing can be prohibitively difficult to maintain during contact-rich interactions involving sliding contact or dynamic object motion necessary for general manipulation.
- **p. 1 / I. INTRODUCTION - extractive body cue:** While effective, many of these approaches assume identical tactile sensors or little to no embodiment gap, which simplifies transfer but limits applicability across diverse robot ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This strict pairing can be prohibitively difficult to maintain during contact-rich interactions involving sliding contact or dynamic object motion necessary for general ... | contact-rich manipulation scene | body wording is the source claim |
| Observation / input | However, most existing human-to-robot (H2R) approaches omit tactile feedback entirely and instead focus on transferring more readily available observations such as egocentric ... | tactile image/force, vision과 proprioceptive history | exact sensor/frame/preprocessing from PDF body |
| State / latent | However, most, existing, human-to-robot, H2R, approaches, omit, tactile, feedback, entirely | contact geometry, force state 또는 latent dynamics | notation and tensor shape require body check |
| Output / action | TactAlign, leverages, rectified, flow, noisy, pseudo-pairs, learn, latent | grasp/contact action, force command 또는 object motion | exact unit/frame/decoder require body check |
| Target outcome | slip/contact success and safe interaction | slip/contact success, force/pose error와 robustness | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | visual/tactile/proprioceptive contact history; body terms: However, most, existing, human-to-robot, H2R, approaches, omit, tactile, feedback, entirely | p. 1 (I. INTRODUCTION), p. 2 (III. METHODOLOGY), p. 2 (I. INTRODUCTION) |
| Decision / output variable | contact-aware action/force; body terms: consists, stages, self-supervised, representation, learning, cross-embodiment, alignment, pseudo-pairs | p. 3 (III. METHODOLOGY), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective / loss / cost | contact prediction/control error; cue terms: step2, aggregate, learned, latents, domains, construct, pseudo-pairs, learn | p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |
| Success / guarantee | slip/contact success and safe interaction | p. 8 (Figure/Table caption), p. 1 (Figure/Table caption), p. 5 (IV. EXPERIMENTS AND RESULTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** While effective, many of these approaches assume identical tactile sensors or little to no embodiment gap, which simplifies transfer but limits applicability across diverse robot ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, existing methods primarily focus on static contact scenarios [30, 29, 11, 10] and coarse semanticlevel alignment objectives [10, 51], leaving their effectiveness for continuous ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Moreover, these approaches often rely on paired supervision or labels, limiting scalability across heterogeneous sensors and robots.

## What the Paper Changes

PDF body contribution framing (p. 3 (III. METHODOLOGY), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (III. METHODOLOGY), p. 1 (I. INTRODUCTION)): Our method consists of two stages: self-supervised representation learning and cross-embodiment alignment via pseudo-pairs.

- **p. 2 / I. INTRODUCTION - extractive body cue:** The core contributions of our work are: • We propose TactAlign, a method for aligning crosssensor tactile data from unpaired demonstrations of the same task.
- **p. 2 / I. INTRODUCTION - extractive body cue:** TactAlign leverages rectified flow with noisy pseudo-pairs to learn a latent mapping that enables H2R policy transfer between humans and robots equipped with heterogeneous tactile ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** Second: We propose incorporating pseudo-pairs into rectified flow to guide the velocity field toward desired correspondences between the source and target distributions.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In contrast, our proposed method enables tactile transfer from unpaired datasets of the same task without requiring such pairing assumptions.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Moreover, tactile alignment alone does not address visual discrepancies between human and robot embodiments. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Incorporating vision and other modalities into a unified multi-modal policy is also an important direction for future work. | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Fig. 3: Red and blue indicate two subsets of the source distribution. The left side of each of ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | We use Manus glove [25] with OSMO tactile sensors [45] for robust hand pose estimation under visual occlusions ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

tactile writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (I. INTRODUCTION), p. 2 (III. METHODOLOGY), p. 2 (I. INTRODUCTION), p. 4 (III. METHODOLOGY). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 1 (I. INTRODUCTION), p. 2 (III. METHODOLOGY), p. 2 (I. INTRODUCTION), p. 4 (III. METHODOLOGY), objective p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** This strict pairing can be prohibitively difficult to maintain during contact-rich interactions involving sliding contact or dynamic object motion necessary for general manipulation. (p. 1, I. INTRODUCTION).
- **Formulation-changing contribution:** The core contributions of our work are: • We propose TactAlign, a method for aligning crosssensor tactile data from unpaired demonstrations of the same task. (p. 2, I. INTRODUCTION).
- **Assumption/failure evidence:** Without alignment, the success rate is also 0%, with failures primarily arising from jamming, from which the policy cannot recover, often leading to complete unscrewing of the light bulb. (p. 7, 8. The pivoting and insertion).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
