# Insights — KPConv: Flexible and Deformable Convolution for Point Clouds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1904.08889; PDF retrieval source: https://arxiv.org/pdf/1904.08889. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, we propose a deformable version of our convolution [7], which consists of learning local shifts applied to the kernel points (see Figure 3).
- **p. 2 / 1. Introduction - extractive body cue:** KPConv also consists of a set of local 3D filters, but overcomes previous point convolution limitations as shown in related work.
- **p. 1 / 1. Introduction - extractive body cue:** Various approaches have been proposed to handle such data, and can be grouped into different categories that we will develop in the related work section.
- **p. 5 / 3.4. Kernel Point Network Architectures - extractive body cue:** Combining analogy with successful image networks and empirical studies, we designed two network architectures for the classification and the segmentation tasks.
- **p. 5 / 3.4. Kernel Point Network Architectures - extractive body cue:** Our convolutional blocks are designed like bottleneck ResNet blocks [12] with a KPConv replacing the image convolution, batch normalization and leaky ReLu activation.
- **p. 5 / 3.4. Kernel Point Network Architectures - extractive body cue:** Skip links are used to pass the features between intermediate layers of the encoder and the decoder.
- **p. 5 / 3.4. Kernel Point Network Architectures - extractive body cue:** The encoder part is the same as in KP-CNN, and the decoder part uses nearest upsampling to get the final pointwise features.
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 5 (3.4. Kernel Point Network Architectures), p. 5 (3.4. Kernel Point Network Architectures), p. 5 (3.4. Kernel Point Network Architectures)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** Input points with a constant scalar feature (in grey) are convolved through a KPConv that is defined by a set of kernel points (in black) ...
- **p. 2 / 1. Introduction - extractive body cue:** KPConv also consists of a set of local 3D filters, but overcomes previous point convolution limitations as shown in related work.
- **p. 2 / 1. Introduction - extractive body cue:** Deformable KPConv thrives on more difficult tasks, like large segmentation datasets offering many object instances and greater diversity.
- **p. 7 / 4.3. Ablation Study - extractive body cue:** We use Scannet dataset (same parameters as before) and use the official validation set, because the test set cannot be used for such evaluations.
- **Boundary to test:** We use Scannet dataset (same parameters as before) and use the official validation set, because the test set cannot be used for such evaluations.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Furthermore, we propose a deformable version of our convolution [7], which consists of learning local shifts applied to the kernel points (see Figure 3). | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Among these 4 datasets, KPConv deformable kernels improved the results on Paris-Lille-3D and S3DIS while the rigid version was better on Scannet and Semantic3D. | p. 6 (4.2. 3D Scene Segmentation), p. 8 (4.4. Learned Features and Effective Receptive Field) |
| Failure/limitation | We use Scannet dataset (same parameters as before) and use the official validation set, because the test set cannot be used for such evaluations. | p. 7 (4.3. Ablation Study) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 Input points with a constant scalar feature (in grey) are convolved through a KPConv that is defined by a set of kernel points (in black) with filter weights on each point. 를 The kernel weights are thus carried by points, like the input features, and their area of influence is defined by a correlation function.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 We use Scannet dataset (same parameters as before) and use the official validation set, because the test set cannot be used for such evaluations.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Furthermore, we propose a deformable version of our convolution [7], which consists of learning local shifts applied to the kernel points (see Figure 3).
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `point cloud, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** We use Scannet dataset (same parameters as before) and use the official validation set, because the test set cannot be used for such evaluations.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The 3D scenes in these datasets are too big to be segmented as a whole..
3. Compare against the body-reported baseline or a matched simpler baseline: As shown on Table 1, our networks outperform other state-of-the-art methods using only points (we do not take into account methods using normals as additional input)..
4. Report the body metric and its denominator/aggregation: Table 6. Semantic segmentation IoU scores on S3DIS Area-5. Additionally, we give the mean class recall, a measure that some previous works call mean class accuracy..
5. Re-run the body-reported ablation/failure condition: For generalizability to real data, we only consider scores obtained without shape normals on ModelNet40 dataset..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (3.4. Kernel Point Network Architectures), p. 5 (3.4. Kernel Point Network Architectures); the primary result is directionally consistent at p. 6 (4.2. 3D Scene Segmentation), p. 8 (4.4. Learned Features and Effective Receptive Field), p. 5 (4.1. 3D Shape Classification and Segmentation); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Furthermore, deformable, version mechanism이 As shown on Table 1, our networks outperform other state-of-the-art methods using only points (we do ... 대비 Table 6. Semantic segmentation IoU scores on S3DIS Area-5. Additionally, we give the mean class recall, a measure ...을 개선하고, We use Scannet dataset (same parameters as before) and use the official validation set, because the ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
