# Insights — LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (42 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2606.23686; PDF retrieval source: https://arxiv.org/pdf/2606.23686. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / 1 INTRODUCTION - extractive body cue:** In summary, we establish this evaluation framework through four core technical and empirical contributions: - Parametric Safety Benchmark and Taxonomy: We introduce the Unified Behavior ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In contrast, our framework holistically assesses semantic reasoning to refuse malicious instructions, general human-robot interaction (HRI) safety for collaborative co-habitation, and uniquely introduces proximal avoidance ...
- **p. 1 / 462 Hand-Object Pairs - extractive body cue:** To systematically evaluate these challenges, we introduce a comprehensive VLA safety benchmark and develop an efficient (b) Data Generation Pipeline to synthesize 19.7K strictly collision-free ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Unlike existing benchmarks, our framework systematically evaluates the physical and semantic safety boundaries of VLA models through parameterized task specifications and multi-dimensional hazard scenarios.
- **p. 5 / 462 Hand-Object Pairs - extractive body cue:** Our benchmark consists of four core components: a parametric environment definition framework (Sec.
- **p. 8 / 462 Hand-Object Pairs - extractive body cue:** Metric Human Teleoperation Ours Human Effort (min/task) 7.4 1.8 Data Scalability 1:1 1:M Collision Guarantee Human-dependent Planner-enforced Spatial Representation World-centric Object-centric Trajectory Consistency High variance ...
- **p. 1 / 462 Hand-Object Pairs - extractive body cue:** Image Input Text Instruction Multi-modal VLM Action Decoder Proprioception Action Tokens World Model Image Input Text Instruction Future State Action Image Input Text Instruction Sys.
- **Contribution anchor:** p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (462 Hand-Object Pairs), p. 3 (1 INTRODUCTION), p. 5 (462 Hand-Object Pairs), p. 8 (462 Hand-Object Pairs)

### Strongest assumption and failure boundary

- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, these benchmarks suffer from two critical limitations.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** First, their exclusive reliance on human teleoperation is prohibitively time-consuming, severely bottlenecking the scalability required to train robust foundation models.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** This infrastructure drives a fivedimensional curriculum that decouples safety into semantic reasoning and physical constraints. - Keypose-Driven Data Generation Pipeline: To overcome the inefficiency and ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our results reveal that while high-diversity training fosters safer trajectories, task success remains bottlenecked by sub-optimal trajectory synthesis and semantic misalignment.
- **p. 39 / C.3 Additional Experimental Results - extractive body cue:** This suggests that broader trajectory coverage can improve safety-aware execution across multiple VLA architectures, although it does not fully eliminate collision or task-completion failures.
- **p. 10 / 4 Experiment - extractive body cue:** To further assess execution quality, we employ 3 supplementary metrics: Collision Rate (CR) isolates collision-induced terminations from standard task failures, Execution Time evaluates operational efficiency ...
- **p. 42 / C.3 Additional Experimental Results - extractive body cue:** These dynamic guardrails will allow the control policy to trigger verified safe fallback maneuvers prior to any catastrophic physical failure.
- **Boundary to test:** This suggests that broader trajectory coverage can improve safety-aware execution across multiple VLA architectures, although it does not fully eliminate collision or task-completion failures.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, we establish this evaluation framework through four core technical and empirical contributions: - Parametric Safety Benchmark and Taxonomy: We introduce the Unified Behavior Domain Definition Language (UBDDL) to enable the ... | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Reported outcome | Among the evaluated standard VLAs, π0.5 achieves the highest overall success rate across all suites and difficulty levels. | p. 11 (4 Experiment), p. 10 (4 Experiment) |
| Failure/limitation | This suggests that broader trajectory coverage can improve safety-aware execution across multiple VLA architectures, although it does not fully eliminate collision or task-completion failures. | p. 39 (C.3 Additional Experimental Results), p. 10 (4 Experiment) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `standardized observation, action, task state와 evaluation split → benchmark state/goal와 method decision → policy/controller trajectory 또는 measured result`.
- 이 논문의 재사용 가능한 지점은 Image Input Text Instruction Multi-modal VLM Action Decoder Proprioception Action Tokens World Model Image Input Text Instruction Future State Action Image Input Text Instruction Sys.를 1 Fast, Low-Level Control High-Frequency Data Planner/ Policy Affordance-Aware Grasping Tabletop Spatial Avoidance Human-Robot Interaction Free-Space Hand-Object Avoidance OpenVLA OpenVLA-OFT VLA-JEPA UniVLA GR00T N1.5 GR00T N1.6 Explic ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 benchmark state/goal와 method decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 This suggests that broader trajectory coverage can improve safety-aware execution across multiple VLA architectures, although it does not fully eliminate collision or task-completion failures.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary, we establish this evaluation framework through four core technical and empirical contributions: - Parametric Safety Benchmark and Taxonomy: We introduce the Unified Behavior Domain Definition Language (UBDDL) to enable the ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model, Benchmark, semantic`.
- **Reading predecessor in the generated track queue:** Pushing the Limits of Cross-Embodiment Learning for Manipulation and Navigation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** end of this track queue (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** This suggests that broader trajectory coverage can improve safety-aware execution across multiple VLA architectures, although it does not fully eliminate collision or task-completion failures.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: In our benchmark, the barrier function is defined by a distance-based safety margin: \la b el {e q:d i stance_barrier} h(z_t)= d(z_t,\mathcal {O}_t)-d_{\mathrm {safe}}, (A.4) where d(zt, Ot) denotes the minimum distance ....
3. Compare against the body-reported baseline or a matched simpler baseline: Across diverse axes of visual and state stochasticity, including image noise (Noise), robot initial state (Init State), viewpoint shifts (View), and scene variations (Scene), the SR remains relatively stable, fluctuating between 56.3% ....
4. Report the body metric and its denominator/aggregation: Metrics are reported as mean Success Rate (SR, %), with standard deviations computed across three training seeds shown in parentheses..
5. Re-run the body-reported ablation/failure condition: To distinguish the safety-evaluation difficulty from the effect of training on LIBERO-Safety, we additionally evaluate two representative policies under two control settings: zero-shot inference without task-specific fine-tuning, and SF ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 8 (462 Hand-Object Pairs), p. 1 (462 Hand-Object Pairs), p. 1 (462 Hand-Object Pairs); the primary result is directionally consistent at p. 11 (4 Experiment), p. 10 (4 Experiment), p. 12 (4 Experiment); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, establish, evaluation mechanism이 Across diverse axes of visual and state stochasticity, including image noise (Noise), robot initial state (Init ... 대비 Metrics are reported as mean Success Rate (SR, %), with standard deviations computed across three training seeds shown ...을 개선하고, This suggests that broader trajectory coverage can improve safety-aware execution across multiple VLA architectures, although it ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
