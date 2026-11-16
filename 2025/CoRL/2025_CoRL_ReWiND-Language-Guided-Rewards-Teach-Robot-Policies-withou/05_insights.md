# ReWiND: Language-Guided Rewards Teach Robot Policies without New Demonstrations

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

소규모 시연으로 언어 조건부 reward와 offline 정책을 학습하고 새 과제에 online 적응한다.

Simulation과 실제 양팔 조작의 미관측 과제 적응을 평가한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/zhang25a.html) · [저자 project/code](https://rewind-reward.github.io/) · [공식 code](https://github.com/rewind-reward/ReWiND). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 사전학습 시연·외부 데이터 사용량, reward leakage, 신규 과제별 인간 감독은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

새 VLA-RL 보상이나 실패 재사용이 기존 언어 보상 일반화와 어떻게 다른지 비교할 선행이다.

### Dependency and Evolution

LIV·RoboCLIP·SPRINT와 언어 보상 및 데이터 재사용 관점에서 비교한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 초기 정책에 학습 보상과 환경 보상을 각각 사용하고 unseen instruction을 별도 평가한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

새 목표 적응의 이득이 보상 일반화에서 오는가, 초기 정책 competence에서 오는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
