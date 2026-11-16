# SAGA: Open-World Mobile Manipulation via Structured Affordance Grounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Target Problem and Bottleneck

다양한 지시와 환경을 하나의 이동 조작 제어기로 연결할 때 semantic intent와 시각 변동을 분리한다.

## Changed Formulation

[방법](./03_method.md)의 입력과 학습/배포 개입을 구분해 선행과 비교한다. 단순 성공률 향상보다 어떤 정보가 언제 추가되는지가 비교의 기준이다.

## Assumptions to Verify — Researcher Interpretation

affordance 생성 오차·policy가 받는 GT·whole-body action 공간·zero/few-shot split.

이는 본문에서 확인할 질문이며 논문이 직접 인정한 실패 목록이 아니다.

## Position in the Robotics Loop

언어·지정 point·예시 시연 → 관측에 정렬된 affordance → quadrupedal manipulator의 whole-body 행동.

정확한 sensor·state·action frame 및 controller 경계는 본문 확인 전 확정하지 않는다.

근거: [공식 paper/abstract](https://ieeexplore.ieee.org/document/11568510/) · [저자 project](https://robot-saga.github.io/).
