# ReViP: Mitigating False Completion in Vision-Language-Action Models with Vision-Proprioception Rebalance

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Authors: Zhuohao Li, Yinghao Li, Jian-Jian Jiang, Lang Zhou, Tianyu Zhang, Jiadong Yin, Mu Lin, Yi-Lin Wei, Wei-Shi Zheng
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, proprioception, robustness
- Aliases: ReViP: Reducing False Completion in Vision-Language-Action Models with Vision–Proprioception Rebalance
- Official paper: https://arxiv.org/abs/2601.16667
- Venue verification: https://arxiv.org/abs/2601.16667
- Code/Project: https://isee-laboratory.github.io/ReViP/
- Code: not_released
- Source audit: 2026-10-21: official abstract / author project 확인. 5개 note는 abstract 기반이며 사용자 정독을 의미하지 않는다. 최신 arXiv v3 title과 project 확인; 이전 Reducing title은 alias로 유지.

## Problem and Importance

실제 목표가 달성되지 않았는데 완료 동작을 이어 가는 false completion을 다룬다.

## Core Idea and Contribution

시각적 task-stage cue로 vision–proprioception 결합을 조정한다.

## Observation–State–Action Interface

영상·언어·state와 stage cue → corrective action.

## Evaluation Scope and Claim Boundary

Object Drop, Distractor Swap, Relayout 및 robot manipulation 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2601.16667) · [저자 project/code](https://isee-laboratory.github.io/ReViP/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

D1에서 단순 vision 강화나 stage feedback을 새 기여로 재주장하지 않게 하는 NEXT다.

## Verification Boundary

arXiv v3와 최신 project 방법 차이, observer latency, 공개 코드을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
