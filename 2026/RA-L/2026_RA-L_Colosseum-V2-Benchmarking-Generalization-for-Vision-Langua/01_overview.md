# Colosseum V2: Benchmarking Generalization for Vision-Language-Action Models

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2026 / RA-L
- Authors: Jeremy Morgan, Hyeonho Oh, Prajwal Vijay, Jincen Song, Ashvin Arora, Hojung Lim, Alina Du, Jesse Thomason, Gaurav S. Sukhatme, Ishika Singh
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Benchmark, generalization
- Aliases:
- Official paper: https://arxiv.org/abs/2605.27759
- Venue verification: https://api.crossref.org/works/10.1109/lra.2026.3741771
- Code/Project: not identified
- Code: not_identified
- Full-text retrieval: https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11726868
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다. 평가 조건은 04_evaluation.md에 쪽수와 함께 기록했다.

## Problem and Importance

Colosseum V2는 단팔·양팔 형태와 여러 교란 조건에서 조작 정책의 일반화를 비교하는 ManiSkill 시뮬레이션 벤치마크다. [PDF 1쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11726868#page=1) · [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11726868#page=3)

## Core Idea and Contribution

- 13개 과제 범주의 28개 과제를 구성하고 ACT와 π0.5 등을 평가할 수 있도록 과제와 교란을 표준화했다. [PDF 1쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11726868#page=1) · [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11726868#page=3) · [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11726868#page=5)
- 단팔 과제 다섯 개는 실물에서도 재현해 ACT의 과제·교란 35개 조합에서 시뮬레이션과 실물 성공률의 관계를 비교했다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11726868#page=5) · [PDF 7쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11726868#page=7)

## Observation–State–Action Interface

Task·robot morphology·분포 변화 → ACT/π0.5 등 policy → task 성능.

## Evaluation Scope and Claim Boundary

실물 대조는 단팔 ACT의 5개 과제 × 7개 조건에 한정했다. 35개 조합의 절대 성공률에 대한 결정계수는 0.49였고 교란별 성공률을 무교란 대비로 정규화한 뒤 시뮬레이션·실물의 평균 절대 차이는 12.3%p였다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11726868#page=5) · [PDF 7쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11726868#page=7)

근거: [공식 paper/abstract](https://arxiv.org/abs/2605.27759).

## Why This Paper Is Here — Researcher Interpretation

THE COLOSSEUM의 후속 평가 자산이며 다양한 로봇을 다루는 사용자 연구축과 직접 연결된다.

## Verification Boundary

morphology별 action/control 정렬, task split과 simulator-real 대응을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
