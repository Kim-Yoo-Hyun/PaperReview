# Learning Native Continuation for Action Chunking Flow Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Target Problem and Bottleneck

Action chunk 경계의 불연속과 multimodal switching이 로봇 동작을 지연시키는 문제를 다룬다.

## Changed Formulation

[방법](./03_method.md)의 입력과 학습/배포 개입을 구분해 선행과 비교한다. 단순 성공률 향상보다 어떤 정보가 언제 추가되는지가 비교의 기준이다.

## Assumptions to Verify — Researcher Interpretation

schedule·delay 분포·실기 controller·성공/시간 trade-off·Kinetix와 실기 구현 차이.

이는 본문에서 확인할 질문이며 논문이 직접 인정한 실패 목록이 아니다.

## Position in the Robotics Loop

관측·이전 action 정보·continuation schedule → flow action chunk → 실행. Inference-time RTC와 학습된 continuation을 구분한다.

정확한 sensor·state·action frame 및 controller 경계는 본문 확인 전 확정하지 않는다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p058.html) · [저자 project](https://lyfeng001.github.io/Legato/).
