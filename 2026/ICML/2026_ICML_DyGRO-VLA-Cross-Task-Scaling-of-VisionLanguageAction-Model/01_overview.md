# DyGRO-VLA: Cross-Task Scaling of Vision–Language–Action Models via Dynamic Grouped Residual Optimization

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Sixu Lin, Yunpeng Qing, Litao Liu, Ming Zhou, Ruixing Jin, Xiaoyi Fan, Guiliang Liu
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: multitask-RL, residual-policy, generalization
- Aliases: DyGRO-VLA
- Official paper: https://proceedings.mlr.press/v306/lin26af.html
- Venue verification: https://proceedings.mlr.press/v306/lin26af.html
- Code/Project: https://github.com/EDEM-AI/DyGRO-VLA
- Code: project_only
- Source audit: 2026-10-19: 공식 paper abstract 및 저자 project/code README 확인; abstract 기반 — 본문 수동 확인 필요.

## Problem and Importance

Task별 RL fine-tuning이 pretrained VLA를 좁은 task에 과적합시켜 cross-task 일반성을 훼손하는 문제다.

## Core Idea and Contribution

Cross-task latent representation과 mixture-of-RL-residuals를 이용한 두 단계 grouped residual optimization을 제안한다.

## Observation–State–Action Interface

VLA observation/language → cross-task latent features 및 residual policy update → robot action.

## Evaluation Scope and Claim Boundary

ICML abstract는 LIBERO, RoboTwin2와 real-world 평가 및 multitask/distribution-shift 조건을 명시한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v306/lin26af.html) · [저자 project/code](https://github.com/EDEM-AI/DyGRO-VLA). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Current trend. RL fine-tuning 중 task-specific overfitting을 줄이는 것이 연구 질문일 때 RL4VLA/ConRFT와 비교한다. 새 architecture라는 이유만으로 CORE로 올리지는 않는다.

## Verification Boundary

Task grouping, residual routing, representation loss와 unseen split leakage을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
