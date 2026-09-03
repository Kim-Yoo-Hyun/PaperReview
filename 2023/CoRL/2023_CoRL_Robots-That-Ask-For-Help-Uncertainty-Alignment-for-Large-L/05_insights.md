# Insights — Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2307.01928; PDF retrieval source: https://arxiv.org/pdf/2307.01928. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 5 / 1 Introduction - extractive body cue:** Here, we present a novel extension of CP to multi-step settings that tackles this challenge.
- **p. 2 / 1 Introduction - extractive body cue:** We propose KNOWNO- Know When You Don't Know - a framework for aligning the uncertainty of LLM-based planners utilizing the theory of conformal prediction (CP) ...
- **p. 4 / 1 Introduction - extractive body cue:** We introduce CP below, and then present the different practical settings we consider (possibly involving multiple planning steps and/or multiple correct plans per step).
- **p. 5 / 1 Introduction - extractive body cue:** Suppose that each data point consists of a sequence of augmented context x = (˜x0,˜x1,...,˜xT-1) and true labels y = (y0,y1,...,yT-1), where T is the ...
- **p. 6 / 1 Introduction - extractive body cue:** We extend our method and confidence guarantees to this setting for both single- and multi-step problems in Section A3 and Section A4.
- **p. 2 / 1 Introduction - extractive body cue:** Language model planners can generate step-by-step robot plans, where each step y is composed of variable-length sequences of symbols (σ1,σ2,...,σk), e.g., text tokens as input ...
- **p. 3 / 1 Introduction - extractive body cue:** The environment e can be formulated as a partially observable Markov decision process (POMDP): at any given state st at time t, given a user ...
- **Contribution anchor:** p. 5 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction), p. 6 (1 Introduction), p. 2 (1 Introduction)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** However, one of the major challenges with current LLMs is their tendency to hallucinate, i.e., to confidently generate outputs that are plausible but incorrect and ...
- **p. 5 / 1 Introduction - extractive body cue:** However, the original CP formulation cannot be applied here since the context xt between steps are dependent; moreover, the robot's actions at step t influence ...
- **p. 1 / 1 Introduction - extractive body cue:** Accurately modeling and accounting for uncertainty is a longstanding challenge towards robots that operate reliably in unstructured and novel environments.
- **p. 2 / 1 Introduction - extractive body cue:** We formalize these challenges via two desiderata: (i) calibrated confidence: the robot should seek sufficient help to ensure a statistically guaranteed level of task success ...
- **p. 4 / 1 Introduction - extractive body cue:** Overall, CP is a powerful and easy-to-use statistical tool to produce (1) tight coverage guarantees-addressing the goal of calibrated confidence, and (2) small prediction sets ...
- **p. 9 / 6 Discussion - extractive body cue:** Limitations and future work: The primary limitation of our work is that the task completion guarantee assumes environments (objects) are fully grounded in the text ...
- **p. 9 / 6 Discussion - extractive body cue:** Another limitation is that, for the task guarantee to hold, the human needs to faithfully provide help when the robot needs it.
- **Boundary to test:** Limitations and future work: The primary limitation of our work is that the task completion guarantee assumes environments (objects) are fully grounded in the text input to the LLM, and the actions ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Here, we present a novel extension of CP to multi-step settings that tackles this challenge. | p. 5 (1 Introduction), p. 2 (1 Introduction) |
| Reported outcome | Nonetheless, KnowNo still achieves 1-ϵ target success rate, as the coverage guarantee from CP makes no assumption about the LLM confidences (e.g., calibrated or accurate) - KnowNo flexibly compensates for the degraded ... | p. 8 (4 Experiments), p. 2 (Figure/Table caption) |
| Failure/limitation | Limitations and future work: The primary limitation of our work is that the task completion guarantee assumes environments (objects) are fully grounded in the text input to the LLM, and the actions ... | p. 9 (6 Discussion), p. 9 (6 Discussion) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `observation, uncertainty/risk estimate와 task command → safe set, recovery state 또는 constraint margin → shielded, recovery 또는 safe action`.
- 이 논문의 재사용 가능한 지점은 The environment e can be formulated as a partially observable Markov decision process (POMDP): at any given state st at time t, given a user instruction ℓ, the robot executes an action ...를 Language model planners can generate step-by-step robot plans, where each step y is composed of variable-length sequences of symbols (σ1,σ2,...,σk), e.g., text tokens as input to a language-conditioned policy [1] (see Fig.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 safe set, recovery state 또는 constraint margin가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Limitations and future work: The primary limitation of our work is that the task completion guarantee assumes environments (objects) are fully grounded in the text input to the LLM, and the actions ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Here, we present a novel extension of CP to multi-step settings that tackles this challenge.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `World models, safety, uncertainty, and recovery`; tags: `Robotics, LLM planning, uncertainty, conformal prediction, human intervention`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Limitations and future work: The primary limitation of our work is that the task completion guarantee assumes environments (objects) are fully grounded in the text input to the LLM, and the actions ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: In future deployment, we envision that a robot can interact with an end-user (e.g., in a home) to collect a dataset through interactions with the human; the human can provide their true ....
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 1: KNOWNO uses Conformal Prediction (CP) to align the uncertainty of LLM planners. Given a language instruction, an LLM generates possible next steps and its confidences (scores) in these options. CP ....
4. Report the body metric and its denominator/aggregation: 4 we vary the target error rate ϵ and show the curves of task success rate vs. prediction set size and human help rate averaged over the three settings..
5. Re-run the body-reported ablation/failure condition: Lastly, we consider No Help where the option with the highest score is always executed without any human intervention..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction); the primary result is directionally consistent at p. 8 (4 Experiments), p. 2 (Figure/Table caption), p. 7 (4 Experiments); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Here, present, novel mechanism이 Figure 1: KNOWNO uses Conformal Prediction (CP) to align the uncertainty of LLM planners. Given a ... 대비 4 we vary the target error rate ϵ and show the curves of task success rate vs. prediction ...을 개선하고, Limitations and future work: The primary limitation of our work is that the task completion guarantee ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
