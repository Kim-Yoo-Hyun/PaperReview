# General agents need world models

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2025 / ICML
- Authors: Jonathan Richens, Tom Everitt, David Abel
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: world model, generalization, theory
- Aliases:
- Official paper: https://proceedings.mlr.press/v267/richens25a.html
- Venue verification: https://proceedings.mlr.press/v267/richens25a.html
- Code/Project: not identified
- Code: not_identified
- Full-text retrieval: https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/richens25a/richens25a.pdf
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다.

## Problem and Importance

다단계 목표군에서 일반화하는 에이전트의 정책으로부터 환경의 예측 모형을 얼마나 정확히 복원할 수 있는지 정리로 보였다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/richens25a/richens25a.pdf#page=1) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/richens25a/richens25a.pdf#page=4)

## Core Idea and Contribution

- 달성 가능한 목표의 종류와 정책의 목표 달성 성능에 따라 복원한 전이 모형의 오차를 제한하는 조건을 도출했다. [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/richens25a/richens25a.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/richens25a/richens25a.pdf#page=5)
- 구성한 실험 환경에서 정책 성능과 복원 오차의 관계를 확인하고, 정책이 내부에 명시적 전이 모형을 구현했는지와 외부에서 복원 가능한지를 구별한다. [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/richens25a/richens25a.pdf#page=5) · [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/richens25a/richens25a.pdf#page=6)

## Observation–State–Action Interface

다양한 목표를 수행하는 policy → 추출 가능한 환경 예측 model.

## Evaluation Scope and Claim Boundary

정리 1은 다단계 목표에서 정책의 실패율과 복원 가능한 환경 모형의 오차를 연결한다. [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/richens25a/richens25a.pdf#page=4)

근거: [공식 paper/abstract](https://proceedings.mlr.press/v267/richens25a.html).

## 검색 태그 근거

목표별 정책을 질의해 환경 전이 모형을 복원할 수 있는 조건과 근사 오차를 분석한다. 정책이 제공하는 정보에 관한 보장이며 특정 로봇의 내부 표현이나 명시적 계획기를 관측한 결과는 아니다. [원문 5쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/richens25a/richens25a.pdf#page=5) · [원문 6쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/richens25a/richens25a.pdf#page=6)

## Why This Paper Is Here — Researcher Interpretation

명시적 video model 사용과 정책에 내재한 예측 능력을 구별하는 AI 이론 참조다.

## Verification Boundary

일반화·목표 집합 정의, 추출 접근 권한, 정리 조건과 실제 로봇 적용 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
