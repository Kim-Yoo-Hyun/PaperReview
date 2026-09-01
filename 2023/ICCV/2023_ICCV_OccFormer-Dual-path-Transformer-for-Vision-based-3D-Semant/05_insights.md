# Insights — OccFormer: Dual-path Transformer for Vision-based 3D Semantic Occupancy Prediction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `CURATION_ONLY`.
> Analysis basis: `CURATION_ONLY`; 01_overview의 source audit와 기존 insight cue를 이관했다: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed. 자동 추출 결과는 수동 정독으로 간주하지 않는다.

## Paper-supported conclusion

> **Evidence boundary:** 현재 내용은 registry와 기존 curation cue를 정리한 것이다. 자동 추출이나 local PDF 보유는 정독 근거로 간주하지 않으며, 상세 claim은 full-text 확인이 필요하다.

### What was actually new

- **Method cue:** To address this issue, we propose the class-guided sampling method.
- **Problem cue:** Though LiDAR-based methods , with explicit depth measurements, have been dominating the leading performance on public datasets , vision-based approaches still offer advantages in terms of cost-effectiveness, stability, ...
- **Claim/result cue:** Experimental results demonstrate that OccFormer significantly outperforms existing methods for semantic scene completion on SemanticKITTI dataset and for LiDAR semantic segmentation on nuScenes dataset.

### Strongest assumption and failure boundary

- Explicit assumptions and negative results are not recorded in the current source note; full-text review is required.

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `observation → state/world model`.
- **Registry interface:** `3D Vision, semantic, occupancy, Transformer` is the paper's recorded topic/interface, not evidence that the full robotics loop was evaluated.
- **Prior interpretation carried forward:**
  - Camera/LiDAR/Radar/BEV/occupancy representation을 robot 또는 autonomous agent의 metric world model로 사용할 수 있다.
  - Sensor fusion의 핵심은 modality-specific noise와 calibration error를 줄이면서 semantics와 geometry를 같은 map으로 정렬하는 것이다.
- Reuse the paper by preserving its input/output boundary and testing downstream success, failure, and latency under a matched baseline budget.

### Dependency and evolution

- Registry position: `Autonomous 3D Perception and Sensor Fusion`; tags: `3D Vision, semantic, occupancy, Transformer`.
- A direct citation predecessor/successor is not recorded in the legacy note; confirm it from references and the track synthesis before asserting lineage.
- Recorded scope boundary/future cue:
  - 논문이 도달한 지점: Experimental results demonstrate that OccFormer significantly outperforms existing methods for semantic scene completion on SemanticKITTI dataset and for LiDAR semantic segmentation on nuScenes dataset.
  - perception benchmark 성능 이후에도 open-vocabulary semantics, online calibration, planning-aware uncertainty는 후속 연구 지점으로 남는다.

### Minimal reproduction

- **Protocol carried forward from the legacy note (candidate, not a verified paper evaluation):**
  - 논문 내 evaluation 단서: KITTI, SemanticKITTI, nuScenes / mIoU, IoU, mAP
  - 내 연구 확장 benchmark 후보: nuScenes, Waymo, KITTI, Occ3D
  - 내 연구 확장 metric 후보: mAP, NDS, IoU, mIoU
  - 검증 초점: detection/occupancy 성능, robustness, calibration sensitivity, planning utility를 확인한다.
- Do not label a candidate benchmark, metric, or extension protocol as the paper's own evaluation until the experiment section is checked.

## Falsifiable research question

multi-sensor 3D representation에 language/semantic feature를 붙이면 planning-relevant perception이 실제로 개선되는가?

**Reject the hypothesis if** the primary metric does not improve at a matched budget, or if the method adds latency, failure, or assumption sensitivity without a compensating closed-loop benefit.
