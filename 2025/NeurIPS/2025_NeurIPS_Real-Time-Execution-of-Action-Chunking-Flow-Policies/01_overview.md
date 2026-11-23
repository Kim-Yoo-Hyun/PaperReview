# Real-Time Execution of Action Chunking Flow Policies

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / NeurIPS
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
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

Real-Time Chunking은 현재 동작을 실행하는 동안 다음 행동 묶음을 생성해 추론 지연 때문에 로봇이 멈추거나 불연속적으로 움직이는 문제를 줄인다. [PDF 1쪽](https://papers.nips.cc/paper_files/paper/2025/file/300ccb2187dedd4edcc07f7e76d8e553-Paper-Conference.pdf#page=1)

## Core Idea and Contribution

- 다음 추론이 끝나기 전에 실행될 행동은 고정하고 남은 구간은 확산·흐름 정책으로 이어서 생성한다. [PDF 3쪽](https://papers.nips.cc/paper_files/paper/2025/file/300ccb2187dedd4edcc07f7e76d8e553-Paper-Conference.pdf#page=3) · [PDF 4쪽](https://papers.nips.cc/paper_files/paper/2025/file/300ccb2187dedd4edcc07f7e76d8e553-Paper-Conference.pdf#page=4)
- Kinetix의 동적 과제와 실제 양팔 조작에서 지연을 변화시키며 성공률과 작업 처리 속도를 비교했다. [PDF 6쪽](https://papers.nips.cc/paper_files/paper/2025/file/300ccb2187dedd4edcc07f7e76d8e553-Paper-Conference.pdf#page=6) · [PDF 7쪽](https://papers.nips.cc/paper_files/paper/2025/file/300ccb2187dedd4edcc07f7e76d8e553-Paper-Conference.pdf#page=7)

## Observation–State–Action Interface

새 관측·이전 chunk·지연 → prefix 제약 → 다음 chunk.

## Evaluation Scope and Claim Boundary

Kinetix 실험과 실제 π0.5 양팔 평가를 구분해 보고한다.

근거: [공식 paper/abstract](https://papers.nips.cc/paper_files/paper/2025/hash/300ccb2187dedd4edcc07f7e76d8e553-Abstract-Conference.html) · [저자 project/code](https://pi.website/research/real_time_chunking). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

초기 지연 후보와 E2가 반드시 비교할 표준 실행 baseline이다.

## Verification Boundary

prefix 길이, delay estimate, inpainting cost, simulator와 VLA 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
