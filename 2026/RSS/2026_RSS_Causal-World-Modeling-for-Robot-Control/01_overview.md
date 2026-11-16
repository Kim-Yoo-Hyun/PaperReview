# Causal World Modeling for Robot Control

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: world-model, action-generation, temporal-context, manipulation
- Aliases: CauVA
- Official paper: https://www.roboticsproceedings.org/rss22/p016.html
- Venue verification: https://www.roboticsproceedings.org/rss22/p016.html
- Code/Project:
- Code: not_identified
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. 공식 RSS abstract만을 canonical scope로 사용한다. 같은 제목의 arXiv2601.21998은 LingBot-VA와 다른 저자 구성·설계를 표기하므로 version mapping을 확정하지 않았고 arXiv ID/code를 자동 합치지 않았다. 별도 중복 등록도 하지 않았다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다.

## Problem and Importance

미래 영상 예측과 실제 행동 생성·feedback을 같은 모델 안에서 다룬다.

## Core Idea and Contribution

RSS abstract의 CauVA는 autoregressive MoT로 frame/action을 처리하고 KV history와 noisy latent augmentation을 사용한다.

## Observation–State–Action Interface

영상·행동 이력 → 인과적 생성 sequence → 미래 영상·robot action.

## Evaluation Scope and Claim Boundary

시뮬레이션과 실제 장시간·정밀·변형체 조작을 평가한다.

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p016.html). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Architecture 통합과 RL 공동 갱신을 구별할 world-action 비교 대상으로 보완한다.

## Verification Boundary

본문에서 확인할 항목: 예측/행동 gradient 경로·추론 history·실제 피드백·버전별 모델 명칭. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
