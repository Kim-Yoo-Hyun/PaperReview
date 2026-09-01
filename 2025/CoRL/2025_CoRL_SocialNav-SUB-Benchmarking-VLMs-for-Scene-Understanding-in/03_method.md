# Method - SocialNav-SUB: Benchmarking VLMs for Scene Understanding in Social Robot Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v305/munje25a.html; PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v305/main/assets/munje25a/munje25a.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction)): Moreover, studies such as SPACE [10] indicate that state-of-the-art large VLMs still lack robust spatial reasoning, raising questions about whether VLMs can understand scenes of complex, realistic social navigation scenarios ...

## Method Body Digest

- **p. 2 / 1 Introduction - extractive PDF cue:** Moreover, studies such as SPACE [10] indicate that state-of-the-art large VLMs still lack robust spatial reasoning, raising questions about whether VLMs can understand scenes of ...
- **p. 1 / 1 Introduction - extractive PDF cue:** As shown in Figure 1, navigating through social navigation scenarios requires robots to interpret human intentions, adhere to social norms, and reason about spatial and ...
- **p. 2 / 1 Introduction - extractive PDF cue:** We run experiments on state-of-the-art large VLMs which reveal notable performance gaps between state-of-the-art large VLMs and both human and rule-based baselines.
- **p. 3 / 1 Introduction - extractive PDF cue:** All models perform worse than human oracle and rule-based performance.
- **p. 3 / 1 Introduction - extractive PDF cue:** Next-Video [17]) on our benchmark against human and rule-based baselines.

## Design Rationale

- **p. 2 / 1 Introduction - extractive PDF cue:** In this paper, we introduce the Social Navigation Scene Understanding Benchmark (SOCIALNAVSUB), a novel Visual Question Answering (VQA) benchmark designed to evaluate VLMs on social ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Social Navigation VQA Benchmark for VLMs: We introduce the first VQA benchmark for assessing VLMs' capabilities in social robot navigation scenarios using 60 unique scenarios ...

## Source Evidence Cues

- **p. 2 / 1 Introduction - extractive PDF cue:** Moreover, studies such as SPACE [10] indicate that state-of-the-art large VLMs still lack robust spatial reasoning, raising questions about whether VLMs can understand scenes of ...
- **p. 1 / 1 Introduction - extractive PDF cue:** As shown in Figure 1, navigating through social navigation scenarios requires robots to interpret human intentions, adhere to social norms, and reason about spatial and ...
- **p. 2 / 1 Introduction - extractive PDF cue:** We run experiments on state-of-the-art large VLMs which reveal notable performance gaps between state-of-the-art large VLMs and both human and rule-based baselines.
- **p. 3 / 1 Introduction - extractive PDF cue:** All models perform worse than human oracle and rule-based performance.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | Moreover, studies such as SPACE [10] indicate that state-of-the-art large VLMs still lack robust spatial reasoning, raising questions about whether VLMs can ... | p. 2 (1 Introduction), p. 1 (1 Introduction) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | As shown in Figure 1, navigating through social navigation scenarios requires robots to interpret human intentions, adhere to social norms, and reason ... | p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | We run experiments on state-of-the-art large VLMs which reveal notable performance gaps between state-of-the-art large VLMs and both human and rule-based baselines. | p. 2 (1 Introduction), p. 3 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Moreover, studies, SPACE, indicate, state-of-the-art, large, VLMs, still, lack, robust, spatial, reasoning, raising, questions | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | Moreover, studies, SPACE, indicate, state-of-the-art, large, VLMs, still, lack, robust | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | introduce, Social, Navigation, Scene, Understanding, Benchmark, SOCIALNAVSUB, novel, Visual, Question | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | not recovered | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive PDF cue:** Moreover, studies such as SPACE [10] indicate that state-of-the-art large VLMs still lack robust spatial reasoning, raising questions about whether VLMs can understand scenes of ...
- **p. 1 / 1 Introduction - extractive PDF cue:** As shown in Figure 1, navigating through social navigation scenarios requires robots to interpret human intentions, adhere to social norms, and reason about spatial and ...
- **p. 2 / 1 Introduction - extractive PDF cue:** We run experiments on state-of-the-art large VLMs which reveal notable performance gaps between state-of-the-art large VLMs and both human and rule-based baselines.
- **p. 3 / 1 Introduction - extractive PDF cue:** Next-Video [17]) on our benchmark against human and rule-based baselines.
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | Using the robot odometry data from SCAND, we transform the relative human poses at future timesteps into global poses relative to the ... | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | SocialNav-SUB provides a unified framework for evaluating VLMs against human and rule-based baselines across VQA tasks requiring spatial, spatiotemporal, and social reasoning ... | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not recovered | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | 3.3 Diverse Scene Understanding Questions Following the aforementioned data processing pipeline, we construct a set of samples consisting of multi-view image sequences ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1 Introduction - extractive PDF cue:** Trained in diverse large-scale multimodal datasets that span various real-world scenarios, large VLMs often learn underlying patterns of human behavior that may implicitly encode an ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Moreover, studies, SPACE, indicate, state-of-the-art, large, VLMs, still, lack, robust, spatial, reasoning, raising, questions, about, whether, understand, scenes, complex, realistic.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | 7.1 Waypoint Selection Experiments To further demonstrate the practical value of SOCIALNAV-SUB in real-world social robot navigation, we conduct preliminary experiments examining ... | p. 14 (7 Appendix), p. 14 (7 Appendix) |
| Baseline harness | Figure 2: An overview of SOCIALNAV-SUB, which facilitates the systematic evaluation of VLMs in social robot navigation scenarios. Using SCAND data, human-labeled ... | p. 3 (Figure/Table caption), p. 14 (7 Appendix) |
| Metric / failure reporting | Overall, when scene context is extracted from the human oracle's responses, VLM performance significantly improves compared to using no context or randomly ... | p. 14 (7 Appendix), p. 23 (7 Appendix) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: Ablation experiment of querying strategies. The metric used is Probability of Agreement (PA). The baseline row BEV+CoT represents the performance with both CoT ...
- **p. 23 / 7 Appendix - extractive PDF cue:** Model Ablation Spatial Spatiotemporal Social Reasoning Reasoning Reasoning GPT-4o CoT+BEV 0.56 ± 0.01 0.51 ± 0.01 0.47 ± 0.01 No CoT 0.58 ± 0.01 0.53 ...
- **p. 14 / 7 Appendix - extractive PDF cue:** Having no context removes the middle portion of the text prompt that includes the context, and having random context randomizes each relational action for the ...
- **p. 23 / 7 Appendix - extractive PDF cue:** The results from removing BEV prompts indicate that there is not a significant effect across the capabilities for LLaVa-Next-Video and Gemini 2.0, but provides a ...
- **p. 24 / Figure/Table caption - extractive PDF cue:** Table 14: Gemini ablation experiments when using ground truth spatial and spatiotemporal answers for CoT reasoning. Our results indicate that better spatial reasoning and spatiotemporal ...
- **p. 20 / Figure/Table caption - extractive PDF cue:** Table 6: Qualitative descriptions of the text components for questions used in SOCIALNAV- SUB, their pertaining primary reasoning capability, and the number of unique questions ...
- **p. 7 / 4.3 Discussion - extractive PDF cue:** Overall, our evaluation reveals that while state-of-the-art large VLMs like OpenAI o4-mini and Gemini 2.0 show promising advances, they still fall short of human oracle ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), objective 본문 anchor 없음, temporal p. 5 (2 Related Work), p. 1 (Front matter), p. 5 (2 Related Work), p. 1 (Front matter), p. 2 (1 Introduction), p. 2 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
