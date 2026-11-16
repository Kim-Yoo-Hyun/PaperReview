# CE-Nav: Flow-Guided Reinforcement Refinement for Cross-Embodiment Local Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Planner 데이터로 embodiment-agnostic flow expert를 학습하고 이를 고정한 채 로봇별 경량 refiner를 online RL로 적응한다.

사족·이족·quadrotor 실험과 실제 배포를 보고한다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/514bdfb12b318ad02c6f28dc68f2feea-Abstract-Conference.html) · [저자 project/code](https://github.com/amap-cvlab/CE-Nav). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 planner 관측 접근, dynamics별 상호작용 분모, morphology별 평가 조건은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Cross-embodiment VLA-RL의 필요성을 검증할 기하 prior+동역학 적응 기준이다.

### Dependency and Evolution

ViNT·NoMaD·RMA와 embodiment adaptation의 정보 및 계층 경계를 비교한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 planner 데이터·online budget에서 frozen prior+refiner와 공동 정책 갱신을 대조한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

단일 정책의 이득이 로봇별 경량 refiner보다 적은 상호작용으로 나타나는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
