# Mobi-π: Mobilizing Your Robot Learning Policy

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / CoRL
- Authors: Jingyun Yang, Isabella Huang, Brandon Vu, Max Bajracharya, Rika Antonova, Jeannette Bohg
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: Robotics, mobile-manipulation, policy-mobilization, 3d-gaussian-splatting, base-placement
- Aliases: Mobi-pi, Mobi-π
- Official paper: https://proceedings.mlr.press/v305/yang25b.html
- Venue verification: https://proceedings.mlr.press/v305/yang25b.html
- Code/Project: https://mobipi.github.io/
- Code: https://github.com/yjy0625/mobipi
- Source audit: 2026-10-28 공식 서지/abstract·저자 project/code 소개 확인. 신규 표준 노트는 abstract 기반이다. 기존 HANDOFF 지정 구간 검토는 별도 source ledger에 있으며 전체 정독·payload·실행 검증을 뜻하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

Mobi-π는 기존 조작 정책이 학습 때와 유사한 장면을 보게 할 이동 베이스의 위치를 선택해 고정형 로봇 정책을 이동 조작에 활용한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/yang25b/yang25b.pdf#page=1)

## Core Idea and Contribution

- 3D 가우시안 스플래팅으로 후보 위치에서의 관측을 합성하고 정책이 익숙한 시점을 점수화해 베이스 자세를 탐색한다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/yang25b/yang25b.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/yang25b/yang25b.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/yang25b/yang25b.pdf#page=5)
- RoboCasa 기반 과제와 실제 로봇에서 위치 선정 전략에 따른 후속 조작 성공을 비교했다. [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/yang25b/yang25b.pdf#page=6) · [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/yang25b/yang25b.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/yang25b/yang25b.pdf#page=8)

## Observation–State–Action Interface

현재 장면과 사전 학습 조작 정책의 데이터 → 장면 표현·후보 pose 점수 → 조작을 시작할 base pose → 기존 정책 실행.

## Evaluation Scope and Claim Boundary

RoboCasa 기반 simulated mobile manipulation과 실로봇에서 pose 선택을 비교한다. 이 비교만으로 다른 정책에 선택된 pose를 재사용할 때의 성능을 확정할 수 없다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/yang25b.html) · [저자 project/code](https://mobipi.github.io/) · [공식 code](https://github.com/yjy0625/mobipi). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

Mobile ALOHA의 whole-body 데이터와 MoTo의 이동–조작 연결을 보완하며, HANDOFF의 정책별 도착 조건을 비교할 직접 선행이다.

## Verification Boundary

pose 후보와 collision/reachability 처리, 정책별 학습 시야와 데이터 접근, 장면 구축 비용, 실제 도착 상태·평가 분모을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
