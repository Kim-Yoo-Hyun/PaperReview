# Insights — Masked Autoencoders Are Scalable Vision Learners

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `CURATION_ONLY`.
> Analysis basis: `CURATION_ONLY`; 01_overview의 source audit와 기존 insight cue를 이관했다: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed. 자동 추출 결과는 수동 정독으로 간주하지 않는다.

## Paper-supported conclusion

> **Evidence boundary:** 현재 내용은 registry와 기존 curation cue를 정리한 것이다. 자동 추출이나 local PDF 보유는 정독 근거로 간주하지 않으며, 상세 claim은 full-text 확인이 필요하다.

### What was actually new

- **Method cue:** First, we develop an asymmetric encoder-decoder architecture, with an encoder that operates only on the visible subset of patches (without mask tokens), along with a lightweight decoder that ...
- **Problem cue:** This paper shows that masked autoencoders (MAE) are scalable self-supervised learners for computer vision.
- **Claim/result cue:** Transfer performance in downstream tasks outperforms supervised pretraining and shows promising scaling behavior. encoder decoder input target .... .... arXiv:2111.06377v3 [cs.CV] 19 Dec 2021 Facebook AI Research (FAIR) ...

### Strongest assumption and failure boundary

- Explicit assumptions and negative results are not recorded in the current source note; full-text review is required.

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `observation/language → task decision → action/control`.
- **Registry interface:** `Vision Foundation Model, self-supervised, representation` is the paper's recorded topic/interface, not evidence that the full robotics loop was evaluated.
- **Prior interpretation carried forward:**
  - Large-scale pretraining feature를 3D perception의 initialization, pseudo-label, open-vocabulary semantic prior로 사용할 수 있다.
  - 2D foundation model의 강한 recognition prior를 3D consistency, view aggregation, robot task relevance로 재해석해야 한다.
- Reuse the paper by preserving its input/output boundary and testing downstream success, failure, and latency under a matched baseline budget.

### Dependency and evolution

- Registry position: `Foundations: Vision and Language Models`; tags: `Vision Foundation Model, self-supervised, representation`.
- A direct citation predecessor/successor is not recorded in the legacy note; confirm it from references and the track synthesis before asserting lineage.
- Recorded scope boundary/future cue:
  - 논문이 도달한 지점: Transfer performance in downstream tasks outperforms supervised pretraining and shows promising scaling behavior. encoder decoder input target .... .... arXiv:2111.06377v3 [cs.CV] 19 Dec 2021 Facebook AI Research (FAIR) ...
  - 2D/vision-language representation 성능 이후에도 3D metric alignment, temporal consistency, robot interaction feedback은 별도 문제로 남는다.

### Minimal reproduction

- **Protocol carried forward from the legacy note (candidate, not a verified paper evaluation):**
  - 논문 내 evaluation 단서: ImageNet, COCO / accuracy, mIoU, AP
  - 내 연구 확장 benchmark 후보: ImageNet, COCO, ScanNet, S3DIS
  - 내 연구 확장 metric 후보: accuracy, mIoU, Recall@K, success rate
  - 검증 초점: 2D recognition transfer, 3D semantic consistency, downstream robotics utility를 확인한다.
- Do not label a candidate benchmark, metric, or extension protocol as the paper's own evaluation until the experiment section is checked.

## Falsifiable research question

2D foundation feature를 3D point/gaussian/map에 정렬할 때 어떤 consistency loss나 aggregation이 가장 안정적인가?

**Reject the hypothesis if** the primary metric does not improve at a matched budget, or if the method adds latency, failure, or assumption sensitivity without a compensating closed-loop benefit.
