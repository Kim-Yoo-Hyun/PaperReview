# Look Before You Act: Bridging Active Perception and Vision-Language-Action Models via Observation-Aligned Data Adaptation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Jiawei Geng, Zhenyang Liu, Yuzheng Wu, Yongchong Gu, Yanwei Fu
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, active perception, manipulation, robustness
- Aliases: ActiveAlign
- Official paper: https://arxiv.org/abs/2610.23378
- Venue verification: https://arxiv.org/abs/2610.23378
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다.

## Problem and Importance

초기 관측 분포 차이 때문에 VLA가 실패하는 상황을 줄인다.

## Core Idea and Contribution

Active perception으로 관측을 맞추고 정렬된 continuation 자료로 adaptation한다.

## Observation–State–Action Interface

초기 영상·state → camera/관측 정렬 → VLA continuation.

## Evaluation Scope and Claim Boundary

LIBERO와 실제 robot manipulation을 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.23378). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

C1/D1의 능동 관측·관측 정렬 주장과 직접 충돌한다.

## Verification Boundary

camera 행동 비용, state change, 성공 continuation 선택, data budget을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
