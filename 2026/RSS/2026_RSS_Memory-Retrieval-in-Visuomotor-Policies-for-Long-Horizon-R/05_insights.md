# Insights — Memory Retrieval in Visuomotor Policies for Long-Horizon Robot Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://roboticsconference.org/program/papers/10/; PDF retrieval source: https://roboticsconference.org/program/papers/10/. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** To address these challenges, we propose HALO: HistoryAware visuomotor policy for LOng-horizon robotic imitation learning.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Across these settings, we show that VQA-induced task priors provide a general solution, improving absolute task success by 7% on average across diverse tasks and ...
- **p. 1 / Abstract - extractive body cue:** To address both challenges, we introduce HALO, a visuomotor policy with an attention-based memory retrieval mechanism for long-horizon control.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This motivates the development of a general memory retrieval mechanism that can be learned end-to-end, rather than tailored to individual tasks or modalities [6]-[9].
- **p. 4 / III. HALO - extractive body cue:** For VQA supervision, the policy backbone is conditioned on the encoded history Mt, the current observation embedding xt, and the question u, and the answer ...
- **p. 4 / III. HALO - extractive body cue:** Motor Action Reducing Model Drift via Sparsification Text Instruction OR Task Instruction Robot Trajectory Text Query Text Answer Put all breads in microwave How many ...
- **p. 3 / III. HALO - extractive body cue:** First, because attention aggregates information from all stored history Mt, the policy may attend to task-irrelevant details and incorporate them into decision-making, leading to spurious ...
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 4 (III. HALO), p. 4 (III. HALO)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** However, directly applying attention-based memory retrieval to long-horizon robotic imitation learning via offline data exposes two fundamental challenges.
- **p. 2 / I. INTRODUCTION - extractive body cue:** HALO learns to retrieve diverse forms of task-relevant information from history, guided by priors distilled from vision-language foundation models. observations can amplify this effect, as ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To address these challenges, we propose HALO: HistoryAware visuomotor policy for LOng-horizon robotic imitation learning.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Long-horizon household tasks require robots to act on information no longer present in the current sensory input.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** These results support our hypothesis that HALO reduces model drift (fewer manipulation failures)
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** In addition, we measure manipulation and memory failures in real-world evaluations, finding that HALO reduces them by 8% and 25% absolute over full attention in ...
- **p. 8 / IV. EXPERIMENTS - extractive body cue:** Method Retrieve Object Return to Container LSTM 0.14 0.12 Mamba 0.20 0.18 TransformerXL 0.12 0.20 Window Attention 0.13 0.16 Strided Attention 0.20 0.28 Hierarchical Attention ...
- **Boundary to test:** Fig. 2. HALO learns to retrieve diverse forms of task-relevant information from history, guided by priors distilled from vision-language foundation models. observations can amplify this effect, as the policy repeatedly attends to ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To address these challenges, we propose HALO: HistoryAware visuomotor policy for LOng-horizon robotic imitation learning. | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Reported outcome | Cotraining VQA and action prediction achieves 64% success, outperforming pretrain-then-finetune (44%) and no-VQA training (42%) by 20 and 22 points, respectively. | p. 8 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Failure/limitation | Fig. 2. HALO learns to retrieve diverse forms of task-relevant information from history, guided by priors distilled from vision-language foundation models. observations can amplify this effect, as the policy repeatedly attends to ... | p. 2 (Figure/Table caption), p. 7 (IV. EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `observation, uncertainty/risk estimate와 task command → safe set, recovery state 또는 constraint margin → shielded, recovery 또는 safe action`.
- 이 논문의 재사용 가능한 지점은 We parameterize the visuomotor policy πθ(at / τt, l) with three main components: (i) modality-specific encoders consisting of an observation encoder gobs θ and an action encoder gact θ , which map ...를 Given Mt, the current embedding xt, and the task instruction l, the policy backbone fθ produces a latent state zt = fθ(Mt, xt, l), This latent state is passed to two prediction ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 safe set, recovery state 또는 constraint margin가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Fig. 2. HALO learns to retrieve diverse forms of task-relevant information from history, guided by priors distilled from vision-language foundation models. observations can amplify this effect, as the policy repeatedly attends to ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To address these challenges, we propose HALO: HistoryAware visuomotor policy for LOng-horizon robotic imitation learning.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `World models, safety, uncertainty, and recovery`; tags: `Robotics, VLA, memory, long horizon, partial observability, Imitation Learning, retrieval`.
- **Reading predecessor in the generated track queue:** Temporal Difference Calibration in Sequential Tasks: Application to Vision-Language-Action Models (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Demonstrating ViSafe: Vision-enabled Safety for High-speed Detect and Avoid (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Fig. 2. HALO learns to retrieve diverse forms of task-relevant information from history, guided by priors distilled from vision-language foundation models. observations can amplify this effect, as the policy repeatedly attends to ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: In addition, we measure manipulation and memory failures in real-world evaluations, finding that HALO reduces them by 8% and 25% absolute over full attention in the ‘Retrieve Object' task, respectively..
3. Compare against the body-reported baseline or a matched simpler baseline: (Table II) We observe a similar trend in real-world settings, where HALO consistently outperforms the standard Transformer baseline by 19%..
4. Report the body metric and its denominator/aggregation: A moderate value (k = 8) achieves the best performance (52% success)..
5. Re-run the body-reported ablation/failure condition: We compare HALO against a variant trained without VQA supervision..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (III. HALO), p. 4 (III. HALO), p. 3 (III. HALO); the primary result is directionally consistent at p. 8 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 address, challenges, HALO mechanism이 (Table II) We observe a similar trend in real-world settings, where HALO consistently outperforms the standard ... 대비 A moderate value (k = 8) achieves the best performance (52% success).을 개선하고, Fig. 2. HALO learns to retrieve diverse forms of task-relevant information from history, guided by priors ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
