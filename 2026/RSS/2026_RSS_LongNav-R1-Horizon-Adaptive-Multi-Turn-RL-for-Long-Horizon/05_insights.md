# LongNav-R1: Horizon-Adaptive Multi-Turn RL for Long-Horizon VLA Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

환경과의 multi-turn 상호작용 및 horizon을 반영한 advantage 추정으로 VLA를 학습한다.

Object navigation과 실제 장기 항법의 zero-shot 평가를 보고한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p068.html) · [저자 project/code](https://github.com/UMich-CURLY/LongNav-R1). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 action 단위, episode 길이별 정규화, rollout 분모, 실제 로봇의 저수준 제어기은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

조작에서 설계한 VLA+RL 목적함수가 항법의 긴 시간축에도 유효한지 비교할 직접 선행이다.

### Dependency and Evolution

PPO/GRPO·SimpleVLA-RL의 rollout 최적화를 장기 navigation credit assignment와 비교한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 초기 정책·상호작용 수에서 advantage 계산과 history 사용만 각각 바꿔 길이별 성공을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

성공률 이득이 horizon-aware advantage에서 오는가, 더 다양한 multi-turn rollout에서 오는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
