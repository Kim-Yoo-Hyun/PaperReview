# Insights — In-Place Scene Labelling and Understanding with Implicit Scene Representation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2103.15875; PDF retrieval source: https://arxiv.org/pdf/2103.15875. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** In addition, multi-view consistency is inherent to the training process and enables the network to produce accurate semantic labels of the scene, including for views ...
- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we show how to design a scene-specific network for joint geometric and semantic prediction and train it on images from a single ...
- **p. 1 / 1. Introduction - extractive body cue:** Unlike scene geometry, however, semantic classes are a human-defined concept and it is not possible to semantically label a novel scene in a purely self-supervised ...
- **p. 2 / 3.1. Preliminaries - extractive body cue:** Specifically, σ(x) is designed to be a function of only 3D position while the radiance c(x, d) is a function of both 3D position and ...
- **p. 3 / 3.4. Implementation - extractive body cue:** Specifically, we use hierarchical volume sampling to jointly optimise coarse and fine networks, where the former provides importance sampling bias so that the latter can ...
- **p. 3 / 3.4. Implementation - extractive body cue:** A scene-specific semantic representation is obtained by training the network from scratch for each scene individually.
- **p. 4 / 3.4. Implementation - extractive body cue:** We train the neural network using the Adam optimiser [7] with a learning rate of 5e-4 for 200,000 iterations.
- **Contribution anchor:** p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (3.1. Preliminaries), p. 3 (3.4. Implementation), p. 3 (3.4. Implementation)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** Semantic scene understanding means attaching class laFusion via Learning Label Denoising Super-Resolution Label Propagation Label Synthesis Label Interpolation Figure 1: Neural radiance fields (NeRF) jointly ...
- **p. 4 / 3.4. Implementation - extractive body cue:** batch size of rays is set to 1024 due to memory limitations.
- **p. 4 / 4.4. Semantic Fusion - extractive body cue:** Given multiple noisy or partial semantic labels, the network can fuse them into a joint implicit 3D space so that we can extract a denoised ...
- **p. 5 / 4.4. Semantic Fusion - extractive body cue:** Quantitative results shown in Table 1 also confirm that accurate denoised labels are obtained after training-as-fusion.
- **p. 5 / 4.4. Semantic Fusion - extractive body cue:** After training using only these noisy labels, we obtain denoised semantic labels by rendering back to the same training poses.
- **p. 6 / 4.4. Semantic Fusion - extractive body cue:** Even when 90% of all training labels are randomly corrupted, we can recover an accurate denoised semantic map.
- **p. 6 / 4.4. Semantic Fusion - extractive body cue:** From left to right are noisy training labels, denoised labels rendered from the same poses after training, and information entropy.
- **Boundary to test:** batch size of rays is set to 1024 due to memory limitations.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In addition, multi-view consistency is inherent to the training process and enables the network to produce accurate semantic labels of the scene, including for views that are substantially different from any in ... | p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Reported outcome | Our method achieves the highest improvement across all metrics, showing the effectiveness of our joint representation in label fusion. | p. 8 (4.4. Semantic Fusion), p. 4 (4.2. Semantic Neural Radiance Fields) |
| Failure/limitation | batch size of rays is set to 1024 due to memory limitations. | p. 4 (3.4. Implementation), p. 4 (4.4. Semantic Fusion) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 Given multiple images of a static scene with known camera intrinsics and extrinsics, NeRF [16] uses MLPs to implicitly represent the continuous 3D scene density σ and colour c = (r, g, ...를 Our system takes as input a set of RGB images with associated known camera poses.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 batch size of rays is set to 1024 due to memory limitations.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In addition, multi-view consistency is inherent to the training process and enables the network to produce accurate semantic labels of the scene, including for views that are substantially different from any in ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `NeRF, semantic, 3D Vision, alignment`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** batch size of rays is set to 1024 due to memory limitations.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: ScanNet ScanNet [3] is a large-scale real-world indoor RGB-D video dataset of 2.5M views in 1513 scenes with rich annotations including semantic segmentation, camera poses and surface reconstructions..
3. Compare against the body-reported baseline or a matched simpler baseline: Our approach relying on consistency of scene representations outperforms baselines aided with depth maps. posed images..
4. Report the body metric and its denominator/aggregation: 0 20 40 60 80 100 Sparsity Ratio (%) 75 80 85 90 95 100 Segmentation Metrics (%) Total Accuracy Class Average Accuracy mIoU 12 15 20 30 57 97145 Baseline Length ....
5. Re-run the body-reported ablation/failure condition: We check the influence of semantics on appearance and geometry by quantitatively computing the quality of rendered RGB images and depth maps on Replica scenes with and without semantic prediction enabled..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (3.4. Implementation), p. 3 (3.4. Implementation), p. 4 (3.4. Implementation); the primary result is directionally consistent at p. 8 (4.4. Semantic Fusion), p. 4 (4.2. Semantic Neural Radiance Fields), p. 7 (4.4. Semantic Fusion); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 addition, multi-view, consistency mechanism이 Our approach relying on consistency of scene representations outperforms baselines aided with depth maps. posed images. 대비 0 20 40 60 80 100 Sparsity Ratio (%) 75 80 85 90 95 100 Segmentation Metrics (%) ...을 개선하고, batch size of rays is set to 1024 due to memory limitations. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
