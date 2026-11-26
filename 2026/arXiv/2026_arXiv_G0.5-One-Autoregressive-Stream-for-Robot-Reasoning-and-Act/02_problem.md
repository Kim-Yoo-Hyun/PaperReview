# Problem — G0.5: One Autoregressive Stream for Robot Reasoning and Action

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §3–5, BEHAVIOR Challenge evaluation, §6 limitations 검토. [방법·평가 원문](https://arxiv.org/html/2608.11739) · [저자 코드](https://github.com/OpenGalaxea/GalaxeaVLA)

## 문제와 검증 범위

추론 텍스트와 다기체 행동을 하나의 자기회귀 모델에서 처리할 때, 로봇마다 제어 축과 토큰 길이가 달라지는 문제를 다룬다.

BEHAVIOR 2025 시뮬레이션의 이동·조작 50과제와 실물 기체의 조작 평가를 보고한다. 하부 구동만의 성능은 독립 평가하지 않았고, 일부 삽입과 반투명 문에서 실패가 남는다. [원문 및 평가 절](https://arxiv.org/html/2608.11739)
