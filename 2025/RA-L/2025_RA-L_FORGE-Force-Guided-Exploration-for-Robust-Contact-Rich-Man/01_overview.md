# FORGE: Force-Guided Exploration for Robust Contact-Rich Manipulation Under Uncertainty

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / RA-L
- Authors: Michael Noseworthy, Bingjie Tang, Bowen Wen, Ankur Handa, Chad Kessens, Nicholas Roy, Dieter Fox, Fabio Ramos, Yashraj Narang, Iretiayo Akinola
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: sim-to-real, force-control, reinforcement-learning, assembly
- Aliases: FORGE
- Official paper: https://api.crossref.org/works/10.1109/LRA.2025.3551637
- Venue verification: https://api.crossref.org/works/10.1109/LRA.2025.3551637
- Code/Project: https://noseworm.github.io/forge/
- Code availability: Isaac Lab 2.3에 배포된 FORGE 시뮬레이터 환경·보상 구현(부분). 실기 정책 파일은 미확인. · forge_env.py · ForgeEnv [근거](https://raw.githubusercontent.com/isaac-sim/IsaacLab/v2.3.0/source/isaaclab_tasks/isaaclab_tasks/direct/forge/forge_env.py)
- Code: https://github.com/isaac-sim/IsaacLab
- Source audit: 2026-11-09: official abstract/project 및 metadata 확인. 2024 preprint와 2025 RA-L은 같은 논문이다. Publisher-deposited Crossref DOI metadata와 저자 연구실 RA-L 기록 확인; IEEE 본문 endpoint는 HTTP418로 직접 접근 실패. Code Coming Soon. 새 5-note는 abstract 기반이며 전체 본문/실행/사용자 정독을 뜻하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

FORGE는 조립 물체의 자세가 불확실할 때 허용 접촉력을 조건으로 주어 시뮬레이션 정책을 실물 접촉 조작에 전이한다. [PDF 1쪽](https://arxiv.org/pdf/2408.04587v2#page=1)

## Core Idea and Contribution

- 힘 임계값과 동역학 무작위화를 함께 사용해 정책을 훈련하고, 자체 성공 예측으로 작업 종료와 이후 시행의 임계값 조정을 지원한다. [PDF 3쪽](https://arxiv.org/pdf/2408.04587v2#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2408.04587v2#page=4)
- 실물의 강한 체결력을 요구하는 커넥터 삽입과 세 단계 유성기어 조립에서 제어 이득·힘 한도와 조립 성공의 관계를 평가했다. [PDF 5쪽](https://arxiv.org/pdf/2408.04587v2#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2408.04587v2#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2408.04587v2#page=7)

## Observation–State–Action Interface

관측·허용 force 조건 → 접촉 동작·성공 예측.

## Evaluation Scope and Claim Boundary

삽입·gear meshing·nut threading과 snap-fit/다단계 조립을 보고한다.

근거: [공식 paper/abstract](https://ieeexplore.ieee.org/document/10925874/) · [저자 project/code](https://noseworm.github.io/forge/). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

VLA의 추가 복잡도 전에 넘어야 할 비-VLA 접촉 RL 기준선이다.

## Verification Boundary

pose uncertainty 범위, gain randomization, 독립 실환경 trials을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 · Isaac Lab v2.3.0의 FORGE 조립 환경 · source/isaaclab_tasks/isaaclab_tasks/direct/forge/forge_env.py [배포 파일](https://raw.githubusercontent.com/isaac-sim/IsaacLab/3c6e67bb5c7ada942a6d1884ab69338f57596f77/source/isaaclab_tasks/isaaclab_tasks/direct/forge/forge_env.py)
