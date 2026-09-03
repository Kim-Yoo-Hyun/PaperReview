# Problem - MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (45 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v229/mandlekar23a.html; PDF retrieval source: https://arxiv.org/pdf/2310.17596. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction)): For example, [3] showed that a dataset of over 20,000 trajectories enables generalization to tasks with modest changes in objects and goals.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Imitation learning from a large set of human demonstrations has proved to be an effective paradigm for building capable robot agents.
- **p. 1 / Abstract - extractive body cue:** However, the demonstrations can be extremely costly and time-consuming to collect.
- **p. 1 / Abstract - extractive body cue:** We introduce MimicGen, a system for automatically synthesizing large-scale, rich datasets from only a small number of human demonstrations by adapting them to new contexts.
- **p. 1 / Abstract - extractive body cue:** We use MimicGen to generate over 50K demonstrations across 18 tasks with diverse scene configurations, object instances, and robot arms from just ∼200 human demonstrations.
- **p. 1 / Abstract - extractive body cue:** We show that robot agents can be effectively trained on this generated dataset by imitation learning to achieve strong performance in longhorizon and high-precision tasks, ...
- **p. 1 / 1 Introduction - extractive body cue:** For example, [3] showed that a dataset of over 20,000 trajectories enables generalization to tasks with modest changes in objects and goals.
- **p. 1 / 1 Introduction - extractive body cue:** These works have shown that imitation learning on large diverse datasets can produce impressive performance, allowing robots to generalize toward new objects and unseen tasks.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | For example, [3] showed that a dataset of over 20,000 trajectories enables generalization to tasks with modest changes in objects and goals. | demonstration으로 정의된 robot task distribution | body wording is the source claim |
| Observation / input | All policy learning results are shown on image-based agents trained with RGB observations (see Appendix Q for low-dim agent results). | observation history와 expert trajectory/action | exact sensor/frame/preprocessing from PDF body |
| State / latent | policy, learning, image-based, agents, trained, RGB, observations, Appendix, low-dim, agent | behavior policy와 temporal action context | notation and tensor shape require body check |
| Output / action | task, default, reset, distribution, source, datasets, collected, variant | predicted action 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | closed-loop task success and robustness | imitation error, task success, robustness와 compounding error | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | observation history o_{t−H:t}; body terms: policy, learning, image-based, agents, trained, RGB, observations, Appendix, low-dim, agent | p. 5 (4 Method), p. 4 (4 Method), p. 4 (4 Method) |
| Decision / output variable | expert-like action/chunk a_{t:t+H}; body terms: make, following, contributions, introduce, MimicGen, system, generating, large | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (4 Method) |
| Objective / loss / cost | imitation or action-distribution loss; cue terms: not stated or recoverable in the selected PDF body | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | 본문 anchor 없음 |
| Success / guarantee | closed-loop task success and robustness | p. 6 (Figure/Table caption), p. 6 (6 Experiments), p. 8 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** These works have shown that imitation learning on large diverse datasets can produce impressive performance, allowing robots to generalize toward new objects and unseen tasks.
- **p. 2 / 1 Introduction - extractive body cue:** Instead, we seek to develop a general-purpose system that can be integrated seamlessly into existing imitation learning pipelines and improve the performance of a wide ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (4 Method), p. 3 (4 Method), p. 4 (4 Method)): We make the following contributions: • We introduce MimicGen, a system for generating large diverse datasets from a small number of human demonstrations by adapting the human demonstrations to novel ...

- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we introduce a novel data collection system that uses a small set of human demonstrations to automatically generate large datasets across diverse ...
- **p. 4 / 4 Method - extractive body cue:** In our experiments, we designed task variants for each robot manipulation task where we vary either the initial state distribution (D), an object in the ...
- **p. 3 / 4 Method - extractive body cue:** 4.1 Parsing the Source Dataset into Object-Centric Segments Each task consists of a sequence of object-centric subtasks (Assumption 2, Sec.
- **p. 4 / 4 Method - extractive body cue:** 2 (right), this consists of three key steps for each subtask: (1) choosing a reference subtask segment in the source dataset, (2) transforming the subtask ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | We hope that MimicGen motivates and enables exploring a more data-centric perspective on imitation learning in future work. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

il writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 5 (4 Method), p. 4 (4 Method), p. 4 (4 Method), p. 5 (4 Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), interface p. 5 (4 Method), p. 4 (4 Method), p. 4 (4 Method), p. 5 (4 Method), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (45 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** For example, [3] showed that a dataset of over 20,000 trajectories enables generalization to tasks with modest changes in objects and goals. (p. 1, 1 Introduction).
- **Formulation-changing contribution:** We make the following contributions: • We introduce MimicGen, a system for generating large diverse datasets from a small number of human demonstrations by adapting the human demonstrations to novel ... (p. 2, 1 Introduction).
- **Assumption/failure evidence:** Why might a data generation attempt result in a failure? (p. 17, 2. What are some limitations of MimicGen?).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
