# Grasp-Then-Plan with Failure Attribution: A Closed Two-Stage Framework for Precise and Generalizable Robotic Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / NeurIPS
- Authors: Jiahao Xu, Peiyuan Wang, Hanzhuo Zhang, Zihao Yu, Tianyu Fu, Hao Chen, Xuanhao Xiang, Zixuan Li, Jianbo Yu, Chenchen Fu, Wanyuan Wang
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, grasping, motion planning, manipulation
- Aliases: GTP-FA
- Official paper: https://arxiv.org/abs/2606.03385
- Venue verification: https://neurips.cc/Downloads/2026
- Code/Project: https://sites.google.com/view/gtp-fa/
- Code: project_only
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다. NeurIPS 2026 공식 Downloads 목록 exact title와 poster 155467 연결 확인. 개최 전 program 기준이며 최종 proceedings 대조는 미완료.

## Problem and Importance

파지 실패와 후속 실행 실패를 구분해 manipulation을 개선한다.

## Core Idea and Contribution

Grasp-then-plan 두 단계와 failure attribution을 연결한다.

## Observation–State–Action Interface

Grasp 후보 → 실행 계획 → 실패 원인 → 두 단계 개선.

## Evaluation Scope and Claim Boundary

Simulation과 실제 manipulation 및 여러 정책 계열 비교를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2606.03385) · [저자 project/code](https://sites.google.com/view/gtp-fa/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

D2에서 downstream outcome·failure attribution을 새 방법으로 주장하지 않게 한다.

## Verification Boundary

failure label 출처, planner 성공과 policy 성공 구분, code 공개을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
