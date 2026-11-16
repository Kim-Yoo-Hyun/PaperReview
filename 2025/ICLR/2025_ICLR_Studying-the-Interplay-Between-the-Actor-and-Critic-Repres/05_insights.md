# Studying the Interplay Between the Actor and Critic Representations in Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

공유/분리 표현과 각 역할의 전문화를 비교한다. 별도 critic은 탐색과 수집 데이터에도 영향을 준다고 보고한다.

공식 abstract의 표현·downstream 성능 비교까지 확인. 세부 환경·seed·수치·모델 용량 통제는 본문 대조 필요.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2025/hash/57da66da25d0ce77e0129b246f358851-Abstract-Conference.html) · [저자 project/code](https://github.com/francelico/deac-rep). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 환경별 capacity·optimizer·data collection 통제, VLA에 그대로 적용 가능한 결론의 범위은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

U1의 일반 actor–critic 표현 간섭 주장이 새롭지 않음을 보여 주는 필수 비교다. VLA 언어 목표 조건의 추가 기여를 정의하기 위해 NEXT에 추가한다.

### Dependency and Evolution

개념 비교: PPO·PPG → 표현 공유/분리 → VLA의 instruction-conditioned 학습 질문.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 초기 정책·고정 old log-prob/return/advantage의 단일 update 진단과 각 조건의 on-policy 학습을 별도로 평가한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 transition의 직접 gradient 효과와 critic이 바꾼 수집 데이터의 효과를 어떻게 분리할 것인가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
