# STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Feng Xu, Guangyao Zhai, Xin Kong, Tingzhong Fu, Daniel F. N. Gordon, Xueli An, Benjamin Busam
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, reinforcement-learning, credit-assignment, reward-shaping
- Aliases: STARE-VLA, Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models
- Official paper: https://arxiv.org/abs/2512.05107
- Venue verification: https://arxiv.org/abs/2512.05107
- Code/Project: https://sites.google.com/view/stare-vla
- Code: not_identified
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. arXiv v2 및 저자 project 확인. 검색 색인의 ICLR 표기는 공식 proceedings/forum으로 확인하지 못해 arXiv 2025로 유지한다. 공개 구현 URL은 식별하지 못했다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다.

## Problem and Importance

긴 action trajectory의 전체 return만으로는 단계별 credit가 거칠다.

## Core Idea and Contribution

의미 있는 단계로 trajectory를 나누고 stage-aware TPO/PPO 및 imitation–preference–interaction 후학습을 구성한다.

## Observation–State–Action Interface

상태·action trajectory → 단계별 강화/선호 신호 → VLA 후학습.

## Evaluation Scope and Claim Boundary

SimplerEnv와 ManiSkill3의 조작 과제를 평가한다. 실제 로봇 결과로 확대하지 않는다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2512.05107) · [저자 project/code](https://sites.google.com/view/stare-vla). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

단계별 credit·보상 shaping 자체가 기존 방법임을 반영하고 원 보상 보존·추가 supervision을 비교하는 직접 선행이다.

## Verification Boundary

본문에서 확인할 항목: stage label·geometric/contact predicate·potential 경계·TPO/PPO 비용. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
