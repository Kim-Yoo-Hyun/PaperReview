# Problem - CodeDiffuser: Attention-Enhanced Diffusion Policy via VLM-Generated Code for Instruction Ambiguity

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p072.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p072.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 3 (A. Problem Statement), p. 3 (A. Problem Statement)): For instance, in the packing battery task illustrated in Figure 2, specifying the mug or branch instance, the probability of each battery-slot pair is 1/18, imposing an additional axis of ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Natural language instructions for robotic manipula tion tasks often exhibit ambiguity and vagueness.
- **p. 1 / Abstract - extractive body cue:** For instance, the instruction "Hang a mug on the mug tree" may Involve
- **p. 1 / Abstract - extractive body cue:** ‘and low-level action genera ptimal performance due 10
- **p. 1 / Abstract - extractive body cue:** To address these challenges, we introduce novel robotic manipulation framework that can accomplish tasks specified by potentially ambiguous natural language.
- **p. 1 / Abstract - extractive body cue:** This framework employs a Vision-Language Model (VIM) to interpret abstract concepts in natural language instructions and generates task-specific code - an interpretable and executable intermediate ...
- **p. 3 / A. Problem Statement - extractive body cue:** For instance, in the packing battery task illustrated in Figure 2, specifying the mug or branch instance, the probability of each battery-slot pair is 1/18, ...
- **p. 3 / A. Problem Statement - extractive body cue:** Notably, we show in Section IV-B that the current state-of the-art methods can fail to achieve a high success rate even with extensive training demonstrations

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | For instance, in the packing battery task illustrated in Figure 2, specifying the mug or branch instance, the probability of each battery-slot ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | [ plalz = =)p(= = z1lor,2), Where 2 is a task-relevant latent representation of the state such that p(ajo,l,2 = =) = ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | plalz, z1lor, Where, task-relevant, latent, representation, state, contains, enough, information | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | instance, packing, battery, task, illustrated, Figure, specifying, branch | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: plalz, z1lor, Where, task-relevant, latent, representation, state, contains, enough, information | p. 3 (A. Problem Statement), p. 4 (A. Problem Statement), p. 3 (A. Problem Statement) |
| Decision / output variable | action, pose, option or chunk a; body terms: contrast, framework, capable, understanding, potentially, ambiguous, natural, language | p. 3 (B. Foundational Vision Model for Roboties), p. 4 (A. Problem Statement), p. 7 (B. Analysis of Existing Imitation Learning Algorithm) |
| Objective / loss / cost | policy/action modeling objective; cue terms: While, performance, ACT, initially, improves, they, generally, diminishing | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 7 (B. Analysis of Existing Imitation Learning Algorithm) |
| Success / guarantee | instruction-conditioned task success | p. 7 (B. Analysis of Existing Imitation Learning Algorithm), p. 6 (IV. EXPERIMENTS), p. 7 (B. Analysis of Existing Imitation Learning Algorithm) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 3 / A. Problem Statement - extractive body cue:** Notably, we show in Section IV-B that the current state-of the-art methods can fail to achieve a high success rate even with extensive training demonstrations

## What the Paper Changes

PDF body contribution framing (p. 3 (B. Foundational Vision Model for Roboties), p. 4 (A. Problem Statement), p. 7 (B. Analysis of Existing Imitation Learning Algorithm), p. 7 (B. Analysis of Existing Imitation Learning Algorithm), p. 8 (B. Analysis of Existing Imitation Learning Algorithm)): In contrast, our framework is capable of understanding potentially ambiguous natural language instructions by using visual-semantic reasoning capabilities of VLM and generated code as an intermediate representation.

- **p. 4 / A. Problem Statement - extractive body cue:** CodeDitfuser consists of three primary components: code generation, 3D attention map computation, and low level policy.
- **p. 7 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** We frst evaluate our method by varying the number of demonstrations on the Pack Bat.tezy task in simulation, as shown in Figure 7 (a).
- **p. 7 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** Our method effectively, leverages the powerful visualsemantic understanding capabilities of VLMs and benefits from explicit spatial relation reasoning using 3D representations.
- **p. 8 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** For the simulation experiments, we compare our method against the following baselines:

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Similarly, as the number of placement options increases, most failures occur during the placement stage of the task. ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | In our experiments, we first identify the key limitations of existing imitation learning algorithms. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | (b) Failure Breakdown of Two Special Scenarios | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | We observe that failure primarily occurs at the task stage with the highest ambiguity, demonstrating a strong cconrelation ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (A. Problem Statement), p. 4 (A. Problem Statement), p. 3 (A. Problem Statement), p. 6 (B. Analysis of Existing Imitation Learning Algorithm). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 3 (A. Problem Statement), p. 3 (A. Problem Statement), interface p. 3 (A. Problem Statement), p. 4 (A. Problem Statement), p. 3 (A. Problem Statement), p. 6 (B. Analysis of Existing Imitation Learning Algorithm), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** For instance, in the packing battery task illustrated in Figure 2, specifying the mug or branch instance, the probability of each battery-slot pair is 1/18, imposing an additional axis of ... (p. 3, A. Problem Statement).
- **Formulation-changing contribution:** To address these challenges, we introduce novel robotic manipulation framework that can accomplish tasks specified by potentially ambiguous natural language. (p. 1, Abstract).
- **Assumption/failure evidence:** Similarly, as the number of placement options increases, most failures occur during the placement stage of the task. ‘The observed correlation between (i) increased task ambiguity and (ii) declining task ... (p. 7, B. Analysis of Existing Imitation Learning Algorithm).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
