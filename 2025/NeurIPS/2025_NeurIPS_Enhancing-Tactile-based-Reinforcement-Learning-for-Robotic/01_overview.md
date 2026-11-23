# Enhancing Tactile-based Reinforcement Learning for Robotic Control

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / NeurIPS
- Authors: Elle Miller, Trevor McInroe, David Abel, Oisin Mac Aodha, Sethu Vijayakumar
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: tactile-RL, binary-contact, self-supervised-learning, dexterity
- Aliases: RoTO, Robot Tactile Olympiad
- Official paper: https://proceedings.neurips.cc/paper_files/paper/2025/hash/bc09efb501c801ed92e181e26a885c2d-Abstract-Conference.html
- Venue verification: https://proceedings.neurips.cc/paper_files/paper/2025/hash/bc09efb501c801ed92e181e26a885c2d-Abstract-Conference.html
- Code/Project: https://elle-miller.github.io/tactile_rl/
- Code: https://github.com/elle-miller/roto
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

접촉 정보를 추가해도 RL이 이를 안정적으로 활용하지 못하며 proprioception만으로 놓치는 물체 움직임이 있다.

## Core Idea and Contribution

희소 이진 접촉·proprioception 표현을 self-supervised learning으로 학습하고 SSL memory와 on-policy memory의 분리를 검토한다.

## Observation–State–Action Interface

Binary contact·proprioception → 표현/memory → contact-rich control.

## Evaluation Scope and Claim Boundary

RoTO 시뮬레이션의 공 튀기기·Baoding 회전 등 dexterity를 평가한다. 실로봇 결과로 확대하지 않는다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/bc09efb501c801ed92e181e26a885c2d-Abstract-Conference.html) · [저자 project/code](https://elle-miller.github.io/tactile_rl/) · [공식 code](https://github.com/elle-miller/roto). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

시각 VLA에 촉각을 넣기 전에 입력 유용성과 표현 학습을 분리할 진단 자원이다.

## Verification Boundary

센서 노이즈·빈도, sim contact의 현실성, 실물 센서 전이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
