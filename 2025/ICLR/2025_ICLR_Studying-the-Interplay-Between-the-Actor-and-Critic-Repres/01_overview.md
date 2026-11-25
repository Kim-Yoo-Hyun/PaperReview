# Studying the Interplay Between the Actor and Critic Representations in Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / ICLR
- Authors: Samuel Garcin, Trevor McInroe, Pablo Samuel Castro, Prakash Panangaden, Christopher G. Lucas, David Abel, Stefano V. Albrecht
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: actor-critic, representation, on-policy-RL, exploration
- Aliases: Actor-Critic Representation Interplay
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2025/hash/57da66da25d0ce77e0129b246f358851-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2025/hash/57da66da25d0ce77e0129b246f358851-Abstract-Conference.html
- Code/Project: https://github.com/francelico/deac-rep
- Code: https://github.com/francelico/deac-rep
- Source audit: 2026-11-06: 공식 proceedings metadata·abstract 확인. 이 5개 노트는 abstract 범위이며 최종 본문 정독/실행 완료가 아니다. 주제 dossier의 지정 preprint/code 읽기와 구별한다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 온폴리시 강화학습에서 행동을 정하는 행위자와 가치를 추정하는 비평가가 어떤 상태 정보를 필요로 하는지 분석한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/57da66da25d0ce77e0129b246f358851-Paper-Conference.pdf#page=1)

## Core Idea and Contribution

- 표현을 공유하거나 분리한 상태에서 상호정보량을 측정해 행위자와 비평가가 각각 행동과 가치·동역학에 관한 정보를 얼마나 담는지 비교했다. [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/57da66da25d0ce77e0129b246f358851-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/57da66da25d0ce77e0129b246f358851-Paper-Conference.pdf#page=5) · [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/57da66da25d0ce77e0129b246f358851-Paper-Conference.pdf#page=7)
- 비평가 표현을 바꿔 탐색과 자료 수집이 달라지는지를 평가해 표현 분리가 훈련 중 행동 분포에도 기여함을 보였다. [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/57da66da25d0ce77e0129b246f358851-Paper-Conference.pdf#page=9) · [PDF 10쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/57da66da25d0ce77e0129b246f358851-Paper-Conference.pdf#page=10)

## Observation–State–Action Interface

고차원 관측 → actor 행동·critic 가치 추정의 on-policy 학습.

## Evaluation Scope and Claim Boundary

공식 abstract의 표현·downstream 성능 비교까지 확인. 세부 환경·seed·수치·모델 용량 통제는 본문 대조 필요.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2025/hash/57da66da25d0ce77e0129b246f358851-Abstract-Conference.html) · [저자 project/code](https://github.com/francelico/deac-rep). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

U1의 일반 actor–critic 표현 간섭 주장이 새롭지 않음을 보여 주는 필수 비교다. VLA 언어 목표 조건의 추가 기여를 정의하기 위해 NEXT에 추가한다.

## Verification Boundary

환경별 capacity·optimizer·data collection 통제, VLA에 그대로 적용 가능한 결론의 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 — Brax 행위자·비평가 표현 실험 · brax_experiments/train_scripts/train_dcpg.py [배포 파일](https://raw.githubusercontent.com/francelico/deac-rep/4dd611159eabd21b1a67cc80acbd09dafb38a3b3/brax_experiments/train_scripts/train_dcpg.py)

## 판본과 출처

저자 표기·순서는 표제면 기준이다. [표제면](https://proceedings.iclr.cc/paper_files/paper/2025/file/57da66da25d0ce77e0129b246f358851-Paper-Conference.pdf#page=1)
