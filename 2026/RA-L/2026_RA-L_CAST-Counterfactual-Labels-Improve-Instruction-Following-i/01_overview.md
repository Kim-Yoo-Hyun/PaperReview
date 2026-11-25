# CAST: Counterfactual Labels Improve Instruction Following in Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RA-L
- Authors: Catherine Glossop, William Chen, Arjun Bhorkar, Dhruv Shah, Sergey Levine
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, counterfactual-data, instruction-following, Navigation, manipulation
- Aliases: CAST, Counterfactual Augmentation with Synthetic Trajectories
- Official paper: https://arxiv.org/abs/2508.13446
- Venue verification: https://api.crossref.org/works/10.1109/lra.2026.3726383
- Code/Project: https://cast-vla.github.io/
- Code: https://github.com/catglossop/CAST
- Source audit: 2026-11-07: 공식 metadata/abstract·저자 project/README 확인. 최초 preprint2025, 최신 v2는2026-06-08. 공식 project/저자 code 확인; 이번 확인으로 main-conference 채택을 확정하지 않는다. 사용자 reading status UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

CAST는 같은 장면에서도 지시에 따라 다른 행동이 필요하다는 점을 학습시키기 위해 기존 로봇 자료에 반사실 지시와 대응 행동을 추가한다. [PDF 1쪽](https://arxiv.org/pdf/2508.13446v2#page=1)

## Core Idea and Contribution

- 로봇의 결정 지점에서 시각언어 모델에 다른 지시를 요청하고 그 지시에 맞는 행동 구간을 생성해 훈련 예시를 늘린다. [PDF 3쪽](https://arxiv.org/pdf/2508.13446v2#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2508.13446v2#page=4)
- 새 시연을 수집하지 않고 실내외 내비게이션의 세 환경에서 지시 이행을 비교하고 방해 물체가 있는 조작 과제로 전이되는지도 평가했다. [PDF 5쪽](https://arxiv.org/pdf/2508.13446v2#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2508.13446v2#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2508.13446v2#page=7)

## Observation–State–Action Interface

기존 trajectory와 counterfactual instruction/action 자료 → VLA 학습 → navigation 또는 manipulation 행동. 실제 수행된 실패의 hindsight 라벨과 합성 counterfactual을 구분한다.

## Evaluation Scope and Claim Boundary

v2 abstract는 실내외 3개 navigation 환경과 distractor가 있는 manipulation의 instruction following을 평가한다고 보고한다. 정확한 trial·split·수치는 본문 확인 필요다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2508.13446) · [저자 project/code](https://cast-vla.github.io/) · [공식 code](https://github.com/catglossop/CAST). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

목표 의미를 바꾸는 학습 자료의 직접 대조. 사실인 실패 라벨 선택과 실행되지 않은 counterfactual augmentation의 차이를 명확히 하는 데 필요하다.

## Verification Boundary

합성 행동의 물리적 유효성, 원 데이터/평가 중복, language와 action 증강 기여 분리, 공개 모델/자료의 논문 version 대응을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 — 반사실 지시 자료 생성 · cast/data/utils/counterfactual.py [배포 파일](https://raw.githubusercontent.com/catglossop/CAST/ec7a214e76167e0f844800ea91d6664863a3d9b1/cast/data/utils/counterfactual.py)
- 가중치·학습 파라미터 — CAST 내비게이션 정책의 파라미터 조각 · cast_checkpoint/0/default/ocdbt.process_0/d/1092e3334d3bc1c52edf6451f6d5e2c1 [배포 파일](https://huggingface.co/catglossop/CounterfactualVLA/resolve/6da195e2dece9732266e5b144d8e5dd0ac50f6fe/cast_checkpoint/0/default/ocdbt.process_0/d/1092e3334d3bc1c52edf6451f6d5e2c1)
- 데이터 — 반사실 내비게이션 지시와 행동 자료 · cast_counterfactual_dataset.tar.gz [배포 파일](https://huggingface.co/datasets/catglossop/CAST-dataset/resolve/fe9de38e1e519e649a40db20c9558f94e52887a0/cast_counterfactual_dataset.tar.gz)
