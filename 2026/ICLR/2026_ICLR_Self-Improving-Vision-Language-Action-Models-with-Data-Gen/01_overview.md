# Self-Improving Vision-Language-Action Models with Data Generation via Residual RL

> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

- Year/Venue
- Authors: Wenli Xiao, Haotian Lin, Andy Peng, Haoru Xue, Tairan He, Zhengyi Luo, Yuqi Xie, Fengyuan Hu, Jim Fan, Guanya Shi, Yuke Zhu
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, residual-RL, data-generation, self-improvement
- Aliases: PLD
- Official paper: https://iclr.cc/virtual/2026/poster/10008318
- Venue verification: https://iclr.cc/virtual/2026/poster/10008318
- Code/Project: https://wenlixiao.com/self-improve-VLA-PLD/
- Code: not identified
- Source audit: 2026-11-03 공식 venue/서지 재확인; 기존 GAP-VRL 검토의 지정 본문 §3, Appendix B.2/C.1/C.2를 반영. 선택 절 검토이며 전체 논문 정독·native 실행은 아님. ICLR 공식 program의 채택과 읽은 arXiv v1을 구별한다. 최종본 동등성·동일 residual의 반복 base 갱신 전이·공식 전체 학습 code는 확인하지 않았다. 사용자 읽기 상태는 UNREAD 유지.

## Problem and Importance

고정 VLA의 조작 실패를 online 경험으로 보완하고 그 경험을 다시 generalist 정책 학습에 쓰는 문제다.

## Core Idea and Contribution

동결 VLA 위에 residual specialist를 학습하고, 배포 조건을 고려한 hybrid rollout에서 얻은 데이터를 generalist의 supervised fine-tuning에 사용한다.

## Observation–State–Action Interface

시각 관측·지시 → VLA 행동과 residual 보정 → rollout → VLA 후학습. Specialist 학습과 generalist 갱신은 다른 단계다.

## Evaluation Scope and Limitations

LIBERO·SimplerEnv와 실제 Franka 조작을 보고한다. 여기서는 단계별 정책 역할을 확인했으며 성공률·trial 수·전체 ablation은 새로 정리하지 않았다.

ICLR 공식 program의 채택과 읽은 arXiv v1을 구별한다. 최종본 동등성·동일 residual의 반복 base 갱신 전이·공식 전체 학습 code는 확인하지 않았다.

근거: [지정 본문](https://arxiv.org/html/2511.00091v1) — §3, Appendix B.2/C.1/C.2.

## Why This Paper Is Here — Researcher Interpretation

VLA의 residual 개선→데이터 생성→base 갱신을 잇는 직접 선행이다. 현재 후보에서 이 루프 자체를 새 기여로 주장하지 않도록 NEXT에 추가한다.
