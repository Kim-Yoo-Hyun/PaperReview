# Insights — What Matters in Learning from Offline Human Demonstrations for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v164/mandlekar22a.html; PDF retrieval source: https://proceedings.mlr.press/v164/mandlekar22a/mandlekar22a.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / Dataset - extractive body cue:** We present success rates averaged over 3 seeds for each method across the low-dim Machine-Generated (MG), Proficient-Human (PH), and Multi-Human (MH) datasets.
- **p. 2 / 1 Introduction - extractive body cue:** We find that history-dependent models can be extremely effective in learning from single and multi-human datasets while state-of-the-art batch RL algorithms struggle to learn from ...
- **p. 3 / Dataset - extractive body cue:** Unlike traditional supervised learning, where model selection can be achieved by using the model with the lowest validation loss [21], offline policy learning often suffers ...
- **p. 4 / Dataset - extractive body cue:** We collected these datasets by first training a state-of-the-art RL algorithm [30] on the Lift and Can task, taking agent checkpoints that are saved regularly ...
- **p. 3 / Dataset - extractive body cue:** In our study, we explore how agent design decisions affect policy performances, including the choice of agent architecture, agent observation space, and hyperparameter choices per ...
- **p. 1 / Abstract - extractive body cue:** Based on the study, we derive a series of lessons including the sensitivity to different algorithmic design choices, the dependence on the quality of the ...
- **p. 2 / 1 Introduction - extractive body cue:** Differences from classic supervised learning, such as a mismatch between training and evaluation objectives (task success rate), can make selecting a final policy challenging [21, ...
- **Contribution anchor:** p. 3 (Dataset), p. 2 (1 Introduction), p. 3 (Dataset), p. 4 (Dataset), p. 3 (Dataset), p. 1 (Abstract)

### Strongest assumption and failure boundary

- **p. 2 / 1 Introduction - extractive body cue:** Unfortunately, a lack of suitable benchmark and human datasets have made studying this setting difficult.
- **p. 2 / 1 Introduction - extractive body cue:** Studying these challenges in the context of robot manipulation and human-provided datasets could be a stepping stone to closing the gap between robot and human ...
- **p. 1 / 1 Introduction - extractive body cue:** What has inhibited the use of large human-provided datasets to address this gap?
- **p. 1 / 1 Introduction - extractive body cue:** Despite these advances, the offline learning paradigm has not been nearly as disruptive in robotics as in other disciplines - there is a large gap ...
- **p. 4 / Dataset - extractive body cue:** We present success rates averaged over 3 seeds for each method across different subsets of the Multi-Human datasets, corresponding to mixtures of demonstrations from "Better", ...
- **p. 6 / 4 Experiments - extractive body cue:** There is a strong expectation for batch RL algorithms to be able to distinguish between actions leading to successful placement and actions leading to task ...
- **p. 6 / 4 Experiments - extractive body cue:** The final row of Table 2 shows additional results on a diagnostic dataset termed Can-Paired, where a single operator collected 2 demonstrations for each of ...
- **Boundary to test:** We present success rates averaged over 3 seeds for each method across different subsets of the Multi-Human datasets, corresponding to mixtures of demonstrations from "Better", "Adequate", and "Worse" human operators, and finally ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We present success rates averaged over 3 seeds for each method across the low-dim Machine-Generated (MG), Proficient-Human (PH), and Multi-Human (MH) datasets. | p. 3 (Dataset), p. 2 (1 Introduction) |
| Reported outcome | Unlike traditional supervised learning, where model selection can be achieved by using the model with the lowest validation loss [21], offline policy learning often suffers from the fact that the training objective ... | p. 3 (Dataset), p. 6 (4 Experiments) |
| Failure/limitation | We present success rates averaged over 3 seeds for each method across different subsets of the Multi-Human datasets, corresponding to mixtures of demonstrations from "Better", "Adequate", and "Worse" human operators, and finally ... | p. 4 (Dataset), p. 6 (4 Experiments) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `standardized observation, action, task state와 evaluation split → benchmark state/goal와 method decision → policy/controller trajectory 또는 measured result`.
- 이 논문의 재사용 가능한 지점은 Offline policy learning is sensitive to the state and action space coverage in the dataset, and by extension, the size of the dataset itself.를 To study the effect of observation modalities, we capture a diverse set of sensor streams when collecting the dataset, including end-effector, gripper fingers, and joints, groundtruth object poses, and images from an ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 benchmark state/goal와 method decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 We present success rates averaged over 3 seeds for each method across different subsets of the Multi-Human datasets, corresponding to mixtures of demonstrations from "Better", "Adequate", and "Worse" human operators, and finally ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We present success rates averaged over 3 seeds for each method across the low-dim Machine-Generated (MG), Proficient-Human (PH), and Multi-Human (MH) datasets.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Imitation Learning, offline learning, robot dataset, Benchmark, robomimic`.
- **Reading predecessor in the generated track queue:** Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Implicit Behavioral Cloning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** We present success rates averaged over 3 seeds for each method across different subsets of the Multi-Human datasets, corresponding to mixtures of demonstrations from "Better", "Adequate", and "Worse" human operators, and finally ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We collected 3 additional real-world datasets with a Franka robotic arm - Lift (Real), Can (Real), and Tool Hang (Real)..
3. Compare against the body-reported baseline or a matched simpler baseline: BC-RNN is a strong baseline on suboptimal human data, but there is room for improvement..
4. Report the body metric and its denominator/aggregation: Figure 3: Effect of Dataset Size. We study how the BC-RNN success rate changes when lowering the quantity of data to 20% and 50%. Results show that less complex tasks (Lift, Can) ....
5. Re-run the body-reported ablation/failure condition: 4.3 Effect of Observation Space (C5) Learning from image observations can match low-dim agent performance..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (1 Introduction), p. 3 (Dataset), p. 4 (Dataset); the primary result is directionally consistent at p. 3 (Dataset), p. 6 (4 Experiments), p. 3 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 present, success, rates mechanism이 BC-RNN is a strong baseline on suboptimal human data, but there is room for improvement. 대비 Figure 3: Effect of Dataset Size. We study how the BC-RNN success rate changes when lowering the quantity ...을 개선하고, We present success rates averaged over 3 seeds for each method across different subsets of the ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
