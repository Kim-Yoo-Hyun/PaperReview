# CompliantVLA-adaptor: VLM-Guided Variable Impedance Action for Safe Contact-Rich Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Authors: Heng Zhang, Wei-Hsing Huang, Qiyi Tong, Gokhan Solak, Puze Liu, Kaidi Zhang, Sheng Liu, Jan Peters, Yu She, Arash Ajoudani
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: VLA, VLM, variable-impedance, force-feedback
- Aliases: CompliantVLA-adaptor
- Official paper: https://arxiv.org/abs/2601.15541
- Venue verification: https://arxiv.org/abs/2601.15541
- Code/Project: https://sites.google.com/view/compliantvla
- Code: not_identified
- Source audit: 2026-11-09: official abstract/project 및 metadata 확인. v2는 under review 표기. Project의 anonymous code 공개 주장은 확인했지만 구체적 repository URL은 이번 확인에서 식별하지 못했다. 새 5-note는 abstract 기반이며 전체 본문/실행/사용자 정독을 뜻하지 않는다.

## Problem and Importance

위치 명령 중심 VLA가 접촉 force와 순응성을 충분히 조절하지 못한다.

## Core Idea and Contribution

VLM이 task context에 따른 impedance를 정하고 실시간 force/torque feedback으로 조절한다.

## Observation–State–Action Interface

이미지·언어 → stiffness/damping; force feedback → controller 보정.

## Evaluation Scope and Claim Boundary

Simulation과 실제 접촉 과제에서 성공률·force violation을 비교한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2601.15541) · [저자 project/code](https://sites.google.com/view/compliantvla). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

단일 VLA RL 이전에 비교할 학습 없는 context/force 기반 controller 대안이다.

## Verification Boundary

Prompt와 controller 설정 비용, force threshold, release 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
