# Insights — 3D Equivariant Visuomotor Policy Learning via Spherical Projection

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=kXJd4JxF34; PDF retrieval source: https://arxiv.org/pdf/2505.16969.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** Our key contributions are summarized as follows: • We introduce Image-to-Sphere Policy (ISP), the first SO(3)-equivariant policy learning framework that uses spherical projection from 2D ...
- **p. 1 / 1 Introduction - extractive body cue:** g Figure 1: We propose the first SO(3)-equivariant policy learning framework based on a single eyein-hand RGB image, where the predicted action sequence transforms equivariantly ...
- **p. 2 / 1 Introduction - extractive body cue:** Our method first projects features extracted from 2D RGB observations onto a sphere and then rotates the resulting spherical signal to compensate for camera motion.
- **p. 4 / 4 Method - extractive body cue:** The observation x ∈X consists of two parts, an eye-in-hand RGB image I, that captures visual information, and proprioceptive data, P ∈R7, including the end-effector's ...
- **p. 6 / 4 Method - extractive body cue:** 4.3 End-to-End Symmetry Analysis In this section, we analyze the equivariant properties of our method.
- **p. 4 / 4 Method - extractive body cue:** In the following subsections, we first describe our observation encoder, which extracts SO(3)-equivariant features from 2D images, and then our equivariant diffusion module.
- **p. 17 / C Implementation of Our Policy - extractive body cue:** In both cases, the denoising network outputs a sequence of 16 action steps, which are used for optimization during training, while only the first 8 ...
- **Contribution anchor:** p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 4 (4 Method), p. 6 (4 Method), p. 4 (4 Method)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** However, existing equivariant diffusion policy frameworks perform best with point cloud data captured from multiple depth cameras [58].
- **p. 1 / 1 Introduction - extractive body cue:** Despite recent advances in equivariant learning [66, 63], there remains a lack of effective network architectures for leveraging equivariant structure in this setting using only ...
- **p. 2 / 1 Introduction - extractive body cue:** This paper addresses this challenge by introducing a novel diffusion policy framework that incorporates SO(3)-equivariance into eye-in-hand visuomotor learning.
- **p. 2 / 1 Introduction - extractive body cue:** Such a capability should also have the potential to serve as a modular, plug-and-play component that generalizes seamlessly to richer sensing setups.
- **p. 3 / 3 Background - extractive body cue:** Recent extensions [65] incorporate symmetry priors by designing the denoiser to be equivariant with respect to a transformation group G.
- **p. 10 / 6 Conclusion - extractive body cue:** Limitations Our method has several limitations for future investigation.
- **p. 9 / 68.7 58.7 58.0 32.0 54.3 (-6.7) - extractive body cue:** See Appendix J for a detailed failure analysis.
- **Boundary to test:** Limitations Our method has several limitations for future investigation.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our key contributions are summarized as follows: • We introduce Image-to-Sphere Policy (ISP), the first SO(3)-equivariant policy learning framework that uses spherical projection from 2D RGB inputs to model 3D symmetries. • ... | p. 2 (1 Introduction), p. 1 (1 Introduction) |
| Reported outcome | Figure 6: Real-world environments for evaluation. A GoPro camera is mounted on the robot's wrist to capture eye-in-hand observations. In each subfigure, the left image shows the initial state, while the right ... | p. 9 (Figure/Table caption), p. 8 (5 Experiments) |
| Failure/limitation | Limitations Our method has several limitations for future investigation. | p. 10 (6 Conclusion), p. 9 (68.7 58.7 58.0 32.0 54.3 (-6.7)) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 Fourier Coefficients Gripper Orientation Figure 2: Overview of Image-to-Sphere Policy (ISP) (a) An SO(3)-equivariant observation encoder extracts features from the RGB input, projects them onto the sphere, and applies an equivariance co ...를 The observation x ∈X consists of two parts, an eye-in-hand RGB image I, that captures visual information, and proprioceptive data, P ∈R7, including the end-effector's 6D pose (position and orientation) and gripper ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Limitations Our method has several limitations for future investigation.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our key contributions are summarized as follows: • We introduce Image-to-Sphere Policy (ISP), the first SO(3)-equivariant policy learning framework that uses spherical projection from 2D RGB inputs to model 3D symmetries. • ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `Robotics, 3D Vision, equivariant`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Limitations Our method has several limitations for future investigation.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: 5.1 Simulation Experiment Setting We evaluate ISP on twelve robotic manipulation tasks from the MimicGen benchmark [40], which is widely used in previous work on closed-loop policy learning [8, 65]..
3. Compare against the body-reported baseline or a matched simpler baseline: Similarly, ISP-SO(2) outperforms baselines in 20 settings, which further validates the effectiveness of our design..
4. Report the body metric and its denominator/aggregation: Table 1: Success rates (%) on MimicGen tasks with 100 and 200 demonstrations, averaged over 3 seeds. We report both overall mean and per-task performance. The best result is highlighted in bold, ....
5. Re-run the body-reported ablation/failure condition: To ensure a fair comparison, all experiments in the following sections, including ablations and method variants, consistently apply SO(2) data augmentation during training by rotating the end-effector pose in both proprioception and ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (4 Method), p. 17 (C Implementation of Our Policy), p. 7 (4 Method); the primary result is directionally consistent at p. 9 (Figure/Table caption), p. 8 (5 Experiments), p. 9 (68.7 58.7 58.0 32.0 54.3 (-6.7)); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 contributions, summarized, follows mechanism이 Similarly, ISP-SO(2) outperforms baselines in 20 settings, which further validates the effectiveness of our design. 대비 Table 1: Success rates (%) on MimicGen tasks with 100 and 200 demonstrations, averaged over 3 seeds. We ...을 개선하고, Limitations Our method has several limitations for future investigation. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
