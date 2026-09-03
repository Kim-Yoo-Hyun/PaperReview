# Insights — VLM See, Robot Do: Human Demo Video to Robot Action Plan via Vision Language Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2410.08792; PDF retrieval source: https://arxiv.org/pdf/2410.08792. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, the contributions of this work are as follows: • We introduce SeeDo, a VLM-based agent that integrates keyframe selection, visual prompting, and VLM ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Inspired by this capability, we propose SeeDo, a modularized agent centered around a VLM.
- **p. 3 / III. METHOD - extractive body cue:** To alleviate these issues, we introduce a visual prompting module in SeeDo that enhances the visual capabilities of the VLM.
- **p. 1 / I. INTRODUCTION - extractive body cue:** First, VLMs' rich commonsense knowledge enables them to understand objects and their relationships, helping robots understand the task goals despite the embodiment gap.
- **p. 3 / III. METHOD - extractive body cue:** The module first instructs the VLM to identify objects in the frames and then use an open-vocabulary object detector [53] to extract object bounding boxes ...
- **p. 4 / III. METHOD - extractive body cue:** In real-world experiment, we follow [1, 20] and first use a segmentation model to segment all objects of interest in the RGB images, then query ...
- **p. 3 / III. METHOD - extractive body cue:** The speed valleys are identified as keyframes. b) The Visual Prompting module detects and tracks objects and then applies the tracking results as visual prompts ...
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 3 (III. METHOD), p. 4 (III. METHOD)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** However, significant challenges remain in teaching robots to learn from human videos due to the substantial domain gap between robots and humans.
- **p. 1 / I. INTRODUCTION - extractive body cue:** To mitigate these limitations, SeeDo integrates not only with a VLM interpreter module but also with a ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Additionally, we identify three types of errors from the failure cases to analyze and provide insights on the strengths and weaknesses of various models on ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** However, spatial errors remain the main source of SeeDo 's failures.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Model Success Rate Failure Reason TSR↑ FSR↑ SSR↑ Vision↓ Spatial↓ Temporal↓ SeeDo w/o V.P.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Error type percentages of all the failure cases of all the methods. Note that error types are not exclusive. The barplot of the ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** These tasks represent some common robotics scenarios that feature a clear temporal sequence and dynamic interactions that cannot be adequately captured with still images or ...
- **Boundary to test:** Additionally, we identify three types of errors from the failure cases to analyze and provide insights on the strengths and weaknesses of various models on our tasks: • Vision Error occurs when ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, the contributions of this work are as follows: • We introduce SeeDo, a VLM-based agent that integrates keyframe selection, visual prompting, and VLM interpreter modules to interpret long-horizon human demonstration ... | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Reported outcome | To achieve success (TSR=1), each step in the plan must match the demo's action sequence in both content and temporal order. • FSR is equivalent to the conventional SR in that it ... | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Failure/limitation | Additionally, we identify three types of errors from the failure cases to analyze and provide insights on the strengths and weaknesses of various models on our tasks: • Vision Error occurs when ... | p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 Some employ pretrained VLMs for further fine-tuning to learn the mapping from visual inputs and language instructions to actions [5, 6], or leverage the general knowledge of VLMs to identify salient objects ...를 In summary, the contributions of this work are as follows: • We introduce SeeDo, a VLM-based agent that integrates keyframe selection, visual prompting, and VLM interpreter modules to interpret long-horizon human demonstration ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Additionally, we identify three types of errors from the failure cases to analyze and provide insights on the strengths and weaknesses of various models on our tasks: • Vision Error occurs when ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary, the contributions of this work are as follows: • We introduce SeeDo, a VLM-based agent that integrates keyframe selection, visual prompting, and VLM interpreter modules to interpret long-horizon human demonstration ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `Vision-Language Model, Robotics`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Additionally, we identify three types of errors from the failure cases to analyze and provide insights on the strengths and weaknesses of various models on our tasks: • Vision Error occurs when ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: These tasks represent some common robotics scenarios that feature a clear temporal sequence and dynamic interactions that cannot be adequately captured with still images or brief descriptions..
3. Compare against the body-reported baseline or a matched simpler baseline: SeeDo outperforms all closed-source and open-source video VLM baselines across TSR, FSR, and SSR..
4. Report the body metric and its denominator/aggregation: Fig. 5: Error type percentages of all the failure cases of all the methods. Note that error types are not exclusive. The barplot of the total success rates on all tasks is ....
5. Re-run the body-reported ablation/failure condition: Since SeeDo utilizes GPT-4o as its VLM, we further test three variants of GPT-4o using different frame sampling strategies while keeping the same prompts: • GPT-4o Init+Final: Uses only the first and ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD); the primary result is directionally consistent at p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, contributions, follows mechanism이 SeeDo outperforms all closed-source and open-source video VLM baselines across TSR, FSR, and SSR. 대비 Fig. 5: Error type percentages of all the failure cases of all the methods. Note that error types ...을 개선하고, Additionally, we identify three types of errors from the failure cases to analyze and provide insights ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
