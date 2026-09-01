# Insights — Learning to Be Uncertain: Pre-training World Models with Horizon-Calibrated Uncertainty

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `CURATION_ONLY`.
> Analysis basis: `CURATION_ONLY`; 기존 insight cue와 registry metadata만 이관했다. 자동 추출 결과는 수동 정독으로 간주하지 않는다.

## Paper-supported conclusion

> **Evidence boundary:** 현재 내용은 registry와 기존 curation cue를 정리한 것이다. 자동 추출이나 local PDF 보유는 정독 근거로 간주하지 않으며, 상세 claim은 full-text 확인이 필요하다.

### What was actually new

- **Claim recorded in prior note:** 논문의 중심 claim은 기존 2D-only, closed-set, 또는 task-specific 접근보다 더 일반화 가능한 3D-aware representation/policy/reasoning을 제공한다는 것이다.
- **Claim recorded in prior note:** Abstract result cue: 자동 추출 없음.
- **Strength recorded in prior note:** `robot manipulation and vision-language-action control` 문제를 3D geometry와 language/action prior를 함께 쓰는 방향으로 밀어붙인다.
- **Strength recorded in prior note:** 사용자의 연구 키워드 중 `Robotics, world model, uncertainty, long-horizon prediction, model-based reinforcement learning`와 직접적으로 연결된다.

### Strongest assumption and failure boundary

- 실제 로봇 배치에서는 센서 calibration, latency, safety, embodiment mismatch, 실패 복구가 추가 변수다.

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `observation → state/world model → decision/recovery`.
- **Registry interface:** `Robotics, world model, uncertainty, long-horizon prediction, model-based reinforcement learning` is the paper's recorded topic/interface, not evidence that the full robotics loop was evaluated.
- **Prior interpretation carried forward:**
  - 이 논문은 `Uncertainty-Aware Robot World Models` 축에서 읽어야 한다.
  - 후속 연구 아이디어: language-grounded 3D memory를 만들고, robot policy가 이를 action feasibility와 uncertainty까지 포함해 조회하도록 설계한다.
- Reuse the paper by preserving its input/output boundary and testing downstream success, failure, and latency under a matched baseline budget.

### Dependency and evolution

- Registry position: `World Models, Safety, and Recovery`; tags: `Robotics, world model, uncertainty, long-horizon prediction, model-based reinforcement learning`.
- A direct citation predecessor/successor is not recorded in the legacy note; confirm it from references and the track synthesis before asserting lineage.
- Recorded scope boundary/future cue:
  - dynamic scene, partial observation, sensor noise, cross-embodiment transfer, real-time inference, safety-aware planning을 추가 검증하는 것이 중요하다.
  - 3D scene graph/semantic Gaussian/SLAM map을 VLA policy의 persistent memory로 연결하는 방향이 유망하다.

### Minimal reproduction

1. Confirm the paper-reported input, output, task, metric, baseline, and split from the full text.
2. Implement the smallest paper-specific component and a simpler matched baseline.
3. Evaluate the primary paper metric plus failure rate, latency, and sensitivity to the assumption most central to the method.
- Do not label a candidate benchmark, metric, or extension protocol as the paper's own evaluation until the experiment section is checked.

## Falsifiable research question

고정된 sensor·compute budget에서 Robotics, world model, uncertainty, long-horizon prediction, model-based reinforcement learning 기반 표현이 robot-relevant state 품질과 downstream task success를 sensor noise와 partial observation 아래 개선하는가?

**Reject the hypothesis if** the primary metric does not improve at a matched budget, or if the method adds latency, failure, or assumption sensitivity without a compensating closed-loop benefit.
