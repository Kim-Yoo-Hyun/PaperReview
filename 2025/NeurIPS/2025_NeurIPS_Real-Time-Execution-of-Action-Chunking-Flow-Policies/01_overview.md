# Real-Time Execution of Action Chunking Flow Policies

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Kevin Black, Manuel Galliker, Sergey Levine
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, action-chunking, feedback, control-frequency
- Aliases: RTC
- Official paper: https://papers.nips.cc/paper_files/paper/2025/hash/300ccb2187dedd4edcc07f7e76d8e553-Abstract-Conference.html
- Venue verification: https://papers.nips.cc/paper_files/paper/2025/hash/300ccb2187dedd4edcc07f7e76d8e553-Abstract-Conference.html
- Code/Project: https://pi.website/research/real_time_chunking
- Code: project_only
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다.

## Problem and Importance

무거운 flow policy의 추론 지연 때문에 action chunk 연결이 끊긴다.

## Core Idea and Contribution

실행이 확정된 prefix를 보존하며 남은 action을 inpainting하는 비동기 추론을 사용한다.

## Observation–State–Action Interface

새 관측·이전 chunk·지연 → prefix 제약 → 다음 chunk.

## Evaluation Scope and Claim Boundary

Kinetix 실험과 실제 π0.5 양팔 평가를 구분해 보고한다.

근거: [공식 paper/abstract](https://papers.nips.cc/paper_files/paper/2025/hash/300ccb2187dedd4edcc07f7e76d8e553-Abstract-Conference.html) · [저자 project/code](https://pi.website/research/real_time_chunking). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

초기 지연 후보와 E2가 반드시 비교할 표준 실행 baseline이다.

## Verification Boundary

prefix 길이, delay estimate, inpainting cost, simulator와 VLA 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
