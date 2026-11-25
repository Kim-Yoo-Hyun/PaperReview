# SAIL: Faster-than-Demonstration Execution of Imitation Learning Policies

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / CoRL
- Authors: Nadun Ranawaka Arachchige, Zhenyang Chen, Wonsuhk Jung, Woo Chul Shin, Rohan Bansal, Pierre Barroso, Yu Hang He, Yingyan Celine Lin, Benjamin Joffe, Shreyas Kousik, Danfei Xu
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: robot-learning, imitation-learning, Control
- Aliases:
- Official paper: https://proceedings.mlr.press/v305/arachchige25a.html
- Venue verification: https://proceedings.mlr.press/v305/arachchige25a.html
- Code/Project: https://nadunranawaka1.github.io/sail-policy
- Code: https://github.com/nadunRanawaka1/SAIL
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

SAIL은 시연보다 빠르게 모방 정책을 실행할 때 로봇 동역학과 상태 분포의 변화 때문에 생기는 추종 오차를 줄인다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/arachchige25a/arachchige25a.pdf#page=1)

## Core Idea and Contribution

- 움직임 복잡도에 따라 속도를 바꾸고 일관성 있는 행동 추론·궤적 추종·지연을 고려한 스케줄링을 결합한다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/arachchige25a/arachchige25a.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/arachchige25a/arachchige25a.pdf#page=4)
- 시뮬레이션과 서로 다른 실물 플랫폼 두 대에서 작업 성공을 유지하며 시연 대비 어느 정도까지 속도를 높일 수 있는지 평가했다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/arachchige25a/arachchige25a.pdf#page=1) · [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/arachchige25a/arachchige25a.pdf#page=7)

## Observation–State–Action Interface

시연 motion target → policy → tracking/speed 제어.

## Evaluation Scope and Claim Boundary

Simulation task와 실제 robot 플랫폼의 빠른 실행을 보고한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/arachchige25a.html) · [저자 project/code](https://nadunranawaka1.github.io/sail-policy). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

E2에서 retiming·tracking·feedback 이득을 분해할 핵심 IL baseline이다.

## Verification Boundary

target/command/torque 주기, motion 재표현, component ablation을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 — 시뮬레이션 시연의 정밀도에 따른 속도 조정 · robomimic/SAIL/precision_processing/dynamic_speed_awe.py [배포 파일](https://raw.githubusercontent.com/nadunRanawaka1/SAIL/1440c16b0017112d7ed5aba2291acd4d638726c2/robomimic/SAIL/precision_processing/dynamic_speed_awe.py)
