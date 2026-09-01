# Insights — Bootstrapping Reinforcement Learning with Imitation for Vision-Based Agile Flight

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `CURATION_ONLY`.
> Analysis basis: `CURATION_ONLY`; 01_overview의 source audit와 기존 insight cue를 이관했다: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed. 자동 추출 결과는 수동 정독으로 간주하지 않는다.

## Paper-supported conclusion

> **Evidence boundary:** 현재 내용은 registry와 기존 curation cue를 정리한 것이다. 자동 추출이나 local PDF 보유는 정독 근거로 간주하지 않으며, 상세 claim은 full-text 확인이 필요하다.

### What was actually new

- **Method cue:** To address these challenges, we propose a novel approach that combines the performance of Reinforcement Learning (RL) and the sample efficiency of Imitation Learning (IL) in the task ...
- **Problem cue:** Thus, the ability to explore and learn efficiently in vision-based RL environments from scratch is essential, presenting a key challenge that our research seeks to overcome.
- **Claim/result cue:** Testing in both simulated and real-world scenarios shows our approach can not only learn in scenarios where RL from scratch fails but also outperforms existing IL methods in ...

### Strongest assumption and failure boundary

- Explicit assumptions and negative results are not recorded in the current source note; full-text review is required.

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `observation → state/world model`.
- **Registry interface:** `Robotics, aerial robotics, Reinforcement Learning, Imitation Learning` is the paper's recorded topic/interface, not evidence that the full robotics loop was evaluated.
- Reuse the paper by preserving its input/output boundary and testing downstream success, failure, and latency under a matched baseline budget.

### Dependency and evolution

- Registry position: `Locomotion, Whole-Body, and Mobile Manipulation`; tags: `Robotics, aerial robotics, Reinforcement Learning, Imitation Learning`.
- A direct citation predecessor/successor is not recorded in the legacy note; confirm it from references and the track synthesis before asserting lineage.
- Recorded scope boundary/future cue:
  - 논문이 도달한 지점: Testing in both simulated and real-world scenarios shows our approach can not only learn in scenarios where RL from scratch fails but also outperforms existing IL methods in ...

### Minimal reproduction

- **Protocol carried forward from the legacy note (candidate, not a verified paper evaluation):**
  - 논문 내 evaluation 단서: ImageNet / mAP, SR, success rate, collision
  - 내 연구 확장 benchmark 후보: ScanNet, Matterport3D, nuScenes, CALVIN
  - 내 연구 확장 metric 후보: mIoU, accuracy, success rate, generalization gap
  - 검증 초점: paper task 성능과 3D/robotics downstream utility를 함께 확인한다.
- Do not label a candidate benchmark, metric, or extension protocol as the paper's own evaluation until the experiment section is checked.

## Falsifiable research question

고정된 sensor·compute budget에서 Robotics, aerial robotics, Reinforcement Learning, Imitation Learning 기반 표현이 robot-relevant state 품질과 downstream task success를 sensor noise와 partial observation 아래 개선하는가?

**Reject the hypothesis if** the primary metric does not improve at a matched budget, or if the method adds latency, failure, or assumption sensitivity without a compensating closed-loop benefit.
