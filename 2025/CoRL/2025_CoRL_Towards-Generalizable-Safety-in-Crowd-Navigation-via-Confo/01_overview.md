# Towards Generalizable Safety in Crowd Navigation via Conformal Uncertainty Handling

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / CoRL
- Authors: Jianpeng Yao, Xiaopan Zhang, Yu Xia, Zejin Wang, Amit K. Roy-Chowdhury, Jiachen Li
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: Navigation, safe RL, conformal prediction, pedestrian prediction
- Aliases:
- Official paper: https://proceedings.mlr.press/v305/yao25a.html
- Venue verification: https://proceedings.mlr.press/v305/yao25a.html
- Code/Project: https://gen-safe-nav.github.io/
- Code: https://github.com/tasl-lab/GenSafeNav
- Source audit: 2026-10-25 공식 abstract와 publication metadata 및 명시된 project/code 공개 링크 확인. 본문 정독·코드 실행·payload 검증은 이번 등록 범위 밖이다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 보행자 이동 예측의 불확실성을 반영해 낯선 군중에서도 충돌을 줄이는 로봇 내비게이션 정책을 학습한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/yao25a/yao25a.pdf#page=1)

## Core Idea and Contribution

- 적응형 컨포멀 예측으로 보행자 궤적의 예측 구간을 갱신하고 이를 제약 강화학습 정책의 관측에 넣는다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/yao25a/yao25a.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/yao25a/yao25a.pdf#page=4)
- 보행자의 속도·방식·집단 이동을 바꾼 시뮬레이션과 실제 군중 환경에서 충돌 회피와 목표 도달을 평가했다. [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/yao25a/yao25a.pdf#page=6) · [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/yao25a/yao25a.pdf#page=7)

## Observation–State–Action Interface

Pedestrian 예측·uncertainty → navigation policy → 이동 행동.

## Evaluation Scope and Claim Boundary

속도·행동 정책·집단 변화 및 실로봇 군중 navigation을 보고한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/yao25a.html). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

GAP-P 계열에서 uncertainty 추가 자체를 새로운 navigation 기여로 삼지 않게 하는 직접 선행이다.

## Verification Boundary

보장의 단위, reactive crowd, calibration update와 intervention 비용을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 원문 대조

저자 표기와 순서는 이 판본의 표제면을 따른다. [표제면](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/yao25a/yao25a.pdf#page=1)

## 공개 자료

- 코드 — 보행자 예측 오차의 순차 보정 · dt_aci/one_step_dtai.py [배포 파일](https://raw.githubusercontent.com/tasl-lab/GenSafeNav/01baf926a5c77c1a4ab28635658eb014ef4f1767/dt_aci/one_step_dtai.py)
- 가중치 — 저자가 학습한 군중 내비게이션 정책 · trained_models/Ours_GST/checkpoints/05207.pt [배포 파일](https://raw.githubusercontent.com/tasl-lab/GenSafeNav/01baf926a5c77c1a4ab28635658eb014ef4f1767/trained_models/Ours_GST/checkpoints/05207.pt)
