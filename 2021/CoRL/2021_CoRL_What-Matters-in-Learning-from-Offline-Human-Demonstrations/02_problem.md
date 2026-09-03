# Problem - What Matters in Learning from Offline Human Demonstrations for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v164/mandlekar22a.html; PDF retrieval source: https://proceedings.mlr.press/v164/mandlekar22a/mandlekar22a.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction)): Unfortunately, a lack of suitable benchmark and human datasets have made studying this setting difficult.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Imitating human demonstrations is a promising approach to endow robots with various manipulation capabilities.
- **p. 1 / Abstract - extractive body cue:** While recent advances have been made in imitation learning and batch (offline) reinforcement learning, a lack of open-source human datasets and reproducible learning methods make ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we conduct an extensive study of six offline learning algorithms for robot manipulation on five simulated and three real-world multi-stage manipulation tasks ...
- **p. 1 / Abstract - extractive body cue:** Our study analyzes the most critical challenges when learning from offline human data for manipulation.
- **p. 1 / Abstract - extractive body cue:** Based on the study, we derive a series of lessons including the sensitivity to different algorithmic design choices, the dependence on the quality of the ...
- **p. 2 / 1 Introduction - extractive body cue:** Unfortunately, a lack of suitable benchmark and human datasets have made studying this setting difficult.
- **p. 2 / 1 Introduction - extractive body cue:** Studying these challenges in the context of robot manipulation and human-provided datasets could be a stepping stone to closing the gap between robot and human ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Unfortunately, a lack of suitable benchmark and human datasets have made studying this setting difficult. | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | Offline policy learning is sensitive to the state and action space coverage in the dataset, and by extension, the size of the ... | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF body |
| State / latent | Offline, policy, learning, sensitive, state, action, space, coverage, dataset, extension | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | Human, demonstrations, differ, machine-generated, datasets, recent, trend, benchmarks | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: Offline, policy, learning, sensitive, state, action, space, coverage, dataset, extension | p. 3 (Dataset), p. 4 (Dataset), p. 2 (1 Introduction) |
| Decision / output variable | method trajectory/action; body terms: present, success, rates, averaged, over, seeds, across, low-dim | p. 3 (Dataset) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: Unlike, traditional, supervised, learning, where, model, selection, achieved | p. 3 (Dataset), p. 1 (Abstract), p. 2 (1 Introduction), p. 5 (Dataset) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (1 Introduction), p. 3 (Dataset), p. 5 (Dataset) |
| Success / guarantee | comparable score and protocol validity | p. 5 (Figure/Table caption), p. 3 (Dataset), p. 3 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive body cue:** Studying these challenges in the context of robot manipulation and human-provided datasets could be a stepping stone to closing the gap between robot and human ...
- **p. 1 / 1 Introduction - extractive body cue:** What has inhibited the use of large human-provided datasets to address this gap?
- **p. 1 / 1 Introduction - extractive body cue:** Despite these advances, the offline learning paradigm has not been nearly as disruptive in robotics as in other disciplines - there is a large gap ...

## What the Paper Changes

PDF body contribution framing (p. 3 (Dataset)): We present success rates averaged over 3 seeds for each method across the low-dim Machine-Generated (MG), Proficient-Human (PH), and Multi-Human (MH) datasets.

- additional contribution PDF body cue not selected; no claim inferred

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 4 | We present success rates averaged over 3 seeds for each method across different subsets of the Multi-Human datasets, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | There is a strong expectation for batch RL algorithms to be able to distinguish between actions leading to ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | The final row of Table 2 shows additional results on a diagnostic dataset termed Can-Paired, where a single ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | In this section, we summarize the lessons from our study and make recommendations for future work. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (Dataset), p. 4 (Dataset), p. 2 (1 Introduction), p. 2 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), interface p. 3 (Dataset), p. 4 (Dataset), p. 2 (1 Introduction), p. 2 (1 Introduction), objective p. 3 (Dataset), p. 1 (Abstract), p. 2 (1 Introduction), p. 5 (Dataset).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** Unfortunately, a lack of suitable benchmark and human datasets have made studying this setting difficult. (p. 2, 1 Introduction).
- **Formulation-changing contribution:** Differences from classic supervised learning, such as a mismatch between training and evaluation objectives (task success rate), can make selecting a final policy challenging [21, 22], especially in real-world settings ... (p. 2, 1 Introduction).
- **Assumption/failure evidence:** We present success rates averaged over 3 seeds for each method across different subsets of the Multi-Human datasets, corresponding to mixtures of demonstrations from "Better", "Adequate", and "Worse" human operators, ... (p. 4, Dataset).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
