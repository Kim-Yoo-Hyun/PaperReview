# Insights — XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (45 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=JO0IsGJg16; PDF retrieval source: https://arxiv.org/pdf/2511.02776.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are summarized as follows: • We propose X Robotic Model 1 (XR-1), a scalable three-stage framework for VLA learning that effectively leverages ...
- **p. 2 / 1. Introduction - extractive body cue:** Addressing the limitations of unimodal representations and inspired by human supramodal cognition, we propose X Robotic Model 1 (XR-1) to achieve cross-data exploitation and cross-embodiment ...
- **p. 4 / 3.1. Overview - extractive body cue:** We introduce XR-1, a scalable framework for cross-robot VLA learning (Figure 2), structured in three stages.
- **p. 5 / 3.1. Overview - extractive body cue:** To unify both modalities, we introduce a VQ-VAE codebook e ∈Rd×f with d discrete entries of dimension f.
- **p. 5 / 3.1. Overview - extractive body cue:** To mitigate this gap, we introduce an alignment loss that constrains visual codes to remain consistent with their motion counterparts: Lalign = DKL(q(ze mo) ∥q(ze ...
- **p. 4 / 3.1. Overview - extractive body cue:** The motion decoder Dmo(·) then takes the latent motion embedding zmo and optional conditions cd as input, such as the language instruction l, proprioceptive states ...
- **p. 4 / 3.1. Overview - extractive body cue:** At each inference step t, the policy π receives a language instruction l and multimodal observations o = ⟨c, m⟩, where c ∈RK×3×H×W denotes K ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.1. Overview), p. 5 (3.1. Overview), p. 5 (3.1. Overview), p. 4 (3.1. Overview)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** Despite VLM advancements, two challenges persist: (i) Precision Gap: Mapping high-dimensional observations to precise low-level actions is difficult due to multimodal uncertainty; even centimeter-level errors ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, prior research (Cui et al., 2023; Shafiullah et al., 2022; Lee et al., 2024; Xie et al., 2025; Zheng et al., ...
- **p. 9 / 5. Conclusion - extractive body cue:** We presented X Robotic Model 1 (XR-1), a unified framework for versatile and scalable vision-language-action learning that addresses the key limitations of existing approaches: precise ...
- **p. 9 / 4.5. Additional Analyses - extractive body cue:** Failure analyses for baselines and XR-1 are provided in Appendix I and Appendix J, respectively, showing that XR-1 reduces baseline failures such as optimization collapse, ...
- **p. 30 / Figure/Table caption - extractive body cue:** Figure 15. Visualizing UVMC across different embodiments (Dual-Arm Franka and Dual-Arm UR) using t-SNE. an intermediate feature supervision signal, UVMC guides the model to generate ...
- **p. 31 / Figure/Table caption - extractive body cue:** Figure 16. Failure cases of baseline methods. Miss Miss Drop XR-1 Precision Deficiency: TK2-CollectScrews
- **p. 31 / Figure/Table caption - extractive body cue:** Figure 17. Failure Cases of XR-1. • Deformable Object Handling: DFR-HangTowelRack. The robot performs a bimanual manipulation task involving deformable object handling: the right arm ...
- **Boundary to test:** We presented X Robotic Model 1 (XR-1), a unified framework for versatile and scalable vision-language-action learning that addresses the key limitations of existing approaches: precise low-level action generation and crossdomain multimo ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our main contributions are summarized as follows: • We propose X Robotic Model 1 (XR-1), a scalable three-stage framework for VLA learning that effectively leverages heterogeneous data sources, including Internet-scale human videos ... | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | As shown in Figure 7, XR-1 achieves significantly higher success rates than ACT and DP, despite the setting favoring 8 | p. 8 (4.4. Generalization Analysis), p. 8 (4.4. Generalization Analysis) |
| Failure/limitation | We presented X Robotic Model 1 (XR-1), a unified framework for versatile and scalable vision-language-action learning that addresses the key limitations of existing approaches: precise low-level action generation and crossdomain multimo ... | p. 9 (5. Conclusion), p. 9 (4.5. Additional Analyses) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 At each inference step t, the policy π receives a language instruction l and multimodal observations o = ⟨c, m⟩, where c ∈RK×3×H×W denotes K RGB images from external or robot-mounted cameras, ...를 The motion decoder Dmo(·) then takes the latent motion embedding zmo and optional conditions cd as input, such as the language instruction l, proprioceptive states m, and the observations o.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 We presented X Robotic Model 1 (XR-1), a unified framework for versatile and scalable vision-language-action learning that addresses the key limitations of existing approaches: precise low-level action generation and crossdomain multimo ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our main contributions are summarized as follows: • We propose X Robotic Model 1 (XR-1), a scalable three-stage framework for VLA learning that effectively leverages heterogeneous data sources, including Internet-scale human videos ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model, Imitation Learning`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** We presented X Robotic Model 1 (XR-1), a unified framework for versatile and scalable vision-language-action learning that addresses the key limitations of existing approaches: precise low-level action generation and crossdomain multimo ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Unlike the UR-5e, this robot is unseen during pretraining (e.g., Stages 1 and 2 for XR1), making the evaluation a stringent embodiment-transfer benchmark..
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 9. Out-of-box evaluation results of 7 tasks on Dual-Arm UR-5e. Out-of-Box Evaluation. In addition to the evaluation on the Dual-Arm Franka, we also conduct an out-of-box evaluation of XR-1 on the ....
4. Report the body metric and its denominator/aggregation: For evaluation, we conduct 20 rollouts per task and report success rates based on human evaluation..
5. Re-run the body-reported ablation/failure condition: Figure 5. Unseen scenario task setup on Dual-Arm Franka. embodiment performance, are provided in Appendix E. Lightweight Models. To validate the applicability of our methods in resource-constrained environments, we extend our evaluation ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3.1. Overview), p. 4 (3.1. Overview), p. 5 (3.1. Overview); the primary result is directionally consistent at p. 8 (4.4. Generalization Analysis), p. 8 (4.4. Generalization Analysis), p. 7 (4.1. Experiment Setup); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 main, contributions, summarized mechanism이 Figure 9. Out-of-box evaluation results of 7 tasks on Dual-Arm UR-5e. Out-of-Box Evaluation. In addition to ... 대비 For evaluation, we conduct 20 rollouts per task and report success rates based on human evaluation.을 개선하고, We presented X Robotic Model 1 (XR-1), a unified framework for versatile and scalable vision-language-action learning ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
