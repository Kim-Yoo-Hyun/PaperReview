# Insights — Fast-in-Slow: A Dual-System VLA Model Unifying Fast Manipulation within Slow Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (35 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=4asFznbzJg; PDF retrieval source: https://papers.nips.cc/paper_files/paper/2025/file/8cf3760422b9d4505589a97c8f9569e7-Paper-Conference.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: • We propose Fast-in-Slow (FiS), a unified dual-system VLA model that embeds System 1 execution within a pretrained ...
- **p. 2 / 1 Introduction - extractive body cue:** To jointly optimize the reasoning and execution components in FiS-VLA, we introduce a dualaware co-training strategy.
- **p. 2 / 1 Introduction - extractive body cue:** Considering these limitations, and motivated by the functional abstraction of Kahneman's dual-system theory, we raise a question: "If a VLM model serves as the central ...
- **p. 1 / Abstract - extractive body cue:** In this work, we propose Fast-in-Slow (FiS), a unified dual-system vision-language-action (VLA) model that embeds the System 1 execution module within the VLM-based System 2 ...
- **p. 1 / Abstract - extractive body cue:** This innovative paradigm not only enables high-frequency execution in System 1, but also facilitates coordination between multimodal reasoning and execution components within a single foundation ...
- **p. 2 / 1 Introduction - extractive body cue:** Block 1 Block 2 Block 3 LLM Lowfrequency Highfrequency Block n-1 Block 1 Block 2 LLM Block n Lowfrequency Highfrequency Separate Policy Model Feature Action ...
- **p. 1 / Abstract - extractive body cue:** To enable coordination between the two systems, a dual-aware co-training strategy is proposed that equips System 1 with action generation capabilities while preserving System 2's ...
- **Contribution anchor:** p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** Simultaneously, enabling robots to execute a broad spectrum of tasks while adapting to variations in objects and environments remains the core challenge.
- **p. 2 / 1 Introduction - extractive body cue:** While these methods improve execution efficiency, their System 1, as a lightweight separate model, lacks internetscale pretrained knowledge and depends solely on feature representations extracted ...
- **p. 2 / 1 Introduction - extractive body cue:** Considering these limitations, and motivated by the functional abstraction of Kahneman's dual-system theory, we raise a question: "If a VLM model serves as the central ...
- **p. 1 / 1 Introduction - extractive body cue:** Recently, some works [7, 8, 9, 10, 11, 12] have sought to leverage the pretrained knowledge of foundational vision-language-models (VLMs) [13, 14, 15, 16, 17, ...
- **p. 9 / 4 Experiments - extractive body cue:** Additional visualizations and failure cases are provided in Appendix C and D, respectively.
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 5: Visualization of generalization setting with key differences highlighted using red box. importance of the heterogeneous modality input design in FiS-VLA's dual systems, which ...
- **p. 34 / Figure/Table caption - extractive body cue:** Figure 11: AlphaBot task execution visualization. We visualize key frames of the agent's execution process from a static exterior view. D Failure Case Analysis. Through ...
- **Boundary to test:** Additional visualizations and failure cases are provided in Appendix C and D, respectively.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, our contributions are as follows: • We propose Fast-in-Slow (FiS), a unified dual-system VLA model that embeds System 1 execution within a pretrained VLM while preserving its inherent System 2 ... | p. 3 (1 Introduction), p. 2 (1 Introduction) |
| Reported outcome | Figure 4: Visualization of real-world experiments with Agilex and AlphaBot dual-arm robots. Quantitative and qualitative results. As shown in Table 2, FiS-VLA consistently outperforms the baseline π0 across eight real-world tasks. On ... | p. 9 (Figure/Table caption), p. 8 (4 Experiments) |
| Failure/limitation | Additional visualizations and failure cases are provided in Appendix C and D, respectively. | p. 9 (4 Experiments), p. 10 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 Block 1 Block 2 Block 3 LLM Lowfrequency Highfrequency Block n-1 Block 1 Block 2 LLM Block n Lowfrequency Highfrequency Separate Policy Model Feature Action (a) Previous Dual-system VLA (b) Fast-in-Slow Dual-system ...를 Most recent end-to-end approaches [22, 23, 24] leverage VLM as System 2 for high-level feature extraction, while appending an additional policy head as System 1 to transform VLM outputs into executable action ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Additional visualizations and failure cases are provided in Appendix C and D, respectively.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary, our contributions are as follows: • We propose Fast-in-Slow (FiS), a unified dual-system VLA model that embeds System 1 execution within a pretrained VLM while preserving its inherent System 2 ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model, Robotics`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Additional visualizations and failure cases are provided in Appendix C and D, respectively.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Models Agilex Dual-Arm Robot Task AlphaBot Dual-Arm Robot Task Pick Lift ball Place bottles Wipe Mean Pick bowl and Handover Pour water Fold towel Mean and place and place at rack blackboard ....
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 4: Visualization of real-world experiments with Agilex and AlphaBot dual-arm robots. Quantitative and qualitative results. As shown in Table 2, FiS-VLA consistently outperforms the baseline π0 across eight real-world tasks. On ....
4. Report the body metric and its denominator/aggregation: Following [22, 5], we evaluate all methods using 20 rollouts from the latest epoch checkpoint, repeating the evaluation three times for each task and reporting the average success rate along with the ....
5. Re-run the body-reported ablation/failure condition: Figure 7: Ablation studies on action chunk size and input variants of FiS-VLA. (Left) Impact of different action chunk sizes on success rate and inference speed. While increasing action chunk size leads ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction); the primary result is directionally consistent at p. 9 (Figure/Table caption), p. 8 (4 Experiments), p. 29 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, contributions, follows mechanism이 Figure 4: Visualization of real-world experiments with Agilex and AlphaBot dual-arm robots. Quantitative and qualitative results. ... 대비 Following [22, 5], we evaluate all methods using 20 rollouts from the latest epoch checkpoint, repeating the evaluation ...을 개선하고, Additional visualizations and failure cases are provided in Appendix C and D, respectively. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
