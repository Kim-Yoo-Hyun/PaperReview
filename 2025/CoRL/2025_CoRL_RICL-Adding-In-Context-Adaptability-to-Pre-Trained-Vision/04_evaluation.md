# RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. 아래에 인용한 원문 절·표의 평가 조건을 대조했다.
> Source audit: 2026-11-25 원문 방법·평가 대조.

## 평가 조건

RICL은 현재 세 카메라 영상·지시·로봇 상태에 검색한 시연의 관측과 행동 묶음을 붙인다. 검색 시연을 활용하는 능력은 먼저 지도학습한다. [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/sridhar25a/sridhar25a.pdf#page=4)

Franka DROID에서 훈련 시연 집합과 새 과제용 시연 집합의 역할이 다르다. 새 과제에서는 문맥만 주는 경우와 가중치도 미세조정하는 경우를 비교한다. [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/sridhar25a/sridhar25a.pdf#page=5)

기본 VLA의 기술 범위를 크게 벗어나는 과제는 소수의 문맥 시연만으로 배우기 어렵다고 저자가 적었다. [PDF 9쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/sridhar25a/sridhar25a.pdf#page=9)

## Paper-Specific Verification Questions

시연 구간·action interpolation·target-task split·검색 query와 inference 예산.

제안 실험과 실제 보고 결과는 [insights](./05_insights.md)에서 구분한다.
