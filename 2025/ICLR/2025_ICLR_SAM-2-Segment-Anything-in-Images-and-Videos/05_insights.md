# Insights — SAM 2: Segment Anything in Images and Videos

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `CURATION_ONLY`.
> Analysis basis: `CURATION_ONLY`; 01_overview의 source audit와 기존 insight cue를 이관했다: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed. 자동 추출 결과는 수동 정독으로 간주하지 않는다.

## Paper-supported conclusion

> **Evidence boundary:** 현재 내용은 registry와 기존 curation cue를 정리한 것이다. 자동 추출이나 local PDF 보유는 정독 근거로 간주하지 않으며, 상세 claim은 full-text 확인이 필요하다.

### What was actually new

- **Method cue:** 1-click 3-click 5-click bounding box ground-truth mask‡ SAM+XMem++ SAM+Cutie SAM 2 56.9 56.7 64.7 68.4 70.1 75.3 70.6 72.2 77.6 67.6 69.4 74.4 72.7 74.1 79.3 Table 4: ...

### Strongest assumption and failure boundary

- Explicit assumptions and negative results are not recorded in the current source note; full-text review is required.

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `observation/language → task decision → action/control`.
- **Registry interface:** `segmentation, foundation model, prompting, video segmentation, memory` is the paper's recorded topic/interface, not evidence that the full robotics loop was evaluated.
- **Prior interpretation carried forward:**
  - Large-scale pretraining feature를 3D perception의 initialization, pseudo-label, open-vocabulary semantic prior로 사용할 수 있다.
  - 2D foundation model의 강한 recognition prior를 3D consistency, view aggregation, robot task relevance로 재해석해야 한다.
- Reuse the paper by preserving its input/output boundary and testing downstream success, failure, and latency under a matched baseline budget.

### Dependency and evolution

- Registry position: `Foundations: Vision and Language Models`; tags: `segmentation, foundation model, prompting, video segmentation, memory`.
- A direct citation predecessor/successor is not recorded in the legacy note; confirm it from references and the track synthesis before asserting lineage.
- Recorded scope boundary/future cue:
  - 2D/vision-language representation 성능 이후에도 3D metric alignment, temporal consistency, robot interaction feedback은 별도 문제로 남는다.

### Minimal reproduction

- **Protocol carried forward from the legacy note (candidate, not a verified paper evaluation):**
  - 논문 내 evaluation 단서: KITTI / accuracy, mIoU, IoU
  - 내 연구 확장 benchmark 후보: ImageNet, COCO, ScanNet, S3DIS
  - 내 연구 확장 metric 후보: accuracy, mIoU, Recall@K, success rate
  - 검증 초점: 2D recognition transfer, 3D semantic consistency, downstream robotics utility를 확인한다.
- Do not label a candidate benchmark, metric, or extension protocol as the paper's own evaluation until the experiment section is checked.

## Falsifiable research question

2D foundation feature를 3D point/gaussian/map에 정렬할 때 어떤 consistency loss나 aggregation이 가장 안정적인가?

**Reject the hypothesis if** the primary metric does not improve at a matched budget, or if the method adds latency, failure, or assumption sensitivity without a compensating closed-loop benefit.
