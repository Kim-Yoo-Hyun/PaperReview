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
- **p. 1 / Abstract - extractive body cue:** 5State Key Laboratory of General Artificial Intelligence.
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

- **Paper-specific interface:** Perturbation Dims: Lighting, Camera pose, Object Color, Language instructions, and Visual Noise. (p. 3, 1. Introduction).
- **Paper-specific mechanism:** We introduce VLA-Arena, the first benchmark to structurally evaluate the performance and safety of VLAs. (p. 2, 1. Introduction).
- **Evidence boundary:** the reported outcome is Table 1. Comprehensive Comparison with Existing Robotics Benchmarks. Benchmarks are grouped by their underlying Physics Engine. Resources: Data (Fine-grained, filtered datasets), Frmwk (Open framework supporting custom uploads). Structu ... (p. 3, Figure/Table caption); the relevant task/metric cue is VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models VLA-Arena (Ours) LIBERO Benchmark 0.0 0.2 0.4 0.6 0.8 1.0 Success Rate -52% -28% -64% -28% w/ Correct Language Instruction w/ Wrong ... (p. 8, 4.3. Diagnosing Semantic and Visual Grounding). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** While VLAs have progressed rapidly, their capability boundaries, limitations, and failure modes remain poorly understood. (p. 2, 1. Introduction).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `Robotics, VLA, Benchmark, safety, distractor, extrapolation, long horizon`.
- **Reading predecessor in the generated track queue:** AVA-VLA: Improving Vision-Language-Action Models with Active Visual Attention (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 8. Visualization of Typical Failure Modes in Dynamic Distractors Tasks. The failure cases are categorized into three types: 1) Misplaced grasp (Top row): General manipulation error where the gripper fails to ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Perturbation Dims: Lighting, Camera pose, Object Color, Language instructions, and Visual Noise. (p. 3, 1. Introduction); preserve the objective/update rule: This dimension evaluates the model's ability to not only complete its primary objective but to do so while adhering to safety constraints, a critical requirement for real-world deployment. (p. 5, 3. Task Suites in VLA-Arena).
2. Use the paper-reported task/data/environment cue: Datasets are organized by level (i.e., L0 or L1) and size (i.e., Small, Medium, and Large, containing 10, 30, and 50 trajectories per task, respectively). (p. 7, 4.1. Experimental Setup).
3. Compare against the reported or matched baseline: In Table 2, a crossmodel comparison indicates that π0 generally outperforms the other models. (p. 7, 4.2. Analysis of Performance and Failure Modes).
4. Report the body metric with its denominator and aggregation: VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models VLA-Arena (Ours) LIBERO Benchmark 0.0 0.2 0.4 0.6 0.8 1.0 Success Rate -52% -28% -64% -28% w/ Correct Language Instruction w/ Wrong ... (p. 8, 4.3. Diagnosing Semantic and Visual Grounding).
5. Re-run the reported ablation or stress/failure condition: Notably, π0 and OpenVLA-OFT maintain partial functionality on V4, suggesting dual-input views aid invariant grounding. (p. 7, 4.3. Diagnosing Semantic and Visual Grounding); if none is reported, design one around: While VLAs have progressed rapidly, their capability boundaries, limitations, and failure modes remain poorly understood. (p. 2, 1. Introduction).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1. Introduction), p. 2 (1. Introduction), match the reported outcome at p. 3 (Figure/Table caption), p. 5 (Figure/Table caption), p. 8 (4.3. Diagnosing Semantic and Visual Grounding), and measure the boundary at p. 2 (1. Introduction), p. 9 (5. Real-Robot Validation).

## Falsifiable research question

Under the paper's stated interface (Perturbation Dims: Lighting, Camera pose, Object Color, Language instructions, and Visual Noise.), does the paper-specific mechanism (We introduce VLA-Arena, the first benchmark to structurally evaluate the performance and safety of VLAs.) retain the reported evaluation outcome (VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models VLA-Arena (Ours) LIBERO Benchmark 0.0 0.2 0.4 0.6 0.8 1.0 ...) when tested against the paper's strongest explicit boundary (While VLAs have progressed rapidly, their capability boundaries, limitations, and failure modes remain poorly understood.)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models VLA-Arena (Ours) LIBERO Benchmark 0.0 0.2 0.4 0.6 0.8 1.0 ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (48 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** We introduce VLA-Arena, the first benchmark to structurally evaluate the performance and safety of VLAs. (p. 2, 1. Introduction).
- **Paper-supported outcome:** Table 1. Comprehensive Comparison with Existing Robotics Benchmarks. Benchmarks are grouped by their underlying Physics Engine. Resources: Data (Fine-grained, filtered datasets), Frmwk (Open framework supporting custom uploads). Structu ... (p. 3, Figure/Table caption).
- **Strongest explicit boundary:** While VLAs have progressed rapidly, their capability boundaries, limitations, and failure modes remain poorly understood. (p. 2, 1. Introduction).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
