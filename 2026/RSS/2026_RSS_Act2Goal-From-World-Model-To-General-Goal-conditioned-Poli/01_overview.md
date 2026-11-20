# Act2Goal: From World Model To General Goal-conditioned Policy

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Pengfei Zhou, Liliang Chen, Shengcong Chen, Di Chen, Wenzhi Zhao, Rongjun Jin, Guanghui Ren, Jianlan Luo
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: goal-conditioning, world-model, manipulation, hindsight
- Aliases: Act2Goal
- Official paper: https://www.roboticsproceedings.org/rss22/p015.html
- Venue verification: https://www.roboticsproceedings.org/rss22/p015.html
- Code/Project: https://act2goal.github.io/
- Code: not_identified
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. RSS 공식 abstract를 기준으로 기록. Project는 접근되지만 이번 웹 도구에서 본문을 읽지 못해 코드 공개 상태는 not identified다. Visual-goal 정책을 언어 지시 VLA와 동일시하지 않는다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다.

## Problem and Importance

시각 목표로 정한 장시간 조작에서 계획의 일관성과 가까운 feedback을 함께 유지한다.

## Core Idea and Contribution

목표 조건부 world model의 미래 영상과 multi-scale temporal hashing을 action expert에 연결하고 hindsight goal relabeling으로 적응한다.

## Observation–State–Action Interface

현재 영상·목표 영상 → imagined frames의 가까운/먼 시간 표현 → motor action.

## Evaluation Scope and Claim Boundary

시뮬레이션·실물 장시간 조작과 보상 없는 online 적응을 보고한다.

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p015.html) · [저자 project/code](https://act2goal.github.io/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Hindsight 목표 변경·world model·단일 정책 연결의 직접 선행이며 언어 VLA와 시각 목표 정책의 경계를 드러낸다.

## Verification Boundary

본문에서 확인할 항목: 시각 목표 접근·hindsight 도달 상태·LoRA 갱신 범위·online 비용. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
