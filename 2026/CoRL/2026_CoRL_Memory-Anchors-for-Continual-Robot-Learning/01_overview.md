# Memory Anchors for Continual Robot Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
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
- Code: https://github.com/MaxDu17/MemoryAnchors
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다. 공식 OpenReview 검색 API의 Conference venueid·CoRL 2026 Poster를 확인했다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

Memory Anchors는 새 과제와 관측 표현은 비슷하지만 필요한 행동은 다른 과거 경험을 찾아 선택적으로 재생한다. [PDF 1쪽](https://arxiv.org/pdf/2608.26545v1#page=1)

## Core Idea and Contribution

- 표현 공간에서 과거와 현재 과제의 관측이 겹치면서 행동은 충돌하는 영역을 찾아 기억 버퍼에 강조했다. [PDF 2쪽](https://arxiv.org/pdf/2608.26545v1#page=2) · [PDF 4쪽](https://arxiv.org/pdf/2608.26545v1#page=4)
- LIBERO에서 해당 경험을 빼거나 더 넣었을 때 망각이 어떻게 달라지는지 비교하고 실제 로봇의 순차 과제에서도 시험했다. [PDF 1쪽](https://arxiv.org/pdf/2608.26545v1#page=1) · [PDF 7쪽](https://arxiv.org/pdf/2608.26545v1#page=7)

## Observation–State–Action Interface

현재/과거 sample의 representation·action → replay 선택 → policy update.

## Evaluation Scope and Claim Boundary

LIBERO와 real-robot continual learning 평가를 보고한다.

근거: [공식 paper/abstract](https://openreview.net/forum?id=dSbtHPqFj9) · [저자 project/code](https://robot-adaptation.github.io/MemoryAnchors). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

E1의 action-conflict replay와 가장 가까운 직접 비교군이다.

## Verification Boundary

latent layer, action normalization, task order, replay step scaling을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 — 행동 충돌을 이용한 리플레이 표본 선택 · memory_anchors/algos/anchor_er.py [배포 파일](https://raw.githubusercontent.com/MaxDu17/MemoryAnchors/4bde628d4dc217df6f7ad16af4b48699d33b8137/memory_anchors/algos/anchor_er.py)
- 데이터 — LIBERO-10 작업별 평균 점수 집계 · 125119.ckpt.json (AnchorER 1% 리플레이) [배포 파일](https://raw.githubusercontent.com/MaxDu17/MemoryAnchors/4bde628d4dc217df6f7ad16af4b48699d33b8137/results/AnchorER-10_1pct/Libero10/2026.05.23-08.19.01_SelER_9010_libero_10_progressive_shorter_order00_libero_policy_libero_10_progressive_diffusion_unet_robomimic_encoder/checkpoints/125119.ckpt.json)
