# Lifelong Autonomous Improvement of Navigation Foundation Models in the Wild

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Offline RL 사전학습과 지속적인 자율 운영·online 적응을 하나의 항법 학습 시스템으로 구성한다.

실세계 open-world 항법 배포에서 자율 수집 데이터로 적응하는 시스템을 보고한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v270/stachowicz25a.html) · [저자 project/code](https://github.com/kylestach/lifelong-nav-rl). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 목표 생성·reset·인간 개입의 범위, 정책 입력의 언어 여부, 이전 장소 회귀은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

VLA+RL의 지속 학습을 manipulation에 한정하지 않고 실제 항법 운영 조건과 비교할 기준이다.

### Dependency and Evolution

NoMaD·ViNT의 navigation foundation과 RLPD의 offline-to-online 학습을 함께 비교한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 사전학습 정책에서 offline 고정·최근 데이터 모방·online RL을 비교하고 이전 장소를 재평가한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

배포 장소의 적응 이득이 새 장소의 성능 유지와 양립하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
