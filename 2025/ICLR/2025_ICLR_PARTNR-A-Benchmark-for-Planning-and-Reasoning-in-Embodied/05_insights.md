# Insights — PARTNR: A Benchmark for Planning and Reasoning in Embodied Multi-agent Tasks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (64 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=T5QLRRHyL1; PDF retrieval source: https://openreview.net/pdf/4bb6ff694eaca45e88773722cf73178602665bfd.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1 INTRODUCTION - extractive body cue:** To bridge this gap, we introduce Planning And Reasoning Tasks in humaN-Robot collaboration (PARTNR), a novel benchmark that evaluates the ability of embodied AI agents ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Instead, we propose a semi-automated approach using 1
- **p. 2 / 1 INTRODUCTION - extractive body cue:** LLM-based helper agents LLM Planner We propose modular LLM-based agent baselines to collaborate in our benchmark.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** As PARTNR consists of natural language tasks and LLMs have shown strong results in planning (Yao et al., 2023; Ahn et al., 2022; Huang et ...
- **p. 34 / A.9.2 IMPLEMENTATION DETAILS - extractive body cue:** We train the model to predict, for every example, the action taken by the agent, which corresponds to the text after the </reserved_special_token_0>/ token.
- **p. 31 / A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS - extractive body cue:** The finetuned model based on Llama-3.1-8B required an average of 0.53s per planning step.
- **p. 31 / A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS - extractive body cue:** For all experiments, LLM inferrence is performed on two Nvidia A100 GPUs using the gpt-fast inference engine PyTorch (2023).
- **Contribution anchor:** p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 34 (A.9.2 IMPLEMENTATION DETAILS), p. 31 (A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS)

### Strongest assumption and failure boundary

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Through systematic evaluation, we reveal critical insights into the current limitations of LLM-based planners, opening interesting future research directions.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Curating such a benchmark of large-scale, natural language tasks with tailored evaluation functions presents significant challenges.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Despite significant progress in the field of embodied AI, there remains a gap in realistic benchmarks that evaluate robots in collaborative settings.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** LLMs also struggle to recover from skill failures and perception grounding errors, resulting in lower performance when privileged skills and privileged perception are removed.
- **p. 24 / Figure/Table caption - extractive body cue:** Table 8: Top three failure modes of 100k-scale task and evaluation generation reported for each task type. Failures of task generation are led by the ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Analysis of planner baselines in various settings. We compare performance using simula- tion steps, success rate and percent complete on the tasks, and ...
- **p. 10 / 5 CONCLUSION - extractive body cue:** PARTNR serves as a challenging benchmark that highlights the substantial limitations of current models.
- **Boundary to test:** Table 8: Top three failure modes of 100k-scale task and evaluation generation reported for each task type. Failures of task generation are led by the hallucination of non-existent entities, while failures of ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To bridge this gap, we introduce Planning And Reasoning Tasks in humaN-Robot collaboration (PARTNR), a novel benchmark that evaluates the ability of embodied AI agents to collaborate with humans across a range ... | p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Reported outcome | Table 3: Human-in-the-Loop Evaluation. We evaluate the performance of a 2-person human team and human-LLM teams, comparing them to solo human performance on PARTNR tasks using metrics described in Section 4.1. Additional ... | p. 10 (Figure/Table caption), p. 35 (Figure/Table caption) |
| Failure/limitation | Table 8: Top three failure modes of 100k-scale task and evaluation generation reported for each task type. Failures of task generation are led by the hallucination of non-existent entities, while failures of ... | p. 24 (Figure/Table caption), p. 9 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `standardized observation, action, task state와 evaluation split → benchmark state/goal와 method decision → policy/controller trajectory 또는 measured result`.
- 이 논문의 재사용 가능한 지점은 PARTNR consists of 100,000 natural language instructions paired with tailored evaluation functions, focusing on four task types: (1) constraint-free, where sub-tasks can be completed in any manner by either agent, (2) spatial ...를 Beyond the conventional challenges of long-horizon planning, partially observed environments, and large state and action spaces, PARTNR emphasizes the need for effective collaboration.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 benchmark state/goal와 method decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Table 8: Top three failure modes of 100k-scale task and evaluation generation reported for each task type. Failures of task generation are led by the hallucination of non-existent entities, while failures of ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To bridge this gap, we introduce Planning And Reasoning Tasks in humaN-Robot collaboration (PARTNR), a novel benchmark that evaluates the ability of embodied AI agents to collaborate with humans across a range ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Planning and control`; tags: `Robotics, Benchmark`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Table 8: Top three failure modes of 100k-scale task and evaluation generation reported for each task type. Failures of task generation are led by the hallucination of non-existent entities, while failures of ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Released data includes extensions of the Habitat Synthetic Scenes Dataset (HSSD) (Khanna et al., 2024), generated benchmark task episodes, and model weights for our trained neural network skills and fine-tuned large planning ....
3. Compare against the body-reported baseline or a matched simpler baseline: Released code includes our PARTNR benchmark tasks, metrics, baseline oracle skills, large planning model framework, and dataset generation utilities..
4. Report the body metric and its denominator/aggregation: Table 11: Baseline results on PARTNR test set. We measure performance using simulation steps required to finish the episode, success rate and completion rate on the tasks, and the average number of ....
5. Re-run the body-reported ablation/failure condition: Figure 1: We present PARTNR, a benchmark for planning and reasoning in embodied multi-agent tasks, featuring 100,000 everyday tasks and evaluation functions generated semi-automatically, spanning 60 houses and 5,819 unique objects. We ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 34 (A.9.2 IMPLEMENTATION DETAILS), p. 31 (A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS), p. 31 (A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS); the primary result is directionally consistent at p. 10 (Figure/Table caption), p. 35 (Figure/Table caption), p. 9 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 bridge, introduce, Planning mechanism이 Released code includes our PARTNR benchmark tasks, metrics, baseline oracle skills, large planning model framework, and ... 대비 Table 11: Baseline results on PARTNR test set. We measure performance using simulation steps required to finish the ...을 개선하고, Table 8: Top three failure modes of 100k-scale task and evaluation generation reported for each task ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
