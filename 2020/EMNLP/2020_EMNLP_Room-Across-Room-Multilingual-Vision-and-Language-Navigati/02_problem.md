# Problem - Room-Across-Room: Multilingual Vision-and-Language Navigation with Dense Spatiotemporal Grounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://aclanthology.org/2020.emnlp-main.356/; PDF retrieval source: https://aclanthology.org/2020.emnlp-main.356.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 3 (1 Introduction), p. 3 (1 Introduction), p. 5 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction)): High variance in path length, such that agents cannot simply exploit a strong length prior.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We introduce Room-Across-Room (RxR), a new Vision-and-Language Navigation (VLN) dataset.
- **p. 1 / Abstract - extractive body cue:** RxR is multilingual (English, Hindi, and Telugu) and larger (more paths and instructions) than other VLN datasets.
- **p. 1 / Abstract - extractive body cue:** It emphasizes the role of language in VLN by addressing known biases in paths and eliciting more references to visible entities.
- **p. 1 / Abstract - extractive body cue:** Furthermore, each word in an instruction is time-aligned to the virtual poses of instruction creators and validators.
- **p. 1 / Abstract - extractive body cue:** We establish baseline scores for monolingual and multilingual settings and multitask learning when including Room-to-Room annotations (Anderson et al., 2018b).
- **p. 3 / 1 Introduction - extractive body cue:** High variance in path length, such that agents cannot simply exploit a strong length prior.
- **p. 3 / 1 Introduction - extractive body cue:** Paths may approach their goal indirectly, so agents cannot simply go straight to the goal.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | High variance in path length, such that agents cannot simply exploit a strong length prior. | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | Guide and Follower pose traces provide dense spatiotemporal alignments between instructions, visual percepts and actions - and both perspectives are useful for ... | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF body |
| State / latent | Guide, Follower, pose, traces, provide, dense, spatiotemporal, alignments, between, instructions | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | Inputs, Guide, Tourist, have, observed, cannot, influence, utterances | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: Guide, Follower, pose, traces, provide, dense, spatiotemporal, alignments, between, instructions | p. 2 (1 Introduction), p. 5 (1 Introduction), p. 6 (29. US English instructions are the longest on av) |
| Decision / output variable | method trajectory/action; body terms: introduce, Room-across-Room, RxR, VLN, dataset, addresses, gaps, existing | p. 1 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: Datasets, have, been, collected, indoor, Anderson, Thomason, outdoor | p. 1 (1 Introduction), p. 5 (1 Introduction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Success / guarantee | comparable score and protocol validity | p. 6 (Figure/Table caption), p. 7 (5 Experiments), p. 7 (5 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 3 / 1 Introduction - extractive body cue:** Paths may approach their goal indirectly, so agents cannot simply go straight to the goal.
- **p. 5 / 1 Introduction - extractive body cue:** If the second Follower also fails, then the path is reenqueued to generate another Guide and Follower annotation.
- **p. 2 / 1 Introduction - extractive body cue:** The dominance of high resource languages is a pervasive problem as it is unclear that research findings generalize to other languages (Bender, 2009).
- **p. 1 / 1 Introduction - extractive body cue:** We introduce Room-across-Room (RxR), a VLN dataset that addresses gaps in existing ones by (1) ∗First two.

## What the Paper Changes

PDF body contribution framing (p. 1 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction)): We introduce Room-across-Room (RxR), a VLN dataset that addresses gaps in existing ones by (1) ∗First two.

- **p. 1 / Abstract - extractive body cue:** We introduce Room-Across-Room (RxR), a new Vision-and-Language Navigation (VLN) dataset.
- **p. 2 / 1 Introduction - extractive body cue:** In addition to verifying instruction quality, this allows us to collect a play-by-play account of how a human interpreted the instructions, represented as a pose ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Although RxR and R2R share the same underlying environments, we note that RxR →R2R cannot exploit R2R's | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | This is consistent with results in multilingual machine translation (MT) and automatic speech recognition (ASR) where adding more ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1 Introduction), p. 5 (1 Introduction), p. 6 (29. US English instructions are the longest on av), p. 5 (29. US English instructions are the longest on av). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 3 (1 Introduction), p. 3 (1 Introduction), p. 5 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), interface p. 2 (1 Introduction), p. 5 (1 Introduction), p. 6 (29. US English instructions are the longest on av), p. 5 (29. US English instructions are the longest on av), objective p. 1 (1 Introduction), p. 5 (1 Introduction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
