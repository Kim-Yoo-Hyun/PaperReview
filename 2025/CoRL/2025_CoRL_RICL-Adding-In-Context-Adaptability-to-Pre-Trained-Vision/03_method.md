# RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Pipeline and Representation

소규모 robot 시연으로 in-context 적응 능력을 후학습하고, 배포 시 관련 시연 구간을 검색해 정책 문맥에 제공한다.

현재 관측·지시와 검색된 시연 → π0-FAST 기반 정책 → 로봇 행동. ICL 능력을 만드는 후학습과 새 task에서의 무갱신 적응을 구분한다.

## Training vs Inference

시연 구간·action interpolation·target-task split·검색 query와 inference 예산을 확인해 추가 supervision과 실제 배포 입력을 분리한다. 공개 code link의 존재를 재현 성공으로 간주하지 않는다.

## Objective and Temporal Contract

Exact loss/control law, optimizer, action horizon, control rate와 memory budget은 이번 abstract/project 확인에서 확정하지 않았다. [평가 조건](./04_evaluation.md)과 함께 읽는다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/sridhar25a.html) · [저자 project](https://ricl-vla.github.io/).
