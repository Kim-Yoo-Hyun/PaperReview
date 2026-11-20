# Emergent Dexterity Via Diverse Resets and Large-Scale Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Patrick Yin, Tyler Westenbroek, Zhengyu Zhang, Ignacio Dagnino, Eeshani Shilamkar, Numfor Mbiziwo-Tiapo, Simran Bagaria, Xinlei Liu, Galen Mullins, Andrey Kolobov, Abhishek Gupta
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: dexterous-manipulation, reset-distribution, sim-to-real, reinforcement-learning
- Aliases: OmniReset
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/8e3e3488623d64c493a7f11cf1f2e49f-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2026/hash/8e3e3488623d64c493a7f11cf1f2e49f-Abstract-Conference.html
- Code/Project: https://omnireset.github.io/
- Code: project_only
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

접촉 조작 RL이 좁은 상태 영역만 반복하면 계산량을 늘려도 장기 탐색이 정체된다.

## Core Idea and Contribution

다양한 robot-object 상호작용 reset을 프로그램으로 생성하고 공통 보상으로 RL을 학습한 뒤 visuomotor 정책으로 증류한다.

## Observation–State–Action Interface

다양한 simulator reset → RL 정책 → 시각 정책 증류 → 실제 로봇.

## Evaluation Scope and Claim Boundary

장기 dexterous manipulation과 넓은 초기 조건, zero-shot 실로봇 전이를 보고한다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8e3e3488623d64c493a7f11cf1f2e49f-Abstract-Conference.html) · [저자 project/code](https://omnireset.github.io/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

VLA-RL의 탐색 개선이 정책 방법보다 reset coverage에서 오는지 분리할 중요한 대조군이다.

## Verification Boundary

reset 생성의 물리 유효성·특권 정보, 증류 비용, 초기 조건 분할을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
