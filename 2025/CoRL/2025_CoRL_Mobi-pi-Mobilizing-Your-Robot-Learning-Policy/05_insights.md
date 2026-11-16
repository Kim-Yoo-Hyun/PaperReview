# Mobi-π: Mobilizing Your Robot Learning Policy

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

정책을 다시 학습하는 대신 실행할 base pose를 찾는 policy mobilization을 정식화한다. 3D Gaussian Splatting의 새 시점 영상, pose 적합도와 sampling 기반 최적화를 연결한다.

RoboCasa 기반 simulated mobile manipulation과 실로봇에서 pose 선택을 비교한다. 이 비교만으로 다른 정책에 선택된 pose를 재사용할 때의 성능을 확정할 수 없다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/yang25b.html) · [저자 project/code](https://mobipi.github.io/) · [공식 code](https://github.com/yjy0625/mobipi). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 pose 후보와 collision/reachability 처리, 정책별 학습 시야와 데이터 접근, 장면 구축 비용, 실제 도착 상태·평가 분모은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Mobile ALOHA의 whole-body 데이터와 MoTo의 이동–조작 연결을 보완하며, HANDOFF의 정책별 도착 조건을 비교할 직접 선행이다.

### Dependency and Evolution

Mobile ALOHA → 이동 후 정책 실행 조건; MoTo ↔ Mobi-π의 policy-aware navigation/base placement 비교; 3DGS → 행동을 위한 시점 합성.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 scene·도착 후보·navigation·비용에서 A 선택 재사용, 정책 무관 고정 pose, 제한된 B validation 재선택을 비교한다. 실제 이동 후 상태를 분기하고 전체 시도 분모를 보존한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

정책 A에 맞춰 고른 base pose가 정책 B에서도 유효한가, 그리고 소수의 B validation으로 재선택하는 단순 대안이 재사용 손실을 줄이는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
