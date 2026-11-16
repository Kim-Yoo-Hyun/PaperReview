# Stable Language Guidance for Vision–Language–Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Pipeline and Representation

Paraphrase에 대한 Monte Carlo 통합과 visual affordance prior를 분리하는 residual semantic steering을 결합한다.

시각 관측·언어 표현들의 분포 → 의미/affordance 분리 추론 → VLA 행동. 검색한 demo를 바꾸는 개입과 현재 지시를 바꾸는 개입은 다르다.

## Training vs Inference

semantic prior 제거 방식·추가 decode 비용·paraphrase 정답 정보·평가 instruction 분리을 확인해 추가 supervision과 실제 배포 입력을 분리한다. 공개 code link의 존재를 재현 성공으로 간주하지 않는다.

## Objective and Temporal Contract

Exact loss/control law, optimizer, action horizon, control rate와 memory budget은 이번 abstract/project 확인에서 확정하지 않았다. [평가 조건](./04_evaluation.md)과 함께 읽는다.

근거: [공식 paper/abstract](https://aclanthology.org/2026.acl-long.190/) · [저자 project](https://github.com/Doo-mon/RSS).
