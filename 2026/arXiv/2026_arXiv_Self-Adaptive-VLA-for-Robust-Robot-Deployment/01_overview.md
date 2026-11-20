# Self-Adaptive VLA for Robust Robot Deployment

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Hongxin Zhang, Chunru Lin, Tsun-Hsuan Wang, Zhenjia Xu, Chuang Gan
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, proprioception, robustness
- Aliases:
- Official paper: https://arxiv.org/abs/2609.30092
- Venue verification: https://arxiv.org/abs/2609.30092
- Code/Project: https://icefoxzhx.github.io/self-adaptive-vla/
- Code: not_identified
- Source audit: 2026-10-21: official abstract / author project 확인. 5개 note는 abstract 기반이며 사용자 정독을 의미하지 않는다.

## Problem and Importance

배포 시 hardware shift로 반복 실패하는 VLA를 적응시킨다.

## Core Idea and Contribution

실패 rollout context를 encoder와 AdaLN으로 주입하고 여러 trial의 token을 합친다.

## Observation–State–Action Interface

영상·proprioception·action history → context-conditioned action.

## Evaluation Scope and Claim Boundary

정밀 bimanual·dexterous 작업의 actuation bias와 encoder offset 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.30092) · [저자 project/code](https://icefoxzhx.github.io/self-adaptive-vla/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

D1의 hardware-cause adaptation과 가장 가까운 NEXT 비교군이다.

## Verification Boundary

episode/trial 간 offset 유지, encoder 모델, expert action 보상을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
