# Problem - SAFE: Multitask Failure Detection for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (36 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.neurips.cc/paper_files/paper/2025/hash/392d0d05e2f514063e6ce6f8b370834c-Abstract-Conference.html; PDF retrieval source: https://proceedings.neurips.cc/paper_files/paper/2025/file/392d0d05e2f514063e6ce6f8b370834c-Paper-Conference.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction)): However, when VLAs are directly deployed on unseen tasks without collecting additional demonstrations and finetuning the model, they still suffer from limited success rates and a wide range of failure ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** While vision-language-action models (VLAs) have shown promising robotic behaviors across a diverse set of manipulation tasks, they achieve limited success rates when deployed on novel ...
- **p. 1 / Abstract - extractive body cue:** To allow these policies to safely interact with their environments, we need a failure detector that gives a timely alert such that the robot can ...
- **p. 1 / Abstract - extractive body cue:** However, existing failure detectors are trained and tested only on one or a few specific tasks, while generalist VLAs require the detector to generalize and ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce the multitask failure detection problem and propose SAFE, a failure detector for generalist robot policies such as VLAs.
- **p. 1 / Abstract - extractive body cue:** We analyze the VLA feature space and find that VLAs have sufficient highlevel knowledge about task success and failure, which is generic across different tasks.
- **p. 1 / 1 Introduction - extractive body cue:** However, when VLAs are directly deployed on unseen tasks without collecting additional demonstrations and finetuning the model, they still suffer from limited success rates and ...
- **p. 1 / 1 Introduction - extractive body cue:** Most existing failure detection methods train a separate failure detector for each task, and evaluate the detector only on that task [8-17].

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, when VLAs are directly deployed on unseen tasks without collecting additional demonstrations and finetuning the model, they still suffer from limited ... | uncertain robot state와 safe/unsafe operating region | body wording is the source claim |
| Observation / input | Encoder 𝒐𝑡 𝑙𝑡 Decoder 𝒆𝑡 Action: 𝑨𝑡 Observation Instruction VLA Model 𝒆1 SAFE-MLP SAFE-LSTM MLP ǁ𝑠1 𝒆2 MLP ǁ𝑠2 𝒆3 MLP ǁ𝑠3 ... | observation, uncertainty/risk estimate와 task command | exact sensor/frame/preprocessing from PDF |
| State / latent | Encoder, Decoder, Action, Observation, Instruction, VLA, Model, SAFE-MLP, SAFE-LSTM, MLP | safe set, recovery state 또는 constraint margin | notation and tensor shape require body check |
| Output / action | contributions, summarized, follows, analyze, VLA, feature, space, across | shielded, recovery 또는 safe action | exact unit/frame/decoder require body check |
| Target outcome | low violation/failure probability with useful intervention | task return과 violation/failure probability | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | state/history and risk h(s); body terms: Encoder, Decoder, Action, Observation, Instruction, VLA, Model, SAFE-MLP, SAFE-LSTM, MLP | p. 5 (4 Method), p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Decision / output variable | filtered/recovery action u_safe; body terms: contributions, summarized, follows, analyze, VLA, feature, space, across | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction) |
| Objective / loss / cost | task utility subject to safety constraint; cue terms: further, illustrates, VLA, features, evolve, feature, space, when | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (4 Method), p. 4 (4 Method) |
| Success / guarantee | low violation/failure probability with useful intervention | p. 6 (5 Experiments), p. 10 (6 Results), p. 10 (6 Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** Most existing failure detection methods train a separate failure detector for each task, and evaluate the detector only on that task [8-17].
- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we focus on the multitask failure detection problem.
- **p. 2 / 1 Introduction - extractive body cue:** To tackle this problem, we study the internal features of VLAs and find that they capture high-level knowledge about task success and failure.

## What the Paper Changes

PDF contribution framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction)): The contributions of our paper can be summarized as follows: • We analyze the VLA feature space and show that, across different task instructions and environments, the internal features of ...

- **p. 2 / 1 Introduction - extractive body cue:** Based on this insight, we introduce SAFE, a ScAlable Failure Estimation method that scales across diverse tasks for generalist policies like VLAs.
- **p. 1 / 1 Introduction - extractive body cue:** VLAs are designed to accomplish diverse tasks and may frequently encounter novel task instructions and unseen environments during deployment.
- **p. 1 / 1 Introduction - extractive body cue:** Recently, scaling up robot manipulation datasets has enabled the development of large visionlanguage-action (VLA) models, which are generalist manipulation policies that can follow language instructions ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 4 | Figure 1: The internal features of a VLA capture high-level information about task success and failure. When the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Figure 5: Failures detected by SAFE-LSTM align well with the actual robot failures, as shown in the corresponding ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Table 1: Failure detection results on simulation benchmarks, measured by area under ROC (ROC- AUC). "-" indicates that ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Inspired by this observation, we design SAFE, which uses the internal features of VLAs for failure detection. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

safety writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 5 (4 Method), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 4 (4 Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), interface p. 5 (4 Method), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 4 (4 Method), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
