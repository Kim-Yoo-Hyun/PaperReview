# LILAC: Language-Conditioned Object-Centric Optical Flow for Open-Loop Trajectory Generation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Pipeline and Representation

언어와 RGB로 object-centric 2D flow를 생성하고 이를 6-DoF 로봇 trajectory로 변환한다.

단일 초기 RGB·지시 → motion flow → 로봇 궤적. Open-loop 궤적 생성과 실행 중 feedback/replanning은 구분한다.

## Training vs Inference

2D→6-DoF 변환·embodiment별 calibration·실행 feedback. 공식 abstract와 project 본문의 loss/adapter 명칭이 달라 원문 version 확인 필요을 확인해 추가 supervision과 실제 배포 입력을 분리한다. 공개 code link의 존재를 재현 성공으로 간주하지 않는다.

## Objective and Temporal Contract

Exact loss/control law, optimizer, action horizon, control rate와 memory budget은 이번 abstract/project 확인에서 확정하지 않았다. [평가 조건](./04_evaluation.md)과 함께 읽는다.

근거: [공식 paper/abstract](https://ieeexplore.ieee.org/abstract/document/11478289) · [저자 project](https://lilac-75srg.kinsta.page/).
