# Problem - Bridging Perception and Action: Spatially-Grounded Mid-Level Representations for Robot Generalization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p155.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p155.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Ivrropuction), p. 2 (1. Ivrropuction), p. 3 (1. Ivrropuction), p. 1 (1. Ivrropuction), p. 2 (1. Ivrropuction)): Large pre-trained robotics models have made significant progress in recent years towards improving robotic generalization capabilities by leveraging large-scale pre-training datasets, However, these models still face challenges in adapt ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** In this work, we investigate how spatially-grounded auxiliary representations can provide both broad, high-level grounding, as well as direct, actionable information to help policy learning ...
- **p. 1 / Abstract - extractive body cue:** We study these mid-level representations across three ‘critical dimensions: object-centricity, pose-awareness, and depthawareness.
- **p. 1 / Abstract - extractive body cue:** We use these interpretable mid-level representations to train specialist encoders via supervised learning, then use these representations as inputs to a diffusion policy to solve ...
- **p. 1 / Abstract - extractive body cue:** We propose a novel mixture-of-experts policy architecture that can combine multiple specialized expert models, each trained on a distinct ‘mid-level representation, to improve the generalization ...
- **p. 1 / Abstract - extractive body cue:** This method achieves an average of 11% hi rate on average over a language-grounded baseline and a 21% higher success rate over a standard diffusion ...
- **p. 1 / 1. Ivrropuction - extractive body cue:** Large pre-trained robotics models have made significant progress in recent years towards improving robotic generalization capabilities by leveraging large-scale pre-training datasets, However, these models still ...
- **p. 2 / 1. Ivrropuction - extractive body cue:** A key challenge with the multi-task policy learning regime is in obtaining policies that generalize to new objects, task variants, environmental factors and so on, ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Large pre-trained robotics models have made significant progress in recent years towards improving robotic generalization capabilities by leveraging large-scale pre-training datasets, However, ... | multi-robot demonstration/dataset ecosystem | body wording is the source claim |
| Observation / input | By iteratively refining the training data and adjusting the weighting of consistent samples, our method creates a feedback loop that promotes tighter ... | multi-view observation, language/task label과 action trajectory | exact sensor/frame/preprocessing from PDF |
| State / latent | iteratively, refining, training, data, adjusting, weighting, consistent, samples, creates, feedback | shared representation, embodiment/task identity와 data distribution | notation and tensor shape require body check |
| Output / action | analyzing, relationship, view, mid-level, representations, bridge, between, sensory | dataset sample 또는 learned policy action | exact unit/frame/decoder require body check |
| Target outcome | cross-domain transfer and task performance | coverage, cross-embodiment transfer, data efficiency와 task success | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | trajectory D with task/embodiment metadata; body terms: iteratively, refining, training, data, adjusting, weighting, consistent, samples, creates, feedback | p. 6 (B. Training), p. 4 (V. ARCHITECTURE), p. 3 (1. Ivrropuction) |
| Decision / output variable | normalized sample or downstream action; body terms: while, different, mid-level, representations, excel, tasks, leverage, task-specitfic | p. 2 (1. Ivrropuction), p. 6 (B. Training), p. 1 (Abstract) |
| Objective / loss / cost | coverage/data efficiency/transfer objective; cue terms: where, represents, advantage, function, modulates, policy, gradient, loss | p. 6 (B. Training), p. 5 (B. Training), p. 6 (B. Training) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (B. Training), p. 5 (B. Training), p. 9 (C. Different Architectures offer Different Tradeoffs berween) |
| Success / guarantee | cross-domain transfer and task performance | p. 1 (Figure/Table caption), p. 6 (Figure/Table caption), p. 8 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Ivrropuction - extractive body cue:** A key challenge with the multi-task policy learning regime is in obtaining policies that generalize to new objects, task variants, environmental factors and so on, ...
- **p. 3 / 1. Ivrropuction - extractive body cue:** While one can hope to learn these relationships directly from end-to-end data, current large-scale robot policies that try to scale up imitation learning still struggle ...
- **p. 1 / 1. Ivrropuction - extractive body cue:** An increasingly popular approach to address this challenge is explicitly establishing deeper connections between robot policies and the abstract patterns and relationships that govern the ...
- **p. 2 / 1. Ivrropuction - extractive body cue:** For instance, for a robot tasked with folding a shirt, a bounding box may help locate a shir's general position but fails to provide actionable ...

## What the Paper Changes

PDF contribution framing (p. 2 (1. Ivrropuction), p. 6 (B. Training), p. 1 (Abstract), p. 2 (1. Ivrropuction), p. 3 (1. Ivrropuction)): We show that while different mid-level representations excel at different tasks, our method can leverage these task-specitfic benefits to achieve consistently higher performance on a wide range of environments.

- **p. 6 / B. Training - extractive body cue:** Similarly, our approach integrates mid-level expert outputs as implicit guidance in scenarios where no explicit reward signal is available, Instead of an advantage function, we ...
- **p. 1 / Abstract - extractive body cue:** We propose a novel mixture-of-experts policy architecture that can combine multiple specialized expert models, each trained on a distinct ‘mid-level representation, to improve the generalization ...
- **p. 2 / 1. Ivrropuction - extractive body cue:** We find that reliance on structured signals presents a trade-off: policies that depend heavily on these representations can become more susceptible to overfiting and reduced ...
- **p. 3 / 1. Ivrropuction - extractive body cue:** While one can hope to learn these relationships directly from end-to-end data, current large-scale robot policies that try to scale up imitation learning still struggle ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | tween responsiveness to structured mid-level representations and robustness to noise or spurious inputs? | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Meanwhile, Table I! records the sensitivity scores for each of our mid-level experts as well as the robustness ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | This suggests that the benefits of more targeted feature utilization outweigh the slight decrease in robustness. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

robot_data writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 6 (B. Training), p. 4 (V. ARCHITECTURE), p. 3 (1. Ivrropuction), p. 4 (1. Ivrropuction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Ivrropuction), p. 2 (1. Ivrropuction), p. 3 (1. Ivrropuction), p. 1 (1. Ivrropuction), p. 2 (1. Ivrropuction), interface p. 6 (B. Training), p. 4 (V. ARCHITECTURE), p. 3 (1. Ivrropuction), p. 4 (1. Ivrropuction), objective p. 6 (B. Training), p. 5 (B. Training), p. 6 (B. Training).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
