# Self-Improving Vision-Language-Action Models with Data Generation via Residual RL

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

## Problem and Bottleneck

고정 VLA의 조작 실패를 online 경험으로 보완하고 그 경험을 다시 generalist 정책 학습에 쓰는 문제다.

## Changed Formulation

동결 VLA 위에 residual specialist를 학습하고, 배포 조건을 고려한 hybrid rollout에서 얻은 데이터를 generalist의 supervised fine-tuning에 사용한다.

## Assumptions and Robotics Loop

Specialist가 개선한 행동과 데이터 수집 분포가 후학습에 유용해야 한다. Base가 바뀐 뒤 이전 residual의 호환성은 별도 질문이다.

시각 관측·지시 → VLA 행동과 residual 보정 → rollout → VLA 후학습. Specialist 학습과 generalist 갱신은 다른 단계다.

근거: [지정 본문](https://arxiv.org/html/2511.00091v1) — §3, Appendix B.2/C.1/C.2.
