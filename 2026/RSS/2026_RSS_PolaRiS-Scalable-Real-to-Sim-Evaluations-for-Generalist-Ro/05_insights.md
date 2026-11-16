# PolaRiS: Scalable Real-to-Sim Evaluations for Generalist Robot Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

짧은 실환경 스캔으로 시뮬레이터를 만들고 simulation co-training으로 잔여 차이를 줄인다.

실제·시뮬레이션의 짝지은 rollout으로 정책 순위 상관을 평가한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p062.html) · [저자 project/code](https://polaris-evals.github.io/) · [공식 code](https://github.com/arhanjain/PolaRiS). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 평가 전에 허용된 co-training 데이터, 독립 실환경 trial, 장면 선택 편향은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

SIMPLER·RoboCasa의 점수를 실제 개선으로 해석하기 전 필요한 평가 타당성 비교다.

### Dependency and Evolution

SIMPLER의 시각적 sim-to-real 평가와 DROID 기반 generalist 정책을 연결하는 비교 축..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 checkpoint들을 동일 task의 실환경·재구성 환경에서 비교하고 co-training 전후 순위를 별도로 계산한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

새 RL 방법의 시뮬레이터상 순위가 환경 재구성 방식에 따라 뒤집히는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
