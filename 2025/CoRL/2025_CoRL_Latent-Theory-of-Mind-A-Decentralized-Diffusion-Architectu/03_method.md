# Method — Latent Theory of Mind: A Decentralized Diffusion Architecture for Cooperative Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.

## Pipeline and Learning Rule

Ego/consensus embedding과 상대 ego decoder를 학습한다. 중앙 학습의 sheaf-inspired 정렬 후 분산 실행하며 통신은 선택적이다.

## Observation, State and Action

로봇별 sensor stream → ego/consensus latent → diffusion action; 선택적으로 consensus를 교환한다.

## Temporal and Implementation Boundary

공식 [code README](https://github.com/StanfordMSL/LatentToM)는 기본 학습 설정의 shared third-person view와 separate camera 설정을 구분한다. 분산 실행이라는 표현만으로 두 설정을 local-only 정보 조건과 같게 두지 않는다. 실행·config 내부 검증은 하지 않았다.

Control rate, action horizon, optimizer 전체 설정·checkpoint 호환성은 이번 노트에서 확정하지 않았다. Abstract에 없는 목적함수·모듈 세부는 본문 확인 필요. Code URL의 존재는 native 실행 검증이 아니다.

근거: [확인한 원문](https://proceedings.mlr.press/v305/he25a.html), 공식 proceedings abstract.
