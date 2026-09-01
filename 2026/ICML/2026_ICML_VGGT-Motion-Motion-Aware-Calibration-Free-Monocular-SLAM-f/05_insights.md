# Insights — VGGT-Motion: Motion-Aware Calibration-Free Monocular SLAM for Long-Range Consistency

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `CURATION_ONLY`.
> Analysis basis: `CURATION_ONLY`; 01_overview의 source audit와 기존 insight cue를 이관했다: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed. 자동 추출 결과는 수동 정독으로 간주하지 않는다.

## Paper-supported conclusion

> **Evidence boundary:** 현재 내용은 registry와 기존 curation cue를 정리한 것이다. 자동 추출이나 local PDF 보유는 정독 근거로 간주하지 않으며, 상세 claim은 full-text 확인이 필요하다.

### What was actually new

- **Method cue:** To address these issues, we propose VGGT-Motion, a calibration-free SLAM system for efficient and robust global consistency over kilometer-scale trajectories.
- **Problem cue:** Motion-agnostic partitioning breaks contextual coherence and causes zero-motion drift, while conventional geometric alignment is computationally expensive.
- **Claim/result cue:** Experiments show that VGGT-Motion markedly improves trajectory accuracy and efficiency, achieving state-of-the-art performance in zero-shot, long-range calibrationfree monocular SLAM.

### Strongest assumption and failure boundary

- Explicit assumptions and negative results are not recorded in the current source note; full-text review is required.

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `observation → state/world model`.
- **Registry interface:** `geometry, depth, 3D Vision` is the paper's recorded topic/interface, not evidence that the full robotics loop was evaluated.
- **Prior interpretation carried forward:**
  - SE(3)/rotation/translation structure를 representation이나 policy에 넣어 viewpoint, pose, sensor-frame 변화에 강한 3D reasoning을 만들 수 있다.
  - Registration/calibration 관점은 multi-view, LiDAR-camera, robot-camera alignment 문제의 공통 기반으로 사용할 수 있다.
- Reuse the paper by preserving its input/output boundary and testing downstream success, failure, and latency under a matched baseline budget.

### Dependency and evolution

- Registry position: `3D Geometry, Registration, and Equivariance`; tags: `geometry, depth, 3D Vision`.
- A direct citation predecessor/successor is not recorded in the legacy note; confirm it from references and the track synthesis before asserting lineage.
- Recorded scope boundary/future cue:
  - 논문이 도달한 지점: Experiments show that VGGT-Motion markedly improves trajectory accuracy and efficiency, achieving state-of-the-art performance in zero-shot, long-range calibrationfree monocular SLAM.
  - symmetry-aware representation이 특정 task에서 성능을 보인 뒤에도 large-scale scene, language grounding, real robot noise에서의 이득은 별도 검증이 필요하다.

### Minimal reproduction

- **Protocol carried forward from the legacy note (candidate, not a verified paper evaluation):**
  - 논문 내 evaluation 단서: KITTI, Waymo / accuracy, mAP, ATE, RMSE
  - 내 연구 확장 benchmark 후보: ModelNet40, ScanNet, KITTI, nuScenes
  - 내 연구 확장 metric 후보: rotation error, translation error, mIoU, success rate
  - 검증 초점: pose robustness, calibration/registration accuracy, downstream perception/action 성능을 확인한다.
- Do not label a candidate benchmark, metric, or extension protocol as the paper's own evaluation until the experiment section is checked.

## Falsifiable research question

SE(3)-equivariant feature가 open-vocabulary 3D grounding이나 manipulation policy에서도 실제 sample efficiency를 높이는가?

**Reject the hypothesis if** the primary metric does not improve at a matched budget, or if the method adds latency, failure, or assumption sensitivity without a compensating closed-loop benefit.
