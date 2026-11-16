# LILAC: Language-Conditioned Object-Centric Optical Flow for Open-Loop Trajectory Generation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Target Problem and Bottleneck

사람/웹 영상에서 얻은 움직임을 언어에 맞는 로봇 궤적으로 변환하는 데 필요한 정렬을 다룬다.

## Changed Formulation

[방법](./03_method.md)의 입력과 학습/배포 개입을 구분해 선행과 비교한다. 단순 성공률 향상보다 어떤 정보가 언제 추가되는지가 비교의 기준이다.

## Assumptions to Verify — Researcher Interpretation

2D→6-DoF 변환·embodiment별 calibration·실행 feedback. 공식 abstract와 project 본문의 loss/adapter 명칭이 달라 원문 version 확인 필요.

이는 본문에서 확인할 질문이며 논문이 직접 인정한 실패 목록이 아니다.

## Position in the Robotics Loop

단일 초기 RGB·지시 → motion flow → 로봇 궤적. Open-loop 궤적 생성과 실행 중 feedback/replanning은 구분한다.

정확한 sensor·state·action frame 및 controller 경계는 본문 확인 전 확정하지 않는다.

근거: [공식 paper/abstract](https://ieeexplore.ieee.org/abstract/document/11478289) · [저자 project](https://lilac-75srg.kinsta.page/).
