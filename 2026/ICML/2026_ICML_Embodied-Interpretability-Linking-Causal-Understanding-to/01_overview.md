# Embodied Interpretability: Linking Causal Understanding to Generalization in Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. 요약·기여와 아래에 인용한 방법·평가를 원문에서 대조했다.

- Year/Venue: 2026 / ICML
- Authors: Hanxin Zhang, Mingshuo Xu, Abdulqader Dhafer, Shigang Yue, Hongbiao Dong, Zhou Daniel Hao
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, causal-attribution, generalization, visual-grounding
- Official paper: https://proceedings.mlr.press/v306/zhang26gz.html
- Venue verification: https://proceedings.mlr.press/v306/zhang26gz.html
- Code/Project: https://github.com/robot-future/vla-explain
- Code: https://github.com/robot-future/vla-explain
- Source audit: 2026-11-25 게재본에서 아래에 인용한 요약·기여와 평가 조건을 대조했다. [평가 노트](./04_evaluation.md)

## Problem and Contribution

분포 변화 아래 실패가 task-irrelevant 시각 단서 의존과 어떤 관계인지 측정한다.

Interventional masking 기반 ISS와 nuisance attribution 비중 NMR을 제안한다.

## Scope and Limitation

Abstract 기반 — 본문 확인 필요. Action error가 causal influence proxy가 되는 조건과 실제 return의 관계를 동일시할 수 없다.

## Why This Paper Is Here — Researcher Interpretation

FEEDBACK에서 attribution 자체를 새 기여로 주장하지 않도록 하는 직접 진단 baseline.

입력·행동은 [method](./03_method.md), 실제 평가 범위는 [evaluation](./04_evaluation.md)을 따른다. 자동 노트는 사용자의 읽기 완료 기록이 아니다.

근거: [확인한 원문](https://proceedings.mlr.press/v306/zhang26gz.html), 공식 proceedings abstract; software landing.

## 공개 자료

- 코드 — 시각 영역에 대한 개입 점수 ISS 계산 · iss_nmr_toolkit/core/iss.py [배포 파일](https://raw.githubusercontent.com/robot-future/vla-explain/202d2a9a00fb4b99083559525d54d8f2a7eb4d3f/iss_nmr_toolkit/core/iss.py)

## 원문 대조

시각 영역을 가렸을 때의 행동 예측 오차로 영역별 영향을 추정해, 과제와 무관한 시각 단서 의존성이 일반화와 어떻게 연결되는지 평가한다. [게재본](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/zhang26gz/zhang26gz.pdf#page=6)

- ISS는 반복 마스킹으로 시각 영역 기여를 추정하고 NMR은 무관한 영역에 집중된 비율을 측정한다. [원문](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/zhang26gz/zhang26gz.pdf#page=5)
- AGNOSTOS의 기존 에피소드에서 π0.5의 진단 지표를 시각 교란 종류와 성공·실패 조건별로 비교한다. [원문](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/zhang26gz/zhang26gz.pdf#page=6)
