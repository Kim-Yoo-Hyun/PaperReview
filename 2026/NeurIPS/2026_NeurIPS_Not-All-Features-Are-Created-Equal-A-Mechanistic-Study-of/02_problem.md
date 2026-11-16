# Problem — Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Target Problem

언어·시각 표현과 실제 운동 생성 사이의 관계를 intervention으로 조사한다.

## Robotics Loop

관측·언어 → VLA 내부 activation → 개입된 action expert → 행동. 주입된 정책과 정상 정책을 구분한다.

## Assumptions to Check — Researcher Interpretation

연구자 점검: 인위적 activation 개입의 효과를 자연 학습 메커니즘으로 일반화하지 않는다.

개념 연결: OpenVLA·π0.5 → mechanistic steering → RL4VLA 후학습 진단.

## Boundary

하드웨어 결과는 한 모델·task pair에 제한된다. 좌표계 해석과 off-manifold 개입의 영향을 분리해야 한다. 모든 정상 VLA가 피드백을 무시한다는 증거가 아니다.

근거: [확인한 원문](https://arxiv.org/pdf/2603.19233v6), v6 (2026-11-02), §4.7–4.8, Appendix B.
