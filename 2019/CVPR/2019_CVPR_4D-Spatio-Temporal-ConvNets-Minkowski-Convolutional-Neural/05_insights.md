# Insights — 4D Spatio-Temporal ConvNets: Minkowski Convolutional Neural Networks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `CURATION_ONLY`.
> Analysis basis: `CURATION_ONLY`; 01_overview의 source audit와 기존 insight cue를 이관했다: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed. 자동 추출 결과는 수동 정독으로 간주하지 않는다.

## Paper-supported conclusion

> **Evidence boundary:** 현재 내용은 registry와 기존 curation cue를 정리한 것이다. 자동 추출이나 local PDF 보유는 정독 근거로 간주하지 않으며, 상세 claim은 full-text 확인이 필요하다.

### What was actually new

- **Method cue:** To overcome challenges in the high-dimensional 4D space, we propose the hybrid kernel, a special case of the generalized sparse convolution, and the trilateral-stationary conditional random field that ...
- **Claim/result cue:** Experimentally, we show that convolutional neural networks with only generalized sparse convolutions can outperform 2D or 2D-3D hybrid methods by a large margin.2 Also, we show that on ...

### Strongest assumption and failure boundary

- Explicit assumptions and negative results are not recorded in the current source note; full-text review is required.

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `observation → state/world model`.
- **Registry interface:** `3D Vision` is the paper's recorded topic/interface, not evidence that the full robotics loop was evaluated.
- **Prior interpretation carried forward:**
  - Point/voxel/patch-level 3D representation을 downstream segmentation, grounding, manipulation state encoding의 backbone으로 사용할 수 있다.
  - Self-supervised 또는 foundation-style 3D feature는 annotation-heavy 3D supervision을 줄이는 방향의 출발점이 된다.
- Reuse the paper by preserving its input/output boundary and testing downstream success, failure, and latency under a matched baseline budget.

### Dependency and evolution

- Registry position: `3D Representation Learning`; tags: `3D Vision`.
- A direct citation predecessor/successor is not recorded in the legacy note; confirm it from references and the track synthesis before asserting lineage.
- Recorded scope boundary/future cue:
  - 논문이 도달한 지점: Experimentally, we show that convolutional neural networks with only generalized sparse convolutions can outperform 2D or 2D-3D hybrid methods by a large margin.2 Also, we show that on ...
  - representation benchmark 성능 이후에도 language alignment, embodied interaction, dynamic scene transfer는 별도 검증이 필요하다.

### Minimal reproduction

- **Protocol carried forward from the legacy note (candidate, not a verified paper evaluation):**
  - 논문 내 evaluation 단서: ScanNet, S3DIS / accuracy, mIoU, IoU, mAP, collision
  - 내 연구 확장 benchmark 후보: ModelNet40, ShapeNet, ScanNet, S3DIS
  - 내 연구 확장 metric 후보: accuracy, mIoU, Chamfer, success rate
  - 검증 초점: 3D representation transfer, semantic grounding, robot downstream performance를 확인한다.
- Do not label a candidate benchmark, metric, or extension protocol as the paper's own evaluation until the experiment section is checked.

## Falsifiable research question

3D pretraining feature가 open-vocabulary grounding과 robot manipulation 모두에 transfer되는가?

**Reject the hypothesis if** the primary metric does not improve at a matched budget, or if the method adds latency, failure, or assumption sensitivity without a compensating closed-loop benefit.
