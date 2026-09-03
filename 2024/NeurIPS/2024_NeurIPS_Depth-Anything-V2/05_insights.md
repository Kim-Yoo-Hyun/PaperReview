# Insights — Depth Anything V2

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (30 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2406.09414; PDF retrieval source: https://arxiv.org/pdf/2406.09414. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 6 / 1 Introduction - extractive body cue:** It consists of three steps: • train a reliable teacher model based on DINOv2-G purely on high-quality synthetic images. • produce precise pseudo depth on ...
- **p. 7 / 1 Introduction - extractive body cue:** To address this, we introduce a second pipeline, where we carefully analyze images and manually identify challenging pairs.
- **p. 4 / 1 Introduction - extractive body cue:** In the right side of Figure 4c, we show the fine-grained prediction of a MDE model trained on synthetic images.
- **p. 3 / 1 Introduction - extractive body cue:** Black regions are ignored during training. such a challenging goal, no fancy or sophisticated techniques need to be developed.
- **p. 9 / Method - extractive body cue:** First, same as V1 [89], we follow the ZoeDepth [6] pipeline, but replace its MiDaS [7] encoder with our pre-trained encoder.
- **p. 9 / Method - extractive body cue:** Different from Depth Anything V1 [89], we further attempt to remove the synthetic images during training student models.
- **p. 8 / Method - extractive body cue:** Even our most lightweight model is superior to all other community models.
- **Contribution anchor:** p. 6 (1 Introduction), p. 7 (1 Introduction), p. 4 (1 Introduction), p. 3 (1 Introduction), p. 9 (Method), p. 9 (Method)

### Strongest assumption and failure boundary

- **p. 4 / 1 Introduction - extractive body cue:** Consequently, despite the astonishing precision of Hypersim [58] or Virtual KITTI [9] (Figure 4b), we cannot expect models trained on them to generalize well in ...
- **p. 7 / 1 Introduction - extractive body cue:** 6 A New Evaluation Benchmark: DA-2K 6.1 Limitations in Existing Benchmarks In Section 2, we demonstrated that commonly used real training sets have noisy depth ...
- **p. 3 / 1 Introduction - extractive body cue:** However, we find current test sets [70] are too noisy to reflect the true strengths of MDE models.
- **p. 3 / 1 Introduction - extractive body cue:** Black regions are ignored during training. such a challenging goal, no fancy or sophisticated techniques need to be developed.
- **p. 4 / 1 Introduction - extractive body cue:** 3 Challenges in Using Synthetic Data If synthetic data are so advantageous, why are real data still dominating MDE?
- **p. 14 / Figure/Table caption - extractive body cue:** Table 13: Comparison among various pre-trained encoders when purely trained on synthetic images. B.7 Benefit of gradient matching loss to fine-grained predictions MiDaS [56] proposes ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 6: Failure cases of the most capable DINOv2-G model when purely trained on synthetic images. Left: the sky should be ultra far. Right: the ...
- **Boundary to test:** Table 13: Comparison among various pre-trained encoders when purely trained on synthetic images. B.7 Benefit of gradient matching loss to fine-grained predictions MiDaS [56] proposes a gradient matching loss Lgm to enhance ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | It consists of three steps: • train a reliable teacher model based on DINOv2-G purely on high-quality synthetic images. • produce precise pseudo depth on large-scale unlabeled real images. • train final ... | p. 6 (1 Introduction), p. 7 (1 Introduction) |
| Reported outcome | We achieve the results without Mapillary [1] or COCO [40] pre-training. our models of various scales consistently achieve the best performance, outperforming other methods remarkably. | p. 12 (Dataset), p. 1 (Figure/Table caption) |
| Failure/limitation | Table 13: Comparison among various pre-trained encoders when purely trained on synthetic images. B.7 Benefit of gradient matching loss to fine-grained predictions MiDaS [56] proposes a gradient matching loss Lgm to enhance ... | p. 14 (Figure/Table caption), p. 5 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 This observation is indeed similar to SAM [33] that only releases its pseudo-labeled masks.를 Precise depth information is not only favorable in classical applications, such as 3D reconstruction [47, 32, 93], navigation [82], and autonomous driving [80], but is also preferable in modern scenarios, e.g., AI-generated ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Table 13: Comparison among various pre-trained encoders when purely trained on synthetic images. B.7 Benefit of gradient matching loss to fine-grained predictions MiDaS [56] proposes a gradient matching loss Lgm to enhance ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: It consists of three steps: • train a reliable teacher model based on DINOv2-G purely on high-quality synthetic images. • produce precise pseudo depth on large-scale unlabeled real images. • train final ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `depth, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Table 13: Comparison among various pre-trained encoders when purely trained on synthetic images. B.7 Benefit of gradient matching loss to fine-grained predictions MiDaS [56] proposes a gradient matching loss Lgm to enhance ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: As shown in Table 3, on our proposed benchmark with diverse scenes, even our smallest model is significantly better than other heavy SD-based 8.
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 1: Depth Anything V2 significantly outperforms V1 [89] in robustness and fine-grained details. Compared with SD-based models [31, 25], it enjoys faster inference speed, fewer parameters, and higher depth accuracy..
4. Report the body metric and its denominator/aggregation: Figure 1: Depth Anything V2 significantly outperforms V1 [89] in robustness and fine-grained details. Compared with SD-based models [31, 25], it enjoys faster inference speed, fewer parameters, and higher depth accuracy..
5. Re-run the body-reported ablation/failure condition: Since our model predicts affine-invariant inverse depth, for fairness, we compare with Depth Anything V1 [89] and MiDaS V3.1 [7] on five unseen test datasets..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 9 (Method), p. 9 (Method), p. 8 (Method); the primary result is directionally consistent at p. 12 (Dataset), p. 1 (Figure/Table caption), p. 9 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 consists, three, steps mechanism이 Figure 1: Depth Anything V2 significantly outperforms V1 [89] in robustness and fine-grained details. Compared with ... 대비 Figure 1: Depth Anything V2 significantly outperforms V1 [89] in robustness and fine-grained details. Compared with SD-based models ...을 개선하고, Table 13: Comparison among various pre-trained encoders when purely trained on synthetic images. B.7 Benefit of ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
