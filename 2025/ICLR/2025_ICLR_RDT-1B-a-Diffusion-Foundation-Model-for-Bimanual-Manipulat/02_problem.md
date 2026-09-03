# Problem - RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=yAzN4tz7oI; PDF retrieval source: https://openreview.net/pdf/29d56379d000b8c0e05906c5958e67e2e870ab0c.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): Developing bimanual manipulation foundation models confronts the dual challenges of data scarcity and architectural limitations.

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** Bimanual manipulation is essential in robotics, yet developing foundation models is extremely challenging due to the inherent complexity of coordinating two robot arms (leading to ...
- **p. 1 / ABSTRACT - extractive body cue:** In this paper, we present the Robotics Diffusion Transformer (RDT), a pioneering diffusion foundation model for bimanual manipulation.
- **p. 1 / ABSTRACT - extractive body cue:** RDT builds on diffusion models to effectively represent multi-modality, with innovative designs of a scalable Transformer to deal with the heterogeneity of multi-modal inputs and ...
- **p. 1 / ABSTRACT - extractive body cue:** To address data scarcity, we further introduce a Physically Interpretable Unified Action Space, which can unify the action representations of various robots while preserving the ...
- **p. 1 / ABSTRACT - extractive body cue:** With these designs, we managed to pre-train RDT on the largest collection of multi-robot datasets to date and scaled it up to 1.2B parameters, which ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Developing bimanual manipulation foundation models confronts the dual challenges of data scarcity and architectural limitations.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, current approaches either depend on task-specific primitives (Mirrazavi Salehian et al., 2017; Rakita et al., 2019; Grannen et al., 2023a) or are limited to ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Developing bimanual manipulation foundation models confronts the dual challenges of data scarcity and architectural limitations. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | It exhibits zeroshot generalization to unseen objects and scenes, understands and follows language instructions, learns new skills with just 1∼5 demonstrations, and ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | exhibits, zeroshot, generalization, unseen, objects, scenes, understands, follows, language, instructions | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | First, doubled, action, space, induces, multi-modal, distributions, Jia | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: exhibits, zeroshot, generalization, unseen, objects, scenes, understands, follows, language, instructions | p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Decision / output variable | action, pose, option or chunk a; body terms: introduce, Robotics, Diffusion, Transformer, RDT, largest, bimanual, manipulation | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Objective / loss / cost | policy/action modeling objective; cue terms: prohibitive, costs, dual-arm, systems, create, severe, data, scarcity | p. 2 (1 INTRODUCTION) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Success / guarantee | instruction-conditioned task success | p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, current approaches either depend on task-specific primitives (Mirrazavi Salehian et al., 2017; Rakita et al., 2019; Grannen et al., 2023a) or are limited to ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Existing solutions either discard robots with structural inconsistencies or retain only cross-robot invariant features (Brohan et al., 2023; Ghosh et al., 2023; Shah et al., ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** For scalability, we harness the Transformer backbone and carefully design the multi-modal encoding to eliminate the heterogeneity of various modalities.

## What the Paper Changes

PDF body contribution framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION)): In this paper, we introduce the Robotics Diffusion Transformer (RDT), the largest bimanual manipulation foundation model with strong generalizability.

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To further enable training RDT on heterogeneous data, we propose the Physically Interpretable Unified Action Space, a unified action format for various robots with gripper ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Developing bimanual manipulation foundation models confronts the dual challenges of data scarcity and architectural limitations.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Following the success in natural language processing (Achiam et al., 2023; Touvron et al., 2023) and computer vision (Radford et al., 2021; Kirillov et al., ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | It probably makes ACT prone to failure. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Figure 4: (a) Unstable loss curve during training without QKNorm & RMSNorm. (b) Success rates of RDT (w/o ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | The robot needs to Pick Up Pen (#1), Switch Hand (#2), Drop Pen (#3), and ensure it can ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | The robot needs to Pick Up Cup (#1), Turn On Faucet (#2), Get Water (#3, to ensure that ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), interface p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), objective p. 2 (1 INTRODUCTION).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (28 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** Developing bimanual manipulation foundation models confronts the dual challenges of data scarcity and architectural limitations. (p. 1, 1 INTRODUCTION).
- **Formulation-changing contribution:** In this paper, we introduce the Robotics Diffusion Transformer (RDT), the largest bimanual manipulation foundation model with strong generalizability. (p. 2, 1 INTRODUCTION).
- **Assumption/failure evidence:** It probably makes ACT prone to failure. (p. 10, 5 EXPERIMENTS).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
