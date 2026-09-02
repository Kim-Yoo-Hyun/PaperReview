# Insights — Evaluating Real-World Robot Manipulation Policies in Simulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=LZh48DTg71; PDF retrieval source: https://arxiv.org/pdf/2405.05941.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, our contributions are as follows: • We introduce SIMPLER, a suite of simulated evaluation environments for commonly-used real robot manipulation setups. • We ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose simulated evaluation as a possible answer, in which manipulation policies trained on real data are evaluated in purpose-built simulated environments ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** 2: We introduce SIMPLER, a suite of open-source simulated evaluation environments for common real robot manipulation setups, namely the Google Robot evaluations from the RT-series ...
- **p. 1 / Abstract - extractive body cue:** We then employ these approaches to create SIMPLER, a collection of simulated environments for manipulation policy evaluation on common real robot setups.
- **p. 2 / I. INTRODUCTION - extractive body cue:** As such, SIMPLER is a first step towards using simulated evaluation as a tool for reliable, scalable, and reproducible manipulation policy evaluation.
- **p. 1 / I. INTRODUCTION - extractive body cue:** These advances are underpinned by large-scale datasets [11, 66] and expressive models [1, 6, 29].
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (Abstract), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)

### Strongest assumption and failure boundary

- **p. 2 / I. INTRODUCTION - extractive body cue:** However, performing simulated evaluations for robotic manipulation poses additional challenges due to the diverse interactions between agent and environment.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This underlines a growing challenge in robot manipulation research: as we scale the capabilities of robot policies, how do we correspondingly scale our ability to ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Through extensive experiments, we examine the challenges of building effective simulated evaluation pipelines: from control disparities to visual disparities between real and simulated environments.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Illustration of Mean Maximum Rank Violation (MMRV, range [0, 1], lower is better) and Pearson correlation coefficient (Pearson r, range [-1, 1], higher ...
- **p. 10 / VII. CONCLUSION - extractive body cue:** Our current set of environments has several limitations.
- **p. 10 / VII. CONCLUSION - extractive body cue:** Additionally, we demonstrate that SIMPLER evaluations accurately capture finegrained characteristics of real-world policies beyond average performance, such as their robustness to various distribution shifts.
- **p. 8 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** We evaluate two RT-1 checkpoints with different robustness behaviors to distribution shifts.
- **Boundary to test:** Fig. 3: Illustration of Mean Maximum Rank Violation (MMRV, range [0, 1], lower is better) and Pearson correlation coefficient (Pearson r, range [-1, 1], higher is better) for assessing the correlation between ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, our contributions are as follows: • We introduce SIMPLER, a suite of simulated evaluation environments for commonly-used real robot manipulation setups. • We address the challenges inherent in simulated manipulation ... | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Reported outcome | Thus, the approaches we introduced in Section IV-B for narrowing the visual gap between simulated and real scene can significantly improve real-andsim evaluation performance correlation, but only if applied jointly and to ... | p. 10 (2) Can simulated evaluations not only capture the perfor), p. 7 (2) Can simulated evaluations not only capture the perfor) |
| Failure/limitation | Fig. 3: Illustration of Mean Maximum Rank Violation (MMRV, range [0, 1], lower is better) and Pearson correlation coefficient (Pearson r, range [-1, 1], higher is better) for assessing the correlation between ... | p. 4 (Figure/Table caption), p. 10 (VII. CONCLUSION) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `standardized observation, action, task state와 evaluation split → benchmark state/goal와 method decision → policy/controller trajectory 또는 measured result`.
- 이 논문의 재사용 가능한 지점은 Simulated Manipulation Policy Evaluation for Real Robot Setups SIMPLER Pick Coke Can Move Near Open/Close Drawer Put Object in Drawer Google Robot Put Carrot on Plate Stack Cubes Put Eggplant in Basket ...를 We then propose and evaluate approaches for mitigating these differences based on offline system identification, "green-screening" simulation observations using realworld backgrounds, and object texture baking from real-world images.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 benchmark state/goal와 method decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Fig. 3: Illustration of Mean Maximum Rank Violation (MMRV, range [0, 1], lower is better) and Pearson correlation coefficient (Pearson r, range [-1, 1], higher is better) for assessing the correlation between ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary, our contributions are as follows: • We introduce SIMPLER, a suite of simulated evaluation environments for commonly-used real robot manipulation setups. • We address the challenges inherent in simulated manipulation ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Benchmark, simulation, real-to-sim, policy evaluation, generalist policy`.
- **Reading predecessor in the generated track queue:** Any-point Trajectory Modeling for Policy Learning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Benchmarking Knowledge Transfer for Lifelong Robot Learning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Fig. 3: Illustration of Mean Maximum Rank Violation (MMRV, range [0, 1], lower is better) and Pearson correlation coefficient (Pearson r, range [-1, 1], higher is better) for assessing the correlation between ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Models that obtain low real-world performance, such as RT1 (Begin) on Google Robot tasks and RT-1-X on BridgeData V2 tasks, similarly have low performance in SIMPLER evaluations in simulation..
3. Compare against the body-reported baseline or a matched simpler baseline: Furthermore, "Visual Matching" (VisMatch) outperforms "Variant Aggregation" (VarAgg)..
4. Report the body metric and its denominator/aggregation: For Octo simulated evaluations, since the model involves a non-deterministic diffusion head, we average its success rates across three different random seeds to produce a lowervariance estimate of the policy's simulation performance..
5. Re-run the body-reported ablation/failure condition: Fig. 8: Change in success rate under various distribution shifts for two RT-1 policies trained without and with data augmentation. Success rates are averaged across Google Robot "Pick Coke Can" and "Move ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (I. INTRODUCTION), p. 1 (Abstract), p. 2 (I. INTRODUCTION); the primary result is directionally consistent at p. 10 (2) Can simulated evaluations not only capture the perfor), p. 7 (2) Can simulated evaluations not only capture the perfor), p. 7 (2) Can simulated evaluations not only capture the perfor); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, contributions, follows mechanism이 Furthermore, "Visual Matching" (VisMatch) outperforms "Variant Aggregation" (VarAgg). 대비 For Octo simulated evaluations, since the model involves a non-deterministic diffusion head, we average its success rates across ...을 개선하고, Fig. 3: Illustration of Mean Maximum Rank Violation (MMRV, range [0, 1], lower is better) and ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
