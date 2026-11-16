# Method — Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Pipeline and Learning Rule

Sparse autoencoder 분석과 activation 주입으로 task 선택과 motor trajectory 생성 경로를 분해한다.

## Observation, State and Action

관측·언어 → VLA 내부 activation → 개입된 action expert → 행동. 주입된 정책과 정상 정책을 구분한다.

## Temporal and Implementation Boundary

Control rate, action horizon, optimizer 전체 설정·checkpoint 호환성은 이번 노트에서 확정하지 않았다. 확인한 pipeline과 source 절을 넘어 수식·실행 가능성을 추정하지 않는다. Code URL의 존재는 native 실행 검증이 아니다.

근거: [확인한 원문](https://arxiv.org/pdf/2603.19233v6), v6 (2026-11-02), §4.7–4.8, Appendix B.
