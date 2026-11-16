# LIBERO-X: Robustness Litmus for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Pipeline and Representation

난이도별 복합 교란 평가와 장면당 여러 조작 목표를 포함하는 teleoperation 데이터를 결합한 benchmark를 제시한다.

공간 배치·물체 속성·지시 표현을 바꾼 관측과 task → VLA 행동 → 다차원 label별 평가.

## Training vs Inference

train/evaluation scene 중복·difficulty별 sample 수·실제 init state 공개 범위·predicate 정의을 확인해 추가 supervision과 실제 배포 입력을 분리한다. 공개 code link의 존재를 재현 성공으로 간주하지 않는다.

## Objective and Temporal Contract

Exact loss/control law, optimizer, action horizon, control rate와 memory budget은 이번 abstract/project 확인에서 확정하지 않았다. [평가 조건](./04_evaluation.md)과 함께 읽는다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p097.html) · [저자 project](https://meituan.github.io/LIBERO-X/).
