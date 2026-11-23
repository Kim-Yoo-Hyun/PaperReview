# Behavior-Skill: A Fine-Grained Benchmark for Evaluating Vision-Language-Action Policies in Long-Horizon Tasks

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Authors: Chunyun Ma, Lun Luo, Xingjian Luo, Xiexing Feng, Hang Zhang, Wei Liu, Feng Qiao, Yaonan Wang, Huimin Lu, Xieyuanli Chen
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, VLA, Benchmark, mobile-manipulation, skill-evaluation
- Aliases: Behavior-Skill
- Official paper: https://arxiv.org/abs/2608.30536
- Venue verification: https://arxiv.org/abs/2608.30536
- Code/Project: https://github.com/nubot-nudt/Behavior-Skill
- Code: https://github.com/nubot-nudt/Behavior-Skill
- Source audit: 2026-10-28 공식 서지/abstract·저자 project/code 소개 확인. 신규 표준 노트는 abstract 기반이다. 기존 HANDOFF 지정 구간 검토는 별도 source ledger에 있으며 전체 정독·payload·실행 검증을 뜻하지 않는다.

## Problem and Importance

긴 household task의 성공률만으로는 어느 중간 skill이 병목인지 분리하기 어렵다.

## Core Idea and Contribution

시연을 실행 가능한 skill로 나누고 instruction·observation/action segment·복원 가능한 중간 상태·skill 성공 조건을 연결하여 개별 skill 평가를 지원한다.

## Observation–State–Action Interface

Skill instruction와 복원된 시작 상태의 관측 → VLA action → skill 성공 판단 및 trajectory/skill 단위 지표.

## Evaluation Scope and Claim Boundary

50개 household task의 시연으로 구성한 benchmark에서 π0.5와 GR00T 등 정책을 평가한다. 복원된 유효 시작 상태의 개별 능력은 이전 정책이 실제 도달한 상태에서의 연결 실행 성능과 구분한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2608.30536) · [저자 project/code](https://github.com/nubot-nudt/Behavior-Skill). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

현재 HANDOFF P0의 직접적인 benchmark/source prerequisite다. 전체 task 성공률과 독립 skill 능력의 차이를 읽을 NEXT로 추가하되 preprint status를 유지한다.

## Verification Boundary

공개 release와 논문 정책 쌍의 일치, 시연 reset과 continuation의 차이, 학습/평가 instance 분리, normalizer와 controller·queue·종료 정의을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
