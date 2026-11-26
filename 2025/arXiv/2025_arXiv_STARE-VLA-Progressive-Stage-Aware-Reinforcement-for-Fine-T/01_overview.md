# STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / arXiv
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
- 방법·평가 확인 (2026-11-25): [원문 6, 7, 8, 9, 10쪽](https://arxiv.org/pdf/2512.05107v2#page=6) · [다축 분류와 공개 범위](../../../work/sources/batches/core_next_10.yaml)
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. arXiv v2 및 저자 project 확인. 검색 색인의 ICLR 표기는 공식 proceedings/forum으로 확인하지 못해 arXiv 2025로 유지한다. 공개 구현 URL은 식별하지 못했다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

StARe-VLA는 긴 조작을 접근·파지·운반처럼 인과적으로 이어지는 단계로 나누어 각 단계에 맞는 신호로 정책을 후학습한다. [PDF 1쪽](https://arxiv.org/pdf/2512.05107v2#page=1)

## Core Idea and Contribution

- 단계별 오프라인 선호 학습과 온라인 상호작용 PPO를 구성하고 지도학습 초기화 뒤 두 단계를 순차 적용하는 절차를 제시했다. [PDF 6쪽](https://arxiv.org/pdf/2512.05107v2#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2512.05107v2#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2512.05107v2#page=8)
- SimplerEnv와 ManiSkill3에서 전체 궤적 단위 학습과 비교해 중간 단계에 보상을 두는 방식과 후학습 순서가 과제 성공에 주는 영향을 평가했다. [PDF 9쪽](https://arxiv.org/pdf/2512.05107v2#page=9) · [PDF 10쪽](https://arxiv.org/pdf/2512.05107v2#page=10)

## Observation–State–Action Interface

상태·action trajectory → 단계별 강화/선호 신호 → VLA 후학습.

## Evaluation Scope and Claim Boundary

SimplerEnv와 ManiSkill3의 조작 과제를 평가한다. 실제 로봇 결과로 확대하지 않는다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2512.05107) · [저자 project/code](https://sites.google.com/view/stare-vla). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

단계별 credit·보상 shaping 자체가 기존 방법임을 반영하고 원 보상 보존·추가 supervision을 비교하는 직접 선행이다.

## Verification Boundary

본문에서 확인할 항목: stage label·geometric/contact predicate·potential 경계·TPO/PPO 비용. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
