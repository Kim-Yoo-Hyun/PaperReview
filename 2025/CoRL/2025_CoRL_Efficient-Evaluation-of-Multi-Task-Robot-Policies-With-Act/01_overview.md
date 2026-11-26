# Efficient Evaluation of Multi-Task Robot Policies With Active Experiment Selection

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2025 / CoRL
- Authors: Abrar Anwar, Rohan Gupta, Zain Merchant, Sayan Ghosh, Willie Neiswanger, Jesse Thomason
- Category: Benchmarks and Datasets
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: robot-evaluation, Benchmark, policy-comparison, VLA
- Aliases: Active Experiment Selection
- Official paper: https://proceedings.mlr.press/v305/anwar25a.html
- Venue verification: https://proceedings.mlr.press/v305/anwar25a.html
- Code/Project: not identified
- Code: not_identified
- Full-text retrieval: https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/anwar25a/anwar25a.pdf
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다.

## Problem and Importance

여러 로봇 정책과 과제를 평가할 때 각 조합의 성능 분포를 추정하고 다음 시행이 줄여 줄 불확실성과 시행 비용을 함께 고려한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/anwar25a/anwar25a.pdf#page=1) · [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/anwar25a/anwar25a.pdf#page=3)

## Core Idea and Contribution

- 과제의 자연어 설명을 과제 간 유사성의 사전정보로 사용하고, 비용을 반영한 기대 정보 이득으로 다음 시험을 고른다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/anwar25a/anwar25a.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/anwar25a/anwar25a.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/anwar25a/anwar25a.pdf#page=5)
- 기존 실물·시뮬레이션 정책 평가 자료에서 동일 예산에 따른 평균 성능 추정 오차와 예측 분포의 적합도를 비교했다. [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/anwar25a/anwar25a.pdf#page=6) · [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/anwar25a/anwar25a.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/anwar25a/anwar25a.pdf#page=8)

## Observation–State–Action Interface

Policy·task·prior·관측 결과 → 다음 평가 선택.

## Evaluation Scope and Claim Boundary

실제 및 simulated 평가 자료를 이용한 효율 비교를 보고한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/anwar25a.html).

## 검색 태그 근거

과제 설명의 임베딩과 실험 비용을 이용해 다음 정책·과제 평가를 선택한다. 실물 근거는 HAMSTER·OpenVLA가 이미 수집한 평가 결과를 이용한 재분석이고, 시뮬레이션에서는 Meta-World 자료를 사용했다. [원문 4쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/anwar25a/anwar25a.pdf#page=4) · [원문 5쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/anwar25a/anwar25a.pdf#page=5)

## Why This Paper Is Here — Researcher Interpretation

C6의 task-aware cost-aware 평가 배분에 대한 직접 REFERENCE다.

## Verification Boundary

prior 언어 정보, 관측 noise, offline matrix와 실제 online 실행 차이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
