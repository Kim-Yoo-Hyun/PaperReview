# SAGA: Open-World Mobile Manipulation via Structured Affordance Grounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Pipeline and Representation

Task를 구조화된 affordance로 표현하고 관측의 3D heatmap에 grounding하여 whole-body 조작 정책을 조건화한다.

언어·지정 point·예시 시연 → 관측에 정렬된 affordance → quadrupedal manipulator의 whole-body 행동.

## Training vs Inference

affordance 생성 오차·policy가 받는 GT·whole-body action 공간·zero/few-shot split을 확인해 추가 supervision과 실제 배포 입력을 분리한다. 공개 code link의 존재를 재현 성공으로 간주하지 않는다.

## Objective and Temporal Contract

Exact loss/control law, optimizer, action horizon, control rate와 memory budget은 이번 abstract/project 확인에서 확정하지 않았다. [평가 조건](./04_evaluation.md)과 함께 읽는다.

근거: [공식 paper/abstract](https://ieeexplore.ieee.org/document/11568510/) · [저자 project](https://robot-saga.github.io/).
