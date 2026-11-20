# Restoring the Right Stream: Training-Free OOD Robustness for Vision–Language–Action Policies

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Zhiyin Yan, Gang Shen
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, proprioception, robustness
- Aliases:
- Official paper: https://api.crossref.org/works/10.3390/e28090975
- Venue verification: https://www.mdpi.com/1099-4300/28/9/975
- Code/Project: https://www.mdpi.com/1099-4300/28/9/975
- Code: not_identified
- Source audit: 2026-10-21: official abstract / author project 확인. 5개 note는 abstract 기반이며 사용자 정독을 의미하지 않는다.

## Problem and Importance

Frozen VLA에서 shift가 들어간 input stream에 맞는 보정을 적용한다.

## Core Idea and Contribution

Gated Per-Stream Manifold Restoration으로 visual/state 입력을 따로 복원한다.

## Observation–State–Action Interface

영상·proprioception·언어 → gated restoration → frozen policy.

## Evaluation Scope and Claim Boundary

OpenVLA-OFT와 LIBERO-Plus 평가를 보고한다.

근거: [공식 paper/abstract](https://www.mdpi.com/1099-4300/28/9/975) · [저자 project/code](https://www.mdpi.com/1099-4300/28/9/975). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Top-tier 선정 논문은 아니지만 D1의 stream diagnosis·correction 주장과 직접 겹쳐 REFERENCE로 등록한다.

## Verification Boundary

native state interface, gate oracle leakage, code·trial manifest 공개을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
