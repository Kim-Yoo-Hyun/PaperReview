# Rethinking Visual-Language-Action Model Scaling: Alignment, Mixture, and Regularization

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Ye Wang, Sipeng Zheng, Hao Luo, Wanpeng Zhang, Haoqi Yuan, Chaoyi Xu, Haiweng Xu, Yicheng Feng, Mingyang Yu, Zhiyu Kang, Zongqing Lu, Qin Jin
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, action-interface, cross-embodiment
- Aliases: Rethinking VLA Scaling
- Official paper: https://arxiv.org/abs/2602.09722
- Venue verification: https://arxiv.org/abs/2602.09722
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다.

## Problem and Importance

이질적인 로봇 데이터를 늘리면 항상 VLA가 좋아지는가.

## Core Idea and Contribution

EEF-relative 정렬·embodiment mixture·regularization을 통제 비교하고 평가자 편향 통제를 제안한다.

## Observation–State–Action Interface

이종 robot demonstration → 정렬된 action 표현 → VLA.

## Evaluation Scope and Claim Boundary

Simulation과 real-robot 평가에서 데이터 혼합과 negative transfer를 분석한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2602.09722). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

E1에서 정상 action 정렬·mixture 자체의 설명력을 먼저 제거할 기준이다.

## Verification Boundary

EEF frame, normalization, split, grouped blind protocol을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
