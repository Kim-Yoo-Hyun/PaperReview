# Insights — MoRE: Unlocking Scalability in Reinforcement Learning for Quadruped Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

## Paper-supported conclusion

저랭크 전문가를 희소 활성화한다. Q 함수 학습을 여러 기술 및 실제 사족 로봇에서 검토한다. [원문 및 평가 절](https://arxiv.org/pdf/2503.08007#page=5)

## Researcher interpretation

사족 로봇에서 VLA를 행동 가치 함수로 학습하는 경로를 대표한다.

- Q-Transformer [30]의 자기회귀 이산 Q 목적을 사족 VLA의 전문가 혼합 미세조정에 맞게 바꾼다. Training objective. [pr-0625 · 원문](https://arxiv.org/pdf/2503.08007#page=4)

## 최소 비교 실험

같은 혼합 품질 경험에서 전문가 라우팅을 고정할 때 Q 학습의 이득을 비교한다.
