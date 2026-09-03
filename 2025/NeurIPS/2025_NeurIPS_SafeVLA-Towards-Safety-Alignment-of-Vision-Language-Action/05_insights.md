# Insights — SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (39 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=dt940loCBT; PDF retrieval source: https://proceedings.neurips.cc/paper_files/paper/2025/file/e185c7be603426028c32ae1003a59d78-Paper-Conference.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** Our study details how these interconnected aspects contribute to a more holistic safety alignment. • Environment: Addressing the gap in comprehensive VLA safety assessment, we ...
- **p. 2 / 1 Introduction - extractive body cue:** Our main contributions are: • Integrated Safety Approach (ISA) Exploration: We conduct a comprehensive investigation into an ISA for VLA safety alignment.
- **p. 1 / 1 Introduction - extractive body cue:** Embodied AI aims to develop a generalist policy that can perform perception, interaction, reasoning, and adaptation in the physical world [1].
- **p. 33 / C.3 Model Selection - extractive body cue:** 2) Long-Horizon Reasoning: The 100-frame transformer context window (Table 6 in SPOC) allows modeling temporal dependencies critical for anticipating and avoiding cumulative safety risks during ...
- **p. 32 / C.3 Model Selection - extractive body cue:** 3) Action Decoder: A causal transformer decoder with 100-step context windows predicts discrete actions by attending to historical observations and actions.
- **p. 33 / C.3 Model Selection - extractive body cue:** We use AllenAct [85] and OmniSafe [39] as the training framework.
- **p. 32 / C.3 Model Selection - extractive body cue:** 2) Visual Encoder: A goal-conditioned transformer encoder fuses RGB observations from dual cameras (navigation and manipulation views) with language embeddings, enabling cross-modal fusion.
- **Contribution anchor:** p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 33 (C.3 Model Selection), p. 32 (C.3 Model Selection), p. 33 (C.3 Model Selection)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** However, these safety mechanisms cannot be directly applied to VLAs, as there is a substantial gap between the abstract safety concerns at the model intention ...
- **p. 1 / 1 Introduction - extractive body cue:** While significant progress has been made in task performance, the explicit integration of safety mechanisms remains an open challenge.
- **p. 2 / 1 Introduction - extractive body cue:** To tackle this challenge, we make the first systematic explorations into VLA safety alignment.
- **p. 2 / 1 Introduction - extractive body cue:** This fundamental limitation motivates an urgent need to explore methodologies capable of explicitly embedding safety constraints into the VLAs [36, 37].
- **p. 3 / 1 Introduction - extractive body cue:** high-risk actions and a drastic reduction in unsafe incident severity; and (III) robust generalization of learned safety behaviors to out-of-distribution (OOD) perturbations.
- **p. 26 / Figure/Table caption - extractive body cue:** Figure 11: Qualitative comparison of ISA-aligned VLA and unaligned VLA behaviors. Left: Trajectory comparison for a representative task. The ISA-aligned VLA exhibits a smoother, more ...
- **p. 10 / 6 Conclusion - extractive body cue:** Crucially, aligned policies showed robust safety assurance, mitigating long-tail risks and generalizing to out-of-distribution perturbations and extreme failures, marking a first systematic integration of explicit ...
- **Boundary to test:** Figure 11: Qualitative comparison of ISA-aligned VLA and unaligned VLA behaviors. Left: Trajectory comparison for a representative task. The ISA-aligned VLA exhibits a smoother, more direct path, while the unaligned VLA shows ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our study details how these interconnected aspects contribute to a more holistic safety alignment. • Environment: Addressing the gap in comprehensive VLA safety assessment, we introduce Safety-CHORES. | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Reported outcome | Figure 5: Comparative performance of VLA models on multiple benchmarks. Left: SR of each model per benchmark. Right: CC incurred by each model on these benchmarks. demonstrates substantial safety improvements, achieving an ... | p. 8 (Figure/Table caption), p. 9 (5 Experiments) |
| Failure/limitation | Figure 11: Qualitative comparison of ISA-aligned VLA and unaligned VLA behaviors. Left: Trajectory comparison for a representative task. The ISA-aligned VLA exhibits a smoother, more direct path, while the unaligned VLA shows ... | p. 26 (Figure/Table caption), p. 10 (6 Conclusion) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 The reward rt is a function of the current state st and the language instruction l: rt = r(st+1/st, at, l) (4) The total immediate cost ct is an aggregation of K ...를 At each time step t, the policy considers a temporal context window defined by ht = {(ot-n, at-n), (ot-n+1, at-n+1), . . . , (ot-1, at-1), ot}, which contains the history of ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 11: Qualitative comparison of ISA-aligned VLA and unaligned VLA behaviors. Left: Trajectory comparison for a representative task. The ISA-aligned VLA exhibits a smoother, more direct path, while the unaligned VLA shows ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our study details how these interconnected aspects contribute to a more holistic safety alignment. • Environment: Addressing the gap in comprehensive VLA safety assessment, we introduce Safety-CHORES.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 11: Qualitative comparison of ISA-aligned VLA and unaligned VLA behaviors. Left: Trajectory comparison for a representative task. The ISA-aligned VLA exhibits a smoother, more direct path, while the unaligned VLA shows ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: 0.0 0.2 0.4 0.6 0.8 1.0 +0.031 -0.038 +0.067 -0.011 Safety-CHORES - SR 0 10 20 30 40 =-23.95 =-36.06 =-26.50 =-29.97 Safety-CHORES - CC 0.0 0.2 0.4 0.6 0.8 1.0 +0.064 ....
3. Compare against the body-reported baseline or a matched simpler baseline: ISA achieves an average SR increase of 3.85% compared to FLaRe, outperforming IL-only baselines and matching or exceeding other RL-based methods..
4. Report the body metric and its denominator/aggregation: 0.00 0.25 0.50 0.75 1.00 Success Rate EmbCLIP 0.00 0.25 0.50 0.75 1.00 Success Rate Embodied-Codebook 0.00 0.25 0.50 0.75 1.00 Success Rate EmbCLIP-DINOv2 0.00 0.25 0.50 0.75 1.00 Success Rate Embodied-Codebook-DINOv2 ....
5. Re-run the body-reported ablation/failure condition: 0.86 0.64 0.75 1.85 5.01 4.75 0.00 0.25 0.50 0.75 1.00 0 1 2 3 4 5 ISA ISA without eliciting FLaRe-RS SR 0.82 0.86 0.87 1.16 1.85 5.91 0.00 0.25 0.50 ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 32 (C.3 Model Selection), p. 33 (C.3 Model Selection), p. 32 (C.3 Model Selection); the primary result is directionally consistent at p. 8 (Figure/Table caption), p. 9 (5 Experiments), p. 8 (5 Experiments); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 study, details, interconnected mechanism이 ISA achieves an average SR increase of 3.85% compared to FLaRe, outperforming IL-only baselines and matching ... 대비 0.00 0.25 0.50 0.75 1.00 Success Rate EmbCLIP 0.00 0.25 0.50 0.75 1.00 Success Rate Embodied-Codebook 0.00 0.25 ...을 개선하고, Figure 11: Qualitative comparison of ISA-aligned VLA and unaligned VLA behaviors. Left: Trajectory comparison for a ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
