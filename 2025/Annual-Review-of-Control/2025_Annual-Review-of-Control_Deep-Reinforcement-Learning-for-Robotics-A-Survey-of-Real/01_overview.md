# Deep Reinforcement Learning for Robotics: A Survey of Real-World Successes

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2025 / Annual Review of Control, Robotics, and Autonomous Systems
- Authors: Chen Tang, Ben Abbatematteo, Jiaheng Hu, Rohan Chandra, Roberto Martín-Martín, Peter Stone
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: reinforcement-learning, Robotics, survey, real-world
- Aliases: Real-world DRL survey
- Official paper: https://api.crossref.org/works/10.1146/annurev-control-030323-022510
- Venue verification: https://www.annualreviews.org/content/journals/10.1146/annurev-control-030323-022510
- Code/Project:
- Code: not_identified
- Full-text retrieval: https://arxiv.org/pdf/2408.03539v3
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다.

## Problem and Importance

실물 로봇에서 심층 강화학습으로 달성한 능력들을 검토하고, 능력별로 물리적 배포를 가능하게 한 학습 조건과 남은 문제를 정리한 서베이다. [PDF 1쪽](https://arxiv.org/pdf/2408.03539v3#page=1) · [PDF 3쪽](https://arxiv.org/pdf/2408.03539v3#page=3)

## Core Idea and Contribution

- 문헌을 로봇의 능력, 문제 정식화, 해결 방법, 실물에서 입증된 성공 수준의 네 축으로 분류해 보행·조작 등에서 증거의 범위를 비교했다. [PDF 3쪽](https://arxiv.org/pdf/2408.03539v3#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2408.03539v3#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2408.03539v3#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2408.03539v3#page=6)
- 실물 상호작용과 충실한 시뮬레이션이 모두 비싼 분야의 사례가 드물다고 지적하고, 표본 효율·학습 안정성 및 장기 과제의 능력 통합을 연구 과제로 제시했다. [PDF 25쪽](https://arxiv.org/pdf/2408.03539v3#page=25) · [PDF 26쪽](https://arxiv.org/pdf/2408.03539v3#page=26) · [PDF 27쪽](https://arxiv.org/pdf/2408.03539v3#page=27)

## Observation–State–Action Interface

과제·정책·실물 수집·평가 프로토콜을 비교하는 survey.

## Evaluation Scope and Claim Boundary

실물 DRL 사례의 종합이며 새 통합 VLA 방법의 성능 실험이 아니다.

근거: [공식 paper/abstract](https://www.annualreviews.org/content/journals/10.1146/annurev-control-030323-022510).

## Why This Paper Is Here — Researcher Interpretation

석사 연구 후보의 구현 부담과 로봇 행동 기여를 평가할 최신 survey로 2013 원전과 함께 사용한다.

## Verification Boundary

본문에서 확인할 항목: 실제 로봇과 simulation 구분·성공 사례 선택 편향·데이터/개입 비용. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
