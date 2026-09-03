# Insights — U-CAN: Unsupervised Point Cloud Denoising with Consistency-Aware Noise2Noise Matching

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=hVFtXE19Me; PDF retrieval source: https://arxiv.org/pdf/2510.25210. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** Our main contributions can be summarized as follows. • We introduce U-CAN, a novel framework for unsupervised point cloud denoising by leveraging a neural network ...
- **p. 2 / 1 Introduction - extractive body cue:** In response to this challenge, we introduce a novel consistency-aware constraint that specifically targets the denoising geometric consistency.
- **p. 1 / Abstract - extractive body cue:** We achieve this by a novel loss which enables statistical reasoning on multiple noisy point cloud observations.
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce U-CAN, an Unsupervised framework for point cloud denoising with Consistency-Aware Noise2Noise matching.
- **p. 1 / Abstract - extractive body cue:** Previous works mostly focus on training neural networks with noisy-clean point cloud pairs for learning denoising priors, which requires extensively manual efforts.
- **p. 2 / 1 Introduction - extractive body cue:** This ambiguity can lead to unstable convergence due to inconsistencies in denoising results across different noisy observations.
- **Contribution anchor:** p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** However, the current unsupervised approaches still struggle to predict
- **p. 2 / 1 Introduction - extractive body cue:** precise clean point cloud while keeping high-fidelity local geometries due to the lack of sufficient constraints at local-level.
- **p. 2 / 1 Introduction - extractive body cue:** Another challenge in predicting robust denoising arises from the unknown location of true surfaces when only noisy observations are available.
- **p. 1 / 1 Introduction - extractive body cue:** The subsequent approaches, such as TotalDenoising [14], therefore turn to explore unsupervised point cloud denoising by leveraging a spatial prior term for total-level denoising.
- **p. 7 / 4 Experiments - extractive body cue:** The unsupervised versions of DMR [28] and ScoreDenoise [29] which leverage the same constraint as TTD, share same limitations of TTD and presents sub-optimal performance ...
- **p. 7 / 4 Experiments - extractive body cue:** For unsupervised denoising, the TTD [14] fails to produce high-fidelity local geometries with only the global constraints.
- **p. 9 / 4 Experiments - extractive body cue:** Note that U-CAN does not require (1) sparse-to-dense point cloud pairs and (2) clean point clouds, where the only required data is the noise point ...
- **Boundary to test:** The unsupervised versions of DMR [28] and ScoreDenoise [29] which leverage the same constraint as TTD, share same limitations of TTD and presents sub-optimal performance at both low and high resolutions due ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our main contributions can be summarized as follows. • We introduce U-CAN, a novel framework for unsupervised point cloud denoising by leveraging a neural network to infer a multi-step denoising path for ... | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Reported outcome | 3, where our method significantly outperforms DMR-TTD and ScoreDenoise-TTD, and also achieve better performance than the supervised method PU-Net designed for the upsampling task. | p. 9 (4 Experiments), p. 7 (4 Experiments) |
| Failure/limitation | The unsupervised versions of DMR [28] and ScoreDenoise [29] which leverage the same constraint as TTD, share same limitations of TTD and presents sub-optimal performance at both low and high resolutions due ... | p. 7 (4 Experiments), p. 7 (4 Experiments) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 Our main contributions can be summarized as follows. • We introduce U-CAN, a novel framework for unsupervised point cloud denoising by leveraging a neural network to infer a multi-step denoising path for ...를 Extensive experiments demonstrate that the proposed U-CAN outperforms state-of-the-art methods in unsupervised point cloud denoising, upsampling and image denoising, where U-CAN even achieves comparable performances with the supervised ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 The unsupervised versions of DMR [28] and ScoreDenoise [29] which leverage the same constraint as TTD, share same limitations of TTD and presents sub-optimal performance at both low and high resolutions due ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our main contributions can be summarized as follows. • We introduce U-CAN, a novel framework for unsupervised point cloud denoising by leveraging a neural network to infer a multi-step denoising path for ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `point cloud, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** The unsupervised versions of DMR [28] and ScoreDenoise [29] which leverage the same constraint as TTD, share same limitations of TTD and presents sub-optimal performance at both low and high resolutions due ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: 4.2 Point Cloud Denoising on Scanned Data For demonstrating the capability of U-CAN to handle real-world point cloud noises, we conduct evaluations under the Paris-rue-Madame dataset [45] which is obtained from real ....
3. Compare against the body-reported baseline or a matched simpler baseline: We provide the visual comparison among the state-of-the-art supervised and unsupervised point cloud denoising methods in Fig..
4. Report the body metric and its denominator/aggregation: The unsupervised versions of DMR [28] and ScoreDenoise [29] which leverage the same constraint as TTD, share same limitations of TTD and presents sub-optimal performance at both low and high resolutions due ....
5. Re-run the body-reported ablation/failure condition: Without LDC, performance significantly drops (e.g., CD Table 4: Ablation studies on the framework and loss designs..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract); the primary result is directionally consistent at p. 9 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 main, contributions, summarized mechanism이 We provide the visual comparison among the state-of-the-art supervised and unsupervised point cloud denoising methods in ... 대비 The unsupervised versions of DMR [28] and ScoreDenoise [29] which leverage the same constraint as TTD, share same ...을 개선하고, The unsupervised versions of DMR [28] and ScoreDenoise [29] which leverage the same constraint as TTD, ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
