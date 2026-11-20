# FORGE: Force-Guided Exploration for Robust Contact-Rich Manipulation Under Uncertainty

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Michael Noseworthy, Bingjie Tang, Bowen Wen, Ankur Handa, Chad Kessens, Nicholas Roy, Dieter Fox, Fabio Ramos, Yashraj Narang, Iretiayo Akinola
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: sim-to-real, force-control, reinforcement-learning, assembly
- Aliases: FORGE
- Official paper: https://api.crossref.org/works/10.1109/LRA.2025.3551637
- Venue verification: https://api.crossref.org/works/10.1109/LRA.2025.3551637
- Code/Project: https://noseworm.github.io/forge/
- Code: https://github.com/isaac-sim/IsaacLab/tree/v2.3.0/source/isaaclab_tasks/isaaclab_tasks/direct/forge
- Source audit: 2026-11-09: official abstract/project 및 metadata 확인. 2024 preprint와 2025 RA-L은 같은 논문이다. Publisher-deposited Crossref DOI metadata와 저자 연구실 RA-L 기록 확인; IEEE 본문 endpoint는 HTTP418로 직접 접근 실패. Code Coming Soon. 새 5-note는 abstract 기반이며 전체 본문/실행/사용자 정독을 뜻하지 않는다.

## Problem and Importance

물체 pose·동역학 불확실성 아래 힘을 제한하면서 조립해야 한다.

## Core Idea and Contribution

Force threshold와 dynamics randomization으로 sim-to-real 접촉 정책을 학습하고 성공을 예측한다.

## Observation–State–Action Interface

관측·허용 force 조건 → 접촉 동작·성공 예측.

## Evaluation Scope and Claim Boundary

삽입·gear meshing·nut threading과 snap-fit/다단계 조립을 보고한다.

근거: [공식 paper/abstract](https://ieeexplore.ieee.org/document/10925874/) · [저자 project/code](https://noseworm.github.io/forge/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

VLA의 추가 복잡도 전에 넘어야 할 비-VLA 접촉 RL 기준선이다.

## Verification Boundary

pose uncertainty 범위, gain randomization, 독립 실환경 trials을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
