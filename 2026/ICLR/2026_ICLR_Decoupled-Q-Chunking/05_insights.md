# Decoupled Q-Chunking

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Critic이 평가하는 chunk 길이와 actor가 출력하는 chunk 길이를 분리한다.

최종 paper의 abstract와 공식 code는 장기 offline goal-conditioned task 평가를 설명한다. 실제 로봇 contact 평가 여부는 확인 필요.

근거: [공식 paper/abstract](https://openreview.net/pdf/bde79a617f6c016e2c51c7771416933c0646102c.pdf) · [저자 project/code](https://github.com/ColinQiyangLi/dqc). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 부분 chunk value 추정, policy extraction objective, reactive 평가의 실제 포함 여부은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Current trend. Critic과 actor의 chunk 길이를 분리한다. Q-chunking의 value propagation 이점과 짧은 action horizon의 반응성 사이의 설계 문제를 직접 다룬다. 실제 contact feedback 성능으로의 확장은 본문/실험 확인이 필요하다.

### Dependency and Evolution

Q-chunking → DQC; action horizon과 value horizon 분리.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

Q-chunking과 DQC의 critic horizon·data를 맞추고 actor chunk만 변경해 성공률 및 관측 외란 이후 회복을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

Critic horizon을 고정하고 actor chunk를 줄이면 장기 task 성능을 유지하면서 외란 대응이 빨라지는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
