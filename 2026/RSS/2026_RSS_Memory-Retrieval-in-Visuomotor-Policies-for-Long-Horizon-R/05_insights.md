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

- **Paper-specific interface:** We parameterize the visuomotor policy πθ(at / τt, l) with three main components: (i) modality-specific encoders consisting of an observation encoder gobs θ and an action encoder gact θ , ... (p. 3, III. HALO).
- **Paper-specific mechanism:** To address these challenges, we propose HALO: HistoryAware visuomotor policy for LOng-horizon robotic imitation learning. (p. 2, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is (Table II) We observe a similar trend in real-world settings, where HALO consistently outperforms the standard Transformer baseline by 19%. (p. 7, IV. EXPERIMENTS); the relevant task/metric cue is A moderate value (k = 8) achieves the best performance (52% success). (p. 8, IV. EXPERIMENTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** These errors introduce noise into the stored representations, which can degrade latent representation quality, leading to model drift and cascading failures over long horizons. (p. 3, III. HALO).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `World models, safety, uncertainty, and recovery`; tags: `Robotics, VLA, memory, long horizon, partial observability, Imitation Learning, retrieval`.
- **Reading predecessor in the generated track queue:** Temporal Difference Calibration in Sequential Tasks: Application to Vision-Language-Action Models (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Demonstrating ViSafe: Vision-enabled Safety for High-speed Detect and Avoid (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Fig. 2. HALO learns to retrieve diverse forms of task-relevant information from history, guided by priors distilled from vision-language foundation models. observations can amplify this effect, as the policy repeatedly attends to ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: We parameterize the visuomotor policy πθ(at / τt, l) with three main components: (i) modality-specific encoders consisting of an observation encoder gobs θ and an action encoder gact θ , ... (p. 3, III. HALO); preserve the objective/update rule: Concretely, it generates task-relevant, memory-dependent question-answer pairs from demonstration trajectories and trains the policy jointly with a video questionanswering objective, transferring VLM priors to the visuomotor policy. (p. 1, Abstract).
2. Use the paper-reported task/data/environment cue: In addition, we measure manipulation and memory failures in real-world evaluations, finding that HALO reduces them by 8% and 25% absolute over full attention in the ‘Retrieve Object' task, respectively. (p. 7, IV. EXPERIMENTS).
3. Compare against the reported or matched baseline: (Table II) We observe a similar trend in real-world settings, where HALO consistently outperforms the standard Transformer baseline by 19%. (p. 7, IV. EXPERIMENTS).
4. Report the body metric with its denominator and aggregation: A moderate value (k = 8) achieves the best performance (52% success). (p. 8, IV. EXPERIMENTS).
5. Re-run the reported ablation or stress/failure condition: We compare HALO against a variant trained without VQA supervision. (p. 8, IV. EXPERIMENTS); if none is reported, design one around: These errors introduce noise into the stored representations, which can degrade latent representation quality, leading to model drift and cascading failures over long horizons. (p. 3, III. HALO).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), match the reported outcome at p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), and measure the boundary at p. 3 (III. HALO), p. 7 (IV. EXPERIMENTS).

## Falsifiable research question

Under the paper's stated interface (We parameterize the visuomotor policy πθ(at / τt, l) with three main components: (i) modality-specific encoders consisting of an observation encoder gobs ...), does the paper-specific mechanism (To address these challenges, we propose HALO: HistoryAware visuomotor policy for LOng-horizon robotic imitation learning.) retain the reported evaluation outcome (A moderate value (k = 8) achieves the best performance (52% success).) when tested against the paper's strongest explicit boundary (These errors introduce noise into the stored representations, which can degrade latent representation quality, leading to model drift ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (A moderate value (k = 8) achieves the best performance (52% success).) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (10 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** To address these challenges, we propose HALO: HistoryAware visuomotor policy for LOng-horizon robotic imitation learning. (p. 2, I. INTRODUCTION).
- **Paper-supported outcome:** (Table II) We observe a similar trend in real-world settings, where HALO consistently outperforms the standard Transformer baseline by 19%. (p. 7, IV. EXPERIMENTS).
- **Strongest explicit boundary:** These errors introduce noise into the stored representations, which can degrade latent representation quality, leading to model drift and cascading failures over long horizons. (p. 3, III. HALO).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
