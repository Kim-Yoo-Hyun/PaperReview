# Insights — Embodied-R1: Reinforced Embodied Reasoning for General Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=i5wlozMFsQ; PDF retrieval source: https://openreview.net/pdf/f96c92cfad0bb9a981c9646c6a5bbcfc1992f8fc.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1 INTRODUCTION - extractive body cue:** To bridge this gap, we propose pointing as an intuitive and effective paradigm to connect high-level understanding with generalizable action.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Simultaneously, its embodiment-agnostic nature enables knowledge transfer across diverse robot platforms, resolving the heterogeneity challenge.
- **p. 18 / B IMPLEMENTATION DETAILS OF EMBODIED-R1 - extractive body cue:** Second, for the VTG task, we introduced an additional constraint on the format: the generated visual trace must consist of exactly 8 points.
- **p. 18 / B IMPLEMENTATION DETAILS OF EMBODIED-R1 - extractive body cue:** As for Embodied-SFT, we used exactly the same data but trained with a supervised learning loss, kept the batch size at 128, and trained for ...
- **p. 18 / B IMPLEMENTATION DETAILS OF EMBODIED-R1 - extractive body cue:** Training Hyperparameters: We conducted model training on eight NVIDIA A100 40G GPUs.
- **Contribution anchor:** p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1), p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1), p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1)

### Strongest assumption and failure boundary

- **p. 1 / 1 INTRODUCTION - extractive body cue:** This disparity is widely recognized as the "seeing-to-doing gap" (Yuan et al., 2025): a failure to reliably translate rich perceptual understanding into effective robotic actions.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** This gap is largely attributed to two key challenges: (a) data scarcity, where limited embodied data prevents from sufficiently grounding language and vision with physical ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** I need to avoid obstacles and carefully move the moka pot from current position to the right side of the drawer. </think> <answer><point>[[450,496],[453,47 8], … ...
- **p. 18 / B IMPLEMENTATION DETAILS OF EMBODIED-R1 - extractive body cue:** We would like to add two clarifying points: First, if the task output fails to meet the required parsing format, subsequent analysis cannot proceed successfully, ...
- **p. 10 / 5 CONCLUSION - extractive body cue:** A detailed discussion of limitations is provided in App.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** D, we conducted an in-depth analysis of failure cases and execution time.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** The score is the accuracy of points falling within the target region.
- **Boundary to test:** We would like to add two clarifying points: First, if the task output fails to meet the required parsing format, subsequent analysis cannot proceed successfully, so the reward is set directly to ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To bridge this gap, we propose pointing as an intuitive and effective paradigm to connect high-level understanding with generalizable action. | p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Reported outcome | 5, Embodied-R1 achieves an 87.5% zero-shot success rate, an improvement of over 60% compared to the RoboPoint and FSD baselines. | p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Failure/limitation | We would like to add two clarifying points: First, if the task output fails to meet the required parsing format, subsequent analysis cannot proceed successfully, so the reward is set directly to ... | p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1), p. 10 (5 CONCLUSION) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 This gap is largely attributed to two key challenges: (a) data scarcity, where limited embodied data prevents from sufficiently grounding language and vision with physical actions (Walke et al., 2023; Lin et ...를 To bridge this gap, we propose pointing as an intuitive and effective paradigm to connect high-level understanding with generalizable action.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 We would like to add two clarifying points: First, if the task output fails to meet the required parsing format, subsequent analysis cannot proceed successfully, so the reward is set directly to ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To bridge this gap, we propose pointing as an intuitive and effective paradigm to connect high-level understanding with generalizable action.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `Vision-Language Model, Robotics, Reinforcement Learning`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** We would like to add two clarifying points: First, if the task output fails to meet the required parsing format, subsequent analysis cannot proceed successfully, so the reward is set directly to ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Our evaluation encompassed 11 QA benchmarks, 4 simulated tasks (SIMPLEREnv) (Li et al., 2024b), and 8 real-world robot (xArm platform) tasks..
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 2: Overview of four embodied pointing abilities. a VLM trained with RFT to resolve the multi-solution dilemma for embodied pointing, delivering powerful reasoning. 4 With only 3B parameters, Embodied-R1 attains state-of-the-art ....
4. Report the body metric and its denominator/aggregation: We attribute this significant improvement to the baselines' poor performance on tasks requiring spatial reasoning (e.g., moving the nearest object) and their low success rates in grasping challenging rigid objects like a ....
5. Re-run the body-reported ablation/failure condition: We also included two key ablations: Embodied-R1 w/o CS, which excludes the ViRL common-sense dataset, and Embodied-SFT, a variant trained only with SFT..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1), p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1); the primary result is directionally consistent at p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 bridge, pointing, intuitive mechanism이 Figure 2: Overview of four embodied pointing abilities. a VLM trained with RFT to resolve the ... 대비 We attribute this significant improvement to the baselines' poor performance on tasks requiring spatial reasoning (e.g., moving the ...을 개선하고, We would like to add two clarifying points: First, if the task output fails to meet ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
