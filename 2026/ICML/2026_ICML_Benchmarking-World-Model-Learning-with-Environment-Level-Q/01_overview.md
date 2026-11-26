# Benchmarking World-Model Learning with Environment-Level Queries

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2026 / ICML
- Authors: Archana Warrier, Thanh Dat Nguyen, Michelangelo Naim, Moksh Jain, Yichao Liang, Karen Schroeder, Cambridge Yang, Joshua B. Tenenbaum, Sebastian Vollmer, Kevin Ellis, Zenna Tavares
- 저자 판본: 학회 서지에는 Dat Nguyen, Sebastian Josef Vollmer로 실려 있다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/warrier26a/warrier26a.pdf#page=1) · [학회 서지](https://proceedings.mlr.press/v306/warrier26a.html)
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: world model, Benchmark, counterfactual, environment-query
- Aliases: WorldTest, AutumnBench
- Official paper: https://proceedings.mlr.press/v306/warrier26a.html
- Venue verification: https://proceedings.mlr.press/v306/warrier26a.html
- Code/Project: https://zenodo.org/records/19498269
- Code: project_only
- Full-text retrieval: https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/warrier26a/warrier26a.pdf
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다.

## Problem and Importance

WorldTest는 에이전트가 탐색한 환경에 대해 개별 궤적의 예측을 넘어 여러 종류의 환경 수준 질문에 답할 수 있는지 평가한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/warrier26a/warrier26a.pdf#page=1) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/warrier26a/warrier26a.pdf#page=5)

## Core Idea and Contribution

- AutumnBench의 격자 환경 43개에서 가려진 프레임 예측, 변화 탐지, 계획의 세 계열로 129개 문제를 구성했다. [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/warrier26a/warrier26a.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/warrier26a/warrier26a.pdf#page=5)
- 참가자 517명과 기반 모델 다섯 개를 평가해 탐색으로 얻은 정보가 서로 다른 질문의 정답으로 얼마나 이어지는지 비교했다. [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/warrier26a/warrier26a.pdf#page=6) · [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/warrier26a/warrier26a.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/warrier26a/warrier26a.pdf#page=8)

## Observation–State–Action Interface

환경 상호작용 → 학습된 model/belief → 여러 유형의 환경 질의.

## Evaluation Scope and Claim Boundary

AutumnBench grid-world에서 사람과 학습 agent를 비교한다. 실로봇 평가는 아니다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v306/warrier26a.html) · [저자 project/code](https://zenodo.org/records/19498269).

## 검색 태그 근거

WorldTest의 환경 수준 질의를 AutumnBench의 프레임 예측·변화 탐지·계획으로 구체화한다. 사람에게는 격자를 그림으로 보여 주고 추론 모델에는 색 이름 배열로 제공한다. [원문 4쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/warrier26a/warrier26a.pdf#page=4) · [원문 7쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/warrier26a/warrier26a.pdf#page=7)

## Why This Paper Is Here — Researcher Interpretation

VLA world model의 시각 품질·정책 순위와 환경 이해를 구분할 평가 방법론이다.

## Verification Boundary

query 정답 접근, exploration budget, 환경 생성 분할, robot task로의 전이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
