# Insights — Continuous 3D Perception Model with Persistent State

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2501.12387; PDF retrieval source: https://arxiv.org/pdf/2501.12387. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1. Introduction - extractive body cue:** The learned prior enables our method to address challenges encountered by traditional methods (e.g., dynamic objects, sparse observations, degenerate camera motion), while the ability to ...
- **p. 2 / 1. Introduction - extractive body cue:** Our framework is designed to be general and flexible, making it well-suited for training on an extensive collection of datasets and adaptable to diverse inference ...
- **p. 1 / 1. Introduction - extractive body cue:** Building on these insights, we introduce an online 3D perception framework that unifies three key capabilities: 1) reconstructing 3D scenes from few observations, 2) continuously ...
- **p. 2 / 1. Introduction - extractive body cue:** We also show that our method can infer previously unseen structures and continuously refine the reconstruction as new observations arrive.
- **p. 3 / 3.1. State-Input Interaction Mechanism - extractive body cue:** Our method takes a stream of images as input.
- **p. 5 / 3.4. Training Strategy - extractive body cue:** We use a ViT-Large model [22] for the image encoder Encoderi, initialized with DUSt3R encoder pretrained weights, and ViT-Base for the decoders.
- **p. 4 / 3.2. Querying the State with Unseen Views - extractive body cue:** Given a query raymap R, we first encode it into token representations Fr using a separate transformer Encoderr: Fr = Encoderr(R).
- **Contribution anchor:** p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. State-Input Interaction Mechanism), p. 5 (3.4. Training Strategy)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** The learned prior enables our method to address challenges encountered by traditional methods (e.g., dynamic objects, sparse observations, degenerate camera motion), while the ability to ...
- **p. 1 / 1. Introduction - extractive body cue:** We achieve these capabilities by integrating data-driven priors with a recurrent update mechanism.
- **p. 2 / 1. Introduction - extractive body cue:** These datasets span a broad spectrum of scene types and contexts-static and dynamic, indoor and outdoor, real and synthetic-enabling the model to acquire robust and ...
- **p. 2 / 1. Introduction - extractive body cue:** During inference, our recurrent framework naturally accepts varying numbers of images, and supports a wide range of input data settings: from streaming video to unstructured ...
- **p. 6 / 4.2. Camera Pose Estimation - extractive body cue:** Unlike most visual odometry methods [17, 34, 96], our method does not require any camera calibration.
- **p. 6 / 4.2. Camera Pose Estimation - extractive body cue:** Most prior approaches do so through test-time optimization, as seen in RobustCVD [47] and CasualSAM [128], which jointly estimate camera parameters and dense depth maps ...
- **p. 16 / Figure/Table caption - extractive body cue:** Table 6. Training Datasets. We provide more details of our training datasets. We classify a dataset as dynamic if annotations exist for moving objects like ...
- **Boundary to test:** Unlike most visual odometry methods [17, 34, 96], our method does not require any camera calibration.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | The learned prior enables our method to address challenges encountered by traditional methods (e.g., dynamic objects, sparse observations, degenerate camera motion), while the ability to continuously update allows it to process new ... | p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Our method significantly outperforms the other online approach Spann3R [101], and achieves comparable or sometimes better results than the top optimization-based method, DUSt3RGA, while operating online at 25× the speed. | p. 7 (4.3. 3D Reconstruction), p. 6 (4.1. Monocular and Video Depth Estimation) |
| Failure/limitation | Unlike most visual odometry methods [17, 34, 96], our method does not require any camera calibration. | p. 6 (4.2. Camera Pose Estimation), p. 6 (4.2. Camera Pose Estimation) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `camera/depth stream, pose, map와 language goal → robot pose, free-space/semantic map와 local goal → collision-free trajectory 또는 velocity command`.
- 이 논문의 재사용 가능한 지점은 Following the state-image interaction, explicit 3D pointmaps and camera poses are extracted for each view.를 F ′ t denotes the image tokens enriched with state information. z is a learnable "pose token" prepended to the image tokens, whose output z′ t captures image-level information related to the ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 robot pose, free-space/semantic map와 local goal가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Unlike most visual odometry methods [17, 34, 96], our method does not require any camera calibration.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: The learned prior enables our method to address challenges encountered by traditional methods (e.g., dynamic objects, sparse observations, degenerate camera motion), while the ability to continuously update allows it to process new ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `3D reconstruction, SLAM, representation`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Unlike most visual odometry methods [17, 34, 96], our method does not require any camera calibration.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: For this experiment, we use the validation set of the MapFree [3] and ARKitScenes datasets, both with metric camera pose annotations..
3. Compare against the body-reported baseline or a matched simpler baseline: We present a subset of baselines here; please refer to the supplementary material for full comparisons..
4. Report the body metric and its denominator/aggregation: We evaluate scene-level reconstruction on the 7-scenes [83] and NRGBD [4] datasets using accuracy (Acc), completion (Comp), and normal consistency (NC) metrics, as in prior works [4, 101, 102, 107, 132]..
5. Re-run the body-reported ablation/failure condition: For metric pointmap methods like ours and MASt3R, we also report results without alignment..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (3.4. Training Strategy), p. 4 (3.2. Querying the State with Unseen Views), p. 3 (3. Method); the primary result is directionally consistent at p. 7 (4.3. 3D Reconstruction), p. 6 (4.1. Monocular and Video Depth Estimation), p. 8 (4.4. Analysis); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 learned, prior, enables mechanism이 We present a subset of baselines here; please refer to the supplementary material for full comparisons. 대비 We evaluate scene-level reconstruction on the 7-scenes [83] and NRGBD [4] datasets using accuracy (Acc), completion (Comp), and ...을 개선하고, Unlike most visual odometry methods [17, 34, 96], our method does not require any camera calibration. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
