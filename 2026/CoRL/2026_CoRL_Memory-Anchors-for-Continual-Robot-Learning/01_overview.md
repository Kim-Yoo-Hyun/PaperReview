# Memory Anchors for Continual Robot Learning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / CoRL
- Authors: Maximilian Du, Zhanyi Sun, Chen Xu, Paarth Shah, Masha Itkina, Shuran Song
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: continual-learning, replay, robot-learning
- Aliases: Memory Anchors
- Official paper: https://arxiv.org/abs/2608.26545
- Venue verification: https://www.corl.org/program/accepted-papers
- Code/Project: https://robot-adaptation.github.io/MemoryAnchors
- Code: project_only
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다. 공식 OpenReview 검색 API의 Conference venueid·CoRL 2026 Poster를 확인했다.

## Problem and Importance

새 task 적응 중 기존 robot 행동을 선택적으로 보존한다.

## Core Idea and Contribution

겹치는 latent representation에서 요구 action이 충돌하는 memory를 replay anchor로 사용한다.

## Observation–State–Action Interface

현재/과거 sample의 representation·action → replay 선택 → policy update.

## Evaluation Scope and Claim Boundary

LIBERO와 real-robot continual learning 평가를 보고한다.

근거: [공식 paper/abstract](https://openreview.net/forum?id=dSbtHPqFj9) · [저자 project/code](https://robot-adaptation.github.io/MemoryAnchors). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

E1의 action-conflict replay와 가장 가까운 직접 비교군이다.

## Verification Boundary

latent layer, action normalization, task order, replay step scaling을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
