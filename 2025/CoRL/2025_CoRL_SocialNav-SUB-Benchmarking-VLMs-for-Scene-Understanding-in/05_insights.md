# Insights — SocialNav-SUB: Benchmarking VLMs for Scene Understanding in Social Robot Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v305/munje25a.html; PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v305/main/assets/munje25a/munje25a.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we introduce the Social Navigation Scene Understanding Benchmark (SOCIALNAVSUB), a novel Visual Question Answering (VQA) benchmark designed to evaluate VLMs on social ...
- **p. 2 / 1 Introduction - extractive body cue:** Social Navigation VQA Benchmark for VLMs: We introduce the first VQA benchmark for assessing VLMs' capabilities in social robot navigation scenarios using 60 unique scenarios ...
- **p. 2 / 1 Introduction - extractive body cue:** Moreover, studies such as SPACE [10] indicate that state-of-the-art large VLMs still lack robust spatial reasoning, raising questions about whether VLMs can understand scenes of ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** Our benchmark sets the stage for further research on foundation models for social robot navigation, offering a framework to explore how VLMs can be tailored ...
- **p. 1 / 1 Introduction - extractive body cue:** As shown in Figure 1, navigating through social navigation scenarios requires robots to interpret human intentions, adhere to social norms, and reason about spatial and ...
- **p. 2 / 1 Introduction - extractive body cue:** We run experiments on state-of-the-art large VLMs which reveal notable performance gaps between state-of-the-art large VLMs and both human and rule-based baselines.
- **p. 3 / 1 Introduction - extractive body cue:** All models perform worse than human oracle and rule-based performance.
- **Contribution anchor:** p. 2 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Body text (section not recovered)), p. 1 (1 Introduction), p. 2 (1 Introduction)

### Strongest assumption and failure boundary

- **p. 2 / 1 Introduction - extractive body cue:** By bridging the gap between VLM capabilities and the challenges of social robot navigation, our work provides a foundation for advancing the use of VLMs ...
- **p. 2 / 1 Introduction - extractive body cue:** Existing evaluations have offered only partial assessments [9, 10], often focusing on controlled settings or lacking temporal components, leading to an incomplete picture of how ...
- **p. 7 / 4.3 Discussion - extractive body cue:** Overall, our evaluation reveals that while state-of-the-art large VLMs like OpenAI o4-mini and Gemini 2.0 show promising advances, they still fall short of human oracle ...
- **p. 17 / 7 Appendix - extractive body cue:** 7.6 Failure Case Analysis As mentioned in Section 4.2, we found cases of VLMs in the experiment failing on questions with high human consensus in ...
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 9: Examples of failure cases for VLMs. Top-left: Failing to recognize that person 5 is on the left. Top-right: Failing to recognize that person ...
- **p. 19 / 7 Appendix - extractive body cue:** Overall FR is the model's failure rate with standard error in smaller type.
- **p. 19 / 7 Appendix - extractive body cue:** Overall 33.8% failure rate; very limited Robot Action to Person diversity-only avoiding (53.1%) and not considering (6.38%).
- **Boundary to test:** Overall, our evaluation reveals that while state-of-the-art large VLMs like OpenAI o4-mini and Gemini 2.0 show promising advances, they still fall short of human oracle and rule-based performance across key reasoning tasks.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this paper, we introduce the Social Navigation Scene Understanding Benchmark (SOCIALNAVSUB), a novel Visual Question Answering (VQA) benchmark designed to evaluate VLMs on social robot navigation tasks. | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Reported outcome | Overall, when scene context is extracted from the human oracle's responses, VLM performance significantly improves compared to using no context or randomly generated context, and also shows slight improvement over using scene ... | p. 14 (7 Appendix), p. 23 (7 Appendix) |
| Failure/limitation | Overall, our evaluation reveals that while state-of-the-art large VLMs like OpenAI o4-mini and Gemini 2.0 show promising advances, they still fall short of human oracle and rule-based performance across key reasoning tasks. | p. 7 (4.3 Discussion), p. 17 (7 Appendix) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `standardized observation, action, task state와 evaluation split → benchmark state/goal와 method decision → policy/controller trajectory 또는 measured result`.
- 이 논문의 재사용 가능한 지점은 Moreover, studies such as SPACE [10] indicate that state-of-the-art large VLMs still lack robust spatial reasoning, raising questions about whether VLMs can understand scenes of complex, realistic social navigation scenarios at all ...를 As shown in Figure 1, navigating through social navigation scenarios requires robots to interpret human intentions, adhere to social norms, and reason about spatial and temporal interactions to respond to dynamic environments.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 benchmark state/goal와 method decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Overall, our evaluation reveals that while state-of-the-art large VLMs like OpenAI o4-mini and Gemini 2.0 show promising advances, they still fall short of human oracle and rule-based performance across key reasoning tasks.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this paper, we introduce the Social Navigation Scene Understanding Benchmark (SOCIALNAVSUB), a novel Visual Question Answering (VQA) benchmark designed to evaluate VLMs on social robot navigation tasks.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `VLM, Navigation, Benchmark`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Overall, our evaluation reveals that while state-of-the-art large VLMs like OpenAI o4-mini and Gemini 2.0 show promising advances, they still fall short of human oracle and rule-based performance across key reasoning tasks.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: 7.1 Waypoint Selection Experiments To further demonstrate the practical value of SOCIALNAV-SUB in real-world social robot navigation, we conduct preliminary experiments examining how scene understanding influences VLMs' performance in w ....
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 2: An overview of SOCIALNAV-SUB, which facilitates the systematic evaluation of VLMs in social robot navigation scenarios. Using SCAND data, human-labeled VQA datasets, and var- ious VLMs, this framework offers the ....
4. Report the body metric and its denominator/aggregation: The evaluation results are averaged over 5 runs, and we report mean accuracy ± standard error..
5. Re-run the body-reported ablation/failure condition: Table 2: Ablation experiment of querying strategies. The metric used is Probability of Agreement (PA). The baseline row BEV+CoT represents the performance with both CoT and BEV prompts enabled. The subsequent rows ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (1 Introduction), p. 1 (Body text (section not recovered)), p. 1 (1 Introduction); the primary result is directionally consistent at p. 14 (7 Appendix), p. 23 (7 Appendix), p. 24 (7 Appendix); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 introduce, Social, Navigation mechanism이 Figure 2: An overview of SOCIALNAV-SUB, which facilitates the systematic evaluation of VLMs in social robot ... 대비 The evaluation results are averaged over 5 runs, and we report mean accuracy ± standard error.을 개선하고, Overall, our evaluation reveals that while state-of-the-art large VLMs like OpenAI o4-mini and Gemini 2.0 show ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
