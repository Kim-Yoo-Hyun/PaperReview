# SocialNav-SUB: Benchmarking VLMs for Scene Understanding in Social Robot Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v305/munje25a.html.
> PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v305/main/assets/munje25a/munje25a.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: VLM, Navigation, Benchmark
- Official paper: https://proceedings.mlr.press/v305/munje25a.html
- Full-text retrieval: https://raw.githubusercontent.com/mlresearch/v305/main/assets/munje25a/munje25a.pdf
- Code/Project: not identified
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 benchmark 문제를 이해하기 위해 읽는다. 본문은 By bridging the gap between VLM capabilities and the challenges of social robot navigation, our work provides a foundation for advancing the use of VLMs for social robot navigation.를 문제로 두고, In this paper, we introduce the Social Navigation Scene Understanding Benchmark (SOCIALNAVSUB), a novel Visual Question Answering (VQA) benchmark designed to evaluate VLMs on social robot navigation tasks.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** Social robot navigation, defined as the ability for robots to move effectively and safely within human-populated environments while adhering to social norms, is a fundamental ...
- **p. 1 / 1 Introduction - extractive body cue:** As shown in Figure 1, navigating through social navigation scenarios requires robots to interpret human intentions, adhere to social norms, and reason about spatial and ...
- **p. 1 / 1 Introduction - extractive body cue:** While promising, learning-based methods that are trained on small datasets and conventional methods are often validated in controlled scenarios with a small number of people, ...
- **p. 2 / 1 Introduction - extractive body cue:** The ability to determine socially compliant navigation actions requires understanding each dynamic scene by spatiotemporal reasoning (e.g. the movements of people in the scene) and ...
- **p. 2 / 1 Introduction - extractive body cue:** Trained in diverse large-scale multimodal datasets that span various real-world scenarios, large VLMs often learn underlying patterns of human behavior that may implicitly encode an ...
- **p. 2 / 1 Introduction - extractive body cue:** By bridging the gap between VLM capabilities and the challenges of social robot navigation, our work provides a foundation for advancing the use of VLMs ...
- **p. 2 / 1 Introduction - extractive body cue:** Existing evaluations have offered only partial assessments [9, 10], often focusing on controlled settings or lacking temporal components, leading to an incomplete picture of how ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we introduce the Social Navigation Scene Understanding Benchmark (SOCIALNAVSUB), a novel Visual Question Answering (VQA) benchmark designed to evaluate VLMs on social ...
- **p. 2 / 1 Introduction - extractive body cue:** Social Navigation VQA Benchmark for VLMs: We introduce the first VQA benchmark for assessing VLMs' capabilities in social robot navigation scenarios using 60 unique scenarios ...
- **p. 2 / 1 Introduction - extractive body cue:** Moreover, studies such as SPACE [10] indicate that state-of-the-art large VLMs still lack robust spatial reasoning, raising questions about whether VLMs can understand scenes of ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** Our benchmark sets the stage for further research on foundation models for social robot navigation, offering a framework to explore how VLMs can be tailored ...
- **p. 1 / 1 Introduction - extractive body cue:** As shown in Figure 1, navigating through social navigation scenarios requires robots to interpret human intentions, adhere to social norms, and reason about spatial and ...
- **p. 2 / 1 Introduction - extractive body cue:** We run experiments on state-of-the-art large VLMs which reveal notable performance gaps between state-of-the-art large VLMs and both human and rule-based baselines.
- **p. 3 / 1 Introduction - extractive body cue:** All models perform worse than human oracle and rule-based performance.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Moreover, studies such as SPACE [10] indicate that state-of-the-art large VLMs still lack robust spatial reasoning, raising questions about whether VLMs can understand scenes of complex, realistic social navigation scenarios at all ... | standardized observation, action, task state와 evaluation split | p. 2 (1 Introduction), p. 1 (1 Introduction) |
| State/latent | Moreover, studies, SPACE, indicate, state-of-the-art, large, VLMs, still, lack, robust, spatial, reasoning | benchmark state/goal와 method decision | p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (Body text (section not recovered)) |
| Output/action | As shown in Figure 1, navigating through social navigation scenarios requires robots to interpret human intentions, adhere to social norms, and reason about spatial and temporal interactions to respond to dynamic environments. | policy/controller trajectory 또는 measured result | p. 1 (1 Introduction), p. 1 (Body text (section not recovered)), p. 2 (1 Introduction) |
| Objective/outcome | Through experiments with state-of-the-art VLMs, we find that while the best-performing VLM achieves an encouraging probability of agreeing with human answers, it still underperforms simpler rule-based approach and human consensus baseli ... | success metric, robustness, generalization과 reproducibility | p. 1 (Body text (section not recovered)) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we introduce the Social Navigation Scene Understanding Benchmark (SOCIALNAVSUB), a novel Visual Question Answering (VQA) benchmark designed to evaluate VLMs on social ...
- **p. 2 / 1 Introduction - extractive body cue:** Social Navigation VQA Benchmark for VLMs: We introduce the first VQA benchmark for assessing VLMs' capabilities in social robot navigation scenarios using 60 unique scenarios ...
- **p. 14 / 7 Appendix - extractive body cue:** Overall, when scene context is extracted from the human oracle's responses, VLM performance significantly improves compared to using no context or randomly generated context, and ...
- **p. 23 / 7 Appendix - extractive body cue:** The results indicate that removing the CoT component does not significantly affect spatial and spatiotemporal reasoning performance.
- **p. 24 / 7 Appendix - extractive body cue:** These results indicate that a strong spatial and spatiotemporal reasoning capabilities can lead to significantly better performance on social reasoning questions.
- **p. 15 / 7 Appendix - extractive body cue:** Estimates achieve an average displacement error of 0.67±0.14 m across all samples.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Average Performance Across Question Categories. The metrics used are PA and CWPA for all questions and for each question category, along with standard ...
- **p. 14 / 7 Appendix - extractive body cue:** The evaluation results are averaged over 5 runs, and we report mean accuracy ± standard error.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 14 (7 Appendix), p. 23 (7 Appendix) |
| Embodiment/environment | 7.1 Waypoint Selection Experiments To further demonstrate the practical value of SOCIALNAV-SUB in real-world social robot navigation, we conduct preliminary experiments examining how scene understanding influences VLMs' performance in w ... | hardware/simulator version and reset protocol | p. 14 (7 Appendix), p. 14 (7 Appendix) |
| Dataset/benchmark | These illustrate variation in environment type, crowd density, and human-robot proximity. | role, split, size and leakage | p. 14 (7 Appendix), p. 14 (7 Appendix), p. 15 (7 Appendix), p. 19 (7 Appendix) |
| Metric | The evaluation results are averaged over 5 runs, and we report mean accuracy ± standard error. | definition, denominator, direction and uncertainty | p. 14 (7 Appendix), p. 7 (Figure/Table caption), p. 19 (7 Appendix) |
| Baseline/ablation | Figure 2: An overview of SOCIALNAV-SUB, which facilitates the systematic evaluation of VLMs in social robot navigation scenarios. Using SCAND data, human-labeled VQA datasets, and var- ious VLMs, this framework offers the ... | fair input/data/compute/action matching | p. 3 (Figure/Table caption), p. 14 (7 Appendix), p. 23 (7 Appendix) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.3 Discussion - extractive body cue:** Overall, our evaluation reveals that while state-of-the-art large VLMs like OpenAI o4-mini and Gemini 2.0 show promising advances, they still fall short of human oracle ...
- **p. 17 / 7 Appendix - extractive body cue:** 7.6 Failure Case Analysis As mentioned in Section 4.2, we found cases of VLMs in the experiment failing on questions with high human consensus in ...
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 9: Examples of failure cases for VLMs. Top-left: Failing to recognize that person 5 is on the left. Top-right: Failing to recognize that person ...
- **p. 19 / 7 Appendix - extractive body cue:** Overall FR is the model's failure rate with standard error in smaller type.
- **p. 19 / 7 Appendix - extractive body cue:** Overall 33.8% failure rate; very limited Robot Action to Person diversity-only avoiding (53.1%) and not considering (6.38%).
- **p. 15 / 7 Appendix - extractive body cue:** Since SCAND does not provide 3D human pose labels, we validated this pipeline and tuned the hyperparameters on the CODa dataset [41], which provides high-quality ...
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 5: Examples of scenes from SOCIALNAV-SUB. These illustrate variation in environment type, crowd density, and human-robot proximity. SOCIALNAV-SUB comprises 60 social robot navigation scenarios ...

## Why Read It

Robotics-enabling 3D perception의 benchmark 문제를 이해하기 위해 읽는다. 본문은 By bridging the gap between VLM capabilities and the challenges of social robot navigation, our work provides a foundation for advancing the use of VLMs for social robot navigation.를 문제로 두고, In this paper, we introduce the Social Navigation Scene Understanding Benchmark (SOCIALNAVSUB), a novel Visual Question Answering (VQA) benchmark designed to evaluate VLMs on social robot navigation tasks.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Body text (section not recovered)), p. 1 (1 Introduction), p. 2 (1 Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
