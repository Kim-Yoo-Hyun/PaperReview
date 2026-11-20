# Studying the Interplay Between the Actor and Critic Representations in Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Samuel Garcin, Trevor McInroe, Pablo Samuel Castro, Christopher Lucas, David Abel, Prakash Panangaden, Stefano V. Albrecht
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: actor-critic, representation, on-policy-RL, exploration
- Aliases: Actor-Critic Representation Interplay
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2025/hash/57da66da25d0ce77e0129b246f358851-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2025/hash/57da66da25d0ce77e0129b246f358851-Abstract-Conference.html
- Code/Project: https://github.com/francelico/deac-rep
- Code: https://github.com/francelico/deac-rep
- Source audit: 2026-11-06: 공식 proceedings metadata·abstract 확인. 이 5개 노트는 abstract 범위이며 최종 본문 정독/실행 완료가 아니다. 주제 dossier의 지정 preprint/code 읽기와 구별한다.

## Problem and Importance

정책과 가치 추정에 필요한 정보가 다를 때 표현을 공유할지 분리할지 다룬다.

## Core Idea and Contribution

공유/분리 표현과 각 역할의 전문화를 비교한다. 별도 critic은 탐색과 수집 데이터에도 영향을 준다고 보고한다.

## Observation–State–Action Interface

고차원 관측 → actor 행동·critic 가치 추정의 on-policy 학습.

## Evaluation Scope and Claim Boundary

공식 abstract의 표현·downstream 성능 비교까지 확인. 세부 환경·seed·수치·모델 용량 통제는 본문 대조 필요.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2025/hash/57da66da25d0ce77e0129b246f358851-Abstract-Conference.html) · [저자 project/code](https://github.com/francelico/deac-rep). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

U1의 일반 actor–critic 표현 간섭 주장이 새롭지 않음을 보여 주는 필수 비교다. VLA 언어 목표 조건의 추가 기여를 정의하기 위해 NEXT에 추가한다.

## Verification Boundary

환경별 capacity·optimizer·data collection 통제, VLA에 그대로 적용 가능한 결론의 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
