# RoboAlign: Learning Test-Time Reasoning for Language-Action Alignment in Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
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
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. arXiv v1의 정확한 제목 사용. 저자 페이지의 이전 제목은 alias로 보존한다. 검색 색인의 ICLR 2026 표기는 공식 acceptance로 확인하지 못해 arXiv로 등록한다. RoboAlign-R1 world-model 논문과 다르다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다.

## Problem and Importance

언어 추론 능력 개선이 low-level robot action 개선으로 항상 전이되지 않는다.

## Core Idea and Contribution

자연어 추론에서 action token을 생성하고 RL로 행동 정확도를 정렬한 MLLM 위에 diffusion action head를 학습한다.

## Observation–State–Action Interface

영상·언어 추론 → action-token 정렬 MLLM → diffusion action head → 조작 행동.

## Evaluation Scope and Claim Boundary

LIBERO·CALVIN·실물 조작에서 alignment와 후속 VLA를 평가한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2603.21341). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

VLM의 RL 정렬과 배포 VLA의 직접 RL 갱신을 구분할 선행으로 단일 정책 연구의 기여 경계를 보완한다.

## Verification Boundary

본문에서 확인할 항목: RL action token과 최종 행동 차이·head 학습 데이터·추론 비용·공유 weight 경로. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
