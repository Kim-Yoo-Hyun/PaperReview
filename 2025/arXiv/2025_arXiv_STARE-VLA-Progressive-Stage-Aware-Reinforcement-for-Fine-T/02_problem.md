# STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Problem and Bottleneck

긴 action trajectory의 전체 return만으로는 단계별 credit가 거칠다.

## Formulation and Robotics Loop

상태·action trajectory → 단계별 강화/선호 신호 → VLA 후학습.

의미 있는 단계로 trajectory를 나누고 stage-aware TPO/PPO 및 imitation–preference–interaction 후학습을 구성한다.

## Assumptions to Verify

stage label·geometric/contact predicate·potential 경계·TPO/PPO 비용.

위 항목은 연구자의 확인 질문이며 논문이 명시한 가정·실패로 확정한 것이 아니다.

## Prior Work and Why It Matters

Potential shaping·GAE·TPO/PPO → STARE-VLA → 장시간 VLA RL의 보상 접근권 비교.

단계별 credit·보상 shaping 자체가 기존 방법임을 반영하고 원 보상 보존·추가 supervision을 비교하는 직접 선행이다.

## Evidence Boundary

[공식 paper/abstract](https://arxiv.org/abs/2512.05107). arXiv v2 및 저자 project 확인. 검색 색인의 ICLR 표기는 공식 proceedings/forum으로 확인하지 못해 arXiv 2025로 유지한다. 공개 구현 URL은 식별하지 못했다.
