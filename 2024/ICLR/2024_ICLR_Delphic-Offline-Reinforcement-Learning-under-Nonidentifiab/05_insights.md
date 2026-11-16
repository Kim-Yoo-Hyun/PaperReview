# Delphic Offline Reinforcement Learning under Nonidentifiable Hidden Confounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

관측과 양립하는 world model 간 차이로 confounding 불확실성을 정의하고 보수적 RL에 반영한다.

Sepsis benchmark와 의료 기록에서 평가하며 robot/VLA 효과를 검증한 논문은 아니다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2024/hash/0b9ff9baa226af39f86045ecdc173672-Abstract-Conference.html). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 비식별성 가정, uncertainty estimator, pessimism 수준, 의료→로봇 적용 한계은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

로봇 시연의 숨은 정보 문제를 단순 모델 불확실성과 혼동하지 않게 하는 방법론 참조다.

### Dependency and Evolution

Offline RL pessimism → Delphic uncertainty; DML-IL과 식별 가정 비교.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

숨은 cue가 있는 작은 환경에서 관측 적합도와 counterfactual action ranking을 따로 검사한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

동일 관측 기록에 양립하는 원인 모델들이 다른 최적 action을 요구하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
