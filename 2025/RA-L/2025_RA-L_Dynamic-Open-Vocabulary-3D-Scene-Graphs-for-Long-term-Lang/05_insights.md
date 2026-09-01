# Insights — Dynamic Open-Vocabulary 3D Scene Graphs for Long-term Language-Guided Mobile Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2410.11989; PDF retrieval source: https://arxiv.org/pdf/2410.11989. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our contributions are as follows: • We propose a novel robotic framework that integrates dynamic open-vocabulary 3D scene graphs with languageguided task planning, enabling accurate ...
- **p. 4 / III. METHOD - extractive body cue:** We propose an efficient method that leverages new RGB-D observations to update the volumetric representation accordingly.
- **p. 2 / III. METHOD - extractive body cue:** DovSG enables mobile robots to perform long-term tasks in indoor environments by constructing dynamic 3D scene graphs and using large language models for task planning.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we enhance robotic capabilities by introducing a novel and practical robotic framework, the DovSG system.
- **p. 4 / III. METHOD - extractive body cue:** To address this issue, we have designed a simple memory update module that can quickly perform local updates to the memory based on new RGB-D ...
- **p. 4 / III. METHOD - extractive body cue:** Then, we apply an advanced Open-Vocal segmentation model to segment regions in the RGB images, extract semantic feature vectors for each region, and project them ...
- **p. 5 / III. METHOD - extractive body cue:** 2) Mobile control: Once the target location is determined, we use the A* [34] algorithm to generate a collision-free navigation path from the start point ...
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 4 (III. METHOD), p. 2 (III. METHOD), p. 1 (I. INTRODUCTION), p. 4 (III. METHOD), p. 4 (III. METHOD)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** This limitation restricts their applicability in real-world scenarios where adaptability is crucial.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To address the challenge of scene perception, our perception module integrates advanced tools such as RecognizeAnything [6], Grounding DINO [7], Segment Anything-2 [8], and CLIP ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our contributions are as follows: • We propose a novel robotic framework that integrates dynamic open-vocabulary 3D scene graphs with languageguided task planning, enabling accurate ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** In the "Positional Shift" scenario, the residual effect of CLIP features can occasionally mislead the robot into navigating toward the object's historical location, ultimately causing ...
- **p. 5 / III. METHOD - extractive body cue:** 2) Mobile control: Once the target location is determined, we use the A* [34] algorithm to generate a collision-free navigation path from the start point ...
- **p. 6 / III. METHOD - extractive body cue:** A buffer of 0.1 is added to account for potential collisions.
- **p. 6 / III. METHOD - extractive body cue:** In the first row, we cropped the point cloud input into anyGrasp within a certain range around the target object, allowing anyGrasp to focus more ...
- **Boundary to test:** In the "Positional Shift" scenario, the residual effect of CLIP features can occasionally mislead the robot into navigating toward the object's historical location, ultimately causing navigation failure.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our contributions are as follows: • We propose a novel robotic framework that integrates dynamic open-vocabulary 3D scene graphs with languageguided task planning, enabling accurate long-term task execution in dynamic and interactive ... | p. 2 (I. INTRODUCTION), p. 4 (III. METHOD) |
| Reported outcome | This makes it highly likely for the robot to navigate near the target, resulting in a significantly higher success rate compared to "Appearance" and "Positional Shift" (in 80 trials, it achieved 5 ... | p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Failure/limitation | In the "Positional Shift" scenario, the residual effect of CLIP features can occasionally mislead the robot into navigating toward the object's historical location, ultimately causing navigation failure. | p. 7 (IV. EXPERIMENTS), p. 5 (III. METHOD) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `egocentric RGB-D, language/task goal, base-arm proprioception → map/object/contact state와 base-arm coordination decision → base motion plus arm/gripper action`.
- 이 논문의 재사용 가능한 지점은 YAN et al.: DYNAMIC OPEN-VOCABULARY 3D SCENE GRAPHS FOR LONG-TERM LANGUAGE-GUIDED MOBILE MANIPULATION 5 and color information, we process each new observation Ik as follows: (1) We transform the all voxel point ...를 After the robot collects new RGB-D observations Ik for k ∈{t + 1, ..., t + n}, where each observation Ik = ⟨Irgb k , Idepth k , Ic2b k ⟩includes the ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 map/object/contact state와 base-arm coordination decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 In the "Positional Shift" scenario, the residual effect of CLIP features can occasionally mislead the robot into navigating toward the object's historical location, ultimately causing navigation failure.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our contributions are as follows: • We propose a novel robotic framework that integrates dynamic open-vocabulary 3D scene graphs with languageguided task planning, enabling accurate long-term task execution in dynamic and interactive ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, 3D Vision, Graph Reasoning, semantic`.
- **Reading predecessor in the generated track queue:** Language-Grounded Dynamic Scene Graphs for Interactive Object Search with Mobile Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In the "Positional Shift" scenario, the residual effect of CLIP features can occasionally mislead the robot into navigating toward the object's historical location, ultimately causing navigation failure.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: 2) Environment and Task Setups: To verify our method's ability to enable robots to perform long-term tasks in dynamic environments, we designed an experiment in 4 real-world rooms..
3. Compare against the body-reported baseline or a matched simpler baseline: In contrast, DovSG, supported by precise relocalization, can accurately identify the voxel index where changes have occurred in the scene, significantly outperforming the baseline..
4. Report the body metric and its denominator/aggregation: (3) Task Success Rate: This metric represents the overall task completion success rate..
5. Re-run the body-reported ablation/failure condition: (2) How effectively does this facilitate the completion of consecutive tasks without manual resets?.
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD); the primary result is directionally consistent at p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 contributions, follows, novel mechanism이 In contrast, DovSG, supported by precise relocalization, can accurately identify the voxel index where changes have ... 대비 (3) Task Success Rate: This metric represents the overall task completion success rate.을 개선하고, In the "Positional Shift" scenario, the residual effect of CLIP features can occasionally mislead the robot ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
