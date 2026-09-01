# Insights — Dens3R: A Foundation Model for 3D Geometry Prediction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `CURATION_ONLY`.
> Analysis basis: `CURATION_ONLY`; 01_overview의 source audit와 기존 insight cue를 이관했다: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed. 자동 추출 결과는 수동 정독으로 간주하지 않는다.

## Paper-supported conclusion

> **Evidence boundary:** 현재 내용은 registry와 기존 curation cue를 정리한 것이다. 자동 추출이나 local PDF 보유는 정독 근거로 간주하지 않으며, 상세 claim은 full-text 확인이 필요하다.

### What was actually new

- **Method cue:** Mean ↓ NYUv2 Med ↓ δ11.25◦ ↑ Mean ↓ ScanNet Med ↓ δ11.25◦ ↑ Mean ↓ DSINE Lotus* GeoWizard StableNormal Ours 18.6 17.5 20.4 19.7 16.1 9.9 8.6 ...

### Strongest assumption and failure boundary

- Explicit assumptions and negative results are not recorded in the current source note; full-text review is required.

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `observation → state/world model`.
- **Registry interface:** `3D Vision` is the paper's recorded topic/interface, not evidence that the full robotics loop was evaluated.
- **Prior interpretation carried forward:**
  - Geometry reconstruction, pose estimation, map update 원리를 robot의 spatial memory와 3D scene understanding 기반으로 사용할 수 있다.
  - Classical geometry/SLAM의 metric constraint는 VLM/LLM 기반 semantic reasoning이 놓치는 scale, pose, visibility 문제를 보정한다.
- Reuse the paper by preserving its input/output boundary and testing downstream success, failure, and latency under a matched baseline budget.

### Dependency and evolution

- Registry position: `3D Representation Learning`; tags: `3D Vision`.
- A direct citation predecessor/successor is not recorded in the legacy note; confirm it from references and the track synthesis before asserting lineage.
- Recorded scope boundary/future cue:
  - geometric accuracy 이후에도 open-vocabulary semantics, dynamic objects, learned priors, task-aware mapping은 후속 연구 지점으로 남는다.

### Minimal reproduction

- **Protocol carried forward from the legacy note (candidate, not a verified paper evaluation):**
  - 논문 내 evaluation 단서: ScanNet, KITTI, Waymo, Argoverse, Objaverse / accuracy, mAP, RMSE
  - 내 연구 확장 benchmark 후보: TUM RGB-D, EuRoC, KITTI, ScanNet
  - 내 연구 확장 metric 후보: ATE, RPE, AbsRel, RMSE
  - 검증 초점: pose/reconstruction accuracy, semantic map consistency, robot navigation/manipulation utility를 확인한다.
- Do not label a candidate benchmark, metric, or extension protocol as the paper's own evaluation until the experiment section is checked.

## Falsifiable research question

SLAM/reconstruction map에 language-aligned semantic feature를 붙여도 geometric consistency가 유지되는가?

**Reject the hypothesis if** the primary metric does not improve at a matched budget, or if the method adds latency, failure, or assumption sensitivity without a compensating closed-loop benefit.
