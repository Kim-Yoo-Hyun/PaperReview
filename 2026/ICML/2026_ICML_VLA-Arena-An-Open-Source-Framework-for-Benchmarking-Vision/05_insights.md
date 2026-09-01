# Insights — VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (48 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://vla-arena.github.io/; PDF retrieval source: https://arxiv.org/pdf/2512.22539. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** We introduce VLA-Arena, the first benchmark to structurally evaluate the performance and safety of VLAs.
- **p. 2 / 1. Introduction - extractive body cue:** To address this challenge, we propose VLA-Arena, a comprehensive and accessible benchmark for evaluating VLA models.
- **p. 3 / 2. Structured Task Design - extractive body cue:** To quantitatively measure the capability frontiers of VLA models, we propose a structured task design, as compared in Table 1.
- **p. 3 / 2. Structured Task Design - extractive body cue:** Based on this classification, we propose the cumulative cost (CC) metric for a trajectory τ of length L: CC(τ) = L-1 X t=0 cinst(st, at) ...
- **p. 1 / Abstract - extractive body cue:** 5State Key Laboratory of General Artificial Intelligence, Peking University. ∗Equal contribution.
- **p. 3 / 1. Introduction - extractive body cue:** Conducting an extensive study on VLA-Arena with leading models from the two dominant architectural paradigms: autoregressive and continuous action generation, our analysis surfaces three key ...
- **p. 6 / 3. Task Suites in VLA-Arena - extractive body cue:** VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models 0.0 0.25 0.5 0.75 1.0 Success Rate StatePreservation L0 OpenVLA OpenVLA-OFT Pi0 UniVLA L1 L2 L0 L1 ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (2. Structured Task Design), p. 3 (2. Structured Task Design), p. 1 (Abstract), p. 3 (1. Introduction)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** This lack of integration prevents understanding how models handle concurrent challenges across visual, linguistic, and structural dimensions of task.
- **p. 3 / 1. Introduction - extractive body cue:** Conducting an extensive study on VLA-Arena with leading models from the two dominant architectural paradigms: autoregressive and continuous action generation, our analysis surfaces three key ...
- **p. 2 / 1. Introduction - extractive body cue:** However, existing benchmarks suffer from several limitations.
- **p. 3 / 1. Introduction - extractive body cue:** (Graded difficulty levels, e.g., L0-L2).
- **p. 22 / Figure/Table caption - extractive body cue:** Figure 8. Visualization of Typical Failure Modes in Dynamic Distractors Tasks. The failure cases are categorized into three types: 1) Misplaced grasp (Top row): General ...
- **p. 20 / Figure/Table caption - extractive body cue:** Figure 6. Attention Visualization for the Token "plate" Comparing OpenVLA and OpenVLA-OFT. The instruction is "pick up the bowl and place it on the plate". ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4. Consistent Failure Modes Observed in Real-World Deployment. When deployed on a physical Franka Research 3 robot, the model exhibits the same vulnerabilities diagnosed ...
- **Boundary to test:** Figure 8. Visualization of Typical Failure Modes in Dynamic Distractors Tasks. The failure cases are categorized into three types: 1) Misplaced grasp (Top row): General manipulation error where the gripper fails to ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We introduce VLA-Arena, the first benchmark to structurally evaluate the performance and safety of VLAs. | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Second, without explicit safety constraints, models prioritize task completion, often incurring high CC to achieve success. | p. 7 (4.2. Analysis of Performance and Failure Modes), p. 7 (4.1. Experimental Setup) |
| Failure/limitation | Figure 8. Visualization of Typical Failure Modes in Dynamic Distractors Tasks. The failure cases are categorized into three types: 1) Misplaced grasp (Top row): General manipulation error where the gripper fails to ... | p. 22 (Figure/Table caption), p. 20 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `standardized observation, action, task state와 evaluation split → benchmark state/goal와 method decision → policy/controller trajectory 또는 measured result`.
- 이 논문의 재사용 가능한 지점은 VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models 0.0 0.25 0.5 0.75 1.0 Success Rate StatePreservation L0 OpenVLA OpenVLA-OFT Pi0 UniVLA L1 L2 L0 L1 L2 W0 W1 W2 W3 W4 0.0 ...를 Collection Methods Smooth Conversion among Data Formats Specify Goal: Lemon on the Bowl (c) Open-source Framework for VLA-Arena Language Command Perturbation Visual Observation Perturbation edible fruit apple eating apple Pick up the ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 benchmark state/goal와 method decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 8. Visualization of Typical Failure Modes in Dynamic Distractors Tasks. The failure cases are categorized into three types: 1) Misplaced grasp (Top row): General manipulation error where the gripper fails to ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We introduce VLA-Arena, the first benchmark to structurally evaluate the performance and safety of VLAs.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `Robotics, VLA, Benchmark, safety, distractor, extrapolation, long horizon`.
- **Reading predecessor in the generated track queue:** AVA-VLA: Improving Vision-Language-Action Models with Active Visual Attention (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 8. Visualization of Typical Failure Modes in Dynamic Distractors Tasks. The failure cases are categorized into three types: 1) Misplaced grasp (Top row): General manipulation error where the gripper fails to ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: To facilitate reproducible fine-tuning, we introduce curated datasets derived from human demonstrations..
3. Compare against the body-reported baseline or a matched simpler baseline: In Table 2, a crossmodel comparison indicates that π0 generally outperforms the other models..
4. Report the body metric and its denominator/aggregation: To provide a comprehensive assessment, we employ success rate (SR) and cumulative cost (CC) as metrics..
5. Re-run the body-reported ablation/failure condition: Table 30. OpenVLA-OFT Fine-tuning Hyperparameters. H.3.5. OPENVLA-OFT TRAINING PARAMETERS The OpenVLA-OFT model was fine-tuned using LoRA. The training utilized 7 devices, resulting in a total effective batch size of 49. The model ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (1. Introduction), p. 6 (3. Task Suites in VLA-Arena), p. 2 (1. Introduction); the primary result is directionally consistent at p. 7 (4.2. Analysis of Performance and Failure Modes), p. 7 (4.1. Experimental Setup), p. 8 (4.3. Diagnosing Semantic and Visual Grounding); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 introduce, VLA-Arena, first mechanism이 In Table 2, a crossmodel comparison indicates that π0 generally outperforms the other models. 대비 To provide a comprehensive assessment, we employ success rate (SR) and cumulative cost (CC) as metrics.을 개선하고, Figure 8. Visualization of Typical Failure Modes in Dynamic Distractors Tasks. The failure cases are categorized ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
