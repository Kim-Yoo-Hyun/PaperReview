# Insights — RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=yAzN4tz7oI; PDF retrieval source: https://openreview.net/pdf/29d56379d000b8c0e05906c5958e67e2e870ab0c.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this paper, we introduce the Robotics Diffusion Transformer (RDT), the largest bimanual manipulation foundation model with strong generalizability.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To further enable training RDT on heterogeneous data, we propose the Physically Interpretable Unified Action Space, a unified action format for various robots with gripper ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Developing bimanual manipulation foundation models confronts the dual challenges of data scarcity and architectural limitations.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Following the success in natural language processing (Achiam et al., 2023; Touvron et al., 2023) and computer vision (Radford et al., 2021; Kirillov et al., ...
- **p. 1 / ABSTRACT - extractive body cue:** Bimanual manipulation is essential in robotics, yet developing foundation models is extremely challenging due to the inherent complexity of coordinating two robot arms (leading to ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** First, the doubled action space induces multi-modal action distributions (Li, 2006; Jia et al., 2024) (see Fig.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Compared with unimanual manipulation, bimanual manipulation has more possible action modes, leading to stronger multi-modality.
- **Contribution anchor:** p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 1 (1 INTRODUCTION)

### Strongest assumption and failure boundary

- **p. 1 / 1 INTRODUCTION - extractive body cue:** Developing bimanual manipulation foundation models confronts the dual challenges of data scarcity and architectural limitations.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, current approaches either depend on task-specific primitives (Mirrazavi Salehian et al., 2017; Rakita et al., 2019; Grannen et al., 2023a) or are limited to ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Existing solutions either discard robots with structural inconsistencies or retain only cross-robot invariant features (Brohan et al., 2023; Ghosh et al., 2023; Shah et al., ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** For scalability, we harness the Transformer backbone and carefully design the multi-modal encoding to eliminate the heterogeneity of various modalities.
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** It probably makes ACT prone to failure.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: (a) Unstable loss curve during training without QKNorm & RMSNorm. (b) Success rates of RDT (w/o MLP Decoder or w/o ACI) in tasks ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** The robot needs to Pick Up Pen (#1), Switch Hand (#2), Drop Pen (#3), and ensure it can Fall into Box (#4).
- **Boundary to test:** It probably makes ACT prone to failure.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this paper, we introduce the Robotics Diffusion Transformer (RDT), the largest bimanual manipulation foundation model with strong generalizability. | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Reported outcome | In Wash Cup and Pour Water, RDT can still achieve a high success rate on unseen scenarios, and its performance is not much different from that on seen ones. | p. 9 (5 EXPERIMENTS), p. 10 (Figure/Table caption) |
| Failure/limitation | It probably makes ACT prone to failure. | p. 10 (5 EXPERIMENTS), p. 6 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** It exhibits zeroshot generalization to unseen objects and scenes, understands and follows language instructions, learns new skills with just 1∼5 demonstrations, and effectively handles complex, dexterous tasks. (p. 1, ABSTRACT).
- **Paper-specific mechanism:** In this paper, we introduce the Robotics Diffusion Transformer (RDT), the largest bimanual manipulation foundation model with strong generalizability. (p. 2, 1 INTRODUCTION).
- **Evidence boundary:** the reported outcome is 5.2 RESULTS ANALYSIS From the results in Table 3, we can see that RDT consistently outperforms other baselines. (p. 9, 5 EXPERIMENTS); the relevant task/metric cue is In Wash Cup and Pour Water, RDT can still achieve a high success rate on unseen scenarios, and its performance is not much different from that on seen ones. (p. 9, 5 EXPERIMENTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** It probably makes ACT prone to failure. (p. 10, 5 EXPERIMENTS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `Robotics, Diffusion`.
- **Reading predecessor in the generated track queue:** Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** It probably makes ACT prone to failure.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: It exhibits zeroshot generalization to unseen objects and scenes, understands and follows language instructions, learns new skills with just 1∼5 demonstrations, and effectively handles complex, dexterous tasks. (p. 1, ABSTRACT); preserve the objective/update rule: The prohibitive costs of dual-arm systems create severe data scarcity (Sharma et al., 2018; Collaboration et al., 2023), fundamentally conflicting with the datahungry nature of foundation models. (p. 1, 1 INTRODUCTION).
2. Use the paper-reported task/data/environment cue: We select 7 challenging tasks to evaluate the generalizability and capabilities of RDT from different dimensions, including complex scenarios that the model may encounter in real-world tasks, such as various ... (p. 7, 5 EXPERIMENTS).
3. Compare against the reported or matched baseline: 5.2 RESULTS ANALYSIS From the results in Table 3, we can see that RDT consistently outperforms other baselines. (p. 9, 5 EXPERIMENTS).
4. Report the body metric with its denominator and aggregation: In Wash Cup and Pour Water, RDT can still achieve a high success rate on unseen scenarios, and its performance is not much different from that on seen ones. (p. 9, 5 EXPERIMENTS).
5. Re-run the reported ablation or stress/failure condition: VARIANT NAME UNSEEN OBJECT UNSEEN SCENE INSTRUCTION FOLLOWING RDT (regress) 12.5 50 12.5 RDT (small) 37.5 62.5 25 RDT (scratch) 0 25 62.5 RDT (ours) 50 62.5 100 Ablation Study. (p. 9, 5 EXPERIMENTS); if none is reported, design one around: It probably makes ACT prone to failure. (p. 10, 5 EXPERIMENTS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), match the reported outcome at p. 9 (5 EXPERIMENTS), p. 9 (Figure/Table caption), p. 10 (Figure/Table caption), and measure the boundary at p. 10 (5 EXPERIMENTS), p. 21 (C PHYSICALLY INTERPRETABLE UNIFIED ACTION SPACE).

## Falsifiable research question

Under the paper's stated interface (It exhibits zeroshot generalization to unseen objects and scenes, understands and follows language instructions, learns new skills with just 1∼5 demonstrations, and ...), does the paper-specific mechanism (In this paper, we introduce the Robotics Diffusion Transformer (RDT), the largest bimanual manipulation foundation model with strong generalizability.) retain the reported evaluation outcome (In Wash Cup and Pour Water, RDT can still achieve a high success rate on unseen scenarios, and ...) when tested against the paper's strongest explicit boundary (It probably makes ACT prone to failure.)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (In Wash Cup and Pour Water, RDT can still achieve a high success rate on unseen scenarios, and ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (28 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** In this paper, we introduce the Robotics Diffusion Transformer (RDT), the largest bimanual manipulation foundation model with strong generalizability. (p. 2, 1 INTRODUCTION).
- **Paper-supported outcome:** 5.2 RESULTS ANALYSIS From the results in Table 3, we can see that RDT consistently outperforms other baselines. (p. 9, 5 EXPERIMENTS).
- **Strongest explicit boundary:** It probably makes ACT prone to failure. (p. 10, 5 EXPERIMENTS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
