# Insights — SPA: 3D Spatial-Awareness Enables Effective Embodied Representation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=6TLdqAZgzn; PDF retrieval source: https://openreview.net/pdf/69efa7c1cd34c4e72171331a81f56b7c914e9e24.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our contribution can be summarized as follows. • We propose a significant spatial hypothesis: 3D spatial awareness is crucial for embodied representation learning.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our experiments provide clear evidence for the hypothesis. • We introduce SPA, a novel paradigm for representation learning in embodied AI.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** In this paper, we introduce SPA, a general 3D spatial-aware representation learning framework for embodied AI.
- **p. 3 / 2 METHODOLOGY - extractive body cue:** Unlike the bird's-eye view (BEV) construction in autonomous driving (Li et al., 2022), which usually relies on a fixed scene range around ego vehicle , ...
- **p. 4 / 2 METHODOLOGY - extractive body cue:** Our framework has the capability to distill knowledge from multiple vision foundation models by adding multiple rendering heads.
- **p. 3 / 2 METHODOLOGY - extractive body cue:** Finally, we explain the image rendering from the feature volume and loss functions for network optimization in Sec.
- **p. 3 / 2 METHODOLOGY - extractive body cue:** We then unpatchify them to obtain a latent feature map of size H P × W P , where P is the ViT patch size.
- **Contribution anchor:** p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 3 (2 METHODOLOGY), p. 4 (2 METHODOLOGY), p. 3 (2 METHODOLOGY)

### Strongest assumption and failure boundary

- **p. 1 / 1 INTRODUCTION - extractive body cue:** This limitation arises from their primary emphasis on 2D semantic understanding, which, though valuable, is still insufficient for the sophisticated spatial reasoning required in embodied ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Existing visual representation learning methods for embodied AI (Nair et al., 2022; Radosavovic et al., 2023; Majumdar et al., 2023; Karamcheti et al., 2023; Shang ...
- **p. 22 / C.1 DATASET DETAILS - extractive body cue:** Since Droid does not provide depth data, we utilize Croco-Stereo Weinzaepfel et al.
- **p. 22 / C.2 PRE-TRAINING DETAILS - extractive body cue:** This initialization does not affect the validity of our conclusions, as demonstrated by the ablation study of SPA-MAE in Sec.
- **p. 24 / C.2 PRE-TRAINING DETAILS - extractive body cue:** Simple multiview attention-based interaction, as used in MV-MAE, does not perform as effectively in learning 3D spatial awareness.
- **p. 7 / Figure/Table caption - extractive body cue:** Tab. 3. For detailed results on each task and each random seed, please refer to Appendix D. We also have visualized the performance radar chart ...
- **Boundary to test:** Since Droid does not provide depth data, we utilize Croco-Stereo Weinzaepfel et al.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our contribution can be summarized as follows. • We propose a significant spatial hypothesis: 3D spatial awareness is crucial for embodied representation learning. | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Reported outcome | Tab. 3. For detailed results on each task and each random seed, please refer to Appendix D. We also have visualized the performance radar chart and the per-task rank distributions in Fig. ... | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Failure/limitation | Since Droid does not provide depth data, we utilize Croco-Stereo Weinzaepfel et al. | p. 22 (C.1 DATASET DETAILS), p. 22 (C.2 PRE-TRAINING DETAILS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 In this section, we first describe our process for handling multi-view image inputs and feature extraction in Sec.를 2.1 INPUT PROCESS AND FEATURE EXTRACTION Given a set of multi-view images I = {I1, I2, . . . , IN}, where each Ii ∈R3×H×W and N ∈Z+, we utilize a 2D ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Since Droid does not provide depth data, we utilize Croco-Stereo Weinzaepfel et al.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our contribution can be summarized as follows. • We propose a significant spatial hypothesis: 3D spatial awareness is crucial for embodied representation learning.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `Robotics, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Since Droid does not provide depth data, we utilize Croco-Stereo Weinzaepfel et al.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: (14) F REAL-WORLD EXPERIMENT DETAILS Our real-world hardware setup is based on the open-source Low-Cost-Robot project (Koch, 2024)..
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 4: Correlation between mean success rate and camera pose regression error. 5.2 ADDITIONAL COMPARISONS (Q1) We primarily compare with SOTA methods using the ViT-L backbone, which is commonly available and pre-trained ....
4. Report the body metric and its denominator/aggregation: Meta-World RL Task Method (ViT-B) Success Rate Episode Reward button-press-topdown-v2 CLIP 0.93 653.97 DINOv2 1.00 746.04 MAE 0.46 517.54 MoCoV3 0.99 749.93 SPA (Ours) 1.00 778.47 hammer-v2 CLIP 0.00 401.41 DINOv2 0.67 ....
5. Re-run the body-reported ablation/failure condition: Table 6: Additional ablations on VC-1. Methods SPA-B SPA-MAE RADIO E-RADIO VC-1 AD.
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (2 METHODOLOGY), p. 3 (2 METHODOLOGY), p. 22 (C.2 PRE-TRAINING DETAILS); the primary result is directionally consistent at p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 contribution, summarized, follows mechanism이 Figure 4: Correlation between mean success rate and camera pose regression error. 5.2 ADDITIONAL COMPARISONS (Q1) ... 대비 Meta-World RL Task Method (ViT-B) Success Rate Episode Reward button-press-topdown-v2 CLIP 0.93 653.97 DINOv2 1.00 746.04 MAE 0.46 ...을 개선하고, Since Droid does not provide depth data, we utilize Croco-Stereo Weinzaepfel et al. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
