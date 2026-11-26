# Method — G0.5: One Autoregressive Stream for Robot Reasoning and Action

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §3–5, BEHAVIOR Challenge evaluation, §6 limitations 검토. [방법·평가 원문](https://arxiv.org/html/2608.11739) · [저자 코드](https://github.com/OpenGalaxea/GalaxeaVLA)

## 관측과 출력

다중 영상·언어 지시·기체 ID·고유수용 상태에서 27차원 공용 명령을 부위별로 부호화한다. 좌우 제어가 각 9축, 그리퍼가 각 1축, 하부가 7축이다. 기체가 쓰지 않는 슬롯은 비운다. 기본 자기회귀 경로와 선택적인 연속 후처리 전문가를 구분한다.

## 학습·실행 방법

Qwen3.5 기반 모델이 선택적으로 물체·하위 과제·그리퍼 경로를 텍스트로 생성한 뒤 행동 코드를 같은 스트림에서 예측한다. ActionCodec이 신체 부위별 이산 코드를 연속 명령으로 복원한다.
