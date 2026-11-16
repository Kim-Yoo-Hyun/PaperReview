# Learning Native Continuation for Action Chunking Flow Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Pipeline and Representation

알려진 action과 noise를 섞는 schedule 및 flow 학습을 통해 chunk continuation을 정책 자체가 익히게 한다.

관측·이전 action 정보·continuation schedule → flow action chunk → 실행. Inference-time RTC와 학습된 continuation을 구분한다.

## Training vs Inference

schedule·delay 분포·실기 controller·성공/시간 trade-off·Kinetix와 실기 구현 차이을 확인해 추가 supervision과 실제 배포 입력을 분리한다. 공개 code link의 존재를 재현 성공으로 간주하지 않는다.

## Objective and Temporal Contract

Exact loss/control law, optimizer, action horizon, control rate와 memory budget은 이번 abstract/project 확인에서 확정하지 않았다. [평가 조건](./04_evaluation.md)과 함께 읽는다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p058.html) · [저자 project](https://lyfeng001.github.io/Legato/).
