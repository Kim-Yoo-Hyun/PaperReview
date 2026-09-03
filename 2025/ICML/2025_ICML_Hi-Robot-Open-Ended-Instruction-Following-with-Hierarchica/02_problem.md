# Problem - Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=lNVHg9npif; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/165445. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Preliminaries and Problem Statement), p. 4 (3. Preliminaries and Problem Statement)): This challenge resembles the distinction between Kahneman's "System 1" and "System 2" cognitive processes (Kahneman, 2011).

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Generalist robots that can perform a range of different tasks in open-world settings must be able to not only reason about the steps needed to ...
- **p. 1 / Abstract - extractive body cue:** Intricate instructions (e.g., "Could you make me a vegetarian sandwich?" or "I don't like that one") require not just the ability to physically perform the ...
- **p. 1 / Abstract - extractive body cue:** In this work, we describe a system that uses vision-language models in a hierarchical structure, first reasoning over complex prompts and user feedback to deduce ...
- **p. 1 / Abstract - extractive body cue:** In contrast to direct instruction following methods that can fulfill simple commands ("pick up the cup"), our system can reason through complex prompts and incorporate ...
- **p. 1 / Abstract - extractive body cue:** We evaluate our system across three robotic platforms, including single-arm, dual-arm, and dualarm mobile robots, demonstrating its ability to handle tasks such as cleaning messy ...
- **p. 1 / 1. Introduction - extractive body cue:** This challenge resembles the distinction between Kahneman's "System 1" and "System 2" cognitive processes (Kahneman, 2011).
- **p. 1 / 1. Introduction - extractive body cue:** For instance, consider a robot tasked with tidying up a table after a meal: instead of rigidly following a single predefined set of steps, the ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This challenge resembles the distinction between Kahneman's "System 1" and "System 2" cognitive processes (Kahneman, 2011). | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | To this end, we provide a state-of-the-art vision-language model with a robot observation and target atomic command, and ask it to come ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | provide, state-of-the-art, vision-language, model, robot, observation, target, atomic, command, come | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | learned, policy, controls, robot, processing, observation, inputs, denote | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: provide, state-of-the-art, vision-language, model, robot, observation, target, atomic, command, come | p. 2 (1. Introduction), p. 4 (3. Preliminaries and Problem Statement), p. 3 (3. Preliminaries and Problem Statement) |
| Decision / output variable | action, pose, option or chunk a; body terms: framework, enables, robot, process, much, more, complex, prompts | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (5.1. Tasks and Baseline Methods) |
| Objective / loss / cost | policy/action modeling objective; cue terms: train, high-level, policy, t/I1, Dsyn, Dlabeled, cross-entropy, loss | p. 5 (4.3. Data Collection and Training Hi Robot), p. 5 (4.3. Data Collection and Training Hi Robot) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (4.3. Data Collection and Training Hi Robot), p. 5 (4.3. Data Collection and Training Hi Robot), p. 7 (5.1. Tasks and Baseline Methods) |
| Success / guarantee | instruction-conditioned task success | p. 7 (5.2. Metrics and Evaluation Protocol), p. 8 (5.3. Core Results), p. 8 (5.2. Metrics and Evaluation Protocol) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** For instance, consider a robot tasked with tidying up a table after a meal: instead of rigidly following a single predefined set of steps, the ...
- **p. 2 / 1. Introduction - extractive body cue:** This low-level policy is itself a vision-language model finetuned for producing robotic actions, also known as a visionlanguage-action (VLA) model (Black et al., 2024; Brohan ...
- **p. 3 / 3. Preliminaries and Problem Statement - extractive body cue:** A particularly powerful approach for handling such complex semantics is provided by visionlanguage-action (VLA) models (Black et al., 2024; Brohan et al., 2023a; Kim et ...
- **p. 4 / 3. Preliminaries and Problem Statement - extractive body cue:** We build on the π0 VLA (Black et al., 2024), which additionally handles multiple images and continuous state observations qt, and modifies the VLM to ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (5.1. Tasks and Baseline Methods), p. 7 (5.1. Tasks and Baseline Methods), p. 4 (3. Preliminaries and Problem Statement)): We show that our framework enables a robot to process much more complex prompts than prior end-to-end instruction following systems and incorporate feedback during task execution (Figure 1).

- **p. 2 / 1. Introduction - extractive body cue:** The main contribution of our paper is a hierarchical interactive robot learning system (Hi Robot), a novel framework that uses VLMs for both high-level reasoning ...
- **p. 5 / 5.1. Tasks and Baseline Methods - extractive body cue:** The training data consists of full table cleaning episodes.
- **p. 7 / 5.1. Tasks and Baseline Methods - extractive body cue:** Hi Robot without synthetic data: This ablation corresponds to our method without synthetic training data, evaluating the importance of including diverse syntheticallygenerated prompts in training.
- **p. 4 / 3. Preliminaries and Problem Statement - extractive body cue:** The policy consists of a high-level and a low-level policy.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | Our system also has a number of limitations that could be studied in future work. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | With human high-level instructions, the lowlevel policy executes nearly flawlessly, showing that failures stem more from reasoning than ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Coupling these two layers more directly, e.g. by allowing the high-level policy to be more aware of how ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | GPT-4o, however, often fails to maintain a coherent internal state, leading to commands like picking up new objects ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1. Introduction), p. 4 (3. Preliminaries and Problem Statement), p. 3 (3. Preliminaries and Problem Statement), p. 4 (3. Preliminaries and Problem Statement). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Preliminaries and Problem Statement), p. 4 (3. Preliminaries and Problem Statement), interface p. 2 (1. Introduction), p. 4 (3. Preliminaries and Problem Statement), p. 3 (3. Preliminaries and Problem Statement), p. 4 (3. Preliminaries and Problem Statement), objective p. 5 (4.3. Data Collection and Training Hi Robot), p. 5 (4.3. Data Collection and Training Hi Robot).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
