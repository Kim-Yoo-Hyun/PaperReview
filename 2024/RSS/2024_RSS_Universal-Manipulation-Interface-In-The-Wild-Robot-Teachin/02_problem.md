# Problem - Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p045.html; PDF retrieval source: https://arxiv.org/pdf/2402.10329. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): Unfortunately, neither ∗Indicates equal contribution is sufficient, as teleoperation requires high setup costs for hardware and expert operators, while human videos exhibit a large embodiment gap to robots.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We present Universal Manipulation Interface (UMI) - a data collection and policy learning framework that allows direct skill transfer from in-the-wild human demonstrations to deployable ...
- **p. 1 / Abstract - extractive body cue:** UMI employs hand-held grippers coupled with careful interface design to enable portable, lowcost, and information-rich data collection for challenging bimanual and dynamic manipulation demonstrations.
- **p. 1 / Abstract - extractive body cue:** To facilitate deployable policy learning, UMI incorporates a carefully designed policy interface with inference-time latency matching and a relative-trajectory action representation.
- **p. 1 / Abstract - extractive body cue:** The resulting learned policies are hardware-agnostic and deployable across multiple robot platforms.
- **p. 1 / Abstract - extractive body cue:** Equipped with these features, UMI framework unlocks new robot manipulation capabilities, allowing zeroshot generalizable dynamic, bimanual, precise, and long-horizon behaviors, by only changing the training ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Unfortunately, neither ∗Indicates equal contribution is sufficient, as teleoperation requires high setup costs for hardware and expert operators, while human videos exhibit a large embodiment ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** As a result, despite achieving impressive visual diversity across hundreds of environments, the collected actions are constrained to simple grasping [41] or quasi-static pick-andplace [50, ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Unfortunately, neither ∗Indicates equal contribution is sufficient, as teleoperation requires high setup costs for hardware and expert operators, while human videos exhibit ... | demonstration으로 정의된 robot task distribution | body wording is the source claim |
| Observation / input | When combined with the GoPro's built-in IMU sensor, we can enable robust tracking under fast motion. • Second, we explore the right ... | observation history와 expert trajectory/action | exact sensor/frame/preprocessing from PDF |
| State / latent | When, combined, GoPro, built-in, IMU, sensor, enable, robust, tracking, under | behavior policy와 temporal action context | notation and tensor shape require body check |
| Output / action | While, users, theoretically, collect, actions, hand-held, devices, much | predicted action 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | closed-loop task success and robustness | imitation error, task success, robustness와 compounding error | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | observation history o_{t−H:t}; body terms: When, combined, GoPro, built-in, IMU, sensor, enable, robust, tracking, under | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Decision / output variable | expert-like action/chunk a_{t:t+H}; body terms: Unfortunately, neither, Indicates, equal, contribution, sufficient, teleoperation, requires | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective / loss / cost | imitation or action-distribution loss; cue terms: not recovered | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | 본문 anchor 없음 |
| Success / guarantee | closed-loop task success and robustness | p. 8 (V. CAPABILITY EXPERIMENTS), p. 11 (Figure/Table caption), p. 7 (V. CAPABILITY EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** As a result, despite achieving impressive visual diversity across hundreds of environments, the collected actions are constrained to simple grasping [41] or quasi-static pick-andplace [50, ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** This issue is especially salient for fast and dynamic actions. • Insufficient policy representation: Prior works often use simple policy representations (e.g., MLPs) with action ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Furthermore, when trained with diverse human demonstrations, the final policy exhibits zero-shot generalization to novel environments and objects, achieving a remarkable 70% success rate in ...

## What the Paper Changes

PDF contribution framing (p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 3 (III. METHOD)): Unfortunately, neither ∗Indicates equal contribution is sufficient, as teleoperation requires high setup costs for hardware and expert operators, while human videos exhibit a large embodiment gap to robots.

- **p. 2 / I. INTRODUCTION - extractive body cue:** 2), we show that UMI is capable of achieving a wide range of manipulation tasks that involve dynamic, bimanual, precise and long-horizon actions by only ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Furthermore, when trained with diverse human demonstrations, the final policy exhibits zero-shot generalization to novel environments and objects, achieving a remarkable 70% success rate in ...
- **p. 3 / III. METHOD - extractive body cue:** It is designed with the following goals in mind: • Portable.
- **p. 3 / III. METHOD - extractive body cue:** Universal Manipulation Interface (UMI) is hand-held data collection and policy learning framework that allows direct transfer from in-the-wild human demonstrations to deployable robot policies.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 11 | While UMI demonstrates policy efficacy across a wide range of tasks and scenarios, a few limitations remain. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Beyond the expected failure mode where the cup is outside of camera view, we found this baseline policy ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | This experiment achieves 18/20 = 90% success rate, with the 2 failure cases being joint limit violations, which ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | (b) Typical failure mode of the baseline/ablation policy. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

il writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. METHOD), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
