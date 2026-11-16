# Restoring Linguistic Grounding in VLA Models via Train-Free Attention Recalibration

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

ICBench로 같은 장면의 모순 지시를 진단하고 추론 시 attention을 재조정하여 언어 영향을 복원한다.

π0·π0.5·OpenVLA-OFT, LIBERO task와 실제 Franka에서 지시 모순에 따른 잘못된 실행을 평가한다.

근거: [공식 paper/abstract](https://link.springer.com/chapter/10.1007/978-3-032-37152-2_3) · [저자 project/code](https://ray-nh.github.io/igar/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 모순의 정답 정의, 무조건 정지 대조, 정상 지시 성능 trade-off은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

RL 이후 성공률이 언어 grounding을 보장하지 않는다는 직접 평가·간단 대안이다.

### Dependency and Evolution

CAST·Contrast Sets·OpenVLA와 instruction consistency를 함께 비교한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

정상/모순 지시 paired set에서 SFT, RL, RL+IGAR를 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

RL 후학습이 정상 성공과 모순 지시 거부 능력을 동시에 개선하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
