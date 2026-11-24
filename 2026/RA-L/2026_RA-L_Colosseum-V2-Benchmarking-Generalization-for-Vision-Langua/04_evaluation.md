# Colosseum V2: Benchmarking Generalization for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 표시한 평가 항목을 확인했다.
> Source audit: 2026-11-24 원문 대조.

## Evaluation in One Sentence

실물 대조는 단팔 ACT의 5개 과제 × 7개 조건에 한정했다. 35개 조합의 절대 성공률에 대한 결정계수는 0.49였고 교란별 성공률을 무교란 대비로 정규화한 뒤 시뮬레이션·실물의 평균 절대 차이는 12.3%p였다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11726868#page=5) · [PDF 7쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11726868#page=7)

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET WITH SIMULATION AND REAL-ROBOT COMPARISON`.

## Dataset / Benchmark Role

전체 시뮬레이션은 28개 과제와 두 로봇 형태를 포함한다. 하드웨어 대조에는 그중 단팔 다섯 과제를 사용했다. [PDF 1쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11726868#page=1) · [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11726868#page=3) · [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11726868#page=5)

## Metrics and Success Definition

절대 성공률과 무교란 성공률을 기준으로 정규화한 상대 강건성을 따로 보고했다. [PDF 7쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11726868#page=7)

## Baselines and Fairness

실물에서는 과제당 시연 60개로 하나의 다중 과제 ACT를 학습했다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11726868#page=5)

## Statistics, Efficiency, and Reproducibility

각 과제·조건 조합에서 시행 20회를 평가했다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11726868#page=5)

## Proposed Evaluation — Researcher Interpretation

같은 task pair에서 morphology와 시각 perturbation을 분리해 비교한다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2605.27759).
