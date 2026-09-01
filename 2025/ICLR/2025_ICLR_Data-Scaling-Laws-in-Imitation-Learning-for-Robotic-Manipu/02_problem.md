# Problem - Data Scaling Laws in Imitation Learning for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (34 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=pISLZG7ktL; PDF retrieval source: https://arxiv.org/pdf/2410.18647. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): (2023), most of today's robotic policies still lack comparable zero-shot generalization (Xie et al., 2024).

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive PDF cue:** Data scaling has revolutionized fields like natural language processing and computer vision, providing models with remarkable generalization capabilities.
- **p. 1 / ABSTRACT - extractive PDF cue:** In this paper, we investigate whether similar data scaling laws exist in robotics, particularly in robotic manipulation, and whether appropriate data scaling can yield single-task ...
- **p. 1 / ABSTRACT - extractive PDF cue:** To this end, we conduct a comprehensive empirical study on data scaling in imitation learning.
- **p. 1 / ABSTRACT - extractive PDF cue:** By collecting data across numerous environments and objects, we study how a policy's generalization performance changes with the number of training environments, objects, and demonstrations.
- **p. 1 / ABSTRACT - extractive PDF cue:** Throughout our research, we collect over 40,000 demonstrations and execute more than 15,000 real-world robot rollouts under a rigorous evaluation protocol.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** (2023), most of today's robotic policies still lack comparable zero-shot generalization (Xie et al., 2024).
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** While data scaling has endowed models in NLP and CV with exceptional generalization capabilities Achiam et al.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | (2023), most of today's robotic policies still lack comparable zero-shot generalization (Xie et al., 2024). | demonstration으로 정의된 robot task distribution | body wording is the source claim |
| Observation / input | There are several key observations: (1) As the number of training objects increases, the policy's performance on unseen objects consistently improves across ... | observation history와 expert trajectory/action | exact sensor/frame/preprocessing from PDF |
| State / latent | There, several, observations, number, training, objects, increases, policy, performance, unseen | behavior policy와 temporal action context | notation and tensor shape require body check |
| Output / action | Temporal, ensemble, Diffusion, Policy, predicts, sequence, actions, every | predicted action 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | closed-loop task success and robustness | imitation error, task success, robustness와 compounding error | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | observation history o_{t−H:t}; body terms: There, several, observations, number, training, objects, increases, policy, performance, unseen | p. 5 (3 APPROACH), p. 4 (3 APPROACH), p. 4 (3 APPROACH) |
| Decision / output variable | expert-like action/chunk a_{t:t+H}; body terms: answer, present, comprehensive, empirical, study, data, scaling, imitation | p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (3 APPROACH) |
| Objective / loss / cost | imitation or action-distribution loss; cue terms: UMI, portability, intuitive, design, cost, make, ideal, tool | p. 7 (3 APPROACH), p. 8 (3 APPROACH) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3 APPROACH), p. 7 (3 APPROACH), p. 8 (3 APPROACH) |
| Success / guarantee | closed-loop task success and robustness | p. 9 (32 Env-Object Pairs), p. 9 (32 Env-Object Pairs), p. 30 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** While data scaling has endowed models in NLP and CV with exceptional generalization capabilities Achiam et al.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Additionally, we examine how the number of demonstrations impacts policy generalization when the number of environments and objects is fixed.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Then, based on these data scaling laws, we propose an efficient data collection strategy to achieve the desired level of generalization (Sec.

## What the Paper Changes

PDF contribution framing (p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (3 APPROACH), p. 3 (3 APPROACH), p. 2 (1 INTRODUCTION)): To answer this, we present a comprehensive empirical study on data scaling in imitation learning, which is a predominant method for learning real-world manipulation skills (Shafiullah et al., 2024).

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Then, based on these data scaling laws, we propose an efficient data collection strategy to achieve the desired level of generalization (Sec.
- **p. 4 / 3 APPROACH - extractive PDF cue:** It enables highly efficient data collection and allows for seamless switching between different in-the-wild environments with minimal setup time.
- **p. 3 / 3 APPROACH - extractive PDF cue:** Finally, we introduce our rigorous evaluation protocol.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Our extensive investigation reveals surprising results and contributions: • Simple power laws.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | 7 DISCUSSION, LIMITATIONS, & FUTURE WORKS Data scaling is an exciting and ongoing event in robotics. | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | While this approach allows precise control over individual factors, it cannot account for all possible variation factors. | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Our work has several limitations that future research can address. | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | To ensure model capacity does not become a bottleneck when scaling data, we utilize a sufficiently large model, ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

il writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 5 (3 APPROACH), p. 4 (3 APPROACH), p. 4 (3 APPROACH), p. 5 (3 APPROACH). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), interface p. 5 (3 APPROACH), p. 4 (3 APPROACH), p. 4 (3 APPROACH), p. 5 (3 APPROACH), objective p. 7 (3 APPROACH), p. 8 (3 APPROACH).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
