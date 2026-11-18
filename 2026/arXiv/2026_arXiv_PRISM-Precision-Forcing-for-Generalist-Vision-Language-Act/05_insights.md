# PRISM: Precision Forcing for Generalist Vision-Language-Action Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

시연의 proprioception으로 정밀도 요구를 점수화하고 flow supervision과 VLM 조건 표현 학습에 반영한다. 저자 project는 학습용 보조 head/label을 추론에서 제거한다고 설명한다.

초록·project는 simulation과 실제 로봇의 connector insertion, 양팔 connector mating, screw tightening을 보고한다. Trial 수·task별 분모·성공 정의와 수치 비교는 본문 대조 전 미확정이다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.14704) · [저자 project/code](https://seen-e.github.io/PRISM/) · [공식 code](https://github.com/seen-e/PRISM). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 정밀도 proxy와 실제 공차의 차이·flow-time weighting·SNR gate·auxiliary loss·task별 trial·공개 구현의 논문 일치은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

작업 허용 오차에 따른 학습 가중과 표현 내재화를 이미 다룬 직접 NEXT다. 일반 tolerance-weighted VLA 학습을 새 기여로 주장하지 않도록 한다.

### Dependency and Evolution

Flow Matching·π₀ 계열 action expert → precision-conditioned supervision/representation → geometry estimator의 별도 잔여 기여 심사. Registry의 pr-0458 depth PRISM과 다른 연구다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

Action-expert 재가중과 geometry adapter 학습을 동일 데이터/label/compute에서 분리하고 정밀도별 성공·일반 task 유지 성능을 함께 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 정밀도 신호·학습량에서 geometry estimator 변경이 정책의 supervision 재가중보다 추가 이득을 주는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
