# Problem - VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2307.05973; PDF retrieval source: https://arxiv.org/pdf/2307.05973. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction)): However, to enable physical interactions with the environment, existing approaches typically rely on a repertoire of pre-defined motion primitives (i.e., skills) that may be invoked by an LLM or a ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Large language models (LLMs) are shown to possess a wealth of actionable knowledge that can be extracted for robot manipulation in the form of reasoning ...
- **p. 1 / Abstract - extractive body cue:** Despite the progress, most still rely on pre-defined motion primitives to carry out the physical interactions with the environment, which remains a major bottleneck.
- **p. 1 / Abstract - extractive body cue:** In this work, we aim to synthesize robot trajectories, i.e., a dense sequence of 6-DoF end-effector waypoints, for a large variety of manipulation tasks given ...
- **p. 1 / Abstract - extractive body cue:** We achieve this by first observing that LLMs excel at inferring affordances and constraints given a free-form language instruction.
- **p. 1 / Abstract - extractive body cue:** More importantly, by leveraging their code-writing capabilities, they can interact with a vision-language model (VLM) to compose 3D value maps to ground the knowledge into ...
- **p. 2 / 1 Introduction - extractive body cue:** However, to enable physical interactions with the environment, existing approaches typically rely on a repertoire of pre-defined motion primitives (i.e., skills) that may be invoked ...
- **p. 2 / 1 Introduction - extractive body cue:** In addressing this challenge, we first note that it is impractical for LLMs to directly output control actions in text, which are typically driven by ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, to enable physical interactions with the environment, existing approaches typically rely on a repertoire of pre-defined motion primitives (i.e., skills) that ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | On top of value map LMPs, we define two high-level LMPs to orchestrate their behaviors: planner takes user instruction L as input ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | value, LMPs, define, high-level, orchestrate, behaviors, planner, takes, user, instruction | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | type, uses, different, LMP, takes, instruction, outputs, voxel | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: value, LMPs, define, high-level, orchestrate, behaviors, planner, takes, user, instruction | p. 6 (3 Method), p. 4 (3 Method), p. 6 (3 Method) |
| Decision / output variable | action, pose, option or chunk a; body terms: represent, sequence, dense, end-effector, waypoints, executed, Operational, Space | p. 4 (3 Method), p. 2 (1 Introduction), p. 3 (3 Method) |
| Objective / loss / cost | policy/action modeling objective; cue terms: Note, while, additional, trajectory, parametrizations, mapped, real-valued, cost | p. 4 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 7 (3 Method), p. 7 (3 Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 7 (3 Method), p. 4 (3 Method), p. 7 (3 Method) |
| Success / guarantee | instruction-conditioned task success | p. 22 (A.5.2 Full Results on Simulated Environments), p. 7 (3 Method), p. 7 (3 Method) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive body cue:** In addressing this challenge, we first note that it is impractical for LLMs to directly output control actions in text, which are typically driven by ...
- **p. 3 / 1 Introduction - extractive body cue:** In this work, we leverage LLMs for zero-shot in-the-wild cost specification with superior generalization.
- **p. 3 / 1 Introduction - extractive body cue:** For robotic applications, concurrent works explored LLM-based reward generation [82-88], among which Yu et al.

## What the Paper Changes

PDF body contribution framing (p. 4 (3 Method), p. 2 (1 Introduction), p. 3 (3 Method), p. 6 (3 Method), p. 3 (1 Introduction)): We represent τ r i as a sequence of dense end-effector waypoints to be executed by an Operational Space Controller [117], where each waypoint consists of a desired 6-DoF end-effector ...

- **p. 2 / 1 Introduction - extractive body cue:** Rather than relying on robotic data that are often of limited amount or variability, the method leverages LLMs for open-world reasoning and VLMs for generalizable ...
- **p. 3 / 3 Method - extractive body cue:** The central problem 2Note that the decomposition and sequencing of these sub-tasks are also done by LLMs in this work, though we do not investigate ...
- **p. 6 / 3 Method - extractive body cue:** We further demonstrate how VoxPoser enables efficient learning of more challenging tasks (Sec.
- **p. 3 / 1 Introduction - extractive body cue:** Despite the promising signs, hand-designed motion primitives are still required, and while LLMs are shown to be capable of composing sequential policy logic, it remains ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | 5 Conclusion, Limitations, & Future Works In this work, we present VOXPOSER, a general framework for extracting affordances ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Despite compelling results, VoxPoser has several limitations. | reported limitation/failure wording; scope must be verified |
| body cue at p. 18 | This serves as a lighthearted example that language models can exhibit limitations similar to human reasoning. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | VoxPoser performs everyday manipulation tasks with high success and is more robust to disturbances than the baseline using ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 6 (3 Method), p. 4 (3 Method), p. 6 (3 Method), p. 3 (3 Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), interface p. 6 (3 Method), p. 4 (3 Method), p. 6 (3 Method), p. 3 (3 Method), objective p. 4 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 7 (3 Method), p. 7 (3 Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (23 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, to enable physical interactions with the environment, existing approaches typically rely on a repertoire of pre-defined motion primitives (i.e., skills) that may be invoked by an LLM or a ... (p. 2, 1 Introduction).
- **Formulation-changing contribution:** Rather than relying on robotic data that are often of limited amount or variability, the method leverages LLMs for open-world reasoning and VLMs for generalizable visual grounding in a model-based ... (p. 2, 1 Introduction).
- **Assumption/failure evidence:** 5 Conclusion, Limitations, & Future Works In this work, we present VOXPOSER, a general framework for extracting affordances and constraints, grounded in 3D perceptual space, from LLMs and VLMs for ... (p. 8, 3 Method).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
