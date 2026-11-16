# General agents need world models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

일반화 가능한 정책에서 예측 world model을 추출할 수 있음을 이론적으로 분석한다.

공식 abstract는 다단계 목표·성능과 모델 정확도의 이론적 관계를 제시한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v267/richens25a.html). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 일반화·목표 집합 정의, 추출 접근 권한, 정리 조건과 실제 로봇 적용 범위은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

명시적 video model 사용과 정책에 내재한 예측 능력을 구별하는 AI 이론 참조다.

### Dependency and Evolution

Model-based/model-free RL → general-agent world-model 필요성 → WorldTest.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

유한 환경에서 theorem 가정을 먼저 고정하고 policy-derived prediction과 별도 모델을 대조한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

정책의 예측 가능 정보와 별도 world-model 모듈의 실제 제어 이득은 어떻게 구별되는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
