# Insights — ReaDy-Go: Real-to-Sim Dynamic 3D Gaussian Splatting Simulation for Environment-Specific Visual Navigation with Moving Obstacles

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2602.11575; PDF retrieval source: https://arxiv.org/pdf/2602.11575. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** The framework consists of three key components: (1) a dynamic GS simulator that integrates a static scene GS, an animatable human GS obstacle, and a ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** By reconstructing environments from RGB videos, GS enables high-fidelity rendering at fast frame rates, novel view synthesis, and simulation with an explicit 3D scene representation.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our contributions are threefold. • Dynamic GS Simulator: We develop a photorealistic realto-sim dynamic 3D Gaussian Splatting simulator with human GS obstacles.
- **p. 3 / III. METHOD - extractive body cue:** GS is a representation that enables 3D geometry reconstruction, high-fidelity novel view synthesis, and fast training and rendering by fitting positions, rotations, scales, opacities, and ...
- **p. 3 / III. METHOD - extractive body cue:** The pipeline consists of three main components: (1) a real-to-sim dynamic 3D Gaussian Splatting (GS) simulator, (2) dynamic navigation dataset generation using the simulator and ...
- **p. 4 / III. METHOD - extractive body cue:** By leveraging the simulator and planners, the pipeline collects RGB observations, actions, and relative goal positions as training samples for a navigation policy.
- **p. 3 / III. METHOD - extractive body cue:** The human animation module places an animatable human GS model in the scene and then generates plausible human motion along a given obstacle trajectory.
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** Such limitations make it difficult to learn safe navigation in the presence of dynamic obstacles and to render photorealistic human appearances within reconstructed real-world environments.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, the resulting sim-toreal distribution gap significantly degrades performance during deployment.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Motivated by these limitations, we propose ReaDy-Go, a photorealistic Real-to-Sim Dynamic 3D Gaussian Splatting Simulation pipeline for environment-specific RGB-only visual navigation with moving obstacles (Fig.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Furthermore, it shows generalization potential via zeroshot sim-to-real deployment in an unseen environment.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** ReaDy-Go yields fewer failures than the baselines, especially in failure modes related to dynamic obstacle avoidance, including Dynamic obstacle collision and Static collision during detour.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** Second, while ReaDy-Go and Vid2Sim showed similar numbers of failures in cases unrelated to dynamic obstacle interactions, ReaDy-Go was more robust in situations involving dynamic ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Visualization of the robot expert planner. (a) The robot follows a collision-free path (red) from start (green) to goal (blue). (b) When a ...
- **Boundary to test:** ReaDy-Go yields fewer failures than the baselines, especially in failure modes related to dynamic obstacle avoidance, including Dynamic obstacle collision and Static collision during detour.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | The framework consists of three key components: (1) a dynamic GS simulator that integrates a static scene GS, an animatable human GS obstacle, and a human motion generation module, enabling the placement ... | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Reported outcome | As in simulation, ReaDy-Go and Vid2Sim achieve comparable success rates in Static, but their performance diverges in Dynamic. | p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Failure/limitation | ReaDy-Go yields fewer failures than the baselines, especially in failure modes related to dynamic obstacle avoidance, including Dynamic obstacle collision and Static collision during detour. | p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `camera/depth stream, pose, map와 language goal → robot pose, free-space/semantic map와 local goal → collision-free trajectory 또는 velocity command`.
- 이 논문의 재사용 가능한 지점은 By leveraging the simulator and planners, the pipeline collects RGB observations, actions, and relative goal positions as training samples for a navigation policy.를 Given a video of a static target deployment environment, ReaDy-Go generates photorealistic navigation datasets with moving human obstacles and trains an environment-specific navigation policy, as shown in Fig.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 robot pose, free-space/semantic map와 local goal가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 ReaDy-Go yields fewer failures than the baselines, especially in failure modes related to dynamic obstacle avoidance, including Dynamic obstacle collision and Static collision during detour.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: The framework consists of three key components: (1) a dynamic GS simulator that integrates a static scene GS, an animatable human GS obstacle, and a human motion generation module, enabling the placement ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `3D Vision, Navigation, Gaussian Splatting`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** ReaDy-Go yields fewer failures than the baselines, especially in failure modes related to dynamic obstacle avoidance, including Dynamic obstacle collision and Static collision during detour.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: For each task and environment, we evaluate 100 episodes in simulation and 10 episodes in real-world experiments..
3. Compare against the body-reported baseline or a matched simpler baseline: For a fair comparison with image-goal navigation baselines (GNM, ViNT, and NoMaD), we provide them goal images captured at goal positions within 10 m of the start, with the camera oriented along ....
4. Report the body metric and its denominator/aggregation: 2) Evaluation metrics: We evaluate navigation performance using Success Rate (SR) and Average Reaching Time (ART)..
5. Re-run the body-reported ablation/failure condition: 3) Baselines: We compare the following baselines against ReaDy-Go visual navigation policies to evaluate the effect of photorealistic dynamic GS simulation data for target deployment environments. • Vid2Sim [11] generates real-to-sim na ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD); the primary result is directionally consistent at p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 framework, consists, three mechanism이 For a fair comparison with image-goal navigation baselines (GNM, ViNT, and NoMaD), we provide them goal ... 대비 2) Evaluation metrics: We evaluate navigation performance using Success Rate (SR) and Average Reaching Time (ART).을 개선하고, ReaDy-Go yields fewer failures than the baselines, especially in failure modes related to dynamic obstacle avoidance, ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
