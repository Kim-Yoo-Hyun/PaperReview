# Insights — ImagineNav: Prompting Vision-Language Models as Embodied Navigator through Scene Imagination

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=vQFw9ryKyK; PDF retrieval source: https://openreview.net/pdf/e349d69236fa6d97f504e96881ee34405d7de516.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, our contributions are: • We propose a mapless navigation approach ImagineNav.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We also provide a detailed ablation analysis to help understand the important conclusions in our framework.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We propose a new decision-making paradigm based on imagined imagery, wherein decisions are made on imaginations, enabling more nuanced, context-aware interactions that better harness VLMs' ...
- **p. 4 / 3 METHODOLOGY - extractive body cue:** The discrete action space consists of the following commands: {Stop, MoveAhead, TurnLeft, TurnRight, LookUp, LookDown}.
- **p. 5 / 3 METHODOLOGY - extractive body cue:** 3.2 FUTURE-VIEW IMAGINATION To better leverage the spatial perception and reasoning capabilities of VLMs for open-vocabulary object navigation in unknown environments, we propose an future-view ...
- **p. 6 / 3 METHODOLOGY - extractive body cue:** To determine the execution actions at each step of the PointNav process, we use Variable Experience Rollout (VER) (Wijmans et al., 2022) as our underlying ...
- **p. 4 / 3 METHODOLOGY - extractive body cue:** Subsequently, the visual observations at these locations are imagined by a NVS model.
- **Contribution anchor:** p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 6 (3 METHODOLOGY)

### Strongest assumption and failure boundary

- **p. 3 / 1 INTRODUCTION - extractive body cue:** However, one limitation of LLMs is their difficulty in embedding the robot's state directly into the planning process.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Although such a pipeline achieves great success in recent years (Zhou et al., 2023; Kuang et al., 2024; Wu et al., 2024b; Zhang et al., ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** As most VLMs cannot understand the continuous physical world, it is infeasible to directly ask VLMs to generate navigable 3D waypoints.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Thirdly, although the semantic information stored on the map can be easily expressed by text (e.g., list the categories of the observed objects), such pure ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Although previous works (Yadav et al., 2022; Ramrakhya et al., 2023; Chaplot et al., 2020; Ramakrishnan et al., 2022) can achieve high success rate in ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** We also present some failure examples at the bottom of Figure 8
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** We identified three key factors contributing to these navigation failures.
- **Boundary to test:** We also present some failure examples at the bottom of Figure 8

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, our contributions are: • We propose a mapless navigation approach ImagineNav. | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Reported outcome | On the HM3D dataset, ImagineNav achieves a success rate of 53.0% and a SPL of 23.8%, significantly outperforming most of the methods especially at success rate. | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Failure/limitation | We also present some failure examples at the bottom of Figure 8 | p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `camera/depth stream, pose, map와 language goal → robot pose, free-space/semantic map와 local goal → collision-free trajectory 또는 velocity command`.
- 이 논문의 재사용 가능한 지점은 As illustrated in Figure 3, the VLM receives the synthesized observations at future navigation waypoints and the navigation goal as inputs.를 Cap (Liang et al., 2023) generates robotic policy code directly from example language commands, enabling autonomous control and task execution based on natural language instructions.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 robot pose, free-space/semantic map와 local goal가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 We also present some failure examples at the bottom of Figure 8에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary, our contributions are: • We propose a mapless navigation approach ImagineNav.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `Vision-Language Model, Robotics, Navigation`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** We also present some failure examples at the bottom of Figure 8; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The HSSD dataset provides 40 high-quality synthetic scenes, comprising 110 training scenes and 40 validation scenes..
3. Compare against the body-reported baseline or a matched simpler baseline: Imagination Where2Imagine NVS HM3D Success Rate SPL ✗ ✗ Oracle 43.0 24.7 ✓ ✗ Oracle 55.0 27.6 ✓ ✓ Oracle 64.0 28.3 ✓ ✗ PolyOculus 49.0 23.3 ✓ ✓ PolyOculus 56.0 24.3 ....
4. Report the body metric and its denominator/aggregation: We report the performance in terms of Success Rate (SR), defined as the proportion of episodes where the agent's distance to the target object is less than 1m after executing the STOP ....
5. Re-run the body-reported ablation/failure condition: Imagination Where2Imagine NVS HM3D Success Rate SPL ✗ ✗ Oracle 43.0 24.7 ✓ ✗ Oracle 55.0 27.6 ✓ ✓ Oracle 64.0 28.3 ✓ ✗ PolyOculus 49.0 23.3 ✓ ✓ PolyOculus 56.0 24.3 ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 6 (3 METHODOLOGY); the primary result is directionally consistent at p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, contributions, mapless mechanism이 Imagination Where2Imagine NVS HM3D Success Rate SPL ✗ ✗ Oracle 43.0 24.7 ✓ ✗ Oracle 55.0 ... 대비 We report the performance in terms of Success Rate (SR), defined as the proportion of episodes where the ...을 개선하고, We also present some failure examples at the bottom of Figure 8 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
