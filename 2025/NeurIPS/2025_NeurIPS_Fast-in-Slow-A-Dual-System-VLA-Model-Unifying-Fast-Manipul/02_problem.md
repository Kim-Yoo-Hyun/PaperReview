# Problem - Fast-in-Slow: A Dual-System VLA Model Unifying Fast Manipulation within Slow Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (35 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=4asFznbzJg; PDF retrieval source: https://papers.nips.cc/paper_files/paper/2025/file/8cf3760422b9d4505589a97c8f9569e7-Paper-Conference.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction)): Simultaneously, enabling robots to execute a broad spectrum of tasks while adapting to variations in objects and environments remains the core challenge.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Generalized policy and execution efficiency constitute the two critical challenges in robotic manipulation.
- **p. 1 / Abstract - extractive body cue:** While recent foundation policies benefit from the commonsense reasoning capabilities of internet-scale pretrained vision-language models (VLMs), they often suffer from low execution frequency.
- **p. 1 / Abstract - extractive body cue:** To mitigate this dilemma, dual-system approaches have been proposed to leverage a VLM-based System 2 module for handling high-level decision-making, and a separate System 1 ...
- **p. 1 / Abstract - extractive body cue:** However, existing designs maintain both systems as separate models, limiting System 1 from fully leveraging the rich pretrained knowledge from the VLM-based System 2.
- **p. 1 / Abstract - extractive body cue:** In this work, we propose Fast-in-Slow (FiS), a unified dual-system vision-language-action (VLA) model that embeds the System 1 execution module within the VLM-based System 2 ...
- **p. 1 / 1 Introduction - extractive body cue:** Simultaneously, enabling robots to execute a broad spectrum of tasks while adapting to variations in objects and environments remains the core challenge.
- **p. 2 / 1 Introduction - extractive body cue:** While these methods improve execution efficiency, their System 1, as a lightweight separate model, lacks internetscale pretrained knowledge and depends solely on feature representations extracted ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Simultaneously, enabling robots to execute a broad spectrum of tasks while adapting to variations in objects and environments remains the core challenge. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | Block 1 Block 2 Block 3 LLM Lowfrequency Highfrequency Block n-1 Block 1 Block 2 LLM Block n Lowfrequency Highfrequency Separate Policy ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | Block, LLM, Lowfrequency, Highfrequency, Separate, Policy, Model, Feature, Action, Previous | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | evaluation, FiS-VLA, outperforms, previous, state-of-the-art, methods, simulation, realworld | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: Block, LLM, Lowfrequency, Highfrequency, Separate, Policy, Model, Feature, Action, Previous | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract) |
| Decision / output variable | action, pose, option or chunk a; body terms: summary, contributions, follows, Fast-in-Slow, FiS, unified, dual-system, VLA | p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Objective / loss / cost | policy/action modeling objective; cue terms: multimodal, comprehension, component, System, exploit, autoregressive, next-token, prediction | p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Success / guarantee | instruction-conditioned task success | p. 7 (4 Experiments), p. 29 (Figure/Table caption), p. 7 (4 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive body cue:** While these methods improve execution efficiency, their System 1, as a lightweight separate model, lacks internetscale pretrained knowledge and depends solely on feature representations extracted ...
- **p. 2 / 1 Introduction - extractive body cue:** Considering these limitations, and motivated by the functional abstraction of Kahneman's dual-system theory, we raise a question: "If a VLM model serves as the central ...
- **p. 1 / 1 Introduction - extractive body cue:** Recently, some works [7, 8, 9, 10, 11, 12] have sought to leverage the pretrained knowledge of foundational vision-language-models (VLMs) [13, 14, 15, 16, 17, ...

## What the Paper Changes

PDF body contribution framing (p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract)): In summary, our contributions are as follows: • We propose Fast-in-Slow (FiS), a unified dual-system VLA model that embeds System 1 execution within a pretrained VLM while preserving its inherent ...

- **p. 2 / 1 Introduction - extractive body cue:** To jointly optimize the reasoning and execution components in FiS-VLA, we introduce a dualaware co-training strategy.
- **p. 2 / 1 Introduction - extractive body cue:** Considering these limitations, and motivated by the functional abstraction of Kahneman's dual-system theory, we raise a question: "If a VLM model serves as the central ...
- **p. 1 / Abstract - extractive body cue:** In this work, we propose Fast-in-Slow (FiS), a unified dual-system vision-language-action (VLA) model that embeds the System 1 execution module within the VLM-based System 2 ...
- **p. 1 / Abstract - extractive body cue:** This innovative paradigm not only enables high-frequency execution in System 1, but also facilitates coordination between multimodal reasoning and execution components within a single foundation ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | Additional visualizations and failure cases are provided in Appendix C and D, respectively. | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Figure 5: Visualization of generalization setting with key differences highlighted using red box. importance of the heterogeneous modality ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 34 | Figure 11: AlphaBot task execution visualization. We visualize key frames of the agent's execution process from a static ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 35 | Figure 12: Failure case visualization. We visualize the failure cases observed in four real-world experiments, with key error ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), interface p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract), objective p. 1 (1 Introduction), p. 2 (1 Introduction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
