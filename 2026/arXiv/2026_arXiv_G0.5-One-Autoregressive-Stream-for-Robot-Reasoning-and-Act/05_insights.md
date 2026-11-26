# Insights — G0.5: One Autoregressive Stream for Robot Reasoning and Action

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §3–5, BEHAVIOR Challenge evaluation, §6 limitations 검토. [방법·평가 원문](https://arxiv.org/html/2608.11739) · [저자 코드](https://github.com/OpenGalaxea/GalaxeaVLA)

## Paper-supported conclusion

Qwen3.5 기반 모델이 선택적으로 물체·하위 과제·그리퍼 경로를 텍스트로 생성한 뒤 행동 코드를 같은 스트림에서 예측한다. ActionCodec이 신체 부위별 이산 코드를 연속 명령으로 복원한다. [원문 및 평가 절](https://arxiv.org/html/2608.11739)

## Researcher interpretation

FAST의 시간축 행동 압축, π0.5의 텍스트·연속 전문가와 비교할 수 있는 부위별 자기회귀 표현이다. 실제로 채워진 기체별 슬롯을 확인해야 한다.

## 최소 비교 실험

이동과 파지를 교대로 또는 겹쳐 써야 하는 같은 장면에서 베이스 슬롯을 가리고, 접근과 파지의 진행률을 따로 기록한다.

## 검증 질문

공용 슬롯의 수만으로 보행 균형이나 동시 전신 제어가 검증되지는 않는다. 베이스와 팔이 같은 시점에 활성인 구간의 평가가 필요하다.
