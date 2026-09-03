# Insights — Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=lNVHg9npif; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/165445. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** We show that our framework enables a robot to process much more complex prompts than prior end-to-end instruction following systems and incorporate feedback during task ...
- **p. 2 / 1. Introduction - extractive body cue:** The main contribution of our paper is a hierarchical interactive robot learning system (Hi Robot), a novel framework that uses VLMs for both high-level reasoning ...
- **p. 5 / 5.1. Tasks and Baseline Methods - extractive body cue:** The training data consists of full table cleaning episodes.
- **p. 7 / 5.1. Tasks and Baseline Methods - extractive body cue:** Hi Robot without synthetic data: This ablation corresponds to our method without synthetic training data, evaluating the importance of including diverse syntheticallygenerated prompts in training.
- **p. 4 / 3. Preliminaries and Problem Statement - extractive body cue:** The policy consists of a high-level and a low-level policy.
- **p. 5 / 4.3. Data Collection and Training Hi Robot - extractive body cue:** To train the low-level policy plo(At/I1 t, ..., In t , ˆℓt, qt), we use Dlabeled ∪Ddemo using a flow-matching objective, following Black et al.
- **p. 6 / 5.1. Tasks and Baseline Methods - extractive body cue:** This requires the high-level model to reason about the task and each object (e.g., recognizing that reusable plastic cups are dishes, while paper cups are ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (5.1. Tasks and Baseline Methods), p. 7 (5.1. Tasks and Baseline Methods), p. 4 (3. Preliminaries and Problem Statement), p. 5 (4.3. Data Collection and Training Hi Robot)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** This challenge resembles the distinction between Kahneman's "System 1" and "System 2" cognitive processes (Kahneman, 2011).
- **p. 1 / 1. Introduction - extractive body cue:** For instance, consider a robot tasked with tidying up a table after a meal: instead of rigidly following a single predefined set of steps, the ...
- **p. 2 / 1. Introduction - extractive body cue:** This low-level policy is itself a vision-language model finetuned for producing robotic actions, also known as a visionlanguage-action (VLA) model (Black et al., 2024; Brohan ...
- **p. 3 / 3. Preliminaries and Problem Statement - extractive body cue:** A particularly powerful approach for handling such complex semantics is provided by visionlanguage-action (VLA) models (Black et al., 2024; Brohan et al., 2023a; Kim et ...
- **p. 4 / 3. Preliminaries and Problem Statement - extractive body cue:** We build on the π0 VLA (Black et al., 2024), which additionally handles multiple images and continuous state observations qt, and modifies the VLM to ...
- **p. 9 / 6. Discussion and Future Work - extractive body cue:** Our system also has a number of limitations that could be studied in future work.
- **p. 8 / 5.3. Core Results - extractive body cue:** With human high-level instructions, the lowlevel policy executes nearly flawlessly, showing that failures stem more from reasoning than actuation.
- **Boundary to test:** Our system also has a number of limitations that could be studied in future work.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We show that our framework enables a robot to process much more complex prompts than prior end-to-end instruction following systems and incorporate feedback during task execution (Figure 1). | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Figure 5: Comparisons to Prior Methods. Hi Robot outperforms GPT-4o and flat VLA on Table Bussing, Sandwich Making, and Grocery Shopping. Hi Robot averages over 40% higher instruction accuracy than GPT-4o, showing ... | p. 7 (Figure/Table caption), p. 9 (Figure/Table caption) |
| Failure/limitation | Our system also has a number of limitations that could be studied in future work. | p. 9 (6. Discussion and Future Work), p. 8 (5.3. Core Results) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 To this end, we provide a state-of-the-art vision-language model with a robot observation and target atomic command, and ask it to come up with a prompt or human interaction that may have ...를 We build on the π0 VLA (Black et al., 2024), which additionally handles multiple images and continuous state observations qt, and modifies the VLM to output continuous action chunk distributions via flow-matching, ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Our system also has a number of limitations that could be studied in future work.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We show that our framework enables a robot to process much more complex prompts than prior end-to-end instruction following systems and incorporate feedback during task execution (Figure 1).
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model, Robotics`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Our system also has a number of limitations that could be studied in future work.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Task progress quantifies how closely the robot matches the intended goal and is computed by the proportion of objects that are successfully placed in their correct locations or configurations..
3. Compare against the body-reported baseline or a matched simpler baseline: Across all tasks, Hi Robot exhibits substantially higher Instruction Accuracy and Task Progress, compared to GPT4o and the flat baseline..
4. Report the body metric and its denominator/aggregation: This score measures how well the high-level policy's predicted instruction aligns with human intent, requiring multi-modal understanding of the current environment and prompt..
5. Re-run the body-reported ablation/failure condition: Figure 8: Hierarchical policy vs. flat policy. The hierarchical approach outperforms the flat variant trained on the same data, as it effectively integrates user feedback and partial instructions, whereas the flat model ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (5.1. Tasks and Baseline Methods), p. 7 (5.1. Tasks and Baseline Methods), p. 5 (4.3. Data Collection and Training Hi Robot); the primary result is directionally consistent at p. 7 (Figure/Table caption), p. 9 (Figure/Table caption), p. 7 (5.2. Metrics and Evaluation Protocol); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 framework, enables, robot mechanism이 Across all tasks, Hi Robot exhibits substantially higher Instruction Accuracy and Task Progress, compared to GPT4o ... 대비 This score measures how well the high-level policy's predicted instruction aligns with human intent, requiring multi-modal understanding of ...을 개선하고, Our system also has a number of limitations that could be studied in future work. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
