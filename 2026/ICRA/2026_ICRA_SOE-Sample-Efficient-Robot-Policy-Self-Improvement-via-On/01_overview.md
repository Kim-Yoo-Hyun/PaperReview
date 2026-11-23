# SOE: Sample-Efficient Robot Policy Self-Improvement via On-Manifold Exploration

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICRA
- Authors: Yang Jin, Jun Lv, Han Xue, Wendi Chen, Chuan Wen, Cewu Lu
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: robot self-improvement, latent exploration, action manifold, manipulation
- Aliases: SOE
- Official paper: https://arxiv.org/abs/2509.19292
- Venue verification: https://api.crossref.org/works/10.1109/icra57385.2026.11696357
- Code/Project: https://ericjin2002.github.io/SOE/
- Code: https://github.com/EricJin2002/SOE
- Source audit: 2026-11-18: 공식 초록·bibliographic record와 연결된 저자 자료 확인. Abstract 기반 등록이며 본문 전체·실험 재현은 미확인. 저자 repo ICRA2026 표기와 일부 BibTeX IROS2025 문구가 혼재한다. 공식 proceedings identity를 확보하지 못해 arXiv2025 유지. 공식 conference/journal acceptance 확인을 확보하지 못해 preprint 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

SOE는 로봇 정책이 이미 알고 있는 유효 행동의 주변을 낮은 차원의 공간에서 탐색해 기본 정책을 개선할 행동을 수집한다. [PDF 1쪽](https://arxiv.org/pdf/2509.19292v1#page=1)

## Core Idea and Contribution

- 과제에 필요한 변화를 담는 잠재 표현을 학습한 뒤 그 공간에서 행동을 바꾸고, 사람이 탐색 방향을 지정할 수도 있게 한다. [PDF 3쪽](https://arxiv.org/pdf/2509.19292v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2509.19292v1#page=4)
- 시뮬레이션과 실물 과제에서 성공률과 함께 탐색 중 움직임의 저크 및 자료 수집량을 비교해 잠재 공간 탐색과 사람의 안내 효과를 측정했다. [PDF 5쪽](https://arxiv.org/pdf/2509.19292v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2509.19292v1#page=6)

## Observation–State–Action Interface

기본 policy에 추가하는 latent exploration 모듈이며 원 VLA 가중치의 공동 갱신과 구별해야 한다.

## Evaluation Scope and Claim Boundary

저자 project는 robomimic의 4개 simulation task와 mug hanging·toaster loading·lamp capping 실제 과제를 제시한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2509.19292) · [저자 project/code](https://ericjin2002.github.io/SOE/) · [공식 code](https://github.com/EricJin2002/SOE). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

관계 조건 탐색이 일반 latent/on-manifold 탐색보다 필요한지 확인할 직접 baseline이다.

## Verification Boundary

Manifold 학습 데이터·추가 supervision·policy update 방식·안전 주장 조건을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
