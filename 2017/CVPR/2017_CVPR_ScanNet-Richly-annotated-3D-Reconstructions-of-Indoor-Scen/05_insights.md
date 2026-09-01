# Insights — ScanNet: Richly-annotated 3D Reconstructions of Indoor Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `CURATION_ONLY`.
> Analysis basis: `CURATION_ONLY`; 01_overview의 source audit와 기존 insight cue를 이관했다: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed. 자동 추출 결과는 수동 정독으로 간주하지 않는다.

## Paper-supported conclusion

> **Evidence boundary:** 현재 내용은 registry와 기존 curation cue를 정리한 것이다. 자동 추출이나 local PDF 보유는 정독 근거로 간주하지 않으며, 상세 claim은 full-text 확인이 필요하다.

### What was actually new

- **Method cue:** To address this issue, we introduce ScanNet, an RGB-D video dataset containing 2.5M views in 1513 scenes annotated with 3D camera poses, surface reconstructions, and semantic segmentations.
- **Problem cue:** Thus, existing work on 3D datasets often fall back to polygon or bounding box annotations on 2.5D RGB-D images , rather than directly annotating in 3D.
- **Claim/result cue:** We show that using this data helps achieve state-of-the-art performance on several 3D scene understanding tasks, including 3D object classification, semantic voxel labeling, and CAD model retrieval.

### Strongest assumption and failure boundary

- Explicit assumptions and negative results are not recorded in the current source note; full-text review is required.

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `observation → state/world model`.
- **Registry interface:** `3D Vision, Dataset, semantic, 3D reconstruction` is the paper's recorded topic/interface, not evidence that the full robotics loop was evaluated.
- **Prior interpretation carried forward:**
  - Geometry reconstruction, pose estimation, map update 원리를 robot의 spatial memory와 3D scene understanding 기반으로 사용할 수 있다.
  - Classical geometry/SLAM의 metric constraint는 VLM/LLM 기반 semantic reasoning이 놓치는 scale, pose, visibility 문제를 보정한다.
- Reuse the paper by preserving its input/output boundary and testing downstream success, failure, and latency under a matched baseline budget.

### Dependency and evolution

- Registry position: `Benchmarks and Datasets`; tags: `3D Vision, Dataset, semantic, 3D reconstruction`.
- A direct citation predecessor/successor is not recorded in the legacy note; confirm it from references and the track synthesis before asserting lineage.
- Recorded scope boundary/future cue:
  - 논문이 도달한 지점: We show that using this data helps achieve state-of-the-art performance on several 3D scene understanding tasks, including 3D object classification, semantic voxel labeling, and CAD model retrieval.
  - geometric accuracy 이후에도 open-vocabulary semantics, dynamic objects, learned priors, task-aware mapping은 후속 연구 지점으로 남는다.

### Minimal reproduction

- **Protocol carried forward from the legacy note (candidate, not a verified paper evaluation):**
  - 논문 내 evaluation 단서: ScanNet, ShapeNet / accuracy
  - 내 연구 확장 benchmark 후보: TUM RGB-D, EuRoC, KITTI, ScanNet
  - 내 연구 확장 metric 후보: ATE, RPE, AbsRel, RMSE
  - 검증 초점: pose/reconstruction accuracy, semantic map consistency, robot navigation/manipulation utility를 확인한다.
- Do not label a candidate benchmark, metric, or extension protocol as the paper's own evaluation until the experiment section is checked.

## Falsifiable research question

SLAM/reconstruction map에 language-aligned semantic feature를 붙여도 geometric consistency가 유지되는가?

**Reject the hypothesis if** the primary metric does not improve at a matched budget, or if the method adds latency, failure, or assumption sensitivity without a compensating closed-loop benefit.
