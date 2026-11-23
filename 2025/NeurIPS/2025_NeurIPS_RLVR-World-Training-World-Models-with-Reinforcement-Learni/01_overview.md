# RLVR-World: Training World Models with Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / NeurIPS
- Authors: Jialong Wu, Shaofeng Yin, Ningya Feng, Mingsheng Long
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: world-model, RLVR, video-prediction
- Aliases: RLVR-World
- Official paper: https://proceedings.neurips.cc/paper_files/paper/2025/hash/b63a24a1832bd14fa945c71f535c0095-Abstract-Conference.html
- Venue verification: https://proceedings.neurips.cc/paper_files/paper/2025/hash/b63a24a1832bd14fa945c71f535c0095-Abstract-Conference.html
- Code/Project: https://thuml.github.io/RLVR-World/
- Code: https://github.com/thuml/RLVR-World
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인. Robot video prediction 결과와 robot policy return을 구분한다. 본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

World model의 likelihood 목표가 실제 예측 평가 지표와 일치하지 않을 수 있다.

## Core Idea and Contribution

Decoded prediction의 검증 가능한 지표를 reward로 삼아 world model을 RL 후학습한다.

## Observation–State–Action Interface

Action-conditioned state prediction → decoded metric reward → world model update.

## Evaluation Scope and Claim Boundary

언어·영상 world model의 여러 도메인을 평가한다. RT-1 로봇 영상의 예측 품질을 로봇 제어 성공으로 해석하지 않는다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b63a24a1832bd14fa945c71f535c0095-Abstract-Conference.html) · [저자 project/code](https://thuml.github.io/RLVR-World/) · [공식 code](https://github.com/thuml/RLVR-World). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

VLA policy RL과 world model RL을 구분하며 예측 개선이 행동에 전달되는지 물을 비교 자료다.

## Verification Boundary

reward metric과 task 목표 정합성, planner의 model exploitation, 로봇 행동 평가 유무을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
