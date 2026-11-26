# Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2024 / CoRL
- Authors: Mitsuhiko Nakamoto, Oier Mees, Aviral Kumar, Sergey Levine
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: value-guidance, offline-RL, generalist-policy
- Aliases: V-GPS
- Official paper: https://proceedings.mlr.press/v270/nakamoto25a.html
- Venue verification: https://proceedings.mlr.press/v270/nakamoto25a.html
- Code/Project: https://nakamotoo.github.io/V-GPS
- Code: https://github.com/nakamotoo/V-GPS
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  CoRL 2024 event; PMLR volume 270 published 2025. Registry year uses event year. 본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

V-GPS는 사전학습 로봇 정책이 제안한 행동 중에서 오프라인으로 학습한 가치 함수의 점수가 높은 행동을 골라 실행한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/nakamoto25a/nakamoto25a.pdf#page=1)

## Core Idea and Contribution

- 기본 정책의 가중치에 접근하거나 이를 갱신할 필요 없이, 후보 행동을 표집할 수 있는 서로 다른 정책에 같은 가치 함수를 적용한다. [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/nakamoto25a/nakamoto25a.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/nakamoto25a/nakamoto25a.pdf#page=5)
- 다섯 종류의 기본 정책과 총 열두 과제에서 행동 재선택의 효과를 평가하고 실물과 SIMPLER의 결과를 구분해 보고했다. [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/nakamoto25a/nakamoto25a.pdf#page=6) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/nakamoto25a/nakamoto25a.pdf#page=8)

## Observation–State–Action Interface

고정 정책의 action samples → 학습 value scoring → 실행 행동. 정책 가중치 갱신과 구분한다.

## Evaluation Scope and Claim Boundary

서로 다른 다섯 정책과 여러 실제 로봇·조작 과제에서 value guidance를 평가한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v270/nakamoto25a.html) · [저자 project/code](https://nakamotoo.github.io/V-GPS) · [공식 code](https://github.com/nakamotoo/V-GPS). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

단일 정책을 RL로 갱신하는 방법이 추론 후보 선택보다 필요한 이유를 검증할 직접 대조군이다.

## Verification Boundary

후보 수와 latency, value 데이터 범위, 정책별 action normalization을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 · 가치 함수로 행동 후보를 재채점하는 평가 · experiments/eval_vgps.py [배포 파일](https://raw.githubusercontent.com/nakamotoo/V-GPS/912a290f95a9f5fcf5942fbb5b9e7b4e99905c7b/experiments/eval_vgps.py)
- 가중치 · Bridge·Fractal로 사전학습한 500k 스텝 가치 함수 · checkpoint [배포 파일](https://drive.google.com/file/d/1mHUhVlFPUj1_AhxgxrFGHF1QxujgSPru/view)
