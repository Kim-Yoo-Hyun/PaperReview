# Towards Long-Lived Robots: Continual Learning VLA Models via Reinforcement Fine-Tuning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

행동 chunk의 이산 일치·연속 궤적 정렬·출력 형식 보상으로 reinforcement fine-tuning한다.

SimplerEnv·LIBERO 및 실제 조작, LIBERO continual learning을 보고한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p086.html). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 참조 궤적 의존성, rehearsal 여부, 순차 task order, 보상별 효과은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

환경 return 최적화와 참조 행동 기반 RLVR을 구별하기 위한 직접 비교다.

### Dependency and Evolution

OpenVLA/OFT의 SFT와 continual VLA 연구를 연결하되 online 환경 RL과 동일시하지 않는다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 참조 데이터로 SFT, 동일 가중 회귀, chunk RL을 비교하고 새·기존 과제를 함께 평가한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

기존 능력 보존 이득이 RL estimator보다 행동 일치 objective·replay 구성에서 발생하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
