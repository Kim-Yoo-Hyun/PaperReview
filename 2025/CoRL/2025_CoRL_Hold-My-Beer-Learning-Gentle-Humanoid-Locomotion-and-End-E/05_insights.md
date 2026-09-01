# Insights — Hold My Beer: Learning Gentle Humanoid Locomotion and End-Effector Stabilization Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `CURATION_ONLY`.
> Analysis basis: `CURATION_ONLY`; 01_overview의 source audit와 기존 insight cue를 이관했다: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed. 자동 추출 결과는 수동 정독으로 간주하지 않는다.

## Paper-supported conclusion

> **Evidence boundary:** 현재 내용은 registry와 기존 curation cue를 정리한 것이다. 자동 추출이나 local PDF 보유는 정독 근거로 간주하지 않으며, 상세 claim은 full-text 확인이 필요하다.

### What was actually new

- **Method cue:** To address this, we propose SoFTA, a Slow-Fast Two-Agent framework that decouples upper-body and lower-body control into separate agents operating at different frequencies and with distinct rewards.
- **Problem cue:** While humanoids are increasingly featured in flashy demos—dancing, delivering packages, traversing rough terrain—fine-grained control during locomotion remains a significant challenge.
- **Claim/result cue:** Our experiments aim to answer the following key questions: • Q1 (Section 4.1): Can the Two-Agent design of SoFTA perform better in simulation? • Q2 (Section 4.2): What ...

### Strongest assumption and failure boundary

- Explicit assumptions and negative results are not recorded in the current source note; full-text review is required.

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `task & motion decision → policy/control`.
- **Registry interface:** `Robotics, humanoid, locomotion, end-effector stabilization, multi-rate control` is the paper's recorded topic/interface, not evidence that the full robotics loop was evaluated.
- Reuse the paper by preserving its input/output boundary and testing downstream success, failure, and latency under a matched baseline budget.

### Dependency and evolution

- Registry position: `Locomotion, Whole-Body, and Mobile Manipulation`; tags: `Robotics, humanoid, locomotion, end-effector stabilization, multi-rate control`.
- A direct citation predecessor/successor is not recorded in the legacy note; confirm it from references and the track synthesis before asserting lineage.
- Recorded scope boundary/future cue:
  - 논문이 도달한 지점: Our experiments aim to answer the following key questions: • Q1 (Section 4.1): Can the Two-Agent design of SoFTA perform better in simulation? • Q2 (Section 4.2): What ...

### Minimal reproduction

- **Protocol carried forward from the legacy note (candidate, not a verified paper evaluation):**
  - 논문 내 evaluation 단서: 자동 추출에서 명확한 dataset 단서 없음 / 자동 추출에서 명확한 metric 단서 없음
  - 내 연구 확장 benchmark 후보: ScanNet, Matterport3D, nuScenes, CALVIN
  - 내 연구 확장 metric 후보: mIoU, accuracy, success rate, generalization gap
  - 검증 초점: paper task 성능과 3D/robotics downstream utility를 함께 확인한다.
- Do not label a candidate benchmark, metric, or extension protocol as the paper's own evaluation until the experiment section is checked.

## Falsifiable research question

고정된 state, action, compute budget에서 Robotics, humanoid, locomotion, end-effector stabilization, multi-rate control formulation이 task cost 또는 success를 유지하면서 perturbation 이후 recovery를 개선하는가?

**Reject the hypothesis if** the primary metric does not improve at a matched budget, or if the method adds latency, failure, or assumption sensitivity without a compensating closed-loop benefit.
