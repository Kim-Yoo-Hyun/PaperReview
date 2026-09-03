# Insights — Generalizable Coarse-to-Fine Robot Manipulation via Language-Aligned 3D Keypoints

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=WXFfMLyB6y; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/244660. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In real-world experiments, our method demonstrate strong generalization ability to novel tasks and object variations with only 10 demonstrations per task.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address these limitations and issues, we propose Coarse-to-fine Language-Aligned manipulation Policy (CLAP), a novel coarse-to-fine 3D manipulation policy.
- **p. 5 / 4 METHOD - extractive body cue:** Our hierarchical policy consists of a coarse task planner and a fine-grained action predictor, as shown in Figure 2.
- **p. 6 / 4 METHOD - extractive body cue:** To mitigate this, we introduce two ideas.
- **p. 6 / 4 METHOD - extractive body cue:** To address this issue, we propose decoupling task planning from keypoint prediction via a two-round inference protocol.
- **p. 6 / 4 METHOD - extractive body cue:** Instead, inspired by Chain-of-Thought reasoning (Mu et al., 2023; Zawalski et al., 2024; Zhao et al., 2025) for robotics, we design a reasoning process by ...
- **p. 7 / 4 METHOD - extractive body cue:** Our feature encoding pipeline consists of three stages to construct a unified 3D-aware and language-aligned representation.
- **Contribution anchor:** p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 5 (4 METHOD), p. 6 (4 METHOD), p. 6 (4 METHOD), p. 6 (4 METHOD)

### Strongest assumption and failure boundary

- **p. 2 / 1 INTRODUCTION - extractive body cue:** For simulation, we use GemBench (Garcia et al., 2025), a benchmark specifically designed to assess the generalization ability of multi-task language-conditioned policies across varying difficulty ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, scaling these methods to a broader range of real-world applications (e.g., industrial, service, or home robotics) requires enhancing both (G1) their generalization to environment ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address these limitations and issues, we propose Coarse-to-fine Language-Aligned manipulation Policy (CLAP), a novel coarse-to-fine 3D manipulation policy.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Empirical evaluations in simulation and on a real robot demonstrate state-of-the-art performance in both robustness to visual and object changes and generalization to unseen tasks.
- **p. 4 / 3 BACKGROUND - extractive body cue:** As a result, it suffers from deficient generalization to visual changes, object variations, and novel tasks.
- **p. 16 / A.5 ADDITIONAL ABLATION STUDY - extractive body cue:** Further increasing the number of robot trajectory improves on the in-domain performance (L1) while does not help in the average success rate.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Furthermore, our design leads to substantial performance gain on the most challenging Level-4 tasks, where several baselines methods fail consistently.
- **Boundary to test:** Further increasing the number of robot trajectory improves on the in-domain performance (L1) while does not help in the average success rate.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In real-world experiments, our method demonstrate strong generalization ability to novel tasks and object variations with only 10 demonstrations per task. | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Reported outcome | Table 2: Ablation study of CLAP on GemBench. Here are the average success rates of 4 levels of evaluation tasks from Gembench under different training settings. state-of-the-art method (Li et al., 2025b). ... | p. 8 (Figure/Table caption), p. 7 (5 EXPERIMENTS) |
| Failure/limitation | Further increasing the number of robot trajectory improves on the in-domain performance (L1) while does not help in the average success rate. | p. 16 (A.5 ADDITIONAL ABLATION STUDY), p. 8 (5 EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 The fine-grained action predictor takes as input both the step instruction and the multi-view RGB-D images and outputs an action.를 In addition to task decomposition done at the beginning, at every execution timestep, the VLM fθ is also exploited to predict both the step instruction ℓtk (used as a novel input of ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Further increasing the number of robot trajectory improves on the in-domain performance (L1) while does not help in the average success rate.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In real-world experiments, our method demonstrate strong generalization ability to novel tasks and object variations with only 10 demonstrations per task.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `Robotics, 3D Vision, Imitation Learning`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Further increasing the number of robot trajectory improves on the in-domain performance (L1) while does not help in the average success rate.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: It is LoRA fine-tuned (Hu et al., 2022) with the object keypoint dataset, language plans, and robot trajectories..
3. Compare against the body-reported baseline or a matched simpler baseline: Table 2: Ablation study of CLAP on GemBench. Here are the average success rates of 4 levels of evaluation tasks from Gembench under different training settings. state-of-the-art method (Li et al., 2025b). ....
4. Report the body metric and its denominator/aggregation: RVT2 CLAP RVT2 CLAP RVT2 CLAP RVT2 CLAP RVT2 CLAP place shape in shape sorter 60% 60% 35% 50% 30% 40% 20% 50% 36.2% 50% put block in cup with same color ....
5. Re-run the body-reported ablation/failure condition: Table 2: Ablation study of CLAP on GemBench. Here are the average success rates of 4 levels of evaluation tasks from Gembench under different training settings. state-of-the-art method (Li et al., 2025b). ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (4 METHOD), p. 6 (4 METHOD), p. 7 (4 METHOD); the primary result is directionally consistent at p. 8 (Figure/Table caption), p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 real-world, experiments, demonstrate mechanism이 Table 2: Ablation study of CLAP on GemBench. Here are the average success rates of 4 ... 대비 RVT2 CLAP RVT2 CLAP RVT2 CLAP RVT2 CLAP RVT2 CLAP place shape in shape sorter 60% 60% 35% ...을 개선하고, Further increasing the number of robot trajectory improves on the in-domain performance (L1) while does not ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
