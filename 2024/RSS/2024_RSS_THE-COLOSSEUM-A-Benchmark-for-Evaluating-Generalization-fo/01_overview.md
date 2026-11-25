# THE COLOSSEUM: A Benchmark for Evaluating Generalization for Robotic Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2024 / RSS
- Authors: Wilbert Pumacay, Ishika Singh, Jiafei Duan, Ranjay Krishna, Jesse Thomason, Dieter Fox
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: manipulation, Benchmark, visual perturbation, generalization
- Aliases:
- Official paper: https://roboticsproceedings.org/rss20/p133.html
- Venue verification: https://roboticsproceedings.org/rss20/p133.html
- Code/Project: https://robot-colosseum.github.io/
- Code: https://github.com/robot-colosseum/robot-colosseum
- Source audit: 2026-10-25 공식 abstract와 publication metadata 및 명시된 project/code 공개 링크 확인. 본문 정독·코드 실행·payload 검증은 이번 등록 범위 밖이다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

THE COLOSSEUM은 조작 정책이 물체·카메라·환경의 어떤 변화에서 실패하는지 교란 요인을 하나씩 바꿔 평가한다. [PDF 1쪽](https://roboticsproceedings.org/rss20/p133.pdf#page=1)

## Core Idea and Contribution

- 20개 조작 과제에서 물체의 외형과 물리 속성, 조명과 카메라 등을 바꾸는 14개 변화 요인을 정의했다. [PDF 4쪽](https://roboticsproceedings.org/rss20/p133.pdf#page=4) · [PDF 5쪽](https://roboticsproceedings.org/rss20/p133.pdf#page=5)
- 다섯 정책을 시뮬레이션 교란별로 비교하고, 실물에서 재현한 네 과제에서는 교란에 따른 성공률 변화가 시뮬레이션과 얼마나 일치하는지 측정했다. [PDF 7쪽](https://roboticsproceedings.org/rss20/p133.pdf#page=7) · [PDF 9쪽](https://roboticsproceedings.org/rss20/p133.pdf#page=9)

## Observation–State–Action Interface

Task·환경 변화 → manipulation policy → 조건별 성공.

## Evaluation Scope and Claim Boundary

Simulation 비교와 대응 실세계 perturbation의 관련성을 보고한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss20/p133.html) · [저자 project/code](https://robot-colosseum.github.io/) · [공식 code](https://github.com/robot-colosseum/robot-colosseum). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

LIBERO 계열에 한정하지 않고 manipulation 일반화를 점검할 benchmark 계보다.

## Verification Boundary

복합 요인 상호작용, simulator와 실세계 조건의 대응을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 — 조작 견고성 벤치마크의 방해물 변형 · colosseum/variations/distractor_object.py [배포 파일](https://raw.githubusercontent.com/robot-colosseum/robot-colosseum/098a910ae1d490524adb49b8d50735b00a1a62de/colosseum/variations/distractor_object.py)
- 데이터 — 농구공 과제의 평가 자료 · basketball_in_hoop.tar.gz [배포 파일](https://huggingface.co/datasets/colosseum/colosseum-challenge/blob/b6e8897b0e2a9b74e4dc50174064661918b60236/basketball_in_hoop.tar.gz)
