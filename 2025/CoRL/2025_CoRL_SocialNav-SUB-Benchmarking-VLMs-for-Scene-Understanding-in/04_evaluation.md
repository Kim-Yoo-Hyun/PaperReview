# Evaluation - SocialNav-SUB: Benchmarking VLMs for Scene Understanding in Social Robot Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v305/munje25a.html; PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v305/main/assets/munje25a/munje25a.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 14 (7 Appendix), p. 23 (7 Appendix), p. 24 (7 Appendix), p. 15 (7 Appendix), p. 7 (Figure/Table caption), p. 14 (7 Appendix)): Overall, when scene context is extracted from the human oracle's responses, VLM performance significantly improves compared to using no context or randomly generated context, and also shows slight improvement over ...

## Evaluation Body Digest

- **p. 14 / 7 Appendix - extractive body cue:** 7.1 Waypoint Selection Experiments To further demonstrate the practical value of SOCIALNAV-SUB in real-world social robot navigation, we conduct preliminary experiments examining how scene understanding ...
- **p. 14 / 7 Appendix - extractive body cue:** Our SOCIALNAV-SUB benchmark provides the community with a valuable dataset and evaluation toolkit to support exploration along this direction.
- **p. 15 / 7 Appendix - extractive body cue:** These illustrate variation in environment type, crowd density, and human-robot proximity.
- **p. 19 / 7 Appendix - extractive body cue:** Overall 15.0% failure rate; higher at blind corners (17.3% vs 14.9%); failure cases show more people in scene (12.26 vs 11.91); Robot Action to Person: ...
- **p. 22 / 7 Appendix - extractive body cue:** These results highlight the deficiencies of non-reasoning VLMs: 1) Gemini [7] has stronger social reasoning than other non-reasoning VLMs for most questions but has worse ...
- **p. 15 / 7 Appendix - extractive body cue:** SOCIALNAV-SUB comprises 60 social robot navigation scenarios in total.
- **p. 18 / 7 Appendix - extractive body cue:** Bottom-left: GPT-4o correctly answers that person 5 is on the left, whereas both Gemini and LLaVa-Next-Video answer that person 5 is behind the robot.
- **p. 18 / 7 Appendix - extractive body cue:** Bottom-right: Most VLMs (but not all) predict that person 6 is being considered as the robot is moving towards the goal, similar to the distribution ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 7 Appendix | BENCHMARK / DATASET | Overall, when scene context is extracted from the human oracle's responses, VLM performance significantly improves compared to using no context or randomly generated context, ... | p. 14 (7 Appendix) |
| 7 Appendix | BENCHMARK / DATASET | The results indicate that removing the CoT component does not significantly affect spatial and spatiotemporal reasoning performance. | p. 23 (7 Appendix) |
| 7 Appendix | BENCHMARK / DATASET | These results indicate that a strong spatial and spatiotemporal reasoning capabilities can lead to significantly better performance on social reasoning questions. | p. 24 (7 Appendix) |
| 7 Appendix | BENCHMARK / DATASET | Estimates achieve an average displacement error of 0.67±0.14 m across all samples. | p. 15 (7 Appendix) |
| Figure/Table caption | BENCHMARK / DATASET | Table 1: Average Performance Across Question Categories. The metrics used are PA and CWPA for all questions and for each question category, along with ... | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 14 / 7 Appendix - extractive body cue:** 7.1 Waypoint Selection Experiments To further demonstrate the practical value of SOCIALNAV-SUB in real-world social robot navigation, we conduct preliminary experiments examining how scene understanding ...
- **p. 14 / 7 Appendix - extractive body cue:** Our SOCIALNAV-SUB benchmark provides the community with a valuable dataset and evaluation toolkit to support exploration along this direction.
- **p. 15 / 7 Appendix - extractive body cue:** These illustrate variation in environment type, crowd density, and human-robot proximity.
- **p. 19 / 7 Appendix - extractive body cue:** Overall 15.0% failure rate; higher at blind corners (17.3% vs 14.9%); failure cases show more people in scene (12.26 vs 11.91); Robot Action to Person: ...
- **p. 22 / 7 Appendix - extractive body cue:** These results highlight the deficiencies of non-reasoning VLMs: 1) Gemini [7] has stronger social reasoning than other non-reasoning VLMs for most questions but has worse ...
- **p. 15 / 7 Appendix - extractive body cue:** SOCIALNAV-SUB comprises 60 social robot navigation scenarios in total.
- **p. 18 / 7 Appendix - extractive body cue:** Bottom-left: GPT-4o correctly answers that person 5 is on the left, whereas both Gemini and LLaVa-Next-Video answer that person 5 is behind the robot.
- **p. 18 / 7 Appendix - extractive body cue:** Bottom-right: Most VLMs (but not all) predict that person 6 is being considered as the robot is moving towards the goal, similar to the distribution ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Examples of social robot navigation scenarios from SCAND [4]. The ability to de- termine socially compliant navigation actions requires understanding each dynamic scene ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: An overview of SOCIALNAV-SUB, which facilitates the systematic evaluation of VLMs in social robot navigation scenarios. Using SCAND data, human-labeled VQA datasets, and ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: The data processing pipeline for VQA prompts in SOCIALNAV-SUB. We first mine social robot navigation scenarios from SCAND [4], then use the PHALP ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Average Performance Across Question Categories. The metrics used are PA and CWPA for all questions and for each question category, along with standard ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Ablation experiment of querying strategies. The metric used is Probability of Agreement (PA). The baseline row BEV+CoT represents the performance with both CoT ...
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 4: An example of the waypoint selection VQA task. This particular example highlights using scene context from the human oracle. Having no context removes ...
- **p. 14 / Figure/Table caption - extractive body cue:** Table 3: Accuracy of various VLMs in selecting the same waypoint as the human operator under social scene contexts from different sources: a random generator, ...
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 5: Examples of scenes from SOCIALNAV-SUB. These illustrate variation in environment type, crowd density, and human-robot proximity. SOCIALNAV-SUB comprises 60 social robot navigation scenarios ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 7.1 Waypoint Selection Experiments To further demonstrate the practical value of SOCIALNAV-SUB in real-world social robot navigation, we conduct preliminary experiments examining how scene ... | embodiment, simulator version and control stack | p. 14 (7 Appendix), p. 14 (7 Appendix) |
| Task/environment | Our SOCIALNAV-SUB benchmark provides the community with a valuable dataset and evaluation toolkit to support exploration along this direction. | reset, timeout, object/scene variation | p. 14 (7 Appendix), p. 15 (7 Appendix) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 1 (1 Introduction) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 1 (Body text (section not recovered)), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The evaluation results are averaged over 5 runs, and we report mean accuracy ± standard error. | definition/direction/unit from same section | p. 14 (7 Appendix) |
| Table 1: Average Performance Across Question Categories. The metrics used are PA and CWPA for all questions and for each question category, along with ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Overall FR is the model's failure rate with standard error in smaller type. | definition/direction/unit from same section | p. 19 (7 Appendix) |
| We summarize quantitative findings shown in Tables 4 and 5 for VLM failure cases (defined as the model's chosen answer received zero human probability); ... | definition/direction/unit from same section | p. 19 (7 Appendix) |
| Candidate scenarios were ranked using a weighted linear score over features we hypothesized to correlate with 14 | definition/direction/unit from same section | p. 14 (7 Appendix) |
| Estimates achieve an average displacement error of 0.67±0.14 m across all samples. | definition/direction/unit from same section | p. 15 (7 Appendix) |
| Empirically we have observed errors are lower for well-observed pedestrians and larger under heavy occlusion. | definition/direction/unit from same section | p. 15 (7 Appendix) |
| Estimates are generally close ( < 1 m displacement error) to pseudo-ground truth for well-observed pedestrians; errors increase for heavily occluded subjects. in the ... | definition/direction/unit from same section | p. 16 (7 Appendix) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 2: An overview of SOCIALNAV-SUB, which facilitates the systematic evaluation of VLMs in social robot navigation scenarios. Using SCAND data, human-labeled VQA datasets, ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |
| Overall, when scene context is extracted from the human oracle's responses, VLM performance significantly improves compared to using no context or randomly generated context, ... | comparison identity and matched condition | p. 14 (7 Appendix) |
| For the Human Oracle and Average Human baselines, these results highlight questions that humans disagreed on more often, showing that determining spatial labels for ... | comparison identity and matched condition | p. 23 (7 Appendix) |
| Table 2: Ablation experiment of querying strategies. The metric used is Probability of Agreement (PA). The baseline row BEV+CoT represents the performance with both ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| This particular example highlights using scene context from the human oracle. | comparison identity and matched condition | p. 14 (7 Appendix) |
| Question Type Options The robot is (Select all that apply) Multiple Select moving ahead; turning left; turning right At the end, {PERSON} ends up ... | comparison identity and matched condition | p. 21 (7 Appendix) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 2: Ablation experiment of querying strategies. The metric used is Probability of Agreement (PA). The baseline row BEV+CoT represents the performance with both ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Model Ablation Spatial Spatiotemporal Social Reasoning Reasoning Reasoning GPT-4o CoT+BEV 0.56 ± 0.01 0.51 ± 0.01 0.47 ± 0.01 No CoT 0.58 ± 0.01 ... | component/input/data sensitivity | p. 23 (7 Appendix) |
| Having no context removes the middle portion of the text prompt that includes the context, and having random context randomizes each relational action for ... | component/input/data sensitivity | p. 14 (7 Appendix) |
| The results from removing BEV prompts indicate that there is not a significant effect across the capabilities for LLaVa-Next-Video and Gemini 2.0, but provides ... | component/input/data sensitivity | p. 23 (7 Appendix) |
| Table 14: Gemini ablation experiments when using ground truth spatial and spatiotemporal answers for CoT reasoning. Our results indicate that better spatial reasoning and ... | component/input/data sensitivity | p. 24 (Figure/Table caption) |
| Table 6: Qualitative descriptions of the text components for questions used in SOCIALNAV- SUB, their pertaining primary reasoning capability, and the number of unique ... | component/input/data sensitivity | p. 20 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we introduce the Social Navigation Scene Understanding Benchmark (SOCIALNAVSUB), a novel Visual Question Answering (VQA) benchmark designed to evaluate VLMs on ... | Overall, when scene context is extracted from the human oracle's responses, VLM performance significantly improves compared to using no context or randomly generated context, ... | PDF body cue; verify exact table/figure and matched conditions | p. 14 (7 Appendix), p. 23 (7 Appendix), p. 24 (7 Appendix), p. 15 (7 Appendix), p. 7 (Figure/Table caption), p. 14 (7 Appendix) |
| Primary metric/result | The results indicate that removing the CoT component does not significantly affect spatial and spatiotemporal reasoning performance. | numeric claim only at cited anchor | p. 23 (7 Appendix) |

- Numeric sentences retained from the body:
- **p. 15 / 7 Appendix - extractive body cue:** Estimates achieve an average displacement error of 0.67±0.14 m across all samples.
- **p. 20 / 7 Appendix - extractive body cue:** 399 Robot Action to Person: The high-level relational action of the robot with respect to the person (e.g., the robot avoided person 2).
- **p. 20 / 7 Appendix - extractive body cue:** 399 Robot Affected by Person at End: Whether the robot's (human operator's) actions are affected by the person at the end of the video.
- **p. 20 / 7 Appendix - extractive body cue:** 399 Robot Action to Person at End: The high-level relational action of the robot with respect to the person at the end of the video.
- **p. 23 / 7 Appendix - extractive body cue:** Model Ablation Spatial Spatiotemporal Social Reasoning Reasoning Reasoning GPT-4o CoT+BEV 0.56 ± 0.01 0.51 ± 0.01 0.47 ± 0.01 No CoT 0.58 ± 0.01 0.53 ...
- **p. 24 / 7 Appendix - extractive body cue:** Question Name CoT CoT with Ground-Truth Spatial(Temporal) Reasoning PA CW PA PA CW PA Robot Affected by Person 0.64 ± 0.02 0.78 ± 0.02 0.78 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Overall, our evaluation reveals that while state-of-the-art large VLMs like OpenAI o4-mini and Gemini 2.0 show promising advances, they still fall short of human ... | p. 7 (4.3 Discussion) |
| body limitation/failure cue | 7.6 Failure Case Analysis As mentioned in Section 4.2, we found cases of VLMs in the experiment failing on questions with high human consensus ... | p. 17 (7 Appendix) |
| body limitation/failure cue | Figure 9: Examples of failure cases for VLMs. Top-left: Failing to recognize that person 5 is on the left. Top-right: Failing to recognize that ... | p. 18 (Figure/Table caption) |
| body limitation/failure cue | Overall FR is the model's failure rate with standard error in smaller type. | p. 19 (7 Appendix) |
| body limitation/failure cue | Overall 33.8% failure rate; very limited Robot Action to Person diversity-only avoiding (53.1%) and not considering (6.38%). | p. 19 (7 Appendix) |
| body limitation/failure cue | Since SCAND does not provide 3D human pose labels, we validated this pipeline and tuned the hyperparameters on the CODa dataset [41], which provides ... | p. 15 (7 Appendix) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Munje1∗, Chen Tang1, Shuijing Liu1, Zichao Hu1, Yifeng Zhu1, Jiaxun Cui1, Garrett Warnell1,2, Joydeep Biswas1, Peter Stone1,3 1Department of Computer Science, The University of ... | p. 1 (Body text (section not recovered)) |
| We run experiments on state-of-the-art large VLMs which reveal notable performance gaps between state-of-the-art large VLMs and both human and rule-based baselines. | p. 2 (1 Introduction) |
| Trained in diverse large-scale multimodal datasets that span various real-world scenarios, large VLMs often learn underlying patterns of human behavior that may implicitly encode ... | p. 2 (1 Introduction) |
| The resulting hyperparameters are then used in the SOCIALNAV-SUB pipeline. | p. 15 (7 Appendix) |
| We computed a weighted sum of these features and selected top-scoring scenes. | p. 15 (7 Appendix) |
| The "Person Goal Obstruction" question may provide sufficient information for the VLM to easily answer the "Robot Affected By Person" question, to which we ... | p. 24 (7 Appendix) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4.3 Discussion - extractive body cue:** Overall, our evaluation reveals that while state-of-the-art large VLMs like OpenAI o4-mini and Gemini 2.0 show promising advances, they still fall short of human oracle ...
- **p. 17 / 7 Appendix - extractive body cue:** 7.6 Failure Case Analysis As mentioned in Section 4.2, we found cases of VLMs in the experiment failing on questions with high human consensus in ...
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 9: Examples of failure cases for VLMs. Top-left: Failing to recognize that person 5 is on the left. Top-right: Failing to recognize that person ...
- **p. 19 / 7 Appendix - extractive body cue:** Overall FR is the model's failure rate with standard error in smaller type.
- **p. 19 / 7 Appendix - extractive body cue:** Overall 33.8% failure rate; very limited Robot Action to Person diversity-only avoiding (53.1%) and not considering (6.38%).
- **p. 15 / 7 Appendix - extractive body cue:** Since SCAND does not provide 3D human pose labels, we validated this pipeline and tuned the hyperparameters on the CODa dataset [41], which provides high-quality ...

- **Evidence anchors reviewed:** datasets p. 14 (7 Appendix), p. 14 (7 Appendix), p. 15 (7 Appendix), p. 19 (7 Appendix), p. 22 (7 Appendix), p. 15 (7 Appendix), metrics p. 14 (7 Appendix), p. 7 (Figure/Table caption), p. 19 (7 Appendix), p. 19 (7 Appendix), p. 14 (7 Appendix), p. 15 (7 Appendix), baselines p. 3 (Figure/Table caption), p. 14 (7 Appendix), p. 23 (7 Appendix), p. 8 (Figure/Table caption), p. 14 (7 Appendix), p. 21 (7 Appendix), results p. 14 (7 Appendix), p. 23 (7 Appendix), p. 24 (7 Appendix), p. 15 (7 Appendix), p. 7 (Figure/Table caption), p. 14 (7 Appendix).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
