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

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 It exhibits zeroshot generalization to unseen objects and scenes, understands and follows language instructions, learns new skills with just 1∼5 demonstrations, and effectively handles complex, dexterous tasks.를 To further enable training RDT on heterogeneous data, we propose the Physically Interpretable Unified Action Space, a unified action format for various robots with gripper arms.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 It probably makes ACT prone to failure.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this paper, we introduce the Robotics Diffusion Transformer (RDT), the largest bimanual manipulation foundation model with strong generalizability.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `Robotics, Diffusion`.
- **Reading predecessor in the generated track queue:** Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** It probably makes ACT prone to failure.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We aim to answer the following questions through real-robot experiments: Q1: Can RDT zero-shot generalize to unseen objects and scenes?.
3. Compare against the body-reported baseline or a matched simpler baseline: 5.2 RESULTS ANALYSIS From the results in Table 3, we can see that RDT consistently outperforms other baselines..
4. Report the body metric and its denominator/aggregation: In Wash Cup and Pour Water, RDT can still achieve a high success rate on unseen scenarios, and its performance is not much different from that on seen ones..
5. Re-run the body-reported ablation/failure condition: VARIANT NAME UNSEEN OBJECT UNSEEN SCENE INSTRUCTION FOLLOWING RDT (regress) 12.5 50 12.5 RDT (small) 37.5 62.5 25 RDT (scratch) 0 25 62.5 RDT (ours) 50 62.5 100 Ablation Study..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT); the primary result is directionally consistent at p. 9 (5 EXPERIMENTS), p. 10 (Figure/Table caption), p. 9 (5 EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 introduce, Robotics, Diffusion mechanism이 5.2 RESULTS ANALYSIS From the results in Table 3, we can see that RDT consistently outperforms ... 대비 In Wash Cup and Pour Water, RDT can still achieve a high success rate on unseen scenarios, and ...을 개선하고, It probably makes ACT prone to failure. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
