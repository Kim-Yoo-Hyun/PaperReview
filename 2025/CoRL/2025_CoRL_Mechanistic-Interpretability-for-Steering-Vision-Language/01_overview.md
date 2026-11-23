# Mechanistic Interpretability for Steering Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / CoRL
- Authors: Bear Häon, Kaylene Caswell Stocking, Ian Chuang, Claire Tomlin
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, evaluation, generalization
- Aliases:
- Official paper: https://proceedings.mlr.press/v305/haon25a.html
- Venue verification: https://proceedings.mlr.press/v305/haon25a.html
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-25 공식 abstract와 publication metadata 및 명시된 project/code 공개 링크 확인. 본문 정독·코드 실행·payload 검증은 이번 등록 범위 밖이다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 VLA 내부의 활성값에서 속도·방향과 연관된 표현을 찾고 추론 중 이를 조절해 로봇 행동을 바꾼다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/haon25a/haon25a.pdf#page=1)

## Core Idea and Contribution

- 트랜스포머의 피드포워드 활성값을 토큰 임베딩 기저에 투영한 뒤 선택한 방향에 직접 개입해 행동과의 인과관계를 시험한다. [PDF 2쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/haon25a/haon25a.pdf#page=2) · [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/haon25a/haon25a.pdf#page=3)
- π0와 OpenVLA를 대상으로 LIBERO 시뮬레이션과 실제 UR5 조작에서 추가 정책 학습 없는 행동 조절을 평가했다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/haon25a/haon25a.pdf#page=1) · [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/haon25a/haon25a.pdf#page=7)

## Observation–State–Action Interface

VLA 내부 activation·semantic 방향 → 개입된 action.

## Evaluation Scope and Claim Boundary

Pi0·OpenVLA를 LIBERO 및 UR5에서 평가한다고 보고한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/haon25a.html). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

Instruction 대응이나 VLA 행동 교정을 연구할 때 fine-tuning 없는 직접 baseline이다.

## Verification Boundary

방향 추출 데이터, 개입 강도, 속도와 성공의 trade-off을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
