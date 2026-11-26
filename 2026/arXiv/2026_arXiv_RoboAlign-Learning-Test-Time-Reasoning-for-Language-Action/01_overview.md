# RoboAlign: Learning Test-Time Reasoning for Language-Action Alignment in Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Authors: Dongyoung Kim, Sumin Park, Woomin Song, Seungku Kim, Taeyoung Kim, Huiwon Jang, Jinwoo Shin, Jaehyung Kim, Younggyo Seo
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, reinforcement-learning, action-alignment, reasoning
- Aliases: RoboAlign, RoboAlign: Reinforcement Learning for Action-Aligned Multimodal Large Language Models
- Official paper: https://arxiv.org/abs/2603.21341
- Venue verification: https://arxiv.org/abs/2603.21341
- Code/Project:
- Code: not_identified
- 방법·평가 확인 (2026-11-25): [원문 4, 5, 6, 7쪽](https://arxiv.org/pdf/2603.21341v1#page=4) · [다축 분류와 공개 범위](../../../work/sources/batches/core_next_10.yaml)
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. arXiv v1의 정확한 제목 사용. 저자 페이지의 이전 제목은 alias로 보존한다. 검색 색인의 ICLR 2026 표기는 공식 acceptance로 확인하지 못해 arXiv로 등록한다. RoboAlign-R1 world-model 논문과 다르다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

RoboAlign은 멀티모달 언어 모델이 추론 후 고른 행동 토큰의 정확도를 보상으로 사용해 언어 표현을 로봇 행동에 맞춘다. [PDF 1쪽](https://arxiv.org/pdf/2603.21341v1#page=1)

## Core Idea and Contribution

- 자연어 추론으로 생성한 FAST 행동 토큰을 강화학습으로 교정하고 정렬을 마친 백본에 확산 기반 행동 출력을 학습시킨다. [PDF 4쪽](https://arxiv.org/pdf/2603.21341v1#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2603.21341v1#page=5)
- LIBERO·CALVIN과 실물 로봇에서 백본 정렬을 적용한 정책과 지도학습 기준선을 비교해 행동 성능으로의 전이를 측정했다. [PDF 6쪽](https://arxiv.org/pdf/2603.21341v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2603.21341v1#page=7)

## Observation–State–Action Interface

영상·언어 추론 → action-token 정렬 MLLM → diffusion action head → 조작 행동.

## Evaluation Scope and Claim Boundary

LIBERO·CALVIN·실물 조작에서 alignment와 후속 VLA를 평가한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2603.21341). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

VLM의 RL 정렬과 배포 VLA의 직접 RL 갱신을 구분할 선행으로 단일 정책 연구의 기여 경계를 보완한다.

## Verification Boundary

본문에서 확인할 항목: RL action token과 최종 행동 차이·head 학습 데이터·추론 비용·공유 weight 경로. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
