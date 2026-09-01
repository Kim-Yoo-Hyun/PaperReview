# Problem - Robot Data Curation with Mutual Information Estimators

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (19 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p023.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p023.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Iyrropucrion), p. 3 (B. Demonstration Curation), p. 3 (B. Demonstration Curation), p. 4 (V. MetHop), p. 4 (I N\)): In robotics, we often do not have access to data at a similar scale due to the difficulty and cost of collection Moreover. even if we assume access to more ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** The performance of imitation learning policies often hhinges on the datasets with which they are trained.
- **p. 1 / Abstract - extractive PDF cue:** Consequently, investment in data collection for robotics has grown across both industrial and academic labs.
- **p. 1 / Abstract - extractive PDF cue:** However, despite the marked increase in the quantity of demonstrations collected, Title work has sought to assess the quality of said data despite mounting evidence ...
- **p. 1 / Abstract - extractive PDF cue:** In this work, we take a critical step towards addressing the data quality in roboties.
- **p. 1 / Abstract - extractive PDF cue:** Given a dataset f demonstrations, we aim to estimate the relative quality of individual demonstrations in terms of both action diversity and predictability.
- **p. 1 / 1. Iyrropucrion - extractive PDF cue:** In robotics, we often do not have access to data at a similar scale due to the difficulty and cost of collection Moreover. even if ...
- **p. 3 / B. Demonstration Curation - extractive PDF cue:** This is a more difficult problem than considered in prior work.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | In robotics, we often do not have access to data at a similar scale due to the difficulty and cost of collection ... | demonstration으로 정의된 robot task distribution | body wording is the source claim |
| Observation / input | In contrast, we believe metrics for imitation learning should be able to measure the relative predictability of the state-action distribution directly, which ... | observation history와 expert trajectory/action | exact sensor/frame/preprocessing from PDF |
| State / latent | contrast, believe, metrics, imitation, learning, should, able, measure, relative, predictability | behavior policy와 temporal action context | notation and tensor shape require body check |
| Output / action | want, train, policy, predict, action, state, Thus, mutual | predicted action 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | closed-loop task success and robustness | imitation error, task success, robustness와 compounding error | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | observation history o_{t−H:t}; body terms: contrast, believe, metrics, imitation, learning, should, able, measure, relative, predictability | p. 1 (1. Iyrropucrion), p. 2 (A. Imitation Learning), p. 3 (B. Demonstration Curation) |
| Decision / output variable | expert-like action/chunk a_{t:t+H}; body terms: come, challenge, Demonstration, Information, Estimation, uses, k-nearest-neighbor, k-NN | p. 4 (V. MetHop), p. 4 (V. MetHop), p. 1 (Abstract) |
| Objective / loss / cost | imitation or action-distribution loss; cue terms: bound, tribution, matching, objective, overall, align, distribution, learned | p. 3 (A. Minimizing Conditional Action Entropy), p. 3 (A. Minimizing Conditional Action Entropy), p. 18 (C. Implementation Derails) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (B. Maximizing Marginal Action Entropy), p. 4 (B. Maximizing Marginal Action Entropy), p. 18 (C. Implementation Derails) |
| Success / guarantee | closed-loop task success and robustness | p. 6 (A. Experimental Setup), p. 6 (A. Experimental Setup), p. 7 (A. Experimental Setup) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 3 / B. Demonstration Curation - extractive PDF cue:** This is a more difficult problem than considered in prior work.
- **p. 3 / B. Demonstration Curation - extractive PDF cue:** Moreover, choices made Within individual demonstrations 7, such as using differing strategies or varied approaches to complete a task, might make learning from the overall ...
- **p. 4 / V. MetHop - extractive PDF cue:** ‘Though mutual information is perhaps a natural metric for data curation, it can be practically difficult to estimate [19].
- **p. 4 / I N\ - extractive PDF cue:** It can be difficult for a policy to fit ‘demonstrations when the data collector has access to information unavailable to the policy.

## What the Paper Changes

PDF contribution framing (p. 4 (V. MetHop), p. 4 (V. MetHop), p. 1 (Abstract), p. 2 (1. Iyrropucrion), p. 2 (1. Iyrropucrion)): come this challenge we propose Demonstration Information Estimation, which uses k-nearest-neighbor (k-NN) estimates of mutual information, Our method involves three steps - representation learning, mutual information estimation, and sco ...

- **p. 4 / V. MetHop - extractive PDF cue:** In this section we propose the Demonstration Information Estimation (DemInf) method for computationally estimating mutual information for demonstration data, Though mutual information is usually considered ...
- **p. 1 / Abstract - extractive PDF cue:** Moreover, training polices based on data filtered bby our method leads to a §-10% improvement in RoboMimic and better performance on real ALOHA and Franka ...
- **p. 2 / 1. Iyrropucrion - extractive PDF cue:** To address this problem, we introduce Demonstration Information Estimation ‘or Deming for short.
- **p. 2 / 1. Iyrropucrion - extractive PDF cue:** For text data, this often consists of simple n-gram classifiers, or metadata filtering, which have been shown to have a large impact oon performance [72].

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | variance across seeds, while the parametric estimators were more unstable and had one or two runs that performed ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Note that while this metric makes sense for active learning, it does not necessarily make sense in the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | This is particularly problematic for downstream data curation, as one often does not have ground truth labels to ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | DemInf's performance is generally robust to this parameter, with no substantial change in performance in both HersheyKiss and ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

il writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (1. Iyrropucrion), p. 2 (A. Imitation Learning), p. 3 (B. Demonstration Curation), p. 4 (B. Maximizing Marginal Action Entropy). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Iyrropucrion), p. 3 (B. Demonstration Curation), p. 3 (B. Demonstration Curation), p. 4 (V. MetHop), p. 4 (I N\), interface p. 1 (1. Iyrropucrion), p. 2 (A. Imitation Learning), p. 3 (B. Demonstration Curation), p. 4 (B. Maximizing Marginal Action Entropy), objective p. 3 (A. Minimizing Conditional Action Entropy), p. 3 (A. Minimizing Conditional Action Entropy), p. 18 (C. Implementation Derails).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
