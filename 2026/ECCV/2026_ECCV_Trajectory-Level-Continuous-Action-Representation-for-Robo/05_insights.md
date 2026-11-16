# Trajectory-Level Continuous Action Representation for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

고정된 실제 시간 구간의 궤적을 continuous latent token으로 압축하고 주파수를 고려한 위치 표현을 사용한다.

LIBERO·MimicGen·실제 장시간 조작에서 backbone과 control frequency를 바꿔 비교한다.

근거: [공식 paper/abstract](https://link.springer.com/chapter/10.1007/978-3-032-37369-4_24). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 미확인 항목: 시간 구간·normalizer·주파수 학습 노출·동일 episode 내 변경 평가 유무.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

제어 간격·물리 시간 조건부 행동 표현 자체를 새 공백으로 오인하지 않게 하는 기준이다.

### Dependency and Evolution

FAST·continuous action representation·고주파 latent chunk와 물리 시간 정렬을 비교한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

정상 주기와 episode 중간 주기 변경을 구별하고 동일 시간·경로에서 행동 오차와 성공을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

주기 간 표현 일관성이 실행 도중 관측 지연·주기 변화의 행동 안정성까지 보장하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
