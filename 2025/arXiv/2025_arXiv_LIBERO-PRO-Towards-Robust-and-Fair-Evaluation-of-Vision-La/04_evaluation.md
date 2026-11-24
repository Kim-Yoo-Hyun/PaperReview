# LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 표시한 평가 항목을 확인했다.
> Source audit: 2026-11-24 원문 대조.

## Evaluation in One Sentence

그림 6은 교란을 다섯 종류로 나누며 작업 목표를 바꾸는 교란은 조합에서 제외한다. 그림 7의 성공률은 모델·교란·과제군별로 달라서 초록의 0.0%를 전체 평균으로 인용할 수 없다. [PDF 6쪽](https://arxiv.org/pdf/2510.03827v2#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2510.03827v2#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2510.03827v2#page=8)

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / SIMULATION`.

## Dataset / Benchmark Role

물체 속성, 배치, 지시, 과제, 시각 환경을 바꾼 후 LIBERO 과제군별 결과를 비교했다. [PDF 6쪽](https://arxiv.org/pdf/2510.03827v2#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2510.03827v2#page=7)

## Baselines and Fairness

OpenVLA는 과제군별 공식 체크포인트 네 개, π0와 π0.5는 모델별 단일 공식 체크포인트를 사용했다. [PDF 8쪽](https://arxiv.org/pdf/2510.03827v2#page=8)

## Statistics, Efficiency, and Reproducibility

과제당 에피소드 50개로 평가했다. [PDF 8쪽](https://arxiv.org/pdf/2510.03827v2#page=8)

## Proposed Evaluation — Researcher Interpretation

Goal/planner/evaluator를 먼저 맞춘 뒤 원본과 변형 task 성공을 비교한다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2510.03827) · [저자 project/code](https://github.com/Zxy-MLlab/LIBERO-PRO).
