# Problem - SocialNav-SUB: Benchmarking VLMs for Scene Understanding in Social Robot Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v305/munje25a.html; PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v305/main/assets/munje25a/munje25a.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction)): By bridging the gap between VLM capabilities and the challenges of social robot navigation, our work provides a foundation for advancing the use of VLMs for social robot navigation.

## PDF Body Digest

- **p. 1 / 1 Introduction - extractive body cue:** Social robot navigation, defined as the ability for robots to move effectively and safely within human-populated environments while adhering to social norms, is a fundamental ...
- **p. 1 / 1 Introduction - extractive body cue:** As shown in Figure 1, navigating through social navigation scenarios requires robots to interpret human intentions, adhere to social norms, and reason about spatial and ...
- **p. 1 / 1 Introduction - extractive body cue:** While promising, learning-based methods that are trained on small datasets and conventional methods are often validated in controlled scenarios with a small number of people, ...
- **p. 2 / 1 Introduction - extractive body cue:** The ability to determine socially compliant navigation actions requires understanding each dynamic scene by spatiotemporal reasoning (e.g. the movements of people in the scene) and ...
- **p. 2 / 1 Introduction - extractive body cue:** Trained in diverse large-scale multimodal datasets that span various real-world scenarios, large VLMs often learn underlying patterns of human behavior that may implicitly encode an ...
- **p. 2 / 1 Introduction - extractive body cue:** By bridging the gap between VLM capabilities and the challenges of social robot navigation, our work provides a foundation for advancing the use of VLMs ...
- **p. 2 / 1 Introduction - extractive body cue:** Existing evaluations have offered only partial assessments [9, 10], often focusing on controlled settings or lacking temporal components, leading to an incomplete picture of how ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | By bridging the gap between VLM capabilities and the challenges of social robot navigation, our work provides a foundation for advancing the ... | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | Moreover, studies such as SPACE [10] indicate that state-of-the-art large VLMs still lack robust spatial reasoning, raising questions about whether VLMs can ... | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF body |
| State / latent | Moreover, studies, SPACE, indicate, state-of-the-art, large, VLMs, still, lack, robust | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | Through, experiments, state-of-the-art, VLMs, find, while, best-performing, VLM | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: Moreover, studies, SPACE, indicate, state-of-the-art, large, VLMs, still, lack, robust | p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (Body text (section not recovered)) |
| Decision / output variable | method trajectory/action; body terms: introduce, Social, Navigation, Scene, Understanding, Benchmark, SOCIALNAVSUB, novel | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: Through, experiments, state-of-the-art, VLMs, find, while, best-performing, VLM | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (Body text (section not recovered)) |
| Success / guarantee | comparable score and protocol validity | p. 14 (7 Appendix), p. 7 (Figure/Table caption), p. 19 (7 Appendix) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive body cue:** Existing evaluations have offered only partial assessments [9, 10], often focusing on controlled settings or lacking temporal components, leading to an incomplete picture of how ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1 Introduction), p. 2 (1 Introduction)): In this paper, we introduce the Social Navigation Scene Understanding Benchmark (SOCIALNAVSUB), a novel Visual Question Answering (VQA) benchmark designed to evaluate VLMs on social robot navigation tasks.

- **p. 2 / 1 Introduction - extractive body cue:** Social Navigation VQA Benchmark for VLMs: We introduce the first VQA benchmark for assessing VLMs' capabilities in social robot navigation scenarios using 60 unique scenarios ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Overall, our evaluation reveals that while state-of-the-art large VLMs like OpenAI o4-mini and Gemini 2.0 show promising advances, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 17 | 7.6 Failure Case Analysis As mentioned in Section 4.2, we found cases of VLMs in the experiment failing ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 18 | Figure 9: Examples of failure cases for VLMs. Top-left: Failing to recognize that person 5 is on the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 19 | Overall FR is the model's failure rate with standard error in smaller type. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (Body text (section not recovered)), p. 2 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), interface p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (Body text (section not recovered)), p. 2 (1 Introduction), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
