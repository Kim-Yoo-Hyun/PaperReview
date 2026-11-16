# Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Offline RL로 학습한 value를 사용하여 범용 정책이 생성한 행동 후보를 추론 시 선택한다.

서로 다른 다섯 정책과 여러 실제 로봇·조작 과제에서 value guidance를 평가한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v270/nakamoto25a.html) · [저자 project/code](https://nakamotoo.github.io/V-GPS) · [공식 code](https://github.com/nakamotoo/V-GPS). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 후보 수와 latency, value 데이터 범위, 정책별 action normalization은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

단일 정책을 RL로 갱신하는 방법이 추론 후보 선택보다 필요한 이유를 검증할 직접 대조군이다.

### Dependency and Evolution

IQL·Cal-QL의 value 학습과 OpenVLA·Octo의 generalist action interface를 연결해 읽는다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 데이터·critic·추론 계산량에서 고정 actor+reranking과 RL actor update를 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

정책 갱신의 이득이 같은 value를 쓴 sample reranking으로 설명되는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
