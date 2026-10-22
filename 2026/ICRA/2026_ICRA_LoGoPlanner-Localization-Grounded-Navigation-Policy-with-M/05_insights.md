# LoGoPlanner: Localization Grounded Navigation Policy with Metric-aware Visual Geometry

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Visual geometry backbone을 metric scale에 맞추고 history 기반 geometry를 복원하여 navigation policy를 conditioning한다.

저자 abstract/project는 simulation과 real-world navigation, obstacle avoidance 및 embodiment/environment generalization 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2512.19629) · [저자 project/code](https://steinate.github.io/logoplanner.github.io/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 정책과 MPC가 각각 보는 pose, calibration, simulator GT 접근 및 metric scale supervision은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Current trend / enabling 3D. Metric-aware geometry와 history 기반 state estimation을 trajectory planning에 연결한다. 일반 reconstruction보다 현재 navigation 목표에 직접적이다. Controller가 실제 사용하는 pose·calibration·simulator GT의 범위는 본문/배포 코드 확인이 필요하다.

### Dependency and Evolution

NavDP + metric 3D memory → LoGoPlanner; VLFM/VLN-CE와 representation 비교.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

Geometry memory 유무를 동일 camera와 controller로 비교하고 pose noise·occlusion 하에서 success·collision·latency를 측정한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

Geometry memory의 이득이 외부 pose/oracle 입력을 통제해도 남는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
