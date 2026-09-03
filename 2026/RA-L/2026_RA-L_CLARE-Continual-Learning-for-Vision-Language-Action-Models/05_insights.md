# Insights — CLARE: Continual Learning for Vision-Language-Action Models via Autonomous Adapter Routing and Expansion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2601.09512; PDF retrieval source: https://arxiv.org/pdf/2601.09512. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / IV. METHODOLOGY - extractive body cue:** As our method is architecture-agnostic, we keep the following sections general.
- **p. 5 / IV. METHODOLOGY - extractive body cue:** We found that introducing at least some new parameters per task is essential for the policy to acquire and retain novel skills.
- **p. 3 / IV. METHODOLOGY - extractive body cue:** To achieve this, we draw inspiration from the mixture-of-experts (MoE) approach in large language models (LLMs) [35], [36], which combines the outputs of specialized sub-networks ...
- **p. 3 / IV. METHODOLOGY - extractive body cue:** Prior work [37], [38] has shown that a large fraction of factual associations and high-level knowledge in transformerbased LLMs is stored inside mid-layer feedforward network ...
- **p. 4 / IV. METHODOLOGY - extractive body cue:** By training the discriminators added at stage n with the loss Lrecon(Dn ℓ) = Exℓ∼Dn  en ℓ(xℓ)  , (5) we ensure they have ...
- **p. 4 / IV. METHODOLOGY - extractive body cue:** A straightforward approach would be to Task 1 Adapter Task 3 Adapter Task 1 Discriminator Task 2 Discriminator Task 3 Discriminator Pre-Trained Module z-score threshold ...
- **p. 5 / IV. METHODOLOGY - extractive body cue:** Then, the routing mechanism activates only adapters from earlier stages in layer ℓ1 during training of Ai ℓ2.
- **Contribution anchor:** p. 3 (IV. METHODOLOGY), p. 5 (IV. METHODOLOGY), p. 3 (IV. METHODOLOGY), p. 3 (IV. METHODOLOGY), p. 4 (IV. METHODOLOGY), p. 4 (IV. METHODOLOGY)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** However, state-of-the-art VLAs still cannot adapt reliably to unseen tasks without fine-tuning on task-specific data [6]- [8].
- **p. 1 / I. INTRODUCTION - extractive body cue:** This long-term adaptability, known as continual or lifelong learning [1], remains an open challenge in robotics despite decades of research [2]-[4].
- **p. 3 / III. PROBLEM SETUP - extractive body cue:** Pre-training has provided the base VLA with general visual, language, and action representations, but it cannot solve new tasks zero-shot [6], [7].
- **p. 3 / III. PROBLEM SETUP - extractive body cue:** 17: else 18: Link Dn ℓto an existing adapter via (8).
- **p. 6 / V. EVALUATION - extractive body cue:** In contrast, ER cannot avoid catastrophic forgetting of several tasks (e.g., T1 and T7), yielding an NBT of 23%.
- **p. 7 / 5. LEGO - extractive body cue:** SeqFFT and SeqLoRA achieve high performance on new tasks, but cannot sufficiently retain the relevant representations from previous tasks.
- **p. 7 / V. EVALUATION - extractive body cue:** 5: Increasing the dynamic expansion threshold γ reduces the number of added adapters and, consequently, the capability to learn new tasks (lower FWT), but does ...
- **Boundary to test:** In contrast, ER cannot avoid catastrophic forgetting of several tasks (e.g., T1 and T7), yielding an NBT of 23%.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | As our method is architecture-agnostic, we keep the following sections general. | p. 3 (IV. METHODOLOGY), p. 5 (IV. METHODOLOGY) |
| Reported outcome | Fig. 8: Success rate curves of CLARE and five baselines on the LIBERO-Long benchmark. The solid lines represent the average success rates across three random seeds, and the shaded regions indicate the ... | p. 10 (Figure/Table caption), p. 6 (V. EVALUATION) |
| Failure/limitation | In contrast, ER cannot avoid catastrophic forgetting of several tasks (e.g., T1 and T7), yielding an NBT of 23%. | p. 6 (V. EVALUATION), p. 7 (5. LEGO) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 23: Train Dn ℓof all layers ℓ∈E from Dn via (5). consisting of camera images I1 t , . . . , INc t , proprioceptive state qt and language command l, ...를 We assume the availability of a base VLA policy π0 = πθ0 with model parameters θ0 that takes as input an observation ot = (I1 t , . . . , INc ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 In contrast, ER cannot avoid catastrophic forgetting of several tasks (e.g., T1 and T7), yielding an NBT of 23%.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: As our method is architecture-agnostic, we keep the following sections general.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In contrast, ER cannot avoid catastrophic forgetting of several tasks (e.g., T1 and T7), yielding an NBT of 23%.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We pre-train the policy on a mix of 1000 demonstrations collected in our lab for tasks different from the five continual learning tasks and 2000 episodes from the DROID dataset [9]..
3. Compare against the body-reported baseline or a matched simpler baseline: 5) Baselines: We include seven baselines for continual learning without oracle task IDs..
4. Report the body metric and its denominator/aggregation: Fig. 8: Success rate curves of CLARE and five baselines on the LIBERO-Long benchmark. The solid lines represent the average success rates across three random seeds, and the shaded regions indicate the ....
5. Re-run the body-reported ablation/failure condition: Fig. 1: CLARE autonomously and continually injects lightweight adapters into selected layers of a pre-trained vision-language-action model (VLA). During inference, the most relevant adapters are activated based on feature similarity, ca ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (IV. METHODOLOGY), p. 3 (IV. METHODOLOGY), p. 4 (IV. METHODOLOGY); the primary result is directionally consistent at p. 10 (Figure/Table caption), p. 6 (V. EVALUATION), p. 6 (V. EVALUATION); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 architecture-agnostic, keep, following mechanism이 5) Baselines: We include seven baselines for continual learning without oracle task IDs. 대비 Fig. 8: Success rate curves of CLARE and five baselines on the LIBERO-Long benchmark. The solid lines represent ...을 개선하고, In contrast, ER cannot avoid catastrophic forgetting of several tasks (e.g., T1 and T7), yielding an ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
