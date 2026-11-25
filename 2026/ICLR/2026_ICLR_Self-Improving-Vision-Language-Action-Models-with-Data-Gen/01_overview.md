# Self-Improving Vision-Language-Action Models with Data Generation via Residual RL

> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

- Year/Venue: 2026 / ICLR
- Authors: Wenli Xiao, Haotian Lin, Andy Peng, Haoru Xue, Tairan He, Yuqi Xie, Fengyuan Hu, Jimmy Wu, Zhengyi Luo, Linxi “Jim” Fan, Guanya Shi, Yuke Zhu
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, residual-RL, data-generation, self-improvement
- Aliases: PLD
- Official paper: https://iclr.cc/virtual/2026/poster/10008318
- Venue verification: https://iclr.cc/virtual/2026/poster/10008318
- Code/Project: https://wenlixiao.com/self-improve-VLA-PLD/
- Code: not identified
- Source audit: 2026-11-25 게재본에서 아래에 인용한 요약·기여와 평가 조건을 대조했다. 초기 arXiv v1의 §3과 부록 B.2·C.1·C.2는 당시 검토 기록에 보존했다. [평가 노트](./04_evaluation.md)

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

## 원문 대조

PLD는 잔차 강화학습으로 고정 VLA의 실패 상태에서 복구 궤적을 수집하고 이 경험을 범용 정책에 증류한다. [게재본](https://proceedings.iclr.cc/paper_files/paper/2026/file/163a875ab0c2631ed30b7435c4c9b8f1-Paper-Conference.pdf#page=5)

- 가벼운 과제별 잔차 정책이 기본 정책이 방문하는 상태에서 개입하도록 자료를 수집한다. [원문](https://proceedings.iclr.cc/paper_files/paper/2026/file/163a875ab0c2631ed30b7435c4c9b8f1-Paper-Conference.pdf#page=5)
- LIBERO·SimplerEnv와 실제 Franka·YAM에서 하이브리드 수집과 후속 SFT의 효과를 평가했다. [원문](https://proceedings.iclr.cc/paper_files/paper/2026/file/163a875ab0c2631ed30b7435c4c9b8f1-Paper-Conference.pdf#page=8)

## 판본과 출처

저자 표기·순서는 표제면 기준이다. [표제면](https://proceedings.iclr.cc/paper_files/paper/2026/file/163a875ab0c2631ed30b7435c4c9b8f1-Paper-Conference.pdf#page=1)
