# MobileVLA-R1: Reinforcing Vision-Language-Action for Mobile Robots

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ECCV
- Authors: Ting Huang, Dongjian Li, Rui Yang, Zeyu Zhang, Zida Yang, Hao Tang
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, GRPO, quadruped, Navigation
- Aliases: MobileVLA-R1, MobileVLA-CoT
- Official paper: https://arxiv.org/abs/2511.17889
- Venue verification: https://eccv.ecva.net/Conferences/2026/AcceptedPapers
- Code/Project: https://aigeeksgroup.github.io/MobileVLA-R1/
- Code: https://github.com/AIGeeksGroup/MobileVLA-R1
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인. ECCV 원 논문과 MobileVLA-R1 2.0(preprint)의 주장·코드를 구분한다. 현 repository 실행 및 원 버전 일치는 미검증. 본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

모바일 로봇의 언어 추론과 실행 가능한 제어를 정합시키기 어렵다.

## Core Idea and Contribution

구조화 CoT alignment 뒤 GRPO RL로 추론·제어 일관성을 학습한다.

## Observation–State–Action Interface

영상·지시 → reasoning과 navigation command/control output → quadruped execution. 출력 형식을 low-level motor torque와 혼동하지 않는다.

## Evaluation Scope and Claim Boundary

VLN·VLA benchmark와 실제 사족 로봇 배포를 보고한다. MobileVLA-R1 2.0의 추가 주장은 포함하지 않는다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2511.17889) · [저자 project/code](https://aigeeksgroup.github.io/MobileVLA-R1/) · [공식 code](https://github.com/AIGeeksGroup/MobileVLA-R1). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Manipulation 외에 단일 VLA 후학습을 검토할 모바일 로봇 선행이다.

## Verification Boundary

속도·이산 행동 output 형식, low-level controller 고정 여부, 2.0 코드와 원 논문 차이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
