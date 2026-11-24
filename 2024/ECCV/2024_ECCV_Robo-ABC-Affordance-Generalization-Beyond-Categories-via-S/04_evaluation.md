# Robo-ABC: Affordance Generalization Beyond Categories via Semantic Correspondence for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 표시한 평가 항목을 확인했다.
> Source audit: 2026-11-24 원문 대조.

## Evaluation in One Sentence

실물 파지 성공률 85.7%와 VRB 기준선의 68.6%는 일곱 물체 범주에서 얻은 값이다. 이미지에 대한 접촉점 예측 정확도는 별도 평가다. [PDF 11쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05748.pdf#page=11) · [PDF 12쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05748.pdf#page=12)

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET AND REAL-ROBOT COMPARISON`.

## Dataset / Benchmark Role

영상에서 접촉점을 평가하고, 범주를 넘는 전이를 실물 파지로도 검사했다. [PDF 10쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05748.pdf#page=10) · [PDF 11쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05748.pdf#page=11)

## Metrics and Success Definition

AnyGrasp가 생성한 파지 후보 중 예측 접촉점에 가장 가까운 후보를 실행해 실물 성공률을 측정했다. [PDF 11쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05748.pdf#page=11) · [PDF 12쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05748.pdf#page=12)

## Baselines and Fairness

실물 비교 대상은 VRB다. [PDF 11쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05748.pdf#page=11) · [PDF 12쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05748.pdf#page=12)

## Proposed Evaluation — Researcher Interpretation

동일 object에서 retrieval 정확도와 실제 reachable grasp 성공을 분리 측정한다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5748_ECCV_2024_paper.php) · [저자 project/code](https://tea-lab.github.io/Robo-ABC/) · [공식 code](https://github.com/TEA-Lab/Robo-ABC).
