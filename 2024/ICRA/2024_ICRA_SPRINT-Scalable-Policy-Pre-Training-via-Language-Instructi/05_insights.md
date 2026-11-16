# SPRINT: Scalable Policy Pre-Training via Language Instruction Relabeling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

LLM을 이용한 지시 재라벨과 서로 다른 궤적의 기술 연결을 offline RL 사전학습에 사용한다.

저자 abstract는 가정용 시뮬레이터와 실제 로봇 주방 조작의 장기 과제 적응을 보고한다. 공개 저장소는 ALFRED-RL simulation 경로를 안내한다.

근거: [공식 paper/abstract](https://doi.org/10.1109/ICRA57147.2024.10610606) · [저자 project/code](https://clvrai.github.io/sprint/) · [공식 code](https://github.com/clvrai/sprint). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 cross-trajectory 연결의 유효성, downstream adaptation 예산, 시뮬레이터와 실로봇의 서로 다른 행동 interface, code의 실제 공개 범위은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

언어 재라벨·기술 조합을 최근 VLA RL만의 신규성으로 오인하지 않게 하는 offline 학습 선행이다.

### Dependency and Evolution

Offline goal-conditioned RL·장기 skill learning → SPRINT → VLA hindsight 재사용 비교. 온라인 정책 효과와 offline pretraining의 추정 대상은 다르다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 원 trajectory와 학습 예산에서 기존 라벨·재라벨만·chaining만·둘 모두를 대조하고 새 장기 과제 성공과 사용 데이터량을 함께 평가한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

새 언어 라벨의 이득은 의미적 다양성 때문인가, skill chaining으로 늘어난 유효 행동·과제 coverage 때문인가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
