# Insights — VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=QZYZ0Xm58q; PDF retrieval source: https://arxiv.org/pdf/2502.02175. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** To address the inefficiency introduced by repeatedly processing static visual information, we present VLA-Cache, a training-free inference acceleration method that exploits temporal continuity in robotic ...
- **p. 3 / 3 Methodology - extractive body cue:** To address this, we propose a method that identifies visually static tokens and filters out semantically important ones based on attention scores from the VLA ...
- **p. 3 / 3 Methodology - extractive body cue:** In the following sections, we introduce its core mechanisms: static token selection, task-relevance filtering, and layer-adaptive reuse to accelerate VLA inference while preserving action accuracy.
- **p. 2 / 1 Introduction - extractive body cue:** This consistency allows for caching the computations of these tokens from the previous step.
- **Contribution anchor:** p. 2 (1 Introduction), p. 3 (3 Methodology), p. 3 (3 Methodology), p. 2 (1 Introduction)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** While effective to some extent, these methods often require architectural modifications or retraining, and more importantly, they lack task-specific design tailored to the intrinsic characteristics ...
- **p. 1 / 1 Introduction - extractive body cue:** Learning a robust and generalizable policy for robotic manipulation through policy learning has long been a challenging problem [1], with traditional reinforcement learning approaches [2, ...
- **p. 2 / 1 Introduction - extractive body cue:** Action (T) LLM Decoder Current Step (T) Tokenize Previous Step (T-1) Action (T-1) Update & Caching LLM Decoder Static Dynamic Tokenize Pick up the gray ...
- **p. 2 / 1 Introduction - extractive body cue:** To further optimize reuse, VLA-Cache employs a layer-adaptive caching strategy that dynamically adjusts the reuse ratio per layer based on attention entropy, prioritizing precise updates ...
- **p. 18 / Figure/Table caption - extractive body cue:** Table 11: Real-world results with trial counts and success rates. Results with Counts and Rates. Table 11 reports per-task successes and failures, along with the ...
- **p. 8 / 5 Experiment - extractive body cue:** In contrast, FastV and SparseVLM fail to improve inference speed and often degrade task performance.
- **p. 8 / 5 Experiment - extractive body cue:** It performs robustly across tasks and exceeds the baseline on goal-oriented manipulation.
- **Boundary to test:** Table 11: Real-world results with trial counts and success rates. Results with Counts and Rates. Table 11 reports per-task successes and failures, along with the corresponding success rate. Average success is computed ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To address the inefficiency introduced by repeatedly processing static visual information, we present VLA-Cache, a training-free inference acceleration method that exploits temporal continuity in robotic perception. | p. 2 (1 Introduction), p. 3 (3 Methodology) |
| Reported outcome | Figure 4: Visualization of VLA-Cache token reuse across settings. (a) LIBERO simulation with OpenVLA. (b) Real-world task under dynamic background. (c) and (d) Main and wrist camera views from OpenVLA-OFT. Blue: static ... | p. 9 (Figure/Table caption), p. 8 (5 Experiment) |
| Failure/limitation | Table 11: Real-world results with trial counts and success rates. Results with Counts and Rates. Table 11 reports per-task successes and failures, along with the corresponding success rate. Average success is computed ... | p. 18 (Figure/Table caption), p. 8 (5 Experiment) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 However, most existing Vision-Language-Action (VLA) 3를 (3) While KV caching is effective for language decoding within a single query in vision-language models, this technique does not address redundancy in the visual stream, especially in Vision-Language-Action (VLA) models.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Table 11: Real-world results with trial counts and success rates. Results with Counts and Rates. Table 11 reports per-task successes and failures, along with the corresponding success rate. Average success is computed ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To address the inefficiency introduced by repeatedly processing static visual information, we present VLA-Cache, a training-free inference acceleration method that exploits temporal continuity in robotic perception.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model, Robotics`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Table 11: Real-world results with trial counts and success rates. Results with Counts and Rates. Table 11 reports per-task successes and failures, along with the corresponding success rate. Average success is computed ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: (Hz) ↑ PickPot PlaceCube PutSausage WipeTable Average OpenVLA 95.0% 83.3% 80.0% 70.0% 82.1% 1.814 64.16 4.02 + VLA-Cache 90.0% 90.0% 85.0% 73.3% 84.6% 1.303 51.85 4.21 5.4 Results on Real Robot Table ....
3. Compare against the body-reported baseline or a matched simpler baseline: Specifically, we adopt two state-of-the-art token-level acceleration techniques SparseVLM [30] and FastV [29] on OpenVLA as compared methods in the LIBERO benchmark..
4. Report the body metric and its denominator/aggregation: Figure 4: Visualization of VLA-Cache token reuse across settings. (a) LIBERO simulation with OpenVLA. (b) Real-world task under dynamic background. (c) and (d) Main and wrist camera views from OpenVLA-OFT. Blue: static ....
5. Re-run the body-reported ablation/failure condition: Table 10: Varying the relevance threshold τ (with k=100). Overall, efficiency (FLOPs and latency) improves monotonically with larger k and τ, while success rate remains consistently high, corroborating the stability of VLA-Cache ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (3 Methodology), p. 3 (3 Methodology); the primary result is directionally consistent at p. 9 (Figure/Table caption), p. 8 (5 Experiment), p. 9 (5 Experiment); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 address, inefficiency, introduced mechanism이 Specifically, we adopt two state-of-the-art token-level acceleration techniques SparseVLM [30] and FastV [29] on OpenVLA as ... 대비 Figure 4: Visualization of VLA-Cache token reuse across settings. (a) LIBERO simulation with OpenVLA. (b) Real-world task under ...을 개선하고, Table 11: Real-world results with trial counts and success rates. Results with Counts and Rates. Table ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
