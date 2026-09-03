# Insights — Seeing Across Views: Benchmarking Spatial Reasoning of Vision-Language Models in Robotic Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (50 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=jXDZJAfRZB; PDF retrieval source: https://openreview.net/pdf/458ff860f6b8211513575bef44521e0241b321c0.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To fill this gap, we introduce MV-RoboBench, a benchmark specifically designed to evaluate multiview spatial reasoning in robotic manipulation scenarios.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** 2 MV-ROBOBENCH 2.1 OVERVIEW We introduce MV-RoboBench, a benchmark designed to evaluate the multi-view reasoning capabilities of VLMs in robotic manipulation scenarios.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our key contributions are as follows: • We establish the first benchmark that integrates spatial and robotic reasoning with synchronized multi-view inputs in robotic manipulation ...
- **p. 23 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** This design enables rapid prototyping of spatial arrangements and provides a consistent interface for generating QA items that require reasoning about relative positions and geometric ...
- **p. 5 / 1 INTRODUCTION - extractive body cue:** For each subtask, task-specific templates were designed, and trained annotators constructed corresponding five-choice QA pairs from the curated image pairs.
- **p. 25 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** We then describe the four robotic subtasks, which extend spatial reasoning to manipulation scenarios: Action Planning, Step Execution, Trajectory Selection, and Affordance Recognition.
- **p. 32 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** They examine whether models can ground spatial understanding into action decisions, ranging from high-level planning to low-level execution, and from trajectory-level reasoning to grasp affordance ...
- **Contribution anchor:** p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 23 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 5 (1 INTRODUCTION), p. 25 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS)

### Strongest assumption and failure boundary

- **p. 10 / 1 INTRODUCTION - extractive body cue:** By isolating failure modes in multi-view grounding rather than in isolated perception, MVRoboBench exposes the precise bottlenecks that future embodied AI systems must overcome.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Singleview inputs are inherently limited by challenges like occlusion, depth ambiguity, and restricted fields of view.
- **p. 10 / 1 INTRODUCTION - extractive body cue:** To address these challenges, specialized approaches (Cheng et al., 2024; Ma et al., 2025; Zhou et al., 2025; Fan et al., 2025; Liu et al., ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Multi-view observations, by contrast, offer complementary perspectives that help overcome these limitations.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** These findings highlight the unique challenges of multi-view reasoning in robotics and the need for specialized benchmarks like MV-RoboBench.
- **p. 36 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** GPT-5 often prefers grasp lines or trajectories that look visually neat (e.g., centered on the visible surface) but would be unstable or collision-prone for a ...
- **p. 49 / Figure/Table caption - extractive body cue:** Figure 30: Case Study 2: Instance-Level Correspondence Failure (Qwen2.5-VL-72B). The scene contains multiple instances of the same class (yellow peppers). The model correctly iden- tifies ...
- **Boundary to test:** GPT-5 often prefers grasp lines or trajectories that look visually neat (e.g., centered on the visible surface) but would be unstable or collision-prone for a parallel gripper in 3D; it 36

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To fill this gap, we introduce MV-RoboBench, a benchmark specifically designed to evaluate multiview spatial reasoning in robotic manipulation scenarios. | p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| Reported outcome | Table 7: Comparison of Single-View vs. Multi-View performance on selected subtasks. The values represent Multi-View accuracy, and values in parentheses indicate the change (∆) compared to the Single-View baseline. Positive ∆indicates th ... | p. 33 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Failure/limitation | GPT-5 often prefers grasp lines or trajectories that look visually neat (e.g., centered on the visible surface) but would be unstable or collision-prone for a parallel gripper in 3D; it 36 | p. 36 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 49 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `standardized observation, action, task state와 evaluation split → benchmark state/goal와 method decision → policy/controller trajectory 또는 measured result`.
- 이 논문의 재사용 가능한 지점은 Top: original inputs from left gripper, head, and right gripper cameras; Bottom: blurry synthesized view from interpolated extrinsics. "text": "Image context: Corresponding estimated depth map.를 Our results suggest that scaling perception alone is insufficient-models require explicit reasoning mechanisms to transform multi-view observations into actionable, embodied understanding.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 benchmark state/goal와 method decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 GPT-5 often prefers grasp lines or trajectories that look visually neat (e.g., centered on the visible surface) but would be unstable or collision-prone for a parallel gripper in 3D; it 36에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To fill this gap, we introduce MV-RoboBench, a benchmark specifically designed to evaluate multiview spatial reasoning in robotic manipulation scenarios.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `Vision-Language Model, Robotics, 3D Vision, Benchmark`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** GPT-5 often prefers grasp lines or trajectories that look visually neat (e.g., centered on the visible surface) but would be unstable or collision-prone for a parallel gripper in 3D; it 36; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: F.10 SUMMARY OF BENCHMARK CONSTRUCTION Taken together, the eight subtasks provide a comprehensive evaluation of spatial and robotic reasoning in multi-view environments..
3. Compare against the body-reported baseline or a matched simpler baseline: Table 7: Comparison of Single-View vs. Multi-View performance on selected subtasks. The values represent Multi-View accuracy, and values in parentheses indicate the change (∆) compared to the Single-View baseline. Positive ∆indicates th ....
4. Report the body metric and its denominator/aggregation: Table 2: Evaluation on MV-RoboBench under a unified zero-shot prompt. denotes the best score and the second-best within each column. Qwen2.5-vl-72B leads among open-source models, while GPT-5 ranks highest overall but still ....
5. Re-run the body-reported ablation/failure condition: Figure 4: Best-per-group model perfor- mance across MV-RoboBench subtasks. indicating that they fail to leverage multi-view infor- mation and effectively guess without spatial integration. In contrast, reasoning-enhanced models rise to ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 25 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 32 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 25 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS); the primary result is directionally consistent at p. 33 (Figure/Table caption), p. 8 (Figure/Table caption), p. 37 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 fill, introduce, MV-RoboBench mechanism이 Table 7: Comparison of Single-View vs. Multi-View performance on selected subtasks. The values represent Multi-View accuracy, ... 대비 Table 2: Evaluation on MV-RoboBench under a unified zero-shot prompt. denotes the best score and the second-best within ...을 개선하고, GPT-5 often prefers grasp lines or trajectories that look visually neat (e.g., centered on the visible ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
